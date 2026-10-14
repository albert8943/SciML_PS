# Identification pillar overview

```{note} Maturity: Draft
Readable teaching prose; examples, figures, and exercises are still growing. See [Status and versions](../100_front/status_and_versions.md) and [Join and contribute](../100_front/contribute.md).
```

:::{tip} Before you start
**Needs:** [Classical estimation](../300_foundations/07_classical_estimation.md) | **Coming from ML:** an inverse problem with a measurement contract | **Coming from power systems:** which parameters explain the records | **New to both:** read the [ML primer](../200_prep/bridge_ml_for_power_systems.md) and finish [Lab 1](../900_labs/lab_01_reference_sim/index.md)
:::

**Engineering question:** Which parameters and dynamic relationships explain the measurements?

## Focus

Identifiability, measurement contracts, excitation, and classical vs physics-informed estimators. Teaching Lab 3 uses classical inertia and damping $(H, D)$. Converter-parameter electives (GFM/GFL reduced-order knobs) stay optional and must name estimands explicitly.

## Learning path

1. Foundations: [classical estimation](../300_foundations/07_classical_estimation.md), [identifiability](../300_foundations/08_identifiability.md), [inverse PINN](../300_foundations/09_inverse_pinn.md)  
2. [Measurements and excitation](01_measurements_and_excitation.md)  
3. [Physical vs equivalent parameters](02_physical_vs_equivalent.md)  
4. [Differentiable simulation](03_differentiable_simulation.md) — gradients through the solver  
5. [Lab 3 — Inertia and damping](../900_labs/lab_03_inertia_damping_id/index.md)

## Honesty rule

Low trajectory error does not certify physical parameter recovery. Report bounds, excitation, and a held-out disturbance test.

## Discussion: what Identification methods can and cannot claim

| Can claim (with evidence) | Cannot claim |
|---------------------------|--------------|
| Recovery of a known $\theta$ in a synthetic test with stated noise and excitation | Recovery on real data without a model-map argument |
| Held-out disturbance error with frozen $\hat{\theta}$ | That $\hat{\theta}$ is a **physical** constant when the model is mismatched (it may be equivalent) |
| Which parameter the data inform weakly (loss surface, sensitivity) | That a faster or gradient-based estimator removes weak identifiability |

**Rule:** least squares, differentiable simulation, and inverse PINN are compared on the same data contract, and every estimate is re-simulated with the reference solver.
