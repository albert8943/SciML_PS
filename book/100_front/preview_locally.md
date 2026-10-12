# Preview this book locally

Use these commands from the **repository root** (the folder that contains `myst.yml`). After the server starts, open the URL printed by the CLI (usually `http://localhost:3000`).

## 1. One-time environment setup

The course environment installs **Python**, **Jupyter Book 2**, and **Node.js** (required by JB2’s MyST site server).

```bash
conda env create -f environment.yml
conda activate sciml_ps
```

On Windows PowerShell you can instead run:

```powershell
.\scripts\setup_env.ps1
conda activate sciml_ps
```

If the environment already exists and dependencies changed (for example after Node.js was added):

```bash
conda env update -f environment.yml --prune
conda activate sciml_ps
```

Confirm both tools:

```bash
jupyter book --help
node --version
```

## 2. Live preview (recommended while reading or editing)

### Option A — helper script (Windows)

```powershell
conda activate sciml_ps
.\scripts\preview.ps1
```

Optional port or notebook execution at build time:

```powershell
.\scripts\preview.ps1 -Port 3001
.\scripts\preview.ps1 -Execute
```

### Option B — helper script (macOS / Linux)

```bash
conda activate sciml_ps
chmod +x scripts/preview.sh scripts/build.sh   # once
./scripts/preview.sh
```

```bash
./scripts/preview.sh --port 3001
./scripts/preview.sh --execute
```

### Option C — raw Jupyter Book commands

On Windows, bind to IPv4 loopback (recommended). Without this, the server may listen only on `::1`, and some browsers fail on `http://localhost:3000`.

```powershell
conda activate sciml_ps
$env:PYTHONUTF8 = "1"
$env:HOST = "127.0.0.1"
jupyter book start --port 3000 --keep-host
```

```bash
conda activate sciml_ps
export HOST=127.0.0.1
jupyter book start --port 3000 --keep-host
```

```bash
jupyter book start --port 3001 --keep-host
jupyter book start --execute --keep-host
```

Edit any page under `book/`, save, and refresh the browser.

**Open in the browser:** `http://127.0.0.1:3000/` or `http://localhost:3000/`  
The preview process must stay running in that terminal (do not close it).

## 3. Static HTML build (no live server)

### Windows

```powershell
conda activate sciml_ps
.\scripts\build.ps1
```

### macOS / Linux

```bash
conda activate sciml_ps
./scripts/build.sh
```

### Raw command

```bash
jupyter book build
```

Open the `index.html` path printed by the CLI (often under `_build/`).

## 4. What you should see

- Sidebar parts: Front matter, Preparation, Foundations, Dynamics, Stability, Identification, Advanced, Laboratories, Reference
- This page under Front matter
- Stub chapters until prose is filled

## 5. Troubleshooting

| Symptom | Fix |
|---------|-----|
| Page will not load / connection refused | Start the server first (`.\scripts\preview.ps1`) and leave that terminal open |
| `localhost:3000` fails but server “started” | Use `http://127.0.0.1:3000/` or restart with `$env:HOST="127.0.0.1"; jupyter book start --keep-host` (scripts do this) |
| `jupyter` / `jupyter book` not found | `conda activate sciml_ps` (or re-run `.\scripts\setup_env.ps1`) |
| `node` not found / JB asks to install Node | `conda activate sciml_ps` then `conda env update -f environment.yml --prune` |
| Unicode / emoji crash in Windows console | Scripts set `PYTHONUTF8=1`; or run `$env:PYTHONUTF8=1` before `jupyter book start` |
| Port already in use | `.\scripts\preview.ps1 -Port 3001` |
| New page missing from sidebar | Add the file under `project.toc` in `myst.yml` |
| Theme download slow first time | Wait; JB2 caches templates under `_build/templates/` |
| CLI flag unknown | Run `jupyter book --help` — JB2 names can change slightly |

Maintainer detail (editing rules, decades-long growth) lives in the git repo under the `docs/guides/` folder (not a book page).
