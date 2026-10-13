# Naming and titles (SciML for PS)

**Audience:** Maintainers.  
**Status:** Locked for the online notes and PDF export.

Use these forms consistently. Do not invent alternate short names (e.g. “SciML-PS notes”) in student chrome.

## Canonical forms

| Form | Text | Use |
|------|------|-----|
| **Full title** | Scientific Machine Learning (SciML) for Power Systems (PS) | Homepage H1, `myst.yml` `project.title`, PDF cover main title (from export), README H1 |
| **Short brand** | SciML for PS | Navbar `logo_text`, sidebar footer, PDF cover **eyebrow** (teal line), prose after first introduction |
| **Focus subtitle** | Focus — dynamic modeling, stability assessment, and system identification | Homepage frontmatter `subtitle`; PDF cover line under the main title |
| **Three applications** (long labels) | SciML for dynamic modeling and simulation; SciML for stability assessment; SciML for parameter estimation and system identification | Homepage table, foundations/pillar framing (from the course planning report) |
| **Pillar nicknames** | Dynamics · Stability · Identification | Sidebar part titles, book map, in-body cross-links |
| **Repo / package** | `SciML_PS` / `sciml_ps` | Git folder, Python package, env name — not student-facing brand copy |

## Where each form is wired

| Surface | File / setting |
|---------|----------------|
| Project title (feeds PDF `\@title`) | [`myst.yml`](../../myst.yml) → `project.title` |
| Navbar short brand | [`myst.yml`](../../myst.yml) → `site.options.logo_text` |
| Homepage H1 + focus subtitle | [`book/index.md`](../../book/index.md) |
| PDF cover eyebrow + focus line | [`templates/sciml_ps_book/template.tex`](../../templates/sciml_ps_book/template.tex) `\maketitle` |
| Site footer | [`book/_site/site_footer.md`](../../book/_site/site_footer.md) |
| Sidebar TOC footer | [`book/_site/primary_sidebar_footer.md`](../../book/_site/primary_sidebar_footer.md) |

## Rules of thumb

1. **Brand stays broad** — SciML for PS. Specificity lives in the focus subtitle and the three-application table, not in a longer navbar string.
2. **Introduce short form once** on the homepage, then prefer **SciML for PS** in later prose.
3. **Student chrome uses public section names only** — see § Student chrome vs repo paths below.
4. After changing titles, rebuild the PDF (`scripts/build_pdf.ps1`) so `exports/sciml_ps_notes.pdf` matches the site.

## Student chrome vs repo paths

**Audience split:** `book/` pages are what students read. Spaced folder IDs (`300_foundations`, `900_labs`, …) are **maintainer packaging** so new parts can be inserted without renumbering neighbors. They belong in git paths, `myst.yml`, and `docs/guides/` — not in student-facing tables or suggested-order lists.

| Surface | Show students | Keep for maintainers |
|---------|---------------|----------------------|
| Book map, overviews, how-to-use | **Preparation**, **Foundations**, **Dynamics**, **Stability**, **Identification**, **Laboratories** | Folder IDs (`400_dynamics`, …) |
| Cross-links | Link text = page/section title | Relative Markdown paths in source (invisible in HTML) |
| Labs index | Lab number + titled topic + status | Raw `lab_01_…` as a table “Folder” column |
| Feedback | Browser URL + page title | Repo file paths as the primary ask |
| Author / vault provenance | Omit or one soft sentence | `docs/guides/vault_import_map.md`, planning report |
| TOC / sidebar titles | Human names | Directory names on disk |

**Do**

- Prefer two-column maps: pillar/section + engineering question (and optional titled links).
- Point “next step” with sidebar vocabulary: “see Laboratories → Lab 3”.
- Document 100-spacing and insert recipes only in the [maintainer handbook](using_preview_edit_and_long_term_development.md) §5.

**Do not**

- Add a **Folder** column on student pages.
- Write suggested order as `` (`300_foundations`) `` or “Part `400`”.
- Put “Content sources (authors)” / Obsidian lesson IDs on student overviews.
- Teach students the 100-spacing scheme on the book map (they only need the sidebar titles).

When inserting a new major part: create the folder, wire `myst.yml`, and add a **named** row to [`book/100_front/book_map.md`](../../book/100_front/book_map.md) — never advertise the raw folder ID as the public label.

## Anti-patterns

| Avoid | Prefer |
|-------|--------|
| Navbar “Made with MyST” | `logo_text: SciML for PS` |
| PDF eyebrow “SciML for Power Systems” | `SciML for PS` |
| PDF subtitle only “Course notes” | Focus — dynamic modeling, stability assessment, and system identification |
| Full title without (SciML)/(PS) on home/PDF | Full expanded form with parentheticals |
| Renaming the book to list all three applications | Keep brand; keep focus subtitle |
| Table column **Folder** with `` `500_stability` `` | Pillar name + question (link the overview) |
| Feedback ask for `book/300_foundations/….md` | Page title + browser URL |
| Book map explaining `300_foundations` packaging | Sidebar section names only |

## Related

- Scope of the three applications: [`scope_lock_three_pillars.md`](scope_lock_three_pillars.md)
- PDF build / cover provenance: [`site_hosting.md`](site_hosting.md)
- Long-term part inserts (100-spacing): [`using_preview_edit_and_long_term_development.md`](using_preview_edit_and_long_term_development.md) §5
- Vault → foundations provenance: [`vault_import_map.md`](vault_import_map.md)
