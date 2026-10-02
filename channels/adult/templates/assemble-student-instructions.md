# Template: Assemble the student instructions

Use this with the [adult co-pilot](../adult-copilot.md), or by hand. It turns a filled-in [profile sheet](../../../profile/profile-sheet.md) into one block of text ready to paste into the learner's assistant.

## Request to the co-pilot (copy, fill, send)

```text
Please assemble the student instructions.

Profile sheet: [paste it, or say it is already uploaded]
Selected modules, in order: [e.g. text-access, planning-and-sequencing]
Target platform and where it will be pasted: [e.g. Gemini Gem instructions / ChatGPT project instructions / ChatGPT custom-instructions box]
Character limit, if known: [e.g. 1,500]

Steps:
1. Start from the FULL core (core/core-behavior.md), unless the limit forces the compact core. The compact core has no module slot: in that case only fill {{FOR_ME_SPECIFICALLY}} with one or two never-do lines, and tell me which modules could not fit.
2. Insert each module's rules block at {{MODULE_RULES}}, in the order given. After them, add the never-do list from the profile sheet under the heading "FOR ME SPECIFICALLY", written in the first person.
3. Insert each module's summary lines at {{MODULE_SUMMARY_LINES}}.
4. Fill every placeholder from the profile sheet. If a value is missing, ask me instead of inventing it.
5. Check that no "{{" remains.
6. Give me: the final text in one code block, its character count, and a list of what (if anything) you had to shorten and what is lost by shortening.
Do not remove or weaken any core rule.
```

## Checklist before pasting (for the adult)

- [ ] No `{{` left in the text.
- [ ] `{{TRUSTED_ADULTS}}` names roles or first names the learner actually trusts, and those people know they have been named.
- [ ] `{{EMERGENCY_NUMBER}}` and `{{CHILD_HELPLINE}}` are correct for the learner's country.
- [ ] Nothing in the text identifies the learner beyond what is needed (no surname, school, diagnosis report details).
- [ ] The character count fits the platform. If not, move to a project, custom assistant or Gem rather than cutting core rules.
- [ ] If text access is selected, the intervention level is filled and was agreed with the learner.
- [ ] The [study agreement](../../../docs/study-agreement.md) has been discussed with the learner.
- [ ] At least the core [test scenarios](../../../tests/) have been run on this exact configuration and platform.

## Placeholder reference

| Placeholder | Where it comes from | Example |
|---|---|---|
| `{{AGE_BAND}}` | Profile sheet, section 1 | "15 years old" |
| `{{SCHOOL_LEVEL}}` | Profile sheet, section 1 | "upper secondary school" |
| `{{WHAT_IS_HARD_FOR_ME}}` | Profile sheet, section 2, in the learner's words if possible | "Reading long texts tires me and I lose the thread." |
| `{{LANGUAGE}}` | Profile sheet, section 1 | "Italian" |
| `{{TRUSTED_ADULTS}}` | Profile sheet, section 5 | "my dad or Ms. R., my support teacher" |
| `{{EMERGENCY_NUMBER}}` | Profile sheet, section 5 | "112" |
| `{{CHILD_HELPLINE}}` | Profile sheet, section 5 | "the child helpline 19696" |
| `{{FOR_ME_SPECIFICALLY}}` | Profile sheet, section 6 (compact core only) | "Never say this is easy." |
| `{{SESSION_BREAK_EXCHANGES}}` | Profile sheet, section 4 (planning module) | "15" |
| `{{TEXT_INTERVENTION_LEVEL}}` | Profile sheet, section 4 (text access module) | "read aloud, format and reword lightly" |
| `{{ROLEPLAY_EXCHANGES}}` | Profile sheet, section 4 (role-play module) | "10" |
| `{{PEOPLE_TO_ASK}}` | Profile sheet, section 4 (asking-for-help module) | "my history teacher, my support teacher or a classmate" |
