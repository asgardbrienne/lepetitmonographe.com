# Registre de travail : 22-flactif

Document interne, non publié sur le site (Bible éditoriale v1.0, chapitres 3, 7, 8, 10 et 13).

## Mode

AUDIT puis RÉNOVATION (retouche légère ou révision ciblée), 21 octobre 2026, lot 3. Dossier lu en entier ; contrôle automatique `verifier_dossier.py` : OK après modifications. Rendu HTML non généré (consigne : ne pas lancer generer.py), donc rendu mobile non testé.
## Audit classé par gravité

- BLOQUANT (résolu) : les trois coaccusés étaient dits condamnés « pour leur aide après les faits », formule que les sources ne soutiennent pas : France 3 (11 avril 2023) écrit que l'ami est « reconnu complice », ICI (11 avril 2023) que les trois sont condamnés « pour complicité ». Décrire une condamnation pour un rôle différent de celui retenu est un risque juridique (bible 6.1).
- MAJEUR (résolu) : les trois coaccusés, condamnés en 2006 à des peines de 7 à 15 ans, étaient nommés en toutes lettres ; leurs noms n'apportent rien à la compréhension et touchent à la vie privée de personnes condamnées il y a vingt ans (bible 6.1, personnes vivantes, condamnés libérés probables mais non vérifiés).
- AMÉLIORATION : « Le couple avait donné des interviews », ambigu (quel couple ?).
- OPTIONNEL : qualification exacte (meurtres ou assassinats) toujours non vérifiée dans l'arrêt, signalée.

## Modifications faites

| Avant | Après | Motif |
|---|---|---|
| Essentiel : « condamnées à 15, 10 et 7 ans pour leur participation après les faits » | « sa compagne et un couple d'amis, […] pour complicité, selon la presse » | Conformité aux sources [1][2] vues en ligne |
| Corps : noms des trois coaccusés et « pour leur aide après les faits » | « l'ami de l'accusé », « la compagne de cet ami », « la compagne de l'accusé », condamnés « pour complicité, selon les comptes rendus de presse » ; mention qu'ils ne sont pas nommés | Exactitude et vie privée |
| « Le couple avait par ailleurs donné des interviews » | « L'accusé et sa compagne avaient… » | Clarté (source ICI) |
| « ses coaccusés pour leur aide » | « pour complicité, selon la presse » | Cohérence |
| « au 13 octobre 2026 » | « dernière recherche le 21 octobre 2026 » | Actualisation de l'état de la procédure |

Champs `corrections` et `verifie` mis à jour.

## Vérifications en ligne

- France 3 Hauts-de-France et ICI (11 avril 2023) consultés : peines (perpétuité avec 22 ans de sûreté ; 15, 10 et 7 ans) et mention « complicité » confirmées.
- Page de la gendarmerie : erreur 403, non consultée.
- Recherche du 21 octobre 2026 : aucune décision publiée sur la demande de libération conditionnelle.

## Points non résolus

- Qualifications exactes (meurtres ou assassinats ; nature de la complicité) : arrêt non accessible.

## Verdict

Publiable après les corrections faites.

## Visuels ajoutés le 21 octobre 2026

Mode RÉNOVATION (narration visuelle). Chaque visuel ne reprend que des éléments déjà présents et sourcés dans le texte du dossier, avec les mêmes appels de note ; aucune donnée nouvelle n'a été ajoutée au texte. Rendu non testé (generer.py non lancé, conformément à la consigne) ; lecture du bloc vérifiée avec figures.lire et figures.rendre, contrôle verifier_dossier.py OK.

### V01 : Où en est la demande de libération conditionnelle

- EMPLACEMENT : fin de « La procédure expliquée ».
- QUESTION POUR LE LECTEUR : Par quelles étapes passe la demande de 2025 et où en est-elle ?
- TYPE : schéma en étapes, 5 lignes.
- INFORMATION MONTRÉE ET APPELS DE NOTE : La demande a été déposée en septembre 2025 ; son examen par le tribunal suppose d'abord une expertise et une évaluation de dangerosité. Appels : [2][3].
- LIMITE : Les étapes 3 et 4 sont celles que décrit le parquet de Nancy [3] ; leur avancement réel depuis mars 2026 n'est pas connu.
- ALTERNATIVE TEXTUELLE : schéma rendu en HTML (liste ou tableau), lisible par les lecteurs d'écran ; pas d'image.
- TEST MOBILE : à faire après génération.
- STATUT : données vérifiées dans le texte du dossier (pas de nouvelle source consultée).

### V02 : Peines et qualification : ce que disent les sources

- EMPLACEMENT : après l'encadré « Les sources ne concordent pas toutes ».
- QUESTION POUR LE LECTEUR : Pourquoi le dossier retient 22 ans de sûreté et 15, 10 et 7 ans pour les coaccusés ?
- TYPE : tableau comparatif (Point | Comptes rendus d'audience et dépêches | Page de la gendarmerie | Ce que retient ce dossier), 3 lignes.
- INFORMATION MONTRÉE ET APPELS DE NOTE : Les comptes rendus d'audience et les dépêches concordent sur 22 ans de sûreté et sur des peines de 15, 10 et 7 ans ; la page de la gendarmerie, qui reprend un récit du site Les Jours, donne d'autres chiffres. Appels : [1][2][3][4][5][8].
- LIMITE : Schéma limité aux éléments cités dans le dossier.
- ALTERNATIVE TEXTUELLE : schéma rendu en HTML (liste ou tableau), lisible par les lecteurs d'écran ; pas d'image.
- TEST MOBILE : à faire après génération.
- STATUT : données vérifiées dans le texte du dossier (pas de nouvelle source consultée).

### V03 : La version de l'accusé et ce qu'en disent les expertises

- EMPLACEMENT : « Versions de l'accusé et expertises », après l'interprétation sur le seul auteur.
- QUESTION POUR LE LECTEUR : En quoi la version des aveux diffère-t-elle de la reconstitution des experts ?
- TYPE : tableau comparatif (Point | Déclarations de l'accusé | Expertises et décision), 2 lignes.
- INFORMATION MONTRÉE ET APPELS DE NOTE : Les expertises citées par la gendarmerie ne confirment pas la version donnée par l'accusé lors de ses aveux ; il a refusé de s'expliquer au procès. Appels : [2][5][9].
- LIMITE : L'arrêt n'a pas été consulté : le déroulement retenu par la cour n'est connu que par la presse et par la gendarmerie. L'ordre des faits est une reconstitution d'expertise.
- ALTERNATIVE TEXTUELLE : schéma rendu en HTML (liste ou tableau), lisible par les lecteurs d'écran ; pas d'image.
- TEST MOBILE : à faire après génération.
- STATUT : données vérifiées dans le texte du dossier (pas de nouvelle source consultée).
