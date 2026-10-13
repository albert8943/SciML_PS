# Reference simulation

## Learning goals

- Build a transparent numerical SMIB reference with an event schedule
- Document solver settings, failures, and scenario-based data splits
- Treat the simulator as scientific ground truth for later ML comparisons

## Reading

- Course report Lab 1; Weeks 2–4  
- Numerical ODE notes in prep package (`200_prep`)

## Why a reference first

Before PINNs or surrogates, you need:

1. Equations and parameters in one place  
2. An event log (fault inception, clearing, horizon)  
3. A convergence / failure policy (do not silently delete failed runs)  
4. A **manifest**: scenario IDs, seeds, solver tolerances, units  

Machine learning cannot repair an undocumented dataset.

## Minimum deliverables (Lab 1)

- SMIB integrator (teaching code in `src/sciml_ps`)  
- At least **two** numerical settings compared (e.g. step size or method)  
- Dataset split **by scenario**, not by randomly shuffling time points across events  
- Flagged numerical failures retained as records  

## Worked example

Compare trajectories for the same physical scenario at two time steps. Report max $|\delta|$ difference and whether the stability label (if defined) flips.

## Lab

- [Lab 1 — Reference simulation and scientific dataset](../900_labs/lab_01_reference_sim/index.md)

## Further reading

- Course report §6.2 Lab 1; §6.3 experiment record fields

## Common misconceptions

- Deleting “ugly” trajectories that failed to converge  
- Splitting every time sample randomly into train/test (leaks the same event)  
- Calling ANDES optional until network labs — classical SMIB does not require ANDES
