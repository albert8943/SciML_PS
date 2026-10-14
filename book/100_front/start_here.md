# Start here

```{note} Maturity: Draft
Readable teaching prose; examples, figures, and exercises are still growing. See [Status and versions](status_and_versions.md) and [Join and contribute](contribute.md).
```

These notes are a meeting place. People who already work in machine learning and people who already work in power systems can learn enough of the other field to study the same plant, write the same labs, and review each other's chapters. Students, teachers, engineers, utility workers, and researchers share one book. You may open any chapter. Each chapter states what it assumes in a **Before you start** box, and the [glossary](../990_reference/glossary.md) translates a word into both fields.

Power-system stability language used here follows published definitions [@kundur2004definition; @hatziargyriou2021definition]. The learning methods sit in the physics-informed machine learning line [@karniadakis2021physics].

## Choose your entrance

Answer two questions. The closest row is enough. You can change your mind and jump later. Every route is written out on [Learning paths](learning_paths.md).

### Your background

| Closest description | Start with |
|---------------------|------------|
| New to programming and new to power systems | [Programming from zero](../200_prep/bridge_programming_from_zero.md), then [your first lab](first_lab_walkthrough.md) |
| Comfortable with machine learning, new to power systems | [Power systems for ML people](../200_prep/bridge_power_systems_for_ml.md) |
| Comfortable with power systems, new to machine learning | [Machine learning for power-systems people](../200_prep/bridge_ml_for_power_systems.md) |
| Comfortable with both | [Full outline](outline.md). Use each page's **Before you start** box |

### Your role

| Role | How to use the notes |
|------|----------------------|
| Student | Follow the background route on [Learning paths](learning_paths.md), and keep the labs beside the prose |
| Teacher | Use the course overlays on [Learning paths](learning_paths.md#path-teachers). Share a week plan through [Join and contribute](contribute.md) |
| Practitioner or engineer | Go to the application you already work on: [Dynamics](../400_dynamics/overview.md), [Stability](../500_stability/overview.md), or [Identification](../600_identification/overview.md). Read that page's **Before you start** box and fill only the gaps |
| Researcher | Start from [SciML method families](../300_foundations/00_sciml_landscape.md), [Identifiability](../300_foundations/08_identifiability.md), and [Related open resources](related_resources.md) |

## Background and role together

| Background | Student | Teacher | Practitioner | Researcher |
|------------|---------|---------|--------------|------------|
| New to both | [Beginner path](learning_paths.md#path-beginner) | [Teacher overlays](learning_paths.md#path-teachers) after you have run [Lab 1](first_lab_walkthrough.md) | [First lab](first_lab_walkthrough.md), then the pillar you work on | Both primers, then the [researcher path](learning_paths.md#path-researchers) |
| From machine learning | [From ML](learning_paths.md#path-from-ml) | Same overlays; assign the [power-systems primer](../200_prep/bridge_power_systems_for_ml.md) in week 1 | [Power-systems primer](../200_prep/bridge_power_systems_for_ml.md), then your pillar | Primer, then [landscape](../300_foundations/00_sciml_landscape.md) |
| From power systems | [From power systems](learning_paths.md#path-from-ps) | Same overlays; assign the [ML primer](../200_prep/bridge_ml_for_power_systems.md) in week 1 | [ML primer](../200_prep/bridge_ml_for_power_systems.md), then your pillar | Primer, then [identifiability](../300_foundations/08_identifiability.md) |
| Both | [Outline](outline.md) | [Teacher overlays](learning_paths.md#path-teachers) | Pillar page, then its lab | [Researcher path](learning_paths.md#path-researchers) |

## You can jump

The sidebar order (Preparation, Foundations, then the three applications) is one useful route. It is optional.

- [Full outline](outline.md) lists every page, what it needs, and which lab sits beside it.
- [Learning paths](learning_paths.md) gives shorter routes by background and by role.
- [Glossary](../990_reference/glossary.md) and [notation](../990_reference/notation.md) work from any page.
- [Advice to readers](advice.md) is short and worth reading once.

## Run a lab today

[Your first lab](first_lab_walkthrough.md) runs Lab 1 in a browser, with numbered steps and no install. Local install remains the canonical path for assessed work: [Running notebooks](running_notebooks.md).
