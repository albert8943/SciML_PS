# Differentiable simulation

## Learning goals

- Explain how a gradient with respect to $(H, D)$ can flow through a numerical solver
- Compare differentiable simulation with simulation-based least squares and inverse PINNs on the same data contract
- State what the method does **not** fix: identifiability, model mismatch, and bound activity

## Reading

- [Classical estimation](../300_foundations/07_classical_estimation.md), [automatic differentiation](../300_foundations/05_differentiation.md), [inverse PINN](../300_foundations/09_inverse_pinn.md)
- B5 Thuerey et al., [differentiable physics](https://physicsbaseddeeplearning.org/diffphys.html) and [differentiable physics versus physics-informed training](https://physicsbaseddeeplearning.org/diffphys-dpvspinn.html) (method background with fluid examples)

## The idea

Simulation-based least squares already puts the simulator in the loop: pick $(H, D)$, simulate, compare with measurements. What it lacks is a cheap **direction** to move $(H, D)$. A grid search simulates many candidates, and finite differences need extra simulations per parameter.

**Differentiable simulation** writes the integrator itself in an automatic-differentiation framework. Each solver step is an ordinary differentiable operation, so reverse-mode AD returns

$$
\frac{\partial \mathcal{L}}{\partial \theta}, \qquad \mathcal{L}(\theta) = \frac{1}{N}\sum_{k} \big(\hat{\omega}_k(\theta) - \omega^{\mathrm{meas}}_k\big)^2, \qquad \theta = (H, D),
$$

from a single forward rollout and one backward pass, where $\hat{\omega}_k(\theta)$ is the **simulated** speed at sample $k$.

## How the gradient flows

For the classical SMIB of [SMIB dynamics](../300_foundations/02_smib_dynamics.md), one RK4 step maps the state $x_k = (\delta_k, \omega_k)$ to

$$
x_{k+1} = \Phi_{\Delta t}(x_k;\, \theta, X_k),
$$

where $X_k$ is the network reactance for the current stage (prefault, fault-on, postfault). The trajectory is a chain $x_0 \to x_1 \to \cdots \to x_N$, and the loss gradient is the chain rule along that chain. Backpropagation computes it automatically, carrying the sensitivity of each state to $H$ and $D$ backward through every step.

Two practical conditions make this work in the teaching model:

1. **Fault switching depends on time only.** The reactance changes at fixed $t_f$ and $t_c$, so put both on the step grid. Each step then sits inside one stage, and nothing non-differentiable happens inside a step. State-triggered events (protection acting on $\delta$) need event-aware solvers and are beyond this course.
2. **Scales are comparable.** Fit $\log H$ and $\log D$, and compare speed deviation $\omega - \omega_0$, as in [gradient scaling](../300_foundations/05_differentiation.md#gradient-scaling).

Course helper: `sciml_ps.smib_torch.rollout_smib` (fixed-step RK4 in PyTorch, tensors `(batch, time, 2)`). `parity_error` checks it against the SciPy reference solver used in Lab 1.

## Three estimators, one data contract

| | Simulation LS (grid or derivative-free) | Differentiable simulation | Inverse PINN |
|---|---|---|---|
| Unknowns | $\theta$ | $\theta$ | NN weights **and** $\theta$ |
| Trajectory obeys the model? | Exactly (solver) | Exactly (solver) | Approximately (residual penalty) |
| Gradient source | None or finite differences | AD through solver steps | AD through network and residual |
| Cost per iteration | One simulation per candidate | One rollout + backward pass | One network pass over collocation points |
| Needs | Any simulator | Differentiable solver | Network, collocation design, loss weights |
| Main failure mode | Coarse grid; many simulations | Long or stiff rollouts give poor gradients; solver must be rewritten in AD | Network absorbs model error; weighting shifts $\theta$ |

The comparison rule from Lab 3 still holds: **same measurements, noise, window, and bounds** for every estimator, and a held-out disturbance for every estimate.

## What it does not fix

- **Identifiability.** Exact gradients of a flat loss surface are still flat. Weak excitation leaves $D$ poorly informed whichever estimator you use ([identifiability](../300_foundations/08_identifiability.md)).
- **Model mismatch.** The fitted $\theta$ is the best value *for the model you differentiated*. If the data come from a different model, $(\hat H, \hat D)$ become **equivalent** parameters ([physical vs equivalent](02_physical_vs_equivalent.md)).
- **Bounds.** Report the bounds and whether an estimate ended on one.

## Where it leads

Differentiable simulators are also the basis of **hybrid models**: a neural term trained *inside* the solver, next to the known swing equation. See [Neural ODE / hybrid](../300_foundations/10_neural_ode_hybrid.md). That is how SciML models can later plug into established simulation workflows instead of replacing them.

## Lab

- [Lab 3 — Inertia and damping estimation](../900_labs/lab_03_inertia_damping_id/index.md), optional section "Differentiable simulation"

## Honesty rule

Fast convergence is not recovery. Report the true or reference $\theta$ when known, the estimate, the bounds, and the held-out disturbance error, as for every other estimator.

## Common misconceptions

- “Exact gradients mean the estimate is exact.”
- “Differentiable simulation is a kind of PINN.” It has no network and no residual penalty; the solver enforces the model.
- Differentiating through a state-triggered switch as if it were smooth
