# Inverse PINNs

## Learning goals

- Formulate an inverse PINN with trainable named parameters
- Compare to classical LS on the same data contract
- Keep network inputs, known signals, and unknowns in separate buckets

## Reading

- Adapted from vault Lessons 4–5  
- Course report Lab 3

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

## Lab

- [Lab 3 — Inertia and damping estimation](../900_labs/lab_03_inertia_damping_id/index.md)

## Further reading

- [Identifiability](08_identifiability.md); identification pillar overview

## Common misconceptions

- Calling any PINN with parameters in the residual a solved identification problem  
- Optimizing $\theta$ without bounds or units  
- Using GFM triad language without declaring an elective model
