# Inverse PINNs

```{note} Maturity: Draft
Readable teaching prose; examples, figures, and exercises are still growing. See [Status and versions](../100_front/status_and_versions.md) and [Join and contribute](../100_front/contribute.md).
```

:::{tip} Before you start
**Needs:** [Forward PINNs](06_forward_pinn.md) and [Classical estimation](07_classical_estimation.md) | **Coming from ML:** network weights and named parameters are different knobs | **Coming from power systems:** H and D become trainable beside the residual | **New to both:** read the [ML primer](../200_prep/bridge_ml_for_power_systems.md) and [Classical estimation](07_classical_estimation.md)
:::

## Learning goals

- Formulate an inverse PINN with trainable named parameters
- Compare to classical LS on the same data contract
- Keep network inputs, known signals, and unknowns in separate buckets

## Reading

- Inverse problems section of @raissi2019physics  
- [Lab 3 — inertia and damping identification](../900_labs/lab_03_inertia_damping_id/index.md)

## Where parameters enter

| Style | Network | Parameters $\theta$ |
|-------|---------|---------------------|
| Forward PINN | Learns $\hat{x}(t)$ | Fixed inside residual |
| Inverse PINN | Learns $\hat{x}(t)$ | **Trainable** variables in residual |

The optimizer updates neural weights **and** $\theta$ (teaching Lab 3: $H$, $D$).

### Buckets (do not confuse)

| Bucket | Examples | Role |
|--------|----------|------|
| Network input | $t$ | Feeds the NN |
| Known signals | measured $P(t)$, setpoints | Residual / forcing |
| Unknowns | NN weights + $\theta$ | Optimized |

Measured power is **not** a parameter; it is a known signal or observation channel.

## Comparison protocol (Lab 3)

1. Same measurements, noise model, window, and bounds  
2. Classical LS baseline  
3. Inverse PINN  
4. Loss-surface or sensitivity diagnostic  
5. Test fitted $\theta$ on a **held-out** disturbance  

## Worked example

Write $\mathcal{L}_{\mathrm{data}} + \lambda_{\mathrm{phys}}\mathcal{L}_{\mathrm{phys}}$ with $\theta=(H,D)$ trainable. List which tensors require `requires_grad=True`.

## Strengths and limits for identification

The forward-PINN limits ([strengths and limits of physics losses](06_forward_pinn.md#strengths-and-limits-of-physics-losses)) carry over. Inverse use adds three of its own.

- **Shared blame.** Network weights and $(H, D)$ are fitted together. A flexible network can absorb model error that should have shown up in $\theta$. So a low loss does not mean $\theta$ is right.
- **Weighting moves $\theta$.** Changing $\lambda_{\mathrm{phys}}$ can shift the estimated $(H, D)$, not only the fit quality. Report estimates for more than one weight.
- **Residual consistency is not trajectory consistency.** Check the fitted $\theta$ by re-simulating with the reference solver (Lab 1). Compare that trajectory with the measurements, not the network output.

A tighter alternative puts the solver itself in the loop: [differentiable simulation](../600_identification/03_differentiable_simulation.md). There, $\theta$ is the only unknown and every candidate trajectory obeys the model exactly.

## Lab

- [Lab 3 — Inertia and damping estimation](../900_labs/lab_03_inertia_damping_id/index.md)

## Further reading

- [Identifiability](08_identifiability.md); identification pillar overview
- @thuerey2021pbdl, [discussion of physical losses](https://physicsbaseddeeplearning.org/physicalloss-discuss.html) and [differentiable physics versus physics-informed training](https://physicsbaseddeeplearning.org/diffphys-dpvspinn.html)

## Common misconceptions

- Calling any PINN with parameters in the residual a solved identification problem  
- Optimizing $\theta$ without bounds or units  
- Using GFM triad language without declaring an elective model
