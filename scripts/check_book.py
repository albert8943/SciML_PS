#!/usr/bin/env python
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Albert Poulose
"""Consistency checks for the book's outline and shared bibliography.

Fails (exit 1) when:

- a ``toc`` page in ``myst.yml`` is missing from, or repeated in, the Full outline;
- a link in the Full outline points to a file that does not exist;
- a bib key is duplicated, or an entry has neither ``doi`` nor ``url``;
- a page in the ``toc`` cites a key that is not in the bibliography.

Warnings (exit 0) when a bib entry is unused, or when a chapter, pillar, or lab page
has no ``Before you start`` box.

Usage: ``python scripts/check_book.py``
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MYST = ROOT / "myst.yml"
OUTLINE = ROOT / "book" / "100_front" / "outline.md"
# Pages that are entry points rather than outline rows.
OUTLINE_EXEMPT = {"book/index.md"}

TOC_FILE = re.compile(r"^\s*-\s*file:\s*(\S+)\s*$", re.MULTILINE)
BIB_FILE = re.compile(r"^\s*bibliography:\s*\n((?:\s*-\s*\S+\s*\n)+)", re.MULTILINE)
MD_LINK = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")
BIB_ENTRY = re.compile(r"^@(\w+)\s*\{\s*([^,\s]+)\s*,", re.MULTILINE)
CITE = re.compile(r"(?<![\w.@/])@([A-Za-z][\w:-]*[A-Za-z0-9])")
FENCE = re.compile(r"^(`{3,}|~{3,}).*?^\1\s*$", re.MULTILINE | re.DOTALL)
INLINE_CODE = re.compile(r"`[^`\n]*`")
HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)


def toc_files(myst_text: str) -> list[str]:
    toc = myst_text.split("\n  toc:", 1)[1].split("\nsite:", 1)[0]
    return TOC_FILE.findall(toc)


def bib_paths(myst_text: str) -> list[Path]:
    m = BIB_FILE.search(myst_text)
    if not m:
        return []
    return [ROOT / line.strip().lstrip("-").strip() for line in m.group(1).splitlines() if line.strip()]


def page_text(path: Path) -> str:
    if path.suffix == ".ipynb":
        cells = json.loads(path.read_text(encoding="utf-8"))["cells"]
        return "\n".join("".join(c["source"]) for c in cells if c["cell_type"] == "markdown")
    return path.read_text(encoding="utf-8")


def cited_keys(text: str) -> set[str]:
    for pattern in (FENCE, HTML_COMMENT, INLINE_CODE):
        text = pattern.sub("", text)
    return set(CITE.findall(text))


def bib_entries(paths: list[Path]) -> tuple[list[str], list[str]]:
    keys: list[str] = []
    missing_link: list[str] = []
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for n, line in enumerate(text.splitlines(), 1):
            if line.lstrip().startswith("%") and "@" in line:
                missing_link.append(f"{path.name}:{n} (at-sign in a comment breaks the BibTeX reader)")
        starts = [m for m in BIB_ENTRY.finditer(text) if m.group(1).lower() not in {"comment", "string", "preamble"}]
        for i, m in enumerate(starts):
            body = text[m.end(): starts[i + 1].start() if i + 1 < len(starts) else len(text)]
            keys.append(m.group(2))
            if not re.search(r"^\s*(doi|url)\s*=", body, re.MULTILINE | re.IGNORECASE):
                missing_link.append(m.group(2))
    return keys, missing_link


def pages_needing_before_you_start() -> list[Path]:
    """Chapter, pillar, and lab pages that should carry a Before you start box."""
    pages: list[Path] = []
    for folder in (
        "300_foundations",
        "400_dynamics",
        "500_stability",
        "600_identification",
        "700_advanced",
    ):
        pages.extend(sorted((ROOT / "book" / folder).glob("*.md")))
    pages.extend(sorted((ROOT / "book" / "900_labs").glob("lab_*/index.md")))
    return pages


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    myst_text = MYST.read_text(encoding="utf-8")
    toc = toc_files(myst_text)

    outline_links = Counter()
    for line in OUTLINE.read_text(encoding="utf-8").splitlines():
        for i, target in enumerate(MD_LINK.findall(line)):
            if "://" in target:
                continue
            resolved = (OUTLINE.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"outline: broken link {target}")
                continue
            # The first link of a table row names the page that row describes.
            if i == 0 and line.startswith("| ["):
                outline_links[resolved.relative_to(ROOT).as_posix()] += 1
    for page in toc:
        if page in OUTLINE_EXEMPT:
            continue
        n = outline_links.get(page, 0)
        if n != 1:
            errors.append(f"outline: {page} appears {n} times as a row link (expected 1)")

    keys, missing_link = bib_entries(bib_paths(myst_text))
    for key, n in Counter(keys).items():
        if n > 1:
            errors.append(f"bib: duplicate key {key}")
    for key in missing_link:
        errors.append(f"bib: {key}" if "at-sign" in key else f"bib: {key} has neither doi nor url")

    known = set(keys)
    used: set[str] = set()
    for page in toc:
        cites = cited_keys(page_text(ROOT / page))
        used |= cites
        for key in sorted(cites - known):
            errors.append(f"cite: {page} cites unknown key @{key}")
    for key in sorted(known - used):
        warnings.append(f"bib: {key} is not cited on any page")

    for page in pages_needing_before_you_start():
        if "Before you start" not in page.read_text(encoding="utf-8"):
            rel = page.relative_to(ROOT).as_posix()
            warnings.append(f"before-you-start: {rel} has no Before you start box")

    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    print(f"check_book: {len(toc)} toc pages, {len(known)} bib entries, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
