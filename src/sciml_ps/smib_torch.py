# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Albert Poulose
"""Differentiable classical SMIB rollout in PyTorch (fixed-step RK4).

Same model, parameters, and fault stages as :mod:`sciml_ps.smib`, written so that
gradients flow from a trajectory loss back to ``H`` and ``D`` through every solver
step. Used by the Identification page on differentiable simulation and the
optional Lab 3 extension.

Tensor layout is time-major ``(batch, time, dim)`` with ``dim = 2`` for
``(delta, omega)``.
"""

from __future__ import annotations

import numpy as np
import torch

from .smib import FaultEvent, SMIBParams, equilibrium_delta, simulate_smib


def _steps(t: float, dt: float) -> int:
    n = round(t / dt)
    if abs(n * dt - t) > 1e-9:
        raise ValueError(f"time {t} is not a multiple of dt={dt}; fault switches must fall on the grid")
    return n


def time_grid(event: FaultEvent, dt: float) -> np.ndarray:
    """Fixed grid ``0, dt, ..., t_end`` with fault and clearing times on grid points."""
    _steps(event.t_fault, dt)
    _steps(event.t_clear, dt)
    return np.arange(_steps(event.t_end, dt) + 1) * dt


def rollout_smib(
    H: torch.Tensor,
    D: torch.Tensor,
    params: SMIBParams | None = None,
    event: FaultEvent | None = None,
    *,
    dt: float = 2e-3,
) -> tuple[np.ndarray, torch.Tensor]:
    """Integrate the classical SMIB with RK4 for a batch of ``(H, D)`` values.

    ``H`` and ``D`` are 1-D tensors of shape ``(batch,)``; other parameters come
    from ``params``. The fault is a function of time only, so every RK4 step sits
    inside one stage and the rollout is differentiable in ``H`` and ``D``.

    Returns ``(t, x)`` with ``t`` of shape ``(time,)`` and ``x`` of shape
    ``(batch, time, 2)``.
    """
    params = params or SMIBParams()
    event = event or FaultEvent()
    H = torch.atleast_1d(H)
    D = torch.atleast_1d(D)
    t = time_grid(event, dt)
    k_fault = _steps(event.t_fault, dt)
    k_clear = _steps(event.t_clear, dt)

    w0 = params.omega0
    EV = params.E * params.V

    def rhs(x: torch.Tensor, X: float) -> torch.Tensor:
        delta, omega = x[:, 0], x[:, 1]
        Pe = (EV / X) * torch.sin(delta)
        ddelta = omega - w0
        domega = (w0 / (2.0 * H)) * (params.Pm - Pe - D * (omega - w0))
        return torch.stack([ddelta, domega], dim=-1)

    batch = H.shape[0]
    delta0 = equilibrium_delta(params, "pre")
    x = torch.tensor([delta0, w0], dtype=H.dtype).repeat(batch, 1)
    states = [x]
    for k in range(len(t) - 1):
        if k < k_fault:
            X = params.X_pre
        elif k < k_clear:
            X = params.X_fault
        else:
            X = params.X_post
        k1 = rhs(x, X)
        k2 = rhs(x + 0.5 * dt * k1, X)
        k3 = rhs(x + 0.5 * dt * k2, X)
        k4 = rhs(x + dt * k3, X)
        x = x + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
        states.append(x)
    return t, torch.stack(states, dim=1)


def parity_error(
    params: SMIBParams | None = None,
    event: FaultEvent | None = None,
    *,
    dt: float = 2e-3,
) -> dict[str, float]:
    """Max absolute gap between this RK4 rollout and the SciPy reference solver."""
    params = params or SMIBParams()
    event = event or FaultEvent()
    ref = simulate_smib(params, event, max_step=1e-3, rtol=1e-8, atol=1e-10)
    if ref["failed"]:
        raise RuntimeError(ref["message"])
    H = torch.tensor([params.H], dtype=torch.float64)
    D = torch.tensor([params.D], dtype=torch.float64)
    with torch.no_grad():
        t, x = rollout_smib(H, D, params, event, dt=dt)
    delta_ref = np.interp(t, ref["t"], ref["delta"])
    omega_ref = np.interp(t, ref["t"], ref["omega"])
    x = x[0].numpy()
    return {
        "delta_max_abs_rad": float(np.max(np.abs(x[:, 0] - delta_ref))),
        "omega_max_abs_rad_s": float(np.max(np.abs(x[:, 1] - omega_ref))),
    }


__all__ = ["parity_error", "rollout_smib", "time_grid"]

if __name__ == "__main__":
    print(parity_error())
