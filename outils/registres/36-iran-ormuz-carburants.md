# Registre de travail : 36-iran-ormuz-carburants

Document interne, non publié sur le site (Bible éditoriale v1.0, chapitres 8 et 10). Mode : AUDIT puis RÉNOVATION, 21 octobre 2026 (lot 4). Rendu HTML et mobile non testés (generer.py non lancé, consigne).

## Audit
- BLOQUANT : aucun.
- MAJEUR : « l'EIA les a révisées de 14 dollars en un mois » : sens et périmètre de la révision non précisés. Selon le STEO, il s'agit d'un relèvement de la seule prévision du quatrième trimestre 2026.
- MAJEUR : le bloc [Interprétation] sur les engrais présentait comme acquise une « hausse des engrais » qu'aucune source du dossier ne chiffre.
- AMÉLIORATION : l'Essentiel donnait le flux de 4,9 Mb/j comme un fait alors que le corps le classe en estimation ; titre de figure à connotation causale (« a suivi les phases de la guerre ») ; The National [8] relaie l'ONU sans être signalé comme source secondaire.
- OPTIONNEL : pas de champ corrections auparavant (créé).

## Modifications
- Essentiel : ajout « selon une estimation de l'EIA ».
- « l'EIA les a révisées de 14 dollars en un mois » → « l'EIA a relevé de 14 dollars en un mois sa prévision pour le quatrième trimestre ».
- Titre de figure → « Le prix du baril de Brent à quelques dates de la guerre ».
- Bloc engrais réécrit au conditionnel, avec la mention que les sources ne chiffrent ni le prix des engrais ni son effet.
- Source [8] : « Source secondaire : ».
- corrections: créé ; verifie: 21 octobre 2026.

## Vérifications en ligne
- EIA STEO (page global oil) : 105 $/b au 4e trimestre 2026, relevé de 14 $/b par rapport au STEO précédent ; 84 $/b en 2027 ; 131 $/b le 15 septembre après la perturbation de l'oléoduc saoudien : vérifié.
- Non revérifiés ce jour : Weekly Oil Bulletin, CRS, impots.gouv.

## Points non résolus
- Aucun bloquant.

## Verdict
Publiable.


## Visuels ajoutés le 21 octobre 2026

Mode : RÉNOVATION (narration visuelle). Les données de chaque visuel sont reprises du texte du dossier, avec les mêmes appels de note ; aucune donnée nouvelle n'a été ajoutée au texte. Rendu HTML et mobile non testés (generer.py non lancé, consigne) ; lecture du bloc par figures.lire et figures.rendre vérifiée sans erreur, verifier_dossier.py OK.

- VISUEL V04
  - Emplacement : Pourquoi le détroit compte autant, après l'estimation de l'EIA sur les flux
  - Question pour le lecteur : De combien le trafic pétrolier par Ormuz a-t-il chuté ?
  - Type : barres ([Figure] barres)
  - Information montrée et appels : 21,6 puis 4,9 millions de barils par jour, moyennes trimestrielles estimées par l'EIA [3]
  - Limite : Deux points seulement, estimations ; le relevé journalier de Kpler (autre méthode) est exclu et signalé
  - Test mobile : à faire
  - Statut : données vérifiées dans le texte

- VISUEL V05
  - Emplacement : À la pompe en France, après le paragraphe sur le sans-plomb et le fioul
  - Question pour le lecteur : Tous les carburants ont-ils augmenté de la même façon ?
  - Type : barres groupées ([Figure] groupes)
  - Information montrée et appels : Gazole, SP95, fioul, semaines du 23 février et du 12 octobre 2026 [5]
  - Limite : Deux semaines seulement ; variations intermédiaires non montrées (voir graphique du gazole)
  - Test mobile : à faire
  - Statut : données vérifiées dans le texte
