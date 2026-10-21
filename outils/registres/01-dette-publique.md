# Registre de travail : 01-dette-publique

Document interne, non publié sur le site (Bible éditoriale v1.0, chapitres 8 et 10).

- Mode : AUDIT puis RÉNOVATION (révision ciblée), 21 octobre 2026, lot 1.
- Rendu mobile : non testé (pages non régénérées, `generer.py` non lancé). Contrôle automatique : `verifier_dossier.py` OK.

## Audit classé par gravité
- BLOQUANT : aucun.
- MAJEUR : aucun. Statuts globalement justes (prévisions étiquetées [Estimation], cours de marché signalés comme sources secondaires).
- AMÉLIORATION : sigle PIB non développé ; « points de base » non expliqués ; « les deux chiffres sont exacts » à propos de deux prévisions ; Essentiel n° 4 affirmant comme un fait que le risque « dépend surtout » du refinancement et de la confiance (interprétation non attribuée) ; paraphrase de l'avis du HCFP éloignée du texte (« amélioration nette » au lieu d'« évolutions conjoncturelles très favorables ») ; HCFP non présenté.
- OPTIONNEL : affirmation « le ratio français augmente de nouveau depuis 2024 [7] » non recontrôlée dans le rapport sur la dette ; chiffre du Japon (FMI via BNP Paribas, avril 2025) ancien.

## Modifications (style et pédagogie, pas de correction de fond)
- Essentiel n° 4 : « le risque dépend surtout de… » → « les analyses mettent surtout en avant… » (interprétation non présentée comme fait).
- Première occurrence : PIB développé (« produit intérieur brut, la richesse produite en un an »).
- « Les deux chiffres… sont exacts » → « Les deux prévisions… ne se contredisent pas » (une prévision n'est pas « exacte »).
- Ajout de la définition du point de base (0,01 point de pourcentage).
- Avis du HCFP : présentation de l'organisme et paraphrase alignée sur l'avis (« sauf évolutions conjoncturelles très favorables »).

## Vérifications en ligne
- France Épargne (30 septembre 2026) consulté : écart OAT-Bund franchissant 100 points de base en septembre, « une première depuis 2012 » : conforme.
- Avis HCFP n° 2026-5 (page hcfp.fr) consulté : « très peu vraisemblable… sauf évolutions conjoncturelles très favorables » : conforme.
- Non reconsultés dans cette passe : Insee IR n° 239, PLF 2027, Eurostat, rapport sur la dette, BNP Paribas, Legifiscal (vérifiés lors des passes du 13 octobre selon l'en-tête).

## Points non résolus
- Aucun bloquant.

## Verdict
Publiable.

## Visuels ajoutés le 21 octobre 2026

Mode : RÉNOVATION (narration visuelle). Statut : données vérifiées dans le texte (aucune donnée nouvelle ; mêmes appels de note). Test mobile : à faire (pages non régénérées, generer.py non lancé). Contrôle : verifier_dossier.py OK, rendu de la figure testé avec figures.rendre.

- V03
  - Emplacement : fin de « Ce que coûte la dette », après le paragraphe sur les intérêts en comptabilité nationale.
  - Question pour le lecteur : Pourquoi lit-on 72,9, 91,2 ou 3 595,5 milliards selon les articles ?
  - Type : tableau.
  - Informations montrées et appels de note : dette de Maastricht et dette nette fin juin 2026 [1], charge de la dette de l'État 2027 [2], intérêts des administrations publiques 2027 [9].
  - Limite : deux prévisions ; le chiffre de 91,2 milliards vient d'une source secondaire ; ne dit rien de la soutenabilité.
  - Statut : données vérifiées dans le texte.
- V04
  - Emplacement : section « Le débat », après le paragraphe exposant les deux positions.
  - Question pour le lecteur : Sur quoi les deux lectures du risque divergent-elles ?
  - Type : tableau.
  - Informations montrées et appels de note : arguments des deux positions tels que résumés dans le texte, ratio en hausse depuis 2024 [7], écart avec la zone euro [5].
  - Limite : simplification ; positions non attribuées à des auteurs ; ne tranche pas.
  - Statut : données vérifiées dans le texte.
