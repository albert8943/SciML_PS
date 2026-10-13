# Classical estimation baselines

## Learning goals

- Set up simulation-based least squares for named parameters with bounds
- Use classical estimators as mandatory baselines before neural inverse methods
- Keep teaching estimands explicit: classical $(H, D)$

## Reading

- Course report Lab 3; system identification references (B3, B6 as assigned)

## Least squares against a simulator

Given measurements $y^{\mathrm{meas}}(t)$ and a simulator $y(t;\theta)$:

$$
\hat{\theta} = \arg\min_{\theta\in\Theta} \sum_i \big\| y^{\mathrm{meas}}(t_i) - y(t_i;\theta) \big\|^2
$$

with explicit bounds $\Theta$ (e.g. positive $H$, non-negative $D$).

| Strength | Limitation |
|----------|------------|
| Interpretable; strong baseline | Needs a reliable simulator in the loop |
| Bounds and units are clear | Local minima; excitation-dependent |
| Easy to plot 2-D loss surfaces for $(H,D)$ | Costly if each loss eval is a long TDS |

## Teaching rule

Lab 3 compares **simulation-based LS** with **inverse PINN** on the **same** measurements, windows, and bounds. Do not silently swap in converter GFM $(M_v,D_v,m_p)$ unless the elective says so.

## Worked example

Fix a load-step experiment. Plot a coarse grid of $\mathcal{L}(H,D)$ and mark the true $(H^\star,D^\star)$ and the LS minimizer.

## Lab

- [Lab 3 — Inertia and damping estimation](../900_labs/lab_03_inertia_damping_id/index.md)

## Further reading

- Course report §6.2 Lab 3; identifiability chapter next

## Common misconceptions

- Skipping the classical baseline because “PINN is modern”  
- Comparing LS and PINN on different noise seeds or windows  
- Reporting percent error without stating the true $\theta$ and bounds
