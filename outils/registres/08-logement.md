# Registre de travail : 08-logement

Document interne, non publié sur le site (Bible éditoriale v1.0, chapitres 8 et 10).

- Mode : AUDIT puis RÉNOVATION (révision ciblée), 21 octobre 2026, lot 1.
- Rendu mobile : non testé (pages non régénérées, `generer.py` non lancé). Contrôle automatique : `verifier_dossier.py` OK.

## Audit classé par gravité
- BLOQUANT : aucun.
- MAJEUR (non résolu, structure) : le titre « pourquoi il reste cher malgré 46 milliards d'aides » présuppose (a) que le logement est cher, sans indicateur sourcé dans le corps (taux d'effort, prix rapportés aux revenus), et (b) que les aides devraient faire baisser les prix, alors que le débat présenté suggère l'inverse. Titre conservé (consigne) ; à revoir par l'autrice.
- MAJEUR (résolu) : bloc [Interprétation] des causes sans attribution ni source.
- AMÉLIORATION : sigles APL, ALS, ALF non développés (APL désigne aussi un autre indicateur dans le dossier 07) ; chapô « le crédit renchérit » plus fort que les données (3,27 → 3,30 %).

## Modifications
- Chapô : « le crédit renchérit » → « renchérit un peu ».
- Aides personnelles développées en toutes lettres.
- Bloc des causes : précise qu'il s'agit d'explications avancées dans le débat public, dont le poids respectif n'est pas établi.
- Pas de correction de fond.

## Vérifications en ligne
- Aucune source reconsultée dans cette passe (vérification du 13 octobre selon l'en-tête).

## Points non résolus
- Ajouter un indicateur sourcé du coût du logement pour les ménages (compte du logement, Insee) ou adapter le titre.

## Verdict
Publiable ; amélioration du titre recommandée.

## Visuels ajoutés le 21 octobre 2026

Mode : RÉNOVATION (narration visuelle). Statut : données vérifiées dans le texte (aucune donnée nouvelle ; mêmes appels de note). Test mobile : à faire (pages non régénérées, generer.py non lancé). Contrôle : verifier_dossier.py OK, rendu de la figure testé avec figures.rendre.

- V02
  - Emplacement : section « Les prix, les loyers et le crédit », après le paragraphe sur l'indice Notaires-Insee.
  - Question pour le lecteur : Les prix baissent-ils de la même façon pour les maisons et les appartements ?
  - Type : barres-h.
  - Informations montrées et appels de note : -1,3 %, -0,1 %, -0,8 % sur un an au deuxième trimestre 2026 [2].
  - Limite : données provisoires ; un seul trimestre.
  - Statut : données vérifiées dans le texte.
- V03
  - Emplacement : même section, après le paragraphe sur les loyers.
  - Question pour le lecteur : Les loyers ont-ils augmenté autant dans le parc libre et dans le parc social ?
  - Type : barres-h.
  - Informations montrées et appels de note : +1,5 % secteur libre, +3,9 % secteur social en 2025 [1].
  - Limite : ensemble des baux, pas les nouveaux baux ; une seule année.
  - Statut : données vérifiées dans le texte.
