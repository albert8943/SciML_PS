# Lab 3 — Inertia and damping estimation

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

## Protocol

1. Generate a “truth” trajectory with known $(H^\star, D^\star)$ and additive noise on $\omega$  
2. Grid or optimize LS loss vs $(H,D)$ with documented bounds  
3. Train inverse PINN / residual estimator with the same data contract  
4. Plot $\mathcal{L}(H,D)$ or slices; discuss physical vs equivalent  
5. Freeze $\hat{\theta}$ and simulate a **held-out** clearing time; compare to truth  

## Deliverables

- Loss-surface figure  
- Table: true $\theta$, LS $\hat{\theta}$, PINN $\hat{\theta}$, held-out trajectory error  
- Short paragraph: which parameter was weakly informed, and why  

## Status

Executable notebook provided for the LS + loss-surface path; inverse PINN cell is a structured template to complete in class or homework.
