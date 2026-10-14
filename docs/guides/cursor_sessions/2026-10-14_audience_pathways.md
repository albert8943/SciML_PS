# 2026-10-14 — Two-community audience pathways

## Intent

One book, many entrances. Machine-learning readers and power-systems readers, including complete beginners, can open any chapter. Students, teachers, practitioners, and researchers each have a route.

## What landed

| Item | Path |
|------|------|
| Chooser | `book/100_front/start_here.md` (background × role) |
| Bridge primers (Draft) | `book/200_prep/bridge_programming_from_zero.md`, `bridge_power_systems_for_ml.md`, `bridge_ml_for_power_systems.md` |
| First lab, text only | `book/100_front/first_lab_walkthrough.md` (Colab, Binder, local Windows/Mac) |
| Two-way glossary | `book/990_reference/glossary.md` (35 terms; linked from notation) |
| Routes | `book/100_front/learning_paths.md` (replaces the stub) |
| Before you start | Chapter template plus Foundations, Dynamics, Stability, Identification, Advanced, and Labs 1–5 |
| Intros | Home, how to use, advice (retitled Advice to readers), prep overview, foundations overview, contribute |
| Wiring | `myst.yml` TOC and a Start here navbar action; outline Needs column; book map; README; CHANGELOG; ROADMAP v0.1 and v0.5; CONTRIBUTING |

`scripts/check_book.py` warns when a chapter, pillar, or lab page has no Before you start box. Missing boxes do not fail the check.

## Checks

- `python scripts/check_book.py`: 56 TOC pages, 16 bib entries, 0 errors, 0 warnings.
- `jupyter book build --html`: 56 pages. `/start-here` returned 200. Heading anchors `path-teachers`, `path-practitioners`, and `glossary-machine` are in the HTML.

## Still uncommitted in this working tree

This pathways work, and the earlier notebook launch stack (`binder/`, `running_notebooks.md`, lab badges). Commit when asked.

## Later (ROADMAP v0.5)

Grow the glossary and the three primers with collaborators from both fields. Week counts on the teacher overlays stay blank until an institution schedules a term.
