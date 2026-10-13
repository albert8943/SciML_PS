# SMIB dynamics

## Learning goals

- Write classical SMIB swing equations in consistent units
- Relate inertia and damping to post-disturbance trajectories
- Name prefault, fault-on, and postfault stages for teaching experiments

## Reading

- Kundur / Malik (B1): swing equations and transient stability framing  
- Course report Weeks 2–3

## Classical swing model (teaching form)

A common classical-machine SMIB model (per-unit power, radian angles) is:

$$
\begin{aligned}
\dot{\delta} &= \omega - \omega_0, \\
\frac{2H}{\omega_0}\dot{\omega} &= P_m - P_e(\delta) - D\,(\omega - \omega_0),
\end{aligned}
$$

with electrical power of the form $P_e = \frac{E V}{X}\sin\delta$ (details and bases documented in the lab notebook).

**Teaching estimands** in Lab 3: inertia $H$ and damping $D$. Keep units and the per-unit base in the dataset manifest.

## Event stages

| Stage | Network / driving | Typical use |
|-------|-------------------|-------------|
| Prefault | Intact network, equilibrium | Initial condition |
| Fault-on | Reduced $P_e$ capability (e.g. bolted fault) | Energy input / acceleration |
| Postfault | Cleared topology | Stability vs loss of synchronism |

Critical clearing time (CCT) later asks: *how long can fault-on last before postfault trajectories are unstable under a stated rule?* See [Stability and CCT](../500_stability/01_stability_and_cct.md).

## Worked example

For fixed $H$, plot qualitative $\delta(t)$ after a short fault vs a long fault. Which parameter mainly scales the “inertia” of the swing?

## Lab

- [Lab 1 — Reference simulation](../900_labs/lab_01_reference_sim/index.md)

## Further reading

- B1 swing chapter; course report Stage A (SMIB classical machine)

## Common misconceptions

- Calling every fitted coefficient “physical inertia” without a model map  
- Mixing SI and per-unit in the same residual without conversion  
- Using converter $(M_v, D_v, m_p)$ language in classical SMIB labs without an explicit elective flag
