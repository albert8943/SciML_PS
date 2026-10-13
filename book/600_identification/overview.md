# Identification pillar overview

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
