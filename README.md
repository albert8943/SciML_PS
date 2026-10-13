# Scientific Machine Learning for Power Systems

Portable teaching book (Jupyter Book 2 / MyST) on SciML for power-system **dynamics**, **stability**, and **parameter estimation**.

This repository is a **scaffold**: stub chapters and labs, not finished prose.

## How to preview, edit, and develop

Maintainer handbook (preview, use, edit, decades-long growth):

[`docs/guides/using_preview_edit_and_long_term_development.md`](docs/guides/using_preview_edit_and_long_term_development.md)

Install teaching package (Lab 1+):

```bash
pip install -e .
```

Site product next steps (CI, Pages, PDF, Form): [`docs/guides/site_hosting.md`](docs/guides/site_hosting.md).

## Layout

| Path | Purpose |
|------|---------|
| `book/` | MyST chapters (parts `100`–`700`, labs `900`, reference `990`) |
| `slides/` | Downloadable slide decks (empty stubs for now) |
| `media/` | Figures and videos |
| `src/sciml_ps/` | Shared teaching Python package |
| `envs/` | Course environment pins (`course_core`, `course_andes`) |
| `docs/planning/` | Curriculum development report (instructor planning) |
| `docs/guides/` | Maintainer how-tos (preview, edit, long-term development) |
| `scripts/` | `setup_env`, `preview`, `build` helpers |
| `portal/` | Optional future landing-page notes |

Part IDs use **100-spacing** (`100`, `200`, `300`, …) so new pillars can be inserted later without renumbering neighbors.

## Content policy

- Teach portable SciML + power examples; cite public literature.
- **Do not** paste sealed research metrics, seed tables, or campaign YAML from research repos.
- Classical Lab 3 targets teaching **inertia/damping** \((H, D)\); do not conflate with research GFM \((M_v, D_v, m_p)\) estimands.
- Pin **one** ANDES version per lab (`envs/course_andes.yml`); never mix 1.10 and 2.0 silently.
- **Scope lock:** three pillars (dynamics / stability / identification) are enough for the core book — see [`docs/guides/scope_lock_three_pillars.md`](docs/guides/scope_lock_three_pillars.md).
- **Future site features** (PDF export, separate course portal, feedback form, hosting — EECS 245–style): [`docs/guides/future_plans_online_resource.md`](docs/guides/future_plans_online_resource.md).
- **Reference pattern:** few living notes books + many term portals — [`docs/references/rampure_notes_vs_course_sites.md`](docs/references/rampure_notes_vs_course_sites.md) (includes Math 124 notes).

## Planning document

Curriculum source of truth for learning outcomes and labs:

[`docs/planning/SciML_for_Power_Systems_Course_Development_Report.md`](docs/planning/SciML_for_Power_Systems_Course_Development_Report.md)

## Build / preview (Jupyter Book 2)

Full copy-paste commands also live **inside the book**: [`book/100_front/preview_locally.md`](book/100_front/preview_locally.md).

**Windows (PowerShell), from repo root:**

```powershell
.\scripts\setup_env.ps1          # creates/updates env (Python + Node.js + JB2)
conda activate sciml_ps
.\scripts\preview.ps1            # jupyter book start
```

Then open `http://127.0.0.1:3000/` (or `http://localhost:3000/`). Leave the preview terminal running.

**macOS / Linux:**

```bash
conda env create -f environment.yml
conda activate sciml_ps
chmod +x scripts/*.sh
./scripts/preview.sh
```

**Raw CLI (any OS):**

```bash
conda activate sciml_ps
jupyter book start          # live preview
jupyter book build          # static HTML
```

Helper scripts: [`scripts/`](scripts/). Config: [`myst.yml`](myst.yml). If a flag differs on your install, check `jupyter book --help`.

## Single book

One site, one TOC. Optional semester packaging lives in `book/100_front/learning_paths.md` (stub). Course I/II split folders are deferred.
