# Glossary

```{note} Maturity: Draft
Readable teaching prose; examples, figures, and exercises are still growing. See [Status and versions](../100_front/status_and_versions.md) and [Join and contribute](../100_front/contribute.md).
```

The same word often means one thing in a power-system course and another in a machine-learning course. This page gives both readings. Symbols and unit rules are on [Notation](notation.md). Textbook depth: @kundur2022power for the machine, @bishop2024deep for training.

Contributions that add a row, or that correct a translation, are welcome: [Join and contribute](../100_front/contribute.md).

(glossary-machine)=
## The machine and the grid

| Term | Plain meaning | Power-systems view | ML view | First used on |
|------|---------------|--------------------|---------|---------------|
| Grid | Generators, loads, and lines that must stay in step | The network under study | The plant that generates the data | [Power systems for ML people](../200_prep/bridge_power_systems_for_ml.md) |
| Generator | A machine that converts mechanical rotation into electrical power | The device whose rotor angle we track | The source of the state trajectory | [SMIB dynamics](../300_foundations/02_smib_dynamics.md) |
| Infinite bus | A grid so large its voltage and frequency stay fixed | The far end of a SMIB model | A constant boundary condition | [SMIB dynamics](../300_foundations/02_smib_dynamics.md) |
| SMIB | Single machine, infinite bus | The shared teaching plant in every lab | The data-generating system reused across tasks | [Foundations overview](../300_foundations/overview.md) |
| Frequency | How fast the shared electrical rhythm repeats (50 Hz or 60 Hz) | A system operating quantity | A slow variable beside rotor speed | [Power systems for ML people](../200_prep/bridge_power_systems_for_ml.md) |
| Fault | A short circuit or similar sudden event | The contingency in a stability study | An input event that changes the dynamics | [Stability labels and CCT](../500_stability/01_stability_and_cct.md) |
| Clearing | Breakers remove the fault at a chosen time | A protection action and a study parameter | An event time in the input | [Lab 1](../900_labs/lab_01_reference_sim/index.md) |
| Synchronism | The machine stays in step with the grid | The operational stability outcome | The positive class, when labels are used | [Stability labels and CCT](../500_stability/01_stability_and_cct.md) |

(glossary-quantities)=
## States, parameters, and units

| Term | Plain meaning | Power-systems view | ML view | First used on |
|------|---------------|--------------------|---------|---------------|
| State | A quantity that moves in time | Rotor angle and speed | The sequence the model predicts | [Problem framing](../300_foundations/01_problem_framing.md) |
| Parameter | A quantity treated as fixed during one simulation | Inertia, damping, network data | A named unknown, separate from network weights | [Problem framing](../300_foundations/01_problem_framing.md) |
| Rotor angle $\delta$ | How far the shaft has drifted from the grid rhythm | A state, in radians | One channel of the trajectory | [SMIB dynamics](../300_foundations/02_smib_dynamics.md) |
| Rotor speed $\omega$ | How fast the angle is changing | A state | The other channel of the trajectory | [SMIB dynamics](../300_foundations/02_smib_dynamics.md) |
| Inertia $H$ | Resistance to a change in speed | A machine constant, in seconds | A named estimand in Lab 3 | [SMIB dynamics](../300_foundations/02_smib_dynamics.md) |
| Damping $D$ | A term that pulls speed back toward the grid | A machine constant in the swing equation | The other Lab 3 estimand | [SMIB dynamics](../300_foundations/02_smib_dynamics.md) |
| Per-unit | A scaling so powers and voltages sit near 1 | The unit system of the labs | A preprocessing choice that must match at test time | [Notation](notation.md) |
| Operating point | Power, voltage, and equilibrium before the event | The prefault condition | A feature, or a conditioner, of the example | [Problem framing](../300_foundations/01_problem_framing.md) |
| Trajectory | Angle and speed over a time window | A simulation result | The regression target | [Reference simulation](../300_foundations/03_reference_simulation.md) |
| Disturbance | The event you apply (fault, clearing time, input) | A study scenario | The axis you split train and test on | [Lab 1](../900_labs/lab_01_reference_sim/index.md) |

(glossary-learning)=
## Learning and losses

| Term | Plain meaning | Power-systems view | ML view | First used on |
|------|---------------|--------------------|---------|---------------|
| Neural network | A flexible function with many knobs | A curve-fit or a dynamics model, depending on the lab | The parameterized function being trained | [Machine learning for power-systems people](../200_prep/bridge_ml_for_power_systems.md) |
| Weights | The knobs inside that function | Distinct from $H$ and $D$ | The parameters gradient descent updates by default | [Machine learning for power-systems people](../200_prep/bridge_ml_for_power_systems.md) |
| Loss | One number that is small when the model agrees with the evidence you named | Comparable to a weighted squared error | The training objective | [Classical estimation](../300_foundations/07_classical_estimation.md) |
| Data loss | The part of the loss that matches samples | Fit to the measured or simulated trajectory | Supervised error | [Forward PINNs](../300_foundations/06_forward_pinn.md) |
| Physics residual | The swing equation evaluated on the network's prediction | The equation you already trust, written as an error | An extra term in the loss | [Forward PINNs](../300_foundations/06_forward_pinn.md) |
| Training | Adjusting knobs so the loss falls | An estimation procedure | Gradient descent for a set number of epochs | [Automatic differentiation](../300_foundations/05_differentiation.md) |
| Epoch | One pass through the training examples | One sweep of the identification records | One optimization epoch | [Machine learning for power-systems people](../200_prep/bridge_ml_for_power_systems.md) |
| Surrogate | A learned stand-in for the simulator | A faster model of trajectories or labels | A supervised model | [Data and surrogates](../300_foundations/04_data_and_surrogates.md) |
| PINN | A network trained with data loss and a physics residual | The equation is part of the fit | Collocation-style physics-informed training | [Forward PINNs](../300_foundations/06_forward_pinn.md) |
| Neural ODE | A numerical solver whose right-hand side includes a learned piece | The integrator stays visible | A different SciML branch from collocation PINNs | [Neural ODEs and hybrid models](../300_foundations/10_neural_ode_hybrid.md) |
| Overfitting | A close fit on the training runs and a poor fit on new ones | A model that fails on the next disturbance | Memorization of the training set | [Machine learning for power-systems people](../200_prep/bridge_ml_for_power_systems.md) |

(glossary-checks)=
## Checks and honesty

| Term | Plain meaning | Power-systems view | ML view | First used on |
|------|---------------|--------------------|---------|---------------|
| CCT | Latest clearing time that still leaves the machine in step, for one scenario | A security margin from a stated fault and window | A decision margin for that scenario | [Stability labels and CCT](../500_stability/01_stability_and_cct.md) |
| False-safe | Calling a case stable when the reference says it is unstable | The dangerous direction of a stability error | A one-sided classification error | [Stability labels and CCT](../500_stability/01_stability_and_cct.md) |
| Identifiability | Whether the measurements can determine the named parameters | Excitation, noise, and model structure | Whether the loss has a unique parameter answer | [Identifiability](../300_foundations/08_identifiability.md) |
| Physical parameter | The constant in the model you wrote down | Nameplate or model-sheet meaning, with units | Keeps the nameplate meaning when the model matches the plant | [Physical vs equivalent parameters](../600_identification/02_physical_vs_equivalent.md) |
| Equivalent parameter | The number that fits the records when the model is incomplete | An effective value, still useful inside its test | A fitted value whose meaning is the fit, not the nameplate | [Physical vs equivalent parameters](../600_identification/02_physical_vs_equivalent.md) |
| Scenario split | Train on some disturbances and test on others | Held-out faults or clearing times | The generalization check this book asks for | [Lab 1](../900_labs/lab_01_reference_sim/index.md) |
