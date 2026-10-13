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
