# Session — Phase 2 blocker (needs author GitHub login)

**Date:** 2026-10-14  
**Status:** Agent work for Phases 0, 3, 4 done; Phase 2 automation ready; **visibility / Pages / DNS / Zenodo blocked** without `gh` or a signed-in browser.

## Already done

| Item | Status |
|------|--------|
| Phase 0 content audit + website figure cleanup | Done (legal checklist updated; site rasters replaced) |
| Collaboration scaffolding (Phase 1) | Done (prior commit) |
| Website Teaching OER card + news | Pushed to `dr-albert-poulose` `f38fd48` |
| Invite drafts | `docs/guides/collaboration/announcement_and_invites.md` |
| `v0.1.0` annotated tag | Pushed to `origin` (`a81f832`) |
| Scripts | `scripts/phase2_go_public.ps1`, `scripts/phase2_set_doi.ps1` |

## Author: finish Phase 2 (about 15–30 min)

```powershell
cd <SciML_PS clone root>
gh auth login --hostname github.com --web
.\scripts\phase2_go_public.ps1
```

Then:

1. Registrar DNS: `CNAME` host `sciml4ps` → `albert8943.github.io`
2. GitHub Pages → custom domain `sciml4ps.albertpoulose.com` → **Enforce HTTPS**
3. Install apps: DCO, all-contributors, Zenodo (link repo)
4. Optional: branch protection; pin Discussion from invite drafts §C
5. After Zenodo DOI appears:

```powershell
.\scripts\phase2_set_doi.ps1 -Doi "10.5281/zenodo.XXXX"
# If the personal site should show the DOI, also set doi in that repo's data/open_resources.yaml
git add CITATION.cff README.md
```

6. Tick KNU employer IP in `docs/guides/legal_and_licensing_considerations.md` §7 when confirmed (before paid use).

## Pre-public secrets note (2026-10-14)

Maintainer contact email in `CODE_OF_CONDUCT.md` is intentional and approved for public sharing. Do not `git add -f` `docs/references/_private/` (third-party offline copies).

## Why agent stopped

- `gh` not authenticated (device login needs you).
- Cursor browser not signed into GitHub (settings URL 404 for private repo).
- DNS cannot be changed from this machine without registrar access.
