import sys, os
OUT = sys.argv[1]

NAV = [
    ("politique-institutions.html", "Politique"),
    ("economie-societe.html", "Économie &amp; Société"),
    ("affaires-enquetes.html", "Affaires &amp; Enquêtes"),
    ("livres.html", "Livres"),
    ("methode.html", "Notre méthode"),
    ("a-propos.html", "À propos"),
]

def A(t):  # élément à compléter avant publication
    return f'<span class="a-completer">{t}</span>'

def page(fichier, titre, description, corps, noindex=False):
    nav = "\n".join(
        f'      <a href="{h}"{" aria-current=\"page\"" if h == fichier else ""}>{l}</a>' for h, l in NAV)
    titre_complet = "Le Petit Monographe · Documents & enquêtes" if fichier == "index.html" else f"{titre} · Le Petit Monographe"
    robots = '\n  <meta name="robots" content="noindex">' if noindex else ""
    html = f'''<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{titre_complet}</title>
  <meta name="description" content="{description}">{robots}
  <link rel="icon" href="favicon.png" type="image/png">
  <link rel="apple-touch-icon" href="apple-touch-icon.png">
  <meta property="og:title" content="{titre_complet}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="https://lepetitmonographe.com/assets/logo-partage.jpg">
  <meta property="og:type" content="website">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Playfair+Display:wght@500;600&family=Source+Serif+4:ital,wght@0,500;0,600;1,500&display=swap">
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>

<header class="entete">
  <div class="conteneur">
    <a class="logo" href="./"><img src="assets/monogramme.png" alt="" width="36" height="36"><span>Le Petit Monographe</span></a>
    <nav class="nav" aria-label="Navigation principale">
{nav}
    </nav>
  </div>
</header>

<main>
{corps}
</main>

<footer class="pied">
  <div class="conteneur">
    <span>© 2026 Le Petit Monographe</span>
    <span><a href="contact.html">Contact</a> · <a href="mentions-legales.html">Mentions légales</a> · <a href="confidentialite.html">Confidentialité</a></span>
  </div>
</footer>

</body>
</html>
'''
    with open(os.path.join(OUT, fichier), "w") as f:
        f.write(html)

def tete(surtitre, h1, chapeau, classe=""):
    return f'''  <section class="tete-page {classe}">
    <div class="conteneur">
      <p class="surtitre">{surtitre}</p>
      <h1>{h1}</h1>
      <p class="chapeau">{chapeau}</p>
    </div>
  </section>'''

def section(contenu, id_=""):
    i = f' id="{id_}"' if id_ else ""
    return f'''  <section class="section"{i}>
    <div class="conteneur">
{contenu}
    </div>
  </section>'''

RUBRIQUES = [
    ("politique-institutions.html", "c-pouvoirs", "Politique &amp; Institutions",
     "Pouvoir, décisions publiques, élections, réformes."),
    ("economie-societe.html", "c-economie", "Économie &amp; Société",
     "Dette, retraites, fiscalité, emploi, services publics."),
    ("affaires-enquetes.html", "c-affaires", "Affaires &amp; Enquêtes",
     "Chronologies judiciaires, pièces du dossier, expertises, faits établis et hypothèses."),
]

LIVRES = {
    "c-pouvoirs": [('<a href="livre-emmanuel-macron-le-bilan.html">Emmanuel Macron, le bilan</a>',
                    "Promesses, réformes, crises et affaires : la présidence passée au crible des faits (2017-2026).")],
    "c-economie": [("Comment redresser les comptes de la France",
                    "Faits, débats, calculs et propositions séparés, avec le degré de certitude de chaque élément. " + A("Titre exact et résumé à valider"))],
    "c-affaires": [(A("Titre de la monographie"), A("Résumé en deux phrases"))],
}
COLLECTION = {"c-pouvoirs": "Pouvoirs &amp; Société", "c-economie": "Pouvoirs &amp; Société", "c-affaires": "Affaires &amp; Enquêtes"}

def carte_livre(classe, titre, resume):
    return f'''        <article class="livre {classe}">
          <div class="couverture" aria-hidden="true">{COLLECTION[classe]}</div>
          <div>
            <h4>{titre}</h4>
            <p>{resume}</p>
            <a class="bouton" href="#" rel="noopener">{A("Lien Amazon")}</a>
          </div>
        </article>'''

def grille_livres(classes):
    cartes = "\n".join(carte_livre(c, t, r) for c in classes for t, r in LIVRES[c])
    return f'      <div class="livres">\n{cartes}\n      </div>'

TYPOLOGIE = '''      <p class="typologie" aria-label="Fait établi, différent de témoignage, différent d'interprétation, différent d'hypothèse, différent de proposition">
        <span>Fait établi</span><span class="ne">≠</span><span>Témoignage</span><span class="ne">≠</span><span>Interprétation</span><span class="ne">≠</span><span>Hypothèse</span><span class="ne">≠</span><span>Proposition</span>
      </p>'''

# ---------- Accueil ----------
portes = "\n".join(f'''        <a class="porte {c}" href="{h}">
          <p class="surtitre">Rubrique</p>
          <h3>{t}</h3>
          <p>{d}</p>
          <span class="suite">Entrer dans la rubrique</span>
        </a>''' for h, c, t, d in RUBRIQUES)

accueil = f'''  <section class="ouverture embleme">
    <div class="conteneur">
      <div class="embleme-monogramme"><img src="assets/monogramme.png" alt="" width="120" height="120"></div>
      <h1 class="embleme-nom">Le Petit Monographe</h1>
      <p class="embleme-sous">Documents <span>&amp;</span> enquêtes</p>
      <p class="embleme-domaines">Politique <i>•</i> Économie <i>•</i> Société <i>•</i> <span>Affaires judiciaires</span></p>
      <p class="chapeau">Des dossiers documentés qui distinguent les faits établis, les désaccords, les hypothèses et les zones d'incertitude.</p>
      <ul class="engagements" aria-label="Engagements éditoriaux">
        <li>Sources datées</li>
        <li>Faits et opinions séparés</li>
        <li>Arguments contradictoires</li>
        <li>Incertitudes signalées</li>
        <li>Corrections publiées</li>
      </ul>
    </div>
  </section>

{section(f"""      <h2>Trois portes d'entrée</h2>
      <p class="intro">Chaque dossier part des pièces disponibles et indique ce qui est établi, ce qui est débattu et ce qui reste incertain.</p>
      <div class="portes">
{portes}
      </div>""")}

  <div class="bandeau">
{section(f"""      <p class="surtitre">Notre méthode</p>
      <h2>Chaque information porte son étiquette</h2>
{TYPOLOGIE}
      <p class="intro">Chaque type d'information est identifié, les sources sont données, les incertitudes sont conservées et les corrections sont publiées.</p>
      <a class="bouton" style="--couleur: var(--marque)" href="methode.html">Lire la méthode</a>""")}
  </div>

{section(f"""      <h2>Les monographies</h2>
      <p class="intro">Quand un article ne suffit plus, les livres approfondissent l'ensemble du dossier.</p>
{grille_livres(["c-pouvoirs", "c-economie", "c-affaires"])}""")}

{section("""      <p class="signature" style="border:0;padding:0;margin:0">Les faits d'abord. Les désaccords ensuite. L'opinion reste au lecteur.</p>
      <p style="margin:8px 0 0;color:var(--encre-douce)"><a href="a-propos.html">À propos du Petit Monographe</a></p>""")}'''

page("index.html", "Accueil",
     "Le Petit Monographe : dossiers documentés sur la politique, l'économie, la société et les affaires judiciaires. Faits établis, désaccords, hypothèses et incertitudes clairement séparés.",
     accueil)

# ---------- Rubriques ----------
DOSSIERS = {
    "c-economie": [("dossier-chomage-emploi.html", "Le chômage remonte, l'emploi reste élevé : comment lire les deux chiffres",
                    "Deux indicateurs qui semblent se contredire et mesurent des choses différentes. Données arrêtées au 8 octobre 2026.")],
}
def cartes_dossiers(c):
    ds = DOSSIERS.get(c, [])
    if not ds:
        return '      <div class="vide-bloc">Les premiers dossiers de cette rubrique sont en préparation.</div>'
    return "\n".join(f'''      <a class="porte {c}" href="{h}">
        <p class="surtitre">Dossier</p>
        <h3>{t}</h3>
        <p>{d}</p>
        <span class="suite">Lire le dossier</span>
      </a>''' for h, t, d in ds)

for h, c, t, d in RUBRIQUES:
    corps = tete("Rubrique", t, d, c) + "\n" + section(f"""      <h2>Les dossiers</h2>
      <div class="portes">
{cartes_dossiers(c)}
      </div>""") + "\n" + section(f"""      <h2>Pour aller plus loin</h2>
      <p class="intro">Les monographies liées à cette rubrique.</p>
{grille_livres([c])}""")
    page(h, t.replace("&amp;", "&"), f"{t.replace('&amp;', '&')} : {d}", corps)

# ---------- Livres ----------
livres = tete("Les monographies", "Le dossier complet, en un volume",
              "Quand un article ne suffit plus, les livres approfondissent l'ensemble du dossier. Deux collections, une même méthode.") + "\n" + section(f"""      <div class="collection c-pouvoirs">
        <div class="collection-tete">
          <p class="surtitre">Collection</p>
          <h3>Pouvoirs &amp; Société</h3>
          <p>Politique, économie, institutions et grands débats français.</p>
        </div>
{grille_livres(["c-pouvoirs", "c-economie"])}
      </div>
      <div class="collection c-affaires">
        <div class="collection-tete">
          <p class="surtitre">Collection</p>
          <h3>Affaires &amp; Enquêtes</h3>
          <p>Affaires judiciaires, erreurs judiciaires, dossiers non résolus. Le dossier rendu lisible : chronologie, pièces, versions contradictoires, décisions de justice et zones d'ombre.</p>
        </div>
{grille_livres(["c-affaires"])}
      </div>""")
page("livres.html", "Livres", "Les monographies du Petit Monographe : collections Pouvoirs & Société et Affaires & Enquêtes.", livres)

# ---------- Méthode ----------
ETIQ = [
    ("Fait établi", "Vérifiable dans une source identifiée et datée : donnée publique, décision de justice, texte officiel, rapport, archive."),
    ("Estimation", "Un chiffre calculé ou extrapolé, et non mesuré directement. Sa méthode et sa marge d'incertitude sont indiquées."),
    ("Interprétation", "Une lecture des faits, par l'auteur ou par un tiers. Toujours attribuée, et confrontée aux lectures concurrentes."),
    ("Débat", "Une question où des positions sérieuses divergent, sans que les faits disponibles permettent de trancher."),
    ("Hypothèse", "Une explication possible que les éléments disponibles ne permettent ni de confirmer ni d'écarter."),
    ("Allégation", "Une affirmation portée par une personne ou une partie, qui n'a pas été établie. Attribuée et présentée comme telle."),
    ("Proposition", "Une piste d'action. Présentée comme un choix discutable, avec ses coûts et ses objections."),
]
ETIQ_JUDICIAIRE = [
    ("Témoignage", "Ce qu'une personne déclare avoir vu, entendu ou vécu. Attribué, daté, et jamais présenté comme un fait établi."),
    ("Expertise", "L'avis d'un expert désigné, avec sa méthode et ses limites. Une expertise peut être contestée par une contre-expertise."),
    ("Élément matériel", "Une pièce du dossier : trace, document, relevé, objet. Ce qu'elle prouve et ce qu'elle ne prouve pas sont distingués."),
    ("État de la procédure", "Enquête, mise en examen, renvoi, procès, appel, condamnation définitive : chaque étape est nommée exactement."),
]
REGLES = [
    ("Séparer les niveaux d'information", "Fait établi, estimation, interprétation, débat, hypothèse, allégation, proposition. Dans les affaires judiciaires, aussi témoignage, expertise, élément matériel et état de la procédure."),
    ("Sourcer chaque donnée importante", "Source identifiable, date, contexte, périmètre. Les sources primaires sont privilégiées ; les sources secondaires sont signalées comme telles."),
    ("Ne jamais transformer une incertitude en certitude", "Quand on ne sait pas, on écrit qu'on ne sait pas. Quand les sources divergent, on l'indique."),
    ("La même exigence de preuve pour tous", "Le même standard pour un gouvernement, une opposition, un suspect, un plaignant, un expert ou un témoin. Sans faux équilibre : une rumeur ne vaut pas une preuve documentée."),
    ("Présenter honnêtement les arguments contraires", "Pas de caricature : on expose le meilleur argument sérieux avant d'y répondre ou d'en montrer les limites."),
    ("Ne jamais prêter une intention sans preuve", "Une déclaration fausse n'est pas automatiquement un mensonge ; une erreur n'est pas automatiquement une manipulation."),
    ("Respecter le droit et la procédure", "Présomption d'innocence ; distinction entre accusation, enquête, mise en examen, procès, appel et condamnation définitive."),
    ("Pas de sensationnalisme", "Pas de « vérité enfin révélée », de « ce qu'on vous cache » ni de titre conçu pour provoquer. Le sujet doit intéresser par les faits eux-mêmes."),
    ("Toujours donner le contexte", "Un chiffre isolé peut tromper : on vérifie la série dans le temps, le dénominateur, la comparaison internationale, les changements de méthode et le périmètre."),
    ("Rendre le raisonnement vérifiable", "Le lecteur doit pouvoir retrouver les sources et comprendre comment on arrive à une conclusion."),
    ("Corriger publiquement", "Si une donnée change ou si nous nous trompons, l'article est mis à jour avec la date et, si nécessaire, une note de correction."),
    ("Laisser le lecteur juger", "Notre rôle est d'expliquer et de documenter, pas de dire pour qui voter, qui croire ou quelle conclusion politique adopter."),
]
def liste_etiq(items):
    return "\n".join(f'''        <div><span class="etiquette">{e}</span><p>{d}</p></div>''' for e, d in items)
regles = "\n".join(f'''        <li><h3>{t}</h3><p>{d}</p></li>''' for t, d in REGLES)
methode = tete("Notre méthode", "Une méthode avant une opinion",
               "Rigueur. Impartialité. Traçabilité. Contradiction. Transparence.") + "\n" + section(f"""      <h2>Douze règles</h2>
      <p class="intro">Elles s'appliquent à chaque dossier, quel que soit le sujet ou le camp concerné.</p>
      <ol class="regles">
{regles}
      </ol>""") + "\n" + section("""      <div class="test-inversion">
        <p class="surtitre">Le test avant publication</p>
        <p class="question">« Si le nom ou le camp était inversé, appliquerions-nous exactement les mêmes critères ? »</p>
        <p>Si la réponse est non, l'article n'est pas prêt.</p>
      </div>""") + "\n" + section(f"""      <h2>Chaque information porte son étiquette</h2>
      <p class="intro">Dans chaque dossier, la nature de l'information est indiquée. Le lecteur sait ce qu'il lit : un fait, une estimation, une interprétation ou une hypothèse.</p>
      <div class="etiquettes">
{liste_etiq(ETIQ)}
      </div>
      <h3 class="sous-titre-etiq">Dans les affaires judiciaires</h3>
      <div class="etiquettes">
{liste_etiq(ETIQ_JUDICIAIRE)}
      </div>""") + "\n" + section("""      <h2>Errata et mises à jour</h2>
      <p class="intro">Une erreur peut toujours se glisser, une source peut être révisée. Chaque correction est listée ici, avec la date et le passage concerné.</p>
      <table class="tableau-errata">
        <thead>
          <tr><th>Date</th><th>Publication</th><th>Passage</th><th>Correction</th></tr>
        </thead>
        <tbody>
          <tr><td colspan="4" class="vide">Les corrections apparaîtront ici au fil des mises à jour.</td></tr>
        </tbody>
      </table>""", "errata")
page("methode.html", "Notre méthode", "Les douze règles du Petit Monographe : niveaux d'information séparés, sources datées, même exigence pour tous les camps, corrections publiques.", methode)

# ---------- À propos ----------
apropos = tete("À propos", "Le Petit Monographe", "Une publication indépendante, sans affiliation partisane.") + "\n" + section("""      <div class="prose">
        <p>Le Petit Monographe publie des dossiers et des monographies documentaires consacrés aux grands sujets politiques, économiques, sociaux et judiciaires contemporains.</p>
        <p>Il n'est lié à aucun parti, mouvement, syndicat ou candidat, et ne soutient aucune candidature. Traiter un sujet politique n'est pas prendre parti : les mêmes règles s'appliquent quel que soit le camp concerné.</p>
        <p>La méthode repose sur un principe simple : distinguer ce qui est établi de ce qui relève de l'interprétation, du débat ou de l'hypothèse. Chaque dossier s'appuie sur des sources identifiées et datées : données publiques, rapports officiels, décisions de justice, travaux parlementaires, archives, auditions et autres documents vérifiables. Lorsque les sources divergent ou qu'un élément demeure incertain, cette incertitude est signalée.</p>
        <p>Dans les affaires judiciaires, les faits établis, les accusations, les témoignages, les expertises et les hypothèses sont présentés séparément, dans le respect de la présomption d'innocence et de l'état réel des procédures.</p>
        <p>L'objectif n'est pas de dire au lecteur ce qu'il doit penser, mais de lui donner les éléments nécessaires pour comprendre, vérifier et se forger sa propre opinion.</p>
        <p class="signature">Les faits d'abord. Les désaccords ensuite. L'opinion reste au lecteur.</p>
      </div>""")
page("a-propos.html", "À propos", "Le Petit Monographe, publication indépendante de dossiers documentaires sur la politique, l'économie, la société et les affaires judiciaires.", apropos)

# ---------- Contact ----------
contact = tete("Contact", "Écrire au Petit Monographe",
               "Presse, lecteurs, signalement d'une erreur ou d'une source : toute remarque argumentée et sourcée est lue.") + "\n" + section(f"""      <div class="prose">
        <p>Pour signaler une erreur, merci d'indiquer la publication, le passage concerné et, si possible, la source qui permet de la corriger.</p>
        <p><a class="bouton" href="#">{A("Adresse e-mail de contact")}</a></p>
      </div>""")
page("contact.html", "Contact", "Contacter Le Petit Monographe : presse, lecteurs, signalement d'erreur.", contact)

# ---------- Mentions légales ----------
mentions = tete("Informations légales", "Mentions légales", "") + "\n" + section(f"""      <div class="prose">
        <h2>Éditeur du site</h2>
        <p>Ce site est édité par une personne physique, à titre non professionnel. Conformément à la loi pour la confiance dans l'économie numérique, son identité a été communiquée à l'hébergeur et n'est pas rendue publique.</p>
        <p>Contact : voir la page <a href="contact.html">Contact</a>.</p>
        <h2>Hébergement</h2>
        <p>{A("Hébergeur : dépend de la solution technique retenue")}</p>
        <h2>Liens vers Amazon</h2>
        <p>{A("Si les liens sont affiliés (Partenaires Amazon), l'indiquer ici")}</p>
      </div>""")
page("mentions-legales.html", "Mentions légales", "Mentions légales du site Le Petit Monographe.", mentions, noindex=True)

# ---------- Confidentialité ----------
conf = tete("Informations légales", "Confidentialité", "") + "\n" + section(f"""      <div class="prose">
        <h2>Cookies et mesure d'audience</h2>
        <p>Ce site ne dépose aucun cookie publicitaire ni de mesure d'audience. {A("À mettre à jour si un outil de statistiques ou une newsletter est ajouté")}</p>
        <h2>Polices de caractères</h2>
        <p>Les polices sont chargées depuis Google Fonts, ce qui transmet l'adresse IP du visiteur à Google.</p>
        <h2>Messages reçus</h2>
        <p>Les messages envoyés par e-mail ne servent qu'à y répondre et ne sont transmis à aucun tiers.</p>
        <h2>Vos droits</h2>
        <p>Vous pouvez demander l'accès, la rectification ou la suppression de vos données en écrivant à l'adresse indiquée sur la page <a href="contact.html">Contact</a>, et saisir la CNIL en cas de difficulté.</p>
      </div>""")
page("confidentialite.html", "Confidentialité", "Politique de confidentialité du site Le Petit Monographe.", conf, noindex=True)

# ---------- Fiche livre : Macron ----------
CHIFFRES = [
    ("7,1 %", "Taux de chômage au début de 2023, le plus bas depuis 1982 hors confinement ; il remonte à 8,3 % mi-2026", "Chapitre 11"),
    ("69,3 %", "Taux d'emploi des 15-64 ans en 2025, un record depuis le début de la mesure, en 1975", "Chapitre 11"),
    ("+1 364 Md€", "Hausse de la dette publique entre mi-2017 et mi-2026", "Chapitre 11"),
    ("15,4 %", "Taux de pauvreté en 2023 et 2024, un record depuis le début de la série, en 1996", "Chapitre 11"),
    ("7", "Premiers ministres en neuf ans, dont quatre depuis la dissolution de 2024", "Chapitre 5"),
    ("16 %", "Opinions favorables au président en septembre 2026 (Ipsos BVA)", "Chapitre 5"),
]
chiffres = "\n".join(f'''        <article><span class="num" style="font-size:1.9rem;color:var(--encre)">{c}</span><p>{d}</p><p style="margin-top:10px;font-size:.75rem;letter-spacing:.08em;text-transform:uppercase;color:var(--marque)">{ch}</p></article>''' for c, d, ch in CHIFFRES)
ENCADRES = [
    ("L'essentiel", "L'essentiel d'un chapitre, à lire en premier."),
    ("Fait établi", "Un fait établi par une source reconnue : donnée publique, décision de justice, rapport officiel."),
    ("Ce que disent les critiques", "Les arguments des opposants, attribués à leurs auteurs."),
    ("Ce que répondent les défenseurs", "Les arguments des défenseurs du bilan, présentés en regard des critiques."),
    ("Débat", "Une question où des positions sérieuses divergent, sans que les faits permettent de trancher."),
    ("Vérification", "Une déclaration confrontée aux faits, avec un verdict."),
    ("Alternative", "Ce que d'autres proposaient de faire, avec leurs chiffrages quand ils existent."),
    ("À noter", "Une limite, une précaution de lecture ou une procédure en cours."),
]
encadres = "\n".join(f'''        <div><span class="etiquette">{e}</span><p>{d}</p></div>''' for e, d in ENCADRES)
PARTIES = [
    ("I · La conquête", ["De Bercy à l'Élysée"]),
    ("II · Le premier quinquennat", ["Transformer vite", "Le temps des crises"]),
    ("III · Le second quinquennat", ["Gouverner sans majorité", "La dissolution et ses suites"]),
    ("IV · Les grands dossiers", ["La France dans le monde", "Sécurité, immigration, laïcité", "Climat, énergie, logement, santé, école", "Société, culture, innovation : les réalisations"]),
    ("V · Le bilan", ["Les promesses", "Les chiffres du bilan", "Vérités, contre-vérités et accusations infondées", "Exemplarité et affaires", "Les méthodes du pouvoir", "L'homme, le style et les erreurs", "Les Français et la politique", "Ce qui aurait pu être fait : les alternatives"]),
]
n = 0; parties = []
for titre, chs in PARTIES:
    items = []
    for c in chs:
        n += 1
        items.append(f"<li><span style=\"color:var(--marque);display:inline-block;min-width:2ch\">{n}</span> {c}</li>")
    parties.append(f'''        <div><p class="surtitre" style="margin:0 0 10px">Partie {titre}</p><ul style="list-style:none;padding:0;margin:0;display:grid;gap:6px">{"".join(items)}</ul></div>''')
parties = "\n".join(parties)

macron = f'''  <section class="tete-page c-pouvoirs">
    <div class="conteneur">
      <p class="surtitre">Collection Pouvoirs &amp; Société</p>
      <h1>Emmanuel Macron, le bilan</h1>
      <p class="chapeau">Promesses, réformes, crises et affaires : la présidence passée au crible des faits (2017-2026).</p>
      <p style="margin:24px 0 0;font-size:.875rem;color:var(--encre-douce)">Première édition, octobre 2026 · Faits et données arrêtés au 6 octobre 2026</p>
      <p style="margin:20px 0 0"><a class="bouton" href="#" rel="noopener">{A("Lien Amazon")}</a></p>
    </div>
  </section>
''' + section("""      <div class="prose">
        <p>Pour ses soutiens, Emmanuel Macron a modernisé un pays bloqué, fait reculer le chômage, rendu la France attractive et tenu dans la tempête : gilets jaunes, pandémie, guerre en Ukraine, crise de l'énergie. Pour ses opposants, il a gouverné pour les plus aisés, contourné le Parlement, creusé la dette et ouvert la voie à l'extrême droite. Les deux récits contiennent des faits exacts. Aucun ne suffit.</p>
        <p>Ce livre ne prend pas parti. Il pose une question simple : qu'a promis Emmanuel Macron, qu'a-t-il fait, avec quels résultats et par quelles méthodes ? Il répond avec les données publiques, les décisions de justice, les rapports parlementaires et les évaluations d'organismes indépendants.</p>
      </div>""") + "\n" + section(f"""      <h2>Le bilan en six chiffres</h2>
      <p class="intro">Six nombres résument neuf ans de pouvoir, dans un sens comme dans l'autre. Chacun est détaillé et sourcé dans le chapitre indiqué.</p>
      <div class="grille-methode">
{chiffres}
      </div>""") + "\n" + section(f"""      <h2>Chaque information porte son étiquette</h2>
      <p class="intro">Dans le texte, des encadrés de couleur distinguent la nature de chaque information. Ils permettent de savoir, d'un coup d'œil, si l'on lit un fait, une critique, une défense ou une vérification.</p>
      <div class="etiquettes">
{encadres}
      </div>""") + "\n" + section("""      <div class="prose">
        <h2>Les sujets sensibles</h2>
        <p><strong>Les « mensonges ».</strong> Prêter une intention de tromper suppose une preuve que l'on a rarement. Le livre confronte donc les déclarations aux faits et qualifie l'écart : promesse non tenue, affirmation inexacte, présentation trompeuse, changement de position. Les accusations portées contre le président sont soumises à la même vérification, et certaines se révèlent fausses.</p>
        <p><strong>Les affaires judiciaires.</strong> Personne n'est présenté comme coupable sans décision de justice définitive. Pour les procédures en cours, la présomption d'innocence est rappelée.</p>
        <p><strong>« Ce qui aurait dû être fait ».</strong> Le dernier chapitre présente les alternatives défendues par les différents camps et les recommandations d'organismes indépendants, chiffrées quand c'est possible.</p>
      </div>""") + "\n" + section(f"""      <h2>Sommaire</h2>
      <p class="intro">Cinq parties, dix-sept chapitres, et en annexe une chronologie complète, un glossaire, une bibliographie et un index des noms.</p>
      <div class="portes" style="gap:32px">
{parties}
      </div>""")
page("livre-emmanuel-macron-le-bilan.html", "Emmanuel Macron, le bilan",
     "Emmanuel Macron, le bilan. Promesses, réformes, crises et affaires : la présidence passée au crible des faits (2017-2026).", macron)

# ---------- Dossier : chômage et emploi ----------
def encadre(etiquette, contenu):
    return f'''        <aside class="encadre"><span class="etiquette">{etiquette}</span>
          {contenu}
        </aside>'''

def note(n):
    return f'<sup class="appel"><a href="#source-{n}" id="appel-{n}">{n}</a></sup>'

SOURCES_CHOMAGE = [
    ("Insee, « Au deuxième trimestre 2026, le taux de chômage augmente de 0,2 point et atteint 8,3 % », Informations rapides n° 192, 7 août 2026.", "https://www.insee.fr/fr/statistiques/9032359"),
    ("Insee, « Une photographie du marché du travail en 2025 », Insee Première n° 2096, 2026.", "https://www.insee.fr/fr/statistiques/8901327"),
    ("Insee, « Au deuxième trimestre 2026, l'emploi salarié est quasi stable (-0,1 %) », Informations rapides n° 214, août 2026.", "https://www.insee.fr/fr/statistiques/9039152"),
    ("Insee, Note de conjoncture, juin 2026, fiche « Emploi ».", "https://www.insee.fr/fr/statistiques/fichier/9007912/ndc-juin-2026-emploi.pdf"),
    ("Insee, « Au quatrième trimestre 2024, le taux de chômage est quasi stable (-0,1 point) à 7,3 % », Informations rapides n° 34, février 2025.", "https://www.insee.fr/fr/statistiques/fichier/version-html/8351234/IR34_Chomage_4T2024.pdf"),
    ("Conseil d'orientation des retraites, Rapport annuel, juin 2026, partie 4, chapitre 1.", "https://www.cor-retraites.fr/sites/default/files/2026-06/RA_Part4_Chap1.pdf"),
    ("Insee, « Les méthodes d'estimation de la précision de l'Enquête Emploi en continu ».", "https://www.insee.fr/fr/statistiques/2022151"),
    ("Insee, « La situation sur le marché du travail des bénéficiaires du RSA à fin 2024 », Insee Analyses n° 108.", "https://www.insee.fr/fr/statistiques/8562837"),
]
sources_html = "\n".join(f'          <li id="source-{i}">{t} <a href="{u}" rel="noopener">{u.replace("https://", "")}</a> <a href="#appel-{i}" class="retour" aria-label="Retour au texte">↑</a></li>' for i, (t, u) in enumerate(SOURCES_CHOMAGE, 1))

dossier = f'''  <section class="tete-page c-economie">
    <div class="conteneur">
      <p class="surtitre">Économie &amp; Société · Dossier</p>
      <h1>Le chômage remonte, l'emploi reste élevé : comment lire les deux chiffres</h1>
      <p class="chapeau">Depuis 2023, le taux de chômage augmente alors que le taux d'emploi a atteint en 2025 son plus haut niveau depuis 1975. Les deux chiffres sont exacts. Ils ne mesurent pas la même chose.</p>
      <p class="meta-dossier">Données arrêtées au 8 octobre 2026 · Première publication le 8 octobre 2026</p>
    </div>
  </section>

  <article class="section dossier">
    <div class="conteneur">
      <div class="prose">
        <p class="a-completer bandeau-verif">Version de travail : chaque chiffre doit être relu sur la publication d'origine avant mise en ligne.</p>

        <aside class="essentiel">
          <p class="surtitre">L'essentiel</p>
          <ul>
            <li>Le taux de chômage est de 8,3 % au deuxième trimestre 2026, son plus haut niveau depuis 2020, après un point bas de 7,1 % début 2023.{note(1)}</li>
            <li>Le taux d'emploi des 15-64 ans a atteint 69,3 % en moyenne en 2025, un niveau inédit depuis 1975. Il recule depuis : 69,0 % au deuxième trimestre 2026.{note(2)}{note(1)}</li>
            <li>Les deux chiffres n'ont pas le même dénominateur. Le chômage peut monter si davantage de personnes cherchent un emploi, même quand le nombre de personnes en emploi ne baisse pas.</li>
            <li>La part exacte de chaque explication dans la hausse du chômage n'est pas établie.</li>
          </ul>
        </aside>

        <h2>Deux chiffres, deux dénominateurs</h2>
{encadre("Fait établi", "<p>Le <strong>taux de chômage</strong> rapporte le nombre de chômeurs à la <strong>population active</strong> : les personnes qui ont un emploi et celles qui en cherchent un. Le <strong>taux d'emploi</strong> rapporte le nombre de personnes en emploi à <strong>toute la population</strong> d'une tranche d'âge, ici les 15-64 ans, qu'elles travaillent, cherchent ou non.</p>")}
{encadre("Fait établi", "<p>Est chômeur au sens du Bureau international du travail (BIT) une personne qui, simultanément, n'a pas travaillé pendant la semaine de référence, est disponible pour travailler dans les deux semaines et a cherché activement un emploi au cours du mois précédent. Est en emploi une personne qui a travaillé au moins une heure pendant la semaine de référence.</p>")}
        <p>Une illustration arithmétique, avec des nombres fictifs, montre comment les deux chiffres peuvent évoluer différemment. Sur 100 personnes de 15 à 64 ans, 69 ont un emploi et 6 en cherchent un. La population active compte 75 personnes. Le taux d'emploi est de 69 % et le taux de chômage de 8 % (6 sur 75). Si une personne jusque-là inactive, par exemple un senior qui aurait auparavant pris sa retraite, se met à chercher un emploi sans en trouver, le taux d'emploi reste à 69 % mais le taux de chômage passe à 9,2 % (7 sur 76).</p>

        <h2>Ce que disent les chiffres</h2>
        <div class="tableau-defilant">
          <table class="tableau-donnees">
            <thead><tr><th>Indicateur</th><th>Période</th><th>Valeur</th><th>Source</th></tr></thead>
            <tbody>
              <tr><td>Taux de chômage (BIT)</td><td>T1 2023</td><td>7,1 %</td><td>Insee{note(5)}</td></tr>
              <tr><td>Taux de chômage (BIT)</td><td>T4 2024</td><td>7,3 %</td><td>Insee{note(5)}</td></tr>
              <tr><td>Taux de chômage (BIT)</td><td>Moyenne 2025</td><td>7,7 %</td><td>Insee{note(2)}</td></tr>
              <tr><td>Taux de chômage (BIT)</td><td>T2 2026</td><td>8,3 %</td><td>Insee{note(1)}</td></tr>
              <tr><td>Nombre de chômeurs (BIT)</td><td>T2 2026</td><td>2,7 millions</td><td>Insee{note(1)}</td></tr>
              <tr><td>Taux d'emploi des 15-64 ans</td><td>Moyenne 2025</td><td>69,3 %</td><td>Insee{note(2)}</td></tr>
              <tr><td>Taux d'emploi des 15-64 ans</td><td>T2 2026</td><td>69,0 %</td><td>Insee{note(1)}</td></tr>
              <tr><td>Taux d'activité des 15-64 ans</td><td>Moyenne 2025</td><td>75,1 %</td><td>Insee{note(2)}</td></tr>
              <tr><td>Taux d'activité des 15-64 ans</td><td>T2 2026</td><td>75,4 %</td><td>Insee{note(1)}</td></tr>
              <tr><td>Taux d'emploi des 55-64 ans</td><td>2025</td><td>61,7 %</td><td>COR{note(6)}</td></tr>
            </tbody>
          </table>
        </div>
        <p>Au deuxième trimestre 2026, le chômage augmente de 0,2 point sur le trimestre et de 0,7 point sur un an, soit 261 000 chômeurs de plus en un an. C'est la sixième hausse trimestrielle consécutive. Le taux reste nettement inférieur à son pic de mi-2015 (2,2 points de moins).{note(1)} Le chômage des 15-24 ans atteint 21,6 %.{note(1)}</p>
        <p>Le taux d'emploi des 55-64 ans est passé de 41 % en 2010 à 61,7 % en 2025, selon le Conseil d'orientation des retraites.{note(6)}</p>
{encadre("À noter", f"<p>À partir du deuxième trimestre 2026, l'Insee publie ses indicateurs sur le champ « France », qui inclut désormais Mayotte. Les séries ont été recalculées sur ce nouveau champ. L'inclusion de Mayotte relève le taux de chômage de 0,06 point et abaisse le taux d'emploi des 15-64 ans de 0,17 point.{note(1)} Les moyennes annuelles 2025 du tableau ont été publiées avant ce changement : les comparer directement aux chiffres de 2026 mélange deux champs. Les évolutions sur un an indiquées par l'Insee dans sa publication d'août 2026 sont, elles, calculées sur le même champ.</p>")}
{encadre("À noter", f"<p>Le taux de chômage est estimé à partir d'une enquête, l'enquête Emploi, et non compté exhaustivement. L'Insee a longtemps indiqué une précision d'environ plus ou moins 0,3 point, sur le niveau comme sur la variation d'un trimestre à l'autre.{note(7)} Une hausse de 0,2 point en un trimestre est donc compatible avec une stabilité. C'est la succession de six hausses qui rend la tendance significative. Nous n'avons pas vérifié si cette marge a été révisée récemment.</p>")}

        <h2>L'emploi salarié et l'emploi non salarié</h2>
{encadre("Fait établi", f"<p>L'emploi salarié recule de 23 500 postes (-0,1 %) au deuxième trimestre 2026. Dans le secteur privé, la baisse atteint 0,4 % sur un an, soit 80 900 emplois.{note(3)}</p>")}
{encadre("Estimation", f"<p>Dans sa note de conjoncture de juin 2026, l'Insee prévoit 60 000 créations d'emplois non salariés en 2026, après 70 000 en 2025. Il anticipe un ralentissement au second semestre, lié à la réduction de l'aide aux créateurs d'entreprise (Acre).{note(4)} Il s'agit d'une prévision, publiée avant les chiffres du deuxième trimestre.</p>")}
        <p>Une hausse de l'emploi non salarié, notamment sous le statut de micro-entrepreneur, compte dans le taux d'emploi dès la première heure travaillée. Elle ne dit rien, à elle seule, du nombre d'heures ni des revenus de ces emplois.</p>

        <h2>Pourquoi les deux chiffres divergent</h2>
{encadre("Fait établi", f"<p>La population active a augmenté : le taux d'activité des 15-64 ans a atteint 75,1 % en 2025, son plus haut niveau depuis 1975.{note(2)} La hausse de l'emploi des seniors y contribue : 61,7 % des 55-64 ans étaient en emploi en 2025.{note(6)}</p>")}
{encadre("Interprétation", "<p>Le recul de l'âge légal de départ à la retraite décidé en 2023 maintient sur le marché du travail des personnes qui seraient auparavant parties à la retraite. Cette lecture est avancée par la Dares et le COR pour expliquer la progression de l'emploi des 60-64 ans. Nous n'avons pas pu consulter directement l'étude de la Dares : ce point repose sur des sources secondaires et reste à confirmer sur la publication d'origine.</p>")}
{encadre("Interprétation", f"<p>Lorsque la population active augmente plus vite que le nombre d'emplois, le chômage monte même si l'emploi ne baisse pas. Plusieurs économistes cités dans la presse avancent cette explication. Elle ne suffit plus pour 2026 : l'emploi salarié privé recule aussi sur un an au deuxième trimestre 2026.{note(3)} La hausse du chômage ne vient donc plus seulement de la croissance de la population active.</p>")}

        <h2>Deux lectures de la situation</h2>
        <div class="deux-lectures">
          <div>
            <p class="surtitre">Lecture 1</p>
            <h3>Une amélioration de fond</h3>
            <p>Le taux d'emploi reste proche de son record historique et l'emploi des seniors progresse fortement. La hausse du chômage reflète en partie l'arrivée sur le marché du travail de personnes qui en étaient absentes. Le chômage reste 2,2 points sous son pic de mi-2015.</p>
          </div>
          <div>
            <p class="surtitre">Lecture 2</p>
            <h3>Une dégradation en cours</h3>
            <p>Le chômage augmente depuis six trimestres consécutifs, le taux d'emploi recule depuis 2025 et l'emploi salarié privé baisse sur un an. Le chômage des jeunes dépasse 21 %. Les créations d'emplois non salariés ne compensent pas l'arrivée de nouveaux actifs.</p>
          </div>
        </div>
        <p>Les deux lectures s'appuient sur des chiffres exacts. Elles diffèrent surtout par la période retenue et l'indicateur mis en avant. La première regarde le niveau atteint, la seconde la tendance récente.</p>

        <h2>Ce qu'on ne sait pas</h2>
        <ul class="liste-inconnues">
          <li><strong>La part de chaque cause dans la hausse du chômage.</strong> Aucune publication que nous avons consultée ne chiffre la contribution respective des seniors, des jeunes et du ralentissement de l'économie.</li>
          <li><strong>L'effet de la loi pour le plein emploi.</strong> Depuis janvier 2025, les bénéficiaires du RSA sont inscrits automatiquement à France Travail. Avant la réforme, près d'un bénéficiaire sur deux l'était déjà.{note(8)} Cette inscription modifie les statistiques de France Travail ; son effet sur le chômage au sens du BIT, mesuré par enquête, est indirect et n'est pas chiffré dans les sources que nous avons consultées. Une affirmation selon laquelle elle expliquerait « la moitié » de la hausse circule dans la presse : nous n'en avons pas trouvé la source.</li>
          <li><strong>La qualité des emplois non salariés créés</strong> : heures travaillées et revenus.</li>
          <li><strong>La suite.</strong> Les prévisions disponibles portent sur quelques trimestres et sont régulièrement révisées.</li>
        </ul>

        <h2>Sources</h2>
        <ol class="sources">
{sources_html}
        </ol>

        <h2>Historique</h2>
        <ul class="historique">
          <li>8 octobre 2026 : première publication.</li>
        </ul>
        <p class="lien-correction">Une erreur ? Une source plus récente ? <a href="contact.html">Signalez-la</a>. Les corrections sont publiées sur la page <a href="methode.html#errata">Méthode</a>.</p>
      </div>
    </div>
  </article>'''
page("dossier-chomage-emploi.html", "Chômage et emploi",
     "Pourquoi le chômage remonte alors que le taux d'emploi est proche de son record : définitions, chiffres de l'Insee, explications et incertitudes.", dossier)
