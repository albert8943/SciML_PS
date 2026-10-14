# Lab 5 — Stability and CCT

```{note} Maturity: Draft
Readable teaching prose; examples, figures, and exercises are still growing. See [Status and versions](../../100_front/status_and_versions.md) and [Join and contribute](../../100_front/contribute.md).
```

:::{tip} Before you start
**Needs:** [Lab 1](../lab_01_reference_sim/index.md) and [Stability labels and CCT](../../500_stability/01_stability_and_cct.md) | **Coming from ML:** report false-safe counts and CCT error beside trajectory error | **Coming from power systems:** build the reference CCT by search, then judge a learned model | **New to both:** read the fault section of the [power-systems primer](../../200_prep/bridge_power_systems_for_ml.md) and finish Lab 1
:::

## Goals

Create reference labels and CCT brackets on classical SMIB (Lab 1 tooling), then evaluate a learned surrogate or forward PINN near the boundary. Report signed and absolute CCT errors, false-safe decisions, and one case where trajectory ranking and CCT ranking disagree.

## Prerequisites

- [Lab 1](../lab_01_reference_sim/index.md)  
- Prefer also [Lab 2](../lab_02_surrogate_vs_pinn/index.md)  
- Chapters: [CCT](../../500_stability/01_stability_and_cct.md), [surrogate stability](../../500_stability/02_surrogate_stability.md), optional [direct methods](../../500_stability/04_direct_methods.md)

## Reference CCT (no ML yet)

Using `simulate_smib` / `angle_stable`:

1. Fix prefault state and fault inception  
2. Sweep or bisect clearing time until the operational label flips  
3. Record bracket width and tolerance  
4. Optional: if the case matches equal-area assumptions, compare search CCT to the classical estimate ([direct methods](../../500_stability/04_direct_methods.md))  


## Learned CCT (after Lab 2)

Replace the inner trajectory call with a surrogate; keep the **same** stability rule. Compare $\hat{t}_{\mathrm{CCT}}$ to the reference CCT.

## Deliverables

- Reference CCT table for ≥3 operating / fault settings  
- Signed CCT errors for the learned method  
- False-safe count on a boundary-focused set  
- One disagreement case write-up  

## Materials (launch paths)

```{note} Under development
Online launch (Binder / Colab) for the **SMIB** Lab 5 notebook will appear when that executable notebook ships (after Lab 2). Canonical path remains local install. Help improve launch paths: [Join and contribute](../../100_front/contribute.md). Guide: [Running notebooks](../../100_front/running_notebooks.md).
```

- Assessed SMIB path: use Lab 1 tooling locally until the dedicated SMIB CCT notebook is added; then Binder/Colab badges will match Labs 1 and 3
- **ANDES network extension is local only** (not on Binder / Colab)

## Optional network extension (after this lab)

Assessed Lab 5 stays on **classical SMIB**. When SMIB CCT works, the preferred network follow-on is Kundur via ANDES (**not** a sixth assessed lab):

- Notebook: [`lab05_network_cct_andes.ipynb`](lab05_network_cct_andes.ipynb) — one-bus CCT sweep + signed error / false-safe metrics (**local / `envs/course_andes.yml` only**)
- Helper: `sciml_ps.andes_cct` (requires `envs/course_andes.yml`, **andes==2.0.0**)
- Bridge page: [ANDES as network reference](../../500_stability/03_andes_network_reference.md)
- Official full map (link only): [Critical Clearing Time Mapping](https://docs.andes.app/en/stable/gallery/critical-clearing-time.html)

## Status

Narrative and protocol ready; full SMIB surrogate CCT notebook follows Lab 2. Network extension notebook + ANDES pin (`2.0.0`) are in place.
