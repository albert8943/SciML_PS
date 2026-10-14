# Governance — SciML for PS

**Status:** Founding rules for a collaborative living textbook (public preview 0.x).  
**Last updated:** 2026-10-14.

This project aims to remain useful for decades through continuous, credited contributions from experts and learners. It is not a one-author dump of research results.

## Roles

| Role | Responsibility |
|------|----------------|
| **Editor-in-chief (EIC)** | Overall direction, scope lock, release tags, dispute resolution, site warning / maturity policy. Founding EIC: Albert Poulose. |
| **Section editors** | Own a pillar or Labs (Dynamics, Stability, Identification, Laboratories). Review PRs in their area; propose chapter maturity upgrades. Appointed by the EIC with community notice. |
| **Reviewers** | Provide substantive review without long-term ownership. |
| **Contributors** | Anyone who opens issues, discussions, or signed-off PRs under [CONTRIBUTING.md](CONTRIBUTING.md). |

Credit: [CONTRIBUTORS.md](CONTRIBUTORS.md). Conduct: [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Decisions

1. **Lazy consensus** on routine edits: propose → discuss on the PR → merge if no blocking objection after a reasonable window (typically one week for non-urgent changes).
2. The **EIC breaks ties** and may fast-track errata, security, or broken builds.
3. **Scope changes** (new top-level pillars, dropping Labs 1–5, relicensing) require an issue labeled for governance, alignment with [docs/guides/scope_lock_three_pillars.md](docs/guides/scope_lock_three_pillars.md), and EIC approval. Section editors should be consulted when appointed.
4. **TOC titles** stay stable for years; pages grow underneath ([docs/guides/toc_architecture_decades.md](docs/guides/toc_architecture_decades.md)).

## Licensing of contributions

Contributions are accepted under the **Developer Certificate of Origin (DCO)** with **inbound = outbound** licensing:

- Content → CC BY-NC-SA 4.0  
- Code → MIT  

See [CONTRIBUTING.md](CONTRIBUTING.md). A future print or commercial edition of chapters that contain substantial third-party contributions will need those contributors’ consent or a rewrite of their parts. Core editorial chapters written by editors remain under the copyright holder’s dual-licensing freedom for NC teaching and separate commercial permission.

## Becoming a section editor

1. Sustained contributions (content, review, or labs) and domain expertise.  
2. Open a collaboration / section-editor interest issue or Discussion.  
3. EIC appointment announced in Discussions / CHANGELOG; `CODEOWNERS` and citation metadata updated.

Start small: one or two section editors in the first year is enough.

## Releases and maturity

| Stage | Meaning |
|-------|---------|
| **v0.x** | Public preview. Site-wide under-development warning stays on. |
| **v1.0** | First stable edition: Foundations, Labs 1 / 3 / 5, and each pillar’s core chapters are `Stable` and reviewed by at least one outside expert. Site-wide warning may be removed; per-page maturity labels remain. |
| **v2.0+** | Major restructures or second editions. |

Details: [book/100_front/status_and_versions.md](book/100_front/status_and_versions.md) (including [how we bump versions](book/100_front/status_and_versions.md#how-we-bump-versions)), [ROADMAP.md](ROADMAP.md), [CHANGELOG.md](CHANGELOG.md).

Tagged releases should attach the notes PDF when available and deposit to Zenodo for a version DOI.

## Institutional home (later)

When the first section editor joins, prefer moving the repository to a **GitHub organization** (for example `sciml4ps`) so the project outlives a single personal account. Old URLs should redirect. Optional later: education grants, IEEE PES education collaboration, JOSE / education paper at v1.0.

## Succession

If the EIC steps down, a successor is named in a governance issue with section-editor input when editors exist. Until then, the founding EIC remains responsible for continuity of the public site and licences.
