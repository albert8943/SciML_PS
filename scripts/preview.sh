#!/usr/bin/env bash
# Local live preview for the SciML_PS Jupyter Book 2 site.
# Usage:
#   ./scripts/preview.sh
#   ./scripts/preview.sh --port 3001
#   ./scripts/preview.sh --execute

set -euo pipefail
export PYTHONIOENCODING=utf-8
export PYTHONUTF8=1
# JB2 theme UI + content server; PDF redirects use http://localhost:<content-port>.
# Keep HOST=localhost so redirects match. See docs/guides/site_hosting.md.
export HOST="${HOST:-localhost}"
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

# Canonical book URL (theme UI). Content/PDF server is usually PORT+100 (3100).
BOOK_URL="http://localhost:${PORT}/"
PDF_URL="http://localhost:${PORT}/exports/sciml_ps_notes.pdf"

if command -v ss >/dev/null 2>&1 && ss -ltn "sport = :$PORT" 2>/dev/null | grep -q ":$PORT"; then
  echo "Preview already running."
  echo "Open this URL only: $BOOK_URL"
  echo "PDF button:          $PDF_URL  (via JB content port; use Chrome/Edge)"
  echo "Do not start a second ./scripts/preview.sh (extra UI ports)."
  exit 0
elif command -v lsof >/dev/null 2>&1 && lsof -iTCP:"$PORT" -sTCP:LISTEN >/dev/null 2>&1; then
  echo "Preview already running."
  echo "Open this URL only: $BOOK_URL"
  echo "PDF button:          $PDF_URL  (via JB content port; use Chrome/Edge)"
  echo "Do not start a second ./scripts/preview.sh (extra UI ports)."
  exit 0
fi

# Navbar PDF → /exports/sciml_ps_notes.pdf (static_files). Does not auto-rebuild.
PDF_PATH="$ROOT/exports/sciml_ps_notes.pdf"
if [[ -f "$PDF_PATH" ]]; then
  if command -v python >/dev/null 2>&1; then
    python "$ROOT/scripts/build_pdf.py" --sync-only >/dev/null 2>&1 || true
  fi
  echo "PDF button serves the last built file: exports/sciml_ps_notes.pdf"
  echo "After editing content, run ./scripts/build_pdf.sh then hard-refresh the PDF URL."
else
  echo "WARNING: exports/sciml_ps_notes.pdf missing — navbar PDF will 404."
  echo "Build it with: ./scripts/build_pdf.sh"
fi

echo "Starting Jupyter Book preview..."
echo "Open this URL only: $BOOK_URL"
echo "PDF navbar uses the same site (JB also listens on ~$((PORT+100)) for files)."
echo "Stop with Ctrl+C"
echo

ARGS=(book start --port "$PORT" --keep-host)
if [[ "$EXECUTE" -eq 1 ]]; then
  ARGS+=(--execute)
fi

exec jupyter "${ARGS[@]}"
