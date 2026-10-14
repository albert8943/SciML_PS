# Neural ODEs and hybrid models

```{note} Maturity: Draft
Readable teaching prose; examples, figures, and exercises are still growing. See [Status and versions](../100_front/status_and_versions.md) and [Join and contribute](../100_front/contribute.md).
```

:::{tip} Before you start
**Needs:** [Forward PINNs](06_forward_pinn.md) | **Coming from ML:** a numerical solver in the loop, distinct from collocation | **Coming from power systems:** the integrator stays visible; a neural term can sit inside the ODE | **New to both:** read the [ML primer](../200_prep/bridge_ml_for_power_systems.md) and [Reference simulation](03_reference_simulation.md)
:::

## Learning goals

- Contrast collocation PINNs with solver-based learned dynamics
- State when Neural ODEs or hybrid/UDE models are appropriate teaching choices
- Keep operator learning (DeepONet/FNO) as a **different SciML branch**

## Reading

- Neural ODEs [@chen2018neural]  
- Universal differential equations [@rackauckas2020universal]

## Collocation PINN vs Neural ODE

| | Collocation PINN | Neural ODE / hybrid |
|--|------------------|---------------------|
| Dynamics | Residual at collocation points | Integrate a learned or hybrid vector field with a solver |
| Strength | Flexible collocation; easy physics residual | Respects solver structure; natural rollouts |
| Watch-outs | Residual ≠ solution quality | Long-rollout drift; adjoint cost |

**Hybrid / UDE idea:** known physics terms plus a neural correction for missing dynamics. The correction can absorb parameter error — treat fits as possibly **equivalent**.

## Operator learning (awareness only)

DeepONet / FNO learn maps between **functions** (e.g. load profile → trajectory). That is not the same as collocation inverse PINN for a few named scalars. See [SciML landscape](00_sciml_landscape.md) and Lab 4 options.

## Worked example

Define a held-out longer time horizon before training a Neural ODE on SMIB data. Report error at train horizon vs extrapolated horizon.

## Lab

- [Lab 4 — Learned dynamics generalization](../900_labs/lab_04_learned_dynamics/index.md)

## Further reading

- [Lab 4 — learned dynamics](../900_labs/lab_04_learned_dynamics/index.md)

## Common misconceptions

- Treating DeepONet as “a type of PINN”  
- Claiming generalization without a pre-registered held-out domain  
- Using hybrid corrections as proof of physical parameter recovery
