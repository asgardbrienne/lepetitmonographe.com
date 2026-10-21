# Registre de travail : 10-ia-emploi

Document interne, non publié sur le site (Bible éditoriale v1.0, chapitre 8). Mode : AUDIT puis RÉNOVATION, 21 octobre 2026, lot 2. Rendu HTML non régénéré ni testé (generer.py non lancé, consigne).

## Audit
- BLOQUANT : l'étude sur les embauches de jeunes était présentée en [Fait établi] alors que seule une reprise de presse avait été lue, et attribuée à « la Banque de France et HEC Paris » ; date d'arrêt (8 octobre) antérieure à la source citée (12 octobre).
- MAJEUR : la réserve « l'IA ne peut être tenue pour seule responsable » venait de la presse, pas des auteurs ; les autres explications examinées par l'étude n'étaient pas citées.
- AMÉLIORATION : champ des données (MMO, secteur privé, hors intérim) absent.
- Points conformes : Coface/OEM (923 professions, 16 %, citation « ne préjuge nullement... », tâches cognitives et qualifiées) vérifiés sur la page Coface ; Aghion et al. (120 millions d'offres, informatique/finance/conseil, hausse de l'emploi total) vérifiés sur le PDF.

## Modifications
- Étude LIFT consultée (PDF, Policy Paper 2026-02, octobre 2026) et ajoutée en source [5] ; attribution corrigée (LIFT d'HEC Paris, en collaboration avec la Banque de France ; le document précise n'engager que ses auteurs) ; titre réel, auteurs, 28,3 %, champ des données, « moins de 4 points après 50 ans ».
- Interprétation : « Les chercheurs rappellent... seule responsable [4] » → résultats qualifiés de « descriptifs » par les auteurs et trois explications alternatives (cycle, télétravail, apprentissage) [5].
- Entreprises utilisatrices : ajout de la réserve des auteurs (un recul de 2 à 3 % ne peut être distingué de zéro).
- « 75 000 CDI » : ordre de grandeur calculé par les auteurs [4][5].
- arret et resume : 8 → 21 octobre 2026 ; verifie : 21 octobre 2026 ; phrase datée dans corrections.

## Non résolu
- La CFE-CGC (5 millions de postes) n'a pas été recontrôlée. Le billet de la Banque de France n'a pas été consulté.

## Verdict
Publiable.

## Visuels ajoutés le 21 octobre 2026

Mode : RÉNOVATION (narration visuelle). Rendu HTML non régénéré ni testé (generer.py non lancé, consigne) ; lecture des blocs testée avec figures.lire et figures.rendre ; verifier_dossier.py : OK.

- V01
  - Emplacement : après le paragraphe [Estimation] Coface et OEM (section « Exposition, transformation, suppression »).
  - Question pour le lecteur : Que mesure exactement le chiffre de 16 % ?
  - Type : [Figure] tableau.
  - Informations montrées et appels de note : définitions des trois notions ; 16 % du contenu du travail potentiellement automatisable ; citation « ne préjuge nullement » [1].
  - Limite : la transformation n'est pas chiffrée dans le dossier ; le tableau ne mesure aucun effet sur l'emploi.
  - Statut : données vérifiées dans le texte du dossier, mêmes appels de note.

- V02
  - Emplacement : après le paragraphe [Fait établi] sur l'étude du LIFT.
  - Question pour le lecteur : Le recul des embauches de jeunes est-il plus fort dans les métiers exposés ?
  - Type : [Figure] groupes (barres horizontales, valeurs négatives).
  - Informations montrées et appels de note : embauches en CDI -28,3 % / -7,5 % ; fins de CDI environ -23 % / -6 % ; 21-29 ans, mars 2026 par rapport à novembre 2022 [5].
  - Limite : résultats descriptifs, pas de causalité ; valeurs des fins de CDI approchées. Donnée précisée dans le texte : la période des fins de CDI (même période que les embauches), vérifiée le 21 octobre 2026 dans le PDF du LIFT (p. 1 et 4), phrase ajoutée dans corrections.
  - Statut : données vérifiées dans le texte du dossier, mêmes appels de note.
