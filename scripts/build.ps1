# Build static HTML for the SciML_PS book.
# Usage: .\scripts\build.ps1

$ErrorActionPreference = "Stop"
$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
Set-Location $Root

if (-not (Get-Command "jupyter" -ErrorAction SilentlyContinue)) {
    Write-Error "jupyter not on PATH. Run: conda activate sciml_ps"
}

Write-Host "Building static site from $Root ..."
& jupyter book build
Write-Host "Done. Open the HTML index reported by the CLI (often under _build/)."
