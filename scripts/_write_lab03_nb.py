"""Write Lab 3 starter notebook."""
import json
from pathlib import Path

nb = {
    "nbformat": 4,
    "nbformat_minor": 5,
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3",
        }
    },
    "cells": [],
}


def md(s: str) -> None:
    nb["cells"].append(
        {"cell_type": "markdown", "metadata": {}, "source": s.splitlines(keepends=True)}
    )


def code(s: str) -> None:
    nb["cells"].append(
        {
            "cell_type": "code",
            "metadata": {},
            "outputs": [],
            "execution_count": None,
            "source": s.splitlines(keepends=True),
        }
    )


md(
    """# Lab 3 — Inertia and damping identification (starter)

Estimands: classical $(H, D)$. Build noisy measurements from Lab 1 SMIB, plot a 2-D LS loss surface, and outline an inverse PINN comparison.
"""
)

code(
    """from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path.cwd().resolve()
for c in [ROOT / "src", ROOT.parents[2] / "src" if len(ROOT.parents) >= 3 else None]:
    if c is not None and c.is_dir():
        sys.path.insert(0, str(c))
        break

from sciml_ps import FaultEvent, SMIBParams, simulate_smib
from dataclasses import replace
"""
)

code(
    """# Truth trajectory
H_true, D_true = 5.0, 0.15
params_true = SMIBParams(H=H_true, D=D_true)
event_train = FaultEvent(t_fault=0.1, t_clear=0.22, t_end=2.0)
truth = simulate_smib(params_true, event_train, max_step=1e-3)
assert not truth["failed"]

rng = np.random.default_rng(0)
sigma = 0.05
omega_meas = truth["omega"] + sigma * rng.normal(size=truth["omega"].shape)
t = truth["t"]
print("samples", t.size)
"""
)

code(
    """# Least-squares loss on omega vs (H, D) grid (simulator in the loop)

def ls_loss(H, D, t_ref, omega_ref, event):
    out = simulate_smib(SMIBParams(H=H, D=D), event, max_step=2e-3, rtol=1e-5)
    if out["failed"] or out["t"].size < 2:
        return np.nan
    omega_hat = np.interp(t_ref, out["t"], out["omega"])
    return float(np.mean((omega_hat - omega_ref) ** 2))

H_grid = np.linspace(3.0, 7.0, 9)
D_grid = np.linspace(0.02, 0.35, 9)
Z = np.zeros((len(D_grid), len(H_grid)))
for i, D in enumerate(D_grid):
    for j, H in enumerate(H_grid):
        Z[i, j] = ls_loss(H, D, t, omega_meas, event_train)

# Best grid point
idx = np.nanargmin(Z)
i_best, j_best = np.unravel_index(idx, Z.shape)
print("grid best H,D", H_grid[j_best], D_grid[i_best], "loss", Z[i_best, j_best])
print("true H,D", H_true, D_true)
"""
)

code(
    """fig, ax = plt.subplots(figsize=(5.5, 4))
pcm = ax.pcolormesh(H_grid, D_grid, np.log10(Z + 1e-16), shading="auto")
ax.plot(H_true, D_true, "w*", ms=14, label="true")
ax.plot(H_grid[j_best], D_grid[i_best], "ro", label="grid LS")
ax.set_xlabel("H")
ax.set_ylabel("D")
fig.colorbar(pcm, ax=ax, label="log10 LS loss")
ax.legend()
plt.tight_layout()
plt.show()
"""
)

code(
    """# Held-out disturbance check with grid-LS estimate
event_test = FaultEvent(t_fault=0.1, t_clear=0.18, t_end=2.0)
truth_test = simulate_smib(params_true, event_test, max_step=1e-3)
pred_test = simulate_smib(SMIBParams(H=H_grid[j_best], D=D_grid[i_best]), event_test, max_step=1e-3)
omega_hat = np.interp(truth_test["t"], pred_test["t"], pred_test["omega"])
rmse = float(np.sqrt(np.mean((omega_hat - truth_test["omega"]) ** 2)))
print("held-out omega RMSE", rmse)
"""
)

md(
    """## Optional: differentiable simulation (gradient through the solver)

The grid search above calls the simulator 81 times and only sees grid points. Here the same SMIB is rolled out with fixed-step RK4 in PyTorch (`sciml_ps.smib_torch`), so the loss gradient with respect to $(H, D)$ comes from automatic differentiation through every solver step. Background: [Differentiable simulation](../../600_identification/03_differentiable_simulation.md).

Choices to notice:

- Fit $\\log H$ and $\\log D$ so both stay positive and have comparable step sizes
- Compare speed **deviation** $\\omega - \\omega_0$, not raw $\\omega \\approx 377$ rad/s
- Clamp to stated bounds after each step
- Needs `torch` (course core environment)
"""
)

code(
    """import torch
from sciml_ps.smib_torch import rollout_smib, time_grid

dt = 2e-3  # fault and clearing times must be multiples of dt
t_grid = time_grid(event_train, dt)
w0 = params_true.omega0
y = torch.tensor(np.interp(t_grid, t, omega_meas) - w0)

lower = torch.log(torch.tensor([1.0, 0.01], dtype=torch.float64))
upper = torch.log(torch.tensor([15.0, 1.0], dtype=torch.float64))
theta = torch.log(torch.tensor([4.0, 0.05], dtype=torch.float64)).requires_grad_(True)
opt = torch.optim.LBFGS([theta], lr=1.0, max_iter=20, line_search_fn="strong_wolfe")

def closure():
    opt.zero_grad()
    H, D = torch.exp(theta)
    _, x = rollout_smib(H[None], D[None], event=event_train, dt=dt)
    loss = torch.mean((x[0, :, 1] - w0 - y) ** 2)
    loss.backward()
    return loss

for it in range(3):
    loss = opt.step(closure)
    with torch.no_grad():
        theta.clamp_(lower, upper)
    H_dp, D_dp = torch.exp(theta).tolist()
    print(f"outer step {it}: loss before step {loss.item():.3e}  ->  H {H_dp:.3f}  D {D_dp:.3f}")

print("grid LS H,D", H_grid[j_best], D_grid[i_best])
print("true H,D   ", H_true, D_true)
"""
)

code(
    """# Same held-out disturbance, re-simulated with the reference solver
pred_dp = simulate_smib(SMIBParams(H=H_dp, D=D_dp), event_test, max_step=1e-3)
omega_dp = np.interp(truth_test["t"], pred_dp["t"], pred_dp["omega"])
rmse_dp = float(np.sqrt(np.mean((omega_dp - truth_test["omega"]) ** 2)))
print("held-out omega RMSE: grid LS", rmse, " differentiable simulation", rmse_dp)
"""
)

md(
    """**Discuss:** both estimators use the same model, so they share its blind spots. Re-run with a model mismatch (e.g. true $X_{post}$ = 0.75 in the data, 0.7 in the fit) and check whether $(\\hat H, \\hat D)$ become *equivalent* rather than physical values.
"""
)

md(
    """## Inverse PINN template (complete in class)

1. Network: $t \\mapsto (\\hat{\\delta}, \\hat{\\omega})$  
2. Trainable parameters: $H, D$ with positive bounds  
3. Losses: data on noisy $\\omega$ + swing residuals via AD  
4. Same train event / held-out event as above  

Compare final $(\\hat H, \\hat D)$ to the grid LS result and discuss physical vs equivalent fits.
"""
)

path = (
    Path(__file__).resolve().parents[1]
    / "book/900_labs/lab_03_inertia_damping_id/lab03_inertia_damping_id.ipynb"
)
path.write_text(json.dumps(nb, indent=1), encoding="utf-8")
print("wrote", path)
