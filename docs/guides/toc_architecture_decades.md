# TOC architecture for decades of continuous development

**Audience:** Maintainers.  
**Status:** Locked product architecture for the SciML for PS notes book.  
**Recorded:** 2026-10-13 (sidebar / section-structure decision).

Student-facing map (named sections only): [`book/100_front/book_map.md`](../../book/100_front/book_map.md).  
Folder IDs and insert bands: [`using_preview_edit_and_long_term_development.md`](using_preview_edit_and_long_term_development.md) §5.

---

## Decision

Keep the **application-led** top-level sections (sidebar / `myst.yml` TOC):

1. Front matter  
2. Preparation  
3. Foundations  
4. Dynamics  
5. Stability  
6. Identification  
7. Advanced topics  
8. Laboratories  
9. Reference  

This skeleton is **appropriate for a long-lived online resource**. Continuous development should deepen pages *under* these parts, not redesign the sidebar every year.

---

## Why this survives decades

| Section | Long-term job |
|---------|----------------|
| Front matter | How to use the *product* (changes rarely) |
| Preparation | Skills gate (NumPy, ODEs, nets, gradients — **not** ANDES; see below) |
| Foundations | Stable SMIB + SciML core (edit carefully; high reuse) |
| Dynamics / Stability / Identification | Grow **in parallel** as teaching and research deepen |
| Advanced topics | Filter / parking lot for thin or early ideas before promotion |
| Laboratories | Assessed spine (fixed count — see [`lab_spine_policy.md`](lab_spine_policy.md)) |
| Reference | Citations and tools (swap without rewriting the TOC) |

Stronger for longevity than a TOC that lists every paper topic or every method as a top-level part.

---

## Rules to protect (do not casually undo)

1. **Three pillars remain the core** — do not add Markets / OPF / RL (etc.) as equal siblings without meeting [`scope_lock_three_pillars.md`](scope_lock_three_pillars.md).  
2. **Laboratories stay a peer of the notes**, not buried under one pillar (labs span dynamics / identification / stability).  
3. **Advanced is a filter**, not a junk drawer that silently becomes a fourth pillar.  
4. **Folder IDs with gaps** (`300`, `400`, insert `350` later) are maintainer packaging; students see **names**, not numbers.  
5. **One living book** + term portals / learning paths later — do not fork a new notes site every semester ([`rampure_notes_vs_course_sites.md`](../references/rampure_notes_vs_course_sites.md)).

---

## Alternatives considered

| Pattern | Idea | Verdict for SciML for PS |
|---------|------|---------------------------|
| **Current (prep → foundations → 3 apps → advanced → labs → ref)** | Application-led | **Default — keep** |
| Method-led (PINN → Neural ODE → DeepONet → …) | Some SciML books | Ages poorly when methods churn; weaker for power engineers |
| Course-week TOC (Week 1…16) | Term packaging | Put in **learning paths / portal**, not the main TOC |
| Separate mini-books per pillar | Three sites | Harder to maintain; splits Foundations three ways |
| Flat “everything in Foundations” | One long spine | Unreadable once content grows |

---

## ANDES is not required Preparation

**Decision (2026-10-13):** Do **not** put an ANDES introduction in the main **Preparation** section.

| Layer | Role |
|-------|------|
| Preparation (`200_prep`) | Shared warm-up for Foundations and Labs 1–3: NumPy, ODE integration, small nets, gradients. Uses `envs/course_core.yml`. |
| Lab 1 | Transparent SMIB **without** ANDES (`sciml_ps.smib`). |
| ANDES | Just-in-time before Lab 5 / network chapters: short quickstart under Stability, Lab 5 brief, or a later *optional* prep notebook marked “Lab 5 only”. Separate pin: `envs/course_andes.yml`. |

**Why:** ANDES is heavier (install, GPL, version pins). Requiring it in Prep blocks students before they need it and muddies the programming diagnostic. Cite ANDES in [Reference — Reading list](../../book/990_reference/reading_list.md); teach it when a lab actually runs it.

---

## Practical “decades” rule

- **TOC titles stay stable** for years.  
- **Pages under each part grow** freely.  
- **New major parts** only when there is a new engineering question + labs (insert with 100-spacing).  
- **Semester packaging** lives in `learning_paths.md` / `portal/`, not by renaming these nine sections.  
- Invest continuous work in **Foundations depth** and **Labs 1 → 3 → 5**, then pillar chapters — not in annual sidebar redesigns.

---

## Related

- [`scope_lock_three_pillars.md`](scope_lock_three_pillars.md)  
- [`lab_spine_policy.md`](lab_spine_policy.md)  
- [`naming_and_titles.md`](naming_and_titles.md)  
- [`future_plans_online_resource.md`](future_plans_online_resource.md)  
