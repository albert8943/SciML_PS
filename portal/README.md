# Portal (course website) — planned

This folder is the home for a **future course operations site**, separate from the Jupyter Book notes.

## Why a separate portal?

Reference pattern (University of Michigan / Suraj Rampure):

| Site | Role |
|------|------|
| [notes.eecs245.org](https://notes.eecs245.org/) | Living **notes book** (shared across terms) |
| [notes.math124.org](https://notes.math124.org/) | Second notes book (in progress) |
| [eecs245.org](https://eecs245.org/) (e.g. [/sp26/](https://eecs245.org/sp26/)) | **Course portal** + term pages — links *to* the notes |

**Rule:** one notes book per subject; portals/archives per semester — **not** a new book website every term. Detail: [`docs/references/rampure_notes_vs_course_sites.md`](../docs/references/rampure_notes_vs_course_sites.md).

SciML_PS should follow the same split:

- **Book** = `book/` + `myst.yml` (dynamics / stability / identification notes and labs) — reuse across offerings
- **Portal** = this directory (when / where / offering logistics); optional `20XX-term/` subfolders later

Do not duplicate chapter prose here. Link out to the published notes URL.

## Planned portal pages (checklist)

- [ ] Home (course title, term, link to notes)
- [ ] Syllabus / grading pointers
- [ ] Calendar or week-by-week plan (can mirror `book/100_front/learning_paths.md`)
- [ ] Environment setup (point at `envs/` + book preview page)
- [ ] Staff / contact
- [ ] Archive of past offerings (optional)

## Stack (decide when building)

Keep the portal **thin**: Quarto, MkDocs, or static HTML are all fine. Prefer whatever is easiest to deploy next to the book (e.g. GitHub Pages project site or `/portal` path).

## Related maintainer docs

- Full feature roadmap: [`docs/guides/future_plans_online_resource.md`](../docs/guides/future_plans_online_resource.md)
- Scope lock (three pillars): [`docs/guides/scope_lock_three_pillars.md`](../docs/guides/scope_lock_three_pillars.md)

## License note

When this portal gains its own pages, keep **operations text** aligned with the book: content **CC BY-NC-SA 4.0**, any custom scripts **MIT**, unless a term-specific university policy requires otherwise. Do not copy third-party course portals wholesale.

## Current status

Placeholder only. Book entry points today: repository `README.md` and `book/index.md` (local preview via `scripts/preview.ps1`).
