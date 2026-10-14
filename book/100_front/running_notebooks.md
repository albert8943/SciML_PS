# Running notebooks

```{warning} Under development (v0.x public preview)
Launch paths and notebooks may change while the notes grow. Contributions are welcome — help harden Binder, Colab setup cells, or new lab notebooks: [Join and contribute](contribute.md). Version labels: [Status and versions](status_and_versions.md).
```

New to notebooks? Follow the numbered steps in [Your first lab](first_lab_walkthrough.md) (Colab, then Binder, then a local install). This page is the full comparison of the three launch paths.

These living notes keep every assessed notebook in the [GitHub repository](https://github.com/albert8943/SciML_PS). You can run them in three ways. Use them in this order of trust:

1. **Local install** — canonical (always works once the repo is cloned)
2. **Binder** — primary online launch (temporary JupyterLab from this repo)
3. **Google Colab** — secondary convenience (personal copy in Google’s cloud)

**Binder and Colab need a public GitHub repository.** Until `albert8943/SciML_PS` is public, use **local install** only. Session edits in Binder or Colab do **not** write back to GitHub; to improve the book, open a pull request ([Contribute](contribute.md)).

## 1. Local install (canonical)

Best for assessed work and for decades of reproducible teaching.

```bash
git clone https://github.com/albert8943/SciML_PS.git
cd SciML_PS
conda env create -f environment.yml
conda activate sciml_ps
pip install -e .
```

Then open the lab notebook (for example `book/900_labs/lab_01_reference_sim/lab01_reference_sim.ipynb`) with Jupyter.

To preview the **book site** locally (HTML), see [Preview this book locally](preview_locally.md). That author path also uses `environment.yml` and needs Node.js for Jupyter Book 2.

Optional network / ANDES path (Lab 5 extension only): use [`envs/course_andes.yml`](https://github.com/albert8943/SciML_PS/blob/master/envs/course_andes.yml) on your machine — not Binder.

## 2. Binder (primary online)

Opens a **temporary** JupyterLab built from this repository. Your edits live only for that session.

- First launch after a change can take **several minutes** while Binder builds the image.
- Uses the lean student env under `binder/` (not the author Jupyter Book stack).
- Does **not** include ANDES.

Example — Lab 1:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/albert8943/SciML_PS/master?filepath=book/900_labs/lab_01_reference_sim/lab01_reference_sim.ipynb)

Lab pages that already ship a notebook also carry a Binder badge under **Materials**.

## 3. Google Colab (secondary)

Opens a **personal copy** of the notebook on Google’s servers. Convenient for a quick try; still not a substitute for local install on assessed work.

Example — Lab 1:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/albert8943/SciML_PS/blob/master/book/900_labs/lab_01_reference_sim/lab01_reference_sim.ipynb)

Run the notebook’s first setup cell so `sciml_ps` installs from GitHub when needed.

## Which labs?

| Lab | Local | Binder / Colab |
|-----|-------|----------------|
| [Lab 1](../900_labs/lab_01_reference_sim/index.md) | Yes | Yes (badges on the lab page) |
| [Lab 3](../900_labs/lab_03_inertia_damping_id/index.md) | Yes | Yes |
| Labs 2 and 4 | When notebooks arrive | Same — badges arrive with the notebook |
| [Lab 5](../900_labs/lab_05_stability_cct/index.md) SMIB path | Yes when the SMIB notebook ships | Planned with that notebook |
| Lab 5 ANDES network extension | **Local only** (`course_andes`) | Not on Binder / Colab |

## Invite collaboration

If Binder builds fail, Colab install cells break, or you want to add launch badges for a new notebook, please [Join and contribute](contribute.md). Improving these launch paths is a welcome contribution to this public preview.
