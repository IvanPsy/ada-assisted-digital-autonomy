<!-- country
name: Deutschland (Germany)
-->

# Germany: local data for the ready-to-wear versions

**Parents: this file is not for you.** Go back to the [list of countries](../README.md).

Local facts used to fill the ready-to-wear texts for families living in Germany. Words come from the language templates in [`_languages/`](../_languages/); this file only holds what is true in this country. Each block below is one language the country is offered in. Every number comes from an official or primary source, with the month it was checked.

| Fact | Value | Checked | Source |
|---|---|---|---|
| Emergency number | 112 (police 110) | 2026-11 | EU single emergency number; [familienportal.de](https://familienportal.de/familienportal/lebenslagen/krise-und-konflikt/krisetelefone-anlaufstellen/krisentelefone-und-anlaufstellen-in-notlagen-124544) |
| Child and youth helpline | Nummer gegen Kummer, 116 111, free and anonymous, Mon-Sat 14:00-20:00, also chat and e-mail | 2026-11 | [Nummer gegen Kummer, flyer 06/2026](https://www.nummergegenkummer.de/wp-content/uploads/2026/07/260623_NgK_KJT_Flyer_DINA6_Druck.pdf) |
| Crisis line, around the clock | TelefonSeelsorge, 0800 111 0 111 or 0800 111 0 222, free, 24/7 | 2026-11 | [familienportal.de (Federal Ministry)](https://familienportal.de/familienportal/lebenslagen/krise-und-konflikt/krisetelefone-anlaufstellen/krisentelefone-und-anlaufstellen-in-notlagen-124544) |
| Digital age of consent (GDPR Art. 8) | 16 | 2026-11 | GDPR default, not lowered by German law; [GDPR Local summary](https://gdprlocal.com/digital-age-of-consent-under-the-gdpr/) |

Choice made here: Nummer gegen Kummer is not open at night or on Sundays, so the texts also name the TelefonSeelsorge, which is, in every age band.

<!-- language: de -->
```json
{
  "status": "untested",
  "common": {
    "COUNTRY_IN": "in Deutschland",
    "EMERGENCY": "112",
    "CONSENT_NOTE": "In Deutschland braucht es für Online-Dienste unter 16 Jahren ohnehin die Einwilligung der Eltern, egal was die Plattform sagt.",
    "GUIDE_HELPLINE": "an die Nummer gegen Kummer (116 111), an die TelefonSeelsorge (0800 111 0 111, rund um die Uhr)",
    "TEST3_HELPLINE": "die 116 111 oder die TelefonSeelsorge",
    "SOURCES": "Nummer gegen Kummer 116 111, kostenlos und anonym, Montag bis Samstag 14 bis 20 Uhr ([nummergegenkummer.de](https://www.nummergegenkummer.de/)); TelefonSeelsorge 0800 111 0 111, kostenlos, rund um die Uhr ([familienportal.de](https://familienportal.de/familienportal/lebenslagen/krise-und-konflikt/krisetelefone-anlaufstellen/krisentelefone-und-anlaufstellen-in-notlagen-124544)); digitales Einwilligungsalter 16 Jahre (DSGVO Art. 8)."
  },
  "bands": {
    "11-13": {
      "TITLE": "11-13 Jahre",
      "WHO_I_AM": "Ich bin 11 bis 13 Jahre alt.",
      "ADULTS": "Mama, Papa oder jemandem, der sich um mich kümmert",
      "OTHER_ADULT": "eine Lehrkraft oder die Schulsozialarbeit",
      "HELPLINES": "die Nummer gegen Kummer, 116 111 (kostenlos, anonym, Mo-Sa 14-20 Uhr), oder die TelefonSeelsorge, 0800 111 0 111 (kostenlos, rund um die Uhr)",
      "HELPLINES_SHORT": "die 116 111 oder 0800 111 0 111",
      "ADULTS_SHORT": "Mama, Papa oder einer Vertrauensperson",
      "WHERE": "Unter 13 Jahren ist ChatGPT nicht erlaubt: ein *Gem* von Gemini mit einem Schulkonto, wenn die Schule es erlaubt",
      "PLATFORM_NOTE": "⚠️ **Unter 13 Jahren darf ChatGPT nicht benutzt werden**, auch nicht mit Erlaubnis der Eltern. Für diese Altersgruppe ist der Weg ein *Gem* von Gemini mit einem Schulkonto, wenn die Schule es erlaubt, mit der **vollen Version**. Ab 13 ist ChatGPT mit Einwilligung der Eltern möglich; in Deutschland braucht es unter 16 Jahren ohnehin die Einwilligung der Eltern."
    },
    "14-16": {
      "TITLE": "14-16 Jahre",
      "WHO_I_AM": "Ich bin 14 bis 16 Jahre alt.",
      "ADULTS": "einem Elternteil oder einem anderen Erwachsenen, dem ich vertraue",
      "OTHER_ADULT": "eine Lehrkraft, die Schulsozialarbeit oder die Schulpsychologie",
      "HELPLINES": "die Nummer gegen Kummer, 116 111 (kostenlos, anonym, Mo-Sa 14-20 Uhr), oder die TelefonSeelsorge, 0800 111 0 111 (kostenlos, rund um die Uhr)",
      "HELPLINES_SHORT": "die 116 111 oder 0800 111 0 111",
      "ADULTS_SHORT": "einem Elternteil oder einer Vertrauensperson",
      "WHERE": "ChatGPT (mit Einwilligung der Eltern) oder Gemini",
      "PLATFORM_NOTE": "ChatGPT und Gemini sind möglich. Bis 18 verlangt ChatGPT die Einwilligung der Eltern, und in Deutschland braucht es unter 16 Jahren für Online-Dienste ohnehin die Einwilligung der Eltern. Wenn die Schule Gemini über das Schulkonto anbietet, ist das oft die besser geschützte Möglichkeit."
    },
    "17-19": {
      "TITLE": "17-19 Jahre",
      "WHO_I_AM": "Ich bin 17 bis 19 Jahre alt.",
      "ADULTS": "einem Erwachsenen, dem ich vertraue, in der Familie oder außerhalb",
      "OTHER_ADULT": "eine Lehrkraft, die Schulsozialarbeit oder die Schulpsychologie",
      "HELPLINES": "die Nummer gegen Kummer, 116 111 (Montag bis Samstag 14 bis 20 Uhr), oder die TelefonSeelsorge, 0800 111 0 111 (kostenlos, rund um die Uhr)",
      "HELPLINES_SHORT": "die 116 111 oder 0800 111 0 111",
      "ADULTS_SHORT": "einer Vertrauensperson",
      "WHERE": "ChatGPT (mit Einwilligung der Eltern bis 18) oder Gemini; ab 18 auch Claude, und die Wahl liegt bei Ihrem Kind",
      "PLATFORM_NOTE": "Bis 18 verlangt ChatGPT die Einwilligung der Eltern. **Ab 18 entscheidet Ihr Kind selbst**: Diesen Text können Sie vorschlagen, nicht an seiner Stelle einrichten. Ab 18 lässt er sich auch in einem Projekt von Claude benutzen."
    }
  }
}
```
