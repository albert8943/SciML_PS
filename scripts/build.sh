#!/usr/bin/env bash
# Build static HTML for the SciML_PS book.
# Usage: ./scripts/build.sh

set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if ! command -v jupyter >/dev/null 2>&1; then
  echo "jupyter not on PATH. Run: conda activate sciml_ps" >&2
  exit 1
fi

echo "Building static site from $ROOT ..."
jupyter book build
echo "Done. Open the HTML index reported by the CLI (often under _build/)."
