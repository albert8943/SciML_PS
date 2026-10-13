# Session — SciML_PS PDF export and local preview (EECS 245–style)

**Date:** 2026-10-13  
**Repo:** SciML_PS  
**Scope:** Full-book LaTeX/jtex PDF pipeline; navbar PDF serving; preview URL/ports; cover provenance; header marks

Canonical maintainer doc (keep this session short): [`../site_hosting.md`](../site_hosting.md).

## What landed

### PDF pipeline

- Replaced Typst stub with full-TOC LaTeX export in `myst.yml` → `exports/sciml_ps_notes.pdf`
- Custom jtex skin: `templates/sciml_ps_book/` (navy/teal, title panel, `tcolorbox` callouts)
- Build helpers: `scripts/build_pdf.py`, `.ps1`, `.sh` (git stamp + TeX polish/recompile + site sync)
- Navbar **PDF** action; CI `build-pdf` job in `.github/workflows/build-book.yml`
- Sample MyST admonitions on index / how_to_use / foundations overview
- Cover shows **Last updated** from latest git commit (local TZ + short hash); build wall-clock removed for a cleaner professional cover
- Running headers show **section/page titles** (not stuck “Contents”)

### Preview / PDF button lessons

- Navbar PDF is **static** — does not regenerate on click; run `build_pdf` then hard-refresh
- `project.static_files: [exports]` + sync to `_build/site/public/exports/` so `/exports/…` is reachable
- JB2 always uses **two ports**: theme **3000** + content/static **~3100** (one preview, not two books)
- Prefer **`http://localhost:3000/`** as the single book URL; scripts use `HOST=localhost` so PDF redirects to `localhost:3100` work
- Forcing `HOST=127.0.0.1` broke PDF redirects (theme sent users to `localhost:3100` while servers bound only to `127.0.0.1`)
- Cursor built-in browser often shows a **blank** PDF viewer — use Chrome/Edge or open `exports/sciml_ps_notes.pdf` on disk

## Verify locally

```powershell
conda activate sciml_ps
.\scripts\build_pdf.ps1
.\scripts\preview.ps1
```

- Book: http://localhost:3000/
- PDF file: `exports/sciml_ps_notes.pdf` (gitignored; CI artifact `sciml-ps-notes-pdf`)

## Docs updated this day

- [`../site_hosting.md`](../site_hosting.md) — ports, PDF button, cover Last updated, headers
- [`../../book/100_front/preview_locally.md`](../../book/100_front/preview_locally.md) — one URL + troubleshooting
- [`../../book/100_front/how_to_use.md`](../../book/100_front/how_to_use.md) — PDF tip
- [`../using_preview_edit_and_long_term_development.md`](../using_preview_edit_and_long_term_development.md) — pointers
- [`../future_plans_online_resource.md`](../future_plans_online_resource.md) — §3.3 status

## Follow-ups

- Polish PDF after more foundations/lab prose
- Playwright figure snapshots only if interactive labs need them
- Public host so `/exports/sciml_ps_notes.pdf` is reachable without local preview
- Google Form URL for Feedback action
