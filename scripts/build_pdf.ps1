# Build the full-book PDF for SciML_PS (MyST → LaTeX).
# Usage: .\scripts\build_pdf.ps1
# Requires: conda env sciml_ps (jupyter-book) and a LaTeX distribution with latexmk.

$ErrorActionPreference = "Stop"
$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
Set-Location $Root

if (-not (Get-Command "python" -ErrorAction SilentlyContinue)) {
    Write-Error "python not on PATH. Run: conda activate sciml_ps"
}

Write-Host "Building PDF from $Root ..."
& python (Join-Path $PSScriptRoot "build_pdf.py")
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
Write-Host "Done. PDF: exports\sciml_ps_notes.pdf"
Write-Host "If preview is running, hard-refresh http://127.0.0.1:3000/exports/sciml_ps_notes.pdf"
