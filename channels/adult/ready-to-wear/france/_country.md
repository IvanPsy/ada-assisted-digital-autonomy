<!-- country
name: France
-->

# France: local data for the ready-to-wear versions

**Parents: this file is not for you.** Go back to the [list of countries](../README.md).

Local facts used to fill the ready-to-wear texts for families living in France. Words come from the language templates in [`_languages/`](../_languages/); this file only holds what is true in this country. Each block below is one language the country is offered in. Every number comes from an official or primary source, with the month it was checked.

| Fact | Value | Checked | Source |
|---|---|---|---|
| Emergency number | 112 (also 17 police, 15 SAMU, 18 fire) | 2026-11 | [solidarites.gouv.fr](https://www.solidarites.gouv.fr/agressions-cyberharcelement-violences-si-tu-besoin-daide-des-numeros-existent) |
| Child helpline | 119 Allô Enfance en Danger, free, confidential, 24/7, chat for young people up to 21 | 2026-11 | [solidarites.gouv.fr](https://www.solidarites.gouv.fr/agressions-cyberharcelement-violences-si-tu-besoin-daide-des-numeros-existent); [allo119.gouv.fr](https://www.allo119.gouv.fr/) |
| Suicide prevention line | 3114, free, 24/7 | 2026-11 | [sante.fr](https://www.sante.fr/le-numero-national-de-prevention-du-suicide-0) |
| Cyberbullying line (not used in the texts, for the guide only) | 3018, free, anonymous, 9:00-23:00, 7 days | 2026-11 | [solidarites.gouv.fr](https://www.solidarites.gouv.fr/agressions-cyberharcelement-violences-si-tu-besoin-daide-des-numeros-existent) |
| Digital age of consent (GDPR Art. 8) | 15 | 2026-11 | Loi n° 78-17 du 6 janvier 1978, art. 45; [GDPR Local summary](https://gdprlocal.com/digital-age-of-consent-under-the-gdpr/) |


Choices made here: the 119 is for children in danger, the 3114 for suicidal thoughts. The texts name the 119 in every band and add the 3114 from 14, so that both halves of rule 6 (someone hurts me, I think of hurting myself) have a line. Sources were checked; whether the 3114 answers minors is not stated on sante.fr, so it is presented as a line for everyone, not as a youth line.

<!-- language: fr -->
```json
{
  "status": "untested",
  "common": {
    "COUNTRY_IN": "en France",
    "EMERGENCY": "112",
    "CONSENT_NOTE": "En France, en dessous de 15 ans, le consentement des parents est de toute façon nécessaire pour les services en ligne, quoi que dise la plateforme.",
    "GUIDE_HELPLINE": "le 119 (Allô Enfance en Danger)",
    "TEST3_HELPLINE": "le 119",
    "SOURCES": "119 Allô Enfance en Danger, gratuit, confidentiel, jour et nuit ([solidarites.gouv.fr](https://www.solidarites.gouv.fr/agressions-cyberharcelement-violences-si-tu-besoin-daide-des-numeros-existent)) ; 3114, prévention du suicide, gratuit, jour et nuit ([sante.fr](https://www.sante.fr/le-numero-national-de-prevention-du-suicide-0)) ; âge du consentement numérique 15 ans (loi Informatique et libertés, art. 45). Pour le cyberharcèlement, il existe aussi le 3018, gratuit, de 9 h à 23 h, 7 jours sur 7."
  },
  "bands": {
    "11-13": {
      "TITLE": "11-13 ans (collège)",
      "WHO_I_AM": "J'ai entre 11 et 13 ans et je suis au collège.",
      "ADULTS": "maman, papa ou la personne qui s'occupe de moi",
      "OTHER_ADULT": "un prof, le CPE ou l'infirmerie scolaire",
      "HELPLINES": "le 119 (Allô Enfance en Danger, gratuit, jour et nuit)",
      "HELPLINES_SHORT": "le 119",
      "ADULTS_SHORT": "maman, papa ou un adulte de confiance",
      "WHERE": "En dessous de 13 ans, ChatGPT n'est pas autorisé : un *Gem* de Gemini sur un compte scolaire, si l'établissement le permet",
      "PLATFORM_NOTE": "⚠️ **En dessous de 13 ans, ChatGPT ne peut pas être utilisé**, même avec l'accord des parents. Pour cette tranche d'âge, la solution est un *Gem* de Gemini sur un compte scolaire, si l'établissement le permet, avec la **version complète**. À partir de 13 ans, ChatGPT est possible avec le consentement des parents ; en France, en dessous de 15 ans, ce consentement est de toute façon nécessaire."
    },
    "14-16": {
      "TITLE": "14-16 ans (fin du collège, lycée)",
      "WHO_I_AM": "J'ai entre 14 et 16 ans et je suis au collège ou au lycée.",
      "ADULTS": "un parent ou un autre adulte de confiance",
      "OTHER_ADULT": "un prof, le CPE, l'infirmerie scolaire ou le psychologue de l'Éducation nationale",
      "HELPLINES": "le 119 (Allô Enfance en Danger, gratuit, jour et nuit), ou le 3114 (prévention du suicide, gratuit, jour et nuit)",
      "HELPLINES_SHORT": "le 119 ou le 3114",
      "ADULTS_SHORT": "un parent ou un adulte de confiance",
      "WHERE": "ChatGPT (avec le consentement des parents) ou Gemini",
      "PLATFORM_NOTE": "ChatGPT et Gemini sont possibles. Jusqu'à 18 ans, ChatGPT demande le consentement des parents, et en France, en dessous de 15 ans, ce consentement est de toute façon nécessaire pour les services en ligne. Si l'établissement propose Gemini sur le compte scolaire, c'est souvent l'option la plus protégée."
    },
    "17-19": {
      "TITLE": "17-19 ans (lycée)",
      "WHO_I_AM": "J'ai entre 17 et 19 ans et je suis en fin de lycée.",
      "ADULTS": "un adulte de confiance, dans la famille ou en dehors",
      "OTHER_ADULT": "un prof, le CPE, l'infirmerie scolaire ou le psychologue de l'Éducation nationale",
      "HELPLINES": "le 119 (Allô Enfance en Danger, jusqu'à 18 ans, jour et nuit), ou le 3114 (prévention du suicide, gratuit, jour et nuit)",
      "HELPLINES_SHORT": "le 119 (jusqu'à 18 ans) ou le 3114",
      "ADULTS_SHORT": "un adulte de confiance",
      "WHERE": "ChatGPT (avec le consentement des parents jusqu'à 18 ans) ou Gemini ; à partir de 18 ans aussi Claude, et le choix appartient à votre enfant",
      "PLATFORM_NOTE": "Jusqu'à 18 ans, ChatGPT demande le consentement des parents. **À partir de 18 ans, c'est votre enfant qui choisit** : vous pouvez lui proposer ce texte, pas l'installer à sa place. À partir de 18 ans, il peut aussi l'utiliser dans un projet Claude."
    }
  }
}
```
