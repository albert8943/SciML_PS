# Lab 2 — Supervised surrogate versus physics residual (PINN)

```{note} Maturity: Stub
This laboratory page is under development. Goals below are the contract; the executable notebook arrives in a later pass.
```

:::{tip} Before you start
**Needs:** [Data and surrogates](../../300_foundations/04_data_and_surrogates.md) and [Lab 1](../lab_01_reference_sim/index.md) | **Coming from ML:** a matched supervised baseline beside a residual loss | **Coming from power systems:** read the [ML primer](../../200_prep/bridge_ml_for_power_systems.md), then this comparison | **New to both:** read the [ML primer](../../200_prep/bridge_ml_for_power_systems.md); the executable notebook is still a stub
:::

## Why this lab names PINN

The teaching contrast is **data-only** versus **data plus a physics residual** on the same SMIB plant, inputs, and training budget. A collocation PINN makes that residual easy to write for the swing equation and easy to remove in an ablation. This lab is not a survey of every SciML method. Neural ODEs, hybrids, and operator learning belong in [Lab 4](../lab_04_learned_dynamics/index.md) and on the [SciML method families](../../300_foundations/00_sciml_landscape.md) map.

## Goals

Matched input/output definitions and a documented training budget. Vary labeled-data amount. Report trajectory errors, residuals, and error near event interfaces. Include a controlled ablation removing the physics term.

## Further practice (optional)

After this lab exists in course form, the [ANDES PINN surrogate gallery](https://docs.andes.app/en/stable/gallery/pinn-surrogate.html) is optional further practice (symbolic DAE extraction). It does **not** replace Lab 2.

## Materials

Binder / Colab badges will appear with the executable notebook. Until then use [Running notebooks](../../100_front/running_notebooks.md) (local install is canonical). Contributions welcome: [Join and contribute](../../100_front/contribute.md).

## Status

Stub — no executable notebook yet.
