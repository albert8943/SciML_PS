---
subtitle: Focus — dynamic modeling, stability assessment, and system identification
---

# Scientific Machine Learning (SciML) for Power Systems (PS)

Welcome. This book teaches **scientific machine learning for power-system applications**: methods in the service of concrete engineering tasks on the grid, with the engineering question stated first. After this page we usually write the short form **SciML for PS**.

Machine-learning readers and power-systems readers share these notes so each group can learn enough of the other field to work on the same plant. Students, teachers, engineers, utility workers, and researchers may open any chapter. [Start here](100_front/start_here.md) matches a route to your background and your role.

:::{warning} Under development — public preview (v0.x)
These are **living teaching notes**, not a finished textbook. Stub chapters, thin prep notebooks, and experimental PDF export are intentional while the core narrative and Labs 1–5 grow. Prefer the HTML site over the PDF snapshot. Versioning and chapter maturity labels: [Status and versions](100_front/status_and_versions.md). Experts and careful readers: [Join and contribute](100_front/contribute.md).
:::

**Choose an entrance:** [Start here](100_front/start_here.md). Each chapter then says what it assumes.

::::{grid} 1 1 2 2

:::{card} Complete beginner
:link: 200_prep/bridge_programming_from_zero.md

Programming words, then a first lab in the browser. No install required to start.
:::

:::{card} From machine learning
:link: 200_prep/bridge_power_systems_for_ml.md

Generators, swing equations, faults, and CCT, in the language of states and losses.
:::

:::{card} From power systems
:link: 200_prep/bridge_ml_for_power_systems.md

Losses, training, and generalization, in the language of least squares and study cases.
:::

:::{card} Teachers
:link: 100_front/learning_paths.md

Course overlays on one book (Teachers section). Week plans can be shared back.
:::

:::{card} Researchers and practitioners
:link: 100_front/learning_paths.md

Practitioners open the application they work on; researchers use the researcher route on the same Learning paths page.
:::

::::

## Three applications

- **Dynamics** (dynamic modeling) — How will the system evolve under specified inputs, parameters, and disturbances?
- **Stability** (stability assessment) — Will the system remain stable, and how close is it to a stability boundary?
- **Identification** (system identification) — Which parameters and dynamic relationships explain the measurements?

Shared tools (SMIB models, data and physics losses, classical baselines) come first in **Foundations**, then you deepen along one or more pillars. What each application *produces*: [Book map](100_front/book_map.md).

## Why this book?

Power-system SciML is scattered across papers, gallery notebooks, and research codes. This book keeps **one living narrative**: three engineering questions on a shared SMIB plant, classical baselines beside neural methods, and runnable labs. Methods appear when an application needs them, not as a method ladder. Interactive notebooks sit beside the prose so you can check claims on the same model you just read about.

**PINN is an early deep path, not the whole book.** Labs 2–3 use physics-informed residuals because the swing equation makes that residual easy to write and to ablate. Other SciML families (Neural ODEs, operator learning, differentiable simulation) appear later on the same plant when the question needs them. The method map: [SciML method families](300_foundations/00_sciml_landscape.md). Where each family is practiced: [Laboratories](900_labs/README.md).

Also read [Advice to readers](100_front/advice.md). How methods show up in reading order: [How to use this book](100_front/how_to_use.md). The sidebar order is one route among several: [Learning paths](100_front/learning_paths.md).

## Explore the notes

::::{grid} 1 1 2 2

:::{card} Getting started
:link: 100_front/how_to_use.md

Entrances, how pages work, local preview, and feedback.
:::

:::{card} Full outline
:link: 100_front/outline.md

Every chapter and lab on one page, with maturity labels.
:::

:::{card} Preparation
:link: 200_prep/overview.md

Self-check and four short notebooks before Foundations.
:::

:::{card} Foundations
:link: 300_foundations/overview.md

Shared SMIB model and core SciML methods before the three pillars.
:::

:::{card} Dynamics
:link: 400_dynamics/overview.md

How will the system evolve under inputs, parameters, and disturbances?
:::

:::{card} Stability
:link: 500_stability/overview.md

Will the system remain stable, and how close is it to the boundary?
:::

:::{card} Identification
:link: 600_identification/overview.md

Which parameters and dynamics explain the measurements?
:::

:::{card} Advanced topics
:link: 700_advanced/overview.md

From assessment to decision, plus optional extensions.
:::

:::{card} Laboratories
:link: 900_labs/README.md

Assessed Labs 1–5 beside the notes.
:::

:::{card} Reference
:link: 990_reference/reading_list.md

Reading list and notation.
:::

::::

:::{note} Prefer the live notes
Work in the **online** book. The navbar **PDF** is a snapshot (experimental; interactive figures may flatten). Its cover **Last updated** stamp follows the latest git commit.
:::

Portable methods and public citations only — no sealed research campaign results on student pages.

## Acknowledgements, feedback, and licence

Product and site patterns for living computational notes were informed by public teaching sites such as the [EECS 245 course notes](https://notes.eecs245.org/) (Suraj Rampure; CC BY-NC-ND 4.0 — we link and reimplement patterns; we do not adapt their text). Method background for physics-informed training draws on [Physics-based Deep Learning](https://physicsbaseddeeplearning.org/) [@thuerey2021pbdl] (Apache-2.0; ideas cited, not copied). Network simulation references use [ANDES](https://docs.andes.app/en/stable/) as an installed tool (GPL-3.0).

How this book sits next to other open SciML, AI-for-power, and PINN materials — including what we do **not** claim: [Related open resources](100_front/related_resources.md).

Typos and unclear pages: [Feedback](100_front/feedback.md).

**License:** content [CC BY-NC-SA 4.0](100_front/license.md); code MIT. Full terms on that page.
