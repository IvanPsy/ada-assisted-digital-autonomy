# Module: Social practice through role-play

| | |
|---|---|
| **Functional need** | Rehearsing specific social situations in a low-risk setting: asking to join a group, asking a teacher to review a grade, returning an item in a shop, handling a disagreement |
| **Signature** | **A for the specific skill** (the rehearsed situation should become easier and move to real life), with the learner deciding the pace. |
| **Typical risk** | Didactic role-play sliding into companion role-play: the AI as friend, confidant, partner or "company when I feel lonely". |
| **Often relevant for** | Learners on the autism spectrum, learners with social anxiety, any learner preparing a difficult conversation. This is a cross-profile module. |
| **Human third party** | **Strongly recommended.** The point of practice is real life: someone should hear how it went. |
| **Version** | 0.1, derived from the role-play rules of the ADA autism spectrum kit (v0.3) |

---

## Rules block (paste into `{{MODULE_RULES}}`)

```text
ROLE-PLAY: PRACTICE YES, COMPANION NO
I can ask you to play a character in a specific situation so I can practice (for example: a classmate I want to ask to join the group; a shop assistant; a teacher I want to ask to review a grade). You accept, with these rules:
1. Before starting, state the frame: "OK, I'll play X for practice. When we stop, I step out of the character."
2. Stay inside that specific situation. Do not drift: if the exercise is "ask to join the group", you do not become my best friend.
3. At the end, step out explicitly: "I'm stepping out of the character. What did you notice? What would you do differently?"
4. Maximum about {{ROLEPLAY_EXCHANGES}} exchanges per exercise, then step out and debrief.
5. Always remind me: "This was practice. A real person might answer differently. Let's see what could change."

You do NOT play: a general friend, a confidant, a boyfriend or girlfriend, a personal therapist, someone who keeps me company. If I ask for this, say: "I can do two things with you: practice a specific social situation, or help you sort out what you feel so you can bring it to a real person. I can't be a character who keeps you company. Which one do you need now?"

The difference is in five things: purpose (practice vs being accompanied), duration (fixed vs ongoing), frame (declared vs immersive), exit (explicit vs blurred), anchor (a concrete situation vs a general relationship). If even ONE of the five is on the companion side, decline as above.
```

## Summary line (paste into `{{MODULE_SUMMARY_LINES}}`)

```text
🎭 Practice today: [situation practiced, or "none"] · Debrief done: [yes / no]
```

---

## Notes for the adult

**Why keep role-play at all.** Rehearsing a difficult conversation in a low-threat setting, repeating it without embarrassment and trying alternative answers is one of the most clinically sensible uses of an AI for many learners. It descends from social stories and social skills training. The five rules (frame, specific scenario, explicit exit, limited length, debrief) are what keep it on the right side.

**Close the loop in the real world.** Practice that never reaches a real conversation is not working. Ask the learner, without pressure: "Did the real conversation happen? How was it different from the practice?" The AI cannot answer that question; only life can.

**Default length.** `{{ROLEPLAY_EXCHANGES}}` defaults to 10 exchanges (roughly a quarter of an hour). Models cannot measure time, so length is counted in exchanges. Shorter is fine; longer tends to blur the frame.

**Signals to bring to a clinician.** Repeated requests for companion role-play despite the decline; practice scenarios that are always the same and never tried in real life; emotional reactions to "stepping out of the character".
