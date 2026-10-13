# Dynamics pillar overview

**Engineering question:** How will the system evolve under specified inputs, parameters, and disturbances?

## Planned depth (stubs later)

- Surrogate rollouts and event interfaces
- Hybrid physics–ML dynamic models
- Multimachine trajectory tasks (after SMIB mastery)

## Labs

- Lab 1 (reference data), Lab 2 (surrogate vs PINN), Lab 4 (learned dynamics)

## Further practice (optional)

- After Labs 1–2: [ANDES PINN surrogate gallery](https://docs.andes.app/en/stable/gallery/pinn-surrogate.html) (SMIB + symbolic DAE path) — does not replace course labs  
- Renewables / frequency projects: [low-inertia IEEE 14 gallery](https://docs.andes.app/en/stable/gallery/low-inertia-freq.html)  
- Network reference overview: [ANDES as network reference](../500_stability/03_andes_network_reference.md)

## Model reduction and long-horizon rollouts

A learned dynamics model is usually trained on short windows but used for long rollouts. Two ideas help:

- **Reduced state.** Learn the dynamics in a small latent state (an encoder compresses the measured state, a learned map advances it, a decoder returns physical variables). For SMIB the full state is already small; the idea matters for multimachine and converter-rich systems.
- **Rollout error growth.** One-step accuracy does not guarantee multi-step accuracy, because errors feed back into the next prediction. Lab 4 should report error **versus horizon**, not one number.

Method background: B5 Thuerey et al., [model reduction and time series](https://physicsbaseddeeplearning.org/others-timeseries.html) (fast-forward overview with pointers to external code; check each linked implementation's own license).

## Discussion: what Dynamics methods can and cannot claim

| Can claim (with evidence) | Cannot claim |
|---------------------------|--------------|
| Trajectory error on stated test disturbances, horizons, and operating points | Accuracy on disturbances, horizons, or operating points outside the test set |
| Speed-up over the reference simulator for the same task | That a fast surrogate replaces the simulator for new topologies |
| Physics residual size, if a residual is reported | That a low residual means the physics is exactly satisfied |

**Rule:** every Dynamics result names its reference simulator (Lab 1), its test disturbances, and its horizon.

## Status

Overview stub only — grow independently after foundations.
