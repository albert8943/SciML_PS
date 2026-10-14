# Automatic differentiation

```{note} Maturity: Draft
Readable teaching prose; examples, figures, and exercises are still growing. See [Status and versions](../100_front/status_and_versions.md) and [Join and contribute](../100_front/contribute.md).
```

## Learning goals

- Contrast finite differences with reverse-mode AD for residual losses
- Explain why AD enables physics-informed training
- Name practical pitfalls (discontinuous events, stiff residuals)

## Reading

- Automatic differentiation survey [@baydin2015automatic]; backpropagation intuition [@bishop2024deep]

## Why AD matters for PINNs

Physics residuals need $\partial \hat{x}/\partial t$ (and often parameter sensitivities). Finite differences are noisy and scale poorly. **Automatic differentiation** gives exact derivatives of the computational graph (up to machine precision) for the operations you coded.

In a typical collocation PINN:

1. Network maps $t \mapsto \hat{x}(t)$  
2. AD supplies $\dot{\hat{x}}$  
3. Residual $r(\hat{x},\dot{\hat{x}},u,\theta)$ enters $\mathcal{L}_{\mathrm{phys}}$

## Forward vs reverse mode (intuition)

- **Forward mode:** efficient with few inputs, many outputs  
- **Reverse mode (backprop):** efficient with many inputs (weights), few outputs (scalar loss) — the usual deep-learning case  

PINN training almost always uses reverse mode on a scalar total loss.

## Gradient scaling

AD gives exact gradients, but exact gradients can still point in an unhelpful direction when the loss terms have very different scales.

In the classical SMIB of [SMIB dynamics](02_smib_dynamics.md), $\omega$ is in rad/s. It sits near $\omega_0 = 2\pi \cdot 60 \approx 377$, while its swing is a few rad/s. The angle $\delta$ is of order 1 rad. Unscaled, $r_\omega$ and the $\omega$ data term can dominate the total loss, so training mostly fits speed and neglects angle. Inverse problems have the same issue in parameter space: $H \approx 5$ and $D \approx 0.1$ have very different sensitivities.

Practical fixes, in the order to try them:

1. **Non-dimensionalize states.** Train on $\Delta\omega = \omega - \omega_0$ (or $\Delta\omega/\omega_0$) and $\delta - \delta_0$, not raw $\omega$.
2. **Normalize each loss term** by a typical magnitude, or report per-term losses so imbalance is visible.
3. **Rescale parameters.** Optimize $\log H$ and $\log D$, or values divided by a nominal, inside stated bounds.
4. **Weight terms explicitly** ($\lambda_{\mathrm{phys}}$ and per-state weights) and report the weights used.

**Plain words:** the optimizer follows whichever number is biggest. Make the numbers comparable before trusting the fit.

Further reading: @thuerey2021pbdl treat this problem in depth, including [scale-invariant physics training](https://physicsbaseddeeplearning.org/physgrad.html) and [half-inverse gradients](https://physicsbaseddeeplearning.org/physgrad-hig.html) demonstrated on coupled oscillators. Those algorithms are beyond this course; the fixes above are enough for the labs.

## Worked example

Differentiate $\sin(w t)$ w.r.t. $t$ with AD in PyTorch/`torch.autograd` and compare to $w\cos(w t)$.

## Lab

- Used implicitly in Labs 2–3 when you implement residual losses

## Further reading

- Framework AD docs; course prep notebook on gradients
- Maths background (external, link only): [gradient descent](https://notes.eecs245.org/gradients/gradient-descent) and [convexity](https://notes.eecs245.org/gradients/convexity) in the EECS 245 notes [@rampure_eecs245] (CC BY-NC-ND 4.0)

## Common misconceptions

- “AD is approximate like finite differences.” — For smooth elementary ops it is not.  
- Differentiating through discontinuous fault switches without careful event handling  
- Forgetting `create_graph=True` when higher-order derivatives are needed
- Feeding raw $\omega \approx 377$ rad/s into a loss next to $\delta \approx 1$ rad and blaming the optimizer
