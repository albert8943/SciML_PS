# Surrogate models for stability tasks

## Learning goals

- Separate trajectory error from boundary / CCT decision error
- Place a learned surrogate inside an operational CCT search carefully
- Require classical simulation baselines on the same scenarios

## Reading

- Course report Lab 2 and Lab 5  
- Forward PINN trajectory surrogate idea (foundations + vault teaching adapt)

## Forward surrogates for TSA

A **forward** surrogate (supervised network or forward PINN) predicts trajectories quickly for many clearing times or operating points. CCT search may call the surrogate instead of the full simulator — but then CCT error and false-safe rate must be reported against the **reference** simulator.

| Safe practice | Unsafe practice |
|---------------|-----------------|
| Same fault, clearing action, horizon, criterion | Mixing criteria between surrogate and reference |
| Boundary-focused test set | Only easy stable cases |
| Signed CCT error + false-safe | Accuracy-only leaderboard |

## Worked example

On SMIB Lab 1 scenarios, compare CCT from dense reference simulation vs CCT from a surrogate with a coarse time grid. Where do rankings disagree?

## Lab

- [Lab 5](../900_labs/lab_05_stability_cct/index.md); trajectory models from [Lab 2](../900_labs/lab_02_surrogate_vs_pinn/index.md)

## Further reading

- [Forward PINNs](../300_foundations/06_forward_pinn.md); landscape page

## Common misconceptions

- “Fast surrogate ⇒ trustworthy CCT”  
- Retraining on the CCT test bracket without disclosure  
- Skipping classical energy-function or TDS baselines when available
