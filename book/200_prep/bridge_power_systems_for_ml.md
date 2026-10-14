# Power systems for ML people

```{note} Maturity: Draft
Readable teaching prose; examples, figures, and exercises are still growing. See [Status and versions](../100_front/status_and_versions.md) and [Join and contribute](../100_front/contribute.md).
```

You already know models, data, and losses. This page names the power-system objects those tools will touch. The textbook treatment is @kundur2022power. Stability words follow the IEEE/CIGRE definitions [@kundur2004definition; @hatziargyriou2021definition]. Symbol-by-symbol translations sit in the [glossary](../990_reference/glossary.md#glossary-machine).

## The grid

Generators produce electrical power. Loads consume it. Transmission lines connect them. The machines must stay in step: their electrical frequency (50 Hz or 60 Hz, depending on the grid) is that shared rhythm. A generator's **rotor angle** is how far its spinning shaft has drifted from the rhythm. **Rotor speed** is how fast that angle is changing.

In machine-learning language, angle and speed are a short **state** sequence. A fault is an input event. The resulting time series is a trajectory you may later predict.

## One machine, one infinite bus

Almost every lab uses a **SMIB** plant: a single machine connected to an infinite bus. The infinite bus is a grid so large that its voltage and frequency stay fixed while the one machine moves. That keeps the equations small enough to learn on, and the same equations reappear in simulation, surrogates, stability labels, and parameter estimation.

The **swing equation** is Newton's law for the rotor, written in electrical units:

- **Inertia** resists a change in speed.
- **Damping** pulls the speed back toward the grid.
- The gap between mechanical power (from the turbine) and electrical power (sent to the grid) sets the acceleration.

In machine-learning language, inertia $H$ and damping $D$ are **parameters**. Forward labs treat them as known inputs. Identification labs treat them as the unknowns to estimate. They are named and bounded. They are separate from the neural network's weights.

## Faults, clearing, and the boundary

A **fault** (a short circuit) suddenly reduces the electrical power the machine can send. The rotor speeds up. **Clearing** means protective breakers remove the fault. If clearing is late, the angle runs away and the machine loses synchronism (it falls out of step with the grid).

**Critical clearing time (CCT)** is the latest clearing time that still leaves the machine in step, for one stated fault and one study window. In machine-learning language, CCT is a margin: a distance to a decision boundary. Stable or unstable is a label on that scenario. A small error in the trajectory can still flip the label when the case sits near the boundary. That is why this book reports CCT error and false-safe decisions together with trajectory error.

## Per-unit

Engineers scale power, voltage, and time to a chosen base so the numbers sit near 1. Labs here use per-unit power and radian angles. The dataset manifest records the base. A model trained in one base and tested in another is a different problem.

## Why a physics term appears in the loss

Labeled recordings from a real grid are scarce, and a wrong stability call has a safety cost. A **physics residual** asks the network to satisfy the swing equation, alongside matching the samples. That is the reason a data loss and a physics loss appear together. The chapter that writes both losses is [Forward PINNs](../300_foundations/06_forward_pinn.md).

## Where to go

1. [Problem framing](../300_foundations/01_problem_framing.md) (three tasks on this one plant)
2. [SMIB dynamics](../300_foundations/02_smib_dynamics.md) (the equation)
3. [Your first lab](../100_front/first_lab_walkthrough.md) if you want to see a trajectory before reading further

If programming itself is new, read [Programming from zero](bridge_programming_from_zero.md) first.
