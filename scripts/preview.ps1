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
# Jupyter Book 2 runs TWO local ports: theme UI (--port, default 3000) and a
# content/static server (usually 3100). PDF links redirect to the content port.
# Keep HOST=localhost so that redirect target matches (127.0.0.1 breaks the PDF
# redirect, which hard-codes http://localhost:<content-port>/...).
if (-not $env:HOST) {
    $env:HOST = "localhost"
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

# Canonical book URL (theme UI). Content/PDF server is usually Port+100 (3100).
$BookUrl = "http://localhost:$Port/"
$PdfUrl = "http://localhost:$Port/exports/sciml_ps_notes.pdf"

$existing = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue |
    Select-Object -First 1
if ($existing) {
    Write-Host "Preview already running."
    Write-Host "Open this URL only: $BookUrl"
    Write-Host "PDF button:          $PdfUrl  (opens via JB content port; use Chrome/Edge)"
    Write-Host "Do not start a second .\scripts\preview.ps1 (extra UI ports)."
    exit 0
}

# Navbar PDF → /exports/sciml_ps_notes.pdf (static_files). Does not auto-rebuild.
$pdfPath = Join-Path $Root "exports\sciml_ps_notes.pdf"
$py = Get-Command "python" -ErrorAction SilentlyContinue
if (Test-Path $pdfPath) {
    if ($py) {
        & python (Join-Path $PSScriptRoot "build_pdf.py") --sync-only 2>$null
    }
    Write-Host "PDF button serves the last built file: exports\sciml_ps_notes.pdf"
    Write-Host "After editing content, run .\scripts\build_pdf.ps1 then hard-refresh the PDF URL."
} else {
    Write-Host "WARNING: exports\sciml_ps_notes.pdf missing — navbar PDF will 404."
    Write-Host "Build it with: .\scripts\build_pdf.ps1"
}

Write-Host "Starting Jupyter Book preview..."
Write-Host "Open this URL only: $BookUrl"
Write-Host "PDF navbar uses the same site (JB also listens on ~$($Port+100) for files)."
Write-Host "Stop with Ctrl+C"
Write-Host ""

$jbArgs = @("book", "start", "--port", "$Port", "--keep-host")
if ($Execute) {
    $jbArgs += "--execute"
}

& jupyter @jbArgs
