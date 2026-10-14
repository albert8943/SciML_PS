# Surrogate models for stability tasks

```{note} Maturity: Draft
Readable teaching prose; examples, figures, and exercises are still growing. See [Status and versions](../100_front/status_and_versions.md) and [Join and contribute](../100_front/contribute.md).
```

:::{tip} Before you start
**Needs:** [Data and surrogates](../300_foundations/04_data_and_surrogates.md) and [Stability labels and CCT](01_stability_and_cct.md) | **Coming from ML:** a classifier, a margin model, and a trajectory model are different outputs | **Coming from power systems:** a close trajectory and a correct CCT ranking can disagree | **New to both:** read the [ML primer](../200_prep/bridge_ml_for_power_systems.md) and the CCT chapter
:::

## Learning goals

- Separate **binary labels**, **margin estimates**, and **trajectory surrogates** as different products
- Separate trajectory error from boundary / CCT decision error
- Place a learned surrogate inside an operational CCT search carefully
- Require classical simulation baselines on the same scenarios

## Reading

- [Lab 2](../900_labs/lab_02_surrogate_vs_pinn/index.md) and [Lab 5](../900_labs/lab_05_stability_cct/index.md)  
- [Stability labels and CCT](01_stability_and_cct.md); [Forward PINNs](../300_foundations/06_forward_pinn.md)

## What the model is asked to produce

| Approach | Typical output | Operational use |
|----------|----------------|-----------------|
| Binary classifier | Stable / unstable | Fast screen only — **no** clearing margin |
| Margin regressor | CCT-like scalar | Needs careful labels and honesty about extrapolation |
| Trajectory surrogate | $\delta(t)$ (and related states), then search | Reuse one model for nominal TSA **and** CCT search if the **same criterion** is used |

Binary stable/unstable labels are not enough for risk-informed decisions that need **how close** the system is to the boundary. Margin regression and trajectory-based search aim at that gap; both still require a stated criterion and a reference simulator.

## One trajectory model, two assessment tasks

A useful teaching pattern (planning-oriented screening):

```text
Time-domain reference (e.g. Lab 1 SMIB / later ANDES)
        → train trajectory surrogate (supervised net or forward PINN)
                → TSA screen at nominal clearing
                → CCT search by bisection on clearing time
```

The same trained checkpoint can serve both tasks **only if** the stability rule (horizon, threshold, persistence window, …) matches the rule used on the reference trajectories. Mixing criteria between surrogate and reference invalidates the comparison.

## Forward surrogates for TSA

A **forward** surrogate predicts trajectories quickly for many clearing times or operating points. CCT search may call the surrogate instead of the full simulator — but then CCT error and false-safe rate must be reported against the **reference** simulator.

| Safe practice | Unsafe practice |
|---------------|-----------------|
| Same fault, clearing action, horizon, criterion | Mixing criteria between surrogate and reference |
| Boundary-focused test set | Only easy stable cases |
| Signed CCT error + false-safe | Accuracy-only leaderboard |
| Report that better trajectories need not yield protection-grade CCT | Treating low trajectory RMSE as CCT certification |

Improved trajectory fidelity helps screening and comparative studies; it does **not** automatically deliver protection-grade CCT estimation.

## Worked example

On SMIB Lab 1 scenarios, compare CCT from dense reference simulation vs CCT from a surrogate with a coarse time grid. Where do rankings disagree? Keep the stability rule identical.

## Lab

- [Lab 5](../900_labs/lab_05_stability_cct/index.md); trajectory models from [Lab 2](../900_labs/lab_02_surrogate_vs_pinn/index.md)

## Further reading

- [Forward PINNs](../300_foundations/06_forward_pinn.md); [SciML landscape](../300_foundations/00_sciml_landscape.md)  
- Optional published SMIB trajectory-surrogate example (Further reading only — not a course lab): @poulose_smib_tsa_benchmark  

## Common misconceptions

- "Fast surrogate implies trustworthy CCT"  
- "Binary accuracy is enough for operational margins"  
- Retraining on the CCT test bracket without disclosure  
- Skipping classical energy-function or TDS baselines when available  
