# Registre de travail : 30-igpn

Document interne, non publié sur le site (Bible éditoriale v1.0, chapitres 8 et 10). Mode : AUDIT puis RÉNOVATION, 21 octobre 2026 (lot 4). Rendu HTML et mobile non testés (generer.py non lancé, consigne).

## Audit
- BLOQUANT : aucun.
- MAJEUR : lecture du graphique des tirs sur véhicules (« culmine en 2017 ») alors que 2018 et 2019 manquent : affirmation non démontrée et rapprochement implicite avec la loi de 2017.
- MAJEUR : hausse des saisines probité donnée à « 45 % » ; 341/234 = +45,7 %, soit environ 46 % (franceinfo écrit 45 % et ne donne pas les effectifs).
- AMÉLIORATION : franceinfo [1] et LCP [10] relaient un rapport (IGPN, mission d'information) sans être signalés comme sources secondaires, alors que la légende de figure parle déjà de « sources secondaires ».
- OPTIONNEL : le reste est rigoureux (distinction enquête/sanction, limites des séries, débat loi 2017 équilibré).

## Modifications
- Essentiel et lecture de figure : « soit une hausse de 45 % » → « environ 46 % (45 % selon franceinfo) » / « environ 46 % » (calcul).
- Lecture figure tirs : « culmine en 2017… puis recule » → « Parmi les années disponibles, le plus élevé est 2017… Les années 2018 et 2019 manquent : on ne peut pas dire si 2017 est un sommet. »
- Sources [1] et [10] : préfixe « Source secondaire : ».
- corrections: et verifie: mis à jour.

## Vérifications en ligne
- franceinfo, 23 septembre 2026 : 1 007 enquêtes, 322 usage de la force (428, 519, 868), « plus bas depuis 2015 », « augmenté de 45 % », 235 enquêtes probité : confirmés. Les effectifs 341 et 234 ne figurent pas sur la page (repris de l'AFP [2], non revérifiée ce jour).

## Points non résolus
- Rapport annuel IGPN 2025 introuvable en ligne (déjà signalé dans le texte).

## Verdict
Publiable.


## Visuels ajoutés le 21 octobre 2026

Mode : RÉNOVATION (narration visuelle). Les données de chaque visuel sont reprises du texte du dossier, avec les mêmes appels de note ; aucune donnée nouvelle n'a été ajoutée au texte. Rendu HTML et mobile non testés (generer.py non lancé, consigne) ; lecture du bloc par figures.lire et figures.rendre vérifiée sans erreur, verifier_dossier.py OK.

- VISUEL V05
  - Emplacement : Comment fonctionne l'IGPN, après l'encadré « À noter » sur les deux types d'enquêtes
  - Question pour le lecteur : Qui saisit l'IGPN et qui décide des suites ?
  - Type : arbre ([Figure] arbre)
  - Information montrée et appels : Enquête judiciaire confiée par un magistrat ; enquête administrative demandée par le ministre, le DGPN ou le préfet de police ; l'IGPN propose, le DGPN ou le préfet décide [7]
  - Limite : Simplifié : exceptions d'auto-saisine et part de 10 % des enquêtes administratives données en note ; les suites judiciaires viennent de l'encadré, sans appel de note
  - Test mobile : à faire
  - Statut : données vérifiées dans le texte

- VISUEL V06
  - Emplacement : Des enquêtes aux sanctions, après le paragraphe sur les propositions de 2024
  - Question pour le lecteur : Que propose l'IGPN pour les agents visés ?
  - Type : barres horizontales ([Figure] barres-h)
  - Information montrée et appels : 89 classements, 90 sanctions du premier groupe, 85 renvois en conseil de discipline en 2024 [7]
  - Limite : Propositions, pas sanctions prononcées ; 23 agents pour lesquels le DGPN n'a pas suivi
  - Test mobile : à faire
  - Statut : données vérifiées dans le texte
