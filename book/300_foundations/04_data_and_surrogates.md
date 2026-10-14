# Data and surrogates

```{note} Maturity: Draft
Readable teaching prose; examples, figures, and exercises are still growing. See [Status and versions](../100_front/status_and_versions.md) and [Join and contribute](../100_front/contribute.md).
```

## Learning goals

- Define matched input/output contracts for a supervised trajectory surrogate
- Separate scenario splits from within-trajectory splits
- State what a surrogate can and cannot claim about physics and stability

## Reading

- [Lab 2 — surrogate versus PINN](../900_labs/lab_02_surrogate_vs_pinn/index.md); neural-network training basics [@bishop2024deep]

## Supervised surrogate

Given features (e.g. time, operating point, clearing time, or a parameter vector) predict trajectories or a reduced output. Training uses labeled simulator data only — **no** residual term unless you add one (then you are moving toward a PINN).

| Strength | Limitation |
|----------|------------|
| Simple baseline; clear budget | Needs enough labeled scenarios |
| Fast evaluation | Extrapolation outside the training distribution is unsafe |
| Easy ablation | Does not enforce physics unless you add constraints |

## Data contracts

Document:

- Channels: which states/outputs are supervised  
- Normalization fit **on training scenarios only**  
- Held-out scenarios chosen **before** training  

## Worked example

Train a small MLP to predict $\delta(t)$ on a grid of clearing times. Report error on a held-out clearing time near the stability boundary vs far from it.

## Lab

- [Lab 2 — Surrogate versus PINN](../900_labs/lab_02_surrogate_vs_pinn/index.md) (after Lab 1)

## Further reading

- [Supervised training discussion](https://physicsbaseddeeplearning.org/supervised-discuss.html) in @thuerey2021pbdl as method background
- Data-driven dynamics [@brunton2022datadriven]

## Common misconceptions

- Low average trajectory error implies correct CCT decisions  
- More capacity always fixes distribution shift  
- Using test events to tune architecture without saying so
