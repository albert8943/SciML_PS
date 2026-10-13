# Identifiability

## Learning goals

- Separate noise, poor excitation, and structural non-identifiability
- Design a simple two-parameter loss-surface or sensitivity diagnostic
- Distinguish **physical** vs **equivalent** fitted parameters

## Reading

- Course report identifiability themes; B6 as assigned  
- Teaching adapt of vault “physical versus equivalent parameters” (no research metrics)

## Three failure modes

| Cause | Symptom | Mitigation |
|-------|---------|------------|
| Noise | Scatter around a identifiable minimum | Longer windows, filtering, repeats |
| Poor excitation | Flat loss valleys | Richer disturbances; multiple events |
| Structural | Many $\theta$ give the same $y$ | Reparametrize; measure more channels; change model |

## Physical vs equivalent parameters

A fitted coefficient is **physical** when it matches a device/control constant under a consistent model map and informative data. It is **equivalent** (effective) when it mainly absorbs mismatch, weak excitation, or an inconsistent residual — even if trajectory error looks small.

Low NRMSE does **not** certify physical meaning.

## Worked example

For $(H,D)$ on one load step, plot $\mathcal{L}(H,D)$. If the valley is elongated along $D$, damping is weakly informed by that experiment — redesign excitation before trusting $\hat{D}$.

## Lab

- Diagnostics required in [Lab 3](../900_labs/lab_03_inertia_damping_id/index.md)  
- Deeper measurement design: [Measurements and excitation](../600_identification/01_measurements_and_excitation.md)

## Further reading

- Course report Lab 3 success criteria; physical vs equivalent discussion in identification pillar

## Common misconceptions

- “Unique minimizer of training loss ⇒ unique physical $\theta$”  
- Bound-clamped estimates reported as if interior physical optima  
- Ignoring that a second disturbance may invalidate an equivalent fit
