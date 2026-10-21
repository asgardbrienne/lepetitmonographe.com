# Registre de travail : 07-deserts-medicaux

Document interne, non publié sur le site (Bible éditoriale v1.0, chapitres 8 et 10).

- Mode : AUDIT puis RÉNOVATION (révision ciblée), 21 octobre 2026, lot 1.
- Rendu mobile : non testé (pages non régénérées, `generer.py` non lancé). Contrôle automatique : `verifier_dossier.py` OK.

## Audit classé par gravité
- BLOQUANT (résolu) : « les zonages des ARS… donnent des chiffres beaucoup plus élevés » : affirmation chiffrée implicite sans source.
- MAJEUR (résolu) : « reporté sans date » plus affirmatif que la source (Egora : « pourrait ne pas reprendre avant plusieurs mois »).
- MAJEUR (résolu) : sources de presse qui rapportent des votes ou une loi (FHF, Egora, Banque des Territoires 2025, Caducée) non signalées comme secondaires.
- AMÉLIORATION : sigles Drees et Irdes non développés ; Essentiel généralisant (« les organisations de médecins »).
- OPTIONNEL : le nombre de places en médecine repose sur un site d'orientation (déjà signalé comme non officiel).

## Modifications
- Retrait de « donnent des chiffres beaucoup plus élevés ». Inscrit dans `corrections:`.
- « a été reporté sans date » → citation d'Egora ; « Ce qu'on ne sait pas » reformulé (« nous n'avons pas trouvé de reprise »). Inscrit dans `corrections:`.
- Drees et Irdes développés ; Essentiel : « des organisations de médecins, dont l'Ordre des médecins [10] ».
- Sources 5 à 8 : préfixe « Source secondaire : ».
- `verifie:` 21 octobre 2026.

## Vérifications en ligne
- Egora, 11 juin 2026 : consulté (215 contre 118, examen non abouti).
- Caducée, 9 mai 2025 : consulté (99 voix contre 9).
- Compte rendu du Sénat du 11 juin 2026 (page 006) : consulté en partie ; le scrutin sur l'article 1er n'y figure pas (autre partie du compte rendu).
- Non reconsultés : Infirmiers.com, note Drees, Localtis, Santé Orientation, FHF, CNOM.

## Points non résolus
- État actuel de l'examen au Sénat après le 11 juin 2026 non vérifié sur le dossier législatif (formulation prudente conservée).

## Verdict
Publiable.

## Visuels ajoutés le 21 octobre 2026

Mode : RÉNOVATION (narration visuelle). Statut : données vérifiées dans le texte (aucune donnée nouvelle ; mêmes appels de note). Test mobile : à faire (pages non régénérées, generer.py non lancé). Contrôle : verifier_dossier.py OK, rendu de la figure testé avec figures.rendre.

- V01
  - Emplacement : section « Pourquoi il manque des médecins », après le paragraphe sur le numerus clausus et la loi Neuder.
  - Question pour le lecteur : Qui fixe le nombre d'étudiants en médecine, et depuis quand ?
  - Type : frise.
  - Informations montrées et appels de note : 1971 numerus clausus, 2020 numerus apertus [4], loi n° 2025-580 du 27 juin 2025 [5].
  - Limite : étapes non à l'échelle ; sources secondaires ; ne montre pas le nombre de places.
  - Statut : données vérifiées dans le texte.
- V02
  - Emplacement : section « Les solutions en débat », après le paragraphe sur la proposition de loi Garot.
  - Question pour le lecteur : En quoi les versions de l'Assemblée et du Sénat diffèrent-elles ?
  - Type : tableau.
  - Informations montrées et appels de note : contenu et votes du 7 mai 2025 [8] et du 11 juin 2026 [6][9].
  - Limite : simplifié (autres articles non détaillés) ; texte non adopté définitivement.
  - Statut : données vérifiées dans le texte.
