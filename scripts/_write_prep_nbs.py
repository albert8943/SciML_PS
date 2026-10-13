import json
from pathlib import Path

base = Path(__file__).resolve().parents[1] / "book/200_prep"


def write_nb(name: str, cells: list[tuple[str, str]]) -> None:
    nb = {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            }
        },
        "cells": [],
    }
    for kind, src in cells:
        if kind == "md":
            nb["cells"].append(
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": src.splitlines(keepends=True),
                }
            )
        else:
            nb["cells"].append(
                {
                    "cell_type": "code",
                    "metadata": {},
                    "outputs": [],
                    "execution_count": None,
                    "source": src.splitlines(keepends=True),
                }
            )
    path = base / name
    path.write_text(json.dumps(nb, indent=1), encoding="utf-8")
    print("wrote", path)


write_nb(
    "nb01_numpy_basics.ipynb",
    [
        (
            "md",
            "# Prep 01 — NumPy basics\n\nPractice array creation, slicing, and a simple plot.\n",
        ),
        (
            "code",
            "import numpy as np\n"
            "import matplotlib.pyplot as plt\n"
            "x = np.linspace(0, 2 * np.pi, 200)\n"
            "y = np.sin(x) + 0.1 * np.random.randn(x.size)\n"
            "plt.plot(x, y)\n"
            "plt.xlabel('x')\n"
            "plt.ylabel('y')\n"
            "plt.grid(True, alpha=0.3)\n"
            "plt.show()\n"
            "print(x.shape, float(y.mean()))\n",
        ),
    ],
)

write_nb(
    "nb02_ode_integration.ipynb",
    [
        (
            "md",
            "# Prep 02 — ODE integration\n\nIntegrate a damped oscillator with scipy.integrate.solve_ivp.\n",
        ),
        (
            "code",
            "import matplotlib.pyplot as plt\n"
            "from scipy.integrate import solve_ivp\n"
            "\n"
            "def rhs(t, z, zeta=0.2, w0=2.0):\n"
            "    x, v = z\n"
            "    return [v, -2 * zeta * w0 * v - w0**2 * x]\n"
            "\n"
            "sol = solve_ivp(rhs, (0, 10), [1.0, 0.0], max_step=1e-2)\n"
            "plt.plot(sol.t, sol.y[0])\n"
            "plt.xlabel('t')\n"
            "plt.ylabel('x')\n"
            "plt.grid(True, alpha=0.3)\n"
            "plt.show()\n",
        ),
    ],
)

write_nb(
    "nb03_nn_regression.ipynb",
    [
        (
            "md",
            "# Prep 03 — Tiny neural regression\n\nFit y = sin(x) with a small MLP when PyTorch is available.\n",
        ),
        (
            "code",
            "try:\n"
            "    import torch\n"
            "    from torch import nn\n"
            "    x = torch.linspace(-3, 3, 200).unsqueeze(1)\n"
            "    y = torch.sin(x)\n"
            "    model = nn.Sequential(nn.Linear(1, 32), nn.Tanh(), nn.Linear(32, 1))\n"
            "    opt = torch.optim.Adam(model.parameters(), lr=1e-2)\n"
            "    for _ in range(1000):\n"
            "        opt.zero_grad()\n"
            "        loss = ((model(x) - y) ** 2).mean()\n"
            "        loss.backward()\n"
            "        opt.step()\n"
            "    print('torch loss', float(loss))\n"
            "except ImportError:\n"
            "    print('PyTorch not installed in this env — use course_core with pytorch.')\n",
        ),
    ],
)

write_nb(
    "nb04_gradients.ipynb",
    [
        (
            "md",
            "# Prep 04 — Gradients\n\nCompare a hand derivative to automatic differentiation when PyTorch is available.\n",
        ),
        (
            "code",
            "import numpy as np\n"
            "w, t = 2.0, 0.3\n"
            "print('analytic', w * np.cos(w * t))\n"
            "try:\n"
            "    import torch\n"
            "    tt = torch.tensor(t, requires_grad=True)\n"
            "    f = torch.sin(w * tt)\n"
            "    f.backward()\n"
            "    print('autograd', float(tt.grad))\n"
            "except ImportError:\n"
            "    print('Install PyTorch in the course env for AD practice.')\n",
        ),
    ],
)
