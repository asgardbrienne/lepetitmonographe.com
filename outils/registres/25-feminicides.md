# Registre de travail : 25-feminicides

Document interne, non publié sur le site (Bible éditoriale v1.0, chapitres 3, 7, 8, 10 et 13).

## Mode

AUDIT puis RÉNOVATION (retouche légère ou révision ciblée), 21 octobre 2026, lot 3. Dossier lu en entier ; contrôle automatique `verifier_dossier.py` : OK après modifications. Rendu HTML non généré (consigne : ne pas lancer generer.py), donc rendu mobile non testé.
## Audit classé par gravité

- BLOQUANT (résolu) : le dossier affirmait que l'étude 2025 du ministère de l'Intérieur n'était pas publiée et rangeait « le chiffre officiel pour 2025 » dans « Ce qu'on ne sait pas ». Or l'étude a été rendue publique à la mi-octobre 2026 (111 femmes et 25 hommes tués au sein du couple en 2025, 136 au total), selon Euronews (15 octobre 2026) et l'AIP (15 octobre 2026, reprenant l'AFP). Information périmée dans l'Essentiel.
- MAJEUR (résolu) : « Ce qu'on ne sait pas » disait ne pas savoir si les victimes avaient signalé les violences, alors que le corps donne 37 signalements sur 50 : contradiction interne.
- MAJEUR (résolu) : quatre sources secondaires (Banque des territoires, Weka, Le Club des juristes, LCP) n'étaient pas signalées comme telles.
- AMÉLIORATION : aucune autre ; distinctions entre méthodes (Intérieur, Justice, collectifs, ONUDC) déjà soigneusement faites, figures conformes (base zéro, champ, source, note de limite).

## Modifications faites

| Avant | Après | Motif |
|---|---|---|
| Essentiel : « l'étude annuelle […] n'était pas publiée au 16 octobre 2026 » | Étude publiée mi-octobre 2026 : 111 femmes tuées, contre 107 en 2024, selon la presse ; rappel du décompte Justice (96) et de sa méthode propre | Information périmée |
| (absent) | Nouveau paragraphe : chiffres 2025 attribués à la presse, divergence sur les tentatives (445 ou 435), étude elle-même non consultée, série et graphiques arrêtés à 2024 | Traçabilité et honnêteté sur la source |
| Ce qu'on ne sait pas : « Le chiffre officiel pour 2025 » | « Le détail de l'étude 2025 », non consultée directement | Mise à jour |
| Ce qu'on ne sait pas : part des victimes « connues des services » | Reformulé avec les 37 signalements sur 50 et la limite réelle (violences non mises au jour) | Contradiction interne |
| Sources 7, 8, 10, 12 | Préfixe « Source secondaire : » | Règle de signalement |
| (absent) | Sources 13 (Euronews) et 14 (AIP), ajoutées en fin de liste (pas de renumérotation) | Sourcer l'ajout |

Champs `corrections` et `verifie` mis à jour.

## Vérifications en ligne

- Euronews, 15 octobre 2026, et AIP, 15 octobre 2026 : chiffres 111, 25 et 136 concordants ; tentatives divergentes.
- Page de l'étude sur interieur.gouv.fr : erreur 403 (WebFetch et curl), non consultée.

## Points non résolus

- Les chiffres 2025 reposent sur deux sources secondaires concordantes ; à remplacer par l'étude primaire du ministère dès qu'elle sera consultable, et la série graphique pourra alors être prolongée à 2025.

## Verdict

Publiable après les corrections faites (chiffres 2025 explicitement présentés comme rapportés par la presse).

## Visuels ajoutés le 21 octobre 2026

Mode RÉNOVATION (narration visuelle). Chaque visuel ne reprend que des éléments déjà présents et sourcés dans le texte du dossier, avec les mêmes appels de note ; aucune donnée nouvelle n'a été ajoutée au texte. Rendu non testé (generer.py non lancé, conformément à la consigne) ; lecture du bloc vérifiée avec figures.lire et figures.rendre, contrôle verifier_dossier.py OK.

### V01 : Ce que la loi a changé depuis 1992 pour les violences au sein du couple

- EMPLACEMENT : fin de « D'où vient le mot et ce que dit le droit ».
- QUESTION POUR LE LECTEUR : Dans quel ordre le droit a-t-il évolué, sans créer d'infraction de féminicide ?
- TYPE : frise chronologique, 8 lignes.
- INFORMATION MONTRÉE ET APPELS DE NOTE : Le droit français n'a pas créé d'infraction de féminicide : depuis 1992, il a ajouté des circonstances aggravantes, une infraction spécifique et des mesures de protection. Appels : [1][3][5][7][8].
- LIMITE : Frise limitée aux lois citées dans ce dossier ; les intervalles entre les dates ne sont pas représentés à l'échelle.
- ALTERNATIVE TEXTUELLE : schéma rendu en HTML (liste ou tableau), lisible par les lecteurs d'écran ; pas d'image.
- TEST MOBILE : à faire après génération.
- STATUT : données vérifiées dans le texte du dossier (pas de nouvelle source consultée).

### V02 : Quatre décomptes qui ne mesurent pas la même chose

- EMPLACEMENT : fin de « Pourquoi les chiffres diffèrent ».
- QUESTION POUR LE LECTEUR : Pourquoi les chiffres officiels et associatifs diffèrent-ils ?
- TYPE : tableau comparatif (Source | Ce qui est compté | Méthode | Chiffre cité dans ce dossier), 4 lignes.
- INFORMATION MONTRÉE ET APPELS DE NOTE : Les chiffres diffèrent d'abord parce que les décomptes ne retiennent pas le même périmètre : le couple pour trois d'entre eux, tous les liens avec l'auteur pour l'Inter Orga Féminicides. Appels : [1][2][3][4].
- LIMITE : Les années ne sont pas les mêmes (2024 ou 2025) : ces chiffres ne se comparent pas terme à terme. Pour 2025, la presse rapporte 111 femmes tuées selon le ministère de l'Intérieur [13][14] et 164 cas au 31 décembre 2025 selon l'Inter Orga Féminicides [3].
- ALTERNATIVE TEXTUELLE : schéma rendu en HTML (liste ou tableau), lisible par les lecteurs d'écran ; pas d'image.
- TEST MOBILE : à faire après génération.
- STATUT : données vérifiées dans le texte du dossier (pas de nouvelle source consultée).
