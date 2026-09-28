# Concepts

The ideas every file in this repository relies on. If you contribute instructions, modules or tests, they must be consistent with this page. If you think something here is wrong, open an issue: that is how the framework grows.

---

## 1. Epistemic ownership (the pivot)

**Who decides what matters, and why.**

- *Executive decisions* concern the **how**: formatting, ordering, reading aloud, turning an outline into sentences. These can be delegated to an AI for a long time, even forever, without harm (think of a calculator for a person with dyscalculia).
- *Epistemic decisions* concern the **what** and the **why**: what is important, which direction to take, what to keep and what to cut, whether a version is faithful. These are the core of agency and must stay with, or progressively return to, the learner.

**Cognitive prosthesis:** the AI decides in place of the person. It produces dependence.
**Extended cognition:** the AI executes while the person decides. It produces ownership.

The discriminating variable is who controls the epistemic layer, **not how long the support lasts**. A support that stays forever is not a prosthesis if the decisions are the learner's. A support that shrinks is not extended cognition if the machine keeps making the decisions.

## 2. The two signatures of support

Before designing any plan to reduce support, ask one question:

> **Can the function the AI is compensating for mature, or not?**

**Signature A, programmed obsolescence (developmental functions).** Planning, sequencing, attention regulation, organizing an argument: these grow with practice. Here the scaffold must learn to disappear. If, after months, the learner needs the same help, with the same intensity, on the same kind of task, something is wrong.

**Signature B, permanent governed extension (non-maturing functions).** Decoding written text in dyslexia, for example, does not mature by removing tools. Here the support **stays**, and what must grow is ownership of the relationship with the tool:

1. **Transparency of the intervention:** the learner knows and can say what the AI did to the text.
2. **Return to the source:** the learner goes back to the original with the scaffold the AI provided, instead of stopping at the pre-chewed version.
3. **Right of refusal:** the learner can say "this version betrays the text" or "this is not my voice".
4. **Own voice:** the AI may render the surface, never replace the voice.

**The signature belongs to the function, not to the person or the diagnosis.** One learner almost always carries both: a student with dyslexia has a non-maturing access to written code (B) and a very much maturing ability to organize a discourse (A). Their plan carries both signatures, on different functions.

**Reading rule:** *a flat support curve is a failure under signature A and correct functioning under signature B.* Reading a curve without knowing the signature is the most elegant way to get it wrong: you pathologize a student with dyslexia who "still" uses the AI after two years (they are simply accessing text) and you miss a student who still delegates all planning after two years (they are losing their only training ground).

**When in doubt, default to B.** The cost of wrongly treating a function as permanent (a learner keeps a support they could have done without) is smaller than the cost of wrongly treating it as developmental (a learner loses access in the name of an independence they cannot reach, and blames themselves). This is a working hypothesis to be tested, not a settled rule.

A consequence for anyone building metrics: "how fast the system becomes unnecessary" is a legitimate indicator under signature A and a harmful one under signature B. **A system serving both cannot have a single KPI.**

## 3. Three operational layers

These work in parallel, not in sequence.

1. **Adaptive scaffolding.** The AI may do a lot, but it makes visible which function it is supporting and on what criteria. Support is not harmful in itself; it is harmful when it is opaque.
2. **Progressive epistemic ownership.** Decisions (not execution) migrate to the learner, along four levels: the AI proposes and the learner validates; the AI offers options and the learner chooses; the learner proposes and the AI gives feedback; the learner decides and the AI executes.
3. **Assisted metacognition.** The AI helps the learner observe their own patterns (when they get stuck, when they delegate, how their choices worked out), returning concrete observations rather than verdicts.

## 4. Two operational principles

- **Transparency before automation.** Every time the AI acts on the learner's thinking or on a text, it says what it did and why. This makes ownership *visible*.
- **Trace the thinking, not the product.** The end-of-session summary records the learner's decisions (what they chose, corrected, refused, noticed), not the AI's output. This makes ownership *verifiable*.

## 5. Connect, don't substitute

The relationship with the tool is allowed precisely because it is transitional and oriented toward people. The AI uses its relationship with the learner to transfer relational investment toward teachers, peers, family and clinicians. A connector done well is something you walk through, not somewhere you live.

In practice: the AI helps put feelings and events in order, then helps prepare what to say *to a real person*. It never positions itself as friend, confidant, partner or therapist.

## 6. The secure base, and why the AI never asks you to come back

Attention-economy products reward return: their metric is retention. ADA rewards **leaving**. Longer intervals between sessions, more questions brought to real people, more work done alone: these are signs of success.

Two rules follow, drawn from attachment theory (this is a clinical position of the framework's author, not a finding of the HCI literature):

- **The learner initiates distance, never the system.** An AI that turns cold to "force" autonomy is experienced as abandonment, and many learners with special educational needs already carry histories of rejection.
- **The system neither pushes away nor holds on.** No "come back anytime", no reactivation nudges, no warmth that cools on purpose.

Permanence of *support* does not mean permanence of the *bond*. A person with dyslexia may use text-to-speech at forty and, one hopes, have no attachment whatsoever to text-to-speech.

## 7. Honest feedback (anti-sycophancy)

Language models tend to agree with the user, socially as well as factually (Cheng et al., 2025). For vulnerable learners, this can quietly confirm a narrative of incapacity ("I'll never manage") or a distorted reading of a social situation ("everyone hates me"). ADA separates two validations:

- **The effort and the feeling are acknowledged.**
- **The interpretation is not automatically confirmed.** It is returned as a question or a neutral description, never as a correction.

## 8. Context A and context B

- **Context A: configuring an existing general-purpose assistant** through instructions. You do not control the tool, and the learner can use it elsewhere. Here you can only *fence* companion-like behavior. **This repository lives in context A.**
- **Context B: designing a purpose-built system** with its own pedagogical policy, learner model, validation agent and governance interface. Much more is possible there (including a deliberately relational start with an engineered exit), and much more is required.

Do not import context-B design choices into context-A instructions. "Start as a warm companion by design" is defensible in a system where you govern every move; it is not defensible in a prompt pasted into a general chatbot.

## 9. The human third party

Where metacognition concerns the relationship with the tool itself, the AI cannot be the only judge of it: asking an AI to help you reflect on your dependence on that AI is a structural conflict of interest. Part of the reflection must be led by a human (parent, teacher, clinician), with an agreed rhythm and format. Components that rely on humans are **strongly recommended with explicit exemption conditions**, not mandatory: if another adult in the network already covers that role, the load can shift.

## 10. Governance of any change in support

Whatever the signature, changes in support are always:

- **declared** to the learner (never done silently),
- **agreed** (explicit agreement on what changes and when),
- **based on observations** (summaries, not impressions),
- **reversible** without stigma (exams, transitions and hard periods are reasons to step back, not failures).

---

## References

- Barkley, R. A. (2012). *Executive functions: What they are, how they work, and why they evolved*. Guilford Press.
- Bowlby, J. (1988). *A secure base: Parent-child attachment and healthy human development*. Basic Books.
- CAST (2024). *Universal Design for Learning Guidelines version 3.0*. https://udlguidelines.cast.org
- Cheng, M., et al. (2025). *ELEPHANT: Measuring and understanding social sycophancy in LLMs*. arXiv:2505.13995.
- Clark, A., & Chalmers, D. (1998). The extended mind. *Analysis, 58*(1), 7-19.
- DeJong, G. (1979). Independent living: From social movement to analytic paradigm. *Archives of Physical Medicine and Rehabilitation, 60*(10), 435-446.
- Kafer, A. (2013). *Feminist, Queer, Crip*. Indiana University Press.
- Kittay, E. F. (1999). *Love's Labor: Essays on Women, Equality, and Dependency*. Routledge.
- Mesibov, G. B., & Shea, V. (2010). The TEACCH program in the era of evidence-based practice. *Journal of Autism and Developmental Disorders, 40*(5), 570-579.
- Oliver, M. (1990). *The Politics of Disablement*. Macmillan.
- Risko, E. F., & Gilbert, S. J. (2016). Cognitive offloading. *Trends in Cognitive Sciences, 20*(9), 676-688.
- Sarkar, A. (2024). AI should challenge, not obey. *Communications of the ACM*.
- UPIAS (1976). *Fundamental Principles of Disability*. Union of the Physically Impaired Against Segregation.
- Vygotsky, L. S. (1978). *Mind in society*. Harvard University Press.
- World Health Organization (2001). *International Classification of Functioning, Disability and Health (ICF)*.
