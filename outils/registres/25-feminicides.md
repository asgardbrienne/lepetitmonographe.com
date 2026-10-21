# Registre de travail : 25-feminicides

Document interne, non publié sur le site (Bible éditoriale v1.0, chapitres 3, 7, 8, 10 et 13).

## Mode

AUDIT puis RÉNOVATION (retouche légère ou révision ciblée), 21 octobre 2026, lot 3. Dossier lu en entier ; contrôle automatique `verifier_dossier.py` : OK après modifications. Rendu HTML non généré (consigne : ne pas lancer generer.py), donc rendu mobile non testé.
## Audit classé par gravité

- BLOQUANT (résolu) : le dossier affirmait que l'étude 2025 du ministère de l'Intérieur n'était pas publiée et rangeait « le chiffre officiel pour 2025 » dans « Ce qu'on ne sait pas ». Or l'étude a été rendue publique à la mi-octobre 2026 (111 femmes et 25 hommes tués au sein du couple en 2025, 136 au total), selon Euronews (15 octobre 2026) et l'AIP (15 octobre 2026, reprenant l'AFP). Information périmée dans l'Essentiel.
- MAJEUR (résolu) : « Ce qu'on ne sait pas » disait ne pas savoir si les victimes avaient signalé les violences, alors que le corps donne 37 signalements sur 50 : contradiction interne.
- MAJEUR (résolu) : quatre sources secondaires (Banque des territoires, Weka, Le Club des juristes, LCP) n'étaient pas signalées comme telles.
- AMÉLIORATION : aucune autre ; distinctions entre méthodes (Intérieur, Justice, collectifs, ONUDC) déjà soigneusement faites, figures conformes (base zéro, champ, source, note de limite).

## Modifications faites

| Avant | Après | Motif |
|---|---|---|
| Essentiel : « l'étude annuelle […] n'était pas publiée au 16 octobre 2026 » | Étude publiée mi-octobre 2026 : 111 femmes tuées, contre 107 en 2024, selon la presse ; rappel du décompte Justice (96) et de sa méthode propre | Information périmée |
| (absent) | Nouveau paragraphe : chiffres 2025 attribués à la presse, divergence sur les tentatives (445 ou 435), étude elle-même non consultée, série et graphiques arrêtés à 2024 | Traçabilité et honnêteté sur la source |
| Ce qu'on ne sait pas : « Le chiffre officiel pour 2025 » | « Le détail de l'étude 2025 », non consultée directement | Mise à jour |
| Ce qu'on ne sait pas : part des victimes « connues des services » | Reformulé avec les 37 signalements sur 50 et la limite réelle (violences non mises au jour) | Contradiction interne |
| Sources 7, 8, 10, 12 | Préfixe « Source secondaire : » | Règle de signalement |
| (absent) | Sources 13 (Euronews) et 14 (AIP), ajoutées en fin de liste (pas de renumérotation) | Sourcer l'ajout |

Champs `corrections` et `verifie` mis à jour.

## Vérifications en ligne

- Euronews, 15 octobre 2026, et AIP, 15 octobre 2026 : chiffres 111, 25 et 136 concordants ; tentatives divergentes.
- Page de l'étude sur interieur.gouv.fr : erreur 403 (WebFetch et curl), non consultée.

## Points non résolus

- Les chiffres 2025 reposent sur deux sources secondaires concordantes ; à remplacer par l'étude primaire du ministère dès qu'elle sera consultable, et la série graphique pourra alors être prolongée à 2025.

## Verdict

Publiable après les corrections faites (chiffres 2025 explicitement présentés comme rapportés par la presse).
