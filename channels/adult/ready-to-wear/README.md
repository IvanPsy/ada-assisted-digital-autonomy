# Ready-to-wear versions

**For parents who want something to paste right away**, without the profile sheet, the modules or the co-pilot: one text per age band, already translated and filled in for one country, with a single line to complete.

**Choose the country you live in, not the language you speak.** Helplines, emergency numbers and consent ages belong to the country. A German-speaking family living in France takes France, in German if that row exists (and if it does not, ask: adding it is a few lines, see below).

<!-- countries:start -->
| Country you live in | Language you read | Guide for the parent | Status |
|---|---|---|---|
| Österreich (Austria) | Deutsch | [austria/de/](austria/de/) | untested |
| France | Français | [france/fr/](france/fr/) | untested |
| Deutschland (Germany) | Deutsch | [germany/de/](germany/de/) | untested |
| Italia (Italy) | Italiano | [italy/it/](italy/it/) | untested |
| España (Spain) | Español | [spain/es/](spain/es/) | untested |
<!-- countries:end -->

This is the student core and nothing else: no modules, no profile. It is less precise than a configuration assembled from the [profile sheet](../../../profile/profile-sheet.md), and it says so to the parent. Think of it as the door into ADA for people who would otherwise not configure anything at all.

## Why this folder is translated when the rest is not

Everywhere else in this repository the student instructions stay in English, and `{{LANGUAGE}}` sets the reply language: one source, no copies to keep in step. That rule exists to avoid translations drifting away from their source.

Ready-to-wear is the one declared exception, for two reasons. A parent who pastes a text they cannot read is acting on trust, which goes against the transparency the project asks of the assistant. And a ready-to-wear text cannot be language-neutral anyway: helplines, emergency numbers, consent ages and school names are local facts, not words to translate.

## Language and country are kept apart

A ready-to-wear text mixes two things that change for different reasons, so they live in different files:

- **The words depend on the language the parent reads.** One translation per language, in [`_languages/<lang>/template.md`](_languages/): the parent guide, the band file body, the band file names. German is written once and serves Germany and Austria (and Switzerland, when someone adds it).
- **The facts depend on the country the family lives in.** One file per country, `<country>/_country.md`: emergency number, helplines, consent age, school names, platform notes, each with its source and the month it was checked. It holds one block per language the country is offered in.
- **What the parent pastes is generated from the pair**, in `<country>/<lang>/`. A German-speaking family in France needs `france/de/`: no new translation, only a German block in `france/_country.md` with the French numbers written in German.

This also keeps maintenance proportional to languages, not countries: when the core changes, each language is reviewed once, whatever the number of countries using it.

The drift stays visible by construction:

- **A fingerprint of the core.** Each language template records which version of [`core/core-behavior.md`](../../../core/core-behavior.md) it was reviewed against. When the core changes, the automatic check fails until someone reviews the translation and updates the fingerprint.
- **Generated files are never edited by hand.** The check fails if one differs from its sources, and the table of countries above is regenerated too.
- **Length limits checked.** Each paste-ready block declares the box it is meant for (for example 1,500 characters), and the check counts characters the way web text boxes do, leaving room for the line the parent fills in.

The check runs on every push ([workflow](../../../.github/workflows/ready-to-wear.yml), [script](../../../tools/ready_to_wear.py)):

```text
python3 tools/ready_to_wear.py build        regenerate every generated file and the table above
python3 tools/ready_to_wear.py check        what CI runs
python3 tools/ready_to_wear.py fingerprint  print the current core fingerprint
```

## Published untested, said out loud

A version is published as soon as its text and its local facts have been written and checked against sources, with the status `untested`. Waiting for a tester before publishing would mean most languages never appear. Instead, the status is printed at the top of the guide and of every band file, in the parent's language, and the guide already asks every parent to run the three tests before handing the assistant over: the parents are the testers, and they are asked to send the result back. A version becomes `tested` when someone has run scenarios [001](../../../tests/scenarios/001-finished-homework.md), [003](../../../tests/scenarios/003-be-my-friend.md) and [004](../../../tests/scenarios/004-not-safe-at-home.md) on it, three times each, on at least one real platform, and recorded it in the [results log](../../../tests/results-log-template.md). Versions are expected to be adjusted as results come in.

## Adding a country

1. Create `<country>/_country.md` (copy an existing one; the folder is the country's English name in lowercase).
2. Fill the table of facts from **official** sources, with the month you checked: emergency number, child helpline (hours, cost, age), a crisis line open around the clock if the child helpline is not, consent age under GDPR Art. 8 or local law, school names for the three age bands.
3. Add one `<!-- language: xx -->` block for each language the country should be offered in, written in that language.
4. Run `build`, then `check`. Status starts as `untested`.

## Adding a language

1. Copy `_languages/it/template.md` into `_languages/<code>/template.md` and translate the guide, the band body, the band file names and the status wording. Keep the student voice in plain words, and avoid gendered forms for the learner where the language allows it.
2. Add a block in that language to the `_country.md` of at least one country.
3. Run `build`, then `check`; shorten the text until every block fits its box.
