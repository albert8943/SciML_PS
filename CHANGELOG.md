# Changelog

All notable changes to the SciML for PS notes and teaching package are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project uses [Semantic Versioning](https://semver.org/) for public tags
(`vMAJOR.MINOR.PATCH`). Until **v1.0.0**, treat the resource as a public preview.

## [Unreleased]

### Added

- Audience pathways: [Start here](book/100_front/start_here.md) (background and role), three bridge primers, [Your first lab](book/100_front/first_lab_walkthrough.md), two-way [glossary](book/990_reference/glossary.md), and a Before you start box on chapter and lab pages
- Notebook launch stack (under development): [Running notebooks](book/100_front/running_notebooks.md) — local install canonical, Binder primary online, Colab secondary; lean `binder/` student env; Materials badges on Labs 1 and 3; collaboration invite on launch paths
- Full outline page (`/outline`): every chapter and lab on one page with summary, maturity, and lab; Outline navbar button; home cards for every section
- Shared bibliography `references.bib` (metadata from DOIs/publisher pages); each page gets its own References section from `[@key]` citations
- `scripts/check_book.py` (outline matches the TOC, bib keys unique with doi/url, cited keys exist), run in CI
- CONTRIBUTING: "Adding a reference" and "Adding a chapter"

### Changed

- Short citation IDs (B1, R3, R-K04, ...) replaced by citations; Reading and Further reading no longer repeat each other
- Reading list cut down to core textbooks, simulators, maths refresher, and the PBDL reuse map
- Maturity labels made uniform (`Maturity: Stub` / `Draft`) on all chapter, lab, and overview pages

### Fixed

- PDF build: arrows glued to the next word (`\rightarrowunstable`) no longer cause undefined control sequences

## [0.1.0] — 2026-10-14

### Added

- Collaboration scaffolding: CONTRIBUTING (DCO), CODE_OF_CONDUCT, GOVERNANCE, CONTRIBUTORS, ROADMAP, CHANGELOG
- Student pages: related open resources, join and contribute, status and versions
- GitHub issue / PR templates, CODEOWNERS, DCO check workflow
- Site-wide under-development notice and chapter maturity labels in the template
- Phase 0 gate audit note; `scripts/phase2_go_public.ps1` and `phase2_set_doi.ps1`
- Collaboration invite drafts under `docs/guides/collaboration/`

### Positioning

- Documented niche claim and neighbors (no “first / only / best” wording)

### Website (sibling repo)

- Teaching page Open educational resources card + launch news item on albertpoulose.com

## [0.0.1] — 2026-10-13

### Added

- Jupyter Book 2 / MyST scaffold with three-pillar TOC
- Dual licence (CC BY-NC-SA 4.0 content / MIT code), CITATION.cff
- CI build and Pages deploy workflow (custom domain planned)
- Experimental full-book PDF export
- Foundations / Stability / Identification stubs and Labs 1–5 placeholders

[Unreleased]: https://github.com/albert8943/SciML_PS/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/albert8943/SciML_PS/releases/tag/v0.1.0
[0.0.1]: https://github.com/albert8943/SciML_PS/releases/tag/v0.0.1
