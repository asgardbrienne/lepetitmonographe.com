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
    <span>© 2026 S. Enault · Le Petit Monographe</span>
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
      <p style="margin:8px 0 0;color:var(--encre-douce)">S. Enault · <a href="a-propos.html">À propos de l'auteur</a></p>""")}'''

page("index.html", "Accueil",
     "Le Petit Monographe : dossiers documentés sur la politique, l'économie, la société et les affaires judiciaires. Faits établis, désaccords, hypothèses et incertitudes clairement séparés.",
     accueil)

# ---------- Rubriques ----------
for h, c, t, d in RUBRIQUES:
    corps = tete("Rubrique", t, d, c) + "\n" + section(f"""      <h2>Les dossiers</h2>
      <div class="vide-bloc">Les premiers dossiers de cette rubrique sont en préparation.</div>""") + "\n" + section(f"""      <h2>Pour aller plus loin</h2>
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
page("livres.html", "Livres", "Les monographies de S. Enault : collections Pouvoirs & Société et Affaires & Enquêtes.", livres)

# ---------- Méthode ----------
ETIQ = [
    ("Fait établi", "Vérifiable dans une source identifiée et datée : donnée publique, décision de justice, texte officiel, rapport, archive."),
    ("Témoignage", "Ce qu'une personne déclare. Attribué nommément, daté, et jamais présenté comme un fait établi."),
    ("Interprétation", "Une lecture des faits, par l'auteur ou par un tiers. Toujours attribuée, et confrontée aux lectures concurrentes."),
    ("Hypothèse", "Une explication possible que les éléments disponibles ne permettent ni de confirmer ni d'écarter."),
    ("Proposition", "Une piste d'action. Présentée comme un choix discutable, avec ses coûts et ses objections."),
]
etiq = "\n".join(f'''        <div><span class="etiquette">{e}</span><p>{d}</p></div>''' for e, d in ETIQ)
methode = tete("Notre méthode", "Une méthode avant une opinion",
               "Le but n'est pas de dire au lecteur ce qu'il doit penser, mais de lui donner de quoi comprendre, vérifier et se forger sa propre opinion.") + "\n" + section(f"""{TYPOLOGIE}
      <div class="etiquettes">
{etiq}
      </div>""") + "\n" + section("""      <div class="prose">
        <h2>Les sources</h2>
        <p>Données publiques, rapports officiels, décisions de justice, travaux parlementaires, archives, auditions. Les sources primaires sont privilégiées. Une source secondaire peut être utilisée : elle est alors signalée comme telle. Chaque chiffre important est daté et renvoie à sa source.</p>
        <h2>Les désaccords</h2>
        <p>Les critiques et les arguments contraires sont présentés et attribués à leurs auteurs. Les désaccords sérieux sont exposés comme tels, sans être tranchés artificiellement. Un écart factuel ne suffit pas à prêter une intention de tromper.</p>
        <h2>L'incertitude</h2>
        <p>Quand les sources divergent ou qu'un élément reste incertain, c'est écrit plutôt que masqué.</p>
        <h2>Les affaires judiciaires</h2>
        <p>Faits établis, accusations, témoignages, expertises et hypothèses sont présentés séparément, dans le respect de la présomption d'innocence et de l'état réel des procédures.</p>
        <h2>Les corrections</h2>
        <p>Une erreur peut toujours se glisser, une source peut être révisée. Les corrections sont publiées ci-dessous, avec la date et le passage concerné.</p>
      </div>""") + "\n" + section("""      <h2>Errata et mises à jour</h2>
      <table class="tableau-errata">
        <thead>
          <tr><th>Date</th><th>Publication</th><th>Passage</th><th>Correction</th></tr>
        </thead>
        <tbody>
          <tr><td colspan="4" class="vide">Les corrections apparaîtront ici au fil des mises à jour.</td></tr>
        </tbody>
      </table>""", "errata")
page("methode.html", "Notre méthode", "Fait établi, témoignage, interprétation, hypothèse, proposition : comment Le Petit Monographe distingue chaque type d'information, cite ses sources et publie ses corrections.", methode)

# ---------- À propos ----------
apropos = tete("À propos", "S. Enault", "Auteur et éditeur du Petit Monographe.") + "\n" + section("""      <div class="prose">
        <p>S. Enault est l'auteur de monographies documentaires consacrées aux grands dossiers politiques, économiques, sociaux et criminels contemporains.</p>
        <p>Sa méthode repose sur un principe simple : distinguer ce qui est établi de ce qui relève de l'interprétation, du débat ou de l'hypothèse. Ses ouvrages s'appuient sur des sources identifiées et datées : données publiques, rapports officiels, décisions de justice, travaux parlementaires, archives, auditions et autres documents vérifiables. Lorsque les sources divergent ou qu'un élément demeure incertain, cette incertitude est signalée.</p>
        <p>Dans les affaires judiciaires, les faits établis, les accusations, les témoignages, les expertises et les hypothèses sont présentés séparément, dans le respect de la présomption d'innocence et de l'état réel des procédures.</p>
        <p>L'objectif n'est pas de dire au lecteur ce qu'il doit penser, mais de lui donner les éléments nécessaires pour comprendre, vérifier et se forger sa propre opinion.</p>
        <p class="signature">Les faits d'abord. Les désaccords ensuite. L'opinion reste au lecteur.</p>
      </div>""")
page("a-propos.html", "À propos", "S. Enault, auteur de monographies documentaires sur les grands dossiers politiques, économiques, sociaux et criminels.", apropos)

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
        <p>{A("Identité de l'éditeur (nom ou dénomination, adresse, e-mail), ou, pour un particulier publiant à titre non professionnel, mention que ces informations ont été communiquées à l'hébergeur")}</p>
        <h2>Directeur de la publication</h2>
        <p>{A("Nom du directeur de la publication")}</p>
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
      <p style="margin:24px 0 0;font-size:.875rem;color:var(--encre-douce)">S. Enault · Première édition, octobre 2026 · Faits et données arrêtés au 6 octobre 2026</p>
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
     "Emmanuel Macron, le bilan, de S. Enault. Promesses, réformes, crises et affaires : la présidence passée au crible des faits (2017-2026).", macron)
