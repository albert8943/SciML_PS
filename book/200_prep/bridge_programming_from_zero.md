# Programming from zero

```{note} Maturity: Draft
Readable teaching prose; examples, figures, and exercises are still growing. See [Status and versions](../100_front/status_and_versions.md) and [Join and contribute](../100_front/contribute.md).
```

This page is for readers who have not programmed before. You can run the first laboratory without installing anything. A longer book on data and dynamical systems, when you want one, is @brunton2022datadriven.

## Words you will see

| Word | Meaning in these notes |
|------|------------------------|
| Python | The programming language used in the labs |
| Notebook | A web page made of text boxes and code boxes. You read the text and run the code |
| Cell | One box. A text cell explains. A code cell computes |
| Run | Ask the computer to carry out that one cell. Use the play button, or press Shift+Enter |
| Kernel | The live Python session behind the notebook. Restarting the kernel forgets earlier cells, so you run the notebook again from the top |
| Package | Reusable code with a name. The teaching package in this book is called `sciml_ps` |
| Error | A red message. Read the last line. It usually says what was missing |

The [first-lab walkthrough](../100_front/first_lab_walkthrough.md) points at each one while you use it.

## Run one notebook today

1. Open [Your first lab](../100_front/first_lab_walkthrough.md).
2. Follow the Google Colab steps (a free browser session). Binder is the fallback if you prefer not to use a Google account.
3. Stop when you see a plot of rotor angle against time. That means the notebook ran.

What you should see after the setup cell: a line that ends with `imports ok`.

## Practice after that

The four notebooks under [Preparation](overview.md) are the next practice (arrays, a small differential equation, a tiny neural fit, gradients). They are still stubs. Use Lab 1 for a complete run, and treat Preparation as optional drills while those notebooks grow.

If a later chapter feels hard only because of the code, come back to this page and to the walkthrough's troubleshooting list.

## Where to go next

| If you also need | Read |
|------------------|------|
| The power-system story | [Power systems for ML people](bridge_power_systems_for_ml.md) |
| The learning story | [Machine learning for power-systems people](bridge_ml_for_power_systems.md) |
| A map of the whole book | [Start here](../100_front/start_here.md) |
