# Vault → SciML_PS import map

**Audience:** Maintainers.  
**Recorded:** 2026-10-13.  
**Policy:** Adapt into MyST teaching prose. Do not paste vault frontmatter, Paper 1 metrics, or research `runs/`.  
**Vault root:** `maintainer's local Obsidian vault (path not recorded in this public repo)`

Science scope stays locked in [`scope_lock_three_pillars.md`](scope_lock_three_pillars.md). Curriculum outcomes stay in [`../planning/SciML_for_Power_Systems_Course_Development_Report.md`](../planning/SciML_for_Power_Systems_Course_Development_Report.md).

**Student chrome:** Do not put vault lesson IDs, “Content sources (authors)”, or repo folder columns on published `book/` pages. Provenance stays in this map; public labels follow [`naming_and_titles.md`](naming_and_titles.md) § Student chrome vs repo paths.

---

## COPY / promote first (rewrite into book or guides)

| Vault path | SciML_PS target | Notes |
|------------|-----------------|-------|
| `08-Teaching/PINN Teaching Index (Beginner Curriculum).md` | Foundations reading order; `book/300_foundations/overview.md` | Retitle off “Paper 1” |
| `08-Teaching/PINN Fundamentals — Beginner Lessons 01-06.md` | `book/300_foundations/01`–`09` (see table below) | Core PINN language |
| `01-Concepts/State versus Parameter Estimation.md` | Folded into `01_problem_framing`, `07`/`09` | Atomic concept |
| `01-Concepts/Inverse PINN.md` | `09_inverse_pinn.md` | |
| `01-Concepts/PINN Data and Physics Losses.md` | `06_forward_pinn.md`, `09_inverse_pinn.md` | |
| `01-Concepts/Forward PINN Trajectory Surrogate for TSA.md` | Seed `500_stability/02_surrogate_stability.md` | |
| `01-Concepts/Critical Clearing Time.md` | Seed `500_stability/01_stability_and_cct.md` | |
| `01-Concepts/Physical versus Equivalent Parameters.md` | Seed `600_identification` honesty box | |
| `00-MOCs/SciML Families for Power System TSA.md` | `book/300_foundations/00_sciml_landscape.md` or `990` / short landscape page | Trim career links |
| `04-Methods/Portable LaTeX Equations Across Obsidian and Manuscripts.md` | `docs/guides/portable_latex_equations.md` | Authors only |

### Lessons 01–06 → foundations pages

| Lesson theme | Book page |
|--------------|-----------|
| What problem are we solving? | `01_problem_framing.md` |
| State vs parameter | `01_problem_framing.md` (+ reminders in `07`, `09`) |
| Forward vs inverse | `01_problem_framing.md`, `06`, `09` |
| PINN pieces / losses | `06_forward_pinn.md` |
| Where parameters enter training | `09_inverse_pinn.md` |
| Two research repos (teaching rewrite) | Replace with “three pillars + labs” map in overview — **do not** copy personal repo status |

SMIB / Lab 1 / classical LS content comes primarily from the **course planning report**, not the vault lessons.

---

## ADAPT later (not Phase A verbatim)

| Vault path | Later target | Notes |
|------------|--------------|-------|
| Lessons 07–12 (Paper 1 Path) | Elective under `600` / `700` | Strip gates, Mode A bakeoff numbers |
| Lessons 13–16 (ANDES, TSA, judgement) | `500`, Lab 5 narrative | De-personalize |
| Hybrid PCC / GFM-GFL concepts and methods | Converter elective | |
| `MOC-PINNs-SciML`, PE/TSA/GFM MOCs | TOC ideas only | |
| Structural / disturbance-dependent identifiability | Deepen `08_identifiability.md` | Shorten for course |
| Synthetic Reduced-Order Recovery Check | Lab protocol later | |
| Career SciML TSA review outline | Optional grad landscape | |

---

## KEEP in vault only

| Vault path | Why |
|------------|-----|
| `08-Teaching/How I Use This Vault…` | Personal Cursor↔Obsidian workflow |
| `06-Project-Maps/*` | Research repo indexes |
| `11-Weekly` / `12-Daily` | Personal journals |
| Findings / evidence ledgers | Research promotion gate |
| Lyapunov / digital twins / PMU MOCs | Outside three-pillar core for now |

---

## Import status checklist

- [x] This map created
- [x] Phase A: foundations chapters filled from Lessons 01–06 + report
- [x] Phase B: Lab 1 executable
- [x] Phase C: identification + Lab 3; stability seeds
- [x] Phase D: prep notebooks + landscape + Portable LaTeX guide
- [x] Phase E: site product scaffold (feedback page, CI build, PDF export stub, portal term template); Pages/Form URL still open
