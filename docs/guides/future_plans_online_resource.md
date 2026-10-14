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
| EECS 245 **notes** (book) | https://notes.eecs245.org/ | Mature MyST-style notes book (Rampure); **CC BY-NC-ND 4.0** — link only; patterns reimplemented (see [`../references/rampure_notes_vs_course_sites.md`](../references/rampure_notes_vs_course_sites.md)) |
| Math 124 **notes** (book) | https://notes.math124.org/ | Second notes book (Prasanna & Rampure); under development Fall 2026; **no licence stated** — patterns only |
| EECS 245 **PDF export** | https://notes.eecs245.org/exports/notes.pdf | Full-book PDF; mark experimental if interactive content does not survive export |
| EECS 245 **course portal** | https://eecs245.org/ (e.g. [/sp26/](https://eecs245.org/sp26/)) | Ops site + **term paths**; links *to* the shared notes book |
| EECS 245 **feedback** | [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSfrAu2o3eBa9ZvjerOFxqDHV63GlR9NoYdA4TOgK8BBoSguCg/viewform) | Lightweight typo / UX feedback without building a CMS |
| Author hub | https://rampure.org/ | Many course *material* sites ≠ many notes books |
| PBDL (method book) | https://physicsbaseddeeplearning.org/ | Computational textbook *product type*; **not** our TOC logic (see §2) |
| PBDL source | https://github.com/tum-pbs/pbdl-book | Jupyter Book **1** + Sphinx (`_config.yml`); Colab notebooks; **Apache-2.0**; reuse rules in [`pbdl_reuse_map.md`](pbdl_reuse_map.md) |
| EEI Days 2026 talk (Rampure) | [Google Slides](https://docs.google.com/presentation/d/1pmyaWjjlKwRmPZqDNxcwOOw01ZCcfCLdo-wCgPnMzBc/edit) | Interactive JB notes + AI authoring; notes in [`docs/references/eecs245_eei_days_2026/`](../references/eecs245_eei_days_2026/) (offline copy git-ignored) |
| EECS 245 notes source | https://github.com/eecs245/notes | Live MyST/JB notes repo cited in that talk |
| Workshop template | https://github.com/math-124/notes-example | Hands-on `jupyter book start` demo from the talk |
| Wealthfolio **docs** (product help UX) | https://wealthfolio.app/docs/introduction/ | Landing discipline only — not our stack or TOC (see §1b) |
| ANDES **docs / gallery** | https://docs.andes.app/en/stable/ | Network reference — summarize-then-link; see [`andes_content_strategy.md`](andes_content_strategy.md) |
| Field positioning (student page) | [`book/100_front/related_resources.md`](../../book/100_front/related_resources.md) | Niche vs neighbors; safe announcement wording; re-check before public launch |

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

SciML_PS today: foundations + Labs 1/3 prose exist; interim Feedback (GitHub issues) + LaTeX/jtex full-book PDF export (`templates/sciml_ps_book`, `scripts/build_pdf.*`, cover **Last updated** from git commit, section headers) + CI HTML/PDF jobs + local preview documented as **one URL** `http://localhost:3000/` (JB content port ~3100) + `portal/20XX-term/` template are in place. Home page uses Wealthfolio-style landing polish (§1b). Live public host, Google Form URL, and further PDF polish remain open (§3 checkboxes). Detail: [`site_hosting.md`](site_hosting.md).

### 1b. Landing UX to borrow (not the docs stack)

Wealthfolio’s help site is an **app manual** (MDX/Nextra/Starlight-*class* tooling). SciML_PS stays **Jupyter Book 2 / MyST** (course notes). Borrow **writing and IA polish** only:

| Borrow | SciML_PS placement |
|--------|-------------------|
| One newcomer CTA | Home: [Start here](../../book/100_front/start_here.md), then a route by background. The long route remains Preparation → Foundations |
| Slim pillar skim + depth elsewhere | Home: three bullets; full “what you produce” table on [book map](../../book/100_front/book_map.md) |
| Explore entry tiles | Home: MyST `{grid}` + `{card}` (Getting started / Foundations / Laboratories / Reference) |
| Quiet version cue | PDF cover **Last updated** (git commit); home note points there — do not add a second maintainer clock on every page |
| Short caveats | One compact “prefer live notes” note; no long status essay on home |
| Site search | Use theme search when hosting; locally sidebar + browser find. Do **not** switch the book engine for search alone |

**Do not** replace JB2 with a product-docs framework, or reshape the TOC into “User Guide / Self-Hosting” buckets.

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

- [x] Interim Feedback page + navbar action (`book/100_front/feedback.md`, GitHub issues)
- [ ] Create a Google Form (typo, broken link, unclear page; optional email).
- [ ] Point `site.actions` Feedback `url:` at the form link.
- [ ] Keep form anonymous by default; do not put student PII into the repo.

### 3.2 Host the book site

- [x] CI: `jupyter book build` on default branch (`.github/workflows/build-book.yml` artifact).
- [ ] Deploy HTML to GitHub Pages (or equivalent); set `BASE_URL` correctly if using a subpath.
- [ ] Put the public notes URL in root `README.md` and `book/100_front/how_to_use.md`.
- [x] Local preview: one URL `http://localhost:3000/` (`HOST=localhost`; JB content port ~3100).
- Detail: [`site_hosting.md`](site_hosting.md).

### 3.3 PDF export of the notes

- [x] Configure `project.exports` in `myst.yml` (LaTeX / jtex full-TOC → `exports/sciml_ps_notes.pdf`).
- [x] Custom skin [`templates/sciml_ps_book/`](../../templates/sciml_ps_book) (navy/teal, title panel, `tcolorbox` callouts).
- [x] Build helpers: `scripts/build_pdf.ps1` / `.sh` / `build_pdf.py`.
- [x] Site action **PDF** → `/exports/sciml_ps_notes.pdf`.
- [x] Document limitations in [`site_hosting.md`](site_hosting.md) (experimental; interactive → static).
- [ ] Polish full-book PDF after more foundations/lab prose lands (Playwright figure snapshots only if labs need them).

### 3.4 Separate course portal (`portal/`)

- [x] Portal placeholder + `portal/20XX-term/` template (Rampure pattern).
- [ ] Build a thin portal site (Quarto, MkDocs, or static HTML) — **not** a second copy of the book.
- [ ] Portal pages: home, syllabus, calendar / week plan, environment setup link, staff, link to **notes** URL.
- [ ] Fill `book/100_front/learning_paths.md` for the offering; portal points at path + notes.
- [ ] Optional second domain later (notes.* vs course.*).
- [ ] Uncomment Course website navbar action in `myst.yml` when URL exists.

### 3.5 Navbar actions (book chrome)

Target actions once URLs exist (via `site.actions` and/or `site.parts.navbar_end`):

| Action | Points to |
|--------|-----------|
| Feedback | Google Form |
| PDF | Exported notes PDF |
| Course website | Portal URL |
| GitHub | Repo (optional; theme may already expose it) |

### 3.6 Optional later (not required for v1 offering)

- [x] Replace default “Made with MyST” (navbar `logo_text` + `site.parts.primary_sidebar_footer` in `book/_site/`).
- [x] Home landing polish (§1b): CTA, slim pillars, Explore cards, short PDF caveat.
- [x] Theme builds `myst.search.json` (local search available in book theme); re-check UX label after public host is live.
- [x] Colab/Binder launch scaffolding (PBDL-style badges + `binder/` + [Running notebooks](../../book/100_front/running_notebooks.md)). Cloud buttons need a public repo; click-test after go-public. Prep `nb01`–`nb04` badges still deferred until those stubs are filled.
- [x] Site-wide footer (`site.parts.footer`); pre-1.0 announcement part + footer notice (2026-10-14).
- [ ] Accessibility pass (alt text, contrast) before a large enrollment.
- [x] License choice: content CC BY-NC-SA 4.0, code MIT (root `LICENSE`). Rationale and remaining pre-public checks: [`legal_and_licensing_considerations.md`](legal_and_licensing_considerations.md).

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
