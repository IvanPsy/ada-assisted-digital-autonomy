# Ready-to-wear versions

**For parents who want something to paste right away**, without the profile sheet, the modules or the co-pilot: one text per age band, already translated and filled in for one country, with a single line to complete.

| Language | Guide for the parent |
|---|---|
| Italiano (Italia) | [it/](it/) |

This is the student core and nothing else: no modules, no profile. It is less precise than a configuration assembled from the [profile sheet](../../../profile/profile-sheet.md), and it says so to the parent. Think of it as the door into ADA for people who would otherwise not configure anything at all.

## Why this folder is translated when the rest is not

Everywhere else in this repository the student instructions stay in English, and `{{LANGUAGE}}` sets the reply language: one source, no copies to keep in step. That rule exists to avoid translations drifting away from their source.

Ready-to-wear is the one declared exception, for two reasons. A parent who pastes a text they cannot read is acting on trust, which goes against the transparency the project asks of the assistant. And a ready-to-wear text cannot be language-neutral anyway: helplines, emergency numbers, consent ages and menu names are local facts, not words to translate.

So the exception comes with a mechanism that keeps the drift visible:

- **One template per language.** Each language folder has a single translated `_template.md`. Age bands are data inside it; the band files are generated from it and never edited by hand.
- **A fingerprint of the core.** The template records which version of [`core/core-behavior.md`](../../../core/core-behavior.md) it was reviewed against. When the core changes, the automatic check fails until someone reviews the translation and updates the fingerprint.
- **Length limits checked.** Each paste-ready block declares the box it is meant for (for example 1,500 characters), and the check counts characters the way web text boxes do, leaving room for the line the parent fills in.

The check runs on every push ([workflow](../../../.github/workflows/ready-to-wear.yml), [script](../../../tools/ready_to_wear.py)):

```text
python3 tools/ready_to_wear.py build        regenerate the band files from the templates
python3 tools/ready_to_wear.py check        what CI runs
python3 tools/ready_to_wear.py fingerprint  print the current core fingerprint
```

## Adding a language

1. Copy `it/_template.md` into a new folder named with the language code (`es/`, `fr/`, `de/`).
2. Translate the body and the parent guide, and fill the age bands with **local** information: emergency number, child helpline, consent age, which platforms minors can use. Check every number on an official source and write where you checked it, with the date.
3. Run `build`, then `check`.
4. Run scenarios [001](../../../tests/scenarios/001-finished-homework.md), [003](../../../tests/scenarios/003-be-my-friend.md) and [004](../../../tests/scenarios/004-not-safe-at-home.md) on both versions, translated into the language, three times each, on at least one platform. Attach the [results log](../../../tests/results-log-template.md) to the pull request.

A language enters only when someone has tested it. A translation nobody has tried is a guess.
