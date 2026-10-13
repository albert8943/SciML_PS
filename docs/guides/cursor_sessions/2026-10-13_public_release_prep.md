# Session — Public release prep (hosting, license, rights audit)

**Date:** 2026-10-13  
**Repo:** SciML_PS (writable). Website `dr-albert-poulose` not edited.

## Delivered

| Item | Path / note |
|------|-------------|
| Pages deploy to `sciml4ps.albertpoulose.com` | `.github/workflows/build-book.yml`; setup steps in [`../site_hosting.md`](../site_hosting.md#hosting) |
| Dual license: content CC BY-NC-SA 4.0, code MIT | `LICENSE`, `LICENSES/*`, `myst.yml`, `pyproject.toml`, site footer, PDF cover, `book/100_front/license.md`, `CITATION.cff`, SPDX headers on `src/sciml_ps/` |
| Original transient-cases figure | `media/figures/smib-transient-cases.png` from `scripts/make_figures.py` (`sciml_ps.smib`) |
| IEEE/CIGRE classification | Mermaid diagram in `book/500_stability/01_stability_and_cct.md`; attribution row `IEEE-CIGRE-CLASS` |
| Third-party EEI Days slides | Removed from repo; offline copies in git-ignored `docs/references/_private/` |
| Local vault path | Scrubbed from `vault_import_map.md` |

## History rewrite

Removed from all commits (`git filter-branch`): EEI Days PDF/PPTX/text extract, `stability-classification.png`, old `transient-stability-cases.png`. Pre-rewrite backup bundle kept outside the repo. Remote needs a one-time force push.

## Open

- Force push, then make the repo public and finish the Pages/DNS checklist.
- Website figures on albertpoulose.com may share the same copied images; check separately.
- Visa / university IP check before any paid use of the content.
