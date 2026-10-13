# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Albert Poulose
"""Classical SMIB swing-equation helper for teaching labs (no ANDES)."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Literal

import numpy as np
from scipy.integrate import solve_ivp


@dataclass(frozen=True)
class SMIBParams:
    """Per-unit classical SMIB parameters (teaching defaults)."""

    H: float = 5.0
    D: float = 0.1
    omega0: float = 2 * np.pi * 60.0
    E: float = 1.05
    V: float = 1.0
    X_pre: float = 0.5
    X_fault: float = 1.0e6  # effectively open: tiny Pe during fault
    X_post: float = 0.7
    Pm: float = 0.8


@dataclass(frozen=True)
class FaultEvent:
    t_fault: float = 0.1
    t_clear: float = 0.25
    t_end: float = 2.0


def electrical_power(delta: float, E: float, V: float, X: float) -> float:
    if not np.isfinite(X) or X <= 0:
        return 0.0
    return (E * V / X) * np.sin(delta)


def _reactance(t: float, params: SMIBParams, event: FaultEvent) -> float:
    if t < event.t_fault:
        return params.X_pre
    if t < event.t_clear:
        return params.X_fault
    return params.X_post


def smib_rhs(t: float, y: np.ndarray, params: SMIBParams, event: FaultEvent) -> list[float]:
    delta, omega = y
    X = _reactance(t, params, event)
    Pe = electrical_power(delta, params.E, params.V, X)
    ddelta = omega - params.omega0
    domega = (params.omega0 / (2.0 * params.H)) * (
        params.Pm - Pe - params.D * (omega - params.omega0)
    )
    return [ddelta, domega]


def equilibrium_delta(params: SMIBParams, stage: Literal["pre", "post"] = "pre") -> float:
    X = params.X_pre if stage == "pre" else params.X_post
    arg = params.Pm * X / (params.E * params.V)
    arg = float(np.clip(arg, -1.0, 1.0))
    return float(np.arcsin(arg))


def simulate_smib(
    params: SMIBParams | None = None,
    event: FaultEvent | None = None,
    *,
    rtol: float = 1e-6,
    atol: float = 1e-8,
    max_step: float | None = 1e-3,
    method: str = "RK45",
) -> dict:
    """Integrate classical SMIB through prefault / fault-on / postfault.

    Returns a dict suitable for a Lab 1 dataset manifest entry.
    """
    params = params or SMIBParams()
    event = event or FaultEvent()
    delta0 = equilibrium_delta(params, "pre")
    y0 = np.array([delta0, params.omega0], dtype=float)

    kwargs = {"rtol": rtol, "atol": atol, "method": method, "dense_output": False}
    if max_step is not None:
        kwargs["max_step"] = max_step

    failed = False
    message = "ok"
    try:
        sol = solve_ivp(
            smib_rhs,
            (0.0, event.t_end),
            y0,
            args=(params, event),
            **kwargs,
        )
        if not sol.success:
            failed = True
            message = sol.message
    except Exception as exc:  # noqa: BLE001 - teaching helper surfaces failures
        failed = True
        message = str(exc)
        return {
            "t": np.asarray([], dtype=float),
            "delta": np.asarray([], dtype=float),
            "omega": np.asarray([], dtype=float),
            "params": asdict(params),
            "event": asdict(event),
            "solver": {"rtol": rtol, "atol": atol, "max_step": max_step, "method": method},
            "failed": True,
            "message": message,
        }

    return {
        "t": sol.t,
        "delta": sol.y[0],
        "omega": sol.y[1],
        "params": asdict(params),
        "event": asdict(event),
        "solver": {"rtol": rtol, "atol": atol, "max_step": max_step, "method": method},
        "failed": failed,
        "message": message,
    }


def angle_stable(
    delta: np.ndarray,
    *,
    threshold_rad: float = np.pi,
) -> bool:
    """Operational label: unstable if |delta| exceeds threshold (teaching default)."""
    if delta.size == 0:
        return False
    return bool(np.max(np.abs(delta)) < threshold_rad)
