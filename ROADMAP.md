# Roadmap — SciML for PS

Public milestones for the living notes. Detail for maintainers also lives in
[docs/guides/future_plans_online_resource.md](docs/guides/future_plans_online_resource.md)
and the lab spine policy.

**Current stage:** public preview (**v0.x**). Under development until v1.0.

## v0.1 — First public preview

- [ ] Repository public; site live at https://sciml4ps.albertpoulose.com (run `.\scripts\phase2_go_public.ps1` after `gh auth login`; DNS CNAME still manual)
- [x] Dual licence (CC BY-NC-SA 4.0 content / MIT code)
- [x] Collaboration scaffolding (CONTRIBUTING, DCO, GOVERNANCE, CoC)
- [x] Related-resources / positioning page (honest niche claim)
- [x] Site-wide under-development warning + maturity labels
- [x] Personal website Teaching link to the book (`dr-albert-poulose` open_resources + news)
- [ ] Zenodo DOI on first GitHub Release (`.\scripts\phase2_set_doi.ps1` after deposit)

## v0.2 — Foundations and Lab 1 usable

- [ ] Early Foundations chapters beyond stubs
- [ ] Lab 1 (reference SMIB) runnable end-to-end
- [ ] Preparation notebooks filled enough for a diagnostic

## v0.3 — Identification and Lab 3

- [ ] Identification pillar core chapters drafted
- [ ] Lab 3 (inertia/damping ID) runnable
- [ ] Classical baselines beside SciML methods on the same plant

## v0.4 — Stability and Lab 5

- [ ] Stability chapters (CCT, surrogates) drafted
- [ ] Lab 5 path clear (ANDES pin documented)
- [ ] Optional Google Form feedback URL

## v0.5 — Dynamics depth and Lab 2 / 4

- [ ] Dynamics pillar thickened
- [ ] Labs 2 and 4 past stub maturity
- [ ] Colab/Binder launch buttons for selected notebooks (optional)

## v1.0 — First stable edition

Criteria (see [GOVERNANCE.md](GOVERNANCE.md)):

- Foundations, Labs 1 / 3 / 5, and each pillar’s core chapters marked **Stable**
- At least one outside expert review per pillar (or documented equivalent)
- Accessibility pass on figures and navigation
- Site-wide “under development” warning may be removed; per-page labels stay
- Education paper / JOSE-style note optional but encouraged

## Later (post-v1.0)

- Course portal per offering (`portal/`)
- Section editors appointed; possible move to a GitHub organization
- Executable notebooks in CI; yearly minor releases + DOI
- Translations, print edition (with contributor consent where needed), grants

## Non-goals for the core book

- Dumping sealed research campaign metrics onto student pages
- Replacing ANDES documentation
- Method-only TOC (PINN → Neural ODE → …) without engineering applications
