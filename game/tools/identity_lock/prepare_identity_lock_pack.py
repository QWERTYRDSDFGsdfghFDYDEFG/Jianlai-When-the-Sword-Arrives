from __future__ import annotations

import json
import shutil
from dataclasses import dataclass
from pathlib import Path


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}


@dataclass(frozen=True)
class CharacterConfig:
    slug: str
    display_name: str
    source_dir: str
    token: str
    summary: str
    docs: list[str]
    anchors: list[str]
    outfit_bases: list[str]
    scene_refs: list[str]
    negatives: list[str]


CHARACTERS: list[CharacterConfig] = [
    CharacterConfig(
        slug="cpa",
        display_name="陈平安",
        source_dir="cpa",
        token="cpa_person",
        summary=(
            "male, age 20-22, slim long face, stable eyebrow-eye-nose-mouth proportions, "
            "calm, reliable, restrained, not idol-like"
        ),
        docs=[
            "lh/cpa/CPA_FACE_IDENTITY_STANDARD.md",
            "陈平安出图标准包.md",
            "陈平安出图10条铁律.md",
            "陈平安轻环境出图规则.md",
        ],
        anchors=[
            "cpa_face_standard_01.png",
            "cpa_face_locked_identity_sheet_01.png",
        ],
        outfit_bases=["cpa_outfit_variant_06_warm_weather.png"],
        scene_refs=[],
        negatives=[
            "wider jaw",
            "bigger eyes",
            "boyish look",
            "older face",
            "idol male lead styling",
        ],
    ),
    CharacterConfig(
        slug="cds",
        display_name="崔东山",
        source_dir="cuidongshan",
        token="cds_person",
        summary=(
            "male, age 18-21, narrow slightly long face, slightly narrow long eyes, "
            "small brow mark, restrained scholar temperament, not template handsome"
        ),
        docs=[
            "lh/cuidongshan/cds_face_ref.md",
            "lh/cuidongshan/cds_face_test.md",
        ],
        anchors=[
            "cuidongshan_face_locked_identity_sheet_02.png",
            "cds_face_test_01_plain_v1.png",
        ],
        outfit_bases=["cds_t00_base_v1.png"],
        scene_refs=[
            "cds_face_test_04_courtyard_night_v1.png",
            "cds_face_test_05_lakeside_night_v1.png",
            "cds_t01_court_v1.png",
            "cds_t02_lake_v1.png",
        ],
        negatives=[
            "wider face",
            "rounder jaw",
            "bigger eyes",
            "idol handsome face",
            "generic ancient-costume male lead",
        ],
    ),
    CharacterConfig(
        slug="lbp",
        display_name="李宝瓶",
        source_dir="lbp",
        token="lbp_person",
        summary=(
            "female child, age 12, straight bangs, high double buns, small bell ornaments, "
            "precise ribbon shape, delicate face, short winter outer jacket with fur collar"
        ),
        docs=[
            "lh/lbp/李宝瓶固定脸部身份与当前服装标准.md",
        ],
        anchors=["lbp.png"],
        outfit_bases=[],
        scene_refs=[],
        negatives=[
            "too young toddler look",
            "older teenager look",
            "long robe silhouette",
            "missing bells",
            "wrong ribbon shape",
        ],
    ),
    CharacterConfig(
        slug="pq",
        display_name="裴钱",
        source_dir="peiqian",
        token="pq_person",
        summary=(
            "female child, stable face identity from master image, same person across poses and scenes"
        ),
        docs=[
            "lh/peiqian/PEIQIAN_FACE_IDENTITY_STANDARD.md",
        ],
        anchors=["peiqian_master_v02.png"],
        outfit_bases=[],
        scene_refs=[],
        negatives=[
            "identity drift",
            "older face",
            "idolized styling",
        ],
    ),
]


def role_for(filename: str, config: CharacterConfig) -> str:
    if filename in config.anchors:
        return "anchor"
    if filename in config.outfit_bases:
        return "outfit_base"
    if filename in config.scene_refs:
        return "scene_ref"
    lower = filename.lower()
    if "face_test" in lower:
        return "face_stress_test"
    if "locked_identity" in lower or "master" in lower:
        return "anchor"
    if "outfit" in lower or "base" in lower:
        return "outfit_base"
    return "reference"


def caption_for(config: CharacterConfig, role: str) -> str:
    base = f"{config.token}, {config.display_name}, {config.summary}"
    if role == "anchor":
        return (
            f"{base}, identity anchor reference, same face in every scene, same person, "
            "preserve exact facial structure and age feeling"
        )
    if role == "outfit_base":
        return (
            f"{base}, outfit base reference, preserve the same face and clothing structure, "
            "stable visual novel character design"
        )
    if role == "scene_ref":
        return (
            f"{base}, same character in another scene, preserve exact face identity under different "
            "lighting and composition"
        )
    if role == "face_stress_test":
        return (
            f"{base}, cross-scene stability test image, preserve exact facial proportions and identity "
            "under angle or lighting changes"
        )
    return (
        f"{base}, reference image, preserve exact face identity and age feeling, "
        "do not redesign the character"
    )


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_readme(output_root: Path, manifest: dict) -> None:
    lines = [
        "# Identity Lock Pack",
        "",
        "This pack is generated from `lh/` and is intended for two related workflows:",
        "",
        "- training a separate low-rank identity adapter for each character",
        "- using the same curated anchors and prompts for non-training reference generation",
        "",
        "Reality check for this machine:",
        "",
        "- `py` is available, but `torch`, `diffusers`, `transformers`, `accelerate`, and `safetensors` are not installed yet.",
        "- GPU detected: NVIDIA RTX 3050 Laptop GPU with 4GB VRAM.",
        "- With 4GB VRAM, do not train one mixed multi-character LoRA for all faces at once.",
        "- The practical route is one character LoRA at a time, then single-character generation first, and scene compositing second.",
        "",
        "Why this exists:",
        "",
        "- The current drift problem comes from re-generating both characters together in scene shots.",
        "- A stable character pipeline needs fixed anchors, fixed captions, fixed negatives, and per-character inference prompts.",
        "- This pack gives one consistent source of truth for that workflow.",
        "",
        "Recommended training strategy:",
        "",
        "1. Train one LoRA per character, not one LoRA for all `lh/` characters together.",
        "2. Start with `cpa`, `lbp`, and `cds` as separate identities.",
        "3. Use the generated `manifest.json` and `characters/*.json` as the dataset contract.",
        "4. Keep inference prompts strict: generate a single character master first, then assemble multi-character scenes.",
        "",
        "Suggested starting hyperparameters for a low-VRAM LoRA experiment:",
        "",
        "- base model: SD 1.5 anime-friendly checkpoint that already matches your project style",
        "- resolution: 512 or 640 square-ish crops for training",
        "- batch size: 1",
        "- network rank (`dim`): 8 to 16",
        "- network alpha: same as rank",
        "- learning rate: `1e-4` for UNet, `5e-5` for text encoder if enabled",
        "- repeats: 8 to 12 for anchors, 4 to 6 for scene variants",
        "- total steps target: roughly 1200 to 2200 per character, checking samples every 100 to 200 steps",
        "",
        "What this pack does not guarantee:",
        "",
        "- no model can honestly guarantee zero drift in every new scene",
        "- stronger consistency still depends on scene workflow discipline and post-compositing",
        "",
        "Generated characters:",
        "",
    ]
    for character in manifest["characters"]:
        lines.append(f"- `{character['slug']}` / {character['display_name']}: {character['image_count']} images")
    lines.extend(
        [
            "",
            "Key files:",
            "",
            "- `manifest.json`: full pack index",
            "- `characters/*.json`: per-character identity contract",
            "- `data/<slug>/`: copied training-ready source images plus sibling caption `.txt` files",
            "- `sample_prompts.md`: strict inference prompt templates",
            "",
        ]
    )
    write_text(output_root / "README.md", "\n".join(lines) + "\n")


def build_sample_prompts(output_root: Path, manifest: dict) -> None:
    lines = [
        "# Sample Prompts",
        "",
        "Use these as inference baselines after training or as strict reference prompts before training.",
        "",
    ]
    for character in manifest["characters"]:
        negatives = ", ".join(character["negatives"])
        lines.extend(
            [
                f"## {character['display_name']} (`{character['slug']}`)",
                "",
                "Positive:",
                "",
                (
                    f"`{character['token']}, {character['display_name']}, {character['summary']}, "
                    "strict identity lock, same face as anchor images, Song-dynasty fantasy visual novel, "
                    "restrained expression, real age feeling, real clothing structure`"
                ),
                "",
                "Negative:",
                "",
                f"`{negatives}`",
                "",
            ]
        )
    lines.extend(
        [
            "## Multi-character scene rule",
            "",
            "Do not rely on one fresh prompt to invent two stable faces at once.",
            "",
            "Recommended route:",
            "",
            "1. Generate or select each character from their own locked identity workflow.",
            "2. Keep scene generation responsible for space, action, and lighting.",
            "3. Treat the characters as hard anchors during compositing or scene redraws.",
            "",
        ]
    )
    write_text(output_root / "sample_prompts.md", "\n".join(lines) + "\n")


def build_pack() -> None:
    script_path = Path(__file__).resolve()
    workspace_root = script_path.parents[2]
    lh_root = workspace_root / "lh"
    output_root = workspace_root / "training" / "identity_lock"
    data_root = output_root / "data"
    characters_root = output_root / "characters"

    manifest: dict[str, object] = {
        "source_root": str(lh_root),
        "output_root": str(output_root),
        "characters": [],
    }

    for config in CHARACTERS:
        source_dir = lh_root / config.source_dir
        if not source_dir.exists():
            continue

        image_paths = sorted(
            [
                path
                for path in source_dir.iterdir()
                if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
            ]
        )

        copied_images: list[dict[str, str]] = []
        char_output_dir = data_root / config.slug
        char_output_dir.mkdir(parents=True, exist_ok=True)

        for image_path in image_paths:
            role = role_for(image_path.name, config)
            destination = char_output_dir / image_path.name
            shutil.copy2(image_path, destination)
            caption = caption_for(config, role)
            write_text(destination.with_suffix(".txt"), caption)
            copied_images.append(
                {
                    "file": str(destination.relative_to(output_root)).replace("\\", "/"),
                    "source": str(image_path.relative_to(workspace_root)).replace("\\", "/"),
                    "role": role,
                    "caption": caption,
                }
            )

        character_payload = {
            "slug": config.slug,
            "display_name": config.display_name,
            "token": config.token,
            "summary": config.summary,
            "docs": config.docs,
            "anchors": config.anchors,
            "outfit_bases": config.outfit_bases,
            "scene_refs": config.scene_refs,
            "negatives": config.negatives,
            "image_count": len(copied_images),
            "images": copied_images,
        }
        manifest["characters"].append(character_payload)
        write_text(
            characters_root / f"{config.slug}.json",
            json.dumps(character_payload, ensure_ascii=False, indent=2) + "\n",
        )

    write_text(output_root / "manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    build_readme(output_root, manifest)
    build_sample_prompts(output_root, manifest)


if __name__ == "__main__":
    build_pack()
