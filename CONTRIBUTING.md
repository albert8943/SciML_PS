# Contributing to SciML for PS

Thank you for helping improve these living teaching notes. This repository is **under active development** (public preview, version 0.x until the first stable edition).

Student-facing summary: [Join and contribute](book/100_front/contribute.md).  
Governance and roles: [GOVERNANCE.md](GOVERNANCE.md).  
Code of conduct: [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).  
Positioning among neighbors: [book/100_front/related_resources.md](book/100_front/related_resources.md).

## Ways to help

| Contribution | How to start |
|--------------|--------------|
| Typo, broken link, unclear page | [Feedback](book/100_front/feedback.md) or a GitHub issue |
| Small content or lab fix | Pull request with DCO sign-off (below) |
| New chapter or major rewrite | Open a **chapter proposal** issue first |
| Section editor / long-term role | Open a collaboration interest issue or Discussion |

## Developer Certificate of Origin (DCO)

Every commit in a pull request must be **signed off**. By signing off, you certify that you have the right to submit the work and that it may be licensed under this repository’s licenses:

- **Book content** (`book/`, `slides/`, `media/`, generated site and PDF): [CC BY-NC-SA 4.0](LICENSES/CC-BY-NC-SA-4.0.txt)
- **Code** (`src/sciml_ps/`, `scripts/`, `tests/`, `templates/`, notebook code cells): [MIT](LICENSES/MIT.txt)

Inbound licence = outbound licence. Contributions are licensed under those same terms.

```bash
git commit -s -m "Your message"
```

Git adds a `Signed-off-by:` line matching your committer name and email. Unsigned commits will fail the DCO check.

Full DCO text: https://developercertificate.org/

## Content policy (required)

1. **Published sources only** — cite public literature; no sealed research metrics, seed tables, or unpublished campaign results on student pages.
2. **Own words and figures** — do not paste third-party course text (especially ND-licensed notes). Link and reimplement patterns.
3. **Teaching voice** — “we/you” or impersonal prose; not CV or paper-promo copy.
4. **Accessibility** — every figure needs `:alt:` text; do not encode meaning only in colour (see `book/chapter_template.md`).
5. **Scope** — keep Dynamics / Stability / Identification as the core; scope changes follow [docs/guides/scope_lock_three_pillars.md](docs/guides/scope_lock_three_pillars.md) and editor review.
6. **Maturity label** — every chapter carries a `{note} Maturity: Stub` (or Draft / In review / Stable) block near the top.

## Adding a reference

All sources live in one shared bibliography, [`references.bib`](references.bib). Each chapter cites what it uses and gets its own **References** list at the bottom of the page automatically; do not write a References heading by hand.

1. Search `references.bib` first; reuse an existing key rather than adding a duplicate.
2. New entry: key `firstauthorYEARword` in lower case (e.g. `raissi2019physics`). Take metadata from the DOI (`https://doi.org/<doi>` with header `Accept: application/x-bibtex`) or the publisher page, never from memory. Every entry needs `doi` or `url`.
3. Cite in the chapter with `[@key]` (parenthetical) or `@key` (in a sentence); several at once: `[@a; @b]`.
4. Link to a specific chapter of a web book inline, next to the citation.

## Adding a chapter

1. Copy [`book/chapter_template.md`](book/chapter_template.md) and keep its section order.
2. Add the page to the `toc` in `myst.yml`.
3. Add one row for it to the [Full outline](book/100_front/outline.md) (title link, one-line summary, maturity, lab).
4. Set the maturity note at the top of the page.
5. Run `python scripts/check_book.py`; CI runs it on every pull request.

## Local preview and build

```powershell
conda activate sciml_ps
.\scripts\preview.ps1          # http://localhost:3000/
```

Maintainer handbook: [docs/guides/using_preview_edit_and_long_term_development.md](docs/guides/using_preview_edit_and_long_term_development.md).

CI builds HTML (and PDF when possible) on every pull request to `master`.

## Pull request checklist

- [ ] Commits are signed off (`git commit -s`)
- [ ] Sources cited; no confidential data
- [ ] Figures have alt text
- [ ] TOC in `myst.yml` and the Full outline updated if you added a page
- [ ] New sources added to `references.bib` and cited with `[@key]`
- [ ] `python scripts/check_book.py` passes
- [ ] Local preview builds without broken links you introduced

## Credit

We use [All Contributors](https://allcontributors.org/) conventions. See [CONTRIBUTORS.md](CONTRIBUTORS.md). Section editors are also listed in governance and citation metadata when appointed.
