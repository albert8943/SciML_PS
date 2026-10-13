# From assessment to decision

## Learning goals

- See how the three book applications connect in one operating-point loop
- Distinguish **finished teaching labs** from a **long-horizon** digital-twin programme
- Avoid claiming a finished twin or protection-grade automation

## Reading

- [Identification overview](../600_identification/overview.md)  
- [Dynamics overview](../400_dynamics/overview.md)  
- [Stability overview](../500_stability/overview.md)  
- Maintainer career alignment: `docs/guides/website_career_to_book.md` (not student-required)

## The three applications in one loop

```text
Identification  →  calibrated parameters / model
        ↓
Dynamics        →  fast trajectories (simulator or SciML surrogate)
        ↓
Stability       →  TSA label and CCT (or other) margin
        ↓
Decision        →  contingency screen, planning study, operator attention
```

Labs practice pieces of this loop on a transparent SMIB plant:

| Piece | Typical lab |
|-------|-------------|
| Reference trajectories | Lab 1 |
| Surrogate vs physics-informed forward model | Lab 2 |
| Parameter recovery $(H, D)$ | Lab 3 |
| Learned dynamics generalization | Lab 4 |
| CCT and false-safe honesty | Lab 5 |

## Building toward a measurement-informed twin

A **grid digital twin**, in this teaching sense, is a **living model of the dynamics**, not a 3D plant replica:

```text
Grid / PMU-like measurements
    → parameter / model update (Identification)
    → dynamic model
    → physics-informed or hybrid surrogate (Dynamics)
    → security margins such as CCT (Stability)
    → operator-facing or planning decision
```

That programme is a **career-scale** direction. Published teaching evidence in this book is strongest on Foundations + classical SMIB SciML tasks. Treat the twin loop as **aspiration and synthesis**, not as a claim that the course already ships a twin.

## Honesty rules

- Finite-horizon CCT searches are planning-oriented unless otherwise certified.  
- Surrogates inherit the criterion and plant of their training / reference data.  
- Converter-rich and cyber-physical extensions belong in later electives after Labs 1–5 run.

## Further reading

- Stability: [CCT](../500_stability/01_stability_and_cct.md), [surrogates](../500_stability/02_surrogate_stability.md), [direct methods](../500_stability/04_direct_methods.md)  
- Reading list R-K04, R-H21; optional software pointer S-PINN-TSA  

## Common misconceptions

- “Digital twin means a visualization of substations.”  
- “Finishing Lab 5 means the twin loop is done.”  
- Collapsing binary TSA accuracy with operational margin decisions.  
