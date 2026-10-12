# Using, previewing, editing, and developing this resource over decades

This guide is for **instructors and maintainers** of the SciML_PS book repository. Student-facing navigation lives in `book/100_front/how_to_use.md`. Curriculum intent lives in [`../planning/SciML_for_Power_Systems_Course_Development_Report.md`](../planning/SciML_for_Power_Systems_Course_Development_Report.md).

---

## 1. What this repository is

| Layer | Path | Role |
|-------|------|------|
| Published book content | `book/` | MyST pages students read |
| Book config / TOC | `myst.yml` | Jupyter Book 2 site structure |
| Teaching code | `src/sciml_ps/` | Shared Python helpers for labs |
| Environments | `environment.yml`, `envs/` | Reproducible runtimes |
| Media / slides | `media/`, `slides/` | Figures, videos, downloadable decks |
| Planning (not the book) | `docs/planning/` | Course design report |
| Maintainer guides | `docs/guides/` | This file and future how-tos |

**Design locks**

- **One book, one TOC** — optional semester tracks go in `book/100_front/learning_paths.md`, not separate Course I/II trees.
- **Part IDs use 100-spacing** (`100`, `200`, `300`, …) so new pillars can be inserted for decades without renumbering neighbors.
- **Content policy** — portable SciML + power examples and public citations. Do **not** paste sealed research metrics, seed tables, or campaign YAML from research repos.

---

## 2. How to preview the contents

Student-facing copy of the same commands (part of the book TOC):

[`book/100_front/preview_locally.md`](../../book/100_front/preview_locally.md)

Helper scripts live in [`scripts/`](../../scripts/).

### 2.1 One-time setup

From the repository root:

```bash
conda env create -f environment.yml
conda activate sciml_ps
```

Windows PowerShell:

```powershell
.\scripts\setup_env.ps1
conda activate sciml_ps
```

If the environment already exists and dependencies changed:

```bash
conda env update -f environment.yml --prune
conda activate sciml_ps
```

Confirm the CLI and Node.js (JB2 requires Node on PATH; pinned via conda `nodejs` in `environment.yml`):

```bash
jupyter book --help
node --version
```

Jupyter Book 2 evolves; if a flag name differs on your install, trust `jupyter book --help` and the [official JB2 docs](https://jupyterbook.org/stable/get-started/init). On Windows consoles, prefer the helper scripts (they set `PYTHONUTF8=1`).

### 2.2 Live preview (preferred while editing)

From the repository root (where `myst.yml` lives):

```powershell
.\scripts\preview.ps1
```

```bash
./scripts/preview.sh
# or:
jupyter book start
```

Open the URL the CLI prints (typically `http://localhost:3000`). Edit a Markdown file under `book/`, save, and refresh to see changes.

### 2.3 Static HTML build

```powershell
.\scripts\build.ps1
```

```bash
./scripts/build.sh
# or:
jupyter book build
```

HTML output lands under a build directory (often `_build/` or as reported by the CLI). Open the generated `index.html` locally if you are not using `start`.

### 2.4 Labs that need ANDES

Use the dedicated env stub when you reach network labs:

```bash
conda env create -f envs/course_andes.yml
conda activate sciml_ps_andes
```

**Pin one ANDES version** in that file after a pilot. Never mix ANDES 1.10 and 2.0 in the same lab narrative or undocumented env.

### 2.5 Preview checklist

- [ ] `myst.yml` TOC paths resolve (no missing files)
- [ ] New pages appear in the sidebar after they are listed in `myst.yml`
- [ ] Math and links render on a sample foundations page
- [ ] Large videos are not forced into git (see `.gitignore`)

---

## 3. How to use this online resource

### 3.1 As a reader / student (once published)

1. Open the hosted site (GitHub Pages or other host — wire later).
2. Read [How to use this book](../../book/100_front/how_to_use.md) and the [book map](../../book/100_front/book_map.md).
3. Follow **Preparation → Foundations**, then deepen along Dynamics, Stability, or Identification.
4. Complete labs under `900_labs` as assigned.

Until hosting exists, use local preview (§2) as the “online” experience.

### 3.2 As an instructor shipping a semester

1. Keep this **single book**; fill `book/100_front/learning_paths.md` with week-by-week pointers.
2. Freeze env pins for that term (`envs/course_core.yml`, and ANDES if used).
3. Point students at the published URL + lab folders, not at research repos.
4. Treat `docs/planning/` as instructor-only curriculum memory unless you deliberately publish excerpts.

### 3.3 As a contributor browsing the repo

| Question | Go here |
|----------|---------|
| What is the course trying to teach? | `docs/planning/…Course_Development_Report.md` |
| What do students see? | `book/` |
| How is the site assembled? | `myst.yml` + this guide |
| Where do I put a new pillar? | §5 below |

---

## 4. How to edit contents

### 4.1 Edit an existing chapter

1. Open the Markdown file under `book/…`.
2. Prefer the sections in `book/chapter_template.md`: learning goals, reading, watch, slides, worked example, lab link, further reading, misconceptions.
3. Preview with `jupyter book start`.
4. Commit when the page is coherent (stubs may say “Status: stub”).

### 4.2 Add a new chapter inside an existing part

Example: new page in foundations.

1. Create `book/300_foundations/11_your_slug.md` (keep local numbering tidy).
2. Add the file to `myst.yml` under the Foundations `children:` list (order = sidebar order).
3. Link it from the part `overview.md` if useful.
4. Preview and fix broken links.

### 4.3 Add or change a lab

1. Add or edit `book/900_labs/lab_XX_slug/index.md`.
2. Register it in `myst.yml` under Laboratories.
3. Cross-link from the relevant chapter(s).
4. Put executable notebooks beside `index.md` when ready (for example `notebook.ipynb`), and document the env in the lab page.

Assessed labs in the planning report are Lab 1–5. Prefer extending those before inventing Lab 6+.

### 4.4 Add slides or media

| Asset | Location | Notes |
|-------|----------|--------|
| Slides PDF/PPTX | `slides/` | Link from the chapter “Slides” section |
| Figures | `media/figures/` | Prefer SVG/PNG; commit small files |
| Videos | `media/videos/` | Keep large binaries out of git; host externally or LFS later; `.gitignore` already ignores common video extensions |

### 4.5 Change site title or global metadata

Edit the `project:` block in `myst.yml` (title, description, keywords). Do not duplicate a second TOC elsewhere.

### 4.6 Shared teaching code

Add helpers under `src/sciml_ps/` and import them from lab notebooks. Keep course code here; do not copy sealed research packages wholesale.

### 4.7 Editing rules that prevent decay

- **No research metrics** in student-facing pages (errors, CCT tables, bakeoff ranks from private campaigns).
- **Name estimands explicitly** — teaching Lab 3 is classical \((H, D)\); converter GFM knobs are a different elective story.
- **Cite public literature** using report biblio IDs (B#, R#, P#, S#) where possible.
- **One ANDES pin per lab** when simulator labs appear.
- Prefer **relative paths** in Markdown links.

---

## 5. How to develop this continuously over decades

### 5.1 Durable architecture (do not casually undo)

```text
100_front → 200_prep → 300_foundations
                            ├─→ 400_dynamics  ─┐
                            ├─→ 500_stability ─┼─→ 700_advanced
                            └─→ 600_identification ┘
                            └─→ 900_labs (cross-linked)
990_reference (reading list, notation)
```

After foundations exist, grow **400 / 500 / 600 in parallel**. That is the long-term scaling path.

### 5.2 Inserting a new major part (100-spacing)

Need a new pillar between foundations and dynamics? Create `book/350_network_daes/` (example), add an overview page, wire it in `myst.yml`, and update the book map. Neighbors `300` and `400` stay put.

Reserved-style examples (optional future IDs):

| ID band | Example use |
|---------|-------------|
| `250_…` | Extra software / tooling prep |
| `350_…` | Network DAEs before deeper dynamics |
| `550_…` | Energy-function / classical TSA depth |
| `650_…` | PMU / measurement contracts |
| `800_…` | Still free for a future major pillar |
| `900` / `990` | Labs and reference — keep these roles stable |

### 5.3 Cadence that survives many years

| Cadence | Action |
|---------|--------|
| Every edit | Preview locally; keep TOC in sync |
| Each filled chapter | Link lab + reading; remove “empty stub” claims when false |
| Each semester offering | Freeze env pins; update `learning_paths.md`; tag a git release (for example `offering-20XX-spring`) |
| When methods age | Add a new chapter or part; deprecate by moving prose to an `archive/` note or marking “historical” — avoid silent rewrites of learning history |
| Every few years | Re-pilot ANDES/PyTorch pins; refresh JB2; re-check external URLs in the reading list |

### 5.4 What to grow first (practical order)

1. `200_prep` notebooks + diagnostic  
2. Early `300_foundations` + `lab_01`  
3. Either `lab_02` (forward SciML) or `lab_03` (identification), then `lab_05` (stability)  
4. Deepen `400` / `500` / `600` stubs into real chapters  
5. Hosting (GitHub Actions → Pages) and first slides/videos  
6. `700_advanced` only after the core labs run cleanly  

### 5.5 Git and release hygiene

- Commit in small topical chunks (one chapter, one lab, or config-only).
- Never commit secrets, huge videos, or research `runs/` dumps.
- Tag offerings so old classes can pin a commit even as the book evolves.
- Prefer branches for experimental pedagogy; merge when the TOC and env still build.

### 5.6 Relationship to research repositories

Research code (parameter estimation, TSA campaigns, TEF baselines) is **instructor memory**, not the student book.

| Do | Do not |
|----|--------|
| Re-implement a clean teaching SMIB or cite public papers | Copy sealed experiment folders into `book/` |
| Rephrase methods you understand | Paste figures with unpublished numbers |
| Point advanced readers to public benchmarks when licensed | Mix Estimation “Paper 1” labels with ANDES-repo “Paper A/B₁” in student prose without explanation |

### 5.7 Hosting later (not required for local preview)

When ready to publish:

1. Add CI that runs `jupyter book build` on the default branch.  
2. Deploy the HTML artifact to GitHub Pages or equivalent.  
3. Put the public URL in the root `README.md` and in `book/100_front/how_to_use.md`.  

Until then, local `jupyter book start` is the preview path.

---

## 6. Quick reference

| Task | Command / place |
|------|-----------------|
| Preview | `.\scripts\preview.ps1` or `jupyter book start` |
| Build HTML | `.\scripts\build.ps1` or `jupyter book build` |
| Preview page in book | `book/100_front/preview_locally.md` |
| Edit prose | `book/**/*.md` |
| Edit TOC | `myst.yml` |
| Chapter shape | `book/chapter_template.md` |
| Lab stubs | `book/900_labs/` |
| Env pins | `environment.yml`, `envs/` |
| Curriculum intent | `docs/planning/…Report.md` |
| Student “how to read” | `book/100_front/how_to_use.md` |

---

## 7. When this guide should be updated

Update this file when you change the engine (for example Quarto migration), the part-numbering rules, the lab set, the env workflow, or the hosting URL. Keep it short enough that a future you can skim it in one sitting.
