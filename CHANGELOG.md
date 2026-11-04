# Changelog

## Unreleased

- New: **ready-to-wear versions** (`channels/adult/ready-to-wear/`) for parents who want something to paste without the profile sheet: the core only, translated and pre-filled by age band, with one line to complete and a short and a full version for the size of the box. First language: Italian (11-13, 14-16, 17-19), with a parent guide and three tests to run before use. Tried in simulation on scenarios 001, 003 and 004; not yet run on ChatGPT or Gemini.
- The one declared exception to "instructions stay in English": each language has a single template, the band files are generated from it, and `tools/ready_to_wear.py` (run on every push by the `ready-to-wear` workflow) fails when the core changes after the translation was reviewed, when a generated file is edited by hand, or when a block no longer fits its box.
- New module: **asking for help** (signature A for the prompts, required human third party), derived from an activity designed in Italian support teaching. The chatbot is a training ground for asking; every session ends with a question taken to a person. Not yet tried with a learner.
- Three new test scenarios for it (010, 011, 012), one of which tests its main risk, substitution.
- New placeholder `{{PEOPLE_TO_ASK}}` in the profile sheet and the assembly template.
- How to install: states that the instructions do not need translating, the `{{LANGUAGE}}` field sets the reply language.

## 0.1.0 (September 2026)

First public structure, derived from the Italian ADA framework (v1.1, July 2026) and its operational kits.

- Core behavior for the student channel, full and compact versions.
- Four functional modules: planning and sequencing (signature A), text access (signature B), predictable interaction (open), social practice role-play (A, learner-paced).
- Adult co-pilot with four templates: assembling student instructions, accessible text, task card, weekly check-in.
- Profile sheet with signatures per function, and a fictional example showing two signatures in one learner.
- Nine test scenarios (five core, four module-specific) with a manual testing protocol.
- Documentation: concepts, platform compatibility (checked September 2026), installation, study agreement, safety, style guide, contributing.

Known gaps: one test scenario per module instead of two; no module yet for working memory, numeracy, emotional regulation during study, AAC users or intellectual disability; no automated evaluation.

Nothing in this release has been validated in the field yet.
