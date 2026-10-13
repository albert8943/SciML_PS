# Stability labels and CCT

## Learning goals

- Define stable/unstable labels under an explicit horizon and criterion
- Define **critical clearing time (CCT)** as a scenario property
- Report signed CCT error and false-safe rate — not accuracy alone

## Reading

- Course report Lab 5; Weeks on CCT  
- Teaching adapt of vault CCT concept (no research campaign numbers)

## Critical clearing time

**CCT** is the longest fault-on duration for which the system remains transiently stable after clearing, under a **stated** stability rule (angle threshold, simulator flag, horizon, …).

Clearing later than CCT leads to instability (e.g. loss of synchronism) after clearance. CCT is a property of the **operating point + contingency + model + criterion**, not of a neural network.

### Operational search

Practitioners often estimate CCT by bisection or grid search over clearing time, assuming a monotone stable→unstable transition inside a bracket. If no valid bracket exists, **label the case** — do not invent a CCT.

## Metrics

| Metric | Meaning |
|--------|---------|
| Signed CCT error | Positive values overestimate available clearing time (dangerous) |
| Absolute CCT error | Magnitude of mistake |
| False-safe rate | Fraction of truly unstable cases predicted stable |

Accuracy alone can hide an unacceptable false-safe imbalance. Test **boundary-adjacent** scenarios separately from easy cases.

## Lab

- [Lab 5 — Stability and CCT](../900_labs/lab_05_stability_cct/index.md)

## Further reading

- Course report §15-style stability metrics discussion; B1 transient stability chapters

## Common misconceptions

- Calling a finite-horizon label a Lyapunov proof  
- Using trajectory NRMSE as a proxy for CCT quality  
- Ignoring bracket saturation in bisection
