# Forward PINNs

## Learning goals

- Write data and physics losses for a known ODE fragment
- Explain the role of the physics weight $\lambda_{\mathrm{phys}}$
- Contrast forward PINNs with supervised surrogates

## Reading

- Adapted from vault Lessons 4–5 (teaching language)  
- Course report PINN rows in §4.3; Raissi et al. (R#) as assigned

## Three pieces

1. **Neural network** — usually input $t$ (and maybe known parameters / controls); output $\hat{x}(t)$  
2. **Data loss** — match measurements or labeled simulator trajectories  

$$
\mathcal{L}_{\mathrm{data}} \approx \|\hat{x}(t) - x^{\mathrm{meas}}(t)\|^2
$$

3. **Physics loss** — collocation residual of the ODE/DAE fragment  

$$
\mathcal{L}_{\mathrm{phys}} \approx \|r(\hat{x},\dot{\hat{x}},u,\theta)\|^2
$$

Total loss:

$$
\mathcal{L} = \mathcal{L}_{\mathrm{data}} + \lambda_{\mathrm{phys}}\mathcal{L}_{\mathrm{phys}} + \cdots
$$

**Plain words:** the network is pulled toward the data **and** toward obeying physics. $\lambda_{\mathrm{phys}}$ sets how hard the physics pull is.

## Forward-style use

In a **forward** PINN, parameters $\theta$ inside the residual are **known and fixed**. The network learns trajectories (or a surrogate solution) consistent with physics and any available labels.

| If $\lambda_{\mathrm{phys}}=0$ | If you ignore data |
|-------------------------------|--------------------|
| You may fit waveforms that violate physics | You may get a residual-minimizing curve that misses measurements |

## Worked example

For the classical swing equations with known $(H,D)$, place collocation points in time and write $r_\delta$ and $r_\omega$ explicitly. Train with a small labeled window plus residual.

## Strengths and limits of physics losses

The points below follow the discussion of physical losses in B5, rewritten for the swing equation.

| Strength | Limit |
|----------|-------|
| Needs no solver: only the network, AD, and the residual $r_\delta, r_\omega$ | **Soft constraint.** The residual is only *penalized*, so a trained $\hat{x}(t)$ still violates the swing equation by some amount. Report the residual next to trajectory error |
| Works with sparse or partial measurements (e.g. only $\omega$ measured) | **Collocation cost.** The residual is only checked at collocation points. Fault switching at $t_f$ and $t_c$ needs points concentrated around the events |
| Same code pattern for forward and inverse problems | **Loss weighting.** $\mathcal{L}_{\mathrm{data}}$, $r_\delta$ and $r_\omega$ have different scales, so $\lambda_{\mathrm{phys}}$ (and per-term weights) change the answer. See [gradient scaling](05_differentiation.md#gradient-scaling) |
| Smooth, differentiable output in $t$ | **Weak extrapolation.** A network trained on $t \in [0, 2]$ s is not a simulator. Outside the training window, or for a new clearing time, it must be re-checked against Lab 1 |

**Plain words:** a PINN is a curve fitted to data and nudged toward the physics. It is not a solver that guarantees the physics.

## Lab

- [Lab 2 — Surrogate versus PINN](../900_labs/lab_02_surrogate_vs_pinn/index.md)  
- Optional further practice (does not replace Lab 2): [ANDES PINN surrogate gallery](https://docs.andes.app/en/stable/gallery/pinn-surrogate.html)

## Further reading

- B5 Thuerey et al., [physical losses](https://physicsbaseddeeplearning.org/physicalloss.html) and [discussion of physical losses](https://physicsbaseddeeplearning.org/physicalloss-discuss.html) (Burgers examples; same ideas); course report Lab 2

## Common misconceptions

- Calling every residual network an “inverse PINN”  
- Reporting only $\mathcal{L}_{\mathrm{phys}}$ without trajectory metrics  
- Assuming a trained forward PINN is a stability certificate
