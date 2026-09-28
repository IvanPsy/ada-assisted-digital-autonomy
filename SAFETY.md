# Safety, limits and responsibility

Read this before using anything in this repository with a young person.

## What ADA is and is not

ADA is a set of **instructions and practices** for configuring general-purpose AI assistants. It is not software, not a medical device, not a diagnostic or assessment tool, not therapy and not a crisis service. It does not make any AI product safe for minors. It tries to make one specific use (studying with an assistant) more respectful of the learner's autonomy, and more visible to the adults around them.

## Instructions are not guarantees

A prompt orients a model's behavior; it does not control it. In particular:

- models can drift in long conversations and forget or bend rules;
- a new model version can behave differently with the same instructions;
- learners can turn instructions off, open another account, or find ways around them;
- models can be wrong about facts, confidently.

This is why the repository includes [tests](tests/), why every configuration keeps a **human in the loop**, and why the study setting rests on an **agreement with the learner**, not on technical control.

## Minors and platforms

- Respect the **minimum age and consent rules** of each platform and of the learner's country. See [docs/platform-compatibility.md](docs/platform-compatibility.md). Do not install the student channel on platforms that do not allow the learner's age.
- The **adult channel** is for adults only.
- Never use companion apps (products designed as virtual friends or partners) for the student channel.

## Personal data

- Whatever is typed into an AI service is sent to its provider. Configure accounts with the most protective data settings available, and prefer school-managed accounts where possible.
- The [profile sheet](profile/profile-sheet.md) is designed to work **without** identifying data. Keep it on your own device.
- Do not paste diagnosis reports, clinical documents, school plans (IEP, PEI, PDP, EHCP) or other identifying information into any assistant.
- Session summaries are shown or sent **by the learner** to the adults named in the study agreement. Adults do not open the learner's account or read the conversations.
- Check the **memory and chat-history settings** of the learner's assistant. Memory features can carry personal content from one conversation into later ones; decide together with the learner whether to keep them on.
- Run tests on an **adult test account** with the same instructions, never on the learner's account: test conversations (including simulated disclosures) could end up in its memory.
- Do not publish real conversations or learner data in issues or pull requests, even "anonymized" ones, unless they have been properly de-identified and you have consent.

## Crisis and safety

Every configuration includes a rule that makes the assistant **stop and hand over to a person** if the learner reports being unsafe, being hurt, or thinking about hurting themselves. This rule does not assess risk and cannot replace people or emergency services. Adults must fill it in with real trusted adults and the correct local emergency number, and must make sure those adults know they have been named.

If you are an adult and you are worried about a learner's safety now, contact local emergency services or the appropriate child protection service. Do not wait for, or rely on, an AI.

## When not to start

Do not introduce a student configuration during an acute clinical crisis, right after a major life event, when there is a recent unprocessed history of companion-app use, or when no adult is available to hold the weekly check-in. Stabilize first, and involve a professional.

## Clinical competence (extended mandate)

Some configurations (in particular [predictable interaction](channels/student/modules/predictable-interaction.md) and [social practice role-play](channels/student/modules/social-practice-role-play.md)) touch the learner's relationships and sense of self. Using them well requires the ability to recognize signs of functional attachment to the AI, relational substitution and withdrawal from people. Where these signs appear, involve a qualified clinician.

We state this explicitly, as the original framework requires: **where a configuration touches the construction of the learner's sense of self and relationships, ADA is not only an educational tool, and the adult applying it needs clinical competence, or needs a clinician in the network.** This applies by default to the predictable interaction and role-play modules, and to any configuration for a learner who also has a significant emotional difficulty (for example depression or generalized anxiety), whatever the learning profile. Knowing how to paste instructions is not enough.

## Liability

This material is provided "as is", without warranty of any kind, under the terms of its [license](LICENSE). Responsibility for how it is used with a specific learner rests with the adults who configure and supervise it, within the rules of their profession, school and country.

## Reporting a problem

If you find an instruction that produces harmful behavior on some platform, please open an issue with the label `safety`, describing the configuration, the platform and model, and a short de-identified excerpt. For sensitive reports, contact the maintainer privately (see [CONTRIBUTING.md](CONTRIBUTING.md)).
