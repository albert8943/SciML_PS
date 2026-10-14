# Scientific Machine Learning (SciML) for Power Systems (PS)

[![Under development](https://img.shields.io/badge/status-under%20development%20(v0.x)-orange)](book/100_front/status_and_versions.md)
[![Content license](https://img.shields.io/badge/content-CC%20BY--NC--SA%204.0-lightgrey)](LICENSES/CC-BY-NC-SA-4.0.txt)
[![Code license](https://img.shields.io/badge/code-MIT-blue)](LICENSES/MIT.txt)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)

Portable teaching book (Jupyter Book 2 / MyST) on SciML for power-system **dynamics**, **stability**, and **parameter estimation**. Short form: **SciML for PS** (repo folder `SciML_PS`). Machine-learning readers and power-systems readers, including complete beginners, choose an entrance on [Start here](book/100_front/start_here.md).

**Status:** public preview (**v0.x**). Living notes; content may change until the first stable edition. See [status and versions](book/100_front/status_and_versions.md) and [roadmap](ROADMAP.md).

**Online book:** <https://sciml4ps.albertpoulose.com> (deployed from `master` by GitHub Actions; one-time setup in [`docs/guides/site_hosting.md`](docs/guides/site_hosting.md#hosting)).

**Positioning:** to our knowledge there is not yet an established open, collaborative living textbook with this three-application spine; see [related open resources](book/100_front/related_resources.md) for neighbouring courses, notes, and research codes.

Title usage (full vs short vs focus subtitle): [`docs/guides/naming_and_titles.md`](docs/guides/naming_and_titles.md).

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

Then open **`http://localhost:3000/`** (one book URL). Leave the preview terminal running.

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

**PDF** (needs LaTeX / latexmk; experimental):

```powershell
.\scripts\build_pdf.ps1
```

Helper scripts: [`scripts/`](scripts/). Config: [`myst.yml`](myst.yml). PDF details: [`docs/guides/site_hosting.md`](docs/guides/site_hosting.md). If a flag differs on your install, check `jupyter book --help`.

## Contributing

Collaborators and section editors are welcome. Start with [`book/100_front/contribute.md`](book/100_front/contribute.md) and [`CONTRIBUTING.md`](CONTRIBUTING.md) (DCO sign-off required). Governance: [`GOVERNANCE.md`](GOVERNANCE.md). Conduct: [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md). Credit: [`CONTRIBUTORS.md`](CONTRIBUTORS.md).

## Cite

See [`CITATION.cff`](CITATION.cff). Prefer a tagged release / Zenodo DOI once published; until then cite the site URL and note the public-preview version.

## License

© 2026 Albert Poulose.

| Material | License | Scope |
|----------|---------|-------|
| Book content | [CC BY-NC-SA 4.0](LICENSES/CC-BY-NC-SA-4.0.txt) | `book/`, `slides/`, `media/`, generated site and PDF |
| Teaching code | [MIT](LICENSES/MIT.txt) | `src/sciml_ps/`, `scripts/`, `tests/`, `templates/`, notebook code cells |

Others may share and adapt the content for **non-commercial** teaching with attribution under the same license. **Commercial** use of the content needs written permission. Contributions use the same licences via DCO. Student summary: [`book/100_front/license.md`](book/100_front/license.md). Full terms: [`LICENSE`](LICENSE).

## Single book

One site, one TOC. Routes by background and by role live in [`book/100_front/learning_paths.md`](book/100_front/learning_paths.md). Course I/II split folders are deferred.
