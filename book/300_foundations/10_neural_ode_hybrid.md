# Neural ODEs and hybrid models

## Learning goals

- Contrast collocation PINNs with solver-based learned dynamics
- State when Neural ODEs or hybrid/UDE models are appropriate teaching choices
- Keep operator learning (DeepONet/FNO) as a **different SciML branch**

## Reading

- Course report §4.3 (Neural ODE, hybrid/UDE, DeepONet)  
- Chen et al., Neural ODEs (R6) as assigned

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

- Course report Lab 4; advanced part overview

## Common misconceptions

- Treating DeepONet as “a type of PINN”  
- Claiming generalization without a pre-registered held-out domain  
- Using hybrid corrections as proof of physical parameter recovery
