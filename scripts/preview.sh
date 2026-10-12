#!/usr/bin/env bash
# Local live preview for the SciML_PS Jupyter Book 2 site.
# Usage:
#   ./scripts/preview.sh
#   ./scripts/preview.sh --port 3001
#   ./scripts/preview.sh --execute

set -euo pipefail
export PYTHONIOENCODING=utf-8
export PYTHONUTF8=1
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

PORT=3000
EXECUTE=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --port) PORT="$2"; shift 2 ;;
    --execute) EXECUTE=1; shift ;;
    *) echo "Unknown arg: $1"; exit 1 ;;
  esac
done

if [[ ! -f "$ROOT/myst.yml" ]]; then
  echo "myst.yml not found at $ROOT" >&2
  exit 1
fi

if ! command -v jupyter >/dev/null 2>&1; then
  cat <<'EOF'
jupyter not found on PATH.

Create / activate the course env first:

  conda env create -f environment.yml
  conda activate sciml_ps

Then re-run:

  ./scripts/preview.sh
EOF
  exit 1
fi

if ! command -v node >/dev/null 2>&1; then
  cat <<'EOF'
Node.js (node) not found on PATH.

Jupyter Book 2 requires Node.js (pinned as conda package nodejs in environment.yml).
Activate / update the env, then retry:

  conda activate sciml_ps
  conda env update -f environment.yml --prune
  ./scripts/preview.sh
EOF
  exit 1
fi

echo "Repository root: $ROOT"
echo "Starting Jupyter Book preview (port $PORT)..."
echo "When ready, open: http://localhost:$PORT"
echo "Stop with Ctrl+C"
echo

ARGS=(book start --port "$PORT")
if [[ "$EXECUTE" -eq 1 ]]; then
  ARGS+=(--execute)
fi

exec jupyter "${ARGS[@]}"
