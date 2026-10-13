---
subtitle: Focus — dynamic modeling, stability assessment, and system identification
---

# Scientific Machine Learning (SciML) for Power Systems (PS)

Welcome. This book is about **using SciML for power-system applications**: scientific machine learning methods in the service of concrete engineering tasks on the grid, not as abstract algorithms alone. After this page we usually write the short form **SciML for PS**.

The three applications:

| Application | Engineering question | What you produce |
|-------------|----------------------|------------------|
| **Dynamic modeling and simulation** | How will the system evolve under specified inputs, parameters, and disturbances? | State trajectories, learned vector fields, hybrid dynamic models, parameterized response maps |
| **Stability assessment** | Will the system remain stable, and how close is it to a stability boundary? | Stable/unstable decisions, critical clearing time (CCT), empirical stability boundaries |
| **Parameter estimation and system identification** | Which parameters and dynamic relationships explain the measurements? | Inertia/damping estimates, controller parameters, learned missing terms, uncertainty estimates |

In the book these appear as **Dynamics**, **Stability**, and **Identification**. Shared tools (SMIB models, data and physics losses, classical baselines) come first in **Foundations**, then you deepen along one or more of the three applications.

## Status

Foundations prose and early labs (especially Labs 1 and 3) are in place. Some pillar chapters and labs remain brief by design and will deepen over time.

:::{note} Online book vs PDF
Prefer the **online** book while you work. The PDF export is experimental: interactive plots become static or may be omitted.
:::

## How to navigate

- Start with [How to use this book](100_front/how_to_use.md) and the [book map](100_front/book_map.md).
- To run the site on your machine, follow [Preview this book locally](100_front/preview_locally.md) (`scripts/preview.ps1` or `jupyter book start`).
- Work through **Preparation** → **Foundations**, then deepen along **Dynamics**, **Stability**, or **Identification**.
- Assessed labs live under **Laboratories** (`900_labs`).

## Content policy (short)

Portable methods and public citations only. No sealed research campaign results in student-facing pages.
