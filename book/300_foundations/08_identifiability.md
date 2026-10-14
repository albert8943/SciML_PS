# Identifiability

```{note} Maturity: Draft
Readable teaching prose; examples, figures, and exercises are still growing. See [Status and versions](../100_front/status_and_versions.md) and [Join and contribute](../100_front/contribute.md).
```

## Learning goals

- Separate noise, poor excitation, and structural non-identifiability
- Design a simple two-parameter loss-surface or sensitivity diagnostic
- Distinguish **physical** vs **equivalent** fitted parameters

## Reading

- B6 (Ljung) on identifiability and experiment design  
- [Physical versus equivalent parameters](../600_identification/02_physical_vs_equivalent.md)

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

- [Lab 3](../900_labs/lab_03_inertia_damping_id/index.md) success criteria; [physical versus equivalent parameters](../600_identification/02_physical_vs_equivalent.md) in the identification part
- Maths background (external, link only): [low-rank approximation](https://notes.eecs245.org/singular-value-decomposition/low-rank-approximation) / [PCA](https://notes.eecs245.org/singular-value-decomposition/principal-components-analysis) in the EECS 245 notes (M-E245, CC BY-NC-ND 4.0) — useful intuition for flat directions in a loss surface

## Common misconceptions

- “Unique minimizer of training loss ⇒ unique physical $\theta$”  
- Bound-clamped estimates reported as if interior physical optima  
- Ignoring that a second disturbance may invalidate an equivalent fit
