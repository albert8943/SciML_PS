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

Stub pages are intentional. Executed labs, full slide decks, and videos arrive in later passes.

:::{tip} PDF download
The navbar **PDF** control opens the last built file in a **new browser tab** (`http://localhost:3100/exports/sciml_ps_notes.pdf` during local preview) so the notes stay on `http://localhost:3000/`. It does **not** regenerate on click. After content changes, run `scripts/build_pdf.ps1` or `scripts/build_pdf.sh` (needs LaTeX), then hard-refresh the PDF tab in **Chrome/Edge**. Treat the export as experimental.
:::

:::{warning} Prefer the live site for labs
For executable laboratories and notebooks, use the HTML book (or Binder/Colab later), not the PDF snapshot.
:::

## Feedback

See [Feedback](feedback.md) (GitHub issues for now; Google Form planned).

## License

Book content is **CC BY-NC-SA 4.0** (free to share and adapt for non-commercial teaching with credit). Teaching code is **MIT**. Full terms: [License](license.md).

## For instructors and maintainers

Previewing, editing chapters, wiring the TOC, and growing parts over many years is documented in the git repo under the `docs/guides/` folder (maintainer handbook; not a book page). Hosting/PDF notes: `docs/guides/site_hosting.md`. Legal checklist: `docs/guides/legal_and_licensing_considerations.md`.
