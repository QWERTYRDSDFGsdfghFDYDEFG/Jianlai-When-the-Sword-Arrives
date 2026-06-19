from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Launch a per-character LoRA training run for identity lock.")
    parser.add_argument("--character", required=True, choices=["lbp", "cds"], help="Character profile slug.")
    parser.add_argument("--base-model", required=True, help="Path to local SD1.5 checkpoint or safetensors file.")
    parser.add_argument(
        "--workspace",
        default=None,
        help="Workspace root. Defaults to repo root inferred from this script location.",
    )
    parser.add_argument(
        "--sd-scripts-dir",
        default="third_party/sd-scripts",
        help="Relative path from workspace root to the sd-scripts checkout.",
    )
    parser.add_argument(
        "--venv-python",
        default="training/identity_lock/.venv/Scripts/python.exe",
        help="Relative path from workspace root to the venv python executable.",
    )
    parser.add_argument("--max-train-steps", type=int, default=None, help="Override max training steps.")
    parser.add_argument("--learning-rate", type=float, default=None, help="Override base learning rate.")
    parser.add_argument("--unet-lr", type=float, default=None, help="Override UNet learning rate.")
    parser.add_argument(
        "--text-encoder-lr",
        type=float,
        default=None,
        help="Override text encoder learning rate. Set to 0 to disable text encoder training.",
    )
    parser.add_argument("--network-dim", type=int, default=None, help="Override LoRA rank.")
    parser.add_argument("--network-alpha", type=int, default=None, help="Override LoRA alpha.")
    parser.add_argument("--resolution", default=None, help="Override training resolution, e.g. 512,512.")
    parser.add_argument("--output-suffix", default=None, help="Optional suffix appended to output name.")
    parser.add_argument("--dry-run", action="store_true", help="Print generated command without running training.")
    parser.add_argument("--sample-prompt-only", action="store_true", help="Print the sample prompt and exit.")
    return parser.parse_args()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_dataset_toml(path: Path, image_dir: Path, repeats: int, resolution: str) -> None:
    width, height = [int(part.strip()) for part in resolution.split(",", 1)]
    content = f"""[general]
enable_bucket = true
caption_extension = ".txt"

[[datasets]]
resolution = [{width}, {height}]
batch_size = 1
keep_tokens = 1

  [[datasets.subsets]]
  image_dir = "{image_dir.as_posix()}"
  num_repeats = {repeats}
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> int:
    args = parse_args()

    script_path = Path(__file__).resolve()
    workspace = Path(args.workspace).resolve() if args.workspace else script_path.parents[2]
    profile_path = workspace / "training" / "identity_lock" / "profiles" / f"{args.character}.json"
    profile = load_json(profile_path)

    base_model = Path(args.base_model).expanduser()
    if not base_model.exists():
        raise FileNotFoundError(f"Base model not found: {base_model}")

    venv_python = (workspace / args.venv_python).resolve()
    if not venv_python.exists():
        raise FileNotFoundError(f"Venv python not found: {venv_python}")

    sd_scripts_dir = (workspace / args.sd_scripts_dir).resolve()
    train_script = sd_scripts_dir / "train_network.py"
    if not train_script.exists():
        raise FileNotFoundError(f"sd-scripts train script not found: {train_script}")

    if args.sample_prompt_only:
        print(profile["sample_prompt"])
        print("")
        print("Negative:")
        print(profile["negative_prompt"])
        return 0

    data_dir = (workspace / profile["data_dir"]).resolve()
    output_dir = (workspace / profile["output_dir"]).resolve()
    generated_dir = (workspace / "training" / "identity_lock" / "generated_configs").resolve()
    generated_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    dataset_toml = generated_dir / f"{args.character}_dataset.toml"
    resolution = args.resolution or profile["resolution"]
    write_dataset_toml(dataset_toml, data_dir, int(profile["num_repeats"]), resolution)

    max_steps = args.max_train_steps or int(profile["max_train_steps"])
    learning_rate = args.learning_rate or float(profile["learning_rate"])
    unet_lr = args.unet_lr or float(profile["unet_lr"])
    text_encoder_lr = (
        args.text_encoder_lr if args.text_encoder_lr is not None else float(profile["text_encoder_lr"])
    )
    network_dim = args.network_dim or int(profile["network_dim"])
    network_alpha = args.network_alpha or int(profile["network_alpha"])
    output_name = profile["output_name"]
    if args.output_suffix:
        output_name = f"{output_name}_{args.output_suffix}"

    command = [
        str(venv_python),
        str(train_script),
        "--pretrained_model_name_or_path",
        str(base_model),
        "--dataset_config",
        str(dataset_toml),
        "--output_dir",
        str(output_dir),
        "--output_name",
        output_name,
        "--save_model_as",
        "safetensors",
        "--prior_loss_weight",
        "1.0",
        "--max_train_steps",
        str(max_steps),
        "--learning_rate",
        str(learning_rate),
        "--unet_lr",
        str(unet_lr),
        "--network_module",
        "networks.lora",
        "--network_dim",
        str(network_dim),
        "--network_alpha",
        str(network_alpha),
        "--resolution",
        resolution,
        "--train_batch_size",
        "1",
        "--gradient_accumulation_steps",
        str(profile["gradient_accumulation_steps"]),
        "--mixed_precision",
        "fp16",
        "--save_precision",
        "fp16",
        "--optimizer_type",
        profile["optimizer_type"],
        "--lr_scheduler",
        profile["lr_scheduler"],
        "--lr_scheduler_num_cycles",
        str(profile["lr_scheduler_num_cycles"]),
        "--cache_latents",
        "--gradient_checkpointing",
        "--max_data_loader_n_workers",
        "0",
        "--bucket_reso_steps",
        "32",
        "--min_bucket_reso",
        "256",
        "--max_bucket_reso",
        "768",
        "--seed",
        str(profile["seed"]),
        "--caption_dropout_rate",
        "0.0",
        "--caption_tag_dropout_rate",
        "0.0",
        "--keep_tokens",
        "1",
    ]

    if text_encoder_lr > 0:
        command.extend(["--text_encoder_lr", str(text_encoder_lr)])
    else:
        command.append("--network_train_unet_only")

    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"

    print("Sample prompt:")
    print(profile["sample_prompt"])
    print("")
    print("Negative prompt:")
    print(profile["negative_prompt"])
    print("")
    print("Command:")
    print(" ".join(f'"{part}"' if " " in part else part for part in command))

    if args.dry_run:
        return 0

    return subprocess.run(command, cwd=sd_scripts_dir, env=env, check=False).returncode


if __name__ == "__main__":
    sys.exit(main())
