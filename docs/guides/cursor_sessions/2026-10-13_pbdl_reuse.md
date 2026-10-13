# Session — PBDL reuse into SciML for PS

**Date:** 2026-10-13  
**Repo:** SciML_PS (writable). PBDL (`tum-pbs/pbdl-book`) read-only external source.  
**Plan:** PBDL reuse into SciML_PS (cite-don't-copy; application-led TOC kept).

## License finding

PBDL repository `LICENSE` is Apache-2.0 at commit `45d2b65` (checked 2026-10-13). No upstream `NOTICE` file. Local copy and provenance header: `LICENSES/PBDL-Apache-2.0.txt`. Nothing from PBDL was copied verbatim; every use is `idea-cited`.

## Delivered

| Item | Path |
|------|------|
| Attribution register (PBDL-01…07, ANDES, DeepXDE) | `docs/references/attribution_register.md` |
| Reuse map, tiers, Apache checklist | `docs/guides/pbdl_reuse_map.md` |
| LICENSE third-party paragraph; report §13.1 PBDL row | `LICENSE`, `docs/planning/…Course_Development_Report.md` |
| Physics-coupling ordering (own Mermaid + table) | `book/300_foundations/00_sciml_landscape.md` |
| Physics-loss strengths and limits | `book/300_foundations/06_forward_pinn.md`, `09_inverse_pinn.md` |
| Gradient scaling (angle vs speed, log-parameters) | `book/300_foundations/05_differentiation.md` |
| New page: differentiable simulation | `book/600_identification/03_differentiable_simulation.md` (TOC after `02_physical_vs_equivalent`) |
| Differentiable RK4 SMIB rollout | `src/sciml_ps/smib_torch.py` (not imported by `sciml_ps/__init__` so torch stays optional) |
| Parity and gradient tests | `tests/test_smib_torch.py` |
| Lab 3 optional DP fit + held-out check | `scripts/_write_lab03_nb.py` → `lab03_inertia_damping_id.ipynb` |
| Pillar Discussion sections | `book/400_dynamics/overview.md`, `500_stability/overview.md`, `600_identification/overview.md` |
| Model reduction pointer; Advanced fast-forward topics | `book/400_dynamics/overview.md`, `book/700_advanced/overview.md` |
| B5 per-chapter map | `book/990_reference/reading_list.md` |
| Optional deps | `pyproject.toml` (`torch`, `dev`) |

## Verification

- `pytest tests/test_smib_torch.py`: 4 passed. RK4 (`dt = 2e-3`) vs SciPy reference: max angle gap about 2e-5 rad, max speed gap about 5e-4 rad/s.
- Lab 3 notebook code ran end to end; differentiable-simulation fit recovered the synthetic $(H, D)$ close to truth, with lower held-out speed error than the coarse grid estimate.
- HTML build: no content warnings; anchors `#gradient-scaling` and `#strengths-and-limits-of-physics-losses` resolve. All 13 linked PBDL URLs return 200.
- PDF build: new pages present. The Mermaid diagram is **not** rendered in PDF (MyST has no LaTeX conversion for `mermaid`); the table below it carries the same content.

## Environment note

The `sciml_ps` conda env currently has no `torch` although `envs/course_core.yml` lists `pytorch`. Verification used the `pinn_andes_2.0` env (Python 3.11, torch). Re-sync `sciml_ps` from `envs/course_core.yml` (plus `pytest`) before students run the Lab 3 option.

## Deferred

- Real adapted PBDL code: none yet; checklist in `pbdl_reuse_map.md` applies when it happens.
- Probabilistic UQ and graph models: Advanced pointers only.
- Book prose license: **chosen** (CC BY-NC-SA 4.0 content + MIT code; see root `LICENSE`). The attribution register still keeps third-party terms decoupled.
