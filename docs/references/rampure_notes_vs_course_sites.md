# Rampure teaching sites: notes books vs course portals

**Audience:** Maintainers.  
**Recorded:** 2026-10-12 (from [rampure.org](https://rampure.org/), live notes sites, and chat).  
**Purpose:** Correct product-pattern facts for SciML_PS planning.

---

## How many Jupyter Book–style *notes books*?

As of this note, **two** public notes books in the EECS 245 / Math 124 style (not “one only”):

| Notes book | URL | Status |
|------------|-----|--------|
| EECS 245 — Mathematics for Machine Learning | https://notes.eecs245.org/ | Mature (10 chapters + appendix); [github.com/eecs245/notes](https://github.com/eecs245/notes) |
| Math 124 — Vectors, Matrices, and Applications | https://notes.math124.org/ | In progress (Fall 2026; planned 9 chapters; co-authors Kartik Prasanna & Suraj Rampure) |

Related: workshop template [github.com/math-124/notes-example](https://github.com/math-124/notes-example); EEI Days 2026 talk notes in [`eecs245_eei_days_2026/`](eecs245_eei_days_2026/).

---

## Does that mean many book websites + a course site every semester?

**Split yes; “new book every semester” no.**

| Layer | What he does | Count / cadence |
|-------|----------------|-----------------|
| **Notes / book** | One **living** notes site **per course subject** | Few (currently ~2 JB-style books) |
| **Course portal** | Separate ops site (syllabus, calendar, staff); often **term pages or archives** | Many offerings over a career (e.g. [eecs245.org](https://eecs245.org/), [eecs245.org/sp26/](https://eecs245.org/sp26/)) |
| **Older course hubs** | Slides / recordings / assignments sites for past UCSD–Berkeley classes | Many — **not** full notes books |

```text
ONE notes book per subject   →  notes.eecs245.org     (shared across terms; updated in place)
TERM portal / path           →  eecs245.org, /sp26/…  (calendar, staff; links TO the notes)

ONE notes book (growing)     →  notes.math124.org
+ course website button      →  Math 124 portal
```

**Do not:** create a new SciML_PS book domain every semester.  
**Do:** keep one SciML_PS book; add portal home or `portal/20XX-term/` (or git tag `offering-20XX`) when teaching.

---

## Also on rampure.org (not notes books)

He publishes materials for **many** courses (EECS 398, DSC 10/80/40A, Data 100, …). Those are open **course material hubs**, not additional full Jupyter Books like EECS 245 / Math 124.

---

## Implication for SciML_PS

| Decision | Choice |
|----------|--------|
| Notes books to build | **One** domain book (this repo) — same idea as one EECS 245 notes site |
| Later sibling books | Only if a truly different subject needs its own narrative (rare) |
| Per-semester | Portal / archive / git tag — **not** a fork of the whole book |
| Science TOC | Still three pillars — [`../guides/scope_lock_three_pillars.md`](../guides/scope_lock_three_pillars.md) |
| Product backlog | [`../guides/future_plans_online_resource.md`](../guides/future_plans_online_resource.md) |

### Layers to grow over time (product packaging)

```text
A  Forever book     book/  (foundations + 400/500/600 + labs)
B  Offering portal  portal/ when teaching
C  Media            slides/videos linked from chapters
D  Interaction      widgets/notebooks where intuition pays off
E  Feedback         Google Form on notes navbar
```

Copy his **ecosystem shape** (notes + portal + deep links + living updates). Do not copy his linear-algebra chapter order.
