# Reading list

Books, papers, and tools cited on chapter pages by short ID (for example B1 or R-K04). Chapter numbers are given only where an edition has been checked.

## Books and core bridges

| ID | Source (short) | Role |
|----|----------------|------|
| B1 | Kundur and Malik, *Power System Stability and Control*, 2nd ed. | Dynamics / stability foundations |
| B3 | Brunton and Kutz, [*Data-Driven Science and Engineering*](https://www.databookuw.com/) | Data-driven dynamics bridge |
| B4 | Bishop and Bishop, [*Deep Learning: Foundations and Concepts*](https://www.bishopbook.com/) (2024) | Neural networks, training, automatic differentiation background |
| B5 | Thuerey et al., [Physics-based Deep Learning](https://physicsbaseddeeplearning.org/intro.html) | Physical losses / differentiable physics |
| B6 | Ljung, *System Identification: Theory for the User*, 2nd ed. | Classical estimation, excitation, identifiability |

## Method papers

| ID | Source (short) | Role |
|----|----------------|------|
| R1 | Karniadakis et al., [Physics-informed machine learning](https://www.nature.com/articles/s42254-021-00314-5), *Nature Reviews Physics*, 2021 | Field overview |
| R2 | Baydin et al., [Automatic differentiation in machine learning: a survey](https://arxiv.org/abs/1502.05767) | Automatic differentiation |
| R3 | Raissi, Perdikaris, and Karniadakis, [Physics-informed neural networks](https://doi.org/10.1016/j.jcp.2018.10.045), *J. Comput. Phys.*, 2019 | Original PINN formulation (forward and inverse) |
| R6 | Chen et al., [Neural Ordinary Differential Equations](https://arxiv.org/abs/1806.07366), 2018 | Neural ODEs |
| R7 | Rackauckas et al., [Universal Differential Equations for Scientific Machine Learning](https://arxiv.org/abs/2001.04385) | Hybrid physics + learned models |

## Simulators

| ID | Source (short) | Role |
|----|----------------|------|
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

## Maths refresher (external, link only)

| ID | Source | Role |
|----|--------|------|
| M-E245 | [EECS 245 course notes](https://notes.eecs245.org/) (Suraj Rampure) | Optional linear-algebra / gradient / SVD background; **CC BY-NC-ND 4.0** — link only, do not adapt; table on [Preparation overview](../200_prep/overview.md) |

## Domain teaching pointers

| ID | Source | Role |
|----|--------|------|
| C13 | [PSCC 2024 tutorial](https://www.chatziva.com/pscc2024.html) | Power-system PINN / trustworthy AI tutorial landing |
| S-PINN-TSA | [Unified PINN SMIB TSA/CCT benchmark (code)](https://github.com/albert8943/unified-physics-informed-neural-surrogate-smib-tsa-cct-benchmark) | Optional further reading for trajectory surrogates — **not** a course lab |

Research code repositories are further reading, not redistributable course material.

**Labs vs this page:** assessed work is only Labs 1–5 under [Laboratories](../900_labs/README.md). External courses and packages are listed here, not on the Labs index.
