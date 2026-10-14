# Chapter title

<!-- Maturity: choose one admonition near the top (see status_and_versions.md). -->

````markdown
```{note} Maturity: Stub
Outline and goals only. Examples and labs will thicken later.
```
````

Other labels: **Draft** (readable prose, still growing), **In review** (awaiting editor/outside review), **Stable** (reviewed for the current edition; errata still welcome).

## Learning goals

- …

## Reading

<!-- Cite sources with [@key] (parenthetical) or @key (in a sentence); keys live in references.bib.
     Do not write a References heading: MyST adds one at the bottom of this page, listing only what it cites.
     New source? Add a bib entry with doi or url (see CONTRIBUTING.md, "Adding a reference"). -->

- What to read *before* this chapter, e.g. "Swing equations [@kundur2022power]".

## Watch

<!-- iframe or link placeholder -->

*Video placeholder.*

## Slides

- Slides: link a file from the repo `slides/` folder when available.

## Worked example

*To be written.*

## Activity (optional)

Use MyST built-in directives (do **not** copy third-party plugins):

````markdown
```{exercise} Short prompt
:label: ex-short-slug
:class: dropdown
Question in your own words.
```

```{solution} ex-short-slug
:class: dropdown
Solution sketch.
```
````

## Lab

- Link the relevant laboratory page (under Laboratories in the sidebar) when ready.

## Further reading

- Where to go *after* this chapter; do not repeat the Reading list. Deep links to a chapter of a web book stay inline, e.g. "[Physical losses](https://physicsbaseddeeplearning.org/physicalloss.html) in @thuerey2021pbdl".

## Common misconceptions

- …

## Accessibility checklist (authors)

- [ ] Every `{figure}` / image has `:alt:` text that describes the content, not “figure 1”
- [ ] Meaning is not carried by colour alone (use labels, linestyles, or markers)
- [ ] Important plots have a one-sentence caption in the surrounding prose
- [ ] Videos (when added) have captions or a transcript link

## Stub / under-development pages

If the chapter is still thin, put a maturity note near the top so readers are not surprised (prefer the labels above):

````markdown
```{note} Maturity: Stub
This section is under development. The learning goals and reading list are stable; examples and labs will thicken in later passes.
```
````
