# Lab 3 — Inertia and damping estimation

```{note} Maturity: Draft
Readable teaching prose; examples, figures, and exercises are still growing. See [Status and versions](../../100_front/status_and_versions.md) and [Join and contribute](../../100_front/contribute.md).
```

## Goals

Compare **simulation-based least squares** with an **inverse PINN** (or collocation residual estimator) on the same measurements and bounds. Vary noise, window length, and excitation. Plot a two-parameter loss surface or local sensitivity diagnostic. Test fitted $(H,D)$ on another disturbance.

## Teaching estimands

Classical SMIB **inertia and damping** $(H, D)$. Do not silently substitute research GFM converter knobs.

## Prerequisites

- [Lab 1](../lab_01_reference_sim/index.md) completed  
- Chapters: [classical estimation](../../300_foundations/07_classical_estimation.md), [identifiability](../../300_foundations/08_identifiability.md), [inverse PINN](../../300_foundations/09_inverse_pinn.md), [physical vs equivalent](../../600_identification/02_physical_vs_equivalent.md)

## Materials

- Starter notebook: [`lab03_inertia_damping_id.ipynb`](lab03_inertia_damping_id.ipynb)  
- Simulator: `sciml_ps.simulate_smib` (same classical SMIB as Lab 1)  
- Optional differentiable rollout: `sciml_ps.smib_torch.rollout_smib` (needs `torch`)

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
