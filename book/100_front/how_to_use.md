# How to use this book

## What this is

A Jupyter Book 2 / MyST computational textbook for **Scientific Machine Learning (SciML) for Power Systems (PS)** — short form **SciML for PS**. Focus: dynamic modeling, stability assessment, and system identification. Maintained by **Albert Poulose** for teaching and research training. The notes are written so machine-learning readers and power-systems readers can enter at their own level, including readers who are new to both. Pages follow a common pattern (goals → reading → media → example → lab → misconceptions).

## You can enter anywhere

[Start here](start_here.md) asks two questions (your background, your role) and links to a route. You may also open the [full outline](outline.md) and jump to a chapter.

Three things make that safe:

- **Before you start** on each chapter names what the page assumes, with a hint for ML readers, a hint for power-systems readers, and a hint if both are new.
- The [glossary](../990_reference/glossary.md) gives the plain meaning, the power-systems reading, and the ML reading of the same word. [Notation](../990_reference/notation.md) is the symbol table.
- [Learning paths](learning_paths.md) writes the routes out in order, including what you can skip.

The sidebar order (Preparation, then Foundations, then Dynamics, Stability, or Identification) is one useful route. It is the `path_core` overlay for a first course. It is optional if your background already covers part of it.

## How SciML methods appear

These notes are organized by **power-system question**, not by a catalogue of architectures.

1. Name the engineering question: [Dynamics](../400_dynamics/overview.md), [Stability](../500_stability/overview.md), or [Identification](../600_identification/overview.md).
2. Use the same plant: [Lab 1](../900_labs/lab_01_reference_sim/index.md) (and Foundations SMIB chapters).
3. Keep a classical or supervised baseline, then meet an early physics-informed path: residual / inverse PINN in Labs 2–3.
4. Meet other families when the same plant needs them — Neural ODEs and operators in [Lab 4](../900_labs/lab_04_learned_dynamics/index.md), differentiable simulation under Identification, frontiers under [Advanced](../700_advanced/overview.md). They do not get a second table of contents.
5. Keep five assessed labs. New methods deepen Labs 1–5 or sit in Advanced; they do not become Lab 6.

Family map: [SciML method families](../300_foundations/00_sciml_landscape.md). Practice table: [Laboratories](../900_labs/README.md).

:::{tip} Browser
Prefer **Google Chrome**, **Microsoft Edge**, or another Chromium-based browser for the live notes. Interactive figures and long pages scroll more reliably there than in Safari.
:::

## If you are new to programming

Use [Programming from zero](../200_prep/bridge_programming_from_zero.md) and [Your first lab](first_lab_walkthrough.md). That walkthrough runs Lab 1 in the browser. Install nothing until you want a copy on your own computer.

## Software

For a local copy of the labs (the canonical path once you are past the browser walkthrough):

- Core Python stack: `envs/course_core.yml` (Labs 1–5 default). Setup steps: [Running notebooks](running_notebooks.md).
- Network / ANDES path (after SMIB CCT): `envs/course_andes.yml` — see [ANDES as network reference](../500_stability/03_andes_network_reference.md)

## Preview the book on your machine

Step-by-step commands and helper scripts, for people who want the HTML site locally:

→ [Preview this book locally](preview_locally.md)

Short path (Windows):

```powershell
.\scripts\setup_env.ps1
conda activate sciml_ps
.\scripts\preview.ps1
```

Then open [http://localhost:3000/](http://localhost:3000/) and leave that terminal running.

Running a single lab notebook is a smaller job than previewing the whole site. Beginners should use [Your first lab](first_lab_walkthrough.md) first.

## What not to expect yet

This book is a **public preview v0.1** (v0.x series) and remains **under development until v1.0**. Stub pages and thin [Preparation](../200_prep/overview.md) notebooks in the sidebar are intentional. Prefer the live HTML site over the experimental PDF. Version labels: [Status and versions](status_and_versions.md). How to run lab notebooks (local = canonical; Binder = primary online; Colab = secondary): [Running notebooks](running_notebooks.md).

:::{tip} PDF download
The navbar **PDF** control opens a snapshot of the notes in a **new browser tab**, built each time the site is published. It may lag slightly behind the HTML pages. Treat the export as experimental. If you preview the book locally, see [Preview this book locally](preview_locally.md) for rebuilding the PDF.
:::

:::{warning} Prefer the live site for labs
For executable laboratories and notebooks, use the HTML book and [Running notebooks](running_notebooks.md), not the PDF snapshot.
:::

## Feedback and collaboration

See [Feedback](feedback.md) (GitHub issues for now; Google Form planned). To help improve the notes, translate a term into the other field, or express interest as a reviewer/section editor: [Join and contribute](contribute.md). Neighbors and positioning: [Related open resources](related_resources.md).

## License

Book content is **CC BY-NC-SA 4.0** (free to share and adapt for non-commercial teaching with credit). Teaching code is **MIT**. Full terms: [License](license.md).

## For instructors and maintainers

Course overlays live on [Learning paths](learning_paths.md#path-teachers). Previewing, editing chapters, wiring the TOC, and growing parts over many years is documented in the git repo under the `docs/guides/` folder (maintainer handbook; not a book page). Hosting/PDF notes: `docs/guides/site_hosting.md`. Legal checklist: `docs/guides/legal_and_licensing_considerations.md`. Governance: root `GOVERNANCE.md`.
