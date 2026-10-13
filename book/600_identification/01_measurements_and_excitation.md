# Measurements and excitation

## Learning goals

- Specify observation channels, noise models, and window lengths
- Design excitation so target parameters are informative
- Tie measurement contracts to Lab 3 protocols

## Reading

- Course report Lab 3; foundations identifiability chapter

## Measurement contract

Before fitting, write down:

| Field | Example (SMIB teaching) |
|-------|-------------------------|
| Channels | $\delta(t)$ and/or $\omega(t)$ (or PMU-like proxies) |
| Sampling | $\Delta t$, window $[t_0,t_1]$ |
| Noise | e.g. i.i.d. Gaussian on $\omega$ with stated $\sigma$ |
| Known inputs | $P_m$, event times |
| Unknowns | $(H,D)$ inside bounds |

## Excitation

A single mild load step may leave $D$ nearly flat on the loss surface. Prefer:

- Clear fault-on/clearing swings (Lab 1 events), or  
- Multiple magnitudes / clearing times, with at least one **held-out** event for validation  

## Worked example

Compare a 2-D $(H,D)$ loss surface for a short clearing time vs a longer (still stable) clearing time. Which experiment tightens the valley along $D$?

## Lab

- [Lab 3](../900_labs/lab_03_inertia_damping_id/index.md)

## Common misconceptions

- Using the same event for training and “validation” without saying so  
- Estimating two weakly excited parameters and claiming both are physical  
- Changing noise between LS and PINN comparisons
