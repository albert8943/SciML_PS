#!/usr/bin/env python
"""Regenerate original teaching figures in media/figures/ from sciml_ps code.

Usage (repo root, sciml_ps env): python scripts/make_figures.py
"""

from __future__ import annotations

from dataclasses import replace
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from sciml_ps.smib import FaultEvent, SMIBParams, simulate_smib

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "media" / "figures"

T_END = 3.0
CASES = (
    # (label, clearing time [s], damping D, line style)
    ("Case 1: stable", 0.15, 0.10, "-"),
    ("Case 2: first-swing unstable", 0.40, 0.10, "-."),
    ("Case 3: oscillatory unstable", 0.15, -0.02, "--"),
)


def transient_stability_cases(path: Path) -> None:
    base = SMIBParams()
    fig, ax = plt.subplots(figsize=(6.0, 4.0), dpi=150)
    for label, t_clear, damping, style in CASES:
        out = simulate_smib(
            replace(base, D=damping),
            FaultEvent(t_fault=0.0, t_clear=t_clear, t_end=T_END),
        )
        delta_deg = np.degrees(out["delta"])
        keep = np.abs(delta_deg) < 200.0
        ax.plot(out["t"][keep], delta_deg[keep], style, color="black", lw=1.4, label=label)
    ax.axhline(0.0, color="0.7", lw=0.6)
    ax.set_xlim(0.0, T_END)
    ax.set_ylim(-75.0, 200.0)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel(r"Rotor angle $\delta$ (deg)")
    ax.legend(frameon=False, loc="upper right", fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)
    print("Wrote", path)


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    transient_stability_cases(FIGURES / "smib-transient-cases.png")


if __name__ == "__main__":
    main()
