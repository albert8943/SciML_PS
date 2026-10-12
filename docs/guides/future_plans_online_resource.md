# Future plans for the SciML_PS online resource

**Status:** Planned / not all implemented.  
**Audience:** Maintainers.  
**Recorded:** 2026-10-12 (from scaffold decisions + reference-site review).  
**Do not confuse with:** curriculum science scope — that stays in [`scope_lock_three_pillars.md`](scope_lock_three_pillars.md).

This note records **product / site features** to add over time, inspired by public references and locked stack choices. Implement in the order in §3 unless a semester offering forces otherwise.

---

## 1. Reference websites (what we are copying as *product pattern*)

| Reference | URL | What to learn |
|-----------|-----|----------------|
| EECS 245 **notes** (book) | https://notes.eecs245.org/ | Mature MyST-style notes book (Rampure) |
| Math 124 **notes** (book) | https://notes.math124.org/ | Second notes book (Prasanna & Rampure); under development Fall 2026 |
| EECS 245 **PDF export** | https://notes.eecs245.org/exports/notes.pdf | Full-book PDF; mark experimental if interactive content does not survive export |
| EECS 245 **course portal** | https://eecs245.org/ (e.g. [/sp26/](https://eecs245.org/sp26/)) | Ops site + **term paths**; links *to* the shared notes book |
| EECS 245 **feedback** | [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSfrAu2o3eBa9ZvjerOFxqDHV63GlR9NoYdA4TOgK8BBoSguCg/viewform) | Lightweight typo / UX feedback without building a CMS |
| Author hub | https://rampure.org/ | Many course *material* sites ≠ many notes books |
| PBDL (method book) | https://physicsbaseddeeplearning.org/ | Computational textbook *product type*; **not** our TOC logic (see §2) |
| PBDL source | https://github.com/tum-pbs/pbdl-book | Jupyter Book **1** + Sphinx (`_config.yml`); Colab notebooks |
| EEI Days 2026 talk (Rampure) | [Google Slides](https://docs.google.com/presentation/d/1pmyaWjjlKwRmPZqDNxcwOOw01ZCcfCLdo-wCgPnMzBc/edit) | Interactive JB notes + AI authoring; **saved locally** in [`docs/references/eecs245_eei_days_2026/`](../references/eecs245_eei_days_2026/) |
| EECS 245 notes source | https://github.com/eecs245/notes | Live MyST/JB notes repo cited in that talk |
| Workshop template | https://github.com/math-124/notes-example | Hands-on `jupyter book start` demo from the talk |

**Rampure pattern (important):**

- **~2 notes books** (EECS 245 + Math 124), not dozens.
- **Many** course/offering hubs over a career (slides, calendar, term pages).
- **Not** a new notes-book website every semester — one living book per subject; portals/archives per term.
- Full write-up: [`docs/references/rampure_notes_vs_course_sites.md`](../references/rampure_notes_vs_course_sites.md).

**Michigan-style split (target architecture for SciML_PS):**

```text
Course portal  (portal/ → e.g. course.example.org or /20XX-term/)  ← syllabus, calendar, offering
Book / notes   (book/  → e.g. notes.example.org)                    ← ONE SciML_PS JB2 site (reuse across terms)
Feedback       (Google Form linked from book navbar)
PDF            (MyST export → /exports/….pdf or Downloads action)
```

SciML_PS today: book scaffold lives; `portal/` is a placeholder; no public host, PDF export, or feedback form yet.

---

## 2. Locked stack and content architecture (do not casually reverse)

| Decision | Choice | Note |
|----------|--------|------|
| Engine | **Jupyter Book 2 + MyST** (`myst.yml`) | Not JB1/Sphinx; “Made with MyST” is theme default |
| Runtime for preview | **Python + Node.js** | Python: content/CLI; Node: book-theme website server |
| TOC logic | Prep → foundations → **three pillars** → advanced + labs | Dynamics / stability / identification — see scope lock |
| vs PBDL | Same *product type*; different *spine* | PBDL = method-coupling ladder; we = power engineering questions |
| Course I/II folders | Deferred | Use `book/100_front/learning_paths.md` for semester packaging |
| Research metrics | Never in student pages | Instructor memory stays in research repos |

JB generations: only **JB1** and **JB2** matter as platforms; there is no JB3 yet. Patch versions (`2.1.x`) are updates inside JB2.

Official docs when implementing exports/site: [Jupyter Book websites](https://jupyterbook.org/stable/build-and-publish/website), [PDF export](https://jupyterbook.org/stable/get-started/export-pdfs/), [MyST exports](https://mystmd.org/guide/documents-exports).

---

## 3. Feature backlog (EECS 245–like)

### 3.1 Feedback form — do first (low cost)

- [ ] Create a Google Form (typo, broken link, unclear page; optional email).
- [ ] Add `site.actions` in `myst.yml`, e.g. title `Feedback`, `url:` form link.
- [ ] Mention the form on `book/100_front/how_to_use.md` once live.
- [ ] Keep form anonymous by default; do not put student PII into the repo.

### 3.2 Host the book site

- [ ] CI: `jupyter book build` on default branch.
- [ ] Deploy HTML to GitHub Pages (or equivalent); set `BASE_URL` correctly if using a subpath.
- [ ] Put the public notes URL in root `README.md` and `book/100_front/how_to_use.md`.
- [ ] Prefer IPv4 loopback locally (`scripts/preview.ps1` already sets `HOST=127.0.0.1`).

### 3.3 PDF export of the notes

- [ ] Configure `project.exports` in `myst.yml` (Typst or LaTeX template; article list or full TOC policy).
- [ ] Build with `jupyter book build --pdf` (or documented JB2 equivalent); publish under `exports/` or CI artifact.
- [ ] Add a site action or Downloads entry: **PDF**.
- [ ] Document limitations (stubs, interactive plots → static), similar to EECS 245’s experimental PDF note.
- [ ] Do **not** prioritize a polished full-book PDF until `300_foundations` has real prose.

### 3.4 Separate course portal (`portal/`)

- [ ] Build a thin portal (Quarto, MkDocs, or static HTML) — **not** a second copy of the book.
- [ ] Portal pages: home, syllabus, calendar / week plan, environment setup link, staff, link to **notes** URL, link to Ed/Discord if any.
- [ ] Fill `book/100_front/learning_paths.md` for the offering; portal points at path + notes.
- [ ] Optional second domain later (notes.* vs course.*), same idea as notes.eecs245.org vs eecs245.org.
- [ ] Per semester: add a term page or `portal/20XX-term/` (or git tag `offering-20XX`) — **do not** fork a new notes book site each term (Rampure pattern).

### 3.5 Navbar actions (book chrome)

Target actions once URLs exist (via `site.actions` and/or `site.parts.navbar_end`):

| Action | Points to |
|--------|-----------|
| Feedback | Google Form |
| PDF | Exported notes PDF |
| Course website | Portal URL |
| GitHub | Repo (optional; theme may already expose it) |

### 3.6 Optional later (not required for v1 offering)

- [ ] Replace or customize “Made with MyST” via `site.parts.primary_sidebar_footer`.
- [ ] Colab/Binder launch buttons for selected lab notebooks (PBDL-style).
- [ ] Site-wide footer / announcement banner (`site.parts`).
- [ ] Accessibility pass (alt text, contrast) before a large enrollment.
- [ ] License choice for book prose (update root `LICENSE`).

---

## 4. Implementation order (default)

| Step | Item | Depends on |
|------|------|------------|
| 1 | Feedback Form + `site.actions` | Nothing |
| 2 | Public book host | Stable `myst.yml` TOC |
| 3 | Substantive `300` + labs content | Scope lock |
| 4 | PDF export + Downloads | Enough prose; host optional but nice |
| 5 | Portal + learning path for a real semester | Decision to offer the course |
| 6 | Polish (footer branding, Colab, a11y) | Steps 2–5 |

Do **not** block chapter writing on PDF or portal.

---

## 5. Out of scope for this “future plans” note

- Changing the three-pillar science scope → [`scope_lock_three_pillars.md`](scope_lock_three_pillars.md)
- Day-to-day preview/edit commands → [`using_preview_edit_and_long_term_development.md`](using_preview_edit_and_long_term_development.md) and `book/100_front/preview_locally.md`
- Full curriculum outcomes / lab rubrics → `docs/planning/…Course_Development_Report.md`

---

## 6. When to update this file

Update when you ship feedback, hosting, PDF, or portal; when domains are chosen; or when dropping JB2 for another engine. Check off boxes in §3 rather than rewriting history silently.
