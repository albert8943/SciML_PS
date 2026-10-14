# Full outline

Every page of the notes on one page, in reading order. The [Book map](book_map.md) explains *why* the book is organized this way; this page lists *what* is in each section. **Needs** says what to read if you jump here directly. Entrances by background and role: [Start here](start_here.md).

**Maturity** follows the labels on each page: **Stub** (outline and goals only), **Draft** (readable prose, still growing), **In review**, **Stable**. Details: [Status and versions](status_and_versions.md). Want to write, review, or extend a chapter? See [Join and contribute](contribute.md).

## Front matter

| Page | What it covers |
|------|----------------|
| [Start here](start_here.md) | Choose an entrance by background and by role |
| [How to use this book](how_to_use.md) | What these notes are, how pages are laid out, how to get help |
| [Advice to readers](advice.md) | How to read a page, work the labs, and avoid common traps |
| [Preview this book locally](preview_locally.md) | Build and serve the notes on your own machine |
| [Running notebooks](running_notebooks.md) | Local (canonical), Binder (primary online), Colab (secondary) |
| [Your first lab](first_lab_walkthrough.md) | Lab 1 in the browser, with numbered steps and no install |
| [Book map](book_map.md) | Big-picture layout and what each application produces |
| [Full outline](outline.md) | This page |
| [Learning paths](learning_paths.md) | Routes by background and by role, plus course overlays |
| [Related open resources](related_resources.md) | Neighbouring courses, notes, and research codes |
| [Join and contribute](contribute.md) | How to report, write, review, or join as a section editor |
| [Status and versions](status_and_versions.md) | Public preview (v0.x), versioning, maturity labels |
| [Feedback](feedback.md) | Typos, broken links, unclear pages |
| [License](license.md) | CC BY-NC-SA 4.0 content, MIT code, contribution sign-off |

## Preparation

| Page | What it covers | Maturity |
|------|----------------|----------|
| [Preparation overview](../200_prep/overview.md) | Self-check before Foundations; optional maths refreshers | Draft |
| [Programming from zero](../200_prep/bridge_programming_from_zero.md) | Notebooks, cells, and a kernel, for readers new to programming | Draft |
| [Power systems for ML people](../200_prep/bridge_power_systems_for_ml.md) | Grid, swing equation, faults, and CCT in machine-learning language | Draft |
| [Machine learning for power-systems people](../200_prep/bridge_ml_for_power_systems.md) | Loss, training, and generalization in power-system language | Draft |
| [Prep 01: NumPy basics](../200_prep/nb01_numpy_basics.ipynb) | Array workflows | Stub |
| [Prep 02: ODE integration](../200_prep/nb02_ode_integration.ipynb) | Numerical integration of small ODEs | Stub |
| [Prep 03: Tiny neural regression](../200_prep/nb03_nn_regression.ipynb) | A minimal neural network fit | Stub |
| [Prep 04: Gradients](../200_prep/nb04_gradients.ipynb) | Gradients and automatic differentiation by hand | Stub |

## Foundations

| Chapter | What it covers | Maturity | Lab | Needs |
|---------|----------------|----------|-----|-------|
| [Foundations overview](../300_foundations/overview.md) | Shared SMIB spine used throughout the book | Draft | | Either bridge primer |
| [SciML method families](../300_foundations/00_sciml_landscape.md) | Map of SciML families used for power-system dynamics and stability | Draft | | [Glossary](../990_reference/glossary.md#glossary-learning) |
| [Problem framing](../300_foundations/01_problem_framing.md) | Forward dynamics, stability assessment, and inverse estimation as distinct tasks | Draft | [Lab 1](../900_labs/lab_01_reference_sim/index.md) | Glossary: state, parameter |
| [SMIB dynamics](../300_foundations/02_smib_dynamics.md) | Classical swing equations in consistent units | Draft | [Lab 1](../900_labs/lab_01_reference_sim/index.md) | [PS primer](../200_prep/bridge_power_systems_for_ml.md) if the machine is new |
| [Reference simulation](../300_foundations/03_reference_simulation.md) | A transparent numerical SMIB reference with an event schedule | Draft | [Lab 1](../900_labs/lab_01_reference_sim/index.md) | SMIB dynamics; [first lab](first_lab_walkthrough.md) |
| [Data and surrogates](../300_foundations/04_data_and_surrogates.md) | Input/output contracts for supervised trajectory surrogates | Draft | [Lab 2](../900_labs/lab_02_surrogate_vs_pinn/index.md) | Problem framing; [ML primer](../200_prep/bridge_ml_for_power_systems.md) if supervised learning is new |
| [Automatic differentiation](../300_foundations/05_differentiation.md) | Finite differences versus reverse-mode AD for residual losses | Draft | | [ML primer](../200_prep/bridge_ml_for_power_systems.md) or Prep 04 |
| [Forward PINNs](../300_foundations/06_forward_pinn.md) | Data and physics losses for a known ODE | Draft | [Lab 2](../900_labs/lab_02_surrogate_vs_pinn/index.md) | Data and surrogates; automatic differentiation |
| [Classical estimation baselines](../300_foundations/07_classical_estimation.md) | Simulation-based least squares for named, bounded parameters | Draft | [Lab 3](../900_labs/lab_03_inertia_damping_id/index.md) | Reference simulation |
| [Identifiability](../300_foundations/08_identifiability.md) | Noise, poor excitation, and structural non-identifiability | Draft | [Lab 3](../900_labs/lab_03_inertia_damping_id/index.md) | Classical estimation |
| [Inverse PINNs](../300_foundations/09_inverse_pinn.md) | Inverse PINNs with trainable named parameters | Draft | [Lab 3](../900_labs/lab_03_inertia_damping_id/index.md) | Forward PINNs; classical estimation |
| [Neural ODEs and hybrid models](../300_foundations/10_neural_ode_hybrid.md) | Collocation PINNs versus solver-based learned dynamics | Draft | [Lab 4](../900_labs/lab_04_learned_dynamics/index.md) | Forward PINNs |

## Dynamics (application 1)

| Chapter | What it covers | Maturity | Lab | Needs |
|---------|----------------|----------|-----|-------|
| [Dynamics pillar overview](../400_dynamics/overview.md) | How will the system evolve under inputs, parameters, and disturbances? Planned chapters | Stub | [Lab 4](../900_labs/lab_04_learned_dynamics/index.md) | SMIB dynamics; Lab 1 |

## Stability (application 2)

| Chapter | What it covers | Maturity | Lab | Needs |
|---------|----------------|----------|-----|-------|
| [Stability pillar overview](../500_stability/overview.md) | Will the system remain stable, and how close is it to the boundary? | Draft | [Lab 5](../900_labs/lab_05_stability_cct/index.md) | Lab 1; SMIB dynamics |
| [Stability labels and CCT](../500_stability/01_stability_and_cct.md) | Rotor-angle security, labels, and critical clearing time by bisection | Draft | [Lab 5](../900_labs/lab_05_stability_cct/index.md) | Stability overview |
| [Surrogate models for stability tasks](../500_stability/02_surrogate_stability.md) | Binary labels, margin estimates, and trajectory surrogates as different products | Draft | [Lab 5](../900_labs/lab_05_stability_cct/index.md) | Data and surrogates; CCT |
| [ANDES as network reference](../500_stability/03_andes_network_reference.md) | Moving from SMIB to a network simulator after the SMIB work | Draft | [Lab 5](../900_labs/lab_05_stability_cct/index.md) | Lab 5 SMIB path |
| [Direct methods](../500_stability/04_direct_methods.md) | Equal-area and energy ideas as an independent CCT check | Draft | [Lab 5](../900_labs/lab_05_stability_cct/index.md) | CCT; SMIB dynamics |

## Identification (application 3)

| Chapter | What it covers | Maturity | Lab | Needs |
|---------|----------------|----------|-----|-------|
| [Identification pillar overview](../600_identification/overview.md) | Which parameters and dynamics explain the measurements? | Draft | [Lab 3](../900_labs/lab_03_inertia_damping_id/index.md) | Classical estimation |
| [Measurements and excitation](../600_identification/01_measurements_and_excitation.md) | Observation channels, noise models, and window lengths | Draft | [Lab 3](../900_labs/lab_03_inertia_damping_id/index.md) | Identifiability |
| [Physical vs equivalent parameters](../600_identification/02_physical_vs_equivalent.md) | Physical versus equivalent (effective) fitted parameters | Draft | [Lab 3](../900_labs/lab_03_inertia_damping_id/index.md) | Identifiability |
| [Differentiable simulation](../600_identification/03_differentiable_simulation.md) | Gradients with respect to $(H, D)$ through a numerical solver | Draft | [Lab 3](../900_labs/lab_03_inertia_damping_id/index.md) | Automatic differentiation; classical estimation |

## Advanced topics

| Chapter | What it covers | Maturity | Lab | Needs |
|---------|----------------|----------|-----|-------|
| [Advanced topics overview](../700_advanced/overview.md) | Optional extensions (operators, uncertainty, converters) | Stub | | Three pillar overviews |
| [From assessment to decision](../700_advanced/01_assessment_to_decision.md) | How the three applications connect in one operating-point loop | Draft | | Three pillar overviews |

## Laboratories

| Lab | What you deliver | Maturity | Needs |
|-----|------------------|----------|-------|
| [Laboratories index](../900_labs/README.md) | How the five assessed labs fit together | Draft | [Start here](start_here.md) |
| [Lab 1: Reference simulation and scientific dataset](../900_labs/lab_01_reference_sim/index.md) | SMIB simulator, event schedule, dataset manifest, convergence check | Draft | [First lab](first_lab_walkthrough.md) |
| [Lab 2: Supervised surrogate versus PINN](../900_labs/lab_02_surrogate_vs_pinn/index.md) | Matched comparison with a physics-term ablation | Stub | Data and surrogates; Lab 1 |
| [Lab 3: Inertia and damping estimation](../900_labs/lab_03_inertia_damping_id/index.md) | Least squares versus inverse PINN on the same measurements | Draft | Lab 1; classical estimation |
| [Lab 4: Generalization of a learned dynamic model](../900_labs/lab_04_learned_dynamics/index.md) | Hybrid/neural ODE or DeepONet tested on a held-out domain | Stub | Neural ODEs; Labs 1–3 |
| [Lab 5: Stability and CCT](../900_labs/lab_05_stability_cct/index.md) | Reference CCT brackets, then a learned model near the boundary | Draft | Lab 1; CCT |

## Reference

| Page | What it covers |
|------|----------------|
| [Reading list](../990_reference/reading_list.md) | Core textbooks, simulators, and how per-chapter references work |
| [Glossary](../990_reference/glossary.md) | Plain meaning plus power-systems and ML readings of the same word |
| [Notation](../990_reference/notation.md) | Symbols and unit conventions |
