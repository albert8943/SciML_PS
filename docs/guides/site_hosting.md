# Site hosting, PDF, and feedback (Phase E)

**Status:** Scaffolded. Public URL and Google Form still require maintainer choices.

## Feedback

- Student page: [`book/100_front/feedback.md`](../../book/100_front/feedback.md)
- Navbar action in [`myst.yml`](../../myst.yml) → `/feedback/` (interim) or Google Form when ready
- **Next:** create a Google Form; set `site.actions` Feedback `url:` to the form link (see EECS 245 pattern in [`future_plans_online_resource.md`](future_plans_online_resource.md))

## Hosting

- CI workflow: [`.github/workflows/build-book.yml`](../../.github/workflows/build-book.yml) builds HTML on `master` and uploads `_build` as an artifact; PDF job builds `exports/sciml_ps_notes.pdf` when TeX is available
- **Next:** enable GitHub Pages (or other host) from the HTML artifact; set `BASE_URL` if using a project subpath; put the public URL in root `README.md` and `book/100_front/how_to_use.md`
- After Pages is live, ensure `exports/sciml_ps_notes.pdf` is published under the site (CI copies into `_build/html/exports/` when HTML exists)

Local preview remains:

```powershell
conda activate sciml_ps
.\scripts\preview.ps1
```

## PDF export

**Engine:** MyST / Jupyter Book 2 → LaTeX (**jtex** template [`templates/sciml_ps_book/`](../../templates/sciml_ps_book)) → PDF.

**Output:** `exports/sciml_ps_notes.pdf` (gitignored; rebuild locally or download the CI artifact).

**Navbar:** `site.actions` entry **PDF** → `/exports/sciml_ps_notes.pdf`.

### Build locally

```powershell
conda activate sciml_ps
.\scripts\build_pdf.ps1
```

```bash
conda activate sciml_ps
./scripts/build_pdf.sh
```

Or: `python scripts/build_pdf.py` (same as the helpers).

### TeX prerequisites

Install a full-ish TeX distribution that includes **latexmk** and **XeLaTeX**:

| OS | Typical install |
|----|-----------------|
| Windows | [MiKTeX](https://miktex.org/) or TeX Live |
| macOS | MacTeX or `brew install --cask mactex-no-gui` |
| Linux / CI | `texlive-xetex`, `texlive-latex-extra`, `latexmk`, and related fonts |

The custom template also uses `tcolorbox`, `titlesec`, `fancyhdr`, `datetime`, and related packages (usually covered by `texlive-latex-extra` / MiKTeX auto-install).

### Experimental limits (same idea as EECS 245)

- Treat the PDF as **experimental** while chapters are stubs.
- Interactive plots / widgets become **static** or may be **omitted**.
- Prefer the HTML book for labs and navigation.
- Cover page stamps **Compiled on** and **Last repo commit** (via `scripts/build_pdf.py` → `gitinfo.tex`).

### Maintainer layout

| Piece | Role |
|-------|------|
| [`myst.yml`](../../myst.yml) `project.exports` | Points at `./templates/sciml_ps_book` → `exports/sciml_ps_notes.pdf` |
| [`templates/sciml_ps_book/`](../../templates/sciml_ps_book) | jtex skin (navy/teal, title panel, callout boxes) |
| [`scripts/build_pdf.py`](../../scripts/build_pdf.py) | Git stamp + `jupyter book build --pdf` + copy into `exports/` |

Polish the template further after foundations / lab prose lands; do not block chapter writing on PDF cosmetics.

## Course portal

[`portal/`](../../portal/) remains the ops site home. Per-term folders (e.g. `portal/20XX-term/`) come when you offer a semester — do not fork a new notes book. Uncomment the Course website navbar action in `myst.yml` when the portal URL exists.
