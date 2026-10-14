# Foundations overview

```{note} Maturity: Draft
Readable teaching prose; examples, figures, and exercises are still growing. See [Status and versions](../100_front/status_and_versions.md) and [Join and contribute](../100_front/contribute.md).
```

:::{tip} Before you start
**Needs:** a bridge primer if either field is new | **Coming from ML:** skim [Power systems for ML people](../200_prep/bridge_power_systems_for_ml.md), then [Problem framing](01_problem_framing.md) | **Coming from power systems:** skim [Machine learning for power-systems people](../200_prep/bridge_ml_for_power_systems.md), then [Problem framing](01_problem_framing.md) | **New to both:** [Programming from zero](../200_prep/bridge_programming_from_zero.md), then both primers
:::

Shared method core before the three application pillars. Use a classical **SMIB** (single-machine infinite-bus) system repeatedly so the same equations appear as forward simulation, surrogate learning, stability labels, and parameter estimation.

:::{important} Shared SMIB spine
Foundations reuse one classical **SMIB** model so forward simulation, surrogates, stability labels, and parameter estimation share the same equations and notation.
:::

## Coming from another field

Chapters in this part can be read out of order when the **Before you start** box on the page is already satisfied.

| If this is you | Do this first |
|----------------|---------------|
| Machine learning, new to power systems | [Power systems for ML people](../200_prep/bridge_power_systems_for_ml.md), then [Problem framing](01_problem_framing.md) |
| Power systems, new to machine learning | [Machine learning for power-systems people](../200_prep/bridge_ml_for_power_systems.md), then [Problem framing](01_problem_framing.md) |
| New to both | [Programming from zero](../200_prep/bridge_programming_from_zero.md) and [Your first lab](../100_front/first_lab_walkthrough.md) |
| Comfortable with both | Use the [outline](../100_front/outline.md) and open the chapter you need |

Word-by-word translations: [Glossary](../990_reference/glossary.md). Routes by role: [Learning paths](../100_front/learning_paths.md).

Foundations teach the shared plant and an early physics-informed path (supervised baseline, then forward and inverse PINNs). [Dynamics](../400_dynamics/overview.md), [Stability](../500_stability/overview.md), and [Identification](../600_identification/overview.md) deepen the three engineering questions. Other SciML families (Neural ODEs, operators) arrive when needed — see [SciML method families](00_sciml_landscape.md) and [Lab 4](../900_labs/lab_04_learned_dynamics/index.md).

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

| Pillar | Engineering question |
|--------|----------------------|
| [Dynamics](../400_dynamics/overview.md) | How will the system evolve? |
| [Stability](../500_stability/overview.md) | Stable or not, and how close to the boundary? |
| [Identification](../600_identification/overview.md) | Which parameters explain the measurements? |
