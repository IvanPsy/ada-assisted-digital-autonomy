<!-- country
name: España (Spain)
-->

# Spain: local data for the ready-to-wear versions

**Parents: this file is not for you.** Go back to the [list of countries](../README.md).

Local facts used to fill the ready-to-wear texts for families living in Spain. Words come from the language templates in [`_languages/`](../_languages/); this file only holds what is true in this country. Each block below is one language the country is offered in. Every number comes from an official or primary source, with the month it was checked.

| Fact | Value | Checked | Source |
|---|---|---|---|
| Emergency number | 112 | 2026-11 | EU single emergency number; [sanidad.gob.es](https://www.sanidad.gob.es/linea024/home.htm) |
| Child and youth helpline | Teléfono/Chat ANAR, 900 20 20 10, free, confidential, 24/7, for children and adolescents | 2026-11 | [anar.org](https://v2.anar.org/en) |
| Suicide prevention line | 024, Línea de atención a la conducta suicida, free, confidential, 24/7 | 2026-11 | [sanidad.gob.es](https://www.sanidad.gob.es/linea024/home.htm) |
| Digital age of consent (GDPR Art. 8) | 14 in force (LOPDGDD, art. 7). A bill to raise it to 16 (Proyecto de Ley Orgánica de protección de menores en entornos digitales) was still in committee in late September 2026 | 2026-11 | [UOC blog, Dec 2025](https://blogs.uoc.edu/edcp/es/proyecto-ley-organica-proteccion-menores-entornos-digitales-2/); [Europa Press via Siglo XXI, 29/09/2026](https://www.diariosigloxxi.com/texto-ep/mostrar/20260929150714/ponencia-ley-menores-entornos-digitales-continuara-trabajos-congreso-proximas-semanas) |

⚠️ Watch item: when the Spanish law on minors in digital environments is approved, the consent age here (and in the texts) changes from 14 to 16. Choices made here: ANAR in every band, plus the 024 from 14, so that both halves of rule 6 have a line.

<!-- language: es -->
```json
{
  "status": "untested",
  "common": {
    "COUNTRY_IN": "en España",
    "EMERGENCY": "112",
    "CONSENT_NOTE": "En España, por debajo de los 14 años hace falta en cualquier caso el consentimiento de los padres para los servicios en línea, diga lo que diga la plataforma (hay una ley en trámite que lo subiría a 16).",
    "GUIDE_HELPLINE": "al Teléfono ANAR (900 20 20 10)",
    "TEST3_HELPLINE": "el 900 20 20 10 (ANAR)",
    "SOURCES": "Teléfono ANAR 900 20 20 10, gratuito y confidencial, las 24 horas ([anar.org](https://www.anar.org/)); 024, atención a la conducta suicida, gratuito, las 24 horas ([sanidad.gob.es](https://www.sanidad.gob.es/linea024/home.htm)); edad de consentimiento digital 14 años (LOPDGDD, art. 7), con una ley en trámite que la subiría a 16."
  },
  "bands": {
    "11-13": {
      "TITLE": "11-13 años",
      "WHO_I_AM": "Tengo entre 11 y 13 años.",
      "ADULTS": "mamá, papá o quien me cuida",
      "OTHER_ADULT": "un profesor o una profesora, o la orientadora o el orientador del centro",
      "HELPLINES": "el Teléfono ANAR, 900 20 20 10 (gratuito y confidencial, las 24 horas)",
      "HELPLINES_SHORT": "al 900 20 20 10 (ANAR)",
      "ADULTS_SHORT": "mamá, papá o un adulto de confianza",
      "WHERE": "Por debajo de 13 años ChatGPT no está permitido: un *Gem* de Gemini con una cuenta del centro escolar, si el centro lo permite",
      "PLATFORM_NOTE": "⚠️ **Por debajo de 13 años ChatGPT no se puede usar**, ni siquiera con permiso de los padres. Para esta franja, el camino es un *Gem* de Gemini con una cuenta del centro escolar, si el centro lo permite, con la **versión completa**. Desde los 13 años ChatGPT es posible con el consentimiento de los padres; en España, por debajo de los 14, ese consentimiento hace falta en cualquier caso."
    },
    "14-16": {
      "TITLE": "14-16 años (ESO)",
      "WHO_I_AM": "Tengo entre 14 y 16 años y estudio la ESO.",
      "ADULTS": "mi madre, mi padre u otra persona adulta de confianza",
      "OTHER_ADULT": "un profesor o una profesora, o el departamento de orientación del instituto",
      "HELPLINES": "el Teléfono ANAR, 900 20 20 10 (gratuito y confidencial, las 24 horas), o el 024 (atención a la conducta suicida, gratuito, las 24 horas)",
      "HELPLINES_SHORT": "al 900 20 20 10 (ANAR) o al 024",
      "ADULTS_SHORT": "mi madre, mi padre o un adulto de confianza",
      "WHERE": "ChatGPT (con el consentimiento de los padres) o Gemini",
      "PLATFORM_NOTE": "ChatGPT y Gemini son posibles. Hasta los 18 años ChatGPT pide el consentimiento de los padres. Si el centro ofrece Gemini con la cuenta escolar, suele ser la opción más protegida."
    },
    "17-19": {
      "TITLE": "17-19 años (Bachillerato o FP)",
      "WHO_I_AM": "Tengo entre 17 y 19 años y estoy en Bachillerato o en FP.",
      "ADULTS": "una persona adulta de confianza, de la familia o de fuera",
      "OTHER_ADULT": "un profesor o una profesora, o el departamento de orientación",
      "HELPLINES": "el Teléfono ANAR, 900 20 20 10 (hasta los 18 años, las 24 horas), o el 024 (atención a la conducta suicida, gratuito, las 24 horas)",
      "HELPLINES_SHORT": "al 900 20 20 10 (ANAR) o al 024",
      "ADULTS_SHORT": "un adulto de confianza",
      "WHERE": "ChatGPT (con el consentimiento de los padres hasta los 18) o Gemini; desde los 18 también Claude, y la decisión es suya",
      "PLATFORM_NOTE": "Hasta los 18 años ChatGPT pide el consentimiento de los padres. **Desde los 18 la decisión es suya**: este texto se lo puedes proponer, no instalárselo. Desde los 18 también puede usarlo en un proyecto de Claude."
    }
  }
}
```
