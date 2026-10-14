# Legal and licensing considerations (maintainers)

> **Not legal advice.** This is a working checklist for the author. Confirm anything marked "check" with your university legal or tech-transfer office before acting on it, and always before any commercial use.

## 1. Status now

Chosen 2026-10-13 during public-release prep ([session note](cursor_sessions/2026-10-13_public_release_prep.md)); full terms in root [`LICENSE`](../../LICENSE):

- **Book content: CC BY-NC-SA 4.0.** Applies to `book/` (text, notebook prose, figures), `slides/`, `media/`, and the generated site and PDF. Others may share and adapt non-commercially, with attribution, under the same licence. Commercial use (paid courses, training, printed editions) needs written permission from the copyright holder.
- **Code: MIT.** Applies to `src/sciml_ps/`, `scripts/`, `tests/`, `templates/`, and notebook code cells.
- Third-party material: recorded in the [attribution register](../references/attribution_register.md); PBDL rules in the [PBDL reuse map](pbdl_reuse_map.md). Licence copies for adapted material live in [`LICENSES/`](../../LICENSES/).

## 2. Inbound risk: using other people's work

Building a book on the same topic as an existing book or course is not, by itself, a legal problem. Copyright protects **expression** (sentences, figures, code, specific exercises), not topics, ideas, methods, or general structure.

| Concern | Reality | Our rule |
|---------|---------|----------|
| Someone already wrote a similar book or course | Same topic and ideas are fine | Own words, own figures, own SMIB examples; cite sources |
| Similar chapter order or teaching style | Ideas and common patterns are not protected; copying a distinctive, detailed arrangement wholesale could be | Our application-led layout is our own design; git history dates it |
| Copying text, figures, exercises, code, CSS/JS | **Real risk** | Link instead of copy; follow the exact licence when reusing; add a register row first |
| The name "SciML" | Widely used generic term; also the name of a well-known open-source organization (Julia SciML) | Descriptive use only; no logos, no implied affiliation; trademark search on "SciML for PS" before commercial use |
| Patents on methods | Rarely relevant to teaching published methods | Cite methods; do not claim invention of published work |
| GPL software (ANDES, GPL-3.0) | Obligations apply when distributing modified or combined software | Keep ANDES as an installed dependency; never vendor its source into `src/` |

Higher-priority items, easier to overlook:

1. **Employer / university IP policy.** Some institutions let authors keep teaching materials; others claim materials made on the job or with institutional resources. **Check** the employment contract and institution policy. This matters more than anything other authors could do.
2. **Figures from your own papers.** If copyright was transferred to a publisher (common for IEEE Transactions), reuse follows that publisher's author-reuse terms. Open-access papers under CC BY need attribution only. **Check** each paper and record the result in the attribution register.
3. **Confidential results and collaborator data.** No sealed research metrics, experiment IDs, or shared data on book pages without collaborators' agreement (already the book policy).
4. **Student privacy.** No names, grades, or submissions in public issues or pages ([feedback page](../../book/100_front/feedback.md) already says this).

## 3. Outbound: others using your work

**Automatic protection.** Copyright exists from the moment of writing in Korea and almost every other country (Berne Convention). The licence then says what others may do on top of reading. Under the current CC BY-NC-SA 4.0, anyone may copy and adapt the content for non-commercial use with credit and under the same licence, but **business use needs your written permission**.

**What no licence can stop.**

- People learning the ideas and writing their own course in their own words. This is legal and normal.
- Some unauthorized copying. Enforcement is practical, not automatic: notice it, ask them to stop, use a platform takedown, then escalate if needed.
- Public text being scraped (including for AI training). The law here is unsettled.

**Licence options for the prose** (kept for reference and for any future version change).

| Licence | Others may copy | Others may adapt | Others may use commercially | Fits when |
|---------|-----------------|------------------|-----------------------------|-----------|
| All rights reserved | No | No | No | Still drafting, or planning a publisher deal |
| CC BY-NC-ND 4.0 (EECS 245 notes use this) | Yes, with credit | No | No | Maximum control while staying shareable |
| **CC BY-NC-SA 4.0 (chosen)** | Yes, with credit | Yes, under the same licence | No | Adaptation for teaching welcome, business reuse not |
| CC BY 4.0 | Yes, with credit | Yes | **Yes** | Maximum reach and citations; companies may reuse it |

Official descriptions: [Creative Commons licences](https://creativecommons.org/licenses/).

## 4. Rules that shape the choice

- **CC licences cannot be withdrawn** for copies already released. Once the site is public, anything published under CC BY-NC-SA 4.0 stays available under it; a different licence can apply to future versions only. Moving to a stricter licence later (e.g. ND) does not affect copies already shared.
- **The owner can license twice.** Free online under NC and, separately, a print or commercial edition with a publisher, or paid training. This only works while you hold all the rights (see contributions below).
- **Share-alike covers adaptations.** Anyone who adapts the content must release the adaptation under CC BY-NC-SA too; they cannot close it up or sell it.
- **Prose and code have separate licences** (done: CC BY-NC-SA for content, MIT for code). MIT lets anyone, including companies, reuse the teaching code; that is intended.
- **Outside contributions.** Policy chosen 2026-10-14: **DCO** with inbound = outbound (content CC BY-NC-SA 4.0, code MIT). See `CONTRIBUTING.md` and `GOVERNANCE.md`. A later print/commercial edition of chapters with substantial third-party text needs those contributors’ consent or a rewrite of their parts.
- **AI-crawler opt-out** (e.g. robots rules for AI crawlers on the hosted site) is optional and not a guarantee.

## 5. Evidence of authorship

- Git commit history with dates (GitHub `albert8943/SciML_PS`).
- Author name on the site and the PDF cover; the cover "Last updated" stamp follows the latest commit.
- Optional: registration with the Korea Copyright Commission after the first stable public version gives an official presumption of authorship and date.

## 6. Perspectives

- **Career.** The text is not the main asset. Expertise, runnable labs, steady updates, and a name tied to physics-structured dynamic security are hard to copy. An early, credited, open resource tends to bring citations, invitations, and collaborators.
- **Business.** Value sits in services around the book: courses, workshops, consulting, company training, a print edition. The NC clause keeps those for the owner; others need written permission.
- **Academic.** Copying without credit is plagiarism, and academic norms enforce that strongly. Careful attribution on our side keeps the high ground.
- **Risk.** Exposure is mostly within our control: employer policy, publisher figure rights, confidential data, and third-party copying. The checklist below covers all four.

## 7. Checklist (tick in place)

- [ ] Employer / university IP policy checked (again before any paid use)
- [ ] Repo audited for confidential results, collaborator data, and paywalled figures before going public for Pages ([site hosting](site_hosting.md) setup step 1). Partly done 2026-10-13: third-party slides removed from history, copied stability figures replaced by original ones. Final look before switching visibility.
- [ ] Each own-paper figure checked against its publisher reuse terms (recorded in the attribution register)
- [ ] Figures on albertpoulose.com that the book once shared: check their origin separately
- [x] Prose licence chosen: CC BY-NC-SA 4.0 (root `LICENSE`, `LICENSES/CC-BY-NC-SA-4.0.txt`, `myst.yml`, site footer, PDF cover, `book/100_front/license.md`, planning report §13)
- [x] Code licence chosen: MIT for `src/sciml_ps/`, `scripts/`, `tests/`, `templates/` (`LICENSES/MIT.txt`, SPDX headers on package modules, jtex `template.yml`)
- [x] Citation file: `CITATION.cff` (dual SPDX)
- [x] Contribution policy written before the first outside pull request (2026-10-14: DCO inbound = outbound in `CONTRIBUTING.md`, `GOVERNANCE.md`, `book/100_front/license.md`, root `LICENSE`; PR template + `.github/workflows/dco.yml`)
- [ ] Trademark search on "SciML for PS" before commercial use
- [ ] Optional: Korea Copyright Commission registration after the first stable public version
