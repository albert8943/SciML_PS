# Direct methods (equal-area and energy ideas)

## Learning goals

- Use a **classical** CCT check (equal-area / energy idea) when assumptions hold, before trusting only bisection or a surrogate
- State when those assumptions fail (damping, multi-swing, converters)
- Keep converter energy-function TSA as an **elective**, not Lab 5 default

## Reading

- B1 equal-area / energy chapters (edition-check before class)  
- [Stability labels and CCT](01_stability_and_cct.md)  
- Course report Lab 5 narrative  

## Why direct methods belong in a SciML course

SciML surrogates speed trajectories and CCT **search**. Direct methods give an independent **physics-based** estimate of clearing margin under simplified models. Comparing search-based CCT to a classical estimate (when valid) catches criterion bugs and overconfident surrogates.

## Equal-area idea (classical SMIB sketch)

For a highly idealized SMIB (constant mechanical power, no damping, classical “before / during / after” network strengths), the **equal-area criterion** balances accelerating and decelerating areas in the $P$–$\delta$ plane. The critical clearing angle (and thus CCT, given fault-on dynamics) is the clearing angle at which the decelerating area just matches the accelerating area.

Teaching use:

1. State the assumptions explicitly.  
2. Compute or look up the classical critical clearing angle / time for a chosen SMIB case.  
3. Run Lab 5-style bisection with the **same** stability rule as elsewhere.  
4. If assumptions hold and the rule is first-swing oriented, expect rough agreement; investigate large disagreements.

Do **not** treat equal-area as a general certificate for damped, multi-machine, or converter-rich cases.

## Energy-function / Lyapunov ideas (preview)

Lyapunov-style **transient energy functions** compare “energy” after clearing to a critical energy associated with a stability boundary. They motivate **direct** TSA and CCT without a long time-domain sweep — under a stated model and energy function.

For this course:

- Classical energy ideas deepen understanding of **why** clearing early helps.  
- **GFM/GFL converter energy-function CCT** is a research-strength topic and belongs as a later **Advanced / elective** case study, not as the assessed Lab 5 plant.

## Relation to Labs and surrogates

| Tool | Role |
|------|------|
| Reference TDS + bisection | Operational CCT under a stated rule (Lab 5 core) |
| Equal-area / classical energy | Independent check when assumptions allow |
| Trajectory surrogate + same rule | Fast repeat of the search (Lab 2 → Lab 5) |

Same rule across all three. Trajectory RMSE alone does not validate CCT.

```{exercise} When equal-area is a fair check
:class: dropdown
You have a classical SMIB Lab 5 bisection CCT under a first-swing $|\delta|$ rule. Name two modelling assumptions that must hold before you treat an equal-area CCT as a meaningful cross-check — and one situation where you should refuse the comparison.
```

```{solution} When equal-area is a fair check
:class: dropdown
Fair when (for example) mechanical power is treated as constant and damping is negligible, and the network is reduced to classical before/during/after strengths matching the equal-area sketch. Refuse the comparison for strongly damped swings, multi-swing criteria, or converter-rich plants where classical equal-area assumptions do not hold — then use energy ideas only as elective background, not as a Lab 5 certificate.
```

## Lab

- [Lab 5 — Stability and CCT](../900_labs/lab_05_stability_cct/index.md): after SMIB bisection works, optionally compare to equal-area under documented assumptions  
- Surrogates: [Surrogate models for stability tasks](02_surrogate_stability.md)

## Further reading

- B1; R-K04 / R-H21 for classification context  
- Converter energy-function TSA: defer to Advanced elective (maintainer note: website programme 01)

## Common misconceptions

- “Equal-area replaces the need to state a simulation criterion.”  
- “Energy methods always apply to GFM/GFL without new models.”  
- Using direct-method CCT from one model to certify a surrogate trained on another plant.  
