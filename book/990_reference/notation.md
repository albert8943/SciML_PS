# Notation

Plain-language meanings, with a power-systems reading and a machine-learning reading of the same word, are in the [glossary](glossary.md). This page is the symbol table.

## Conventions (teaching draft)

| Symbol | Meaning |
|--------|---------|
| $\delta, \omega$ | Rotor angle, speed (classical SMIB) |
| $H, D$ | Inertia, damping (Lab 3 estimands) |
| $P_m, P_e$ | Mechanical / electrical power |
| $\theta$ | Generic parameter vector |
| $\hat{x}(t)$ | Network-predicted state |
| $\mathcal{L}_{\mathrm{data}}, \mathcal{L}_{\mathrm{phys}}$ | Data and physics losses |
| $\lambda_{\mathrm{phys}}$ | Physics loss weight |
| CCT | Critical clearing time |

## Rules

- Prefer **per-unit** classical SMIB in labs; document the base in the manifest.
- Tensor batches in code examples: `(batch, time, dim)` when tensors appear.
- Distinguish **physical** vs **equivalent/effective** parameters in prose.
- Converter GFM symbols $(M_v, D_v, m_p)$ appear only in electives with an explicit model map.

Equation authoring across MyST and manuscripts is documented for maintainers in the repository guides (portable LaTeX equations).
