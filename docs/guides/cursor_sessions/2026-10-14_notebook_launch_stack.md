# 2026-10-14 — Notebook launch stack (pre-public)

## Policy (locked)

| Priority | Path | Role |
|----------|------|------|
| 1 | Local install from `SciML_PS` | Canonical — assessed work, decades survival |
| 2 | Binder (`binder/`) | Primary online launch |
| 3 | Google Colab | Secondary convenience |

Thebe / JupyterLite / Codespaces: out of scope this pass.

## What landed

| Item | Path |
|------|------|
| Student Binder env | `binder/environment.yml`, `binder/postBuild`, `binder/README.md` (no JB/Node/ANDES) |
| Student guide | `book/100_front/running_notebooks.md` (under-dev warning + contribute invite) |
| TOC | `myst.yml` after `preview_locally.md` |
| Lab badges | Labs 1 and 3 Materials; Lab 5 notes SMIB badges later + ANDES local-only; Labs 2/4 stubs point to the guide |
| Notebook setup | Lab 1 / Lab 3 first cells: local `src` or `pip install` from GitHub |
| Docs | `how_to_use.md`, prep overview, outline, book_map, ROADMAP v0.1, CONTRIBUTING, CHANGELOG |

## Constraint

Binder and Colab “Open from GitHub” need a **public** repo. Until `phase2_go_public.ps1` succeeds, use local install only.

## Post-public click-test (owner)

1. Open Lab 1 Binder badge once; wait for first image build; confirm `import sciml_ps`.
2. Open Lab 1 Colab badge once; run setup cell; confirm imports.
3. Fix `binder/` or setup cells if either fails.
4. First Binder builds can take several minutes (already stated on the student page).

## Not committed in this session note alone

Commit when the user asks.
