param([switch]$Execute)
$ErrorActionPreference = 'Stop'
$root = [IO.Path]::GetFullPath('F:\project\JianlaiWhentheSwordArrives')
$prefix = $root + [IO.Path]::DirectorySeparatorChar
$audit = Join-Path $root 'work\project_cleanup'
$manifestPath = Join-Path $audit 'manifest.json'
$manifestHash = (Get-FileHash -LiteralPath $manifestPath -Algorithm SHA256).Hash.ToLowerInvariant()
if ($manifestHash -ne '34b4d6622855a08d7661a084af5f06346d8922feee95e9c8e5c0fd12f57805d6') { throw 'Approved manifest changed.' }
$manifest = Get-Content -LiteralPath $manifestPath -Raw -Encoding UTF8 | ConvertFrom-Json
if ($manifest.files.Count -ne 1032 -or $manifest.totalBytes -ne 39814794) { throw 'Approved totals changed.' }
if ([IO.Path]::GetFullPath($manifest.scope) -ne $root) { throw 'Scope changed.' }
$resultPath = Join-Path $audit 'result.json'
if ((Test-Path -LiteralPath $resultPath) -or (Test-Path -LiteralPath (Join-Path $audit 'execution.jsonl'))) { throw 'Existing execution record; inspect before any retry.' }

function Scoped-Path([string]$Path) {
    $full = [IO.Path]::GetFullPath($Path)
    if (-not $full.StartsWith($prefix, [StringComparison]::OrdinalIgnoreCase)) { throw "Outside project: $full" }
    $cursor = $full
    while ($cursor) {
        if (Test-Path -LiteralPath $cursor) {
            $item = Get-Item -LiteralPath $cursor -Force
            if (($item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) { throw "Reparse point: $cursor" }
        }
        $cursor = [IO.Path]::GetDirectoryName($cursor)
    }
    return $full
}
function Check-File($Entry, [switch]$Time) {
    $path = Scoped-Path $Entry.path
    if ($path -ne [IO.Path]::GetFullPath((Join-Path $root $Entry.relative))) { throw "Relative path mismatch: $path" }
    $item = Get-Item -LiteralPath $path -Force
    if ($item.PSIsContainer -or $item.Length -ne $Entry.bytes) { throw "File type/size changed: $path" }
    if ($Time) {
        [long]$ns = ($item.LastWriteTimeUtc.ToFileTimeUtc() - 116444736000000000L) * 100L
        if ($ns -ne $Entry.mtimeNs) { throw "Modification time changed: $path" }
    }
    if ((Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash -ne $Entry.sha256) { throw "Content changed: $path" }
}
$selected = [Collections.Generic.HashSet[string]]::new([StringComparer]::OrdinalIgnoreCase)
$directories = [Collections.Generic.HashSet[string]]::new([StringComparer]::OrdinalIgnoreCase)
foreach ($entry in $manifest.files) {
    Check-File $entry -Time
    $path = [IO.Path]::GetFullPath($entry.path)
    if (-not $selected.Add($path)) { throw "Duplicate candidate: $path" }
    $parent = [IO.Path]::GetDirectoryName($path)
    while ($parent -and $parent.StartsWith($prefix, [StringComparison]::OrdinalIgnoreCase)) {
        [void]$directories.Add($parent)
        $parent = [IO.Path]::GetDirectoryName($parent)
    }
}
foreach ($entry in $manifest.protectedFiles) {
    if ($selected.Contains([IO.Path]::GetFullPath($entry.path))) { throw "Protected file selected: $($entry.relative)" }
    Check-File $entry
}
Write-Output "Preflight passed: $($selected.Count) approved files, $($manifest.protectedFiles.Count) protected files."
if (-not $Execute) { return }

$started = [DateTimeOffset]::Now.ToString('o')
$writer = [IO.StreamWriter]::new((Join-Path $audit 'execution.jsonl'), $false, [Text.UTF8Encoding]::new($false))
$writer.AutoFlush = $true
$deleted = 0
[long]$bytes = 0
$empty = 0
$failure = $null
try {
    foreach ($entry in $manifest.files) {
        Check-File $entry -Time
        $path = Scoped-Path $entry.path
        # This frozen manifest has explicit one-time batch deletion authorization.
        Remove-Item -LiteralPath $path -Force -ErrorAction Stop
        $deleted++
        $bytes += $entry.bytes
        $writer.WriteLine((@{relative=$entry.relative; bytes=$entry.bytes; sha256=$entry.sha256; deletedAt=[DateTimeOffset]::Now.ToString('o')} | ConvertTo-Json -Compress))
    }
    foreach ($dir in ($directories | Sort-Object Length -Descending)) {
        if (-not (Test-Path -LiteralPath $dir)) { continue }
        $literalDir = Scoped-Path $dir
        if (@(Get-ChildItem -LiteralPath $literalDir -Force | Select-Object -First 1).Count -eq 0) {
            [IO.Directory]::Delete($literalDir, $false)
            $empty++
        }
    }
} catch { $failure = $_.Exception.Message } finally { $writer.Dispose() }
$errors = [Collections.Generic.List[string]]::new()
foreach ($entry in $manifest.protectedFiles) {
    try { Check-File $entry } catch { $errors.Add($_.Exception.Message) }
}
$remaining = @($manifest.files | Where-Object { Test-Path -LiteralPath $_.path })
$result = [ordered]@{
    status = if ($null -eq $failure -and $errors.Count -eq 0 -and $remaining.Count -eq 0) { 'complete' } else { 'needs_attention' }
    authorization = '允许按这份新清单批量删除'
    manifestSha256 = $manifestHash
    started = $started
    completed = [DateTimeOffset]::Now.ToString('o')
    deletedFiles = $deleted
    deletedBytes = $bytes
    emptyDirectoriesRemoved = $empty
    protectedFilesVerified = $manifest.protectedFiles.Count
    remainingSelectedFilesBeforeQA = $remaining.Count
    executionError = $failure
    verificationErrors = @($errors)
}
$result | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $resultPath -Encoding UTF8
$result | ConvertTo-Json -Depth 5
if ($result.status -ne 'complete') { throw 'Inspect cleanup execution results before continuing.' }
