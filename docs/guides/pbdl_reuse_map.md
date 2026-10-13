# PBDL reuse map (maintainers)

How SciML_PS uses the *Physics-based Deep Learning* book (Thuerey et al., v0.3; reading list **B5**). PBDL is a method-led textbook built on fluid examples. SciML_PS is application-led (Dynamics, Stability, Identification on one SMIB plant). We take PBDL's methods and teaching patterns and keep our own spine ([scope lock](scope_lock_three_pillars.md)).

## License facts

- Repository: <https://github.com/tum-pbs/pbdl-book>. Its `LICENSE` is **Apache-2.0** (checked 2026-10-13 at commit `45d2b65`). Local copy: [`LICENSES/PBDL-Apache-2.0.txt`](../../LICENSES/PBDL-Apache-2.0.txt).
- There was no `NOTICE` file upstream at that commit.
- The authors ask readers to cite the book (`thuerey2021pbdl`).

## Default: cite, don't copy

Explain ideas in our own words, use SMIB examples, reimplement from equations, and cite B5 (report §13.2). Copy PBDL text or code only when it is clearly better than rewriting.

## Apache-2.0 checklist (only for `adapted-text` / `adapted-code`)

- [ ] License copy present in `LICENSES/`
- [ ] Modified file has a prominent header: source file, commit, "Apache-2.0", "modified by … for SciML_PS"
- [ ] Upstream copyright and attribution notices kept
- [ ] Re-check for an upstream `NOTICE` file at the commit you copy from
- [ ] No use of the "PBDL" name as our brand or chapter title (Apache §6)
- [ ] Figures redrawn, never copied
- [ ] Row added to the [attribution register](../references/attribution_register.md)

## Section map

Tiers: **Adapt** = ideas used now in a book page; **Later** = Advanced pointer when the pillar is ready; **Link** = further reading only; **Skip** = out of scope.

| PBDL part (source files) | Tier | SciML_PS target | Register |
|--------------------------|------|-----------------|----------|
| Introduction: overview, models and equations (`overview.md`, `overview-equations.md`) | Adapt | `300_foundations/00_sciml_landscape.md` § How tightly is physics coupled? | PBDL-01 |
| Introduction: Burgers / Navier-Stokes forward notebooks | Skip | (fluid examples) | n/a |
| Neural surrogates (`supervised.md`, `supervised-discuss.md`) | Adapt | `300_foundations/04_data_and_surrogates.md`; Lab 2; pillar Discussion sections | PBDL-05 |
| Neural surrogates: architectures (`supervised-arch.md`) | Later | `700_advanced` graph models for multimachine | PBDL-07 |
| Neural surrogates: airfoils (`supervised-airfoils.ipynb`) | Skip | (fluid example) | n/a |
| Physical losses (`physicalloss.md`, `physicalloss-discuss.md`) | Adapt | `06_forward_pinn.md`, `09_inverse_pinn.md` § Strengths and limits | PBDL-02 |
| Physical losses code (`physicalloss-code.ipynb`, Burgers PINN) | Link | Pattern only; our PINN is written for the swing equation | n/a |
| Differentiable physics (`diffphys.md`, `diffphys-dpvspinn.md`, `diffphys-discuss.md`) | Adapt | `600_identification/03_differentiable_simulation.md`; `src/sciml_ps/smib_torch.py`; Lab 3 extension | PBDL-04 |
| Differentiable physics code (Burgers, Navier-Stokes, solver-in-the-loop, control) | Link | Further reading for hybrid models (`10_neural_ode_hybrid.md`) | n/a |
| Improved gradients (`physgrad.md`, `physgrad-hig.md`, coupled-oscillator HIG notebook) | Adapt (idea) / Link (algorithms) | `05_differentiation.md` § Gradient scaling | PBDL-03 |
| Probabilistic learning (diffusion, flow matching, `probmodels-phys.md`, `probmodels-time.ipynb`) | Later | `700_advanced` uncertainty pointer | PBDL-07 |
| Probabilistic learning: graph diffusion (`probmodels-graph.md`) | Later | `700_advanced` graph pointer | PBDL-07 |
| Reinforcement learning (`reinflearn-*`) | Link | `700_advanced` out-of-scope curiosity | n/a |
| Fast forward: model reduction and time series (`others-timeseries.md`) | Adapt (pointer) | `400_dynamics/overview.md`; Lab 4 | PBDL-06 |
| Fast forward: Lagrangian / meshless (`others-lagrangian.md`) | Skip | (not our domain) | n/a |
| Fast forward: GANs (`others-GANs.md`) | Skip | (weak fit to the three pillars) | n/a |

## Teaching patterns reused (no license step)

1. A closing **Discussion** at the end of each part. Ours is a section in each pillar `overview.md`, so the TOC does not change.
2. **Fast-forward topics**: short introductions without notebooks, pointing to external code. Ours live in `700_advanced/overview.md`.
3. Every concept paired with a runnable notebook (already our lab pattern).

## When PBDL releases a new version

Re-check the license and commit, update `LICENSES/PBDL-Apache-2.0.txt` if the text changed, and update the version column in the register. Do not change book pages unless a cited idea changed.
