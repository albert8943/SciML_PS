# Full outline

Every page of the notes on one page, in reading order. The [Book map](book_map.md) explains *why* the book is organized this way; this page lists *what* is in each section.

**Maturity** follows the labels on each page: **Stub** (outline and goals only), **Draft** (readable prose, still growing), **In review**, **Stable**. Details: [Status and versions](status_and_versions.md). Want to write, review, or extend a chapter? See [Join and contribute](contribute.md).

## Front matter

| Page | What it covers |
|------|----------------|
| [How to use this book](how_to_use.md) | What these notes are, how pages are laid out, how to get help |
| [Advice to the student](advice.md) | How to read a page, work the labs, and avoid common traps |
| [Preview this book locally](preview_locally.md) | Build and serve the notes on your own machine |
| [Running notebooks](running_notebooks.md) | Local (canonical), Binder (primary online), Colab (secondary) |
| [Book map](book_map.md) | Big-picture layout and what each application produces |
| [Full outline](outline.md) | This page |
| [Learning paths](learning_paths.md) | Semester paths (stub until a course offering is packaged) |
| [Related open resources](related_resources.md) | Neighbouring courses, notes, and research codes |
| [Join and contribute](contribute.md) | How to report, write, review, or join as a section editor |
| [Status and versions](status_and_versions.md) | Public preview (v0.x), versioning, maturity labels |
| [Feedback](feedback.md) | Typos, broken links, unclear pages |
| [License](license.md) | CC BY-NC-SA 4.0 content, MIT code, contribution sign-off |

## Preparation

| Page | What it covers | Maturity |
|------|----------------|----------|
| [Preparation overview](../200_prep/overview.md) | Self-check before Foundations; optional maths refreshers | Draft |
| [Prep 01: NumPy basics](../200_prep/nb01_numpy_basics.ipynb) | Array workflows | Stub |
| [Prep 02: ODE integration](../200_prep/nb02_ode_integration.ipynb) | Numerical integration of small ODEs | Stub |
| [Prep 03: Tiny neural regression](../200_prep/nb03_nn_regression.ipynb) | A minimal neural network fit | Stub |
| [Prep 04: Gradients](../200_prep/nb04_gradients.ipynb) | Gradients and automatic differentiation by hand | Stub |

## Foundations

| Chapter | What it covers | Maturity | Lab |
|---------|----------------|----------|-----|
| [Foundations overview](../300_foundations/overview.md) | Shared SMIB spine used throughout the book | Draft | |
| [SciML method families](../300_foundations/00_sciml_landscape.md) | Map of SciML families used for power-system dynamics and stability | Draft | |
| [Problem framing](../300_foundations/01_problem_framing.md) | Forward dynamics, stability assessment, and inverse estimation as distinct tasks | Draft | [Lab 1](../900_labs/lab_01_reference_sim/index.md) |
| [SMIB dynamics](../300_foundations/02_smib_dynamics.md) | Classical swing equations in consistent units | Draft | [Lab 1](../900_labs/lab_01_reference_sim/index.md) |
| [Reference simulation](../300_foundations/03_reference_simulation.md) | A transparent numerical SMIB reference with an event schedule | Draft | [Lab 1](../900_labs/lab_01_reference_sim/index.md) |
| [Data and surrogates](../300_foundations/04_data_and_surrogates.md) | Input/output contracts for supervised trajectory surrogates | Draft | [Lab 2](../900_labs/lab_02_surrogate_vs_pinn/index.md) |
| [Automatic differentiation](../300_foundations/05_differentiation.md) | Finite differences versus reverse-mode AD for residual losses | Draft | |
| [Forward PINNs](../300_foundations/06_forward_pinn.md) | Data and physics losses for a known ODE | Draft | [Lab 2](../900_labs/lab_02_surrogate_vs_pinn/index.md) |
| [Classical estimation baselines](../300_foundations/07_classical_estimation.md) | Simulation-based least squares for named, bounded parameters | Draft | [Lab 3](../900_labs/lab_03_inertia_damping_id/index.md) |
| [Identifiability](../300_foundations/08_identifiability.md) | Noise, poor excitation, and structural non-identifiability | Draft | [Lab 3](../900_labs/lab_03_inertia_damping_id/index.md) |
| [Inverse PINNs](../300_foundations/09_inverse_pinn.md) | Inverse PINNs with trainable named parameters | Draft | [Lab 3](../900_labs/lab_03_inertia_damping_id/index.md) |
| [Neural ODEs and hybrid models](../300_foundations/10_neural_ode_hybrid.md) | Collocation PINNs versus solver-based learned dynamics | Draft | [Lab 4](../900_labs/lab_04_learned_dynamics/index.md) |

## Dynamics (application 1)

| Chapter | What it covers | Maturity | Lab |
|---------|----------------|----------|-----|
| [Dynamics pillar overview](../400_dynamics/overview.md) | How will the system evolve under inputs, parameters, and disturbances? Planned chapters | Stub | [Lab 4](../900_labs/lab_04_learned_dynamics/index.md) |

## Stability (application 2)

| Chapter | What it covers | Maturity | Lab |
|---------|----------------|----------|-----|
| [Stability pillar overview](../500_stability/overview.md) | Will the system remain stable, and how close is it to the boundary? | Draft | [Lab 5](../900_labs/lab_05_stability_cct/index.md) |
| [Stability labels and CCT](../500_stability/01_stability_and_cct.md) | Rotor-angle security, labels, and critical clearing time by bisection | Draft | [Lab 5](../900_labs/lab_05_stability_cct/index.md) |
| [Surrogate models for stability tasks](../500_stability/02_surrogate_stability.md) | Binary labels, margin estimates, and trajectory surrogates as different products | Draft | [Lab 5](../900_labs/lab_05_stability_cct/index.md) |
| [ANDES as network reference](../500_stability/03_andes_network_reference.md) | Moving from SMIB to a network simulator after the SMIB work | Draft | [Lab 5](../900_labs/lab_05_stability_cct/index.md) |
| [Direct methods](../500_stability/04_direct_methods.md) | Equal-area and energy ideas as an independent CCT check | Draft | [Lab 5](../900_labs/lab_05_stability_cct/index.md) |

## Identification (application 3)

| Chapter | What it covers | Maturity | Lab |
|---------|----------------|----------|-----|
| [Identification pillar overview](../600_identification/overview.md) | Which parameters and dynamics explain the measurements? | Draft | [Lab 3](../900_labs/lab_03_inertia_damping_id/index.md) |
| [Measurements and excitation](../600_identification/01_measurements_and_excitation.md) | Observation channels, noise models, and window lengths | Draft | [Lab 3](../900_labs/lab_03_inertia_damping_id/index.md) |
| [Physical vs equivalent parameters](../600_identification/02_physical_vs_equivalent.md) | Physical versus equivalent (effective) fitted parameters | Draft | [Lab 3](../900_labs/lab_03_inertia_damping_id/index.md) |
| [Differentiable simulation](../600_identification/03_differentiable_simulation.md) | Gradients with respect to $(H, D)$ through a numerical solver | Draft | [Lab 3](../900_labs/lab_03_inertia_damping_id/index.md) |

## Advanced topics

| Chapter | What it covers | Maturity | Lab |
|---------|----------------|----------|-----|
| [Advanced topics overview](../700_advanced/overview.md) | Optional extensions (operators, uncertainty, converters) | Stub | |
| [From assessment to decision](../700_advanced/01_assessment_to_decision.md) | How the three applications connect in one operating-point loop | Draft | |

## Laboratories

| Lab | What you deliver | Maturity |
|-----|------------------|----------|
| [Laboratories index](../900_labs/README.md) | How the five assessed labs fit together | Draft |
| [Lab 1: Reference simulation and scientific dataset](../900_labs/lab_01_reference_sim/index.md) | SMIB simulator, event schedule, dataset manifest, convergence check | Draft |
| [Lab 2: Supervised surrogate versus PINN](../900_labs/lab_02_surrogate_vs_pinn/index.md) | Matched comparison with a physics-term ablation | Stub |
| [Lab 3: Inertia and damping estimation](../900_labs/lab_03_inertia_damping_id/index.md) | Least squares versus inverse PINN on the same measurements | Draft |
| [Lab 4: Generalization of a learned dynamic model](../900_labs/lab_04_learned_dynamics/index.md) | Hybrid/neural ODE or DeepONet tested on a held-out domain | Stub |
| [Lab 5: Stability and CCT](../900_labs/lab_05_stability_cct/index.md) | Reference CCT brackets, then a learned model near the boundary | Draft |

## Reference

| Page | What it covers |
|------|----------------|
| [Reading list](../990_reference/reading_list.md) | Core textbooks, simulators, and how per-chapter references work |
| [Notation](../990_reference/notation.md) | Symbols and unit conventions |
