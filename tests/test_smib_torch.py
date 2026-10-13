"""Parity and gradient checks for the differentiable SMIB rollout."""

import pytest

torch = pytest.importorskip("torch")

from sciml_ps import FaultEvent, SMIBParams
from sciml_ps.smib_torch import parity_error, rollout_smib


def test_rk4_matches_scipy_reference():
    event = FaultEvent(t_fault=0.1, t_clear=0.22, t_end=2.0)
    err = parity_error(SMIBParams(H=5.0, D=0.15), event, dt=2e-3)
    assert err["delta_max_abs_rad"] < 1e-3
    assert err["omega_max_abs_rad_s"] < 1e-2


def test_gradients_reach_H_and_D():
    H = torch.tensor([5.0], dtype=torch.float64, requires_grad=True)
    D = torch.tensor([0.15], dtype=torch.float64, requires_grad=True)
    _, x = rollout_smib(H, D, event=FaultEvent(t_end=0.5), dt=2e-3)
    x[..., 1].sum().backward()
    assert torch.isfinite(H.grad).all() and H.grad.abs().item() > 0
    assert torch.isfinite(D.grad).all() and D.grad.abs().item() > 0


def test_batch_layout():
    H = torch.tensor([4.0, 5.0, 6.0], dtype=torch.float64)
    D = torch.full((3,), 0.1, dtype=torch.float64)
    t, x = rollout_smib(H, D, event=FaultEvent(t_end=0.2), dt=2e-3)
    assert x.shape == (3, len(t), 2)


def test_off_grid_event_rejected():
    with pytest.raises(ValueError):
        rollout_smib(torch.tensor([5.0]), torch.tensor([0.1]), event=FaultEvent(t_clear=0.2501), dt=2e-3)
