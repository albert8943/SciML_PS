# Physical vs equivalent parameters

```{note} Maturity: Draft
Readable teaching prose; examples, figures, and exercises are still growing. See [Status and versions](../100_front/status_and_versions.md) and [Join and contribute](../100_front/contribute.md).
```

:::{tip} Before you start
**Needs:** [Identifiability](../300_foundations/08_identifiability.md) | **Coming from ML:** a fitted number is a physical constant only when the model matches the plant | **Coming from power systems:** an equivalent parameter absorbs model error and still has a stated test | **New to both:** read physical and equivalent parameter in the [glossary](../990_reference/glossary.md#glossary-checks)
:::

## Learning goals

- Define physical vs equivalent (effective) fitted parameters
- Give examples of mismatch that force equivalence
- Require recovery checks beyond trajectory NRMSE

## Reading

- Model structure and parameter interpretation [@ljung1999system]  
- [Identifiability](../300_foundations/08_identifiability.md)

## Definitions

- **Physical:** coefficient matches a device/control constant under a consistent model map and informative data.  
- **Equivalent:** coefficient mainly absorbs unmodeled dynamics, bad excitation, or residual mismatch — even if waveforms look good.

## Practical checks

1. Loss-surface / sensitivity along each parameter  
2. Bound activity (clamped estimates are suspicious)  
3. Predict a **held-out** disturbance with frozen $\hat{\theta}$  
4. Optional: synthetic recovery with known true $\theta$ before real data  

## Converter elective note

Reduced-order GFM/GFL parameters are a different estimand family from classical $(H,D)$. If you introduce them, document the simulator map explicitly — do not relabel foreign block constants as if they were identical.

## Lab

- Required discussion prompt in [Lab 3](../900_labs/lab_03_inertia_damping_id/index.md)

## Common misconceptions

- “We estimated $D$, therefore we know machine damping.”  
- Treating bound-saturated values as interior physical optima
