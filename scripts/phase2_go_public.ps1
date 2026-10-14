#Requires -Version 5.1
<#
.SYNOPSIS
  Automate Phase 2 GitHub steps for SciML_PS after `gh auth login`.

.DESCRIPTION
  Makes the repo public (optional), sets Pages to GitHub Actions, creates labels,
  enables Discussions topics via API where possible, creates v0.1.0 tag + release.
  DNS CNAME at the registrar and Enforce HTTPS must still be done manually.

.NOTES
  Run from repo root:  .\scripts\phase2_go_public.ps1
  Prerequisites: gh authenticated with repo + admin scope.
#>
param(
  [switch]$SkipVisibilityChange,
  [switch]$SkipRelease,
  [string]$Tag = "v0.1.0"
)

$ErrorActionPreference = "Stop"
$repo = "albert8943/SciML_PS"

Write-Host "Checking gh auth..."
gh auth status
if ($LASTEXITCODE -ne 0) {
  Write-Error "Run: gh auth login --hostname github.com --web"
}

Write-Host "`n=== Repo about / homepage / topics ==="
gh repo edit $repo `
  --description "Living teaching book: SciML for power-system dynamics, stability, and identification (public preview v0.x)" `
  --homepage "https://sciml4ps.albertpoulose.com" `
  --add-topic "scientific-machine-learning" `
  --add-topic "power-systems" `
  --add-topic "jupyter-book" `
  --add-topic "open-educational-resources" `
  --add-topic "pinn" `
  --add-topic "transient-stability"

if (-not $SkipVisibilityChange) {
  Write-Host "`n=== Visibility → public ==="
  gh repo edit $repo --visibility public --accept-visibility-change-consequences
}

Write-Host "`n=== Enable Discussions ==="
gh api -X PATCH "repos/$repo" -f has_discussions=true | Out-Null

Write-Host "`n=== Labels ==="
$labels = @(
  @{ name = "good first issue"; color = "7057ff"; description = "Good for newcomers" },
  @{ name = "help wanted"; color = "008672"; description = "Extra attention welcome" },
  @{ name = "pillar:dynamics"; color = "1d76db"; description = "Dynamics pillar" },
  @{ name = "pillar:stability"; color = "0e8a16"; description = "Stability pillar" },
  @{ name = "pillar:identification"; color = "fbca04"; description = "Identification pillar" },
  @{ name = "labs"; color = "d93f0b"; description = "Laboratories" },
  @{ name = "erratum"; color = "c2e0c6"; description = "Typo / link / clarity fix" },
  @{ name = "chapter-proposal"; color = "5319e7"; description = "New chapter proposal" }
)
foreach ($l in $labels) {
  gh label create $l.name --repo $repo --color $l.color --description $l.description --force 2>$null
  if ($LASTEXITCODE -ne 0) {
    gh api -X PATCH "repos/$repo/labels/$([uri]::EscapeDataString($l.name))" `
      -f color=$($l.color) -f description=$($l.description) 2>$null | Out-Null
  }
}

Write-Host "`n=== Pages: GitHub Actions source ==="
# Enable Pages with GitHub Actions as build/deploy source
gh api -X POST "repos/$repo/pages" -f build_type=workflow 2>$null
gh api -X PUT "repos/$repo/pages" `
  -f build_type=workflow `
  -f cname="sciml4ps.albertpoulose.com" 2>$null
Write-Host "Confirm Settings → Pages → Source = GitHub Actions, custom domain sciml4ps.albertpoulose.com, then Enforce HTTPS."

if (-not $SkipRelease) {
  Write-Host "`n=== Tag and GitHub Release $Tag ==="
  $exists = git rev-parse "refs/tags/$Tag" 2>$null
  if (-not $exists) {
    git tag -a $Tag -m "SciML for PS public preview $Tag"
  }
  git push origin $Tag
  $notes = @"
## SciML for PS $Tag — public preview

Living teaching notes on scientific machine learning for power-system dynamics, stability assessment, and system identification.

**Status:** under development (v0.x). Content may change until v1.0.

- Site: https://sciml4ps.albertpoulose.com
- Contribute: https://sciml4ps.albertpoulose.com/contribute
- Licence: content CC BY-NC-SA 4.0; code MIT

See CHANGELOG.md and ROADMAP.md.
"@
  gh release create $Tag --repo $repo --title "SciML for PS $Tag (public preview)" --notes $notes
  Write-Host "If PDF artifact exists from CI, attach it to the release manually or re-run after Pages build."
}

Write-Host @"

=== Manual steps remaining ===
1. DNS at albertpoulose.com registrar: CNAME host=sciml4ps value=albert8943.github.io
2. Pages → Enforce HTTPS after certificate issues
3. Branch protection on master (optional while solo): require PR + build-book + DCO
4. Install GitHub Apps: DCO, all-contributors, Zenodo
5. Pin Discussion from docs/guides/collaboration/announcement_and_invites.md §C
6. After Zenodo DOI appears, run: .\scripts\phase2_set_doi.ps1 -Doi '10.5281/zenodo.XXXX'
"@
