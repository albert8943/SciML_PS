# Preparation overview

## Learning goals

- Confirm Python/NumPy fluency for array workflows
- Integrate a simple ODE and plot trajectories
- Fit a small neural regression model and compute gradients

## Prep package (four notebooks)

| Notebook | Focus |
|----------|--------|
| [`nb01_numpy_basics.ipynb`](nb01_numpy_basics.ipynb) | Arrays, broadcasting, plotting |
| [`nb02_ode_integration.ipynb`](nb02_ode_integration.ipynb) | `solve_ivp` on a damped oscillator |
| [`nb03_nn_regression.ipynb`](nb03_nn_regression.ipynb) | Tiny MLP curve fit (NumPy or PyTorch) |
| [`nb04_gradients.ipynb`](nb04_gradients.ipynb) | Manual vs AD gradients |

## Diagnostic

After the four notebooks, simulate a damped oscillator and fit a simple regression model to its samples. If that is painful, finish a programming bridge course before Lab 1.

## Maths refresher (optional, external)

If linear algebra or multivariable calculus feels rusty, these **external** sections from the [EECS 245 course notes](https://notes.eecs245.org/) (Suraj Rampure, University of Michigan; **CC BY-NC-ND 4.0**) are useful background. We **link only** — we do not copy or adapt their text (ND forbids distributing derivatives). Read them on their site; then return here for power-system examples.

| Topic | EECS 245 section | Used in SciML for PS |
|-------|------------------|----------------------|
| Partial derivatives | [Partial derivatives](https://notes.eecs245.org/simple-linear-regression/partial-derivatives) | [Automatic differentiation](../300_foundations/05_differentiation.md) |
| Least squares | [Least squares](https://notes.eecs245.org/simple-linear-regression/least-squares) | [Classical estimation](../300_foundations/07_classical_estimation.md), Lab 3 |
| Gradients and gradient descent | [Gradient descent](https://notes.eecs245.org/gradients/gradient-descent), [convexity](https://notes.eecs245.org/gradients/convexity) | Training and inverse fits |
| Eigenvalues | [Eigenvalues and eigenvectors](https://notes.eecs245.org/eigenvalues-and-eigenvectors/eigenvalues-eigenvectors) | Small-signal / modal ideas (later) |
| SVD / low-rank / PCA | [Low-rank approximation](https://notes.eecs245.org/singular-value-decomposition/low-rank-approximation), [PCA](https://notes.eecs245.org/singular-value-decomposition/principal-components-analysis) | [Identifiability](../300_foundations/08_identifiability.md), model reduction |

Reading-list ID: **M-E245**.

## What is not in Preparation

**ANDES** (network power-system simulator) is **not** part of this section. Lab 1 uses a small SMIB helper without ANDES. You meet ANDES later if a stability / CCT lab or network chapter needs it (separate environment). Tool docs: [Reference — Reading list](../990_reference/reading_list.md).

## Next

- [Foundations overview](../300_foundations/overview.md)
