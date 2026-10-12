# Scope lock: three pillars are enough (for now)

**Status:** Locked teaching architecture for SciML_PS.  
**Audience:** Maintainers (not a student-facing book page).  
**Aligned with:** [`docs/planning/SciML_for_Power_Systems_Course_Development_Report.md`](../planning/SciML_for_Power_Systems_Course_Development_Report.md) §1 three application categories.  
**Recorded:** 2026-10-12 (chat decision for future reference).

---

## Decision

The book’s **core generalization** is three power-system SciML questions:

| Pillar | Folder | Engineering question |
|--------|--------|----------------------|
| Dynamics | `400_dynamics` | How will the system evolve under specified inputs, parameters, and disturbances? |
| Stability | `500_stability` | Will the system remain stable, and how close is it to a stability boundary? |
| Identification | `600_identification` | Which parameters and dynamic relationships explain the measurements? |

Shared trunk: `200_prep` → `300_foundations` (SMIB + core methods).  
Practice: `900_labs`. Frontiers / overflow: `700_advanced`.  
Insert room: 100-spacing part IDs (see maintainer handbook §5).

**Verdict:** These three pillars are **enough for now**. Do **not** widen the *core* definition of the book to “all AI for power.”

---

## Why this is enough

- Covers the main SciML uses in power-system *dynamic* work: forward models, engineering decisions, inverse problems.
- Broad enough to teach for years; narrow enough that chapters and labs can stay deep.
- Matches the course planning report’s recommended identity (not a catch-all power+AI encyclopedia).
- Product type can resemble PBDL (computational textbook); **TOC logic does not** — PBDL climbs method-coupling tightness; SciML_PS organizes by engineering questions.

---

## What stays outside the core (unless promoted later)

Do not promote these to equal pillars in the first offerings:

- Markets, load forecasting, optimal power flow  
- Protection coordination  
- Full voltage-stability or small-signal as co-equal spines  
- Reinforcement-learning control as a main TOC spine  
- Multimachine / converters as *third organizing axes* (prefer depth **inside** 400/500/600, stages in the planning report, or later numbered inserts)

Put emerging or thin topics in `700_advanced`, electives, or short “fast forward” subsections — not a fourth equal spine.

---

## When width is allowed later

Add a **new major part** (for example `350_…`, `550_…`, `800_…`) only when **all** hold:

1. Foundations + at least one pillar + labs actually run for students.  
2. The topic needs its **own** learning goals and labs, not a chapter under 400/500/600.  
3. You can name a clear engineering question in the same style as the three pillars.  
4. Portable teaching content exists (public citations; **no** sealed research metrics).

Until then: deepen `300` and labs 1–5; grow one pillar at a time; use `700_advanced` for overflow.

---

## Practical horizons

| Horizon | Action |
|---------|--------|
| Now – first offering | Stick to three pillars; fill `300` + labs 1–5; deepen one pillar at a time |
| Next few years | Insert numbered parts only for true new questions (e.g. network DAEs, measurement contracts) |
| Later | Optional fourth pillar only if a new question becomes central (e.g. control with learned models) — not before |

---

## Do not casually undo

- Do not rename the book around markets/OPF/forecasting as co-equal cores.  
- Do not split into Course I/II folder trees; use `100_front/learning_paths.md` for semester packaging.  
- Do not paste research-repo campaign numbers into student pages when “widening” examples.

Related:

- [Using, previewing, editing, and long-term development](using_preview_edit_and_long_term_development.md) §5  
- [Future plans for the online resource](future_plans_online_resource.md) (PDF, portal, feedback — not science-scope changes)
