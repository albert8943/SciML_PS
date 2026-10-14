# Lab 3 — Inertia and damping estimation

```{note} Maturity: Draft
Readable teaching prose; examples, figures, and exercises are still growing. See [Status and versions](../../100_front/status_and_versions.md) and [Join and contribute](../../100_front/contribute.md).
```

:::{tip} Before you start
**Needs:** [Lab 1](../lab_01_reference_sim/index.md), [classical estimation](../../300_foundations/07_classical_estimation.md), [identifiability](../../300_foundations/08_identifiability.md), and [inverse PINNs](../../300_foundations/09_inverse_pinn.md) | **Coming from ML:** H and D are named parameters with bounds, separate from network weights | **Coming from power systems:** least squares beside an inverse PINN on the same records | **New to both:** read the [ML primer](../../200_prep/bridge_ml_for_power_systems.md) and finish Lab 1
:::

## Goals

Compare **simulation-based least squares** with an **inverse PINN** (or collocation residual estimator) on the same measurements and bounds. Vary noise, window length, and excitation. Plot a two-parameter loss surface or local sensitivity diagnostic. Test fitted $(H,D)$ on another disturbance.

## Teaching estimands

Classical SMIB **inertia and damping** $(H, D)$. Do not silently substitute research GFM converter knobs.

## Prerequisites

- [Lab 1](../lab_01_reference_sim/index.md) completed  
- Chapters: [classical estimation](../../300_foundations/07_classical_estimation.md), [identifiability](../../300_foundations/08_identifiability.md), [inverse PINN](../../300_foundations/09_inverse_pinn.md), [physical vs equivalent](../../600_identification/02_physical_vs_equivalent.md)

## Materials

```{note} Under development
Online launch (Binder / Colab) is a public-preview convenience and may change.
Canonical path: local install. Help improve these paths: [Join and contribute](../../100_front/contribute.md). Full guide: [Running notebooks](../../100_front/running_notebooks.md).
```

- Starter notebook: [`lab03_inertia_damping_id.ipynb`](lab03_inertia_damping_id.ipynb) · [Running notebooks](../../100_front/running_notebooks.md)
- [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/albert8943/SciML_PS/master?filepath=book/900_labs/lab_03_inertia_damping_id/lab03_inertia_damping_id.ipynb) · [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/albert8943/SciML_PS/blob/master/book/900_labs/lab_03_inertia_damping_id/lab03_inertia_damping_id.ipynb)
- Simulator: `sciml_ps.simulate_smib` (same classical SMIB as Lab 1)
- Optional differentiable rollout: `sciml_ps.smib_torch.rollout_smib` (needs `torch`; install with `pip install -e ".[torch]"` locally)

Local (canonical): `conda activate sciml_ps` → `pip install -e .` → open the notebook. Binder/Colab need the **public** GitHub repo.

## Protocol

1. Generate a “truth” trajectory with known $(H^\star, D^\star)$ and additive noise on $\omega$  
2. Grid or optimize LS loss vs $(H,D)$ with documented bounds  
3. Train inverse PINN / residual estimator with the same data contract  
   - *Optional:* fit $(H,D)$ by [differentiable simulation](../../600_identification/03_differentiable_simulation.md) (gradient through an RK4 rollout) and add it to the table  
4. Plot $\mathcal{L}(H,D)$ or slices; discuss physical vs equivalent  
5. Freeze $\hat{\theta}$ and simulate a **held-out** clearing time; compare to truth  

## Deliverables

- Loss-surface figure  
- Table: true $\theta$, LS $\hat{\theta}$, PINN $\hat{\theta}$, held-out trajectory error  
- Short paragraph: which parameter was weakly informed, and why  

## Status

Executable notebook provided for the LS + loss-surface path and the optional differentiable-simulation fit; inverse PINN cell is a structured template to complete in class or homework.
