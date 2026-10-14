# Machine learning for power-systems people

```{note} Maturity: Draft
Readable teaching prose; examples, figures, and exercises are still growing. See [Status and versions](../100_front/status_and_versions.md) and [Join and contribute](../100_front/contribute.md).
```

You already know models, measurements, and simulation. This page names the learning words these notes use, in power-system language. Training and neural networks: @bishop2024deep. Data and dynamical systems: @brunton2022datadriven. Physics-informed training: @karniadakis2021physics. Both readings of each word are in the [glossary](../990_reference/glossary.md#glossary-learning).

## A model is a function with knobs

A **neural network** is a flexible function. Its knobs are called **weights**. Weights are free numbers inside the function. They are separate from inertia $H$ and damping $D$. When a chapter says the estimands are $(H, D)$, those two stay named parameters with units and bounds. The network is only there to represent a trajectory or a missing term.

## Data

One **example** is one simulation run or one measured window. Inputs might be time, a clearing time, or a parameter value. Outputs might be rotor angle and speed over that window, or a stable/unstable label. A table of many runs is the dataset. The [Lab 1](../900_labs/lab_01_reference_sim/index.md) manifest is that table, written down.

## Loss, in the language of least squares

A **loss** is a single number that is small when the model agrees with the evidence you named. Least squares between a simulated angle and a measured angle is a loss. Training moves the knobs to reduce that number.

**Gradient descent** takes a step downhill on the loss. **Automatic differentiation** computes that downhill direction for you. One pass through the training examples is an **epoch**. You will see these words in [Automatic differentiation](../300_foundations/05_differentiation.md) and [Classical estimation](../300_foundations/07_classical_estimation.md). Classical least squares remains the baseline beside every neural estimator in this book.

## Generalization

A fit can match the runs used to train it and fail on a new disturbance. **Overfitting** means the model memorized the training runs. These notes split data by **scenario** (a different clearing time or a different fault), and they ask you to report the scenarios that were held out. A low loss on the training window is a training result. A held-out disturbance is the check.

## What "physics-informed" adds

A physics-informed neural network keeps the data loss and adds a **residual** of the differential equation. The swing equation you already trust becomes part of the number being minimized. The residual is small when the network's angle and speed satisfy that equation at a set of time points. Details: [Forward PINNs](../300_foundations/06_forward_pinn.md).

## Where to go

1. [Data and surrogates](../300_foundations/04_data_and_surrogates.md)
2. [Classical estimation](../300_foundations/07_classical_estimation.md) (the baseline you already know how to judge)
3. [Forward PINNs](../300_foundations/06_forward_pinn.md)

If you have never run a notebook, start with [Programming from zero](bridge_programming_from_zero.md) and [Your first lab](../100_front/first_lab_walkthrough.md). If the machine model itself should be refreshed, skim [SMIB dynamics](../300_foundations/02_smib_dynamics.md) for the units this book uses.
