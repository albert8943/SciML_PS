#Requires -Version 5.1
<#
.SYNOPSIS
  Record a Zenodo DOI in CITATION.cff, README, and (optionally) website open_resources.yaml.

.EXAMPLE
  .\scripts\phase2_set_doi.ps1 -Doi "10.5281/zenodo.12345678"
#>
param(
  [Parameter(Mandatory = $true)]
  [string]$Doi,
  [string]$WebsiteOpenResources = ""
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $root

$doiUrl = if ($Doi -match '^https?://') { $Doi } else { "https://doi.org/$Doi" }
$doiId = $Doi -replace '^https?://(dx\.)?doi\.org/', ''

$cff = Get-Content -Raw CITATION.cff
if ($cff -notmatch '(?m)^identifiers:') {
  $block = @"

identifiers:
  - type: doi
    value: "$doiId"
    description: Zenodo version DOI for this release
"@
  if ($cff -match '(?m)^version:') {
    $cff = $cff -replace '(?m)^(version:.*)$', "`$1$block"
  } else {
    $cff = $cff.TrimEnd() + "`n$block`n"
  }
} else {
  Write-Host "CITATION.cff already has identifiers; update the DOI by hand if needed."
}
Set-Content -Path CITATION.cff -Value $cff -NoNewline

$readme = Get-Content -Raw README.md
if ($readme -notmatch [regex]::Escape($doiId)) {
  $readme = $readme -replace '(## Cite\r?\n\r?\n)', "`$1Zenodo DOI: [$doiId]($doiUrl)`n`n"
  Set-Content -Path README.md -Value $readme -NoNewline
}

Write-Host "Updated CITATION.cff / README for DOI $doiId"
Write-Host "Also set doi: `"$doiId`" in dr-albert-poulose data/open_resources.yaml if the site link should show DOI."
if ($WebsiteOpenResources -and (Test-Path $WebsiteOpenResources)) {
  $y = Get-Content -Raw $WebsiteOpenResources
  $y = $y -replace '(?m)^(\s*doi:\s*)""', "`$1`"$doiId`""
  Set-Content -Path $WebsiteOpenResources -Value $y -NoNewline
  Write-Host "Updated $WebsiteOpenResources"
}
