# Session: SciML_PS content development plan

**Date:** 2026-10-13  
**Repo:** `SciML_PS`  
**Scope:** Implement content-development plan Phases 0–E (prose-first; no plan-file edits).

## Delivered

| Phase | Outcome |
|-------|---------|
| 0 | `docs/guides/vault_import_map.md` + guides README link |
| A | `book/300_foundations/` chapters 00–10 filled; landscape page; overview outcomes |
| B | `src/sciml_ps/smib.py` + Lab 1 notebook; cross-link from foundations §03 |
| C | `book/600_identification/` depth + Lab 3 notebook; `500_stability` seed + Lab 5 narrative |
| D | `book/200_prep/` notebook stubs; Portable LaTeX author guide |
| E | Feedback page + navbar action; Typst PDF stub in `myst.yml`; CI `build-book.yml`; `site_hosting.md`; `portal/20XX-term/` |

## Explicitly deferred

- Live Google Form URL, GitHub Pages deploy, polished full-book PDF
- Lab 2 / full inverse-PINN Lab 3 / executable Lab 5 ANDES CCT
- Lessons 07–12 Mode A/B/C bakeoff; research experiment IDs

## Later same day — student chrome vs folder IDs

Removed student-facing **Folder** columns and bare part IDs from book overviews / how-to-use / labs index; provenance stays in maintainer guides. Canonical rule: [`../naming_and_titles.md`](../naming_and_titles.md) § Student chrome vs repo paths.

## Later same day — home landing polish (Wealthfolio UX, JB2 stack)

Rewrote [`book/index.md`](../../../book/index.md): newcomer CTA, slim three-application bullets, Explore `{grid}`/`{card}` tiles, short live-vs-PDF note. Full “what you produce” table moved to book map. Pattern locked in [`../future_plans_online_resource.md`](../future_plans_online_resource.md) §1b (borrow UX, not product-docs tooling).

## Verify

- `python -c "from sciml_ps import simulate_smib"` smoke OK
- Preview: `scripts/preview.ps1` (Node.js + `HOST=localhost`; one URL `http://localhost:3000/`)
