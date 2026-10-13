# Stability pillar overview

**Engineering question:** Will the system remain stable, and how close is it to a stability boundary?

## Focus

Transient rotor-angle stability and **critical clearing time (CCT)** under stated fault/clearing rules. Finite-horizon simulation labels are **operational**, not asymptotic certificates.

## Learning path

1. [Stability labels and CCT](01_stability_and_cct.md)  
2. [Surrogate models for stability tasks](02_surrogate_stability.md)  
3. [Lab 5 — Stability and CCT](../900_labs/lab_05_stability_cct/index.md)

## Relation to foundations

Use the same SMIB reference from Lab 1. Trajectory accuracy alone does not imply correct CCT or safe decisions near the boundary.

## Status

Teaching narrative filled; executable CCT search notebooks come after Lab 1–2 tooling is stable. ANDES network cases use a pinned `envs/course_andes.yml` when introduced.
