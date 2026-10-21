# Registre de travail : 27-romand

Document interne, non publié sur le site (Bible éditoriale v1.0, chapitres 3, 7, 8, 10 et 13).

## Mode

AUDIT puis RÉNOVATION (retouche légère ou révision ciblée), 21 octobre 2026, lot 3. Dossier lu en entier ; contrôle automatique `verifier_dossier.py` : OK après modifications. Rendu HTML non généré (consigne : ne pas lancer generer.py), donc rendu mobile non testé.
## Audit classé par gravité

- BLOQUANT : aucun. Condamnation définitive, absence d'appel en 1996, absence de motivation, expertises judiciaires attribuées (pas de diagnostic à distance par le site), libération conditionnelle de 2019 décrite avec ses motifs publiés.
- MAJEUR (résolu) : l'état de la procédure affirmait au présent que le condamné « bénéficie » des obligations de 2019, sans vérification actuelle (bible 6.1, condamné libéré).
- MAJEUR (résolu) : dix sources de presse non signalées comme secondaires.
- AMÉLIORATION : phrase sur la CEDH (« a rappelé […] a rappelé ») maladroite et trop générale ; reformulée en distinguant l'argument (réexamen d'une perpétuité) de sa présentation par Slate.
- OPTIONNEL : montant de 3 millions d'euros attribué à Europe 1, sans source judiciaire, déjà signalé.

## Modifications faites

| Avant | Après | Motif |
|---|---|---|
| « Le condamné bénéficie depuis 2019 d'une libération conditionnelle, qui comporte… » | « a obtenu en 2019 une libération conditionnelle qui comporte notamment, selon le communiqué du parquet général de Bourges, … Nous n'avons pas vérifié l'exécution actuelle de cette mesure » | Ne pas affirmer une situation actuelle non vérifiée |
| Phrase CEDH | « L'argument juridique général est qu'une peine perpétuelle doit pouvoir être réexaminée : selon Slate, la CEDH a rappelé en 2014… » | Clarté et attribution |
| Sources 1 à 9 et 13 | Préfixe « Source secondaire : » | Règle de signalement |

Pas de correction factuelle : `corrections` et `verifie` inchangés.

## Vérifications en ligne

- Article de Slate (source 8) : erreur 403, non consulté ; la référence à une décision de la CEDH de 2014 reste attribuée à Slate sans vérification de la décision elle-même.

## Points non résolus

- Décision de la CEDH de 2014 évoquée par Slate non identifiée (non bloquant, attribuée).

## Verdict

Publiable.

## Visuels ajoutés le 21 octobre 2026

Mode RÉNOVATION (narration visuelle). Chaque visuel ne reprend que des éléments déjà présents et sourcés dans le texte du dossier, avec les mêmes appels de note ; aucune donnée nouvelle n'a été ajoutée au texte. Rendu non testé (generer.py non lancé, conformément à la consigne) ; lecture du bloc vérifiée avec figures.lire et figures.rendre, contrôle verifier_dossier.py OK.

### V01 : Le procès de 1996 et les règles adoptées depuis

- EMPLACEMENT : fin de « La procédure de 1996 expliquée ».
- QUESTION POUR LE LECTEUR : Pourquoi le verdict de 1996 n'a-t-il ni appel ni motivation ?
- TYPE : tableau comparatif (Règle | En 1996 | Depuis les réformes), 2 lignes.
- INFORMATION MONTRÉE ET APPELS DE NOTE : Le verdict de 1996 ne pouvait pas être rejugé en appel et n'était pas motivé : aucun document n'explique quels arguments la cour a retenus. Appels : [12].
- LIMITE : Ces réformes générales ne s'appliquaient pas à ce procès [12]. Nous n'avons pas trouvé de source indiquant si un pourvoi a été formé.
- ALTERNATIVE TEXTUELLE : schéma rendu en HTML (liste ou tableau), lisible par les lecteurs d'écran ; pas d'image.
- TEST MOBILE : à faire après génération.
- STATUT : données vérifiées dans le texte du dossier (pas de nouvelle source consultée).

### V02 : Ce que soutenaient l'accusation, la défense et les experts en 1996

- EMPLACEMENT : fin de « Accusation, défense, expertises ».
- QUESTION POUR LE LECTEUR : Sur quoi portait le débat du procès, puisque les faits n'étaient pas contestés ?
- TYPE : tableau comparatif (Acteur | Position rapportée | Sur quoi elle s'appuie), 5 lignes.
- INFORMATION MONTRÉE ET APPELS DE NOTE : Les faits n'étaient pas contestés ; le débat portait sur la préméditation, la sincérité de la tentative de suicide et la responsabilité pénale. Appels : [2][5][6][8][12].
- LIMITE : Positions résumées à partir de comptes rendus de presse ; l'arrêt et les rapports d'expertise n'ont pas été consultés.
- ALTERNATIVE TEXTUELLE : schéma rendu en HTML (liste ou tableau), lisible par les lecteurs d'écran ; pas d'image.
- TEST MOBILE : à faire après génération.
- STATUT : données vérifiées dans le texte du dossier (pas de nouvelle source consultée).

### V03 : Libération conditionnelle d'un condamné à perpétuité : avant et après la loi du 23 mars 2019

- EMPLACEMENT : « Comment un condamné à perpétuité peut être libéré », après le premier paragraphe.
- QUESTION POUR LE LECTEUR : Quelles étapes précèdent la libération conditionnelle d'un condamné à perpétuité, et qu'a changé la loi de 2019 ?
- TYPE : tableau comparatif (Étape | Régime des lois de 2008 et 2011 | Depuis la loi du 23 mars 2019), 3 lignes.
- INFORMATION MONTRÉE ET APPELS DE NOTE : La loi du 23 mars 2019 a supprimé l'avis de la commission pluridisciplinaire, mais maintenu l'évaluation de dangerosité avant toute libération conditionnelle. Appels : [11].
- LIMITE : Les sources consultées ne disent pas quelle version de la procédure a été appliquée à la demande déposée en septembre 2018 [2][11]. En appel, c'est la chambre de l'application des peines qui statue [1].
- ALTERNATIVE TEXTUELLE : schéma rendu en HTML (liste ou tableau), lisible par les lecteurs d'écran ; pas d'image.
- TEST MOBILE : à faire après génération.
- STATUT : données vérifiées dans le texte du dossier (pas de nouvelle source consultée).
