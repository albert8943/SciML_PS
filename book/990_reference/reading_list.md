# Reading list

Seed from the course planning report bibliography. Replace stubs with edition-checked chapter numbers before student release.

## Primary engineering / SciML bridges (report IDs)

| ID | Source (short) | Role |
|----|----------------|------|
| B1 | Kundur and Malik, *Power System Stability and Control* | Dynamics / stability foundations |
| B3 | Brunton and Kutz, *Data-Driven Science and Engineering* | Data-driven dynamics bridge |
| B5 | Thuerey et al., [Physics-based Deep Learning](https://physicsbaseddeeplearning.org/intro.html) | Physical losses / differentiable physics |
| S1 | [ANDES documentation](https://docs.andes.app/en/stable/) | Network simulation reference (GPL v3); course bridge: [ANDES as network reference](../500_stability/03_andes_network_reference.md) |
| S1a | [ANDES Gallery](https://docs.andes.app/en/stable/gallery/index.html) | Optional cases; preferred class network CCT: [Kundur CCT mapping](https://docs.andes.app/en/stable/gallery/critical-clearing-time.html) |

## B5 by chapter: where this book uses it

B5 is a method textbook with fluid-dynamics examples. This book takes its ideas and rewrites them for the SMIB swing equation; it does not copy its figures or notebooks.

| B5 chapter | Used in |
|------------|---------|
| [Overview and models](https://physicsbaseddeeplearning.org/overview.html) | [SciML landscape](../300_foundations/00_sciml_landscape.md) § How tightly is physics coupled? |
| [Supervised training discussion](https://physicsbaseddeeplearning.org/supervised-discuss.html) | [Data and surrogates](../300_foundations/04_data_and_surrogates.md); pillar Discussion sections |
| [Physical losses](https://physicsbaseddeeplearning.org/physicalloss.html), [discussion](https://physicsbaseddeeplearning.org/physicalloss-discuss.html) | [Forward PINN](../300_foundations/06_forward_pinn.md), [inverse PINN](../300_foundations/09_inverse_pinn.md) |
| [Differentiable physics](https://physicsbaseddeeplearning.org/diffphys.html), [DP versus PINN](https://physicsbaseddeeplearning.org/diffphys-dpvspinn.html) | [Differentiable simulation](../600_identification/03_differentiable_simulation.md); Lab 3 option |
| [Improved gradients](https://physicsbaseddeeplearning.org/physgrad.html), [half-inverse gradients](https://physicsbaseddeeplearning.org/physgrad-hig.html) | [Automatic differentiation](../300_foundations/05_differentiation.md) § Gradient scaling (further reading) |
| [Model reduction and time series](https://physicsbaseddeeplearning.org/others-timeseries.html) | [Dynamics overview](../400_dynamics/overview.md); Lab 4 |
| [Probabilistic learning](https://physicsbaseddeeplearning.org/probmodels-intro.html), [graph diffusion](https://physicsbaseddeeplearning.org/probmodels-graph.html), [reinforcement learning](https://physicsbaseddeeplearning.org/reinflearn-intro.html) | [Advanced overview](../700_advanced/overview.md) § Fast-forward topics |

Fluids-only examples (Navier-Stokes, airfoils, Lagrangian and meshless methods, GANs): link only if a student asks; not part of this course.

## Stability classification and margins

| ID | Source (short) | Role |
|----|----------------|------|
| R-K04 | [Kundur et al., IEEE Trans. Power Syst., 2004](https://doi.org/10.1109/TPWRS.2004.825981) | IEEE/CIGRE stability definitions (classic framework) |
| R-H21 | [Hatziargyriou et al., IEEE Trans. Power Syst., 2021](https://doi.org/10.1109/TPWRS.2020.3041774) | Converter-era stability classification update |

## Domain teaching pointers

| ID | Source | Role |
|----|--------|------|
| C13 | [PSCC 2024 tutorial](https://www.chatziva.com/pscc2024.html) | Power-system PINN / trustworthy AI tutorial landing |
| S-PINN-TSA | [Unified PINN SMIB TSA/CCT benchmark (code)](https://github.com/albert8943/unified-physics-informed-neural-surrogate-smib-tsa-cct-benchmark) | Optional further reading for trajectory surrogates — **not** a course lab |

A longer annotated bibliography lives in the course planning report (repository `docs/planning/`, maintainers). Do not treat research-repo notebooks as redistributable course materials without a license check.

**Labs vs this page:** assessed work is only Labs 1–5 under Laboratories. Put third-party GitHub courses and packages here (or in maintainer docs), not on the Labs index. Maintainer policy: `docs/guides/lab_spine_policy.md`.
