param(
    [string]$VenvPath = "training/identity_lock/.venv",
    [string]$SdScriptsDir = "third_party/sd-scripts"
)

$ErrorActionPreference = "Stop"

$workspace = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$venvFullPath = Join-Path $workspace $VenvPath
$sdScriptsFullPath = Join-Path $workspace $SdScriptsDir

if (-not (Test-Path $venvFullPath)) {
    py -3.12 -m venv $venvFullPath
}

$venvPython = Join-Path $venvFullPath "Scripts\python.exe"

& $venvPython -m pip install --upgrade pip setuptools wheel
& $venvPython -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
& $venvPython -m pip install accelerate diffusers transformers safetensors peft datasets pillow toml

if (-not (Test-Path $sdScriptsFullPath)) {
    git clone https://github.com/kohya-ss/sd-scripts.git $sdScriptsFullPath
}

& $venvPython -m pip install -r (Join-Path $sdScriptsFullPath "requirements.txt")

Write-Host ""
Write-Host "LoRA environment ready."
Write-Host "Venv: $venvFullPath"
Write-Host "sd-scripts: $sdScriptsFullPath"
