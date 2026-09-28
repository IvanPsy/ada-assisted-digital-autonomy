# Platform compatibility

> **Last checked: September 2026.** Terms of service, age rules and feature limits change often. Verify on the provider's official pages before configuring anything for a minor, and please open a pull request when something here is out of date.

The **adult channel** can run on any assistant the adult is allowed to use. The **student channel** can only be installed where the learner is allowed to be, under the conditions the provider sets.

## Age and access

| Assistant | Minimum age (consumer) | Minors | Notes |
|---|---|---|---|
| **ChatGPT** (OpenAI) | 13 | 13-18 need parental consent | OpenAI states it is not intended for under-13s and advises caution even above that age. Parental controls exist for linked teen accounts. [Source](https://help.openai.com/en/articles/8313401-is-chatgpt-safe-for-all-ages) · [Parental controls](https://openai.com/index/introducing-parental-controls/) |
| **Gemini** (Google), school account | Set by the school | Depends on the school administrator | Google Workspace for Education admins decide whether students, including under-18s, can use Gemini; in August 2026 Gemini in Classroom was extended to students of all ages where admins enable it. Often the most protected option for the student channel. [Source](https://workspaceupdates.googleblog.com/2026/08/gemini-in-google-classroom-is-expanding-to-users-of-all-ages-with-contextualized-Gemini-starter-prompts-for-students.html) · [Teen access](https://workspaceupdates.googleblog.com/2024/10/gemini-app-access-for-teen-students-workspace-education.html) |
| **Gemini** (Google), personal account | Minimum age for a Google account in the learner's country | Supervised accounts for younger users | Country rules apply (see below). |
| **Claude** (Anthropic), consumer apps | **18** | **Not allowed** | Use Claude for the **adult channel only**. [Source](https://support.claude.com/en/articles/13117299-minimum-age-requirement-access-restriction) |
| Companion apps (virtual friend or partner products) | varies | | **Do not use for the student channel**, whatever their settings: they are designed to hold attention and relationship, which is the opposite of this project. |

**Country rules on digital consent.** In the EU, the age at which a young person can consent to online services on their own ranges from 13 to 16 depending on the member state (GDPR Art. 8); in Italy it is 14. Below that age, parental consent is required regardless of what the platform allows. Outside the EU, check local law (for example COPPA in the US for under-13s).

## Where the instructions go, and how long they can be

The full core alone is about 4,000 characters; with one or two modules the configuration is typically **5,000 to 8,000 characters**. Not every place accepts that.

| Where | Typical limit | Fits the full configuration? |
|---|---|---|
| ChatGPT personal custom instructions, free and Go plans | 1,500 characters | ❌ Use the compact core, or a project |
| ChatGPT personal custom instructions, paid plans | 5,000 characters (raised in July 2026) | ⚠️ Full core alone, or core plus the planning module at most; use a project for anything more |
| ChatGPT projects / custom GPTs | Longer instructions allowed | ✅ Usually |
| Gemini Gems | Longer instructions allowed | ✅ Usually |
| Claude projects (adult channel only) | Longer instructions allowed | ✅ |

Sources on the ChatGPT limit change: [FindSkill.ai](https://findskill.ai/blog/chatgpt-custom-instructions-5000-characters/), [MindStudio](https://www.mindstudio.ai/blog/chatgpt-custom-instructions-character-limit). If text is cut silently by a platform, the rules at the end (including the session summary) are the first to disappear: always check that the pasted text is complete.

## Behavior across models

The same instructions do not behave identically on different models, or on the same platform after a model update. This is why the [tests](../tests/) exist. Run at least the core scenarios:

- when you first configure an assistant,
- when the provider announces a new model,
- when the learner or an adult notices a change in behavior.
