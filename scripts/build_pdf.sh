#!/usr/bin/env bash
# Build the full-book PDF for SciML_PS (MyST → LaTeX).
# Usage: ./scripts/build_pdf.sh
# Requires: sciml_ps env (jupyter-book) and a LaTeX distribution with latexmk.

set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if ! command -v python >/dev/null 2>&1; then
  echo "python not on PATH. Run: conda activate sciml_ps" >&2
  exit 1
fi

echo "Building PDF from $ROOT ..."
python "$ROOT/scripts/build_pdf.py"
echo "Done. PDF: exports/sciml_ps_notes.pdf"
