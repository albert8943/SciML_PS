"""One-shot helper to write Lab 1 notebook (run from repo root)."""
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
    """# Lab 1 — Reference simulation and scientific dataset

Compare two solver settings on the same classical SMIB fault scenario. Build a small scenario table and a manifest. Keep failed runs flagged.

**Env:** `sciml_ps` / `course_core` (no ANDES). From repo root: `pip install -e .` or add `src` to `PYTHONPATH`.
"""
)

code(
    """from pathlib import Path
import sys
import json
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path.cwd().resolve()
candidates = [ROOT / "src", ROOT.parents[2] / "src" if len(ROOT.parents) >= 3 else None]
for c in candidates:
    if c is not None and c.is_dir():
        sys.path.insert(0, str(c))
        break

from sciml_ps import FaultEvent, SMIBParams, angle_stable, simulate_smib
print("imports ok")
"""
)

code(
    """# Same physics, two numerical settings
params = SMIBParams()
event = FaultEvent(t_fault=0.1, t_clear=0.22, t_end=2.0)

fine = simulate_smib(params, event, max_step=1e-3, rtol=1e-6)
coarse = simulate_smib(params, event, max_step=5e-2, rtol=1e-3)

print("fine failed:", fine["failed"], fine["message"])
print("coarse failed:", coarse["failed"], coarse["message"])
print("fine stable:", angle_stable(fine["delta"]))
print("coarse stable:", angle_stable(coarse["delta"]))
"""
)

code(
    """fig, ax = plt.subplots(figsize=(7, 3.5))
if not fine["failed"]:
    ax.plot(fine["t"], fine["delta"], label="max_step=1e-3")
if not coarse["failed"]:
    ax.plot(coarse["t"], coarse["delta"], "--", label="max_step=5e-2")
ax.axvline(event.t_fault, color="k", lw=0.8, alpha=0.5)
ax.axvline(event.t_clear, color="r", lw=0.8, alpha=0.5)
ax.set_xlabel("t [s]")
ax.set_ylabel(r"$\\delta$ [rad]")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
"""
)

code(
    """# Scenario table: vary clearing time (split by scenario, not by time index)
clearing_times = [0.15, 0.20, 0.25, 0.30]
rows = []
for tc in clearing_times:
    ev = FaultEvent(t_fault=0.1, t_clear=tc, t_end=2.0)
    out = simulate_smib(params, ev, max_step=1e-3)
    rows.append({
        "scenario_id": f"fault_clear_{tc:.2f}",
        "t_clear": tc,
        "failed": out["failed"],
        "stable": None if out["failed"] else angle_stable(out["delta"]),
        "max_abs_delta": None if out["failed"] else float(np.max(np.abs(out["delta"]))),
        "n_steps": int(out["t"].size),
    })

for r in rows:
    print(r)

train_ids = {rows[0]["scenario_id"], rows[1]["scenario_id"]}
test_ids = {r["scenario_id"] for r in rows} - train_ids
print("train", train_ids)
print("test", test_ids)
"""
)

code(
    """manifest = {
    "lab": "lab_01_reference_sim",
    "model": "classical_SMIB",
    "params": fine["params"],
    "event_template": {"t_fault": 0.1, "t_end": 2.0},
    "solver_settings_compared": [
        {"name": "fine", "max_step": 1e-3, "rtol": 1e-6},
        {"name": "coarse", "max_step": 5e-2, "rtol": 1e-3},
    ],
    "stability_rule": "max|delta| < pi",
    "scenarios": rows,
    "split": {
        "train_scenario_ids": sorted(train_ids),
        "test_scenario_ids": sorted(test_ids),
    },
    "policy": "Retain numerical failures as flagged records; do not silently delete them.",
}
out_path = Path("lab01_manifest.json")
out_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
print("wrote", out_path.resolve())
"""
)

md(
    """## Deliverables checklist

1. Plots comparing two solver settings on one scenario
2. `lab01_manifest.json` (or equivalent) with scenario IDs and split
3. Short note: did the stability label flip between solver settings for any clearing time?
"""
)

path = Path(__file__).resolve().parents[1] / "book/900_labs/lab_01_reference_sim/lab01_reference_sim.ipynb"
path.write_text(json.dumps(nb, indent=1), encoding="utf-8")
print("wrote", path)
