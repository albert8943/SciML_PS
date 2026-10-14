# Reading list

## How references work in this book

Each chapter has its own **References** section at the bottom of the page, listing only the works that chapter cites. Use those lists when you study a topic; this page keeps only the few sources the whole book leans on.

All entries come from one shared bibliography (`references.bib` in the [repository](https://github.com/albert8943/SciML_PS)), so a source has the same citation everywhere. Missing a key paper, or found a wrong DOI? Please [tell us](../100_front/feedback.md) or [contribute](../100_front/contribute.md) a fix.

## Core textbooks

| Textbook | Used for |
|----------|----------|
| @kundur2022power | Power-system dynamics and transient stability |
| @brunton2022datadriven | Data-driven dynamics |
| @bishop2024deep | Neural networks, training, and backpropagation |
| @thuerey2021pbdl | Physical losses and differentiable physics |
| @ljung1999system | Classical estimation, excitation, and identifiability |

Chapter or section numbers are given on chapter pages only where an edition has been checked.

## Simulators

| Tool | Role |
|------|------|
| [ANDES](https://docs.andes.app/en/stable/) [@cui2021hybrid; @andes] | Network simulation reference (GPL-3.0). Course bridge: [ANDES as network reference](../500_stability/03_andes_network_reference.md) |
| [ANDES Gallery](https://docs.andes.app/en/stable/gallery/index.html) | Optional cases; preferred network CCT example: [Kundur CCT mapping](https://docs.andes.app/en/stable/gallery/critical-clearing-time.html) |

## Maths refresher (external, link only)

The [EECS 245 course notes](https://notes.eecs245.org/) [@rampure_eecs245] give optional linear-algebra, gradient, and SVD background. They are **CC BY-NC-ND 4.0**, so this book links to them and does not adapt them. Topic table: [Preparation overview](../200_prep/overview.md).

## Where this book reuses Physics-based Deep Learning

@thuerey2021pbdl is a method textbook with fluid-dynamics examples. This book takes its ideas and rewrites them for the SMIB swing equation; it does not copy its figures or notebooks.

| PBDL chapter | Used in |
|--------------|---------|
| [Overview and models](https://physicsbaseddeeplearning.org/overview.html) | [SciML landscape](../300_foundations/00_sciml_landscape.md) § How tightly is physics coupled? |
| [Supervised training discussion](https://physicsbaseddeeplearning.org/supervised-discuss.html) | [Data and surrogates](../300_foundations/04_data_and_surrogates.md); pillar Discussion sections |
| [Physical losses](https://physicsbaseddeeplearning.org/physicalloss.html), [discussion](https://physicsbaseddeeplearning.org/physicalloss-discuss.html) | [Forward PINN](../300_foundations/06_forward_pinn.md), [inverse PINN](../300_foundations/09_inverse_pinn.md) |
| [Differentiable physics](https://physicsbaseddeeplearning.org/diffphys.html), [DP versus PINN](https://physicsbaseddeeplearning.org/diffphys-dpvspinn.html) | [Differentiable simulation](../600_identification/03_differentiable_simulation.md); Lab 3 option |
| [Improved gradients](https://physicsbaseddeeplearning.org/physgrad.html), [half-inverse gradients](https://physicsbaseddeeplearning.org/physgrad-hig.html) | [Automatic differentiation](../300_foundations/05_differentiation.md) § Gradient scaling |
| [Model reduction and time series](https://physicsbaseddeeplearning.org/others-timeseries.html) | [Dynamics overview](../400_dynamics/overview.md); Lab 4 |
| [Probabilistic learning](https://physicsbaseddeeplearning.org/probmodels-intro.html), [graph diffusion](https://physicsbaseddeeplearning.org/probmodels-graph.html), [reinforcement learning](https://physicsbaseddeeplearning.org/reinflearn-intro.html) | [Advanced overview](../700_advanced/overview.md) § Fast-forward topics |

Fluids-only examples (Navier-Stokes, airfoils, Lagrangian and meshless methods, GANs) are not part of this course.

## Neighbouring courses and code

Other open courses, tutorials, and research codes are listed on [Related open resources](../100_front/related_resources.md). Research code repositories are further reading, not redistributable course material; assessed work is only Labs 1–5 under [Laboratories](../900_labs/README.md).
