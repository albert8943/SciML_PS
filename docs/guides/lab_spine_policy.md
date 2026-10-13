# Lab spine and external repositories

**Audience:** Maintainers.  
**Status:** Locked for the first offerings (aligned with course planning report §6).  
**Recorded:** 2026-10-13 (product decision for future reference).

---

## Decision

Keep **exactly five assessed laboratories** (Labs 1–5). Do **not** grow the lab *list* to look more complete. Enhance **depth** (runnable notebooks and helpers), not count.

| Lab | Role in the spine | Priority to deepen |
|-----|-------------------|--------------------|
| 1 | Reference SMIB simulation and scientific dataset | First (already notebook + `sciml_ps.smib`) |
| 2 | Supervised surrogate versus PINN | After Lab 1 runs cleanly |
| 3 | Inertia and damping (\(H\), \(D\)) estimation | Second (classical LS + loss surface; PINN next) |
| 4 | Generalization of a learned dynamic model | After Labs 1–3 |
| 5 | Stability and CCT | Third among “must run” (protocol + Lab 1 tooling; ANDES just-in-time — **not** in Prep) |

Suggested finish order for runnable offerings: **1 → 3 → 5**, then 2 and 4.

Five labs for a ~16-week course is already a full assessed load. Extra labs dilute quality.

---

## Where things live (student chrome)

| Surface | What belongs there |
|---------|-------------------|
| [`book/900_labs/`](../../book/900_labs/) | The five tasks, status, how to run **this** course’s code (`sciml_ps`, lab notebooks) |
| [`book/990_reference/reading_list.md`](../../book/990_reference/reading_list.md) | Optional books, tutorials, and **pinned tools** (ANDES, DeepXDE, torchdiffeq, …) with licenses |
| Instructor / planning docs | Full bibliography, attribution register, third-party course audits |

The Labs index answers: **what do I submit?**  
It does **not** answer: **what exists on GitHub?**

---

## External GitHub repos — do / don’t

**Do**

- Teach from code **in this repository** (`src/sciml_ps/`, lab notebooks under `book/900_labs/`).
- When a lab needs an external simulator or library, pin **one** version in `envs/` and cite it in Reference / the lab brief.
- Keep longer “related courses and packages” lists in the reading list or `docs/planning/` / `docs/references/`, with license checks (planning report § attribution).

**Don’t**

- Paste catalogs of third-party course repos onto the Labs table.
- Point students at research campaign repos (e.g. Estimation Mode A/B bakeoffs, sealed ANDES paper runs) as if they were course labs.
- Treat other universities’ SciML course GitHubs as redistributable lab materials without a license and attribution check.

---

## Relationship to pillars

Labs serve the three applications (dynamics / stability / identification); they are not a fourth pillar. Pillar width rules stay in [`scope_lock_three_pillars.md`](scope_lock_three_pillars.md). Lab *count* rules stay here.

---

## Related

- Course planning report §6 laboratory design — `docs/planning/SciML_for_Power_Systems_Course_Development_Report.md`
- Student lab index — [`book/900_labs/README.md`](../../book/900_labs/README.md)
- Sidebar / TOC longevity — [`toc_architecture_decades.md`](toc_architecture_decades.md)
- Maintainer handbook — [`using_preview_edit_and_long_term_development.md`](using_preview_edit_and_long_term_development.md)
