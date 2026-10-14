# Binder student runtime

This folder is the **student** environment for [mybinder.org](https://mybinder.org/) launches from the lab pages.

| File | Role |
|------|------|
| `environment.yml` | Lean conda env (NumPy / SciPy / Matplotlib / Jupyter) |
| `postBuild` | `pip install -e .` so `sciml_ps` is importable |

**Do not** add Jupyter Book, Node.js, or ANDES here. Author site preview stays on the repository-root `environment.yml`. Network / ANDES work uses `envs/course_andes.yml` on a local machine.

After the GitHub repository is **public**, Binder URLs on the lab pages and [Running notebooks](../book/100_front/running_notebooks.md) become usable. First builds can take several minutes.
