# Lab 1 — Reference simulation and scientific dataset

```{note} Maturity: Draft
Readable teaching prose; examples, figures, and exercises are still growing. See [Status and versions](../../100_front/status_and_versions.md) and [Join and contribute](../../100_front/contribute.md).
```

## Goals

Deliver an SMIB simulator, event schedule, dataset manifest, and convergence check. Compare at least two numerical settings. Explain scenario-based splits. Retain numerical failures as flagged records.

## Materials

```{note} Under development
Online launch (Binder / Colab) is a public-preview convenience and may change.
Canonical path: local install. Help improve these paths: [Join and contribute](../../100_front/contribute.md). Full guide: [Running notebooks](../../100_front/running_notebooks.md).
```

- Notebook: [`lab01_reference_sim.ipynb`](lab01_reference_sim.ipynb) · [Running notebooks](../../100_front/running_notebooks.md)
- [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/albert8943/SciML_PS/master?filepath=book/900_labs/lab_01_reference_sim/lab01_reference_sim.ipynb) · [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/albert8943/SciML_PS/blob/master/book/900_labs/lab_01_reference_sim/lab01_reference_sim.ipynb)
- Teaching helper: `src/sciml_ps/smib.py` (`simulate_smib`, `SMIBParams`, `FaultEvent`)

## Setup (local — canonical)

```bash
conda activate sciml_ps
cd /path/to/SciML_PS   # repository root
pip install -e .
jupyter notebook book/900_labs/lab_01_reference_sim/lab01_reference_sim.ipynb
```

Binder and Colab need the **public** GitHub repo; until then use local install. No ANDES required.

## Deliverables

1. Plot comparing two solver settings on one fault scenario  
2. Manifest JSON with scenario IDs, solver metadata, and train/test **scenario** split  
3. Short note: whether stability labels flipped between solver settings  

## Linked chapters

- [Reference simulation](../../300_foundations/03_reference_simulation.md)  
- [SMIB dynamics](../../300_foundations/02_smib_dynamics.md)
