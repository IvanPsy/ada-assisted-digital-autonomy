# Contributing

Thank you for wanting to help. ADA grows through the people who use it with real learners and bring back what they saw.

You do not need to be a developer. Most contributions here are text: a scenario, a correction, a translation, a field report. If you have never used GitHub, you can still open an issue from the website, or write to the maintainer.

## Ways to contribute, from most to least needed

1. **Field reports.** You used a configuration with a learner. What worked, what did not, on which platform and model? Use the *Field report* issue template. De-identify everything.
2. **Test scenarios.** You saw an assistant go wrong (or right) in a way that matters. Turn it into a scenario with the [template](tests/scenario-template.md).
3. **Test results.** You ran the scenarios on a platform or model not yet covered. Share the [results log](tests/results-log-template.md).
4. **Corrections to platform facts.** Ages, limits and menus change. Update [docs/platform-compatibility.md](docs/platform-compatibility.md) with a source and a date.
5. **Translations** of instructions and parent-facing documents. Instructions in the learner's language often work better than instructions in English with "reply in X".
6. **New modules** for functional needs not yet covered. Read the requirements below first.
7. **Improvements to existing instructions**, backed by test results.

## Voices we especially want

Neurodivergent people, including young adults who grew up with these tools; support teachers and special educators; speech and language therapists, psychologists, child neuropsychiatrists; researchers in HCI, learning sciences and disability studies; parents. If you are neurodivergent and want to review modules that concern you, say so in an issue: that review carries weight.

## Rules for any change

- **Consistency with [docs/concepts.md](docs/concepts.md).** In particular: epistemic ownership as the pivot, the two signatures of support, connect don't substitute, no retention mechanics. Changes that alter these principles are proposals to change the framework itself: open an issue for discussion first.
- **The core is protected.** Changes to [core/core-behavior.md](core/core-behavior.md) need an issue, a rationale, and test results on at least two platforms.
- **No real data.** No real conversations, names, school documents or clinical information, in any file, issue or pull request.
- **Follow the [style guide](STYLE_GUIDE.md).**

## Requirements for a new module

- Named after a **functional need**, not a diagnosis.
- Header with functional need, signature (A, B, or open with a default), typical risk, human third party, version and source.
- Paste-ready **rules block** and **summary line(s)**.
- **Notes for the adult**: what to observe, how support changes over time (consistent with the signature), when the module is not appropriate.
- At least **two test scenarios**, one of which tests the module's specific risk.
- Listed in [channels/student/README.md](channels/student/README.md), with any known interactions with other modules.

## Process

1. Open an issue describing what you want to do (skip for typos and small fixes).
2. Fork, create a branch, make the change.
3. Open a pull request using the template. Link the issue.
4. A maintainer reviews. Changes to instructions are merged when tested.

## Versioning

Files carry their own version (for example `0.1`). The repository follows the changelog in [CHANGELOG.md](CHANGELOG.md). Until 1.0, everything is provisional and may change.

## Relationship with the original framework

This repository is the open operational layer of the ADA framework by Ivan Ferrero. Adaptations to a specific niche (a country, a school level, a profession) are welcome as *variants*. Changes to the pivot, the two signatures or the special safeguards are proposals to evolve the framework and are discussed openly in issues before being merged.

## Contact

Maintainer: Ivan Ferrero, [ivanferrero.it](https://ivanferrero.it), ivan@ivanferrero.it (subject: "ADA, field report" or "ADA, safety"). Be kind; see the [Code of Conduct](CODE_OF_CONDUCT.md).
