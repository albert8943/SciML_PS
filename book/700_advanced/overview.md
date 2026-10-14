# Advanced topics overview

```{note} Maturity: Stub
This section is under development. Start with [assessment to decision](01_assessment_to_decision.md); other Advanced topics thicken after Labs 1–5.
```

:::{tip} Before you start
**Needs:** a skim of the Dynamics, Stability, and Identification overviews | **Coming from ML:** operator learning and uncertainty sit here after a SMIB PINN is familiar | **Coming from power systems:** multimachine and converter pointers sit here after the SMIB labs | **New to both:** follow a route on [Learning paths](../100_front/learning_paths.md)
:::

## Start here

1. [From assessment to decision](01_assessment_to_decision.md) — how Identification, Dynamics, and Stability connect toward operating-point decisions  

## Planned directions (stubs later)

- Operator learning (DeepONet / FNO) as a **forward** function→function branch — not a PINN variant
- Uncertainty quantification for estimated parameters
- Multimachine / network scaling after SMIB mastery (ANDES / Kundur path under Stability)
- Selected converter synchronization case studies (after Labs 1–5; VSM–swing bridge first)

## Fast-forward topics

Short pointers to directions this book does not teach yet. Each needs Labs 1–5 first. Method background is @thuerey2021pbdl; linked external code carries its own license.

- **Probabilistic learning for uncertainty.** Generative models (diffusion, flow matching) learn a *distribution* of trajectories or parameters instead of one answer. In this book's terms: a spread of plausible $(H, D)$ or a probability of instability, instead of a point estimate. Background: [probabilistic learning introduction](https://physicsbaseddeeplearning.org/probmodels-intro.html).
- **Graph architectures for networks.** Multimachine systems are graphs (buses and lines). Graph neural networks and graph-based generative models respect that structure and are a natural next step after the Kundur path. Background: [network architectures](https://physicsbaseddeeplearning.org/supervised-arch.html), [graph-based diffusion models](https://physicsbaseddeeplearning.org/probmodels-graph.html).
- **Reinforcement learning for control.** Learning control actions (e.g. damping) from interaction. It is outside the three pillars of this book; treat it as curiosity. Background: [reinforcement learning introduction](https://physicsbaseddeeplearning.org/reinflearn-intro.html); applied example: the ANDES RL gallery entry below.

## Linked further practice (ANDES gallery)

Summarize-then-link only — not core TOC spines:

- [Forced oscillation (WECC 179)](https://docs.andes.app/en/stable/gallery/forced-oscillation.html) — large-system elective  
- [RL oscillation damping (SMIB)](https://docs.andes.app/en/stable/gallery/smib-oscillation.html) — outside the three pillars; curiosity  
- Gallery index: https://docs.andes.app/en/stable/gallery/index.html

## Status

Synthesis page filled; other Advanced topics remain stubs until Labs 1–5 deepen.
