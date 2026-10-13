"""Teaching utilities for Scientific Machine Learning for Power Systems."""

from .smib import FaultEvent, SMIBParams, angle_stable, simulate_smib

__version__ = "0.0.1"
__all__ = [
    "FaultEvent",
    "SMIBParams",
    "angle_stable",
    "simulate_smib",
    "__version__",
]
