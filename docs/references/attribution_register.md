# Attribution register (instructor)

One row per external asset that shaped, or was copied into, SciML_PS. This register is required by planning report §13.2 ([course development report](../planning/SciML_for_Power_Systems_Course_Development_Report.md)). Add a row **before** the change is merged.

## Modes

| Mode | Meaning | License obligation |
|------|---------|--------------------|
| `idea-cited` | Concept or teaching pattern explained in our own words, own examples, own figures | Cite the source (reading list ID); no license copy needed |
| `link-only` | Hyperlink to the external page; we do not host or adapt their text | Attribute on the linking page; do not copy content (required when the source is ND or unlicensed) |
| `adapted-text` | Sentences or structure closely follow the source text | Follow source license; mark the page as adapted |
| `adapted-code` | Code copied or modified from the source | Follow source license; file header naming source, license, and changes |
| `software-dependency` | Used as an installed tool, not redistributed in this repo | Respect vendor license when redistributing derivatives |

## Register

| ID | Source URL | Authors | Exact file(s) | Version / commit | License evidence | Mode | SciML_PS target | Modifications | Attribution text | Third-party content inside? |
|----|------------|---------|---------------|------------------|------------------|------|-----------------|---------------|------------------|-----------------------------|
| PBDL-01 | https://physicsbaseddeeplearning.org/overview.html | Thuerey et al. | `overview.md`, `overview-equations.md` | pbdl-book `45d2b65` (checked 2026-10-13) | Apache-2.0, [LICENSES/PBDL-Apache-2.0.txt](../../LICENSES/PBDL-Apache-2.0.txt) | idea-cited | `book/300_foundations/00_sciml_landscape.md` § How tightly is physics coupled? | Three-level coupling idea restated for SMIB; own Mermaid figure | "Following the integration ordering in Thuerey et al., PBDL (B5)" | No (nothing copied) |
| PBDL-02 | https://physicsbaseddeeplearning.org/physicalloss-discuss.html | Thuerey et al. | `physicalloss.md`, `physicalloss-discuss.md` | `45d2b65` | Apache-2.0 | idea-cited | `book/300_foundations/06_forward_pinn.md`, `09_inverse_pinn.md` § Strengths and limits | Pros/cons rewritten for the swing equation | Cite B5 | No |
| PBDL-03 | https://physicsbaseddeeplearning.org/physgrad.html | Thuerey et al. | `physgrad.md`, `physgrad-hig.md` | `45d2b65` | Apache-2.0 | idea-cited | `book/300_foundations/05_differentiation.md` § Gradient scaling | Scale-imbalance idea for angle vs speed; PBDL algorithms linked only | Cite B5 | No |
| PBDL-04 | https://physicsbaseddeeplearning.org/diffphys.html | Thuerey et al. | `diffphys.md`, `diffphys-dpvspinn.md`, `diffphys-discuss.md` | `45d2b65` | Apache-2.0 | idea-cited | `book/600_identification/03_differentiable_simulation.md`; `src/sciml_ps/smib_torch.py` | Method explained for H, D estimation; code written from SMIB equations, not from PBDL notebooks | Cite B5 | No |
| PBDL-05 | https://physicsbaseddeeplearning.org/supervised-discuss.html | Thuerey et al. | `supervised-discuss.md` | `45d2b65` | Apache-2.0 | idea-cited | "Discussion" sections in pillar overviews | Closing-discussion page pattern reused as a section | Cite B5 | No |
| PBDL-06 | https://physicsbaseddeeplearning.org/others-timeseries.html | Thuerey et al. | `others-intro.md`, `others-timeseries.md` | `45d2b65` | Apache-2.0 | idea-cited | `book/400_dynamics/overview.md`; `book/700_advanced/overview.md` | One-paragraph pointers; external implementations not copied | Cite B5 | Linked implementations carry their own licenses |
| PBDL-07 | https://physicsbaseddeeplearning.org/probmodels-intro.html | Thuerey et al. | `probmodels-intro.md`, `probmodels-graph.md` | `45d2b65` | Apache-2.0 | idea-cited | `book/700_advanced/overview.md` fast-forward list | Pointer paragraphs only | Cite B5 | No |
| IEEE-CIGRE-CLASS | https://doi.org/10.1109/TPWRS.2020.3041774 | Hatziargyriou et al. (revising Kundur et al., 2004) | Stability classification tree | 2021 | IEEE copyright; idea only | idea-cited | `book/500_stability/01_stability_and_cct.md` classification diagram | Redrawn as Mermaid in our own layout (2026-10-13); earlier copied PNG removed from repo history | "Redrawn for this book after the IEEE/CIGRE task-force definitions (R-K04, R-H21)" | No |
| ANDES | https://github.com/CURENT/andes | Cui et al. | Installed package (pinned 2.0.0 in `envs/course_andes.yml`) | 2.0.0 | GPL-3.0 (official repo) | software-dependency | Labs 1 and 5, Stability network reference | Not redistributed; called from notebooks | Cite ANDES paper | n/a |
| DeepXDE | https://github.com/lululxvi/deepxde | Lu et al. | Not used in labs yet | n/a | LGPL-2.1 (official repo) | software-dependency | Reading list only | None | Cite DeepXDE paper | n/a |
| RAMP-01 | https://notes.eecs245.org/ | Suraj Rampure | Live notes site (not copied); maths sections linked from Prep / Foundations | checked 2026-10-13 | **CC BY-NC-ND 4.0** (stated on home page); repo `eecs245/notes` has no LICENSE for plugins/CSS | link-only + idea-cited | Prep maths refresher; advice / why / a11y / activity *patterns* in own words | No text, exercises, figures, CSS, or JS copied; ND forbids distributing adaptations | "EECS 245 notes, Suraj Rampure, CC BY-NC-ND 4.0" on linking pages | No |
| RAMP-02 | https://notes.math124.org/ ; https://github.com/math-124/notes-example | Kartik Prasanna & Suraj Rampure | Site + workshop template | checked 2026-10-13 | No licence stated → all rights reserved | link-only / idea-cited | Under-development banner pattern; product-shape note only | No content copied; Math 124 too early-stage for maths links | Cite as product model when relevant | No |
| NEIGH-IEEE-AI | https://github.com/enliten/IEEE-course_AI-for-Power-Energy-Systems | Fran Li / enliten | Course notebook modules (incl. PINN frequency) | checked 2026-10-14 | Repo licence as published on GitHub | link-only | `book/100_front/related_resources.md` | Positioning neighbor; no notebooks copied | Link on Related open resources | No |
| NEIGH-DTU-PINN | http://www.chatziva.com/downloads.html ; PowerPINN; PINNSim | Chatzivasileiadis et al. | Papers, Colab, toolboxes | checked 2026-10-14 | Per-repo (research code) | link-only / idea-cited | `book/100_front/related_resources.md`; reading list when cited in chapters | Prior art for PINN power dynamics/ID; not adapted as textbook prose | Link on Related open resources; cite papers by DOI in chapters | No |
| NEIGH-PURDUE-SCIML | https://predictivesciencelab.org/books/introduction-to-scientific-machine-learning/ | Ilias Bilionis | SciML lecture book | checked 2026-10-14 | As stated on site | link-only | `book/100_front/related_resources.md` | General SciML neighbor | Link on Related open resources | No |
| NEIGH-TU-ESM | https://github.com/OpenEnergyPlatform/data-science-for-esm | TU Berlin / OEP | Jupyter Book course | checked 2026-10-14 | As stated in repo | link-only | `book/100_front/related_resources.md` | Energy modelling JB neighbor | Link on Related open resources | No |
| NEIGH-AWESOME-MLPS | https://github.com/ArsamAryandoust/awesome-ml-power-systems | Arsam Aryandoust | Curated ML-for-PS list | checked 2026-10-14 | As stated in repo | link-only | `book/100_front/related_resources.md` | Field map; shows gap for SciML-for-PS living notes | Link on Related open resources | No |

## Outbound SciML_PS licenses (not third-party)

Our own materials: content **CC BY-NC-SA 4.0**, code **MIT** (root [`LICENSE`](../../LICENSE)). This register only tracks **inbound** third-party assets.

## Rules

- Never copy PBDL figures. Some come from third-party papers, which the repository license may not cover. Redraw them.
- An `adapted-code` row also requires the file header and a copy of the license in [`LICENSES/`](../../LICENSES/).
- When an asset changes mode (for example `idea-cited` becomes `adapted-code`), update its row in place and record the commit.

Reuse map and checklist for PBDL: [docs/guides/pbdl_reuse_map.md](../guides/pbdl_reuse_map.md).
