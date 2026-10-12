# Scientific Machine Learning for Power Systems

Portable teaching book (Jupyter Book 2 / MyST) on SciML for power-system **dynamics**, **stability**, and **parameter estimation**.

This repository is a **scaffold**: stub chapters and labs, not finished prose.

## Layout

| Path | Purpose |
|------|---------|
| `book/` | MyST chapters (parts `100`–`700`, labs `900`, reference `990`) |
| `slides/` | Downloadable slide decks (empty stubs for now) |
| `media/` | Figures and videos |
| `src/sciml_ps/` | Shared teaching Python package |
| `envs/` | Course environment pins (`course_core`, `course_andes`) |
| `docs/planning/` | Curriculum development report (instructor planning) |
| `portal/` | Optional future landing-page notes |

Part IDs use **100-spacing** (`100`, `200`, `300`, …) so new pillars can be inserted later without renumbering neighbors.

## Content policy

- Teach portable SciML + power examples; cite public literature.
- **Do not** paste sealed research metrics, seed tables, or campaign YAML from research repos.
- Classical Lab 3 targets teaching **inertia/damping** \((H, D)\); do not conflate with research GFM \((M_v, D_v, m_p)\) estimands.
- Pin **one** ANDES version per lab (`envs/course_andes.yml`); never mix 1.10 and 2.0 silently.

## Planning document

Curriculum source of truth for learning outcomes and labs:

[`docs/planning/SciML_for_Power_Systems_Course_Development_Report.md`](docs/planning/SciML_for_Power_Systems_Course_Development_Report.md)

## Build / preview (Jupyter Book 2)

Create an environment (example):

```bash
conda env create -f environment.yml
conda activate sciml_ps
```

From the repository root:

```bash
# Local preview server (JB2 / MyST)
jupyter book start

# Or build static HTML
jupyter book build
```

If your installed CLI differs slightly, check `jupyter book --help` for the current JB2 commands. Configuration lives in [`myst.yml`](myst.yml).

## Single book

One site, one TOC. Optional semester packaging lives in `book/100_front/learning_paths.md` (stub). Course I/II split folders are deferred.
