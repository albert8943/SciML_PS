# Book map

Part IDs use 100-spacing so new pillars can be inserted later (for example `350_…` between foundations and dynamics).

| Part | Folder | Role |
|------|--------|------|
| 100 | `100_front` | How to use, local preview commands, map, learning paths |
| 200 | `200_prep` | Prerequisites and diagnostic |
| 300 | `300_foundations` | SMIB + core SciML methods |
| 400 | `400_dynamics` | Deeper dynamic modeling / surrogates |
| 500 | `500_stability` | TSA labels, CCT, surrogate stability |
| 600 | `600_identification` | Identifiability, measurements, PE depth |
| 700 | `700_advanced` | Operator learning, UQ, multimachine |
| 900 | `900_labs` | Assessed laboratories 1–5 |
| 990 | `990_reference` | Reading list, notation |

## Parallel growth

After foundations stubs exist, `400` / `500` / `600` can grow independently. Labs cross-link from chapters.

## Scope lock (maintainers)

The three application pillars are the intentional core. Wider topics belong in `700_advanced` or future 100-spaced inserts only after promotion criteria are met. Full decision note (git repo, not a student chapter): `docs/guides/scope_lock_three_pillars.md`.

## Future product features (maintainers)

PDF export is wired (navbar **PDF**, `scripts/build_pdf.*`, experimental LaTeX skin). Still planned: public hosting, Google Form feedback, and a separate course portal (notes vs course site, like EECS 245 / Math 124). One living book across terms; portals per offering — not a new book site each semester. Roadmap: `docs/guides/future_plans_online_resource.md`. Pattern note: `docs/references/rampure_notes_vs_course_sites.md`.
