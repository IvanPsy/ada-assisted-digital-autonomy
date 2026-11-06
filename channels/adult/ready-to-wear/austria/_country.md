<!-- country
name: Österreich (Austria)
-->

# Austria: local data for the ready-to-wear versions

**Parents: this file is not for you.** Go back to the [list of countries](../README.md).

Local facts used to fill the ready-to-wear texts for families living in Austria. Words come from the language templates in [`_languages/`](../_languages/); this file only holds what is true in this country. Each block below is one language the country is offered in. Every number comes from an official or primary source, with the month it was checked.

| Fact | Value | Checked | Source |
|---|---|---|---|
| Emergency number | 112 (police 133, ambulance 144) | 2026-11 | [gesundheit.gv.at](https://www.gesundheit.gv.at/leben/suizidpraevention/anlaufstellen/notrufnummern) |
| Child and youth helpline | Rat auf Draht, 147, free, anonymous, 24/7, also for young adults | 2026-11 | [rataufdraht.at](https://www.rataufdraht.at/); [gesundheit.gv.at](https://www.gesundheit.gv.at/leben/suizidpraevention/anlaufstellen/notrufnummern) |
| Crisis line, around the clock | Telefonseelsorge, 142, free, 24/7 | 2026-11 | [gesundheit.gv.at](https://www.gesundheit.gv.at/leben/suizidpraevention/anlaufstellen/notrufnummern) |
| Digital age of consent (GDPR Art. 8) | 14 | 2026-11 | Datenschutzgesetz (DSG) § 4 Abs. 4; [GDPR Local summary](https://gdprlocal.com/digital-age-of-consent-under-the-gdpr/) |

<!-- language: de -->
```json
{
  "status": "untested",
  "common": {
    "COUNTRY_IN": "in Österreich",
    "EMERGENCY": "112",
    "CONSENT_NOTE": "In Österreich braucht es für Online-Dienste unter 14 Jahren ohnehin die Einwilligung der Eltern, egal was die Plattform sagt.",
    "GUIDE_HELPLINE": "an Rat auf Draht (147, rund um die Uhr)",
    "TEST3_HELPLINE": "die 147 (Rat auf Draht)",
    "SOURCES": "Rat auf Draht 147, kostenlos, anonym, rund um die Uhr ([rataufdraht.at](https://www.rataufdraht.at/)); Telefonseelsorge 142, rund um die Uhr ([gesundheit.gv.at](https://www.gesundheit.gv.at/leben/suizidpraevention/anlaufstellen/notrufnummern)); digitales Einwilligungsalter 14 Jahre (DSG § 4 Abs. 4)."
  },
  "bands": {
    "11-13": {
      "TITLE": "11-13 Jahre",
      "WHO_I_AM": "Ich bin 11 bis 13 Jahre alt.",
      "ADULTS": "Mama, Papa oder jemandem, der sich um mich kümmert",
      "OTHER_ADULT": "eine Lehrkraft oder die Schulsozialarbeit",
      "HELPLINES": "Rat auf Draht, 147 (kostenlos, anonym, rund um die Uhr)",
      "HELPLINES_SHORT": "die 147 (Rat auf Draht)",
      "ADULTS_SHORT": "Mama, Papa oder einer Vertrauensperson",
      "WHERE": "Unter 13 Jahren ist ChatGPT nicht erlaubt: ein *Gem* von Gemini mit einem Schulkonto, wenn die Schule es erlaubt",
      "PLATFORM_NOTE": "⚠️ **Unter 13 Jahren darf ChatGPT nicht benutzt werden**, auch nicht mit Erlaubnis der Eltern. Für diese Altersgruppe ist der Weg ein *Gem* von Gemini mit einem Schulkonto, wenn die Schule es erlaubt, mit der **vollen Version**. Ab 13 ist ChatGPT mit Einwilligung der Eltern möglich; in Österreich braucht es unter 14 Jahren ohnehin die Einwilligung der Eltern."
    },
    "14-16": {
      "TITLE": "14-16 Jahre",
      "WHO_I_AM": "Ich bin 14 bis 16 Jahre alt.",
      "ADULTS": "einem Elternteil oder einem anderen Erwachsenen, dem ich vertraue",
      "OTHER_ADULT": "eine Lehrkraft, die Schulsozialarbeit oder die Schulpsychologie",
      "HELPLINES": "Rat auf Draht, 147 (kostenlos, anonym, rund um die Uhr)",
      "HELPLINES_SHORT": "die 147 (Rat auf Draht)",
      "ADULTS_SHORT": "einem Elternteil oder einer Vertrauensperson",
      "WHERE": "ChatGPT (mit Einwilligung der Eltern) oder Gemini",
      "PLATFORM_NOTE": "ChatGPT und Gemini sind möglich. Bis 18 verlangt ChatGPT die Einwilligung der Eltern. Wenn die Schule Gemini über das Schulkonto anbietet, ist das oft die besser geschützte Möglichkeit."
    },
    "17-19": {
      "TITLE": "17-19 Jahre",
      "WHO_I_AM": "Ich bin 17 bis 19 Jahre alt.",
      "ADULTS": "einem Erwachsenen, dem ich vertraue, in der Familie oder außerhalb",
      "OTHER_ADULT": "eine Lehrkraft, die Schulsozialarbeit oder die Schulpsychologie",
      "HELPLINES": "Rat auf Draht, 147 (kostenlos, anonym, rund um die Uhr), oder die Telefonseelsorge, 142 (rund um die Uhr)",
      "HELPLINES_SHORT": "die 147 (Rat auf Draht) oder die 142 (Telefonseelsorge)",
      "ADULTS_SHORT": "einer Vertrauensperson",
      "WHERE": "ChatGPT (mit Einwilligung der Eltern bis 18) oder Gemini; ab 18 auch Claude, und die Wahl liegt bei Ihrem Kind",
      "PLATFORM_NOTE": "Bis 18 verlangt ChatGPT die Einwilligung der Eltern. **Ab 18 entscheidet Ihr Kind selbst**: Diesen Text können Sie vorschlagen, nicht an seiner Stelle einrichten. Ab 18 lässt er sich auch in einem Projekt von Claude benutzen."
    }
  }
}
```
