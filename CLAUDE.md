# Le Petit Monographe : règles éditoriales

Toute rédaction ou modification de contenu sur ce site applique ces règles sans exception.

1. Séparer clairement les niveaux d'information : fait établi, estimation, interprétation, débat, hypothèse, allégation, proposition. En true crime, distinguer aussi témoignage, expertise, élément matériel et état de la procédure.
2. Sourcer chaque donnée importante : source identifiable, date, contexte, périmètre. Les sources primaires sont privilégiées ; les sources secondaires sont signalées comme telles.
3. Ne jamais transformer une incertitude en certitude : quand on ne sait pas, on écrit qu'on ne sait pas. Quand les sources divergent, on l'indique.
4. Appliquer la même exigence de preuve à tous les camps (gouvernement, opposition, suspect, plaignant, expert, témoin), sans créer de faux équilibre : une rumeur ne vaut pas une preuve documentée.
5. Présenter honnêtement les arguments contraires : exposer le meilleur argument sérieux avant d'y répondre ou d'en montrer les limites.
6. Ne jamais prêter une intention sans preuve : une déclaration fausse n'est pas automatiquement un mensonge ; une erreur n'est pas automatiquement une manipulation.
7. Respecter strictement le droit et la procédure : présomption d'innocence, distinction entre accusation, enquête, mise en examen, procès, appel et condamnation définitive.
8. Éviter tout sensationnalisme : pas de « vérité enfin révélée », « ce qu'on vous cache », « scandale absolu ». Pas de « vraiment » ou « réellement » dans les titres.
9. Toujours donner le contexte d'un chiffre : série temporelle, dénominateur, comparaison internationale, changements de méthode, périmètre.
10. Rendre le raisonnement vérifiable : le lecteur retrouve les sources et comprend comment on arrive à une conclusion.
11. Corriger publiquement les erreurs : mise à jour datée et, si nécessaire, note de correction (page Méthode, section Errata).
12. Écrire pour permettre au lecteur de juger lui-même : expliquer et documenter, jamais dire pour qui voter, qui croire ou quelle conclusion politique adopter.

**Test avant publication :** « Si le nom ou le camp était inversé, appliquerions-nous exactement les mêmes critères ? » Si la réponse est non, l'article n'est pas prêt.

**Formule :** Rigueur. Impartialité. Traçabilité. Contradiction. Transparence.

## Bible éditoriale, journalistique et visuelle (v1.0, 21 octobre 2026)

Le référentiel complet est `outils/bible-editoriale-v1.0.md`. Il s'applique à toute création, audit, rénovation, mise à jour ou validation. La page publique « Notre méthode » prime en cas de divergence. Points d'application permanents :

- Ordre de priorité : droit et respect des personnes, puis faits et sources, puis les douze règles et les cinq statuts, puis la bible, puis les consignes du sujet. Une exigence de style, de SEO ou de rapidité ne modifie jamais une information.
- Annoncer le mode de travail (CRÉATION, AUDIT, RÉNOVATION, MISE À JOUR, VALIDATION). Ne jamais prétendre avoir ouvert une URL, lu un document en entier, vérifié un chiffre ou testé un rendu mobile si ce n'est pas le cas.
- Chaque nouveau dossier a son registre de travail interne dans `outils/registres/NN-slug.md`, sur le modèle `outils/registres/MODELE.md` : fiche d'angle, journal de recherche, registre des affirmations, storyboard visuel, contrôle qualité. Ces fichiers ne sont pas publiés comme pages.
- Format honnête (bible 3.2) : article explicatif, analyse, enquête documentaire, investigation originale. Un texte n'est pas une « enquête » parce qu'il est long ou très sourcé.
- Un visuel est prévu dès le plan et seulement s'il fait comprendre quelque chose : question pédagogique, source, période, limite, texte alternatif. L'absence de visuel inutile est une décision de qualité. Aucune donnée fabriquée.
- Trois relectures distinctes avant mise en ligne : factuelle et juridique, critique et méthodologique, pédagogique et visuelle. Elles ne sont pas présentées comme une validation indépendante.
- Conditions d'arrêt (bible 10.2) : source ou citation inventée ou non consultée, chiffre déterminant non vérifié, accusation non étayée, motif judiciaire supposé, illustration générée présentée comme document, correction antérieure supprimée sans le dire, contradiction entre chapô, texte, graphique et conclusion. Dans ces cas, le dossier est « non publiable en l'état » et on dit précisément ce qui manque.
- Rénovation d'un dossier existant : améliorer sans effacer. Conserver URL, ancres, sources, crédits et historique ; auditer d'abord, classer les problèmes (bloquant, majeur, amélioration, optionnel), puis modifier ; une correction de fond figure dans l'historique public.
- Rendu à l'autrice après chaque travail : sources réellement consultées et non consultées, points non vérifiés, tests effectués (rendu, liens), verdict. Une demande explicite de l'autrice d'écrire et de publier vaut autorisation de mise en ligne.

## Règles pratiques

- Aucun chiffre, aucune date, aucune décision de justice ne vient de mémoire ou d'une liste générée par une IA : chaque élément est vérifié à sa source avant d'être écrit.
- Les sources sont toujours recherchées par Claude lui-même, jamais demandées à l'autrice. Ce sont des sources réelles, publiées, qu'un lecteur retrouve facilement par une recherche Google : publications officielles, décisions, rapports, médias identifiés. Chaque source porte son titre, son auteur ou média, sa date et un lien qui fonctionne. Pas de source sans lien, pas de lien inventé.
- Si aucune source vérifiable n'est trouvée, l'information n'est pas publiée, ou elle est présentée explicitement comme non établie.
- Chaque dossier porte une date d'arrêt des données et un historique de mises à jour.
- Directrice de la publication : S. Enault, nommée dans les mentions légales et la page À propos ; jamais de prénom. Les dossiers restent signés « Le Petit Monographe ».
- Les monographies sont écrites par la directrice de la publication, qui en perçoit les revenus : ce lien d'intérêt est signalé sur la page Monographies, dans À propos et dans les mentions légales.
- Vérification avant mise en ligne : un chiffre, une citation ou une source non retrouvés à l'origine ne sont pas publiés. L'erratum reste l'exception.
- Enquêtes originales (documents, entretiens) : toute personne ou organisation mise en cause est sollicitée avant publication ; sa réponse, ou l'absence de réponse et la date de la demande, est indiquée dans le dossier.
- Positionnement : la référence du dossier long et sourcé ; publication à rythme régulier, dossiers mis à jour quand les faits évoluent.
- Pas de tiret cadratin dans les textes.
- Les pages sont générées par `outils/generer.py` (`python3 outils/generer.py .`).
- Aspect du site : maquette « édition » demandée par l'autrice le 17 octobre 2026 (sept vues de référence : logo à gauche et barre de navigation avec bouton Newsletter, accueil avec carrousel « Enquête à la une », piliers, dernières enquêtes, tuiles de rubrique et bande méthode ; page d'enquête en une colonne avec fil d'Ariane, signature, sommaire numéroté, encadré « En résumé » et chronologie à statuts ; rubrique avec bandeau photo, onglets et liste ; pages Monographies et Méthode avec visuel à droite), dans l'esprit de la charte V1.1. Les visuels de maquette générés par IA ne sont jamais repris : photos libres et créditées uniquement. Ivoire #F8F5EF, bleu nuit #152840 / #11243D, or #A78346 (décor et grands titres ; #8C6A2E pour les petits textes dorés), gris #626773, blanc éditorial #FFFDF9, vert preuve #2A6654 réservé au statut Fait établi. Titres en Playfair Display, interface en DM Sans, lecture longue en Source Serif 4. Mode sombre disponible. Contrastes WCAG AA.
- Affichage des étiquettes : cinq statuts (Fait établi, Témoignage, Interprétation, Hypothèse, Proposition). Les nuances de la règle 1 restent visibles en précision sous le statut : [Estimation] et [Débat] et [Expertise] s'affichent en Interprétation, [Allégation] en Témoignage, [Élément matériel] et [État de la procédure] en Fait établi.

## Graphiques et chronologies

- Les graphiques s'écrivent dans le fichier du dossier avec un bloc `[Figure] barres`, `barres-h`, `groupes` ou `frise` (syntaxe détaillée en tête de `outils/figures.py`).
- Une figure ne reprend que des chiffres déjà vérifiés et sourcés dans le texte du dossier, avec les mêmes appels de note. Elle porte un titre informatif, son unité, son champ et sa période, une phrase de lecture, sa source datée et, si besoin, une note de limite.
- Barres partant de zéro, une seule échelle, pas d'effet 3D. Les prévisions sont hachurées et signalées en légende. Un axe non continu (années manquantes) est signalé en note.
- Ne pas mettre côte à côte des chiffres de méthodes ou de périmètres différents sans le dire dans la note.

## Images

- Chaque dossier reçoit une image d'illustration (champs `image`, `image_alt`, `image_credit`, `image_lien` en tête du fichier du dossier, image enregistrée dans `assets/images/`).
- Licences acceptées uniquement : domaine public ou CC0, licence Unsplash, licence Pexels, CC BY et CC BY-SA. La licence est vérifiée sur la page de la photo elle-même avant tout usage. Pas de licence « NC » (non commerciale), pas de « ND », pas d'image trouvée sans licence explicite.
- Crédit systématique, même quand il n'est pas obligatoire : « Photo : auteur, licence, source », avec un lien vers la page de la photo.
- Aucune photo de victime, d'enfant, de personne mise en cause ou de particulier. Les dossiers judiciaires sont illustrés par des lieux, des bâtiments ou des objets, sans identifier de personne. Pas d'image racoleuse ni de mise en scène sanglante.
- Pas d'image générée par IA présentée comme une photo.
