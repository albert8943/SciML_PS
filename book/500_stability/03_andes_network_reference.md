# ANDES as network reference

After you can run **SMIB** stability and CCT work ([Lab 5](../900_labs/lab_05_stability_cct/index.md)), the next plant fidelity step is a **network** simulator. This course uses [ANDES](https://docs.andes.app/en/stable/) as that reference: load a case, run power flow and time-domain simulation, then apply the **same SciML evaluation ideas** (scenarios, operational labels, CCT brackets, manifests) you already used on SMIB.

ANDES is open-source (GPL v3). We summarize what you need here and point to the official docs for full tutorials and derivations — we do not republish the ANDES manual in this book.

:::{note} SMIB first
Foundations and assessed Labs 1–5 stay on classical SMIB. Treat this page as the bridge to network depth, not a replacement for Foundations.
:::

## Install (short)

Use the course ANDES environment from the repository root:

```powershell
conda env create -f envs/course_andes.yml
conda activate sciml_ps_andes
```

Course pin: **andes==2.0.0** in `envs/course_andes.yml`. After create/activate, run `andes prep` once if prompted. Do not mix ANDES 1.x and 2.x in the same lab narrative.

Optional notebook (Lab 5 extension): [`lab05_network_cct_andes.ipynb`](../900_labs/lab_05_stability_cct/lab05_network_cct_andes.ipynb).

Details: [ANDES installation](https://docs.andes.app/en/stable/tutorials/01-installation.html).

## Concepts you will touch (summaries)

| Idea in this course | Meaning for SciML labs | Details |
|---------------------|------------------------|---------|
| **Power flow (PFlow)** | Find a steady operating point before dynamics | [Power flow](https://docs.andes.app/en/stable/tutorials/03-power-flow.html) |
| **Time-domain (TDS)** | Simulate faults and clearing; get trajectories for labels / CCT | [Time-domain simulation](https://docs.andes.app/en/stable/tutorials/04-time-domain.html) |
| **Case file** | Documented network + machines + events | [Data and formats](https://docs.andes.app/en/stable/tutorials/05-data-and-formats.html) |
| **Plots / channels** | Extract angles, speeds, etc. for your metrics | [Plotting](https://docs.andes.app/en/stable/tutorials/06-plotting.html) |

Minimal workflow in words: load case → `PFlow.run()` → configure fault/clearing → `TDS.run()` → read trajectories → apply **your** stability rule and CCT search. Full API options stay in the tutorials above and the [reference](https://docs.andes.app/en/stable/reference/index.html).

## Preferred class network case: Kundur

| Item | Choice |
|------|--------|
| Case | `andes.get_case("kundur/kundur_full.xlsx")` |
| Why | Two-area multimachine plant; matches course stage C after SMIB |
| Official walkthrough | [Critical Clearing Time Mapping](https://docs.andes.app/en/stable/gallery/critical-clearing-time.html) |

That gallery sweeps fault clearing times across buses, classifies stable / unstable / non-convergent outcomes, and maps CCT. Use it to learn the **ANDES CCT workflow**. Your course extension (when assigned) still reports **SciML metrics**: signed CCT error, false-safe rate, and comparison to a learned surrogate — same spirit as Lab 5 on SMIB.

:::{tip} Start smaller if needed
On a first pass, fix **one** fault bus and a short clearing-time grid before running a full bus-wise map.
:::

## Self-study path (ANDES), then return here

1. [Installation](https://docs.andes.app/en/stable/tutorials/01-installation.html)  
2. [First simulation](https://docs.andes.app/en/stable/tutorials/02-first-simulation.html)  
3. [Power flow](https://docs.andes.app/en/stable/tutorials/03-power-flow.html)  
4. [Time-domain](https://docs.andes.app/en/stable/tutorials/04-time-domain.html)  
5. [Data and formats](https://docs.andes.app/en/stable/tutorials/05-data-and-formats.html)  
6. [Plotting](https://docs.andes.app/en/stable/tutorials/06-plotting.html)  

Then return to Lab 5 / this network path. Tutorials 07+ (eigenvalue, sweeps, contingency, …), the [Modeling guide](https://docs.andes.app/en/stable/modeling/index.html), and [Verification](https://docs.andes.app/en/stable/verification/index.html) are **further practice**, not assessed core.

## Other gallery examples (optional)

Full index: [ANDES Gallery](https://docs.andes.app/en/stable/gallery/index.html).

| Gallery | How it connects to this book |
|---------|------------------------------|
| [PINN surrogate (SMIB)](https://docs.andes.app/en/stable/gallery/pinn-surrogate.html) | Further practice after Labs 1–2 — does not replace them |
| [Low-inertia frequency (IEEE 14)](https://docs.andes.app/en/stable/gallery/low-inertia-freq.html) | Project / Advanced (frequency / RoCoF), not the CCT spine |
| [Forced oscillation (WECC 179)](https://docs.andes.app/en/stable/gallery/forced-oscillation.html) | Large-system elective / project |
| [RL oscillation damping (SMIB)](https://docs.andes.app/en/stable/gallery/smib-oscillation.html) | Outside the core three pillars; curiosity only |

## Honesty

Network simulation labels and CCT values are **operational** under a stated criterion and model set. They are not automatic certificates of real-world security. Always record ANDES version, case name, fault/clearing definitions, and the stability rule in your manifest.

## Citation

Hantao Cui et al., ANDES — [documentation](https://docs.andes.app/en/stable/), [GitHub](https://github.com/CURENT/andes). License: GPL v3.
