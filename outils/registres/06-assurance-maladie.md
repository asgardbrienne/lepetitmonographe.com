# Registre de travail : 06-assurance-maladie

Document interne, non publié sur le site (Bible éditoriale v1.0, chapitres 8 et 10).

- Mode : AUDIT puis RÉNOVATION (révision ciblée), 21 octobre 2026, lot 1.
- Rendu mobile : non testé (pages non régénérées, `generer.py` non lancé). Contrôle automatique : `verifier_dossier.py` OK.

## Audit classé par gravité
- BLOQUANT : aucun.
- MAJEUR (résolu) : 11,3 milliards (régime général, IJ maladie) et 17,9 milliards (Cour, ensemble des IJ des soins de ville) juxtaposés sans signaler la différence de périmètre.
- MAJEUR (résolu) : Légifiscal et Banque des Territoires, qui rapportent des textes officiels, non signalés comme sources secondaires.
- AMÉLIORATION : la somme des sous-objectifs de l'Ondam n'atteint pas le total sans explication.
- OPTIONNEL : la description (« augmentent si vite ») est un peu appuyée ; champ protégé, non modifié.

## Modifications
- Ajout d'une phrase de périmètre sur 11,3 / 17,9 milliards.
- Mention des autres sous-objectifs de l'Ondam (dont le fonds d'intervention régional).
- Sources 5 et 6 : préfixe « Source secondaire : ».
- Pas de correction de fond : `corrections:` et `verifie:` inchangés.

## Vérifications en ligne
- Aucune source de ce dossier n'a été reconsultée dans cette passe. Les montants de l'Ondam, de la Cour et de la DSS reposent sur la vérification du 13 octobre (en-tête). Le chiffre de 49 M€ (arrêts de travail) est confirmé par le communiqué des ministères du 8 avril 2026, consulté pour le dossier 04.

## Points non résolus
- Aucun bloquant.

## Verdict
Publiable.

## Visuels ajoutés le 21 octobre 2026

Mode : RÉNOVATION (narration visuelle). Statut : données vérifiées dans le texte (aucune donnée nouvelle ; mêmes appels de note). Test mobile : à faire (pages non régénérées, generer.py non lancé). Contrôle : verifier_dossier.py OK, rendu de la figure testé avec figures.rendre.

- V01
  - Emplacement : section « Où va l'argent », après le paragraphe sur l'Ondam 2027.
  - Question pour le lecteur : Comment se répartit l'Ondam et comment évolue-t-il entre 2026 et 2027 ?
  - Type : groupes.
  - Informations montrées et appels de note : quatre sous-objectifs, loi pour 2026 [5] et projet pour 2027 [1].
  - Limite : 2026 = loi initiale (objectif total révisé depuis, révision par sous-objectif non disponible) ; 2027 = projet ; autres sous-objectifs non représentés ; source secondaire pour 2026.
  - Statut : données vérifiées dans le texte.
- V02
  - Emplacement : section « Les arrêts de travail », après le paragraphe sur 2014-2019 et 2019-2025.
  - Question pour le lecteur : Les dépenses d'arrêts maladie accélèrent-elles depuis la crise sanitaire ?
  - Type : groupes.
  - Informations montrées et appels de note : 3,7 et 4,4 % par an (moins de trois mois), 4,1 et 6,7 % (plus de trois mois) [3].
  - Limite : dépenses en euros : effet salaires et effet volume non séparés ; aucune cause montrée.
  - Statut : données vérifiées dans le texte.
