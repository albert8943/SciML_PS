# Local live preview for the SciML_PS Jupyter Book 2 site.
# Run from anywhere; script cds to the repository root.
# Usage:
#   .\scripts\preview.ps1
#   .\scripts\preview.ps1 -Port 3001
#   .\scripts\preview.ps1 -Execute

param(
    [int]$Port = 3000,
    [switch]$Execute
)

$ErrorActionPreference = "Stop"
# Avoid Windows console Unicode crashes in jupyter-book's Node installer prompts.
$env:PYTHONIOENCODING = "utf-8"
$env:PYTHONUTF8 = "1"
# Bind the site server to IPv4 loopback. Default JB2/MyST often listens on ::1 only,
# which breaks browsers that resolve localhost → 127.0.0.1.
if (-not $env:HOST) {
    $env:HOST = "127.0.0.1"
}

$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
Set-Location $Root

if (-not (Test-Path (Join-Path $Root "myst.yml"))) {
    Write-Error "myst.yml not found at $Root"
}

$jb = Get-Command "jupyter" -ErrorAction SilentlyContinue
if (-not $jb) {
    Write-Host @"
jupyter not found on PATH.

Create / activate the course env first:

  .\scripts\setup_env.ps1
  conda activate sciml_ps

Then re-run:

  .\scripts\preview.ps1
"@
    exit 1
}

$node = Get-Command "node" -ErrorAction SilentlyContinue
if (-not $node) {
    Write-Host @"
Node.js (node) not found on PATH.

Jupyter Book 2 requires Node.js. The course env pins nodejs via conda.
Activate the env (so conda’s node is on PATH), then retry:

  conda activate sciml_ps
  .\scripts\preview.ps1

Or update the env:

  conda env update -f environment.yml --prune
"@
    exit 1
}

Write-Host "Repository root: $Root"
Write-Host "Starting Jupyter Book preview (port $Port)..."
Write-Host "When ready, open: http://localhost:$Port"
Write-Host "Stop with Ctrl+C"
Write-Host ""

$jbArgs = @("book", "start", "--port", "$Port", "--keep-host")
if ($Execute) {
    $jbArgs += "--execute"
}

& jupyter @jbArgs
