---
subtitle: Focus — dynamic modeling, stability assessment, and system identification
---

# Scientific Machine Learning (SciML) for Power Systems (PS)

Welcome. This book teaches **scientific machine learning for power-system applications**: methods in the service of concrete engineering tasks on the grid, not abstract algorithms alone. After this page we usually write the short form **SciML for PS**.

:::{warning} Under development — public preview (v0.x)
These are **living teaching notes**, not a finished textbook. Stub chapters, thin prep notebooks, and experimental PDF export are intentional while the core narrative and Labs 1–5 grow. Prefer the HTML site over the PDF snapshot. Versioning and chapter maturity labels: [Status and versions](100_front/status_and_versions.md). Experts and careful readers: [Join and contribute](100_front/contribute.md).
:::

**New here?** Start with [How to use this book](100_front/how_to_use.md), then [Preparation](200_prep/overview.md) → [Foundations](300_foundations/overview.md).

## Three applications

- **Dynamics** — How will the system evolve under specified inputs, parameters, and disturbances?
- **Stability** — Will the system remain stable, and how close is it to a stability boundary?
- **Identification** — Which parameters and dynamic relationships explain the measurements?

Shared tools (SMIB models, data and physics losses, classical baselines) come first in **Foundations**, then you deepen along one or more pillars. What each application *produces*: [Book map](100_front/book_map.md).

## Why this book?

Power-system SciML is scattered across papers, gallery notebooks, and research codes. This book keeps **one living narrative**: three engineering questions on a shared SMIB plant, classical baselines beside neural methods, and runnable labs. Methods appear when an application needs them, not as a method ladder. Interactive notebooks sit beside the prose so you can check claims on the same model you just read about.

New here? Also read [Advice to the student](100_front/advice.md).

## Explore the notes

::::{grid} 1 1 2 2

:::{card} Getting started
:link: 100_front/how_to_use.md

How to use the book, local preview, learning paths, and feedback.
:::

:::{card} Foundations
:link: 300_foundations/overview.md

Shared SMIB model and core SciML methods before the three pillars.
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

Product and site patterns for living computational notes were informed by public teaching sites such as the [EECS 245 course notes](https://notes.eecs245.org/) (Suraj Rampure; CC BY-NC-ND 4.0 — we link and reimplement patterns; we do not adapt their text). Method background for physics-informed training draws on [Physics-based Deep Learning](https://physicsbaseddeeplearning.org/) (Thuerey et al.; Apache-2.0 ideas cited as B5). Network simulation references use [ANDES](https://docs.andes.app/en/stable/) as an installed tool (GPL-3.0).

How this book sits next to other open SciML, AI-for-power, and PINN materials — including what we do **not** claim: [Related open resources](100_front/related_resources.md).

Typos and unclear pages: [Feedback](100_front/feedback.md).

**License:** content [CC BY-NC-SA 4.0](100_front/license.md); code MIT. Full terms on that page.
