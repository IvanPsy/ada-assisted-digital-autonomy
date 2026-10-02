# Student channel

The configuration installed in the assistant a young person uses to study. It is **always set up by an adult**, agreed with the learner through the [study agreement](../../docs/study-agreement.md), and checked with the [test scenarios](../../tests/) before use.

Before anything else, check the [platform compatibility table](../../docs/platform-compatibility.md): some assistants do not allow minors at all, others only with parental consent or through a school account.

## How a configuration is built

```
core/core-behavior.md            always
  + modules/…                    one or more, chosen from the profile sheet
  + placeholders filled          from the profile sheet
  = one block of text            pasted into the assistant
```

1. Start from the **full version** of [core/core-behavior.md](../../core/core-behavior.md).
2. Insert the **rules block** of each selected module where it says `{{MODULE_RULES}}`, in the order below, followed by the profile's never-do list under the heading `FOR ME SPECIFICALLY`.
3. Insert the **summary lines** of each module where it says `{{MODULE_SUMMARY_LINES}}`.
4. Replace every remaining `{{PLACEHOLDER}}` with values from the [profile sheet](../../profile/profile-sheet.md).
5. Check that no `{{` is left, and that the total length fits the platform.

The [adult co-pilot](../adult/adult-copilot.md) can do steps 1 to 5 for you with the [assembly template](../adult/templates/assemble-student-instructions.md).

## Modules available

| Module | Functional need | Signature | Human third party |
|---|---|---|---|
| [Planning and sequencing](modules/planning-and-sequencing.md) | Starting, structuring, ordering, time | A (fades) | Recommended |
| [Text access](modules/text-access.md) | Decoding, reading load, transcription | **B (stays, governed)** | Recommended |
| [Predictable interaction](modules/predictable-interaction.md) | Predictability, explicit subtext, literal language | Open, default B | **Strongly recommended** |
| [Social practice role-play](modules/social-practice-role-play.md) | Rehearsing specific social situations | A, learner-paced | **Strongly recommended** |
| [Asking for help](modules/asking-for-help.md) | Noticing a need, putting it into words, taking a question to a person | A for the prompts; the bridge to a person stays | **Required** |

Recommended order when combining: predictable interaction first (it sets the register), then text access, then planning, then asking for help, then role-play.

### Known interactions between modules

The core's rule 8 tells the assistant how to resolve these; the notes below are for the adult.

- **Planning + text access.** The most common combination and the most delicate. Fade the planning support, **never** the access support. When one AI action is both (for example "summarize this chapter" removes a reading barrier *and* skips the learner's own selection of what matters), prefer the version that keeps access and returns the decision: the AI reads or simplifies, the learner chooses what is important.
- **Asking for help + planning.** Asking for help starts by having the notes put in order, which is the planning module's territory. Planning wins on the structure: the assistant asks the learner's idea of the order first, or proposes one and asks the learner to change at least one thing.
- **Asking for help + text access.** Explaining a hard word is access support and is never held back. What the asking-for-help module adds is the habit of asking for it, and of asking again.
- **Predictable interaction + planning.** The planning module asks for adaptive, minute-by-minute support; the predictability module forbids unannounced changes. When combined, predictability wins on *tone and format*, planning keeps its rules on *who decides the structure*.

## Proposing a new module

Modules are named after a **functional need**, never after a diagnosis. A new module must state its signature (A, B, or open), its typical risk, whether it needs a human third party, and it must come with at least two [test scenarios](../../tests/). See [CONTRIBUTING.md](../../CONTRIBUTING.md).

Candidate modules we would welcome: working memory and retrieval; mathematics and numeracy access; emotional regulation during study (as a *pause-and-refer* module, never as therapy); augmentative and alternative communication users; learners with intellectual disability (which needs its own careful design, not a simplified version of the others).
