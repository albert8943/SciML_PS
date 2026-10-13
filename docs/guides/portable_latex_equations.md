# Portable LaTeX equations (authors)

**Audience:** Maintainers writing SciML_PS book pages and manuscripts.  
**Adapted from:** Obsidian method note *Portable LaTeX Equations Across Obsidian and Manuscripts* (vault `04-Methods/`).

## Purpose

Keep a single **equation body** in conventional LaTeX so the same mathematics moves between MyST/Obsidian Markdown and `.tex` manuscripts. Change only the **outer delimiters**.

## Procedure

1. Write the expression with standard LaTeX (`\frac`, `\dot`, `\mathrm`, Greek, sub/superscripts).  
2. In MyST / Obsidian `.md`:
   - Inline: `$...$`
   - Display: `$$...$$`
3. In `.tex` manuscripts, wrap the **same body**:
   - Inline: `\(...\)`
   - Display: `\[...\]` or `equation` + `\label`
4. Add numbering, `\label`, `\ref`, and journal formatting **only** in the manuscript.  
5. Avoid vault-only or course-only macros that MathJax / MyST may not define — prefer expanded conventional TeX in student pages.

## Delimiter table

| Context | Inline | Display |
|---------|--------|---------|
| Book / Obsidian `.md` | `$...$` | `$$...$$` |
| LaTeX `.tex` | `\(...\)` | `\[...\]` or `equation` |

## Teaching note for SciML_PS

Student-facing classical SMIB labs use $(H, D)$. If you paste converter equations from research notes, keep estimands labeled and do not mix GFM triad symbols into Lab 3 without an elective flag.

## See also

- [`vault_import_map.md`](vault_import_map.md)  
- Book [`990_reference/notation.md`](../../book/990_reference/notation.md)
