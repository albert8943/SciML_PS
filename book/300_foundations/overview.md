# Foundations overview

Shared method core before the three application pillars. Use a classical **SMIB** (single-machine infinite-bus) system repeatedly so the same equations appear as forward simulation, surrogate learning, stability labels, and parameter estimation.

:::{important} Shared SMIB spine
Foundations reuse one classical **SMIB** model so forward simulation, surrogates, stability labels, and parameter estimation share the same equations and notation.
:::

## Learning outcomes

After this part you should be able to:

- State forward, inverse, and stability-assessment tasks with clear inputs and outputs
- Distinguish **states** (time-varying) from **parameters** (usually fixed unknowns)
- Build or use a transparent numerical SMIB reference with documented events
- Explain data loss vs physics residual loss in a PINN
- Contrast classical least squares with inverse PINNs for named parameters
- Know when Neural ODEs / operator learning are a different SciML branch

## Suggested reading order

1. [Problem framing](01_problem_framing.md) — tasks, state vs parameter, forward vs inverse  
2. [SMIB dynamics](02_smib_dynamics.md)  
3. [Reference simulation](03_reference_simulation.md) then [Lab 1](../900_labs/lab_01_reference_sim/index.md)
4. [Data and surrogates](04_data_and_surrogates.md)  
5. [Automatic differentiation](05_differentiation.md)  
6. [Forward PINNs](06_forward_pinn.md)  
7. [Classical estimation](07_classical_estimation.md)  
8. [Identifiability](08_identifiability.md)  
9. [Inverse PINNs](09_inverse_pinn.md) then [Lab 3](../900_labs/lab_03_inertia_damping_id/index.md)
10. [Neural ODEs and hybrids](10_neural_ode_hybrid.md)

Optional landscape: [SciML method families](00_sciml_landscape.md).

## Pillars after this part

| Pillar | Folder | Engineering question |
|--------|--------|----------------------|
| Dynamics | `400_dynamics` | How will the system evolve? |
| Stability | `500_stability` | Stable or not, and how close to the boundary? |
| Identification | `600_identification` | Which parameters explain the measurements? |

## Content sources (authors)

Adapted from the course planning report and Obsidian beginner PINN lessons (01–06). Student pages do not carry research campaign metrics.
