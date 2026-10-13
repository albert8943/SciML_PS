# Stability pillar overview

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

## Status

Stability narrative deepened (classification, surrogates, direct methods). Executable SMIB CCT notebooks come after Lab 1–2 tooling is stable. Network path: summarize-then-link to ANDES; pin `envs/course_andes.yml`.
