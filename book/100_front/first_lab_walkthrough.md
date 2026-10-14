# Your first lab

```{note} Maturity: Draft
Readable teaching prose; examples, figures, and exercises are still growing. See [Status and versions](status_and_versions.md) and [Join and contribute](contribute.md).
```

```{warning} Under development (v0.x public preview)
Launch buttons and the notebook may change while the notes grow. Help improve these steps: [Join and contribute](contribute.md).
```

This page runs [Lab 1](../900_labs/lab_01_reference_sim/index.md) with no programming background. The notebook simulates a classical single-machine swing model [@kundur2022power]. Plan on about 15 minutes. You will simulate one generator after a short fault and see a plot of rotor angle against time.

Three ways to run it, in the order a new reader should try:

1. **Google Colab** below (browser, Google account, no install)
2. **Binder** if you prefer not to use Google (browser, no install, slower the first time)
3. **Local install** when you want the canonical copy on your own computer

Assessed coursework should use local install once you are comfortable. The full comparison is [Running notebooks](running_notebooks.md). Binder and Colab need the GitHub repository to be public. Until then, use the local steps.

## Before you click

A notebook is a page of boxes called cells. Text cells explain. Code cells compute. You run a code cell with its play button. The computer remembers the cells you have already run until you restart the session.

## Route A. Google Colab

You need a free Google account.

1. Open the Lab 1 notebook in Colab: [Open Lab 1 in Colab](https://colab.research.google.com/github/albert8943/SciML_PS/blob/master/book/900_labs/lab_01_reference_sim/lab01_reference_sim.ipynb).
   What you should see: a Colab page titled like the lab, with a column of gray and white cells. The first cell is an explanation. The next cell is code.
2. If Colab asks you to sign in, sign in. If it warns you that the notebook comes from GitHub, continue. That warning is expected.
3. Click the play button on the **first code cell** (it starts with `import sys`).
   What you should see: Colab may spend a minute installing the teaching package. The cell finishes with the line `imports ok`. A green check, or a number in brackets beside the cell, means that cell finished.
4. Click the play button on the **next code cell** (it starts with `# Same physics, two numerical settings`).
   What you should see: four printed lines. Two say whether a fine and a coarse simulation failed. Two say whether each result was stable.
5. Run the **following code cell** (it starts with `fig, ax = plt.subplots`).
   What you should see: a plot. The horizontal axis is time in seconds. The vertical axis is rotor angle in radians. Vertical lines mark the fault and the clearing time.
6. Run the remaining code cells in order.
   What you should see: a short table of scenarios, the words `train` and `test`, and a line that starts with `wrote` and ends with `lab01_manifest.json`.

To run every cell without clicking each one: menu **Runtime**, then **Run all**. Wait until the last cell finishes.

Your edits stay in your Colab copy. They do not change the book. To suggest a fix, use [Feedback](feedback.md).

## Route B. Binder

Binder builds a temporary JupyterLab from this repository. The first launch can take several minutes. Your edits disappear when you close the tab.

1. Open [Launch Lab 1 on Binder](https://mybinder.org/v2/gh/albert8943/SciML_PS/master?filepath=book/900_labs/lab_01_reference_sim/lab01_reference_sim.ipynb).
   What you should see: a waiting page, then Jupyter with the Lab 1 notebook open.
2. Menu **Run**, then **Run All Cells**.
   What you should see: the same `imports ok` line, the same four printed lines, and the same angle plot as in Route A. Binder uses the copy of the code already in the repository, so the setup cell should print `Using local src:`.

## Route C. On your own computer

Do this when Colab and Binder are unavailable, or when a teacher asks for a local run. Install [Miniconda](https://docs.anaconda.com/miniconda/) first and allow the installer to add `conda` to your PATH. Then get the repository either by downloading the ZIP from the GitHub **Code** button or by cloning it.

### Windows

In PowerShell, from the folder that contains `environment.yml`:

```powershell
.\scripts\setup_env.ps1
conda activate sciml_ps
pip install -e .
jupyter lab
```

What you should see: a browser tab opens with a file list. Open `book`, then `900_labs`, then `lab_01_reference_sim`, then `lab01_reference_sim.ipynb`. Menu **Run**, then **Run All Cells**. The setup cell should print `sciml_ps already importable` or `Using local src:`.

### Mac or Linux

The Windows script is a small wrapper around the same commands. In a terminal, from the folder that contains `environment.yml`:

```bash
conda env create -f environment.yml
conda activate sciml_ps
pip install -e .
jupyter lab
```

If the environment already exists, use `conda env update -f environment.yml --prune` instead of `conda env create`. Then follow the same Jupyter clicks as on Windows.

Previewing the whole website (the HTML book) is a separate, optional step: [Preview this book locally](preview_locally.md).

## Troubleshooting

| What happened | What to do |
|---------------|------------|
| The setup cell says it is installing from GitHub, then fails | Binder and Colab need a **public** repository. Until this repository is public, use Route C |
| A later cell says `sciml_ps` is not defined, or a name is missing | Restart the kernel (Colab: **Runtime → Restart session**. Jupyter: **Kernel → Restart**). Run all cells again from the top |
| Binder has been on a waiting page for a long time | The first build often takes several minutes. Leave the tab open. If it errors, use Route A or Route C |
| Colab shows a red error in a cell | Read the **last** line of the error. If it is still unclear, copy that last line into a [feedback issue](feedback.md). Leave out private data |
| You see no plot | Run the cell that starts with `fig, ax = plt.subplots` after the simulation cell has finished |
| You changed a cell and the result looks stale | Run all cells from the top again. The kernel only knows what it has run in this session |

## After the plot

Read the Lab 1 goals on the [lab page](../900_labs/lab_01_reference_sim/index.md), then [SMIB dynamics](../300_foundations/02_smib_dynamics.md) for the equation behind the plot. If the power-system words are new, read [Power systems for ML people](../200_prep/bridge_power_systems_for_ml.md). If the learning words are new, read [Machine learning for power-systems people](../200_prep/bridge_ml_for_power_systems.md).
