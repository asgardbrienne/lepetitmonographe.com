# Registre de travail : 03-niches-fiscales

Document interne, non publié sur le site (Bible éditoriale v1.0, chapitres 8 et 10).

- Mode : AUDIT puis RÉNOVATION (révision ciblée), 21 octobre 2026, lot 1.
- Rendu mobile : non testé (pages non régénérées, `generer.py` non lancé). Contrôle automatique : `verifier_dossier.py` OK.

## Audit classé par gravité
- BLOQUANT (résolu) : contradiction interne : « Ce qu'on ne sait pas » affirmait que « près de la moitié des dispositifs n'est pas chiffrée ou l'est mal », alors que le corps (corrigé le 13 octobre) indique 13 % sans coût connu et 42 % sans nombre de bénéficiaires connu.
- MAJEUR (résolu) : « les chiffrages initiaux sont régulièrement inférieurs » reposait sur un seul exemple (2025).
- AMÉLIORATION : pacte Dutreil non expliqué.
- OPTIONNEL : un graphique comparant prévision initiale et coût définitif (2024, 2025) serait utile ; sources [1], [3], [4], [5] secondaires (signalées), l'annexe Voies et moyens tome II pourrait être citée directement.

## Modifications
- « Ce qu'on ne sait pas » : remplacé par les chiffres de la Cour des comptes [2]. Inscrit dans `corrections:`.
- À noter : ajout du second exemple vérifié (dépenses 2024 : 78,4 milliards estimés au PLF 2024, 89,4 milliards définitifs).
- Définition du pacte Dutreil (exonération partielle des droits de mutation à titre gratuit sur la transmission d'entreprises), d'après la Cour.
- `verifie:` 21 octobre 2026.

## Vérifications en ligne
- Cour des comptes, « Le budget de l'État en 2025 » (vie-publique.fr, PDF) : consulté ; vérifiés 85,09 → 91,83 Md€, 3,2 Md€ Dutreil (47,5 % de l'écart), 89,40 Md€ définitifs pour 2024, 78,41 Md€ au PLF 2024, 103,11 Md€ selon l'ancienne convention TVA, 13 % et 42 % sur 474 dépenses.
- Non reconsultés : Moneyvox, L'Esprit Français, Club des juristes.

## Points non résolus
- Aucun bloquant.

## Verdict
Publiable.

## Visuels ajoutés le 21 octobre 2026

Mode : RÉNOVATION (narration visuelle). Statut : données vérifiées dans le texte (aucune donnée nouvelle ; mêmes appels de note). Test mobile : à faire (pages non régénérées, generer.py non lancé). Contrôle : verifier_dossier.py OK, rendu de la figure testé avec figures.rendre.

- V01
  - Emplacement : section « Combien elles coûtent », après le paragraphe sur l'écart entre chiffrages initiaux et coûts constatés.
  - Question pour le lecteur : Le coût des niches est-il connu à l'avance ?
  - Type : groupes.
  - Informations montrées et appels de note : 2024 : 78,4 prévu, 89,4 définitif ; 2025 : 85,1 prévu, 91,8 estimé [2].
  - Limite : 2025 encore provisoire ; la part du pacte Dutreil dans l'écart n'est pas représentée, le texte ne l'attribuant pas clairement à une année.
  - Statut : données vérifiées dans le texte.
- V02
  - Emplacement : même section, après le paragraphe sur la convention TVA.
  - Question pour le lecteur : Combien change le total si l'on compte la TVA autrement ?
  - Type : groupes.
  - Informations montrées et appels de note : 89,4 et 91,8 (convention actuelle), 103,1 et 105,6 (ancienne convention) [2].
  - Limite : 13 % des dispositifs sans coût connu ; total = ordre de grandeur.
  - Statut : données vérifiées dans le texte.
