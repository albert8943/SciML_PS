# Status and versions

## Public preview (v0.x)

SciML for PS is released early on purpose so learners and collaborators can use and improve it.

**Say both when you cite or announce it:** this is a **public preview (currently v0.1)** in the **v0.x** series, and it stays **under development until v1.0**. A site-wide under-development notice remains until that first stable edition.

| Stage | Meaning |
|-------|---------|
| **v0.1** (current) | First public preview tag (`v0.1.0`). Usable, incomplete. |
| **v0.x** | Preview series. Goals and TOC are stable; many chapters are Stub or Draft. |
| **v1.0** | First stable edition (see criteria below). Site-wide warning may be removed. |
| **v2.0+** | Later editions after major restructures. |

Roadmap: [ROADMAP.md](https://github.com/albert8943/SciML_PS/blob/master/ROADMAP.md).  
Release notes: [CHANGELOG.md](https://github.com/albert8943/SciML_PS/blob/master/CHANGELOG.md).  
Governance (v1.0 bar): [GOVERNANCE.md](https://github.com/albert8943/SciML_PS/blob/master/GOVERNANCE.md).

## How we bump versions

Maintainers and collaborators use this when tagging a release. Milestone *what* lives in the roadmap; this section is *when* to bump.

| Change | When to ship | Example |
|--------|--------------|---------|
| **v0.N → v0.N+1** (e.g. 0.1 → 0.2) | The matching checklist in [ROADMAP.md](https://github.com/albert8943/SciML_PS/blob/master/ROADMAP.md) is honestly done | Lab 1 runnable + early Foundations → **v0.2** |
| **v0.N.P → v0.N.P+1** (patch) | Fixes only; no new roadmap milestone | Broken Binder, typos, bad links → **v0.1.1** |
| **→ v1.0** | First stable edition criteria in [GOVERNANCE.md](https://github.com/albert8943/SciML_PS/blob/master/GOVERNANCE.md) (and the v1.0 list in the roadmap) | Foundations + Labs 1/3/5 + pillar cores **Stable** and reviewed |
| **→ v2.0+** | Major restructure of scope or TOC | New edition shape |

**Practice**

1. Open the next `v0.N` checklist in the roadmap.  
2. When those items are done, tag `v0.N.0`, update [CHANGELOG.md](https://github.com/albert8943/SciML_PS/blob/master/CHANGELOG.md), and deposit Zenodo when you use DOIs.  
3. Between milestones, use patch tags only.  
4. Do **not** invent unused minors (no forced path through 0.6–0.9). Skip numbers that have no milestone.  
5. Do **not** call it **v1.0** only because calendar time passed.

Chapter labels (**Stub** / **Draft** / **In review** / **Stable**) are per page. The book **version** is a whole tagged release.

## Chapter maturity labels

Authors mark pages near the top with one of:

| Label | Meaning |
|-------|---------|
| **Stub** | Outline and goals only; little runnable content |
| **Draft** | Readable teaching prose; examples and labs still growing |
| **In review** | Proposed as near-complete; awaiting outside or editor review |
| **Stable** | Reviewed for the current edition; still may receive errata |

After v1.0, per-page labels remain so individual chapters can improve without pretending the whole book is frozen.

## How to cite

Prefer a **versioned** citation when you rely on a specific wording or figure:

1. Use the site URL and the PDF cover **Last updated** stamp (git commit), or  
2. Cite a **tagged release** and Zenodo DOI once published (see root `CITATION.cff`).

Suggested form (update the version when you pin a release):

> Albert Poulose, *Scientific Machine Learning (SciML) for Power Systems (PS)*,  
> version 0.1 (public preview; under development until v1.0),  
> https://sciml4ps.albertpoulose.com, licensed under CC BY-NC-SA 4.0.

## Prefer the live notes

The HTML book is the primary product. The navbar **PDF** is an experimental snapshot; interactive material may flatten. Prefer linking the live page for teaching.
