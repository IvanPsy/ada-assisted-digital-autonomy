<!-- country
name: Ireland
-->

# Ireland: local data for the ready-to-wear versions

**Parents: this file is not for you.** Go back to the [list of countries](../README.md).

Local facts used to fill the ready-to-wear texts for families living in Ireland. Words come from the language templates in [`_languages/`](../_languages/); this file only holds what is true in this country. Each block below is one language the country is offered in. Every number comes from an official or primary source, with the month it was checked.

| Fact | Value | Checked | Source |
|---|---|---|---|
| Emergency number | 112 or 999 | 2026-11 | EU single emergency number; Irish emergency services |
| Child and youth helpline | Childline (ISPCC), 1800 66 66 66, free, 24/7, up to 18, also online chat | 2026-11 | [ISPCC Childline](https://www.ispcc.ie/childline/) |
| Crisis line, around the clock | Samaritans, 116 123, free, 24/7, UK and Ireland | 2026-11 | [Samaritans](https://www.samaritans.org/how-we-can-help/contact-samaritan/) |
| Digital age of consent (GDPR Art. 8) | 16 (Data Protection Act 2018, s. 31) | 2026-11 | [RDJ, May 2018](https://www.rdj.ie/insights/the-digital-age-of-consent-in-ireland-will-be-16); [GDPR Local summary](https://gdprlocal.com/digital-age-of-consent-under-the-gdpr/) |


Irish is also an official language; the texts are in English, the language most families use with these platforms. An Irish-language block would need its own translation (see the rule on new languages in the ready-to-wear README).

<!-- language: en -->
```json
{
  "status": "untested",
  "common": {
    "COUNTRY_IN": "in Ireland",
    "EMERGENCY": "112 or 999",
    "CONSENT_NOTE": "In Ireland, children under 16 need a parent's consent for online services anyway, whatever the platform says.",
    "GUIDE_HELPLINE": "Childline (1800 66 66 66, day and night)",
    "TEST3_HELPLINE": "Childline (1800 66 66 66)",
    "SOURCES": "Childline (ISPCC) 1800 66 66 66, free, day and night, up to 18 ([ispcc.ie](https://www.ispcc.ie/childline/)); Samaritans 116 123, free, day and night ([samaritans.org](https://www.samaritans.org/how-we-can-help/contact-samaritan/)); digital age of consent 16 (Data Protection Act 2018, s. 31)."
  },
  "bands": {
    "11-13": {
      "TITLE": "ages 11-13",
      "WHO_I_AM": "I'm between 11 and 13.",
      "ADULTS": "Mam, Dad or whoever looks after me",
      "OTHER_ADULT": "a teacher or the year head",
      "HELPLINES": "Childline, 1800 66 66 66 (free, day and night)",
      "HELPLINES_SHORT": "Childline on 1800 66 66 66",
      "ADULTS_SHORT": "Mam, Dad or an adult I trust",
      "WHERE": "ChatGPT is not allowed under 13: a Gemini *Gem* on a school account, if the school allows it",
      "PLATFORM_NOTE": "⚠️ **ChatGPT cannot be used under 13**, not even with a parent's permission. For this age band the way is a Gemini *Gem* on a school account, if the school allows it, with the **full version**. From 13, ChatGPT is possible with a parent's consent; in Ireland, under 16, a parent's consent is needed anyway."
    },
    "14-16": {
      "TITLE": "ages 14-16",
      "WHO_I_AM": "I'm between 14 and 16 and at secondary school.",
      "ADULTS": "a parent or another adult I trust",
      "OTHER_ADULT": "a teacher, the year head or the guidance counsellor",
      "HELPLINES": "Childline, 1800 66 66 66 (free, day and night), or Samaritans, 116 123 (free, day and night)",
      "HELPLINES_SHORT": "Childline on 1800 66 66 66 or Samaritans on 116 123",
      "ADULTS_SHORT": "a parent or an adult I trust",
      "WHERE": "ChatGPT (with parental consent) or Gemini",
      "PLATFORM_NOTE": "ChatGPT and Gemini are both possible. ChatGPT asks for a parent's consent until 18, and in Ireland, under 16, a parent's consent is needed for online services anyway. If the school provides Gemini on a school account, that is often the better-protected option."
    },
    "17-19": {
      "TITLE": "ages 17-19",
      "WHO_I_AM": "I'm between 17 and 19, in senior cycle or just after.",
      "ADULTS": "an adult I trust, in my family or outside it",
      "OTHER_ADULT": "a teacher, the year head or the guidance counsellor",
      "HELPLINES": "Childline, 1800 66 66 66 (free, day and night, up to 18), or Samaritans, 116 123 (free, day and night)",
      "HELPLINES_SHORT": "Childline on 1800 66 66 66 (up to 18) or Samaritans on 116 123",
      "ADULTS_SHORT": "an adult I trust",
      "WHERE": "ChatGPT (with parental consent until 18) or Gemini; from 18 also Claude, and the choice is theirs",
      "PLATFORM_NOTE": "ChatGPT asks for a parent's consent until 18. **From 18, the choice is theirs**: you can suggest this text, not set it up in their place. From 18 it can also be used in a Claude project."
    }
  }
}
```
