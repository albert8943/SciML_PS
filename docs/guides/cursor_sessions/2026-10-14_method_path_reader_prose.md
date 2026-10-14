# 2026-10-14 — Method path visible to readers

## Intent

Surface the locked teaching strategy on student pages: applications first; PINN as an early core SciML path (not the whole book); other families under Labs 3–5 / Advanced; keep five labs and deepen them.

## Pages touched

| Page | Change |
|------|--------|
| `book/index.md` | Why this book: PINN early path + links to landscape and Labs |
| `book/100_front/how_to_use.md` | Section **How SciML methods appear** |
| `book/100_front/advice.md` | ML / power-systems honesty bullets |
| `book/300_foundations/00_sciml_landscape.md` | **Reader path** important box |
| `book/300_foundations/overview.md` | Foundations vs pillars vs Lab 4 paragraph |
| `book/900_labs/README.md` | Method-placement table; Lab 2 link text |
| `book/900_labs/lab_02_surrogate_vs_pinn/index.md` | Soft H1 + **Why this lab names PINN** (slug unchanged) |
| `book/100_front/outline.md` | Lab 2 display title |
| `book/100_front/book_map.md` | Methods / five-lab sentence |
| `book/100_front/contribute.md` | Collaborator cue: deepen Labs 1–5, not Lab 6 |
| `CHANGELOG.md` | Unreleased Changed entry |

## Checks

- `python scripts/check_book.py` after the edit.

## Not done here

Lab 2 / Lab 4 executable notebooks; PDF rebuild.
