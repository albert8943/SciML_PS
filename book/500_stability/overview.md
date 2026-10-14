# Stability pillar overview

```{note} Maturity: Draft
Readable teaching prose; examples, figures, and exercises are still growing. See [Status and versions](../100_front/status_and_versions.md) and [Join and contribute](../100_front/contribute.md).
```

**Engineering question:** Will the system remain stable, and how close is it to a stability boundary?

## Focus

Transient rotor-angle stability and **critical clearing time (CCT)** under stated fault/clearing rules. Finite-horizon simulation labels are **operational**, not asymptotic certificates.

## Learning path

1. [Stability labels and CCT](01_stability_and_cct.md) — IEEE/CIGRE placement, three cases, CCT metrics  
2. [Surrogate models for stability tasks](02_surrogate_stability.md) — classifier vs trajectory vs margin  
3. [Direct methods](04_direct_methods.md) — equal-area / energy as classical check  
4. [Lab 5 — Stability and CCT](../900_labs/lab_05_stability_cct/index.md) (SMIB first)  
5. [ANDES as network reference](03_andes_network_reference.md) — after SMIB CCT works; Kundur gallery as linked depth  

## Relation to foundations

Use the same SMIB reference from Lab 1. Trajectory accuracy alone does not imply correct CCT or safe decisions near the boundary. Network CCT (ANDES / Kundur) reuses the same SciML evaluation ideas on a larger plant — it does not replace Foundations.

## Discussion: what Stability methods can and cannot claim

| Can claim (with evidence) | Cannot claim |
|---------------------------|--------------|
| CCT error and false-safe count against the reference simulator, under a stated fault, clearing rule, and study window | A stability certificate beyond the study window or the tested faults |
| Agreement with the equal-area criterion on the classical SMIB | That a learned margin is protection-grade near the boundary |
| Ranking of surrogates under the **same** stability criterion | That a better trajectory fit implies a better CCT |

**Rule:** report false-safe errors separately from average error. Near the boundary, one optimistic mistake matters more than many small ones.

## Status

Stability narrative deepened (classification, surrogates, direct methods). Executable SMIB CCT notebooks come after Lab 1–2 tooling is stable. Network path: summarize-then-link to ANDES; pin `envs/course_andes.yml`.
