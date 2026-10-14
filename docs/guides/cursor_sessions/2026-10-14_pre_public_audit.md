# 2026-10-14 — Pre-public audit (licences, warnings, contribution invites)

## Checked and already fine

- `LICENSE` / `LICENSES/` (CC BY-NC-SA 4.0 content, MIT code), SPDX headers on `src/sciml_ps/*.py` and `scripts/*.py`, `book/100_front/license.md` (incl. DCO), `CITATION.cff` v0.1.0.
- Under-development notices: site-wide announcement bar, home `{warning}`, footer, README status/badges.
- Contribution invites: navbar Contribute + Feedback, `contribute.md`, `CONTRIBUTING.md` (DCO), Code of Conduct, governance, issue forms.

## Fixed

- Draft maturity note added to 26 chapter/lab pages that had none (reference, licence, and front pages left without).
- Exercise/solution pairs now link by `:label:` (two build warnings removed; template updated).
- Footer links use site pages (`/contribute`, `/status-and-versions`, `/license`) instead of GitHub blob URLs.
- PDF cover: v0.x under-development + contributions-welcome line.
- Removed maintainer-only wording ("do not announce as first/only") from README and `related_resources.md`.
- Invite draft URL `/related_resources` → `/related-resources`; all-contributors avatar URL fixed.

## Still open (owner)

- KNU IP policy confirmation; `gh auth login` then `scripts/phase2_go_public.ps1`; DNS CNAME; Zenodo DOI.
