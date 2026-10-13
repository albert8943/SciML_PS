# Lab 1 — Reference simulation and scientific dataset

## Goals

Deliver an SMIB simulator, event schedule, dataset manifest, and convergence check. Compare at least two numerical settings. Explain scenario-based splits. Retain numerical failures as flagged records.

## Materials

- Notebook: [`lab01_reference_sim.ipynb`](lab01_reference_sim.ipynb)
- Teaching helper: `src/sciml_ps/smib.py` (`simulate_smib`, `SMIBParams`, `FaultEvent`)

## Setup

```bash
conda activate sciml_ps
cd /path/to/SciML_PS
pip install -e .
jupyter notebook book/900_labs/lab_01_reference_sim/lab01_reference_sim.ipynb
```

No ANDES required.

## Deliverables

1. Plot comparing two solver settings on one fault scenario  
2. Manifest JSON with scenario IDs, solver metadata, and train/test **scenario** split  
3. Short note: whether stability labels flipped between solver settings  

## Linked chapters

- [Reference simulation](../../300_foundations/03_reference_simulation.md)  
- [SMIB dynamics](../../300_foundations/02_smib_dynamics.md)
