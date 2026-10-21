# Registre de travail : 05-retraites

Document interne, non publié sur le site (Bible éditoriale v1.0, chapitres 8 et 10).

- Mode : AUDIT puis RÉNOVATION (révision ciblée), 21 octobre 2026, lot 1.
- Rendu mobile : non testé (pages non régénérées, `generer.py` non lancé). Contrôle automatique : `verifier_dossier.py` OK.

## Audit classé par gravité
- BLOQUANT (résolu) : « certains économistes en concluent que le déficit réel est plus important » : affirmation importante sans source ni auteur identifié.
- MAJEUR (résolu) : le déficit 2025 présenté en [Fait établi] et qualifié de « constaté » dans la note de la figure, alors que le COR écrit qu'il « serait » de 5,1 milliards (estimation).
- MAJEUR (résolu) : figure à axe non continu (2030, 2045, 2070) non signalée en note.
- AMÉLIORATION : réforme de 2023 non expliquée ; PIB non développé ; le lien exonérations / impôts affectés non sourcé.

## Modifications
- Débat : la phrase sur « certains économistes » est remplacée par l'analyse de la Cour des comptes [3] (« autant de formules de calcul que de conventions comptables », présentations sans incidence sur la charge totale) ; ajout de la comparaison 1,29 / 2,05 cotisant par retraité (COR). Inscrit dans `corrections:`.
- Bloc solde : [Fait établi] → [Estimation], citation « serait déficitaire » ; note de la figure : « constaté » → « le COR estime », axe non continu signalé. Inscrit dans `corrections:`.
- Réforme de 2023 : « qui relevait progressivement l'âge légal de départ » (Cour des comptes : âge porté à 64 ans).
- Exonérations : appel [3] ajouté (Cour : hausse de la part des impôts affectés « notamment sous l'effet » des exonérations).
- `verifie:` 21 octobre 2026.

## Vérifications en ligne
- Synthèse du rapport annuel du COR, juin 2026 (PDF) : consultée ; conformes : 417 Md€, « serait déficitaire de 5,1 milliards », citation « tend à masquer la fragilité persistante… », 1,29 cotisant par retraité en 2020.
- Cour des comptes, février 2025 (PDF vie-publique) : consulté ; conformes : deux tiers de cotisations, 7 % → 14 % depuis 2004, passage sur les conventions de présentation.
- Non reconsultés : COR 2025, UNSA Retraités.

## Points non résolus
- Aucun bloquant. Le point de vue selon lequel le déficit serait sous-estimé n'est plus porté par une source nommée ; s'il doit être exposé, trouver une publication identifiée.

## Verdict
Publiable après les corrections faites.

## Visuels ajoutés le 21 octobre 2026

Mode : RÉNOVATION (narration visuelle). Statut : données vérifiées dans le texte (aucune donnée nouvelle ; mêmes appels de note). Test mobile : à faire (pages non régénérées, generer.py non lancé). Contrôle : verifier_dossier.py OK, rendu de la figure testé avec figures.rendre.

- V02
  - Emplacement : section « D'où vient l'argent », après le paragraphe sur le calcul de l'UNSA Retraités.
  - Question pour le lecteur : D'où viennent les ressources des retraites ?
  - Type : barres-h.
  - Informations montrées et appels de note : 65,1 %, 15 %, 11,7 %, 8,2 % pour 2024 [4] ; caractère conventionnel [1].
  - Limite : calcul syndical (source secondaire), non publié sous cette forme par le COR ; signalé dans le titre et la note.
  - Statut : données vérifiées dans le texte.
- V03
  - Emplacement : section « Le solde », après le paragraphe [Débat].
  - Question pour le lecteur : Pourquoi le COR, la Cour des comptes et un syndicat lisent-ils différemment le même solde ?
  - Type : tableau.
  - Informations montrées et appels de note : citations du COR [2], de la Cour des comptes [3] et de l'UNSA Retraités [4] déjà présentes dans le texte.
  - Limite : ne tranche pas entre les lectures ; déficit 2025 hors produits financiers.
  - Statut : données vérifiées dans le texte.
