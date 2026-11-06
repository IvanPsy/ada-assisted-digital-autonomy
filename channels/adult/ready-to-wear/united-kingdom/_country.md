<!-- country
name: United Kingdom
-->

# the United Kingdom: local data for the ready-to-wear versions

**Parents: this file is not for you.** Go back to the [list of countries](../README.md).

Local facts used to fill the ready-to-wear texts for families living in the United Kingdom. Words come from the language templates in [`_languages/`](../_languages/); this file only holds what is true in this country. Each block below is one language the country is offered in. Every number comes from an official or primary source, with the month it was checked.

| Fact | Value | Checked | Source |
|---|---|---|---|
| Emergency number | 999 (112 also works) | 2026-11 | UK emergency services |
| Child and youth helpline | Childline, 0800 1111, free, 24/7, under 19, across the UK | 2026-11 | [NSPCC, Childline](https://www.nspcc.org.uk/keeping-children-safe/our-services/childline/) |
| Crisis line, around the clock | Samaritans, 116 123, free, 24/7, UK and Ireland; Welsh Language Line 0808 164 0123 | 2026-11 | [Samaritans](https://www.samaritans.org/how-we-can-help/contact-samaritan/) |
| Northern Ireland only | Lifeline, 0808 808 8000, free, 24/7, crisis line for everyone in Northern Ireland (not used in the texts, which stay UK-wide) | 2026-11 | [nidirect](https://www.nidirect.gov.uk/node/3301) |
| Digital age of consent | 13, one rule for the whole UK (UK GDPR Art. 8, Data Protection Act 2018 s. 9) | 2026-11 | [ICO](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/children-and-the-uk-gdpr/what-are-the-rules-about-an-iss-and-consent/) |


**One file for England, Scotland, Wales and Northern Ireland.** The helplines used (Childline, Samaritans), the emergency number and the consent age are the same in all four nations, so a single file is enough. What differs is school: children in Scotland and Northern Ireland are still in primary school at 11, and the names of the years differ (Year 7-13, S1-S6, post-primary). The texts therefore name age bands, not school years, and talk about "the pastoral or guidance staff at school", which works in all four systems. Northern Ireland also has Lifeline, a 24/7 crisis line, listed above for the guide and for other uses. If a nation-specific version is ever needed, it is a separate country folder with the same English template.

<!-- language: en -->
```json
{
  "status": "untested",
  "common": {
    "COUNTRY_IN": "in the United Kingdom (England, Scotland, Wales, Northern Ireland)",
    "EMERGENCY": "999",
    "CONSENT_NOTE": "In the UK, children under 13 need a parent's consent for online services anyway, whatever the platform says; ChatGPT asks for parental consent until 18.",
    "GUIDE_HELPLINE": "Childline (0800 1111, day and night)",
    "TEST3_HELPLINE": "Childline (0800 1111)",
    "SOURCES": "Childline 0800 1111, free, day and night, for under-19s across the UK ([NSPCC](https://www.nspcc.org.uk/keeping-children-safe/our-services/childline/)); Samaritans 116 123, free, day and night ([samaritans.org](https://www.samaritans.org/how-we-can-help/contact-samaritan/)); in Northern Ireland also Lifeline, 0808 808 8000, day and night ([nidirect](https://www.nidirect.gov.uk/node/3301)); digital age of consent 13 ([ICO](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/children-and-the-uk-gdpr/what-are-the-rules-about-an-iss-and-consent/))."
  },
  "bands": {
    "11-13": {
      "TITLE": "ages 11-13",
      "WHO_I_AM": "I'm between 11 and 13.",
      "ADULTS": "Mum, Dad or whoever looks after me",
      "OTHER_ADULT": "a teacher or the pastoral or guidance staff at school",
      "HELPLINES": "Childline, 0800 1111 (free, day and night)",
      "HELPLINES_SHORT": "Childline on 0800 1111",
      "ADULTS_SHORT": "Mum, Dad or an adult I trust",
      "WHERE": "ChatGPT is not allowed under 13: a Gemini *Gem* on a school account, if the school allows it",
      "PLATFORM_NOTE": "⚠️ **ChatGPT cannot be used under 13**, not even with a parent's permission. For this age band the way is a Gemini *Gem* on a school account, if the school allows it, with the **full version**. From 13, ChatGPT is possible with a parent's consent."
    },
    "14-16": {
      "TITLE": "ages 14-16",
      "WHO_I_AM": "I'm between 14 and 16 and at secondary school.",
      "ADULTS": "a parent or another adult I trust",
      "OTHER_ADULT": "a teacher, the pastoral or guidance staff, or the school counsellor",
      "HELPLINES": "Childline, 0800 1111 (free, day and night), or Samaritans, 116 123 (free, day and night)",
      "HELPLINES_SHORT": "Childline on 0800 1111 or Samaritans on 116 123",
      "ADULTS_SHORT": "a parent or an adult I trust",
      "WHERE": "ChatGPT (with parental consent) or Gemini",
      "PLATFORM_NOTE": "ChatGPT and Gemini are both possible. ChatGPT asks for a parent's consent until 18. If the school provides Gemini on a school account, that is often the better-protected option."
    },
    "17-19": {
      "TITLE": "ages 17-19",
      "WHO_I_AM": "I'm between 17 and 19, finishing school or at college.",
      "ADULTS": "an adult I trust, in my family or outside it",
      "OTHER_ADULT": "a teacher, a tutor or the student support team",
      "HELPLINES": "Childline, 0800 1111 (free, day and night, under 19), or Samaritans, 116 123 (free, day and night)",
      "HELPLINES_SHORT": "Childline on 0800 1111 (under 19) or Samaritans on 116 123",
      "ADULTS_SHORT": "an adult I trust",
      "WHERE": "ChatGPT (with parental consent until 18) or Gemini; from 18 also Claude, and the choice is theirs",
      "PLATFORM_NOTE": "ChatGPT asks for a parent's consent until 18. **From 18, the choice is theirs**: you can suggest this text, not set it up in their place. From 18 it can also be used in a Claude project."
    }
  }
}
```
