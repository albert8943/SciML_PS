# Advice to readers

## How to read a page

Most chapter pages follow the same order: learning goals → reading → worked example → lab → misconceptions. Skim the goals and the **Before you start** box first. If a word is unfamiliar, open the [glossary](../990_reference/glossary.md). Then read the example and open the lab notebook. Misconceptions are worth reading even when the rest felt easy.

You may skip a chapter when the Before you start box is already satisfied. [Start here](start_here.md) and [Learning paths](learning_paths.md) list routes by background and by role.

## If you are new to programming

Run the notebook before you try to understand every line. [Your first lab](first_lab_walkthrough.md) is numbered and says what you should see. Restarting the kernel and running all cells from the top fixes many early errors.

## If you come from machine learning

Respect units, per-unit bases, and operating limits. A trajectory error is one score. Test on a disturbance the model did not train on, and report stability labels and CCT beside that error when the chapter is about security. Inertia and damping are named parameters with bounds. They are separate from network weights. Do not treat every neural method as a PINN — read the [SciML method families](../300_foundations/00_sciml_landscape.md) map first.

## If you come from power systems

A low training loss is a fit, and a held-out disturbance is the check. Ask whether a fitted $(H, D)$ is the physical constant in the model or an equivalent value that absorbed model error. Classical least squares stays beside the neural estimator so you can see what the extra machinery changed. In these notes, a PINN means the swing-equation residual enters the loss (Labs 2–3). Lab 4 and Lab 5 are other SciML jobs on the same plant — learned dynamics and CCT margins — not more PINN chapters by another name.

## Run the notebook while you read

These notes are meant to be used with code open. Open prep notebooks from the **Preparation** sidebar (they may still be stubs) and laboratory notebooks from **Laboratories**. Execute cells as you go. Reading alone is not enough for Labs 1–5. Browser steps: [Your first lab](first_lab_walkthrough.md). Local, Binder, and Colab: [Running notebooks](running_notebooks.md).

## State units, bounds, and test disturbances

Every fitted parameter and every stability label needs a contract: units (or per-unit base), bounds, and which disturbance or clearing time was used for training versus testing. A low trajectory error without that contract is not a result this course accepts.

## Prefer the live site for labs

Use the HTML book for notebooks. The PDF is a snapshot; interactive figures and runnable cells may flatten. Prefer a Chromium-based browser (Chrome, Edge, or similar) for smoother scrolling and interactive figures.

## Ask for help early

Typos, unclear steps, and broken links: [Feedback](feedback.md). Do not paste confidential research data or grades into public issues. A useful early contribution is a glossary row that translates a term into the other field: [Join and contribute](contribute.md).

## Honesty about metrics

Report what you measured (RMSE, CCT error, false-safe count, held-out disturbance) against a named reference simulator. Do not claim physical parameter recovery or protection-grade CCT from a single training loss.
