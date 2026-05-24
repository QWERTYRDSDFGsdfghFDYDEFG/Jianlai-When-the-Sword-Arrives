param(
  [string]$GameDir = (Get-Location).Path,
  [string]$ScriptPath = "script.rpy",
  [string]$IndexPath = "audio_index.rpy",
  [switch]$DryRun
)

$ErrorActionPreference = "Stop"

function Slugify([string]$text) {
  $t = $text.Trim().ToLowerInvariant()
  $t = $t -replace "[^a-z0-9_\\s-]", ""
  $t = $t -replace "[\\s-]+", "_"
  $t = $t -replace "_{2,}", "_"
  $t = $t.Trim("_")
  if ([string]::IsNullOrWhiteSpace($t)) { $t = "scene" }
  return $t
}

function Ensure-Dir([string]$path) {
  if (-not (Test-Path -LiteralPath $path)) {
    if ($DryRun) { Write-Output "[DryRun] mkdir $path" }
    else { New-Item -ItemType Directory -Force -Path $path | Out-Null }
  }
}

$scriptFull = Join-Path $GameDir $ScriptPath
if (-not (Test-Path -LiteralPath $scriptFull)) { throw "script not found: $scriptFull" }

$indexFull = Join-Path $GameDir $IndexPath
if (-not (Test-Path -LiteralPath $indexFull)) { throw "index not found: $indexFull" }

$audioDir = Join-Path $GameDir "audio"
$voiceRoot = Join-Path $audioDir "voice"

# Avoid non-ASCII literals in this file for Windows PowerShell compatibility.
$CN_LI_BAO_PING = ([char]0x674E)+([char]0x5B9D)+([char]0x74F6)
$CN_CUI_DONG_SHAN = ([char]0x5D14)+([char]0x4E1C)+([char]0x5C71)
$CN_LI_HUAI = ([char]0x674E)+([char]0x69D0)
$CN_ZHU_LIAN = ([char]0x6731)+([char]0x655B)
$CN_SHI_ROU = ([char]0x77F3)+([char]0x67D4)
$CN_PANG_BAI = ([char]0x65C1)+([char]0x767D)
$CN_PEI_QIAN = ([char]0x88F4)+([char]0x94B1)
$CN_CHEN_PING_AN = ([char]0x9648)+([char]0x5E73)+([char]0x5B89)
$CN_MAO_XIAO_DONG = ([char]0x8305)+([char]0x5C0F)+([char]0x51AC)

$roleMap = @{}
$roleMap[$CN_LI_BAO_PING] = "lbp"
$roleMap[$CN_CUI_DONG_SHAN] = "cds"
$roleMap[$CN_LI_HUAI] = "lh"
$roleMap[$CN_ZHU_LIAN] = "zl"
$roleMap[$CN_SHI_ROU] = "sr"
$roleMap[$CN_PANG_BAI] = "narr"
$roleMap[$CN_PEI_QIAN] = "pq"
$roleMap[$CN_CHEN_PING_AN] = "cpy"
$roleMap[$CN_MAO_XIAO_DONG] = "mxd"

$lines = Get-Content -LiteralPath $scriptFull

# scene slug -> scn_0001_xxx
$sceneIdBySlug = @{}
$sceneOrder = New-Object System.Collections.Generic.List[string]

function Get-SceneId([string]$slug) {
  if ($sceneIdBySlug.ContainsKey($slug)) { return $sceneIdBySlug[$slug] }
  $n = $sceneOrder.Count + 1
  $sceneNum = $n.ToString("0000")
  $sceneId = "scn_${sceneNum}_${slug}"
  $sceneIdBySlug[$slug] = $sceneId
  $sceneOrder.Add($slug) | Out-Null
  return $sceneId
}

# Extract existing index mappings
$indexText = Get-Content -LiteralPath $indexFull -Raw
$existingIndex = @{}
foreach ($m in [regex]::Matches($indexText, '"(?<id>voice\.[^"]+)"\s*:\s*"(?<path>audio/[^"]+)"')) {
  $existingIndex[$m.Groups["id"].Value] = $m.Groups["path"].Value
}

$newIndex = @{}
$newIndex += $existingIndex

$currentSceneSlug = "unknown"
$seqBySceneRole = @{} # key: "$sceneId|$role" -> int

for ($i=0; $i -lt $lines.Count; $i++) {
  $line = $lines[$i]

  $sceneMatch = [regex]::Match($line, '^\s*scene\s+bg\s+(?<name>.+?)\s*$')
  if ($sceneMatch.Success) {
    $bgName = $sceneMatch.Groups["name"].Value
    $currentSceneSlug = Slugify $bgName
    continue
  }

  # If already-migrated, register its scene order so new scenes continue numbering.
  $alreadyMatch = [regex]::Match($line, '^\s*voice\s+voice_id\("(?<id>voice\.(?<scene>scn_\d{4}_[^.]+)\.[^.]+\.\d{4})"\)\s*$')
  if ($alreadyMatch.Success) {
    $sceneId = $alreadyMatch.Groups["scene"].Value
    $slug = $sceneId -replace '^scn_\d{4}_', ''
    if (-not $sceneIdBySlug.ContainsKey($slug)) {
      $sceneIdBySlug[$slug] = $sceneId
      $sceneOrder.Add($slug) | Out-Null
    }
    continue
  }

  $voiceMatch = [regex]::Match($line, '^\s*voice\s+"(?<path>audio/[^"]+)"\s*$')
  if (-not $voiceMatch.Success) { continue }

  $relPath = $voiceMatch.Groups["path"].Value
  $fileName = [System.IO.Path]::GetFileName($relPath)
  $baseName = [System.IO.Path]::GetFileNameWithoutExtension($fileName)
  $namePrefix = ($baseName -replace "\d+$", "")

  if (-not $roleMap.ContainsKey($namePrefix)) {
    throw "Unknown role prefix '$namePrefix' for file '$relPath' at line $($i+1). Add to roleMap."
  }

  $role = $roleMap[$namePrefix]
  $sceneId = Get-SceneId $currentSceneSlug
  $seqKey = "$sceneId|$role"
  if (-not $seqBySceneRole.ContainsKey($seqKey)) { $seqBySceneRole[$seqKey] = 0 }
  $seqBySceneRole[$seqKey]++
  $seq = $seqBySceneRole[$seqKey].ToString("0000")

  $voiceId = "voice.$sceneId.$role.$seq"
  $destRel = "audio/voice/$sceneId/$role/$seq.mp3"
  $destFull = Join-Path $GameDir ($destRel -replace "/", "\\")
  $srcFull = Join-Path $GameDir ($relPath -replace "/", "\\")

  $destDir = Split-Path -Parent $destFull
  Ensure-Dir $destDir

  if (-not (Test-Path -LiteralPath $srcFull)) {
    throw "Source audio not found: $srcFull (from $relPath at line $($i+1))"
  }

  if ($DryRun) { Write-Output "[DryRun] move $relPath -> $destRel" }
  else { Move-Item -LiteralPath $srcFull -Destination $destFull }

  $newIndex[$voiceId] = $destRel
  $indent = ([regex]::Match($line, '^\s*')).Value
  $lines[$i] = "${indent}voice voice_id(`"$voiceId`")"
}

# Write updated script.rpy
if ($DryRun) { Write-Output "[DryRun] write $ScriptPath" }
else { Set-Content -LiteralPath $scriptFull -Value $lines -Encoding UTF8 }

# Rewrite VOICE_INDEX block in audio_index.rpy (keep other code intact)
function Build-IndexBlock([hashtable]$index) {
  $keys = $index.Keys | Sort-Object
  $out = New-Object System.Collections.Generic.List[string]
  $out.Add("    VOICE_INDEX = {") | Out-Null
  foreach ($k in $keys) {
    $p = $index[$k]
    $out.Add("        `"$k`": `"$p`",") | Out-Null
  }
  $out.Add("    }") | Out-Null
  return ($out -join "`r`n")
}

$newBlock = Build-IndexBlock $newIndex
$updatedIndexText = [regex]::Replace(
  $indexText,
  '(?s)^\s*VOICE_INDEX\s*=\s*\{.*?^\s*\}\s*$',
  ($newBlock -replace "\$", '$$'),
  [System.Text.RegularExpressions.RegexOptions]::Multiline
)

if ($DryRun) { Write-Output "[DryRun] update $IndexPath" }
else { Set-Content -LiteralPath $indexFull -Value $updatedIndexText -Encoding UTF8 }

Write-Output "Migrated voice lines. Scenes: $($sceneOrder.Count). Index entries: $($newIndex.Count)."
