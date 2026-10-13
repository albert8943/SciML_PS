# ANDES content strategy (SciML for PS)

**Audience:** Maintainers.  
**Status:** Locked teaching product rule (2026-10-13).  
**Aligned with:** course planning report §6.1 / §13; [scope lock](scope_lock_three_pillars.md); [lab spine](lab_spine_policy.md).

ANDES ([docs.andes.app](https://docs.andes.app/en/stable/)) is the **optional network / TSA reference toolchain**. SciML_PS is **not** an ANDES textbook. Student page: [`book/500_stability/03_andes_network_reference.md`](../../book/500_stability/03_andes_network_reference.md).

---

## Pedagogical pattern: summarize, then link out

| In SciML_PS (short) | At docs.andes.app (detail) |
|---------------------|----------------------------|
| 1–3 sentences: what the tool step does for *this* SciML lab | Full tutorial (install, PFlow, TDS, plotting, …) |
| Minimal recipe (load → run → extract channels you need) | Complete API / CLI / config reference |
| Named teaching case + event intent | Case formats, model equations, custom modeling |
| Honesty / SciML framing (labels, CCT, version pin) | Verification, gallery deep-dives |

**Rules**

- Course voice only — do not paste ANDES chapter prose into `book/`.
- Every summary that needs depth ends with an explicit official link.
- Cap ~half page or one tip/note box per topic; if it becomes a tutorial, cut and link.
- Do not re-derive the ANDES symbolic-numeric framework in the book ([Modeling guide](https://docs.andes.app/en/stable/modeling/index.html)).

**License:** ANDES is **GPL v3**. Install and call it from labs; cite and link docs; short paraphrases + links are fine. Do not republish large tutorial or derivation text. Keep book prose license separate from the software license (planning report §13).

---

## SMIB first vs large systems

| Stage | System | Role |
|-------|--------|------|
| A | Classical **SMIB** | Foundations + assessed Labs 1–5 |
| B | WSCC 9-bus (optional lighter alternate) | Network depth if Kundur is too heavy |
| C | **Kundur two-area** (preferred class network case) | Post–Lab 5 Stability path via ANDES |
| D–E | Converter / larger network | Electives, Advanced, projects |

SMIB is the **teaching plant** for SciML methods. Networks come **after** SMIB CCT works. Do not delay all SciML until “full large-system foundations” are done. Do not require both 9-bus and Kundur.

---

## Preferred network case

| Field | Value |
|-------|--------|
| Case | `andes.get_case("kundur/kundur_full.xlsx")` |
| Gallery | [Critical Clearing Time Mapping](https://docs.andes.app/en/stable/gallery/critical-clearing-time.html) |
| Env | [`envs/course_andes.yml`](../../envs/course_andes.yml) — pinned **`andes==2.0.0`** (run `andes prep` once after install) |
| Notebook | [`lab05_network_cct_andes.ipynb`](../../book/900_labs/lab_05_stability_cct/lab05_network_cct_andes.ipynb) |
| Helper | [`src/sciml_ps/andes_cct.py`](../../src/sciml_ps/andes_cct.py) |
| Assessed spine | Still Labs 1–5 only; Kundur is an **optional Lab 5 network extension**, not Lab 6 |

---

## Gallery → book story map

Index: [ANDES Gallery](https://docs.andes.app/en/stable/gallery/index.html).

| Gallery | SciML_PS role |
|---------|----------------|
| [CCT Mapping (Kundur)](https://docs.andes.app/en/stable/gallery/critical-clearing-time.html) | **Primary network path** after SMIB Lab 5 |
| [PINN surrogate (SMIB)](https://docs.andes.app/en/stable/gallery/pinn-surrogate.html) | Further practice after Labs 1–2 — do not replace them |
| [Low-inertia IEEE 14](https://docs.andes.app/en/stable/gallery/low-inertia-freq.html) | Project / Advanced link |
| [Forced oscillation WECC 179](https://docs.andes.app/en/stable/gallery/forced-oscillation.html) | Elective / project only |
| [RL damping SMIB](https://docs.andes.app/en/stable/gallery/smib-oscillation.html) | Out of core (scope lock); Advanced curiosity link only |

**Incorporation checklist:** name the pillar → ≤½ page hook → deep link → course deliverable only if SciML metrics are yours → never mirror the gallery ToC in the sidebar.

---

## Tutorials: link-out map

Students self-study ANDES **01–06**, then return to SciML_PS. Tutorials **07+**, Modeling, Verification, and Reference stay outbound ([tutorials index](https://docs.andes.app/en/stable/tutorials/index.html)).

---

## Explicit non-goals

- Cloning ANDES docs into the book sidebar  
- Core chapters that re-derive ANDES models  
- Promoting frequency / FO / RL galleries to equal pillars  
- Growing beyond five assessed labs to “add ANDES”  

---

## Implementation inventory (2026-10-13)

What landed in the **online book** under this strategy (commits `a546034`, `aaadda5`). Canonical detail stays here so future agents do not re-audit git blindly.

### New student pages / artifacts

| Item | Path |
|------|------|
| ANDES bridge chapter | [`book/500_stability/03_andes_network_reference.md`](../../book/500_stability/03_andes_network_reference.md) |
| Optional Lab 5 network notebook | [`book/900_labs/lab_05_stability_cct/lab05_network_cct_andes.ipynb`](../../book/900_labs/lab_05_stability_cct/lab05_network_cct_andes.ipynb) |
| Helper | [`src/sciml_ps/andes_cct.py`](../../src/sciml_ps/andes_cct.py) |
| Env pin | [`envs/course_andes.yml`](../../envs/course_andes.yml) (`andes==2.0.0`) |

### Existing book pages updated (hooks only)

| Part | File | Change |
|------|------|--------|
| Front | [`book/100_front/how_to_use.md`](../../book/100_front/how_to_use.md) | ANDES env + bridge link |
| Front | [`book/100_front/book_map.md`](../../book/100_front/book_map.md) | Stability row mentions ANDES bridge |
| Foundations | [`book/300_foundations/06_forward_pinn.md`](../../book/300_foundations/06_forward_pinn.md) | Optional PINN gallery link |
| Dynamics | [`book/400_dynamics/overview.md`](../../book/400_dynamics/overview.md) | Further-practice gallery links |
| Stability | [`book/500_stability/overview.md`](../../book/500_stability/overview.md) | Learning path step → ANDES page |
| Advanced | [`book/700_advanced/overview.md`](../../book/700_advanced/overview.md) | FO / RL gallery links |
| Lab 2 | [`book/900_labs/lab_02_surrogate_vs_pinn/index.md`](../../book/900_labs/lab_02_surrogate_vs_pinn/index.md) | Further-practice note |
| Lab 5 | [`book/900_labs/lab_05_stability_cct/index.md`](../../book/900_labs/lab_05_stability_cct/index.md) | Network extension section |
| Labs index | [`book/900_labs/README.md`](../../book/900_labs/README.md) | Lab 5 status + notebook link |
| Reference | [`book/990_reference/reading_list.md`](../../book/990_reference/reading_list.md) | S1 / S1a ANDES + gallery |

TOC: `myst.yml` lists `03_andes_network_reference.md` under Stability.

### Not rewritten

Most Foundations chapters (`01`–`05`, `07`–`10`), Identification pages, Prep, and Stability `01_stability_and_cct` / `02_surrogate_stability` **bodies** were left as-is (only overview/hooks above).

### Story in one line

SMIB SciML first → short ANDES bridge in Stability → optional Kundur CCT notebook → detailed tutorials/gallery stay on [docs.andes.app](https://docs.andes.app/en/stable/).

Session journal: [`cursor_sessions/2026-10-13_andes_content_strategy.md`](cursor_sessions/2026-10-13_andes_content_strategy.md).

Related: [lab spine](lab_spine_policy.md), [naming / student chrome](naming_and_titles.md), [using_preview handbook](using_preview_edit_and_long_term_development.md) §2.4.
