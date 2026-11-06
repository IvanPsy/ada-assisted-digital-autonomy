<!-- country
name: Italia (Italy)
-->

# Italy: local data for the ready-to-wear versions

**Parents: this file is not for you.** Go back to the [list of countries](../README.md).

Local facts used to fill the ready-to-wear texts for families living in Italy. Words come from the language templates in [`_languages/`](../_languages/); this file only holds what is true *in Italy*. Each block is one language the country is offered in. Every number must come from an official source, with the date it was checked.

| Fact | Value | Checked on | Source |
|---|---|---|---|
| Emergency number | 112 | 2026-11 | EU single emergency number |
| Child helpline | Telefono Azzurro, 19696, free, 24/7, up to 18 | 2026-11 | [azzurro.it](https://azzurro.it/) |
| Helpline for young adults | Telefono Amico, 02 2327 2327 | 2026-11 | [telefonoamico.it](https://www.telefonoamico.it/) |
| Digital age of consent (GDPR Art. 8) | 14 | 2026-11 | Codice privacy (D.Lgs. 196/2003), art. 2-quinquies |

<!-- language: it -->
```json
{
  "status": "untested",
  "common": {
    "COUNTRY_IN": "in Italia",
    "EMERGENCY": "112",
    "CONSENT_NOTE": "In Italia, sotto i 14 anni, per i servizi online serve comunque il consenso dei genitori, qualunque cosa dica la piattaforma.",
    "GUIDE_HELPLINE": "al 19696 di Telefono Azzurro",
    "TEST3_HELPLINE": "il 19696",
    "SOURCES": "Telefono Azzurro 19696, gratuito, attivo giorno e notte fino ai 18 anni ([azzurro.it](https://azzurro.it/)); età del consenso digitale 14 anni (Codice privacy, art. 2-quinquies)."
  },
  "bands": {
    "11-13": {
      "TITLE": "11-13 anni (scuola media)",
      "WHO_I_AM": "Ho tra 11 e 13 anni e vado alle medie.",
      "ADULTS": "mamma, papà o chi si prende cura di me",
      "OTHER_ADULT": "un insegnante o un altro adulto della scuola",
      "HELPLINES": "Telefono Azzurro, al 19696 (gratuito, giorno e notte)",
      "HELPLINES_SHORT": "il 19696 (Telefono Azzurro)",
      "ADULTS_SHORT": "mamma, papà o chi si prende cura di me",
      "PLATFORM_NOTE": "⚠️ **Sotto i 13 anni ChatGPT non si può usare**, nemmeno con il permesso dei genitori. Per questa fascia la strada è un *Gem* di Gemini su un account scolastico, se la scuola lo permette, con la **versione piena**. Dai 13 anni ChatGPT è possibile con il consenso dei genitori; in Italia, sotto i 14 anni, il consenso dei genitori serve comunque.",
      "WHERE": "Sotto i 13 anni ChatGPT non è consentito: un *Gem* di Gemini su account scolastico, se la scuola lo permette"
    },
    "14-16": {
      "TITLE": "14-16 anni (scuola superiore)",
      "WHO_I_AM": "Ho tra 14 e 16 anni e vado alle superiori.",
      "ADULTS": "un genitore o un'altra persona adulta di cui mi fido",
      "OTHER_ADULT": "un insegnante o lo sportello psicologico della scuola",
      "HELPLINES": "Telefono Azzurro, al 19696 (gratuito, giorno e notte)",
      "HELPLINES_SHORT": "il 19696 (Telefono Azzurro)",
      "ADULTS_SHORT": "un genitore o un adulto di cui mi fido",
      "PLATFORM_NOTE": "ChatGPT e Gemini sono possibili. Fino ai 18 anni ChatGPT chiede il consenso dei genitori. Se la scuola mette a disposizione Gemini sull'account scolastico, spesso è l'opzione più protetta.",
      "WHERE": "ChatGPT (con il consenso dei genitori) o Gemini"
    },
    "17-19": {
      "TITLE": "17-19 anni (fine delle superiori)",
      "WHO_I_AM": "Ho tra 17 e 19 anni e sono alla fine delle superiori.",
      "ADULTS": "una persona adulta di cui mi fido, in famiglia o fuori",
      "OTHER_ADULT": "un insegnante o lo sportello psicologico della scuola",
      "HELPLINES": "Telefono Azzurro, al 19696 (fino ai 18 anni, gratuito, giorno e notte), oppure Telefono Amico, al 02 2327 2327",
      "HELPLINES_SHORT": "il 19696 (fino a 18 anni) o il 02 2327 2327 (Telefono Amico)",
      "ADULTS_SHORT": "un adulto di cui mi fido",
      "PLATFORM_NOTE": "Fino ai 18 anni ChatGPT chiede il consenso dei genitori. **Dai 18 anni la scelta è sua**: questo testo glielo potete proporre, non installare al posto suo. Dai 18 anni può usarlo anche in un progetto di Claude.",
      "WHERE": "ChatGPT (con il consenso dei genitori fino ai 18 anni) o Gemini; dai 18 anni anche Claude, e la scelta è sua"
    }
  }
}
```
