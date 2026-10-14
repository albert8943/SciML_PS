# Laboratories

```{note} Maturity: Draft
Readable teaching prose; examples, figures, and exercises are still growing. See [Status and versions](../100_front/status_and_versions.md) and [Join and contribute](../100_front/contribute.md).
```

Five assessed laboratories aligned to the course plan. This **is** the full lab set for SciML for PS — we deepen these rather than adding Lab 6+.

| Lab | Topic | Status |
|-----|-------|--------|
| 1 | [Reference simulation and scientific dataset](lab_01_reference_sim/index.md) | Notebook + `sciml_ps.smib` helper |
| 2 | [Surrogate versus PINN](lab_02_surrogate_vs_pinn/index.md) | Brief only (after Lab 1) |
| 3 | [Inertia and damping estimation](lab_03_inertia_damping_id/index.md) | LS + loss-surface notebook; PINN template |
| 4 | [Learned dynamics generalization](lab_04_learned_dynamics/index.md) | Brief only |
| 5 | [Stability and CCT](lab_05_stability_cct/index.md) | Protocol ready; SMIB path + optional [Kundur/ANDES notebook](lab_05_stability_cct/lab05_network_cct_andes.ipynb) |

Install helpers from the repository root: `pip install -e .`

How to run notebooks (local = canonical; Binder = primary online; Colab = secondary): [Running notebooks](../100_front/running_notebooks.md). Online launch is under development and needs a public GitHub repo; contributions welcome via [Join and contribute](../100_front/contribute.md).

Suggested path when building the course: get **Lab 1** solid, then **Lab 3**, then **Lab 5**; fill **2** and **4** after those run.

Books, simulators, and optional external packages live under [Reference — Reading list](../990_reference/reading_list.md), not as a second lab menu.
