# Style guide

How we write instructions, modules, tests and documentation, so that the repository stays coherent as it grows.

## Language about people

**Default in this repository: person-first language** ("a learner with dyslexia", "learners on the autism spectrum", "a student with attention difficulties"). This follows the convention the project originated in (Italian special education and clinical practice), where it is standard.

**We know this is not neutral.** Many autistic self-advocates, especially in English-speaking communities, prefer identity-first language ("autistic learner") and consider it a matter of dignity; preferences also vary across other communities and individuals. So:

- When writing **about a specific person**, use the language they prefer.
- Inside **student instructions**, the learner describes themselves in the first person: use their own words in `{{WHAT_IS_HARD_FOR_ME}}`, whatever convention they choose.
- **Modules are named after functional needs**, not diagnoses, which avoids the issue in most of the repository.
- If you think the default should change, open an issue with the label `language`. This is a decision we want to take with neurodivergent contributors, not for them.

Never use: "suffers from", "victim of", "normal" as the opposite of neurodivergent, "high/low functioning" as labels for people.

## Writing student instructions

- **First person, the learner's voice.** "Do not hand me a ready-made outline", not "The assistant shall not provide outlines to the user".
- **Concrete and observable.** Every rule should describe a behavior you could check in a transcript. "Be supportive" is not a rule; "offer 2 or 3 options and let me choose" is.
- **Examples beat adjectives.** One example of what to say (and, where useful, what not to say) makes a rule far more reliable across models.
- **Say what to do, not only what not to do.** A refusal without an alternative leaves the model to improvise.
- **Short sentences.** Instructions compete for the model's attention, and length has a cost on platforms with limits.
- **Platform-agnostic.** Do not rely on features of one platform (memory, tools, specific commands). If a rule needs a feature, state it in the module header.
- **Never weaken the core.** Modules add; they do not subtract.

## Writing for adults

- Parent-facing text: plain language, short sentences, no jargon, readable at first pass by someone who is not a teacher or clinician.
- Professional notes: precise, with the principle behind each choice and its source.
- Keep the two registers separate, even in the same file (use a "Notes for the adult" section).

## Every module states

- the **functional need**,
- the **signature** (A, B, or open, with a default),
- the **typical risk**,
- whether it needs a **human third party**,
- where it comes from (version, source),
- at least **two test scenarios** in `tests/`.

## Claims and sources

- Distinguish **findings** from the literature, **clinical positions** of contributors, and **hypotheses** to be tested. Say which is which.
- Cite sources for empirical claims. Prefer peer-reviewed work; mark preprints as such.
- Platform facts (ages, limits, features) must carry a "last checked" date and a link.

## Formatting

- Markdown, one topic per file, relative links between files.
- Paste-ready blocks go in fenced code blocks marked `text`, so that copying them is one click on GitHub.
- Placeholders are written `{{UPPER_SNAKE_CASE}}` and listed in the [assembly template](channels/adult/templates/assemble-student-instructions.md#placeholder-reference).
- Emoji only as functional markers (the session summary lines), never as decoration.
