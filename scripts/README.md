# Scripts

| Script | Purpose |
|--------|---------|
| `setup_env.ps1` | Create/update the `sciml_ps` conda env |
| `preview.ps1` / `preview.sh` | Live local preview (`jupyter book start`) |
| `build.ps1` / `build.sh` | Static HTML build (`jupyter book build`) |
| `build_pdf.ps1` / `build_pdf.sh` / `build_pdf.py` | Full-book PDF (`exports/sciml_ps_notes.pdf`) |
| `build_pdf.py --sync-only` | Copy existing PDF into `_build/site/public/exports/` for a running preview |

The navbar **PDF** button does not rebuild the PDF; run `build_pdf` after content changes. PDF notes: [`docs/guides/site_hosting.md`](../docs/guides/site_hosting.md).

Book page with HTML preview commands: [`book/100_front/preview_locally.md`](../book/100_front/preview_locally.md).

**License:** scripts are **MIT** (see root [`LICENSE`](../LICENSE)). Figure regeneration: `make_figures.py`.
