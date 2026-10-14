# Book map

How the notes are organized. Use the left sidebar for day-to-day navigation; this page is the big picture. For every chapter and lab on one page, see the [Full outline](outline.md).

| Section | What you find here |
|---------|-------------------|
| **Front matter** | How to use, local preview, [running notebooks](running_notebooks.md), this map, [full outline](outline.md), learning paths, [related open resources](related_resources.md), [contribute](contribute.md), [status](status_and_versions.md), feedback, [license](license.md) |
| **Preparation** | Overview plus four diagnostic notebooks in the sidebar (stubs today: NumPy, ODEs, tiny MLP, gradients) |
| **Foundations** | Shared SMIB model and core SciML ideas (losses, forward/inverse PINN, baselines) |
| **Dynamics** | Deeper dynamic modeling and simulation (SciML for trajectories / vector fields) |
| **Stability** | Stability assessment (labels, CCT, surrogate stability; ANDES network bridge after SMIB) |
| **Identification** | Parameter estimation and system identification |
| **Advanced topics** | Synthesis (assessment → decision) plus optional extensions (operators, UQ, converters) |
| **Laboratories** | Assessed Labs 1–5 |
| **Reference** | Reading list and notation |

Read **Preparation → Foundations**, then deepen along **Dynamics**, **Stability**, or **Identification**. Labs sit beside the notes and cross-link from chapters.

This top-level layout is intentional and meant to stay stable as the notes grow: shared foundations, three applications, labs beside the prose, and a separate reference section. Semester week-by-week paths belong under [Learning paths](learning_paths.md), not as a rewrite of these sections.

## What each application produces

| Application | Engineering question | What you produce |
|-------------|----------------------|------------------|
| **Dynamic modeling and simulation** | How will the system evolve under specified inputs, parameters, and disturbances? | State trajectories, learned vector fields, hybrid dynamic models, parameterized response maps |
| **Stability assessment** | Will the system remain stable, and how close is it to a stability boundary? | Stable/unstable decisions, critical clearing time (CCT), empirical stability boundaries |
| **Parameter estimation and system identification** | Which parameters and dynamic relationships explain the measurements? | Inertia/damping estimates, controller parameters, learned missing terms, uncertainty estimates |

In the sidebar these appear as **Dynamics**, **Stability**, and **Identification**.
