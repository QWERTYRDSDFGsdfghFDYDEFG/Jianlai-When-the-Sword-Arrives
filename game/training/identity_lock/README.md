# Identity Lock Pack

This pack is generated from `lh/` and is intended for two related workflows:

- training a separate low-rank identity adapter for each character
- using the same curated anchors and prompts for non-training reference generation

Reality check for this machine:

- `py` is available, but `torch`, `diffusers`, `transformers`, `accelerate`, and `safetensors` are not installed yet.
- GPU detected: NVIDIA RTX 3050 Laptop GPU with 4GB VRAM.
- With 4GB VRAM, do not train one mixed multi-character LoRA for all faces at once.
- The practical route is one character LoRA at a time, then single-character generation first, and scene compositing second.

Why this exists:

- The current drift problem comes from re-generating both characters together in scene shots.
- A stable character pipeline needs fixed anchors, fixed captions, fixed negatives, and per-character inference prompts.
- This pack gives one consistent source of truth for that workflow.

Recommended training strategy:

1. Train one LoRA per character, not one LoRA for all `lh/` characters together.
2. Start with `cpa`, `lbp`, and `cds` as separate identities.
3. Use the generated `manifest.json` and `characters/*.json` as the dataset contract.
4. Keep inference prompts strict: generate a single character master first, then assemble multi-character scenes.

Suggested starting hyperparameters for a low-VRAM LoRA experiment:

- base model: SD 1.5 anime-friendly checkpoint that already matches your project style
- resolution: 512 or 640 square-ish crops for training
- batch size: 1
- network rank (`dim`): 8 to 16
- network alpha: same as rank
- learning rate: `1e-4` for UNet, `5e-5` for text encoder if enabled
- repeats: 8 to 12 for anchors, 4 to 6 for scene variants
- total steps target: roughly 1200 to 2200 per character, checking samples every 100 to 200 steps

What this pack does not guarantee:

- no model can honestly guarantee zero drift in every new scene
- stronger consistency still depends on scene workflow discipline and post-compositing

Generated characters:

- `cpa` / 陈平安: 3 images
- `cds` / 崔东山: 16 images
- `lbp` / 李宝瓶: 9 images
- `pq` / 裴钱: 1 images

Key files:

- `manifest.json`: full pack index
- `characters/*.json`: per-character identity contract
- `data/<slug>/`: copied training-ready source images plus sibling caption `.txt` files
- `sample_prompts.md`: strict inference prompt templates
- `profiles/lbp.json` and `profiles/cds.json`: per-character LoRA training profiles
- `tools/identity_lock/setup_lora_env.ps1`: environment bootstrap for Windows
- `tools/identity_lock/train_character_lora.py`: launcher for per-character LoRA runs

Bootstrap and launch:

1. Run `powershell -ExecutionPolicy Bypass -File tools/identity_lock/setup_lora_env.ps1`
2. Locate a local SD1.5-compatible base model file path
3. Dry run one character:
   `training/identity_lock/.venv/Scripts/python.exe tools/identity_lock/train_character_lora.py --character lbp --base-model "X:\path\to\model.safetensors" --dry-run`
4. Start training when the command looks correct:
   `training/identity_lock/.venv/Scripts/python.exe tools/identity_lock/train_character_lora.py --character lbp --base-model "X:\path\to\model.safetensors"`
5. Repeat for `cds`

