# 2026-10-14 — Full outline page and per-chapter references

## What changed

| Area | Files |
|------|-------|
| One-page outline | `book/100_front/outline.md` (new; per-section tables: linked page, summary, maturity, lab); `myst.yml` TOC + **Outline** navbar action; links from `book_map.md`, `how_to_use.md`, home cards in `book/index.md` (now every section) |
| Bibliography | `references.bib` (new, 16 entries); `myst.yml` `project.bibliography` |
| Citations | Short IDs replaced by `[@key]` / `@key` across Foundations, Stability, Identification, Dynamics/Advanced overviews, prep overview, home, ANDES chapter; duplicated Reading / Further reading lines replaced by forward pointers |
| Reading list | `book/990_reference/reading_list.md` rewritten: how references work, core textbooks, simulators, maths refresher, PBDL reuse map; PSCC 2024 tutorial moved to `related_resources.md` |
| Template / contributing | `book/chapter_template.md` citation guidance + `Maturity: Stub` note; `CONTRIBUTING.md` "Adding a reference", "Adding a chapter", PR checklist |
| Checks | `scripts/check_book.py` (new) run in `.github/workflows/build-book.yml` before the build |
| Maturity labels | Lab 2, Lab 4, Dynamics overview, Advanced overview → `Maturity: Stub`; prep overview → `Maturity: Draft` |
| PDF fix | `scripts/build_pdf.py`: wrap arrow macros glued to the next word |

## Bibliography provenance

Metadata fetched from `https://doi.org/<doi>` (BibTeX content negotiation) for all DOI sources. Kundur et al. 2004 authors from Semantic Scholar (Crossref record has none). Kundur and Malik 2nd ed. (2022) and Ljung 2nd ed. from Open Library ISBN records. Baydin et al. cited as the arXiv record (2015), key `baydin2015automatic`.

## Verification

- `python scripts/check_book.py`: 49 TOC pages, 16 bib entries, 0 errors, 0 warnings.
- HTML build: 49 pages, no citation or cross-reference warnings; References render per page (Forward PINNs lists Raissi only; Stability and CCT lists Kundur 2004, Hatziargyriou 2021, Kundur and Malik).
- PDF build: BibTeX 16 items, 0 LaTeX errors, 0 undefined citations. Three BibTeX "empty year" warnings for web entries (expected).

## Gotcha

An at-sign inside a `%` comment in `references.bib` breaks the MyST BibTeX reader; `check_book.py` now flags it.

## Not committed

Awaiting user instruction.
