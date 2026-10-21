# Registre de travail : 15-climat-cout

Document interne, non publié sur le site (Bible éditoriale v1.0, chapitre 8). Mode : AUDIT puis RÉNOVATION, 21 octobre 2026, lot 2. Rendu HTML non régénéré ni testé (generer.py non lancé, consigne).

## Audit
- AMÉLIORATION : les projections de France Assureurs à 2050 n'étaient pas datées ; dans l'Essentiel, le chiffre de 5,2 Md€ couvrait implicitement tous les événements naturels (dont la grêle), alors que le titre parle de canicules et sécheresses.
- AMÉLIORATION : dans le bulletin de Santé publique France, les bornes des épisodes diffèrent selon les passages (17 ou 19 juin, 20 ou 22 juillet).
- Points conformes : communiqué de Santé publique France du 22 juillet 2026 (5 764, plus de 36 %, 92 départements, 98,5 %) et bulletin du 16 septembre 2026 (817, +5,2 %, 75 ans et plus, 1 243) consultés ; France Assureurs 2025 (5,2 Md, grêle 2,2 Md, sécheresse « frôle le milliard » selon la CCR) et projections (73,4 → 143 Md, établies en 2021) consultées.

## Modifications
- Essentiel : périmètre « tous événements confondus, dont la grêle et la sécheresse ».
- Projections : « établies en 2021 ».
- [À noter] : signalement des bornes divergentes dans le bulletin.
- verifie et corrections mis à jour.

## Non résolu
- Données agricoles (Pleinchamp, info.gouv.fr), rapport Lavarde et surprime catastrophes naturelles non recontrôlés lors de ce passage.

## Verdict
Publiable.

## Visuels ajoutés le 21 octobre 2026

Mode : RÉNOVATION (narration visuelle). Rendu HTML non régénéré ni testé (generer.py non lancé, consigne) ; lecture des blocs testée avec figures.lire et figures.rendre ; verifier_dossier.py : OK.

- V01
  - Emplacement : après le [À noter] de la section « La santé ».
  - Question pour le lecteur : Quel épisode de l'été 2026 s'est accompagné du plus de décès en excès ?
  - Type : [Figure] barres-h.
  - Informations montrées et appels de note : 5 764, 1 243 et 817 décès en excès au moins, par épisode [1][2].
  - Limite : estimations préliminaires, périodes et départements différents, non additionnables ; décès en excès pas tous dus à la chaleur.
  - Statut : données vérifiées dans le texte du dossier, mêmes appels de note.

- V02
  - Emplacement : après le paragraphe sur les projections de France Assureurs.
  - Question pour le lecteur : De combien les assureurs projettent-ils la hausse des sinistres ?
  - Type : [Figure] barres (projection hachurée).
  - Informations montrées et appels de note : 73,4 milliards (1989-2019) et 143 milliards projetés (2020-2050) [4] ; chiffres revus sur la page de France Assureurs le 21 octobre 2026.
  - Limite : projection et non mesure ; euros courants ou constants non précisés par la source.
  - Statut : données vérifiées dans le texte du dossier, mêmes appels de note.

- V03
  - Emplacement : après le paragraphe sur le retrait-gonflement des argiles et la surprime.
  - Question pour le lecteur : Comment la surprime catastrophes naturelles a-t-elle changé ?
  - Type : [Figure] tableau.
  - Informations montrées et appels de note : taux de 12 à 20 % et de 6 à 9 % au 1er janvier 2025 ; 1,2 milliard attendu [6].
  - Limite : le montant de 1,2 milliard est une prévision du Gouvernement.
  - Statut : données vérifiées dans le texte du dossier, mêmes appels de note.
