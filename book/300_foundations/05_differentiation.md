# Automatic differentiation

## Learning goals

- Contrast finite differences with reverse-mode AD for residual losses
- Explain why AD enables physics-informed training
- Name practical pitfalls (discontinuous events, stiff residuals)

## Reading

- Course report Weeks on gradients / PyTorch; Goodfellow-style AD intuition (B4 if assigned)

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

## Worked example

Differentiate $\sin(w t)$ w.r.t. $t$ with AD in PyTorch/`torch.autograd` and compare to $w\cos(w t)$.

## Lab

- Used implicitly in Labs 2–3 when you implement residual losses

## Further reading

- Framework AD docs; course prep notebook on gradients

## Common misconceptions

- “AD is approximate like finite differences.” — For smooth elementary ops it is not.  
- Differentiating through discontinuous fault switches without careful event handling  
- Forgetting `create_graph=True` when higher-order derivatives are needed
