param(
  [string]$GameDir = (Get-Location).Path,
  [switch]$WriteCatalog
)

$ErrorActionPreference = "Stop"

function Normalize-RelPath([string]$baseDir, [string]$fullPath) {
  $base = (Resolve-Path -LiteralPath $baseDir).Path
  $full = (Resolve-Path -LiteralPath $fullPath).Path

  if (-not $base.EndsWith("\")) { $base = $base + "\" }
  $baseUri = New-Object System.Uri($base)
  $fullUri = New-Object System.Uri($full)

  $rel = $baseUri.MakeRelativeUri($fullUri).ToString()
  $rel = [System.Uri]::UnescapeDataString($rel)
  return $rel -replace "\\\\", "/"
}

$audioDir = Join-Path $GameDir "audio"
if (-not (Test-Path -LiteralPath $audioDir)) {
  throw "audio dir not found: $audioDir"
}

$rpyFiles = Get-ChildItem -LiteralPath $GameDir -Recurse -File -Filter *.rpy |
  Where-Object { $_.FullName -notmatch "\\\\cache\\\\" }

$audioFiles = Get-ChildItem -LiteralPath $audioDir -Recurse -File |
  Where-Object { $_.Extension -in @(".mp3", ".ogg", ".wav", ".flac", ".m4a") }

$audioRelSet = New-Object "System.Collections.Generic.HashSet[string]"
foreach ($f in $audioFiles) {
  [void]$audioRelSet.Add((Normalize-RelPath $GameDir $f.FullName))
}

# 收集脚本里引用到的音频路径（目前主要是 voice "audio/..."
$refRelSet = New-Object "System.Collections.Generic.HashSet[string]"
$refHits = @()
$refVoiceIds = New-Object "System.Collections.Generic.HashSet[string]"

$patterns = @(
  # voice "audio/xxx.ext"
  '(?m)^\s*voice\s+"(?<path>audio/[^"]+)"',
  # play music/sound "audio/xxx.ext"
  '(?m)^\s*play\s+(music|sound)\s+"(?<path>audio/[^"]+)"'
)

$voiceIdPattern = '(?m)^\s*voice\s+voice_id\("(?<id>[^"]+)"\)'
$voiceIdInterpPattern = '(?m)^\s*voice\s+"\[voice_id\(''(?<id>[^'']+)''\)\]"'

foreach ($file in $rpyFiles) {
  $text = Get-Content -LiteralPath $file.FullName -Raw
  foreach ($pat in $patterns) {
    foreach ($m in [regex]::Matches($text, $pat)) {
      $p = $m.Groups["path"].Value
      if ([string]::IsNullOrWhiteSpace($p)) { continue }
      $p = $p.Trim()
      [void]$refRelSet.Add($p)
      $refHits += [pscustomobject]@{
        File = (Normalize-RelPath $GameDir $file.FullName)
        Path = $p
      }
    }
  }

  foreach ($m in [regex]::Matches($text, $voiceIdPattern)) {
    $id = $m.Groups["id"].Value
    if ([string]::IsNullOrWhiteSpace($id)) { continue }
    [void]$refVoiceIds.Add($id.Trim())
    $refHits += [pscustomobject]@{
      File = (Normalize-RelPath $GameDir $file.FullName)
      Path = ("voice_id:" + $id.Trim())
    }
  }

  foreach ($m in [regex]::Matches($text, $voiceIdInterpPattern)) {
    $id = $m.Groups["id"].Value
    if ([string]::IsNullOrWhiteSpace($id)) { continue }
    [void]$refVoiceIds.Add($id.Trim())
    $refHits += [pscustomobject]@{
      File = (Normalize-RelPath $GameDir $file.FullName)
      Path = ("voice_id:" + $id.Trim())
    }
  }
}

# If audio_index.rpy exists, resolve used voice IDs -> actual file paths so they participate in missing/unreferenced checks.
$voiceIndexPath = Join-Path $GameDir "audio_index.rpy"
if ((Test-Path -LiteralPath $voiceIndexPath) -and ($refVoiceIds.Count -gt 0)) {
  $indexText = Get-Content -LiteralPath $voiceIndexPath -Raw

  # Extract "id": "audio/..."
  $indexPairs = @{}
  foreach ($m in [regex]::Matches($indexText, '"(?<id>voice\.[^"]+)"\s*:\s*"(?<path>audio/[^"]+)"')) {
    $id = $m.Groups["id"].Value
    $p = $m.Groups["path"].Value
    if (-not [string]::IsNullOrWhiteSpace($id) -and -not [string]::IsNullOrWhiteSpace($p)) {
      $indexPairs[$id] = $p
    }
  }

  foreach ($id in $refVoiceIds) {
    if ($indexPairs.ContainsKey($id)) {
      [void]$refRelSet.Add($indexPairs[$id])
    }
  }
}

$missingRefs = @()
foreach ($p in $refRelSet) {
  if (-not $audioRelSet.Contains($p)) {
    $missingRefs += $p
  }
}

$unreferenced = @()
foreach ($p in $audioRelSet) {
  if (-not $refRelSet.Contains($p)) {
    $unreferenced += $p
  }
}

Write-Output "Audio files: $($audioRelSet.Count)"
Write-Output "Referenced paths in .rpy: $($refRelSet.Count)"
Write-Output ""

if ($missingRefs.Count -gt 0) {
  Write-Output "=== Missing referenced files (script -> file not found) ==="
  $missingRefs | Sort-Object | ForEach-Object { Write-Output $_ }
  Write-Output ""
} else {
  Write-Output "No missing referenced files."
  Write-Output ""
}

if ($unreferenced.Count -gt 0) {
  Write-Output "=== Unreferenced audio files (file -> not used in scripts) ==="
  $unreferenced | Sort-Object | ForEach-Object { Write-Output $_ }
  Write-Output ""
} else {
  Write-Output "No unreferenced audio files."
  Write-Output ""
}

# 简单按“文件名去掉末尾数字”统计（适配你当前的：旁白10.mp3 / 陈平安7.mp3 …）
$voiceStats = @{}
foreach ($f in $audioFiles) {
  if ($f.DirectoryName -ne $audioDir) { continue }
  $name = [System.IO.Path]::GetFileNameWithoutExtension($f.Name)
  $key = ($name -replace "\d+$", "")
  if (-not $voiceStats.ContainsKey($key)) { $voiceStats[$key] = 0 }
  $voiceStats[$key]++
}

if ($voiceStats.Keys.Count -gt 0) {
  Write-Output "=== Top-level voice file counts (by name prefix) ==="
  $voiceStats.GetEnumerator() |
    Sort-Object -Property Value -Descending |
    ForEach-Object { "{0,-10} {1,4}" -f $_.Key, $_.Value } |
    ForEach-Object { Write-Output $_ }
  Write-Output ""
}

if ($WriteCatalog) {
  $outDir = Join-Path $audioDir "_audit"
  New-Item -ItemType Directory -Force -Path $outDir | Out-Null

  $catalogPath = Join-Path $outDir "catalog.csv"
  $audioFiles |
    Sort-Object FullName |
    ForEach-Object {
      [pscustomobject]@{
        RelPath = (Normalize-RelPath $GameDir $_.FullName)
        Bytes = $_.Length
        LastWriteTime = $_.LastWriteTime.ToString("s")
      }
    } |
    Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath $catalogPath

  $refsPath = Join-Path $outDir "references.csv"
  $refHits |
    Sort-Object File, Path |
    Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath $refsPath

  Write-Output "Wrote: $(Normalize-RelPath $GameDir $catalogPath)"
  Write-Output "Wrote: $(Normalize-RelPath $GameDir $refsPath)"
}

if ($missingRefs.Count -gt 0) { exit 2 }
