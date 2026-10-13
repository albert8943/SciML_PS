# SciML method families (landscape)

## Learning goals

- Name major SciML families used for power-system dynamics and TSA
- Say what each family **learns** (trajectory, vector field, operator, …)
- Avoid treating every neural method as “a PINN”

## Reading

- Course report §4.3 method table  
- Teaching adapt of vault “SciML Families for Power System TSA” (career links removed)

## Plain-words map

SciML here means: neural models with **physics structure** for dynamics or margins — not only black-box stable/unstable classifiers.

| Family | Learns (roughly) | Teaching role in this book |
|--------|------------------|----------------------------|
| Supervised surrogate | Map features → trajectories / labels | Mandatory baseline (Lab 2) |
| PINN (collocation) | $\hat{x}(t)$ with residual loss | Core forward / inverse path |
| Neural ODE / hybrid | Vector field (+ optional known physics) | Lab 4 option |
| Operator learning (DeepONet / FNO) | Function → function | Advanced / Lab 4 option; not inverse named-$\theta$ default |
| Differentiable simulator | Sensitivities through a solver | Awareness; advanced |
| Classical simulation | Reference trajectories | Lab 1 and all baselines |

For **transient stability**, families differ mainly by whether they output trajectories, decisions, or operators — and how CCT search sits on top. Details: [Stability pillar](../500_stability/overview.md).

## Further reading

- B5 PBDL overview; report R6 (Neural ODE); operator-learning papers as assigned

## Common misconceptions

- “DeepONet is a PINN variant”  
- Ranking methods by hype instead of task fit  
- Skipping classical simulation because a neural method exists
