# Classical estimation baselines

```{note} Maturity: Draft
Readable teaching prose; examples, figures, and exercises are still growing. See [Status and versions](../100_front/status_and_versions.md) and [Join and contribute](../100_front/contribute.md).
```

## Learning goals

- Set up simulation-based least squares for named parameters with bounds
- Use classical estimators as mandatory baselines before neural inverse methods
- Keep teaching estimands explicit: classical $(H, D)$

## Reading

- [Lab 3 — inertia and damping identification](../900_labs/lab_03_inertia_damping_id/index.md); system identification references [@ljung1999system; @brunton2022datadriven]

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

- [Lab 3](../900_labs/lab_03_inertia_damping_id/index.md); [identifiability](08_identifiability.md) chapter next
- Gradient-based version of the same LS problem: [differentiable simulation](../600_identification/03_differentiable_simulation.md)
- Maths background (external, link only): [least squares](https://notes.eecs245.org/simple-linear-regression/least-squares) in the EECS 245 notes [@rampure_eecs245] (CC BY-NC-ND 4.0)

## Common misconceptions

- Skipping the classical baseline because “PINN is modern”  
- Comparing LS and PINN on different noise seeds or windows  
- Reporting percent error without stating the true $\theta$ and bounds
