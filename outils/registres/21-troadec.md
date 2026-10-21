# Registre de travail : 21-troadec

Document interne, non publié sur le site (Bible éditoriale v1.0, chapitres 3, 7, 8, 10 et 13).

## Mode

AUDIT puis RÉNOVATION (retouche légère ou révision ciblée), 21 octobre 2026, lot 3. Dossier lu en entier ; contrôle automatique `verifier_dossier.py` : OK après modifications. Rendu HTML non généré (consigne : ne pas lancer generer.py), donc rendu mobile non testé.
## Audit classé par gravité

- BLOQUANT : aucun. Condamnation, peine, absence d'appel pénal, appel civil et altération du discernement présentés avec leur portée exacte ; fils victime traité avec soin ; préméditation non insinuée (meurtres, pas assassinats).
- MAJEUR : incohérence de date sur les aveux (5 mars dans le texte, « 5 ou 6 mars selon les sources » dans la frise).
- AMÉLIORATION : « arrêt de mise en accusation » au lieu d'« ordonnance de mise en accusation », contradictoire avec un autre passage ; état de la procédure sans repère temporel.
- OPTIONNEL : toutes les sources sont secondaires (presse), faute d'arrêt publié ; c'est signalé.

## Modifications faites

| Avant | Après | Motif |
|---|---|---|
| « L'aveu du beau-frère, le 5 mars 2017, met fin à cette piste [14] » | « Les aveux du beau-frère, le 5 ou le 6 mars 2017 selon les sources, mettent fin à cette piste [9][10][14] » | Cohérence avec la chronologie et les sources |
| « l'arrêt de mise en accusation » | « l'ordonnance de mise en accusation » | Cohérence procédurale interne |
| « Les sources consultées ne font état… » | « À la date d'arrêt des données, les sources consultées… » | Dater l'état de la procédure (bible 6.1) |

Champs `corrections` et `verifie` mis à jour.

## Vérifications en ligne

Aucune vérification nouvelle des chiffres (30 ans, sûreté légale de 15 ans, trois ans dont un avec sursis) : ils sont déjà attribués à des comptes rendus identifiés. Pas de recherche nouvelle sur l'appel civil.

## Points non résolus

- Issue de l'appel civil et date de l'ordonnance de mise en accusation, inconnues et signalées.
- La compagne condamnée (trois ans, dont un avec sursis, 2021) n'est pas nommée dans le texte, ce qui convient ; son nom figure dans le titre d'une source, sans incidence.

## Verdict

Publiable.

## Visuels ajoutés le 21 octobre 2026

Mode RÉNOVATION (narration visuelle). Chaque visuel ne reprend que des éléments déjà présents et sourcés dans le texte du dossier, avec les mêmes appels de note ; aucune donnée nouvelle n'a été ajoutée au texte. Rendu non testé (generer.py non lancé, conformément à la consigne) ; lecture du bloc vérifiée avec figures.lire et figures.rendre, contrôle verifier_dossier.py OK.

### V01 : De la mise en examen au verdict : qualifications et peines

- EMPLACEMENT : fin de « Les faits jugés ».
- QUESTION POUR LE LECTEUR : Comment la qualification et la peine ont-elles évolué entre la mise en examen et le verdict, pour chacun des deux accusés ?
- TYPE : tableau comparatif (Étape | Le principal accusé | Sa compagne), 5 lignes.
- INFORMATION MONTRÉE ET APPELS DE NOTE : Mis en examen pour assassinats, le principal accusé a été renvoyé et condamné pour meurtres, qualification sans préméditation ; la peine prononcée est inférieure aux réquisitions. Appels : [1][2][3][4][5][6][7][9][10][13].
- LIMITE : Ni l'ordonnance de mise en accusation ni l'arrêt de la cour d'assises n'ont été consultés : les qualifications sont celles que rapporte la presse.
- ALTERNATIVE TEXTUELLE : schéma rendu en HTML (liste ou tableau), lisible par les lecteurs d'écran ; pas d'image.
- TEST MOBILE : à faire après génération.
- STATUT : données vérifiées dans le texte du dossier (pas de nouvelle source consultée).

### V02 : Les déclarations de l'accusé et les éléments de l'enquête

- EMPLACEMENT : fin de « Ce qui est resté contesté ».
- QUESTION POUR LE LECTEUR : Qu'a déclaré l'accusé, et qu'ont relevé l'enquête et les expertises sur chaque point ?
- TYPE : tableau comparatif (Point | Déclarations de l'accusé | Éléments de l'enquête et expertises), 4 lignes.
- INFORMATION MONTRÉE ET APPELS DE NOTE : La préméditation, contestée par l'accusé, n'a pas été retenue ; ses autres déclarations ont été confrontées à des éléments matériels et à des expertises qui ne les confirment pas. Appels : [1][8][9][10][11][12].
- LIMITE : Le déroulement exact des faits n'a pas été établi : l'avocat général a déclaré à l'audience qu'on ne savait « même pas de quoi ils sont morts » [5]. Une expertise éclaire la cour sans la lier.
- ALTERNATIVE TEXTUELLE : schéma rendu en HTML (liste ou tableau), lisible par les lecteurs d'écran ; pas d'image.
- TEST MOBILE : à faire après génération.
- STATUT : données vérifiées dans le texte du dossier (pas de nouvelle source consultée).
