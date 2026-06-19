param(
    [string[]]$Roots = @(
        "C:\Users\fld16\Desktop",
        "C:\Users\fld16\Documents",
        "C:\Users\fld16\Downloads",
        "D:\",
        "E:\"
    ),
    [int]$MaxResults = 50
)

$ErrorActionPreference = "SilentlyContinue"

$patterns = @(
    "sd15",
    "sd1.5",
    "stable-diffusion-v1-5",
    "v1-5-pruned",
    "anything",
    "counterfeit",
    "meinamix",
    "majicmix",
    "revanimated",
    "dreamshaper",
    "deliberate",
    "pastelmix"
)

$results = foreach ($root in $Roots) {
    if (-not (Test-Path $root)) {
        continue
    }

    Get-ChildItem -Path $root -Recurse -File -Include *.safetensors,*.ckpt |
        Where-Object {
            $name = $_.Name.ToLower()
            $_.Length -gt 500MB -and (
                ($patterns | Where-Object { $name -like "*$_*" }).Count -gt 0
            )
        } |
        Select-Object FullName, Length, LastWriteTime
}

$results |
    Sort-Object Length -Descending |
    Select-Object -First $MaxResults |
    Format-Table -AutoSize
