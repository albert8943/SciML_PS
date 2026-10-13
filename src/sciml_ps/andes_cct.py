"""Thin ANDES helpers for Lab 5 network CCT extension (optional dependency).

Preferred case: ``andes.get_case("kundur/kundur_full.xlsx")``.
Full gallery walkthrough (do not paste into the book):
https://docs.andes.app/en/stable/gallery/critical-clearing-time.html

Requires ``andes==2.0.0`` (see ``envs/course_andes.yml``). Run ``andes prep`` once
after install if generated pycode is missing.
"""

from __future__ import annotations

from typing import Any, Literal

import numpy as np

Outcome = Literal["stable", "unstable", "non_convergent"]

KUNDUR_CASE = "kundur/kundur_full.xlsx"
GALLERY_CCT_URL = (
    "https://docs.andes.app/en/stable/gallery/critical-clearing-time.html"
)


def require_andes():
    try:
        import andes
    except ImportError as exc:  # pragma: no cover - env-dependent
        raise ImportError(
            "ANDES is required for network CCT helpers. "
            "Use envs/course_andes.yml (andes==2.0.0) and: conda activate sciml_ps_andes"
        ) from exc
    return andes


def signed_cct_error(t_hat: float, t_ref: float) -> float:
    """Signed CCT error: positive means the estimate is optimistic (false-safe risk)."""
    return float(t_hat - t_ref)


def false_safe_count(
    t_hat: np.ndarray | list[float],
    t_ref: np.ndarray | list[float],
    *,
    margin: float = 0.0,
) -> int:
    """Count cases where predicted CCT exceeds reference by more than ``margin``."""
    th = np.asarray(t_hat, dtype=float)
    tr = np.asarray(t_ref, dtype=float)
    return int(np.sum(th > tr + margin))


def load_kundur(*, disable_toggle: bool = True):
    """Load the preferred class Kundur case (Toggle line-trip disabled by default)."""
    andes = require_andes()
    case_path = andes.get_case(KUNDUR_CASE)
    ss = andes.load(case_path, no_output=True)
    if disable_toggle and hasattr(ss, "Toggle") and len(ss.Toggle.u.v):
        ss.Toggle.u.v[0] = 0
    return ss, case_path


def _max_angle_sep_deg(ss) -> float:
    delta = ss.dae.ts.x[:, ss.GENROU.delta.a]
    sep = np.rad2deg(np.max(delta, axis=1) - np.min(delta, axis=1))
    return float(np.nanmax(sep))


def classify_tds(ss) -> Outcome:
    """Map ANDES TDS termination to a coarse operational outcome (gallery-aligned)."""
    if not ss.TDS.busted:
        return "stable"
    msg = (ss.TDS.err_msg or "").lower()
    if "criteria" in msg:
        return "unstable"
    return "non_convergent"


def simulate_fault_clearing(
    case_path: str,
    *,
    bus: Any,
    t_fault: float,
    t_clear: float,
    xf: float = 1e-4,
    t_end: float = 8.0,
    disable_criteria: bool = False,
) -> dict:
    """One fault-on / clear scenario on Kundur (or any compatible case path)."""
    andes = require_andes()
    ss = andes.load(case_path, setup=False, no_output=True)
    if hasattr(ss, "Toggle") and len(ss.Toggle.u.v):
        ss.Toggle.u.v[0] = 0
    ss.add("Fault", bus=bus, tf=t_fault, tc=t_clear, xf=xf)
    ss.setup()
    ss.config.warn_abnormal = 0
    ss.PFlow.run()
    ss.TDS.config.tf = t_end
    ss.TDS.config.no_tqdm = 1
    if disable_criteria:
        ss.TDS.config.criteria = 0
    ss.TDS.run(no_summary=True)
    outcome = classify_tds(ss)
    return {
        "bus": bus,
        "t_fault": float(t_fault),
        "t_clear": float(t_clear),
        "clearing_duration": float(t_clear - t_fault),
        "outcome": outcome,
        "max_sep_deg": _max_angle_sep_deg(ss) if ss.dae.ts.x is not None else float("nan"),
        "busted": bool(ss.TDS.busted),
        "err_msg": ss.TDS.err_msg or "",
        "andes_version": andes.__version__,
        "case": KUNDUR_CASE,
    }


def cct_sweep_one_bus(
    *,
    bus: Any = 8,
    t_fault: float = 1.0,
    tc_values: np.ndarray | None = None,
    xf: float = 1e-4,
    t_end: float = 8.0,
) -> dict:
    """Sweep clearing durations for one bus; report first failing duration as CCT.

    ``tc_values`` are clearing *durations* in seconds (same convention as the gallery).
    """
    andes = require_andes()
    case_path = andes.get_case(KUNDUR_CASE)
    if tc_values is None:
        tc_values = np.arange(0.025, 0.40, 0.025)
    tc_values = np.asarray(tc_values, dtype=float)

    rows: list[dict] = []
    cct = float("nan")
    for tc in tc_values:
        row = simulate_fault_clearing(
            case_path,
            bus=bus,
            t_fault=t_fault,
            t_clear=t_fault + float(tc),
            xf=xf,
            t_end=t_end,
        )
        rows.append(row)
        if row["outcome"] != "stable" and not np.isfinite(cct):
            cct = float(tc)

    if not np.isfinite(cct) and rows:
        cct = float(tc_values[-1])

    return {
        "bus": bus,
        "t_fault": t_fault,
        "tc_values": tc_values.tolist(),
        "cct_duration_s": cct,
        "rows": rows,
        "case": KUNDUR_CASE,
        "gallery": GALLERY_CCT_URL,
        "andes_version": andes.__version__,
    }
