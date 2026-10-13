# Lab 5 — Stability and CCT

## Goals

Create reference labels and CCT brackets on classical SMIB (Lab 1 tooling), then evaluate a learned surrogate or forward PINN near the boundary. Report signed and absolute CCT errors, false-safe decisions, and one case where trajectory ranking and CCT ranking disagree.

## Prerequisites

- [Lab 1](../lab_01_reference_sim/index.md)  
- Prefer also [Lab 2](../lab_02_surrogate_vs_pinn/index.md)  
- Chapters: [CCT](../../500_stability/01_stability_and_cct.md), [surrogate stability](../../500_stability/02_surrogate_stability.md)

## Reference CCT (no ML yet)

Using `simulate_smib` / `angle_stable`:

1. Fix prefault state and fault inception  
2. Sweep or bisect clearing time until the operational label flips  
3. Record bracket width and tolerance  

## Learned CCT (after Lab 2)

Replace the inner trajectory call with a surrogate; keep the **same** stability rule. Compare $\hat{t}_{\mathrm{CCT}}$ to the reference CCT.

## Deliverables

- Reference CCT table for ≥3 operating / fault settings  
- Signed CCT errors for the learned method  
- False-safe count on a boundary-focused set  
- One disagreement case write-up  

## ANDES note

Network-level CCT labs may use `envs/course_andes.yml` later. This lab’s minimum viable path is classical SMIB only.

## Status

Narrative and protocol ready; full surrogate CCT notebook follows Lab 2 implementation.
