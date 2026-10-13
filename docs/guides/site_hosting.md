# Site hosting, PDF, and feedback (Phase E)

**Status:** Scaffolded. Public URL and Google Form still require maintainer choices.

## Feedback

- Student page: [`book/100_front/feedback.md`](../../book/100_front/feedback.md)
- Navbar action in [`myst.yml`](../../myst.yml) → `/feedback/`
- **Next:** create a Google Form; set `site.actions` Feedback `url:` to the form link (see EECS 245 pattern in [`future_plans_online_resource.md`](future_plans_online_resource.md))

## Hosting

- CI workflow: [`.github/workflows/build-book.yml`](../../.github/workflows/build-book.yml) builds on `master` and uploads `_build` as an artifact
- **Next:** enable GitHub Pages (or other host) from the HTML artifact; set `BASE_URL` if using a project subpath; put the public URL in root `README.md` and `book/100_front/how_to_use.md`

Local preview remains:

```powershell
conda activate sciml_ps
.\scripts\preview.ps1
```

## PDF export

Configured under `project.exports` in `myst.yml` (Typst stub targeting `book/index.md`).

```bash
jupyter book build --pdf
```

Expand `articles` / TOC coverage once foundations prose is stable enough for a full notes PDF. Treat early PDFs as experimental (interactive notebooks will not survive).

## Course portal

[`portal/`](../../portal/) remains the ops site home. Per-term folders (e.g. `portal/20XX-term/`) come when you offer a semester — do not fork a new notes book. Uncomment the Course website navbar action in `myst.yml` when the portal URL exists.
