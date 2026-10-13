# Session — ANDES content strategy for SciML_PS

**Date:** 2026-10-13  
**Repo:** SciML_PS  
**Scope:** Implement ANDES summarize-then-link strategy (SMIB first; Kundur gallery as preferred network case)  
**Commits:** `a546034` (bridge + wiring), `aaadda5` (pin + notebook + helper)

Canonical maintainer rule + full inventory: [`../andes_content_strategy.md`](../andes_content_strategy.md) § Implementation inventory.

## Delivered

### New

- Student bridge: [`../../book/500_stability/03_andes_network_reference.md`](../../../book/500_stability/03_andes_network_reference.md) (in `myst.yml` Stability TOC)
- Notebook: [`../../book/900_labs/lab_05_stability_cct/lab05_network_cct_andes.ipynb`](../../../book/900_labs/lab_05_stability_cct/lab05_network_cct_andes.ipynb)
- Helper: [`../../src/sciml_ps/andes_cct.py`](../../../src/sciml_ps/andes_cct.py)
- Env: [`../../envs/course_andes.yml`](../../../envs/course_andes.yml) pinned **`andes==2.0.0`** (local Kundur PFlow/TDS smoke OK; run `andes prep` once if needed)

### Book pages updated (hooks)

| Part | Path |
|------|------|
| Front | `book/100_front/how_to_use.md`, `book_map.md` |
| Foundations | `book/300_foundations/06_forward_pinn.md` |
| Dynamics | `book/400_dynamics/overview.md` |
| Stability | `book/500_stability/overview.md` (+ new `03_…`) |
| Advanced | `book/700_advanced/overview.md` |
| Labs | `lab_02` index, `lab_05` index, `900_labs/README.md` |
| Reference | `book/990_reference/reading_list.md` (S1 / S1a) |

### Maintainer docs touched

- [`../andes_content_strategy.md`](../andes_content_strategy.md)
- [`../lab_spine_policy.md`](../lab_spine_policy.md), [`../using_preview_edit_and_long_term_development.md`](../using_preview_edit_and_long_term_development.md) §2.4, [`../future_plans_online_resource.md`](../future_plans_online_resource.md), [`../README.md`](../README.md)

## Still optional later

- Broader bus-wise heatmap (use official [CCT gallery](https://docs.andes.app/en/stable/gallery/critical-clearing-time.html); do not paste)
- Surrogate-in-the-loop network CCT after Lab 2 exists

## Policy reminders

- Still exactly five assessed labs (Kundur path = Lab 5 extension only)
- Gallery items link-out by pillar story; RL/FO not core spines
- Summarize in `book/`; detail on docs.andes.app
