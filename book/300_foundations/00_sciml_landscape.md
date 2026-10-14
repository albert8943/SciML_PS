# SciML method families (landscape)

```{note} Maturity: Draft
Readable teaching prose; examples, figures, and exercises are still growing. See [Status and versions](../100_front/status_and_versions.md) and [Join and contribute](../100_front/contribute.md).
```

:::{tip} Before you start
**Needs:** names of PINN and Neural ODE in the [glossary](../990_reference/glossary.md#glossary-learning) | **Coming from ML:** these are the families this book uses on one grid model | **Coming from power systems:** a PINN is a neural model trained with a residual of the equations you already write | **New to both:** read both primers on [Start here](../100_front/start_here.md), then use this page as a map
:::

:::{important} Reader path
Practice order on the shared plant: [Lab 1](../900_labs/lab_01_reference_sim/index.md) (reference) → [Lab 2](../900_labs/lab_02_surrogate_vs_pinn/index.md) (supervised surrogate versus PINN residual) → [Lab 3](../900_labs/lab_03_inertia_damping_id/index.md) (inverse) → [Lab 4](../900_labs/lab_04_learned_dynamics/index.md) (Neural ODE / operator options) → [Lab 5](../900_labs/lab_05_stability_cct/index.md) (CCT). Pick the physics-coupling level from the engineering question and the data contract, not from climbing the ladder below. The table on this page says where each family lives in the book.
:::

## Learning goals

- Name major SciML families used for power-system dynamics and TSA
- Say what each family **learns** (trajectory, vector field, operator, …)
- Avoid treating every neural method as “a PINN”

## Reading

- Physics-informed machine learning overview [@karniadakis2021physics]  
- [Overview and models](https://physicsbaseddeeplearning.org/overview.html) chapter of @thuerey2021pbdl

## Plain-words map

SciML here means: neural models with **physics structure** for dynamics or margins — not only black-box stable/unstable classifiers.

| Family | Learns (roughly) | Teaching role in this book |
|--------|------------------|----------------------------|
| Supervised surrogate | Map features → trajectories / labels | Mandatory baseline (Lab 2) |
| PINN (collocation) | $\hat{x}(t)$ with residual loss | Core forward / inverse path |
| Neural ODE / hybrid | Vector field (+ optional known physics) | Lab 4 option |
| Operator learning (DeepONet / FNO) | Function → function | Advanced / Lab 4 option; not inverse named-$\theta$ default |
| Differentiable simulator | Sensitivities through a solver | Identification ([differentiable simulation](../600_identification/03_differentiable_simulation.md)); Lab 3 option |
| Classical simulation | Reference trajectories | Lab 1 and all baselines |

For **transient stability**, families differ mainly by whether they output trajectories, decisions, or operators — and how CCT search sits on top. Details: [Stability pillar](../500_stability/overview.md).

## How tightly is physics coupled?

A second way to sort the same families is by **how tightly the physics is built into training**. This ordering follows the method textbook by @thuerey2021pbdl. Here it is restated for the SMIB swing equation.

```{mermaid}
flowchart LR
  sup["1. Supervised surrogate: physics only in the training data"] --> loss["2. Physics loss (PINN): swing-equation residual added to the loss"]
  loss --> dp["3. Differentiable simulator: the solver itself sits in the training loop"]
```

| Level | Where the swing equation enters | Gradient comes from | In this book |
|-------|---------------------------------|---------------------|--------------|
| 1. Supervised surrogate | Only through simulator-generated labels | Data mismatch | [Data and surrogates](04_data_and_surrogates.md), Lab 2 baseline |
| 2. Physics loss (PINN) | Residual $r_\delta, r_\omega$ at collocation points | Data mismatch + residual (soft constraint) | [Forward PINN](06_forward_pinn.md), [inverse PINN](09_inverse_pinn.md), Labs 2–3 |
| 3. Differentiable simulator | A numerical integrator (e.g. RK4) rolled out in an AD framework | Mismatch of the **simulated** trajectory, differentiated through every solver step | [Differentiable simulation](../600_identification/03_differentiable_simulation.md), Lab 3 option; hybrid models in [Neural ODE / hybrid](10_neural_ode_hybrid.md) |

**Plain words:** moving down the table, the model is allowed to break the physics less, but each training step costs more and needs a solver you can differentiate.

Tighter coupling is not automatically better. Pick the level from the engineering question and the data contract, not from the ladder.

## Further reading

- Neural ODEs [@chen2018neural] and universal differential equations [@rackauckas2020universal], developed in [Neural ODEs and hybrid models](10_neural_ode_hybrid.md)

## Common misconceptions

- “DeepONet is a PINN variant”  
- Ranking methods by hype instead of task fit  
- Skipping classical simulation because a neural method exists
- “The most tightly coupled method is always the best one”
