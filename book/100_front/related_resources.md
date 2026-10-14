# Related open resources

This page situates **SciML for PS** among nearby open materials. It is a positioning note for readers and collaborators, not a claim of uniqueness.

## Positioning (honest wording)

To our knowledge, there is **not yet** an established open, collaborative *living textbook* that organizes scientific machine learning around power-system **dynamics**, **stability assessment**, and **system identification** as three engineering applications with a shared plant, classical baselines, and an assessed lab spine.

Related research codes, short courses, general SciML notes, and energy-system Jupyter Books **do** exist. This book aims to fill the **teaching-product** gap: one long-lived narrative you can study, cite by version, and help improve. If you know a resource we have missed, please [tell us](feedback.md) so this page stays fair.

## Neighbors worth knowing

### Product patterns (how living notes are built)

| Resource | Role relative to this book |
|----------|----------------------------|
| [EECS 245 course notes](https://notes.eecs245.org/) (Rampure) | Living MyST notes + separate course portal; **CC BY-NC-ND 4.0** — we link and reimplement *patterns*, we do not adapt their text |
| [Physics-based Deep Learning](https://physicsbaseddeeplearning.org/) (Thuerey et al.) | Method textbook with runnable notebooks; ideas cited as B5, rewritten for SMIB |
| [The Turing Way](https://the-turing-way.netlify.app/), [Dive into Deep Learning](https://d2l.ai/), [Project Pythia](https://projectpythia.org/) | Models for governance, editions, and executable notebooks (patterns only) |

### General SciML (methods, not power-system applications)

| Resource | Role |
|----------|------|
| [Introduction to Scientific Machine Learning](https://predictivesciencelab.org/books/introduction-to-scientific-machine-learning/) (Bilionis, Purdue) | Probability-first SciML lecture notes |
| [Cornell Virtual Workshop: SciML](https://cvw.cac.cornell.edu/SciML) | Tutorial path on AD, PINNs, operators |
| [JHU SciML Course](https://github.com/drgona/SciML-Course) (Drgoňa) | Course materials on SciML for dynamical systems; related research includes SciML for power, but not this book’s three-pillar teaching spine |

### Power systems + AI / data (adjacent open teaching)

| Resource | Role |
|----------|------|
| [IEEE course notebooks: AI for Power and Energy Systems](https://github.com/enliten/IEEE-course_AI-for-Power-Energy-Systems) (Fran Li) | Modular Colab notebooks across AI tasks; includes a PINN frequency / swing module among load, power-flow, and optimization examples |
| [Data Science for Energy System Modelling](https://github.com/OpenEnergyPlatform/data-science-for-esm) (TU Berlin) | Jupyter Book on energy-system modelling with data — planning / modelling focus, not TSA / SciML ID |
| [Power Systems Optimization](https://github.com/power-systems-optimization-course/power-systems-optimization) | Open Julia/JuMP course on dispatch, UC, OPF, capacity planning |
| [Causality in Electricity Markets](https://github.com/dcacciarelli/my-causality-book) | Open tutorials on causal ML for markets |
| [MIT OCW: Seminar in Electric Power Systems](https://oercommons.org/courses/seminar-in-electric-power-systems) | Classical dynamics and transient stability OER (no SciML) |

### PINN / SciML research code for power dynamics (cite; do not treat as a textbook)

The DTU group around Spyros Chatzivasileiadis has published foundational papers and open code for PINNs on power-system dynamics and identification, plus toolboxes and tutorials (Colab demos, assignments, [PowerPINN](https://github.com/radiakos/PowerPINN), [PINNSim](https://github.com/jbesty/PINNSim)). See [downloads](http://www.chatziva.com/downloads.html). These are **research and tutorial artifacts**, not a collaborative living course book with the Dynamics / Stability / Identification spine used here.

Curated paper and tool lists such as [awesome-ml-power-systems](https://github.com/ArsamAryandoust/awesome-ml-power-systems) still point learners mainly to **general** ML textbooks; that gap is part of why this resource exists.

## How we use neighbors

- **Cite and link** public literature and docs; rewrite in teaching voice.
- **Do not** paste sealed research metrics or unpublished campaign results into student pages.
- **Do not** copy ND-licensed or unlicensed course text (EECS 245, Math 124 patterns are link-only).
- ANDES and similar simulators are **installed dependencies**, not redistributed sources.

Attribution modes and register: maintainer file `docs/references/attribution_register.md`. Licence summary: [License](license.md).

## Suggest a missing neighbor

If you know another open book, course, or long-lived notes site that covers this niche, open a [Feedback](feedback.md) issue or discussion with the URL. We will update this page when the comparison changes.
