# How to use this book

## What this is

A Jupyter Book 2 / MyST computational textbook scaffold for SciML in power systems. Pages follow a common pattern (goals → reading → media → example → lab → misconceptions). See `book/chapter_template.md`.

## Suggested order

1. Complete the preparation overview (`200_prep`).
2. Work through foundations (`300_foundations`) before specializing.
3. Deepen along dynamics (`400`), stability (`500`), or identification (`600`) in any order after foundations.
4. Use laboratories (`900_labs`) as assessed practicals.

## Software

- Core Python stack: `envs/course_core.yml`
- ANDES labs: `envs/course_andes.yml` (pin one version; pilot before class)

## Preview the book on your machine

Step-by-step commands and helper scripts:

→ [Preview this book locally](preview_locally.md)

Short path (Windows):

```powershell
.\scripts\setup_env.ps1
conda activate sciml_ps
.\scripts\preview.ps1
```

Then open `http://127.0.0.1:3000/` and leave that terminal running.

## What not to expect yet

Stub pages are intentional. Executed labs, full slide decks, and videos arrive in later passes.

## For instructors and maintainers

Previewing, editing chapters, wiring the TOC, and growing parts over many years is documented in the git repo under the `docs/guides/` folder (maintainer handbook; not a book page).
