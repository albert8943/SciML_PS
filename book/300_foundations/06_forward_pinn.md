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

## Lab

- [Lab 2 — Surrogate versus PINN](../900_labs/lab_02_surrogate_vs_pinn/index.md)

## Further reading

- Physics-based Deep Learning (B5) physical-loss chapters; course report Lab 2

## Common misconceptions

- Calling every residual network an “inverse PINN”  
- Reporting only $\mathcal{L}_{\mathrm{phys}}$ without trajectory metrics  
- Assuming a trained forward PINN is a stability certificate
