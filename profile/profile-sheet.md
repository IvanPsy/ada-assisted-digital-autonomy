# Profile sheet

The bridge between the two channels. **The adult fills it in, ideally together with the learner**, on their own computer. It describes what the learner *needs*, not who they are.

> ⚠️ **Privacy.** Whatever you paste into an AI service is sent to a company. Do not include surnames, school names, addresses, diagnosis reports, clinical history or anything you would not want stored by a third party. First names or roles for trusted adults are enough. Diagnoses are optional: functional needs are what matter here. In the EU, health-related data about a minor is a special category under the GDPR (Art. 9); treat it accordingly.

Copy this file, fill it in, keep it private.

---

## 1. Basics

- **Age band:** [e.g. 14-15]
- **School level:** [e.g. upper secondary]
- **Language for replies:** [...]
- **Platform the learner will use:** [see docs/platform-compatibility.md; check the age rules]
- **Account type:** [personal / school account / supervised account]

## 2. What is hard, in the learner's words

Ask the learner. Write one or two sentences in their words, in the first person. This becomes `{{WHAT_IS_HARD_FOR_ME}}`.

> [e.g. "Reading long texts tires me and I lose the thread. Starting homework is the hardest part."]

What helps, in their words (optional):

> [...]

## 3. Functional needs and their signature

For each need that applies, decide the signature **with** whoever knows the learner best (support teacher, clinician). The signature belongs to the function, not the diagnosis. In doubt, choose B.

| Functional need | Applies? | Signature: A (can mature, support fades) / B (does not mature, support stays governed) / unsure | Module |
|---|---|---|---|
| Getting started, planning, ordering steps, time | ☐ | ☐ A ☐ B ☐ unsure | planning-and-sequencing |
| Decoding text, reading load | ☐ | ☐ A ☒ **B (default)** ☐ unsure | text-access |
| Spelling, handwriting, transcription | ☐ | ☐ A ☒ **B (default)** ☐ unsure | text-access |
| Organizing an argument when writing | ☐ | ☐ A ☐ B ☐ unsure | planning-and-sequencing |
| Predictability, explicit rules, literal language | ☐ | ☐ A ☐ B ☐ unsure | predictable-interaction |
| Rehearsing specific social situations | ☐ | ☐ A ☐ B ☐ unsure | social-practice-role-play |
| Other: [...] | ☐ | ☐ A ☐ B ☐ unsure | (no module yet: open an issue) |

**What the signature changes.** The module text is the same either way. The signature changes how the adults read the summaries and whether support is ever reduced: under A, support is reduced step by step with the learner; under B, it is never reduced, and what you watch for is transparency, return to the original, refusal and voice. Decoding and transcription are pre-marked B: choose A only with a clinician's reasoning, because treating an access function as developmental is the most harmful mistake this framework knows.

Diagnosis, if you choose to note it (optional). **Delete this line before uploading the sheet to any assistant:** [...]

## 4. Module settings

- **Planning and sequencing:** suggest a break after `{{SESSION_BREAK_EXCHANGES}}` = [15] exchanges (the model cannot measure minutes). Current support level (1-4): [1]
- **Text access:** `{{TEXT_INTERVENTION_LEVEL}}` = ☐ read aloud and format only ☐ read aloud, format and reword lightly ☐ read aloud, format, reword and simplify in depth. Agreed with the learner? ☐
- **Social practice role-play:** `{{ROLEPLAY_EXCHANGES}}` = [10] exchanges per exercise

## 5. People and safety

- **Trusted adults** (roles or first names the learner actually trusts; ask them): `{{TRUSTED_ADULTS}}` = [e.g. "my mum or Mr. B., my support teacher"]. Do these people know they have been named? ☐
- **Local emergency number:** `{{EMERGENCY_NUMBER}}` = [e.g. 112 EU, 911 US/Canada, 999 UK]
- **Child helpline** (for when the trusted adults are not the right people): `{{CHILD_HELPLINE}}` = [e.g. 116 111 in many European countries; 19696 Telefono Azzurro in Italy; check your country]
- **Who holds the weekly check-in** (human third party): [name/role] · Cadence: [weekly]
- **Who else is in the network:** ☐ support teacher ☐ clinician ☐ other: [...]

## 6. Never-do list

Things the assistant must never do with this learner, beyond the core rules. Keep it short and concrete.

- [e.g. "Never use timers or countdowns: they cause anxiety."]
- [e.g. "Never refer to grades."]

These lines go at the end of `{{MODULE_RULES}}` under the heading `FOR ME SPECIFICALLY` (in the compact core, one or two of them go in `{{FOR_ME_SPECIFICALLY}}`).

## 7. Do not start yet if…

☐ there is an acute crisis (anxiety, depression, conduct) · ☐ a recent loss, separation or school change is still fresh · ☐ there is a recent, unprocessed history of companion-app use · ☐ no adult at all is available to hold the check-in

If any box is ticked, stabilize the context first and talk to a professional. Introducing a new tool during overload can make things worse.

## 8. Agreement

- Study agreement discussed with the learner on: [date]
- Trial period agreed: [e.g. 4 weeks], review on: [date]
- Test scenarios run on this configuration on: [date], results: [...]
