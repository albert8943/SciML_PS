# How to use this book

## What this is

A Jupyter Book 2 / MyST computational textbook for **Scientific Machine Learning (SciML) for Power Systems (PS)** — short form **SciML for PS**. Focus: dynamic modeling, stability assessment, and system identification. Maintained by **Albert Poulose** for teaching and research training. Pages follow a common pattern (goals → reading → media → example → lab → misconceptions).

## Suggested order

**New here?** After this page, go to [Preparation](../200_prep/overview.md), then [Foundations](../300_foundations/overview.md). The [home page](../index.md) also has Explore cards into Getting started, Foundations, Laboratories, and Reference.

1. Complete [Preparation](../200_prep/overview.md).
2. Work through [Foundations](../300_foundations/overview.md) before specializing.
3. Deepen along [Dynamics](../400_dynamics/overview.md), [Stability](../500_stability/overview.md), or [Identification](../600_identification/overview.md) in any order after foundations.
4. Use [Laboratories](../900_labs/README.md) as assessed practicals.

Use the left sidebar to move around. On a hosted site, use the theme search box when available; locally, sidebar titles plus browser find (`Ctrl+F` / `Cmd+F`) are enough.

:::{tip} Browser
Prefer **Google Chrome**, **Microsoft Edge**, or another Chromium-based browser for the live notes. Interactive figures and long pages scroll more reliably there than in Safari.
:::

## Software

- Core Python stack: `envs/course_core.yml` (Labs 1–5 default)
- Network / ANDES path (after SMIB CCT): `envs/course_andes.yml` — see [ANDES as network reference](../500_stability/03_andes_network_reference.md)

## Preview the book on your machine

Step-by-step commands and helper scripts:

→ [Preview this book locally](preview_locally.md)

Short path (Windows):

```powershell
.\scripts\setup_env.ps1
conda activate sciml_ps
.\scripts\preview.ps1
```

Then open [http://localhost:3000/](http://localhost:3000/) and leave that terminal running.

## What not to expect yet

This book is a **public preview (v0.x)** under active development. Stub pages and thin [Preparation](../200_prep/overview.md) notebooks in the sidebar are intentional. Filled labs, full slide decks, videos, and Colab/Binder launch buttons arrive in later passes. Prefer the live HTML site over the experimental PDF. Version labels: [Status and versions](status_and_versions.md).

:::{tip} PDF download
The navbar **PDF** control opens a snapshot of the notes in a **new browser tab**, built each time the site is published. It may lag slightly behind the HTML pages. Treat the export as experimental. If you preview the book locally, see [Preview this book locally](preview_locally.md) for rebuilding the PDF.
:::

:::{warning} Prefer the live site for labs
For executable laboratories and notebooks, use the HTML book (or Binder/Colab later), not the PDF snapshot.
:::

## Feedback and collaboration

See [Feedback](feedback.md) (GitHub issues for now; Google Form planned). To help improve the notes or express interest as a reviewer/section editor: [Join and contribute](contribute.md). Neighbors and positioning: [Related open resources](related_resources.md).

## License

Book content is **CC BY-NC-SA 4.0** (free to share and adapt for non-commercial teaching with credit). Teaching code is **MIT**. Full terms: [License](license.md).

## For instructors and maintainers

Previewing, editing chapters, wiring the TOC, and growing parts over many years is documented in the git repo under the `docs/guides/` folder (maintainer handbook; not a book page). Hosting/PDF notes: `docs/guides/site_hosting.md`. Legal checklist: `docs/guides/legal_and_licensing_considerations.md`. Governance: root `GOVERNANCE.md`.
