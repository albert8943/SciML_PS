# Site hosting, PDF, and feedback (Phase E)

**Status:** Scaffolded. Public URL and Google Form still require maintainer choices.  
**Audience:** Maintainers.  
**Related session:** [`cursor_sessions/2026-10-13_pdf_export.md`](cursor_sessions/2026-10-13_pdf_export.md).

---

## Branding (navbar + sidebar + footer)

MyST Book Theme puts “Made with MyST” in **two** places unless you override them:

| Slot | Default | Our override |
|------|---------|----------------|
| **Top-left navbar** | `logo_text` missing → “Made with MyST” | `site.options.logo_text: SciML for PS` (full title on homepage / PDF) in [`myst.yml`](../../myst.yml) |
| **Bottom of left TOC** | Made-with-MyST badge | [`book/_site/primary_sidebar_footer.md`](../../book/_site/primary_sidebar_footer.md) via `site.parts.primary_sidebar_footer` |
| **Site-wide footer** | (none) | [`book/_site/site_footer.md`](../../book/_site/site_footer.md) via `site.parts.footer` (quiet MyST/JB credit) |

Optional later: add `logo` / `logo_dark` image files under `book/_site/` and point `site.options.logo` at them. Empty the sidebar footer file to hide that slot only.

## Feedback

- Student page: [`book/100_front/feedback.md`](../../book/100_front/feedback.md)
- Navbar action in [`myst.yml`](../../myst.yml) → GitHub issues (interim) or Google Form when ready
- **Next:** create a Google Form; set `site.actions` Feedback `url:` to the form link (see EECS 245 pattern in [`future_plans_online_resource.md`](future_plans_online_resource.md))

### PDF button opens in a new tab

`site.actions` URLs that are **relative** (`/exports/…`) navigate in the **same tab**. Absolute `http(s)://…` actions open with `target="_blank"` (theme behavior). Per-action `target` is not configurable yet ([mystmd#2788](https://github.com/jupyter-book/mystmd/issues/2788)); footer `<script>` tags are stripped from MyST parts.

| Context | `site.actions` PDF `url` in [`myst.yml`](../../myst.yml) |
|---------|---------------------------|
| Local `jupyter book start` | `http://localhost:3100/exports/sciml_ps_notes.pdf` (content server; keeps notes on port 3000) |
| Public host | Absolute URL to the published PDF (same new-tab behavior) |

Restart preview after changing the URL.

---

## Hosting

**Public URL:** <https://sciml4ps.albertpoulose.com> (GitHub Pages, subdomain of the personal site `albertpoulose.com`).

The book lives only in this repo. The personal website repo (`dr-albert-poulose`, Hugo) just links to it; do not copy book sources or `src/sciml_ps/` there.

- CI workflow: [`.github/workflows/build-book.yml`](../../.github/workflows/build-book.yml) builds the PDF, then static HTML (`jupyter book build --html` → `_build/html`), syncs the PDF into `_build/html/exports/`, and deploys to Pages on every push to `master`. Pull requests build only.
- CI rewrites the navbar PDF action from the local `localhost:3100` URL to `https://sciml4ps.albertpoulose.com/exports/sciml_ps_notes.pdf`; `myst.yml` keeps the local URL for preview.
- A failed PDF build does not block the HTML deploy.

### One-time setup (maintainer)

1. **Repo visibility:** GitHub Pages on a free plan needs a **public** repo. Audit for sealed research content, then Settings → General → Change visibility. (Alternatives: GitHub Pro, or Cloudflare Pages / Netlify from a private repo.)
2. **Pages source:** Settings → Pages → Build and deployment → Source: **GitHub Actions**.
3. **DNS** at the `albertpoulose.com` registrar: add `CNAME` record, host `sciml4ps`, value `albert8943.github.io`.
4. **Custom domain:** Settings → Pages → Custom domain: `sciml4ps.albertpoulose.com`, then tick **Enforce HTTPS** once the certificate is issued.
5. **Personal site:** add a nav link (e.g. Teaching / Books) to `https://sciml4ps.albertpoulose.com` in the Hugo repo.

### Local preview (one book URL)

```powershell
conda activate sciml_ps
.\scripts\preview.ps1
```

**Open only:** [http://localhost:3000/](http://localhost:3000/)

Do not start a second `preview.ps1` while one is running (that creates an extra UI port and confuses everyone).

---

## Local preview: ports and PDF viewing (lessons learned)

Jupyter Book 2 / MyST **always** runs two local servers during `jupyter book start`:

| Port (typical) | Role |
|----------------|------|
| **3000** | Book theme UI (what you bookmark) |
| **3100** | Content / static file server (PDF and hashed assets) |

- **3000 and 3100 together are one preview**, not two books.
- The navbar PDF path `/exports/sciml_ps_notes.pdf` is often **redirected** from the theme (3000) to the content server (`http://localhost:3100/exports/...`). That is normal.
- Preview scripts set `HOST=localhost` (with `--keep-host`) so that redirect target matches. Forcing `HOST=127.0.0.1` made PDF redirects point at `localhost:3100` while servers listened only on `127.0.0.1`, which produced blank/failed PDF tabs on Windows.
- **Cursor’s built-in browser** often shows the PDF filename chrome and a **blank dark page**. Open the book/PDF in **Chrome or Edge**, or open the file on disk: `exports/sciml_ps_notes.pdf`.
- `127.0.0.1` and `localhost` both mean “this computer”; the **port** is what selects the app. Prefer the single documented book URL above.

---

## PDF export

**Engine:** MyST / Jupyter Book 2 → LaTeX (**jtex** template [`templates/sciml_ps_book/`](../../templates/sciml_ps_book)) → XeLaTeX / `latexmk`.  
Inspired by [EECS 245 notes PDF](https://notes.eecs245.org/exports/notes.pdf) (custom LaTeX skin + CI), not HTML print-to-PDF.

**Output:** `exports/sciml_ps_notes.pdf` (gitignored; rebuild locally or download CI artifact `sciml-ps-notes-pdf`).

**Navbar:** `site.actions` **PDF** → `/exports/sciml_ps_notes.pdf`.

That link is a **static download**, not a live rebuild. After content edits:

```powershell
.\scripts\build_pdf.ps1
# then hard-refresh the PDF URL (Ctrl+F5) in Chrome/Edge
```

### MyST wiring

- `project.exports` id `notes-pdf` → `./templates/sciml_ps_book` → `exports/sciml_ps_notes.pdf`
- `project.downloads` → same id (download panel)
- `project.static_files: [exports]` — stable `/exports/…` path for the navbar
- After each build, `scripts/build_pdf.py` syncs into `_build/site/public/exports/` for a running preview

If preview is already up and the PDF on disk is already rebuilt:

```powershell
python scripts/build_pdf.py --sync-only
```

### Cover page (professional minimum)

Title forms follow [`naming_and_titles.md`](naming_and_titles.md). The PDF cover shows:

| Cover line | Form |
|------------|------|
| Teal eyebrow | **SciML for PS** (short brand) |
| Main title | From `myst.yml` `project.title` → full **Scientific Machine Learning (SciML) for Power Systems (PS)** |
| Focus line | Focus — dynamic modeling, stability assessment, and system identification |
| Provenance | **Last updated:** git commit local time + short hash |
| Caveat | Experimental PDF note |

Author line and experimental caveat remain below the navy block.

`scripts/build_pdf.py` writes `templates/sciml_ps_book/gitinfo.tex` with:

- `\lastcommitdate` — shown as **Last updated:** local date/time + short hash

That stamp is the **latest git commit** (not PDF build wall-clock). Time is converted to the **builder machine’s local timezone**, labeled e.g. `(UTC+09:00)` or `(UTC+05:30)`. Rebuild clock / compile-time lines are intentionally omitted from the cover.

### Page headers (not stuck on “Contents”)

MyST exports parts as `\section` and pages as `\subsection` (not `\chapter`). The jtex template sets `\sectionmark` / `\subsectionmark` so fancyhdr shows the **current page/section title** instead of a stuck TOC “Contents” mark.

### Build locally

```powershell
conda activate sciml_ps
.\scripts\build_pdf.ps1
```

```bash
conda activate sciml_ps
./scripts/build_pdf.sh
```

Or: `python scripts/build_pdf.py`.

### TeX prerequisites

Install a full-ish TeX distribution that includes **latexmk** and **XeLaTeX**:

| OS | Typical install |
|----|-----------------|
| Windows | [MiKTeX](https://miktex.org/) or TeX Live |
| macOS | MacTeX or `brew install --cask mactex-no-gui` |
| Linux / CI | `texlive-xetex`, `texlive-latex-extra`, `latexmk`, and related fonts |

The custom template also uses `tcolorbox`, `titlesec`, `fancyhdr`, and related packages (usually covered by `texlive-latex-extra` / MiKTeX auto-install).

### Experimental limits (same idea as EECS 245)

- Treat the PDF as **experimental** while chapters are stubs.
- Interactive plots / widgets become **static** or may be **omitted**.
- Prefer the HTML book for labs and navigation.

### Maintainer layout

| Piece | Role |
|-------|------|
| [`myst.yml`](../../myst.yml) `project.exports` / `static_files` / `downloads` | Export + stable `/exports/` + download panel |
| [`templates/sciml_ps_book/`](../../templates/sciml_ps_book) | jtex skin (navy/teal, title panel, callout boxes, header marks) |
| [`scripts/build_pdf.py`](../../scripts/build_pdf.py) | Local TZ stamps, MyST PDF build, TeX polish, site sync |
| [`scripts/preview.ps1`](../../scripts/preview.ps1) / `.sh` | One book URL; `HOST=localhost`; refuse second UI if port busy |

Polish the template further after foundations / lab prose lands; do not block chapter writing on PDF cosmetics. Playwright figure snapshots only if interactive labs need them later.

---

## Course portal

[`portal/`](../../portal/) remains the ops site home. Per-term folders (e.g. `portal/20XX-term/`) come when you offer a semester — do not fork a new notes book. Uncomment the Course website navbar action in `myst.yml` when the portal URL exists.
