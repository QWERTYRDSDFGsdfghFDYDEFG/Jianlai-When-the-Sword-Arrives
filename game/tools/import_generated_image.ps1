param(
  [string]$GameDir = (Get-Location).Path,
  [Parameter(Mandatory = $true)]
  [string]$ImageName,
  [int]$Chapter = 0,
  [string]$SourcePath,
  [string]$GeneratedDir = "$env:USERPROFILE\.codex\generated_images",
  [switch]$Overwrite
)

$ErrorActionPreference = "Stop"

function Resolve-NormalizedPath([string]$PathValue) {
  return [System.IO.Path]::GetFullPath($PathValue)
}

function Test-ValidImageName([string]$NameValue) {
  return $NameValue -match '^[a-z0-9]+(?:_[a-z0-9]+)*$'
}

function Get-LatestGeneratedImage([string]$RootDir) {
  if (-not (Test-Path -LiteralPath $RootDir)) {
    throw "Generated image directory not found: $RootDir"
  }

  $latest = Get-ChildItem -LiteralPath $RootDir -Recurse -File |
    Where-Object { $_.Extension.ToLowerInvariant() -in @(".png", ".jpg", ".jpeg", ".webp") } |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1

  if ($null -eq $latest) {
    throw "No generated image found under: $RootDir"
  }

  return $latest.FullName
}

function Get-RelativePath([string]$BaseDir, [string]$FullPath) {
  $base = Resolve-Path -LiteralPath $BaseDir
  $full = Resolve-Path -LiteralPath $FullPath

  $basePath = $base.Path
  if (-not $basePath.EndsWith("\")) {
    $basePath = $basePath + "\"
  }

  $baseUri = New-Object System.Uri($basePath)
  $fullUri = New-Object System.Uri($full.Path)
  $relative = $baseUri.MakeRelativeUri($fullUri).ToString()
  return [System.Uri]::UnescapeDataString($relative) -replace "/", "\"
}

if (-not (Test-ValidImageName $ImageName)) {
  throw "ImageName must use lowercase letters, digits, and underscores only."
}

$gameRoot = Resolve-NormalizedPath $GameDir
$imagesRoot = Join-Path $gameRoot "images"

if (-not (Test-Path -LiteralPath $imagesRoot)) {
  throw "images directory not found under game dir: $imagesRoot"
}

if ([string]::IsNullOrWhiteSpace($SourcePath)) {
  $sourceFullPath = Get-LatestGeneratedImage $GeneratedDir
} else {
  if (-not (Test-Path -LiteralPath $SourcePath)) {
    throw "Source image not found: $SourcePath"
  }
  $sourceFullPath = Resolve-NormalizedPath $SourcePath
}

$sourceItem = Get-Item -LiteralPath $sourceFullPath
$ext = $sourceItem.Extension.ToLowerInvariant()
if ($ext -notin @(".png", ".jpg", ".jpeg", ".webp")) {
  throw "Unsupported image extension: $ext"
}

if ($Chapter -gt 0) {
  $targetDir = Join-Path $imagesRoot ("chapter" + $Chapter)
} elseif ($ImageName -match '^c(?<chapter>\d+)_') {
  $targetDir = Join-Path $imagesRoot ("chapter" + [int]$Matches["chapter"])
} else {
  $targetDir = $imagesRoot
}

New-Item -ItemType Directory -Force -Path $targetDir | Out-Null

$targetFileName = $ImageName + $ext
$targetPath = Join-Path $targetDir $targetFileName

if ((Test-Path -LiteralPath $targetPath) -and (-not $Overwrite)) {
  throw "Target file already exists: $targetPath`nUse -Overwrite to replace it."
}

Copy-Item -LiteralPath $sourceFullPath -Destination $targetPath -Force

$relativeTarget = Get-RelativePath $gameRoot $targetPath
$bgName = $ImageName
$renpyPath = $relativeTarget -replace "\\", "/"

Write-Output "Imported image:"
Write-Output $targetPath
Write-Output ""
Write-Output "Recommended Ren'Py lines:"
Write-Output "image bg $bgName = im.Scale(`"$renpyPath`", 1920, 1080)"
Write-Output "scene bg $bgName"
