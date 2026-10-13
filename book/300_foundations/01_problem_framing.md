# Problem framing

## Learning goals

- Formulate forward dynamics, stability assessment, and inverse estimation as distinct tasks
- Distinguish **states** from **parameters**
- Contrast forward simulation with inverse identification

## Reading

- B1 for power-system context; R1 for the SciML landscape  
- [Book map](../100_front/book_map.md) for the three applications

## Three tasks (same SMIB, different questions)

| Task | Given | Infer | Evaluate |
|------|-------|-------|----------|
| Forward dynamics | Model, initial state, inputs, parameters $\theta$ | Trajectories $x(t)$ | Trajectory / rollout error |
| Stability assessment | Operating point, contingency, clearing rule | Stable/unstable or CCT | False-safe rate, CCT error |
| Inverse estimation | Measurements (+ known inputs) | Parameters $\theta$ (and often $x(t)$) | Recovery, identifiability, held-out events |

Do not mix metrics: a model with low trajectory NRMSE can still be **false-safe** near a stability boundary, or recover the **wrong** parameters.

## State vs parameter

**State estimation** asks: *what is the system doing over time?*  
Examples: rotor angle $\delta(t)$, speed $\omega(t)$. States **change with time**.

**Parameter estimation** asks: *what are the fixed unknown constants in the model?*  
Teaching examples: inertia $H$, damping $D$. (Converter virtual inertia / droop appear later as electives — keep estimands explicit.)

Analogy:

- **State** = movie frames  
- **Parameter** = camera / machine settings  

A network can draw a beautiful trajectory while guessing the wrong settings. Nice plots are not enough; later labs need recovery checks and held-out disturbances.

## Forward vs inverse

```text
FORWARD:   known θ  +  inputs / disturbance  →  trajectories x(t)
INVERSE:   measured trajectories (+ known inputs)  →  unknown θ
```

| Style | Typical goal |
|-------|----------------|
| Forward PINN / surrogate | Fast trajectories when $\theta$ is known or assumed |
| Inverse PINN | Calibrate named $\theta$ from PMU-like data |
| Classical simulator (e.g. ANDES later) | High-fidelity forward reference |

Changing $H$ in a simulator and re-running is **forward**. Given frequency after a load step and asking for $H$ is **inverse**.

## Worked example

Specify one SMIB fault-on/clearing case in writing:

1. What is known? What is unknown?  
2. Is the goal a trajectory, a stability label/CCT, or a parameter vector?  
3. Which metric would decide success?

## Lab

- Foundations continue into [Lab 1 — reference simulation](../900_labs/lab_01_reference_sim/index.md)

## Further reading

- Kundur (B1) for swing-equation context; R1 for the method families

## Common misconceptions

- “Good waveform fit proves parameters are correct.” — No.  
- “PINN replaces the need to define the engineering task.” — No; the task defines the loss and metrics.  
- Treating converter GFM knobs and classical $(H,D)$ as interchangeable without saying so.
