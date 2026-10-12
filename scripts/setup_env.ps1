# Create or update the sciml_ps conda environment.
# Usage: .\scripts\setup_env.ps1

$ErrorActionPreference = "Stop"
$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
Set-Location $Root

if (-not (Get-Command "conda" -ErrorAction SilentlyContinue)) {
    Write-Error "conda not found on PATH."
}

$envPath = Join-Path $Root "environment.yml"
Write-Host "Creating/updating conda env from $envPath ..."

$existing = conda env list | Select-String -Pattern "^\s*sciml_ps\s"
if ($existing) {
    conda env update -f $envPath --prune
} else {
    conda env create -f $envPath
}

Write-Host ""
Write-Host "Next:"
Write-Host "  conda activate sciml_ps"
Write-Host "  .\scripts\preview.ps1"
