# Website / career → SciML for PS book

**Audience:** Maintainers.  
**Status:** Locked alignment for decades-long book growth.  
**Writable:** `SciML_PS` only.  
**Read-only sources:** personal site repo `dr-albert-poulose` ([albertpoulose.com](https://albertpoulose.com/)); Obsidian career notes (do not write vault unless authorized).

---

## Decision

Keep the book **application-led** (Dynamics / Stability / Identification). Use the website’s three research programmes as a **content source**, not as a second TOC.

| Website / career programme | Book home | Rule |
|----------------------------|-----------|------|
| 01 Modern grid stability | `500_stability` (+ later Advanced elective) | Teach criteria and CCT; no campaign metrics |
| 02 Scientific AI for grid dynamics | Foundations + Dynamics + Identification + Stability surrogates | Multi-method; not a PINN-branded book |
| 03 Grid digital twins | `700_advanced` synthesis only | “Building toward,” not claimed results |
| Personal site (CV / Teaching) | Author line; Teaching link **later** when book URL is public | Book is notes, not a CV mirror |

Career identity (vault): **physics-structured dynamic security** — surrogates and criteria that plug into real simulation — not “I am the PINN person.”

---

## Hugo file map (adapt, do not dump)

Most website copy lives in config/data; Research Notes body is layouts (see site `CONTENT-GUIDE.md`).

| Website asset | Path under `dr-albert-poulose` | Book destination |
|---------------|--------------------------------|------------------|
| Dynamic security definition | `config/_default/hugo.toml` → `researchDefinition` | `book/500_stability/01_stability_and_cct.md` |
| IEEE/CIGRE placement + three TSA cases | `layouts/partials/research-stability-context.html` + related params | Same chapter |
| Classification / cases figures | `static/images/research/*.png` | `media/figures/` (cite IEEE papers, not “from my website”) |
| Classifier vs trajectory story | Pillar 02 + `layouts/partials/research-fig-02.html` | `book/500_stability/02_surrogate_stability.md` |
| Energy / direct methods | `data/research_pillars.yaml` programme 01 | `book/500_stability/04_direct_methods.md` (classical SMIB first) |
| Twin loop | Programme 03 pipeline | `book/700_advanced/01_assessment_to_decision.md` |
| PINN-TSA software card | `data/software.yaml` | Reading list Further reading only — never a Lab |
| Teaching courses YAML | `data/teaching.yaml` | **Not** SciML chapter source (Numerical Analysis / Logic Circuits, etc.) |

**Voice:** rewrite in teaching “we/you” or impersonal prose. Do not paste first-person research promo, abstracts, or Access metrics into student pages.

**Citation hygiene:** use Hatziargyriou (full spelling) with DOI `10.1109/TPWRS.2020.3041774` (R-H21).

---

## Phase 3 deferrals (after Labs 1 / 3 / 5 runnable)

- Converter elective under Advanced (VSM–swing bridge first; GFL/PLL later)
- Synchronizing-torque index as optional multimachine depth
- When SciML_PS has a **public URL**: add a Teaching card on the **website** (`teaching.yaml`) pointing at the book — separate website PR; do not block book prose on that
- Portal / Google Form — [`future_plans_online_resource.md`](future_plans_online_resource.md)

---

## Explicit non-goals

- Renaming book parts to website programme titles  
- Editing `dr-albert-poulose` from SciML_PS content sprints by default  
- Listing research GitHubs as assessed labs  
- Importing non-SciML syllabi into Preparation  

---

## Related

- [`toc_architecture_decades.md`](toc_architecture_decades.md)  
- [`scope_lock_three_pillars.md`](scope_lock_three_pillars.md)  
- [`lab_spine_policy.md`](lab_spine_policy.md)  
- [`naming_and_titles.md`](naming_and_titles.md)  
