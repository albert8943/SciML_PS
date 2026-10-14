# Learning paths

```{note} Maturity: Draft
Routes below are usable now. Week counts stay blank until an institution packages a semester. See [Status and versions](status_and_versions.md) and [Join and contribute](contribute.md).
```

One book, one table of contents. The routes on this page are overlays. They are not separate books. [Start here](start_here.md) helps you pick a route. On any chapter, the **Before you start** box says whether you can skip ahead.

(path-beginner)=
## Complete beginner

For readers new to programming and new to power systems.

1. [Programming from zero](../200_prep/bridge_programming_from_zero.md)
2. [Your first lab](first_lab_walkthrough.md) (Lab 1 in the browser)
3. [Power systems for ML people](../200_prep/bridge_power_systems_for_ml.md)
4. [Machine learning for power-systems people](../200_prep/bridge_ml_for_power_systems.md)
5. [Problem framing](../300_foundations/01_problem_framing.md)
6. [SMIB dynamics](../300_foundations/02_smib_dynamics.md)
7. The assessed write-up on [Lab 1](../900_labs/lab_01_reference_sim/index.md)

You can skip [Running notebooks](running_notebooks.md) until you want a local install. Prep notebooks are optional drills while they are still stubs.

(path-from-ml)=
## From machine learning

1. [Power systems for ML people](../200_prep/bridge_power_systems_for_ml.md)
2. [Glossary](../990_reference/glossary.md#glossary-machine) (machine and grid)
3. [Problem framing](../300_foundations/01_problem_framing.md)
4. [SMIB dynamics](../300_foundations/02_smib_dynamics.md)
5. [Reference simulation](../300_foundations/03_reference_simulation.md) and [Lab 1](../900_labs/lab_01_reference_sim/index.md)
6. Continue at [Data and surrogates](../300_foundations/04_data_and_surrogates.md) and the [Foundations overview](../300_foundations/overview.md) order

You can skip [Automatic differentiation](../300_foundations/05_differentiation.md) if you already use reverse-mode AD, and skip Prep 03–04. Still read the SMIB units before Lab 3.

(path-from-ps)=
## From power systems

1. [Machine learning for power-systems people](../200_prep/bridge_ml_for_power_systems.md)
2. [Your first lab](first_lab_walkthrough.md) if you have not run a notebook before. Otherwise open [Lab 1](../900_labs/lab_01_reference_sim/index.md) locally
3. [Problem framing](../300_foundations/01_problem_framing.md)
4. Skim [SMIB dynamics](../300_foundations/02_smib_dynamics.md) for the per-unit form this book uses
5. [Data and surrogates](../300_foundations/04_data_and_surrogates.md)
6. [Classical estimation](../300_foundations/07_classical_estimation.md), then [Forward PINNs](../300_foundations/06_forward_pinn.md)

You can skip the power-systems primer. You can skip a full re-derivation of the swing equation after the units skim.

(path-teachers)=
## For teachers

Use one book. Assign an overlay. Students who already know one side read the matching primer in week 1 and then join the same labs.

| Path ID | Audience | Suggested parts | Notes |
|---------|----------|-----------------|-------|
| `path_core` | First offering | [Preparation](../200_prep/overview.md) → [Foundations](../300_foundations/overview.md) → Labs 1–3 | Week count TBD when an institution schedules delivery |
| `path_stability` | Stability / CCT focus | Foundations → [Stability](../500_stability/overview.md) → [Lab 5](../900_labs/lab_05_stability_cct/index.md) | Assumes Lab 1 |
| `path_identification` | Parameter estimation focus | Foundations → [Identification](../600_identification/overview.md) → [Lab 3](../900_labs/lab_03_inertia_damping_id/index.md) | Classical least squares beside the inverse PINN |

Share a week-by-week overlay through [Join and contribute](contribute.md). Overlays stay on this page so the sidebar order does not fork into a second book.

(path-practitioners)=
## For practitioners

Go to the question you already work on. Read that page's **Before you start** box and fill only the gaps. The [full outline](outline.md) lists a short "Needs" note on each row.

| Question you already ask | Open |
|--------------------------|------|
| How will the system evolve? | [SMIB dynamics](../300_foundations/02_smib_dynamics.md), [Lab 1](../900_labs/lab_01_reference_sim/index.md), [Dynamics](../400_dynamics/overview.md) |
| Will it stay in step, and how close is the boundary? | [Stability](../500_stability/overview.md), [CCT](../500_stability/01_stability_and_cct.md), [Lab 5](../900_labs/lab_05_stability_cct/index.md) |
| Which parameters explain the measurements? | [Identification](../600_identification/overview.md), [Lab 3](../900_labs/lab_03_inertia_damping_id/index.md) |

If the learning vocabulary is new, read [Machine learning for power-systems people](../200_prep/bridge_ml_for_power_systems.md) first. If the machine vocabulary is new, read [Power systems for ML people](../200_prep/bridge_power_systems_for_ml.md) first.

(path-researchers)=
## For researchers

1. [SciML method families](../300_foundations/00_sciml_landscape.md)
2. [Identifiability](../300_foundations/08_identifiability.md) and [Physical vs equivalent parameters](../600_identification/02_physical_vs_equivalent.md)
3. The pillar you intend to extend: [Dynamics](../400_dynamics/overview.md), [Stability](../500_stability/overview.md), or [Identification](../600_identification/overview.md)
4. [From assessment to decision](../700_advanced/01_assessment_to_decision.md)
5. [Related open resources](related_resources.md) for neighboring notes and codes

Cross-domain review of a chapter (one ML reader and one power-systems reader) is a useful contribution: [Join and contribute](contribute.md).
