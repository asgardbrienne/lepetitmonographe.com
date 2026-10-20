import sys, os, re
import html as _html
OUT = sys.argv[1]

NAV = [  # (page, libellé, pages rattachées)
    ("index.html", "Accueil", ()),
    ("dossiers.html", "Enquêtes", ("dossier-",)),
    ("livres.html", "Monographies", ("livre-",)),
    ("#rubriques", "Rubriques", ("politique-institutions.html", "economie-societe.html", "monde.html", "affaires-enquetes.html", "psychologie-societe-justice.html")),
    ("methode.html", "Méthode", ()),
    ("a-propos.html", "À propos", ()),
]
RUB_SEO = {  # page -> (titre affiché par les moteurs, description)
    "politique-institutions.html": ("Analyses politiques factuelles · Le Petit Monographe",
        "Analyses politiques factuelles et sourcées : institutions, élections, réformes, maintien de l'ordre, services publics. Chaque chiffre est vérifié à sa source."),
    "economie-societe.html": ("Économie et société : dossiers sourcés · Le Petit Monographe",
        "Dette, budget, retraites, fiscalité, emploi : des dossiers économiques sourcés, avec séries longues, comparaisons et limites des chiffres expliquées."),
    "monde.html": ("Actualité internationale décryptée · Le Petit Monographe",
        "Décisions internationales, conflits, énergie : ce qui a été décidé, ce qui reste incertain et ce que cela peut changer, sources officielles à l'appui."),
    "affaires-enquetes.html": ("Affaires judiciaires et enquêtes · Le Petit Monographe",
        "Affaires judiciaires et enquêtes : chronologies, pièces du dossier, expertises et état de la procédure, dans le respect de la présomption d'innocence."),
    "psychologie-societe-justice.html": ("Psychologie, société et justice · Le Petit Monographe",
        "Emprise, témoignage, mémoire, persuasion : ce que la recherche en psychologie et les décisions de justice établissent, études et méta-analyses à l'appui."),
}

NAV_RUBRIQUES = [
    ("politique-institutions.html", "Politique &amp; Institutions"),
    ("economie-societe.html", "Économie &amp; Société"),
    ("monde.html", "Monde"),
    ("affaires-enquetes.html", "Affaires &amp; Enquêtes"),
    ("psychologie-societe-justice.html", "Psychologie, Société &amp; Justice"),
]
LOUPE = '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M15.5 15.5 21 21" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>'

def _actif(fichier, h, rattachees):
    return fichier == h or any(fichier == r or (r.endswith("-") and fichier.startswith(r)) for r in rattachees)

def A(t):  # élément à compléter avant publication
    return f'<span class="a-completer">{t}</span>'

import hashlib as _hashlib
def _version(chemin):
    """Empreinte du fichier : chaque modification change l'adresse, le navigateur recharge."""
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", chemin), "rb") as f:
        return _hashlib.md5(f.read()).hexdigest()[:8]
V_CSS, V_JS = _version("assets/style.css"), _version("assets/site.js")

def meta_description(texte, limite=165):
    """Description pour les moteurs : phrases entières tant qu'elles tiennent dans la limite affichée par Google."""
    texte = re.sub(r"\s+", " ", _html.unescape(re.sub(r"<[^>]+>", "", texte))).strip()
    if len(texte) <= limite:
        return texte
    phrases, sortie = re.split(r"(?<=[.!?])\s+", texte), ""
    for ph in phrases:
        if len(sortie) + len(ph) + 1 > limite:
            break
        sortie = f"{sortie} {ph}".strip()
    if len(sortie) >= 90:
        return sortie
    coupe = texte[:limite - 1].rsplit(" ", 1)[0].rstrip(" ,;:")
    return coupe + "…"

def page(fichier, titre, description, corps, noindex=False, classe="", titre_seo=None, image=None, type_og="website"):
    liens = []
    for h, l, r in NAV:
        cur = ' aria-current="page"' if _actif(fichier, h, r) else ""
        if h == "#rubriques":
            sous = "".join(f'<li><a href="{rh}"{" aria-current=\"page\"" if rh == fichier else ""}>{rl}</a></li>' for rh, rl in NAV_RUBRIQUES)
            liens.append(f'''        <li class="nav-deroulant"><details><summary{" class=\"actif\"" if cur else ""}>{l}<svg viewBox="0 0 10 6" width="9" height="6" aria-hidden="true"><path d="M1 1l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.4"/></svg></summary><ul>{sous}</ul></details></li>''')
        else:
            liens.append(f'        <li><a href="{"./" if h == "index.html" else h}"{cur}>{l}</a></li>')
    nav = "\n".join(liens)
    titre_complet = titre_seo or f"{titre} · Le Petit Monographe"
    description = _html.escape(meta_description(description), quote=False).replace('"', "&quot;")
    robots = '\n  <meta name="robots" content="noindex">' if noindex else ""
    url = "https://lepetitmonographe.com/" + ("" if fichier == "index.html" else fichier)
    html = f'''<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{titre_complet}</title>
  <meta name="description" content="{description}">{robots}
  <link rel="canonical" href="{url}">
  <link rel="alternate" type="application/rss+xml" title="Le Petit Monographe : nouveaux dossiers" href="https://lepetitmonographe.com/flux.xml">
  <meta property="og:url" content="{url}">
  <link rel="icon" href="favicon.png" type="image/png">
  <link rel="apple-touch-icon" href="apple-touch-icon.png">
  <meta property="og:title" content="{titre_complet}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="https://lepetitmonographe.com/{image or "assets/logo-partage.jpg"}">
  <meta property="og:type" content="{type_og}">
  <meta property="og:site_name" content="Le Petit Monographe">
  <meta property="og:locale" content="fr_FR">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;0,8..60,600;1,8..60,400&display=swap">
  <link rel="stylesheet" href="assets/style.css?v={V_CSS}">
  <script>try{{var t=localStorage.getItem("lpm-theme");if(t)document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
</head>
<body{f' class="{classe}"' if classe else ""}>

<a class="evitement" href="#contenu">Aller au contenu</a>
<header class="entete">
  <div class="conteneur entete-haut">
    <button class="bouton-icone bouton-menu" type="button" aria-expanded="false" aria-controls="menu-principal" aria-label="Menu"><span class="bouton-menu-barres" aria-hidden="true"></span></button>
    <a class="logo" href="./"><img class="logo-img" src="assets/monogramme.png" alt="" width="48" height="48"><img class="logo-img-clair" src="assets/monogramme-clair.png" alt="" width="48" height="48"><span class="logo-texte"><span class="logo-nom">Le Petit Monographe</span><span class="logo-devise">Les faits d'abord. L'opinion reste au lecteur.</span></span></a>
    <div class="entete-droite">
      <form class="recherche-entete" action="dossiers.html" method="get" role="search">
        {LOUPE}
        <input type="search" name="q" placeholder="Rechercher…" aria-label="Rechercher un dossier">
      </form>
      <button class="bouton-icone bouton-theme" type="button" aria-label="Changer l'apparence (clair ou sombre)"><svg class="theme-lune" viewBox="0 0 24 24" width="17" height="17" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4 8 8 0 1 0 20 14.5z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg><svg class="theme-soleil" viewBox="0 0 24 24" width="17" height="17" aria-hidden="true"><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 2.5v2.5M12 19v2.5M2.5 12H5M19 12h2.5M5.3 5.3l1.8 1.8M16.9 16.9l1.8 1.8M5.3 18.7l1.8-1.8M16.9 7.1l1.8-1.8" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></button>
      <a class="bouton-icone bouton-loupe" href="dossiers.html#recherche" aria-label="Rechercher un dossier">{LOUPE}</a>
    </div>
  </div>
  <nav class="nav" id="menu-principal" aria-label="Navigation principale">
    <div class="conteneur nav-barre">
      <ul class="nav-liens">
{nav}
      </ul>
      <button class="bouton-theme nav-theme lien-fleche" type="button">Changer l'apparence (clair ou sombre)</button>
      <a class="bouton-lettre" href="./#lettre">Newsletter</a>
    </div>
  </nav>
</header>

<main id="contenu">
{corps}
</main>

<footer class="pied">
  <div class="conteneur pied-grille">
    <div>
      <p class="pied-marque">Le Petit Monographe</p>
      <p>Les faits d'abord. L'opinion reste au lecteur.</p>
    </div>
    <nav aria-label="Rubriques">
      <p class="pied-titre">Rubriques</p>
      <a href="dossiers.html">Tous les dossiers</a>
      <a href="politique-institutions.html">Politique &amp; Institutions</a>
      <a href="economie-societe.html">Économie &amp; Société</a>
      <a href="monde.html">Monde</a>
      <a href="affaires-enquetes.html">Affaires &amp; Enquêtes</a>
      <a href="psychologie-societe-justice.html">Psychologie, Société &amp; Justice</a>
      <a href="livres.html">Livres</a>
    </nav>
    <nav aria-label="Le site">
      <p class="pied-titre">Le site</p>
      <a href="methode.html">Notre méthode</a>
      <a href="methode.html#errata">Errata</a>
      <a href="a-propos.html">À propos</a>
      <a href="contact.html">Contact</a>
      <a href="mentions-legales.html">Mentions légales</a>
      <a href="confidentialite.html">Confidentialité</a>
      <a href="flux.xml">Flux RSS</a>
    </nav>
  </div>
  <div class="conteneur pied-bas">© 2026 Le Petit Monographe</div>
</footer>
<a class="haut-de-page" href="#contenu" aria-label="Revenir en haut de la page">↑</a>
<script src="assets/site.js?v={V_JS}" defer></script>
</body>
</html>
'''
    with open(os.path.join(OUT, fichier), "w") as f:
        f.write(html)

def tete(surtitre, h1, chapeau, classe=""):
    return f'''  <section class="tete-simple {classe}">
    <div class="conteneur">
      <nav class="ariane" aria-label="Fil d'Ariane"><a href="./">Accueil</a><span aria-hidden="true">›</span><span aria-current="page">{surtitre}</span></nav>
      <h1>{h1}</h1>
      {f'<p class="chapeau">{chapeau}</p>' if chapeau else ""}
    </div>
  </section>'''

def tete_visuel(ariane, h1, chapeau, visuel, credit=""):
    """En-tête des pages Monographies et Méthode : texte à gauche, visuel à droite."""
    return f'''  <section class="tete-visuel">
    <div class="conteneur tete-visuel-grille">
      <div class="tete-visuel-texte">
        <nav class="ariane" aria-label="Fil d'Ariane"><a href="./">Accueil</a><span aria-hidden="true">›</span><span aria-current="page">{ariane}</span></nav>
        <h1>{h1}</h1>
        <p class="chapeau">{chapeau}</p>
      </div>
      <figure class="tete-visuel-image">{visuel}{f'<figcaption>{credit}</figcaption>' if credit else ""}</figure>
    </div>
  </section>'''

# Charte V1.1 : cinq statuts d'information. Les nuances de la méthode
# (estimation, débat, allégation, expertise...) restent visibles en précision.
STATUTS = {
    "Fait établi": ("Fait établi", ""),
    "Témoignage": ("Témoignage", ""),
    "Interprétation": ("Interprétation", ""),
    "Hypothèse": ("Hypothèse", ""),
    "Proposition": ("Proposition", ""),
    "Estimation": ("Interprétation", "estimation chiffrée"),
    "Débat": ("Interprétation", "lectures divergentes"),
    "Expertise": ("Interprétation", "expertise"),
    "Allégation": ("Témoignage", "allégation non établie"),
    "Élément matériel": ("Fait établi", "élément matériel"),
    "État de la procédure": ("Fait établi", "état de la procédure"),
}
SLUG = {"Fait établi": "fait", "Témoignage": "temoignage", "Interprétation": "interpretation", "Hypothèse": "hypothese", "Proposition": "proposition"}
def badge(etiquette):
    if etiquette not in STATUTS:
        return f'<span class="etiquette etiquette-note">{etiquette}</span>'
    st, prec = STATUTS[etiquette]
    pr = f'<span class="precision">{prec}</span>' if prec else ""
    return f'<span class="etiquette statut statut-{SLUG[st]}">{st}{pr}</span>'

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
    ("monde.html", "c-monde", "Monde",
     "Décisions internationales, conflits, énergie : ce qui a été décidé, ce qui reste incertain, ce que cela peut changer."),
    ("affaires-enquetes.html", "c-affaires", "Affaires &amp; Enquêtes",
     "Chronologies judiciaires, pièces du dossier, expertises, faits établis et hypothèses."),
    ("psychologie-societe-justice.html", "c-psycho", "Psychologie, Société &amp; Justice",
     "Emprise, témoignage, mémoire, persuasion : ce que la recherche, le droit et les décisions de justice permettent d'établir. Ni conseils ni diagnostic individuel."),
]

AMAZON_MACRON = "https://www.amazon.fr/dp/B0HMC5NJ9V"
AMAZON_COMPTES = "https://www.amazon.fr/dp/B0HMC3C84M"
AMAZON_GREGORY = "https://www.amazon.fr/dp/B0GYQ8HRHG"
LIVRES = {
    "c-pouvoirs": [('<a href="livre-emmanuel-macron-le-bilan.html">Emmanuel Macron, le bilan</a>',
                    "Promesses, réformes, crises et affaires : la présidence passée au crible des faits (2017-2026).",
                    AMAZON_MACRON, "assets/couverture-macron.png")],
    "c-economie": [("Comment redresser les comptes de la France",
                    "Dette, déficit, retraites, dépenses publiques : 17 mesures chiffrées pour agir d'ici 2036. Faits, débats, calculs et propositions séparés.",
                    AMAZON_COMPTES, "assets/couverture-comptes.png")],
    "c-affaires": [("Grégory : pourquoi l'affaire n'a jamais été résolue",
                    "Les erreurs des premières 48 heures qui ont tout fait échouer. Volume 4 de la collection « Affaires qui ont choqué la France », environ 60 minutes de lecture.",
                    AMAZON_GREGORY, "assets/couverture-gregory.jpg")],
}
COLLECTION = {"c-pouvoirs": "Pouvoirs &amp; Société", "c-economie": "Pouvoirs &amp; Société", "c-affaires": "Affaires &amp; Enquêtes"}

def carte_livre(classe, titre, resume, lien=None, couverture=None):
    visuel = (f'<img src="{couverture}" alt="" width="142" height="231" loading="lazy">' if couverture
              else COLLECTION[classe])
    bouton = (f'<a class="bouton-contour" href="{lien}" target="_blank" rel="noopener">Voir sur Amazon<svg class="fleche" viewBox="0 0 16 10" width="14" height="9" aria-hidden="true"><path d="M0 5h14M10 1l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.4"/></svg></a>' if lien
              else f'<a class="bouton-contour" href="#" rel="noopener">{A("Lien Amazon")}</a>')
    return f'''        <article class="livre {classe}">
          <div class="couverture" aria-hidden="true">{visuel}</div>
          <div class="livre-texte">
            <h3>{titre}</h3>
            <p>{resume}</p>
            {bouton}
          </div>
        </article>'''

def grille_livres(classes):
    cartes = "\n".join(carte_livre(c, *l) for c in classes for l in LIVRES[c])
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

ICONES_STATUTS = {
    "fait": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 3h7l4 4v14H7z M14 3v4h4 M9.5 12h6 M9.5 15h6 M9.5 18h4" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>',
    "temoignage": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="9" cy="8.5" r="3" fill="none" stroke="currentColor" stroke-width="1.5"/><circle cx="16.5" cy="9.5" r="2.4" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M3.5 19c.6-3.3 2.8-5 5.5-5s4.9 1.7 5.5 5 M14.5 14.6c.6-.3 1.3-.4 2-.4 2.3 0 3.9 1.5 4.4 4.3" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>',
    "interpretation": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 19V12 M11 19V6 M16 19v-9 M3.5 19.5h17" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    "hypothese": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 9.2a3 3 0 1 1 4.4 2.6c-.9.5-1.4 1.1-1.4 2.2v.6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><circle cx="12" cy="18" r="1" fill="currentColor"/></svg>',
    "proposition": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8.5 14.5a5.5 5.5 0 1 1 7 0c-.7.6-1 1.3-1 2.1V17h-5v-.4c0-.8-.3-1.5-1-2.1z M10 20h4" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
}
STATUTS_ACCUEIL = [
    ("fait", "Fait établi", "Éléments vérifiés et sourcés."),
    ("temoignage", "Témoignage", "Paroles attribuées et datées."),
    ("interpretation", "Interprétation", "Analyses attribuées à leur auteur."),
    ("hypothese", "Hypothèse", "Pistes plausibles, non démontrées."),
    ("proposition", "Proposition", "Pistes d'action, distinctes des constats."),
]
_statuts_html = "\n".join(f'''          <li><span class="statut-icone">{ICONES_STATUTS[k]}</span><strong>{t}</strong> <span>{d}</span></li>''' for k, t, d in STATUTS_ACCUEIL)
_livres_accueil = "\n".join(f'''          <article class="livre-ligne"><img src="{couv}" alt="" width="96" height="144" loading="lazy"><div><h3>{re.sub(r"<[^>]+>", "", titre)}</h3><p>{resume}</p><a class="bouton bouton-fin" href="{lien}" target="_blank" rel="noopener">Voir sur Amazon</a></div></article>'''
                            for c in ["c-pouvoirs", "c-economie", "c-affaires"] for titre, resume, lien, couv in LIVRES[c])

# ---------- Rubriques ----------
DOSSIERS = {
    "c-economie": [("dossier-chomage-emploi.html", "Le chômage remonte, l'emploi reste élevé : comment lire les deux chiffres",
                    "Deux indicateurs qui semblent se contredire et mesurent des choses différentes. Données arrêtées au 8 octobre 2026.")],
}
# ---------- Livres ----------
_couvs = "".join(f'<img src="{couv}" alt="" width="142" height="231">' for c in ["c-economie", "c-pouvoirs", "c-affaires"] for _t, _r, _l, couv in LIVRES[c])
livres = tete_visuel("Monographies", "Monographies",
                     "Des ouvrages de référence pour comprendre en profondeur les grands enjeux français. Quand un article ne suffit plus, le livre approfondit l'ensemble du dossier : deux collections, une même méthode.",
                     f'<span class="couvertures-eventail">{_couvs}</span>') + "\n" + section("""      <div class="encart-methode definition-monographie">
        <h2>Qu'est-ce qu'une monographie ?</h2>
        <p>Une monographie est une « étude détaillée et complète d'un sujet particulier relativement restreint et se présentant normalement en un seul ouvrage », selon la définition de l'<a href="https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8353257/monographie" rel="noopener">Office québécois de la langue française</a>. Autrement dit : un livre entier consacré à un seul sujet, traité à fond.</p>
        <p>Le mot a aussi un sens plus courant dans le monde de l'art : un ouvrage <a href="https://www.lalanguefrancaise.com/dictionnaire/definition/monographie" rel="noopener">consacré à une personne</a>, par exemple à l'œuvre d'un peintre ou d'un photographe. C'est pourquoi une recherche sur Internet fait surtout apparaître de beaux livres illustrés. <strong>Les monographies du Petit Monographe ne sont pas des livres de photographies.</strong></p>
        <p>Ce sont des livres documentaires : un sujet d'actualité ou une affaire judiciaire, repris dans son ensemble, avec la chronologie, les chiffres, les décisions, les arguments de chaque camp et toutes les sources. Ils suivent la même <a href="methode.html">méthode</a> que les dossiers du site : faits établis et interprétations séparés, sources citées et datées, incertitudes signalées.</p>
      </div>""", "definition") + "\n" + section(f"""      <div class="collection c-pouvoirs">
        <div class="titre-section"><h2>Collection Pouvoirs &amp; Société</h2></div>
        <p class="intro">Politique, économie, institutions et grands débats français.</p>
{grille_livres(["c-pouvoirs", "c-economie"])}
      </div>
      <div class="collection c-affaires">
        <div class="titre-section"><h2>Collection Affaires &amp; Enquêtes</h2></div>
        <p class="intro">Affaires judiciaires, erreurs judiciaires, dossiers non résolus. Le dossier rendu lisible : chronologie, pièces, versions contradictoires, décisions de justice et zones d'ombre.</p>
{grille_livres(["c-affaires"])}
      </div>""")
page("livres.html", "Monographies", "Une monographie est un livre consacré à un seul sujet, étudié en détail. Ici, pas de livres de photographies : des dossiers documentaires complets et sourcés.", livres,
     titre_seo="Monographies : un sujet traité à fond · Le Petit Monographe")

# ---------- Méthode ----------
ETIQ = [
    ("Fait établi", "Donnée ou événement vérifiable, avec sa source et ses limites : donnée publique, texte officiel, décision de justice, rapport, archive, pièce du dossier."),
    ("Témoignage", "Parole attribuée, datée et contextualisée. Elle ne vaut pas preuve à elle seule. Une accusation non établie entre dans cette catégorie et est présentée comme telle."),
    ("Interprétation", "Analyse argumentée, explicitement attribuée à son auteur : économiste, institution, expert, commentateur. Les lectures concurrentes sont exposées."),
    ("Hypothèse", "Possibilité non confirmée, avec les conditions qui permettraient de la vérifier ou de l'écarter."),
    ("Proposition", "Mesure ou scénario, distinct des constats documentaires. Présentée comme un choix discutable, avec ses coûts et ses objections."),
]
ETIQ_JUDICIAIRE = [
    ("Estimation chiffrée", "Un chiffre calculé ou extrapolé, et non mesuré directement. Classé en interprétation, avec sa méthode et son auteur."),
    ("Lectures divergentes", "Une question où des positions sérieuses s'opposent. Classée en interprétation : chaque position est attribuée."),
    ("Expertise", "L'avis d'un expert désigné, avec sa méthode et ses limites. Classée en interprétation : une expertise peut être contredite."),
    ("Allégation non établie", "Une affirmation portée par une personne ou une partie. Classée en témoignage, jamais en fait."),
    ("Élément matériel, état de la procédure", "Une pièce du dossier ou une étape judiciaire exactement nommée : enquête, mise en examen, renvoi, procès, appel, condamnation définitive. Classés en fait établi lorsqu'ils sont documentés."),
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
    return "\n".join(f'''        <div>{badge(e) if e in STATUTS else f'<span class="etiquette etiquette-note">{e}</span>'}<p>{d}</p></div>''' for e, d in items)
regles = "\n".join(f'''        <li><h3>{t}</h3><p>{d}</p></li>''' for t, d in REGLES)
_statuts_cartes = "\n".join(f'''        <li class="statut-carte statut-carte-{k}"><span class="statut-icone">{ICONES_STATUTS[k]}</span><strong>{t}</strong> <span>{d}</span></li>''' for k, t, d in STATUTS_ACCUEIL)
methode = tete_visuel("Méthode", "Notre méthode",
                      "Une information rigoureuse, claire et sourcée. Nos dossiers distinguent cinq niveaux de lecture pour mieux comprendre les débats publics. Rigueur, impartialité, traçabilité, contradiction, transparence.",
                      '<img src="assets/images/methode.jpg" alt="La voûte de la salle Labrouste, à la Bibliothèque nationale de France" width="1400" height="770">',
                      'Salle Labrouste, Paris. Photo : <a href="https://commons.wikimedia.org/wiki/File:Biblioth%C3%A8que_nationale_de_France_Salle_Labrouste_Vo%C3%BBte.jpg" target="_blank" rel="noopener">Stefan Drößler, CC BY 4.0, recadrée, Wikimedia Commons</a>') + "\n" + section(f"""      <ul class="statuts-cartes">
{_statuts_cartes}
      </ul>
      <div class="deux-encarts">
        <section class="encart-methode">
          <h2>Nos sources</h2>
          <p>Des sources réelles et publiées, que chacun peut retrouver : données publiques, textes officiels, décisions de justice, rapports, médias identifiés. Chacune porte son titre, son auteur, sa date et un lien. Les sources primaires sont privilégiées ; les sources secondaires sont signalées comme telles.</p>
        </section>
        <section class="encart-methode">
          <h2>Notre démarche</h2>
          <p>Chaque dossier porte une date d'arrêt des données et un historique de mises à jour. Les arguments contraires sont présentés à leur meilleur niveau, la même exigence de preuve s'applique à tous les camps, et les erreurs sont corrigées publiquement.</p>
        </section>
      </div>""") + "\n" + section(f"""      <h2>Douze règles</h2>
      <p class="intro">Elles s'appliquent à chaque dossier, quel que soit le sujet ou le camp concerné.</p>
      <ol class="regles">
{regles}
      </ol>""") + "\n" + section("""      <div class="test-inversion">
        <p class="surtitre">Le test avant publication</p>
        <p class="question">« Si le nom ou le camp était inversé, appliquerions-nous exactement les mêmes critères ? »</p>
        <p>Si la réponse est non, l'article n'est pas prêt.</p>
      </div>""") + "\n" + section(f"""      <h2>Cinq statuts d'information</h2>
      <p class="intro">Dans chaque dossier, les passages décisifs portent leur statut, écrit en toutes lettres : la couleur ne suffit jamais. Un statut indique la nature d'une information, pas un tampon de vérité.</p>
      <div class="etiquettes">
{liste_etiq(ETIQ)}
      </div>
      <h3 class="sous-titre-etiq">Les précisions qui accompagnent un statut</h3>
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
page("methode.html", "Notre méthode", "Les douze règles éditoriales du Petit Monographe : faits et interprétations séparés, sources datées, même exigence pour tous les camps, corrections publiques.", methode,
     titre_seo="Méthode et règles éditoriales · Le Petit Monographe")

# ---------- À propos ----------
apropos = tete("À propos", "Le Petit Monographe", "Une publication indépendante, sans affiliation partisane.") + "\n" + section("""      <div class="prose">
        <p>Le Petit Monographe publie des dossiers et des monographies documentaires consacrés aux grands sujets politiques, économiques, sociaux et judiciaires contemporains. Une monographie est un livre consacré à un seul sujet, étudié en détail ; ce ne sont pas des livres de photographies (<a href="livres.html#definition">en savoir plus</a>).</p>
        <p>Il n'est lié à aucun parti, mouvement, syndicat ou candidat, et ne soutient aucune candidature. Traiter un sujet politique n'est pas prendre parti : les mêmes règles s'appliquent quel que soit le camp concerné.</p>
        <p>La méthode repose sur un principe simple : distinguer ce qui est établi de ce qui relève de l'interprétation, du débat ou de l'hypothèse. Chaque dossier s'appuie sur des sources identifiées et datées : données publiques, rapports officiels, décisions de justice, travaux parlementaires, archives, auditions et autres documents vérifiables. Lorsque les sources divergent ou qu'un élément demeure incertain, cette incertitude est signalée.</p>
        <p>Dans les affaires judiciaires, les faits établis, les accusations, les témoignages, les expertises et les hypothèses sont présentés séparément, dans le respect de la présomption d'innocence et de l'état réel des procédures.</p>
        <p>L'objectif n'est pas de dire au lecteur ce qu'il doit penser, mais de lui donner les éléments nécessaires pour comprendre, vérifier et se forger sa propre opinion.</p>
        <h2>Pourquoi les dossiers ne sont pas signés</h2>
        <p>Le Petit Monographe est édité par une personne physique, à titre non professionnel. Comme la loi le permet dans ce cas, son identité a été communiquée à l'hébergeur et n'est pas rendue publique (voir les <a href="mentions-legales.html">mentions légales</a>).</p>
        <p>Ce choix a une raison éditoriale : un dossier doit convaincre par ses sources, pas par le nom ou la notoriété de la personne qui l'écrit. C'est pourquoi l'anonymat s'accompagne d'obligations plus strictes que celles d'un article signé : chaque affirmation importante renvoie à une source publique que le lecteur peut ouvrir, chaque dossier porte sa date d'arrêt des données, et toute correction est rendue publique.</p>
        <p>La responsabilité éditoriale n'est pas diluée pour autant. Une erreur, une source mal citée ou un oubli peuvent être signalés par la page <a href="contact.html">Contact</a> ; ils sont examinés et, si le signalement est fondé, corrigés et inscrits dans l'<a href="methode.html#errata">historique des corrections</a>.</p>
        <h2>Comment un dossier est vérifié avant publication</h2>
        <ol>
          <li><strong>Rien de mémoire.</strong> Chaque chiffre, chaque date, chaque décision de justice est relu sur la publication d'origine avant d'être écrit.</li>
          <li><strong>La source d'abord.</strong> Les documents officiels, décisions, rapports et données publiques sont privilégiés. Un article de presse qui rapporte un document est signalé comme source secondaire.</li>
          <li><strong>Des sources que l'on peut ouvrir.</strong> Chaque source porte son titre, son auteur ou son média, sa date et un lien. Les liens sont contrôlés avant la mise en ligne.</li>
          <li><strong>Un statut pour chaque passage.</strong> Fait établi, témoignage, interprétation, hypothèse ou proposition : le lecteur sait toujours ce qu'il lit.</li>
          <li><strong>Ce qui ne se vérifie pas ne se publie pas.</strong> Une information sans source vérifiable est retirée, ou présentée explicitement comme non établie.</li>
          <li><strong>Le test du camp inversé.</strong> Avant publication, une question : si le nom ou le camp était inversé, appliquerions-nous exactement les mêmes critères ? Si la réponse est non, le dossier n'est pas prêt.</li>
          <li><strong>Une date et un historique.</strong> Chaque dossier indique la date d'arrêt de ses données et la date de sa dernière vérification.</li>
        </ol>
        <p>Cette méthode n'empêche pas toute erreur. En octobre 2026, tous les dossiers publiés ont été relus sur leurs sources d'origine ; les corrections qui en ont résulté sont listées, une par une, dans l'<a href="methode.html#errata">historique des corrections</a>.</p>
        <p class="signature">Les faits d'abord. L'opinion reste au lecteur.</p>
      </div>""")
page("a-propos.html", "À propos", "Le Petit Monographe, publication indépendante d'enquêtes et de dossiers documentaires sourcés sur la politique, l'économie, la société et la justice.", apropos)

# ---------- Contact ----------
contact = tete("Contact", "Écrire au Petit Monographe",
               "Presse, lecteurs, signalement d'une erreur ou d'une source : toute remarque argumentée et sourcée est lue.") + "\n" + section(f"""      <div class="prose">
        <p>Pour signaler une erreur, merci d'indiquer la publication, le passage concerné et, si possible, la source qui permet de la corriger.</p>
        <p><a class="bouton" href="#">{A("Adresse e-mail de contact")}</a></p>
      </div>""")
page("contact.html", "Contact", "Contacter Le Petit Monographe : questions de lecteurs, demandes de la presse, signalement d'une erreur ou d'une source plus récente.", contact)

# ---------- Mentions légales ----------
mentions = tete("Informations légales", "Mentions légales", "") + "\n" + section(f"""      <div class="prose">
        <h2>Éditeur du site</h2>
        <p>Ce site est édité par une personne physique, à titre non professionnel. Conformément à la loi pour la confiance dans l'économie numérique, son identité a été communiquée à l'hébergeur et n'est pas rendue publique.</p>
        <p>Contact : voir la page <a href="contact.html">Contact</a>.</p>
        <h2>Hébergement</h2>
        <p>GitHub, Inc. (service GitHub Pages), 88 Colin P. Kelly Jr. St., San Francisco, CA 94107, États-Unis. Site : <a href="https://github.com">github.com</a>.</p>
        <h2>Crédits photographiques</h2>
        <p>Les photographies proviennent de Wikimedia Commons et de Flickr, sous licence libre (domaine public, CC0, CC BY ou CC BY-SA). L'auteur, la licence et la source de chaque photo sont indiqués sous celle-ci, avec un lien vers sa page d'origine.</p>
        <h2>Liens vers Amazon</h2>
        <p>Les liens vers Amazon présents sur la page Livres et dans certains dossiers ne sont pas des liens affiliés : le site ne perçoit aucune commission sur les achats effectués à partir de ces liens.</p>
      </div>""")
page("mentions-legales.html", "Mentions légales", "Mentions légales du site Le Petit Monographe.", mentions, noindex=True)

# ---------- Confidentialité ----------
# À mettre à jour si un outil de statistiques ou une newsletter est ajouté.
conf = tete("Informations légales", "Confidentialité", "") + "\n" + section(f"""      <div class="prose">
        <h2>Cookies et mesure d'audience</h2>
        <p>Ce site ne dépose aucun cookie publicitaire ni de mesure d'audience.</p>
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
      <div class="livre-entete">
      <img class="couverture-grande" src="assets/couverture-macron.png" alt="Couverture du livre Emmanuel Macron, le bilan" width="142" height="231">
      <div>
      <p class="surtitre">Collection Pouvoirs &amp; Société</p>
      <h1>Emmanuel Macron, le bilan</h1>
      <p class="chapeau">Promesses, réformes, crises et affaires : la présidence passée au crible des faits (2017-2026).</p>
      <p style="margin:24px 0 0;font-size:.875rem;color:var(--encre-douce)">Première édition, octobre 2026 · Faits et données arrêtés au 6 octobre 2026</p>
      <p style="margin:20px 0 0"><a class="bouton" href="{AMAZON_MACRON}" target="_blank" rel="noopener">Voir sur Amazon</a></p>
      </div>
      </div>
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
    return f'''        <aside class="encadre">{badge(etiquette)}
          {contenu}
        </aside>'''

def note(n):
    return f'<sup class="appel"><a href="#source-{n}" id="appel-{n}">{n}</a></sup>'

SOURCES_CHOMAGE = [
    ("Insee, « Au deuxième trimestre 2026, le taux de chômage augmente de 0,2 point et atteint 8,3 % », Informations rapides n° 192, 7 août 2026.", "https://www.insee.fr/fr/statistiques/9032359"),
    ("Insee, « Une photographie du marché du travail en 2025 », Insee Première n° 2096, Émilie Pénicaud, 25 mars 2026.", "https://www.insee.fr/fr/statistiques/8901327"),
    ("Insee, « Au deuxième trimestre 2026, l'emploi salarié est quasi stable (-0,1 %) », Informations rapides n° 214, 28 août 2026.", "https://www.insee.fr/fr/statistiques/9039152"),
    ("Insee, Note de conjoncture, 17 juin 2026, fiche « Emploi ».", "https://www.insee.fr/fr/statistiques/fichier/9007912/ndc-juin-2026-emploi.pdf"),
    ("Insee, « Au quatrième trimestre 2024, le taux de chômage est quasi stable (-0,1 point) à 7,3 % », Informations rapides n° 34, 11 février 2025.", "https://www.insee.fr/fr/statistiques/fichier/version-html/8351234/IR34_Chomage_4T2024.pdf"),
    ("Conseil d'orientation des retraites, Rapport annuel, juin 2026, partie 4, chapitre 1.", "https://www.cor-retraites.fr/sites/default/files/2026-06/RA_Part4_Chap1.pdf"),
    ("Insee, Emmanuel Gros et Karim Moussallam, « Les méthodes d'estimation de la précision de l'Enquête Emploi en continu », Documents de travail n° M2016/02, 14 juin 2016.", "https://www.insee.fr/fr/statistiques/2022151"),
    ("Insee, « La situation sur le marché du travail des bénéficiaires du RSA à fin 2024 », Eliette Castelain et Vivien Guérin, Insee Analyses n° 108, 24 avril 2025.", "https://www.insee.fr/fr/statistiques/8562837"),
]
sources_html = "\n".join(f'          <li id="source-{i}">{t} <a href="{u}" rel="noopener">{u.replace("https://", "")}</a> <a href="#appel-{i}" class="retour" aria-label="Retour au texte">↑</a></li>' for i, (t, u) in enumerate(SOURCES_CHOMAGE, 1))

_CHOMAGE_ESSENTIEL = '''
            <li>Le taux de chômage est de 8,3 % au deuxième trimestre 2026, son plus haut niveau depuis le troisième trimestre 2020, après un point bas de 7,1 % début 2023 (champ hors Mayotte).{note(1)}{note(5)}</li>
            <li>Le taux d'emploi des 15-64 ans a atteint 69,3 % en moyenne en 2025, un niveau inédit depuis 1975. Il recule depuis : 69,0 % au deuxième trimestre 2026.{note(2)}{note(1)}</li>
            <li>Les deux chiffres n'ont pas le même dénominateur. Le chômage peut monter si davantage de personnes cherchent un emploi, même quand le nombre de personnes en emploi ne baisse pas.</li>
            <li>Selon l'Insee, les bénéficiaires du RSA et les jeunes inscrits à France Travail, publics visés par la loi pour le plein emploi, contribuent pour près de la moitié de la hausse du chômage depuis fin 2024 (+0,44 point sur +0,98 point). Cette contribution comptable ne distingue pas l'effet de la loi de celui de la conjoncture.{note(1)}</li>
          '''
_CHOMAGE_CORPS = f'''        <h2>Deux chiffres, deux dénominateurs</h2>
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
{encadre("À noter", f"<p>Le taux de chômage est estimé à partir d'une enquête, l'enquête Emploi, et non compté exhaustivement. L'Insee indique une précision de plus ou moins 0,3 point, sur le niveau comme sur la variation d'un trimestre à l'autre.{note(1)}{note(7)} Une hausse de 0,2 point en un trimestre est donc compatible avec une stabilité. C'est la succession de six hausses qui rend la tendance significative.</p>")}

        <h2>L'emploi salarié et l'emploi non salarié</h2>
{encadre("Fait établi", f"<p>L'emploi salarié recule de 23 500 postes (-0,1 %) au deuxième trimestre 2026. Dans le secteur privé, la baisse atteint 0,4 % sur un an, soit 80 900 emplois.{note(3)}</p>")}
{encadre("Estimation", f"<p>Dans sa note de conjoncture de juin 2026, l'Insee prévoit 60 000 créations d'emplois non salariés en 2026, après 70 000 en 2025. Il anticipe un ralentissement au second semestre, lié à la réduction de l'aide aux créateurs d'entreprise (Acre).{note(4)} Il s'agit d'une prévision, publiée avant les chiffres du deuxième trimestre.</p>")}
        <p>Une hausse de l'emploi non salarié, notamment sous le statut de micro-entrepreneur, compte dans le taux d'emploi dès la première heure travaillée. Elle ne dit rien, à elle seule, du nombre d'heures ni des revenus de ces emplois.</p>

        <h2>Pourquoi les deux chiffres divergent</h2>
{encadre("Fait établi", f"<p>La population active a augmenté : le taux d'activité des 15-64 ans a atteint 75,1 % en 2025, son plus haut niveau depuis 1975.{note(2)} La hausse de l'emploi des seniors y contribue : 61,7 % des 55-64 ans étaient en emploi en 2025.{note(6)}</p>")}
{encadre("Interprétation", f"<p>Selon le Conseil d'orientation des retraites, la hausse de l'emploi des seniors résulte en grande partie des réformes des retraites successives, dont celle de 2023, qui a reculé l'âge légal de départ : le taux d'emploi des 60-64 ans a progressé de 2,0 points en 2025, à 44,4 %. La loi de financement de la sécurité sociale pour 2026 a suspendu cette réforme : l'âge de 64 ans ne sera atteint qu'à partir de la génération 1969, au lieu de 1968.{note(6)}</p>")}
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
            <p>Le chômage augmente depuis six trimestres consécutifs, le taux d'emploi recule depuis 2025 et l'emploi salarié privé baisse sur un an. Le chômage des jeunes dépasse 21 %. Sur un an, l'emploi total ne progresse que de 47 000 postes, quand le nombre de chômeurs augmente de 261 000.{note(3)}{note(1)}</p>
          </div>
        </div>
        <p>Les deux lectures s'appuient sur des chiffres exacts. Elles diffèrent surtout par la période retenue et l'indicateur mis en avant. La première regarde le niveau atteint, la seconde la tendance récente.</p>

'''
_CHOMAGE_INCONNUES = f'''        <ul class="liste-inconnues">
          <li><strong>La part de chaque cause dans la hausse du chômage.</strong> L'Insee chiffre la contribution comptable des publics de la loi pour le plein emploi (voir ci-dessous), mais aucune publication que nous avons consultée ne chiffre celle des seniors ni celle du ralentissement de l'économie.</li>
          <li><strong>L'effet de la loi pour le plein emploi.</strong> Depuis début 2025, la loi prévoit l'inscription systématique des bénéficiaires du RSA à France Travail. Avant la réforme, près d'un bénéficiaire sur deux l'était déjà.{note(8)} L'Insee chiffre à +0,31 point la contribution des bénéficiaires du RSA à la hausse du chômage depuis fin 2024 (+0,98 point au total), et à +0,44 point celle de l'ensemble des publics visés par la loi, soit près de la moitié. Il précise que ces contributions, fragiles du fait des aléas d'enquête, ne permettent pas de distinguer l'effet de la loi de celui de la conjoncture.{note(1)}</li>
          <li><strong>La qualité des emplois non salariés créés</strong> : heures travaillées et revenus.</li>
          <li><strong>La suite.</strong> Les prévisions disponibles portent sur quelques trimestres et sont régulièrement révisées.</li>
        </ul>'''
_CHOMAGE_HISTORIQUE = '''
          <li>8 octobre 2026 : première publication.</li>
          <li>13 octobre 2026 : chiffres, dates et décisions relus sur les sources d'origine. Contribution de la loi pour le plein emploi chiffrée par l'Insee, suspension de la réforme des retraites et dates des sources ajoutées.</li>
        '''
DOSSIER_CHOMAGE = {"fichier": "dossier-chomage-emploi.html", "rubrique": "economie",
    "titre": "Le chômage remonte, l'emploi reste élevé : comment lire les deux chiffres",
    "titre_court": "Chômage et emploi",
    "chapeau": "Après trois années de quasi-stabilité, le taux de chômage augmente depuis début 2025 alors que le taux d'emploi a atteint en 2025 son plus haut niveau depuis 1975. Les deux chiffres sont exacts. Ils ne mesurent pas la même chose.",
    "resume": "Deux indicateurs qui semblent se contredire et mesurent des choses différentes. Données arrêtées au 8 octobre 2026.",
    "arret": "8 octobre 2026", "publication": "8 octobre 2026", "verifie": "13 octobre 2026",
    "image": "assets/images/dossier-chomage-emploi.jpg", "image_alt": "La cour de l'hôtel du Châtelet, siège du ministère du Travail, à Paris",
    "image_credit": "Croquant, CC BY-SA 3.0, recadrée, Wikimedia Commons", "image_lien": "https://commons.wikimedia.org/wiki/File:H%C3%B4tel_du_Ch%C3%A2telet_JP2011_fa%C3%A7ade_cour.jpg"}

# ---------- Dossiers écrits en format simple (outils/dossiers/*.txt) ----------
# Format : en-tête « clé: valeur » jusqu'à une ligne « --- », puis le corps.
# Corps : blocs séparés par une ligne vide.
#   ## Titre              -> intertitre
#   [Étiquette] texte     -> encadré étiqueté (Fait établi, Estimation, Débat...)
#   - élément             -> liste (lignes consécutives)
#   [n] dans le texte     -> appel de note vers la source n
#   texte                 -> paragraphe
# Sections spéciales : « ## Sources » (lignes « - texte | url ») et « ## Essentiel ».
import glob, json, re, html as _html

RUB_CLASSES = {"economie": "c-economie", "politique": "c-pouvoirs", "monde": "c-monde", "affaires": "c-affaires", "psychologie": "c-psycho"}
RUB_NOMS = {"economie": "Économie &amp; Société", "politique": "Politique &amp; Institutions", "monde": "Monde", "affaires": "Affaires &amp; Enquêtes", "psychologie": "Psychologie, Société &amp; Justice"}

def _inline(t):
    t = t.replace("&", "&amp;").replace("&amp;amp;", "&amp;")
    # typographie française : espace insécable avant ? ! ; : et à l'intérieur des guillemets
    t = re.sub(r" ([?!;:»])", "\u00a0\\1", t).replace("« ", "«\u00a0")
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\[(\d+)\]", lambda m: note(int(m.group(1))), t)
    return t

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import figures as _figures
import scrutins as _scrutins
_NUM_FIG = {"frise": 0, "fig": 0}

def _blocs(corps):
    out = []
    for bloc in [b.strip() for b in corps.strip().split("\n\n") if b.strip()]:
        m = re.match(r"^\[([^\]\d][^\]]*)\]\s*(.*)$", bloc, re.S)
        if bloc.startswith("[Figure]"):
            f = _figures.lire(bloc)
            k = "frise" if f["type"] == "frise" else "fig"
            _NUM_FIG[k] += 1
            out.append(_figures.rendre(f, _NUM_FIG[k], _inline))
        elif bloc.startswith("[Scrutins]"):
            out.append(_scrutins.rendre(bloc))
        elif bloc.startswith("## "):
            out.append(f"        <h2>{_inline(bloc[3:])}</h2>")
        elif m:
            out.append(encadre(m.group(1), f"<p>{_inline(m.group(2))}</p>"))
        elif bloc.startswith("- "):
            items = "".join(f"<li>{_inline(l[2:])}</li>" for l in bloc.split("\n"))
            out.append(f'        <ul class="liste-inconnues">{items}</ul>')
        else:
            out.append(f"        <p>{_inline(bloc)}</p>")
    return "\n".join(out)

def lire_dossier(chemin):
    brut = open(chemin, encoding="utf-8").read()
    tete_, corps = brut.split("\n---\n", 1)
    meta = dict(l.split(": ", 1) for l in tete_.strip().split("\n"))
    parties = re.split(r"^## (Essentiel|Sources|Ce qu'on ne sait pas)\s*$", corps, flags=re.M)
    texte = parties[0]; speciales = {}
    for i in range(1, len(parties), 2):
        contenu = parties[i + 1]
        if parties[i] == "Essentiel":
            # la liste de l'essentiel s'arrête au premier bloc ; la suite est le corps du dossier
            liste, _, suite = contenu.strip().partition("\n\n")
            contenu = liste
            texte += "\n\n" + suite
        speciales[parties[i]] = contenu
    # les sections normales peuvent suivre « Ce qu'on ne sait pas » : on les garde dans l'ordre
    return meta, texte, speciales

# ---------- Maquette « édition » : composants communs ----------
MOIS_COURT = {"janvier": "janv.", "février": "févr.", "mars": "mars", "avril": "avr.", "mai": "mai", "juin": "juin",
              "juillet": "juil.", "août": "août", "septembre": "sept.", "octobre": "oct.", "novembre": "nov.", "décembre": "déc."}
MOIS_NUM = {m: i for i, m in enumerate(MOIS_COURT, 1)}

def date_courte(d):
    """« 8 octobre 2026 » -> « 8 oct. 2026 » (affiché en capitales par la feuille de style)."""
    p = d.split()
    return f"{p[0]} {MOIS_COURT.get(p[1], p[1])} {p[2]}" if len(p) == 3 else d

def date_iso(d):
    p = d.split()
    return f"{p[2]}-{MOIS_NUM.get(p[1], 1):02d}-{int(p[0].replace('er', '')):02d}" if len(p) == 3 else ""

RUB_PAGES = {"c-pouvoirs": "politique-institutions.html", "c-economie": "economie-societe.html", "c-monde": "monde.html", "c-affaires": "affaires-enquetes.html", "c-psycho": "psychologie-societe-justice.html"}
RUB_COURTS = {"c-pouvoirs": "Politique", "c-economie": "Économie &amp; Société", "c-monde": "Monde", "c-affaires": "Affaires &amp; Enquêtes", "c-psycho": "Psychologie"}
FLECHE = '<svg class="fleche" viewBox="0 0 16 10" width="14" height="9" aria-hidden="true"><path d="M0 5h14M10 1l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>'
ICONE_IMPRIMER = '<svg viewBox="0 0 24 24" width="19" height="19" aria-hidden="true"><path d="M7 9V3h10v6M7 17H4v-7h16v7h-3M7 14h10v7H7z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>'
ICONE_LIEN = '<svg viewBox="0 0 24 24" width="19" height="19" aria-hidden="true"><path d="M10 14a4 4 0 0 0 5.7 0l3.5-3.5a4 4 0 0 0-5.7-5.7l-1.2 1.2M14 10a4 4 0 0 0-5.7 0l-3.5 3.5a4 4 0 0 0 5.7 5.7l1.2-1.2" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>'
ICONE_PARTAGER = '<svg viewBox="0 0 24 24" width="19" height="19" aria-hidden="true"><circle cx="6" cy="12" r="2.3" fill="none" stroke="currentColor" stroke-width="1.5"/><circle cx="17.5" cy="6" r="2.3" fill="none" stroke="currentColor" stroke-width="1.5"/><circle cx="17.5" cy="18" r="2.3" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="m8.1 11 7.3-3.9M8.1 13l7.3 3.9" stroke="currentColor" stroke-width="1.5"/></svg>'

def credit_photo(meta):
    credit = _inline(meta.get("image_credit", ""))
    if meta.get("image_lien"):
        credit = f'<a href="{meta["image_lien"]}" target="_blank" rel="noopener">{credit}</a>'
    return f"Photo : {credit}"

def gabarit_dossier(meta, essentiel, corps_html, inconnues_html, sources_html, n_sources, historique):
    """Page d'enquête : en-tête éditorial, image, sommaire, « En résumé », corps, sources, historique.
    Les repères <!--LECTURE-->, <!--SOMMAIRE--> et <!--LIREAUSSI--> sont remplis une fois tous les dossiers connus."""
    c = RUB_CLASSES[meta["rubrique"]]
    maj = meta.get("verifie") or meta["publication"]
    image = ""
    if meta.get("image"):
        image = f'''
      <figure class="article-image">
        <img src="{meta["image"]}" alt="{_html.escape(meta.get("image_alt", ""))}" width="1200" height="600" loading="eager">
        <figcaption>{_html.escape(meta.get("image_alt", ""))}. {credit_photo(meta)}</figcaption>
      </figure>'''
    bandeau = "" if meta.get("verifie") else '        <p class="a-completer bandeau-verif">Version de travail : chaque chiffre doit être relu sur la publication d\'origine avant mise en ligne.</p>\n'
    corps = f'''  <article class="article {c}">
    <header class="article-tete conteneur-article">
      <nav class="ariane" aria-label="Fil d'Ariane"><a href="./">Accueil</a><span aria-hidden="true">›</span><a href="{RUB_PAGES[c]}">{RUB_NOMS[meta["rubrique"]]}</a><span aria-hidden="true">›</span><span aria-current="page">{_inline(meta.get("titre_court", meta["titre"]))}</span></nav>
      <p class="article-meta"><a class="article-rubrique" href="{RUB_PAGES[c]}">{RUB_COURTS[c]}</a><time datetime="{date_iso(meta["publication"])}">{date_courte(meta["publication"])}</time><span><!--LECTURE--> min<span class="mobile-cache"> de lecture</span></span></p>
      <h1>{_inline(meta["titre"])}</h1>
      <p class="article-chapeau">{_inline(meta["chapeau"])}</p>
      <div class="article-signature">
        <span class="avatar" aria-hidden="true"><img class="logo-img" src="assets/monogramme.png" alt="" width="40" height="40"><img class="logo-img-clair" src="assets/monogramme-clair.png" alt="" width="40" height="40"></span>
        <p><strong>Par Le Petit Monographe</strong> <span>Mis à jour : {maj} · Données arrêtées au {meta["arret"]} · {n_sources} sources</span></p>
        <div class="article-outils">
          <button type="button" class="bouton-icone" data-action="imprimer" aria-label="Imprimer ou enregistrer en PDF" title="Imprimer ou enregistrer en PDF">{ICONE_IMPRIMER}</button>
          <button type="button" class="bouton-icone" data-action="copier" aria-label="Copier le lien du dossier" title="Copier le lien">{ICONE_LIEN}</button>
          <button type="button" class="bouton-icone" data-action="partager" aria-label="Partager ce dossier" title="Partager">{ICONE_PARTAGER}</button>
        </div>
      </div>{image}
    </header>
    <div class="conteneur-article article-corps prose">
<!--SOMMAIRE-->
        <aside class="en-resume" id="en-resume">
          <h2 class="en-resume-titre">En résumé</h2>
          <ul>{essentiel}</ul>
        </aside>
{bandeau}{corps_html}
        <h2>Ce qu'on ne sait pas</h2>
{inconnues_html}
        <h2>Sources</h2>
        <ol class="sources">
{sources_html}
        </ol>
        <h2>Historique</h2>
        <ul class="historique" id="corrections">{historique}</ul>
        <p class="lien-correction">Une erreur ? Une source plus récente ? <a href="contact.html">Signalez-la</a>. Les corrections sont publiées sur la page <a href="methode.html#errata">Méthode</a>.</p>
    </div>
  </article>
<!--LIREAUSSI-->'''
    page(meta["fichier"], meta.get("titre_seo") or meta.get("titre_court", meta["titre"]), meta.get("description") or meta["chapeau"], corps,
         classe="page-article", image=meta.get("image"), type_og="article")
    return meta

def rendre_dossier(chemin):
    _NUM_FIG.update(frise=0, fig=0)
    meta, texte, sp = lire_dossier(chemin)
    essentiel = "".join(f"<li>{_inline(l[2:])}</li>" for l in sp.get("Essentiel", "").strip().split("\n") if l.startswith("- "))
    sources = []
    for l in sp.get("Sources", "").strip().split("\n"):
        if l.startswith("- "):
            t, _, u = l[2:].partition(" | ")
            sources.append((t.rstrip(" |").strip(), u.strip()))
    src_html = "\n".join(
        f'          <li id="source-{i}">{_inline(t)}' + (f' <a href="{u}" rel="noopener">{u.replace("https://", "")}</a>' if u else "") + f' <a href="#appel-{i}" class="retour" aria-label="Retour au texte">↑</a></li>'
        for i, (t, u) in enumerate(sources, 1))
    historique = f'<li>{meta["publication"]} : première publication.</li>' + (
        f'<li>{meta["verifie"]} : chiffres, dates et décisions relus sur les sources d\'origine.{(" " + _inline(meta["corrections"])) if meta.get("corrections") else ""}</li>' if meta.get("verifie") else "")
    return gabarit_dossier(meta, essentiel, _blocs(texte), _blocs(sp.get("Ce qu'on ne sait pas", "").strip()), src_html, len(sources), historique)

gabarit_dossier(DOSSIER_CHOMAGE, _CHOMAGE_ESSENTIEL, _CHOMAGE_CORPS, _CHOMAGE_INCONNUES, sources_html, len(SOURCES_CHOMAGE), _CHOMAGE_HISTORIQUE)
_dossiers_simples = [rendre_dossier(f) for f in sorted(glob.glob(os.path.join(os.environ.get("LPM_DOSSIERS") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "dossiers"), "*.txt")))]
for m in _dossiers_simples:
    DOSSIERS.setdefault(RUB_CLASSES[m["rubrique"]], []).append((m["fichier"], _inline(m["titre"]), _inline(m["resume"])))

RUB_INFO = {  # classe -> (nom, page, clé de filtre)
    "c-pouvoirs": ("Politique &amp; Institutions", "politique-institutions.html", "politique"),
    "c-economie": ("Économie &amp; Société", "economie-societe.html", "economie"),
    "c-monde": ("Monde", "monde.html", "monde"),
    "c-affaires": ("Affaires &amp; Enquêtes", "affaires-enquetes.html", "affaires"),
    "c-psycho": ("Psychologie, Société &amp; Justice", "psychologie-societe-justice.html", "psychologie"),
}

def _texte_brut(h):
    return _html.unescape(re.sub(r"<[^>]+>", " ", h))

def _temps_lecture(fichier):
    # texte courant seulement : les sources, les listes de votes et les tableaux de données se consultent, ils ne se lisent pas d'une traite
    contenu = open(os.path.join(OUT, fichier), encoding="utf-8").read()
    corps = contenu.split('<main id="contenu">', 1)[1].split("</main>", 1)[0].split("<h2>Sources</h2>", 1)[0]
    corps = re.sub(r"<!--scrutins-->.*?<!--/scrutins-->|<table.*?</table>", " ", corps, flags=re.S)
    return max(1, round(len(_texte_brut(corps).split()) / 220))

def _texte_recherche(h, t, d):
    # texte intégral du dossier, sans les sources ni l'historique
    contenu = open(os.path.join(OUT, h), encoding="utf-8").read()
    corps = contenu.split('<main id="contenu">', 1)[1].split("<h2>Sources</h2>", 1)[0]
    corps = re.sub(r"<!--scrutins-->.*?<!--/scrutins-->", " ", corps, flags=re.S)  # listes de votes : hors recherche
    return _html.escape(re.sub(r"\s+", " ", _texte_brut(t + " " + d + " " + corps).lower()))

# Fiche de chaque dossier, utilisée par les cartes et les listes
INFOS = {}
for _m in [DOSSIER_CHOMAGE] + _dossiers_simples:
    _c = RUB_CLASSES[_m["rubrique"]]
    INFOS[_m["fichier"]] = {"c": _c, "titre": _inline(_m["titre"]), "court": _inline(_m.get("titre_court", _m["titre"])),
                            "resume": _inline(_m["resume"]), "image": _m.get("image", ""), "date": _m["publication"],
                            "min": _temps_lecture(_m["fichier"]), "meta": _m}

SITE = "https://lepetitmonographe.com"

def donnees_structurees(h):
    """Fiche schema.org de l'article et fil d'Ariane, pour les moteurs de recherche."""
    i, m = INFOS[h], INFOS[h]["meta"]
    nom_rub, page_rub, _k = RUB_INFO[i["c"]]
    editeur = {"@type": "Organization", "name": "Le Petit Monographe", "url": SITE + "/",
               "logo": {"@type": "ImageObject", "url": SITE + "/assets/monogramme.png"}}
    article = {"@context": "https://schema.org", "@type": "Article", "headline": _texte_brut(i["titre"]),
               "description": _texte_brut(i["resume"]), "inLanguage": "fr", "url": f"{SITE}/{h}",
               "mainEntityOfPage": f"{SITE}/{h}", "datePublished": date_iso(m["publication"]),
               "dateModified": date_iso(m.get("verifie") or m["publication"]),
               "articleSection": _texte_brut(nom_rub), "author": editeur, "publisher": editeur}
    if i["image"]:
        article["image"] = f"{SITE}/{i['image']}"
    ariane = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Accueil", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": _texte_brut(nom_rub), "item": f"{SITE}/{page_rub}"},
        {"@type": "ListItem", "position": 3, "name": _texte_brut(i["court"]), "item": f"{SITE}/{h}"}]}
    return "\n".join(f'  <script type="application/ld+json">{json.dumps(x, ensure_ascii=False).replace("</", "<\\/")}</script>' for x in (article, ariane))

def meta_carte(h):
    i = INFOS[h]
    return f'<span class="meta-ligne"><time datetime="{date_iso(i["date"])}">{date_courte(i["date"])}</time><span aria-hidden="true">|</span><span>{i["min"]} min</span></span>'

def carte(h, titre_niveau="h3"):
    i = INFOS[h]
    return f'''        <article class="carte {i["c"]}">
          <a href="{h}">
            <span class="carte-image"><img src="{i["image"]}" alt="" width="400" height="250" loading="lazy"></span>
            <span class="carte-texte">
              <span class="rubrique-etiquette">{RUB_COURTS[i["c"]]}</span>
              <{titre_niveau} class="carte-titre">{i["titre"]}</{titre_niveau}>
              {meta_carte(h)}
            </span>
          </a>
        </article>'''

def ligne(h, attributs=""):
    i = INFOS[h]
    return f'''        <article class="ligne {i["c"]}"{attributs}>
          <a href="{h}">
            <span class="ligne-image"><img src="{i["image"]}" alt="" width="320" height="200" loading="lazy"></span>
            <span class="ligne-texte">
              <span class="rubrique-etiquette">{RUB_COURTS[i["c"]]}</span>
              <h3 class="ligne-titre">{i["titre"]}</h3>
              <span class="ligne-resume">{i["resume"]}</span>
              {meta_carte(h)}
            </span>
          </a>
        </article>'''

# ---------- Page « Tous les dossiers » ----------
_liste = [(c, h, t, d, INFOS[h]["min"]) for c in ["c-monde", "c-pouvoirs", "c-economie", "c-affaires", "c-psycho"] for h, t, d in DOSSIERS.get(c, [])]
_lignes_toutes = "\n".join(ligne(h, f' data-rubrique="{RUB_INFO[c][2]}" data-texte="{_texte_recherche(h, t, d)}"') for c, h, t, d, m in _liste)
_filtres = "".join(f'<button type="button" class="filtre" data-filtre="{k}" aria-pressed="false">{n}</button>' for _, (n, _p, k) in RUB_INFO.items())
dossiers_page = f'''  <section class="tete-simple">
    <div class="conteneur">
      <nav class="ariane" aria-label="Fil d'Ariane"><a href="./">Accueil</a><span aria-hidden="true">›</span><span aria-current="page">Enquêtes</span></nav>
      <h1>Toutes les enquêtes</h1>
      <p class="chapeau">{len(_liste)} dossiers documentés. Cherchez par mot-clé ou filtrez par rubrique : chaque dossier sépare les faits établis, les débats et ce qu'on ne sait pas.</p>
    </div>
  </section>
  <section class="section">
    <div class="conteneur">
      <div class="barre-recherche" id="recherche">
        <label for="champ-recherche" class="visuellement-cache">Rechercher un dossier</label>
        <div class="champ-loupe">{LOUPE}<input type="search" id="champ-recherche" placeholder="Dette, Outreau, retraites, logement…" autocomplete="off"></div>
        <div class="onglets" role="group" aria-label="Filtrer par rubrique">
          <button type="button" class="filtre" data-filtre="tous" aria-pressed="true">Tous</button>{_filtres}
        </div>
        <p class="compteur" aria-live="polite"><span id="nb-resultats">{len(_liste)}</span> dossiers</p>
      </div>
      <div class="liste-lignes" id="liste-dossiers">
{_lignes_toutes}
      </div>
      <p class="vide-bloc" id="aucun-resultat" hidden>Aucun dossier ne correspond. Essayez un autre mot ou une autre rubrique.</p>
    </div>
  </section>'''
page("dossiers.html", "Toutes les enquêtes", "Tous les dossiers d'actualité sourcés du Petit Monographe : politique, économie, monde, affaires judiciaires et psychologie. Recherche par mot-clé et par rubrique.", dossiers_page,
     titre_seo="Toutes les enquêtes et dossiers sourcés · Le Petit Monographe")

# ---------- Dossiers : temps de lecture, sommaire numéroté, « À lire aussi » ----------
for c, h, t, d, m in _liste:
    chemin = os.path.join(OUT, h)
    s_ = open(chemin, encoding="utf-8").read().replace("<!--LECTURE-->", str(m), 1)
    titres = []
    def _ancre(mt):
        txt = _texte_brut(mt.group(1)).strip()
        ident = re.sub(r"[^a-z0-9]+", "-", txt.lower().translate(str.maketrans("àâäéèêëîïôöùûüçœ", "aaaeeeeiioouuuco"))).strip("-")
        titres.append((ident, mt.group(1)))
        return f'<h2 id="{ident}"><span class="h2-num">{len(titres) + 1}.</span> {mt.group(1)}</h2>'
    debut = s_.index('<div class="conteneur-article article-corps prose">')
    s_ = s_[:debut] + re.sub(r"<h2>(.*?)</h2>", _ancre, s_[debut:])
    items = [("en-resume", "En résumé")] + titres
    moitie = (len(items) + 1) // 2
    sommaire = f'''        <nav class="sommaire" aria-labelledby="sommaire-titre">
          <p class="sommaire-titre" id="sommaire-titre">{FLECHE}Sommaire</p>
          <ol style="--lignes:{moitie}">{"".join(f'<li><a href="#{i}">{tx}</a></li>' for i, tx in items)}</ol>
        </nav>'''
    s_ = s_.replace("<!--SOMMAIRE-->", sommaire, 1)
    if 'graphique-frise' in s_:
        s_ = s_.replace('<figure class="graphique graphique-frise">', '<figure class="graphique graphique-frise" id="chronologie">', 1)
    # liens choisis à la main (champ « voir_aussi », y compris d'autres rubriques), complétés par la même rubrique
    _choisis = [f.strip() for f in INFOS[h]["meta"].get("voir_aussi", "").split(",") if f.strip() in INFOS]
    autres = (_choisis + [x[0] for x in DOSSIERS.get(c, []) if x[0] != h and x[0] not in _choisis])[:3]
    nom, page_rub, _k = RUB_INFO[c]
    lire_aussi = f'''  <section class="section a-lire-aussi">
    <div class="conteneur">
      <div class="titre-section"><h2>À lire aussi</h2><a class="lien-fleche" href="{page_rub}">Tous les dossiers {nom}{FLECHE}</a></div>
      <div class="grille-cartes grille-3">
{"".join(carte(a) for a in autres)}
      </div>
    </div>
  </section>''' if autres else ""
    s_ = s_.replace("<!--LIREAUSSI-->", lire_aussi, 1)
    s_ = s_.replace("</head>", donnees_structurees(h) + "\n</head>", 1)
    if INFOS[h]["image"]:
        s_ = s_.replace('content="https://lepetitmonographe.com/assets/logo-partage.jpg"', f'content="{SITE}/{INFOS[h]["image"]}"', 1)
    s_ = s_.replace('<meta property="og:type" content="website">', '<meta property="og:type" content="article">', 1)
    open(chemin, "w", encoding="utf-8").write(s_)

# ---------- Pages de rubrique ----------
# Règle propre à la rubrique psychologie : quatre niveaux toujours séparés, pas de diagnostic à distance
RUB_METHODE = {"c-psycho": """  <section class="section section-claire">
    <div class="conteneur">
      <div class="titre-section"><h2>Ce que cette rubrique sépare toujours</h2><a class="lien-fleche" href="methode.html">Notre méthode""" + FLECHE + """</a></div>
      <div class="deux-encarts">
        <section class="encart-methode">
          <h3>Ce que les études établissent</h3>
          <p>Avec la population étudiée, la méthode et les limites des résultats. Une expérience de laboratoire ne vaut pas une mesure sur l'ensemble de la population.</p>
        </section>
        <section class="encart-methode">
          <h3>Ce que les témoignages rapportent</h3>
          <p>Attribués et datés, sans valeur de preuve générale. Un appel à témoignages n'est pas un échantillon représentatif.</p>
        </section>
        <section class="encart-methode">
          <h3>Ce que les décisions de justice établissent</h3>
          <p>Avec l'état exact de la procédure. Une décision judiciaire n'est pas une conclusion scientifique, et l'inverse non plus.</p>
        </section>
        <section class="encart-methode">
          <h3>Ce qui reste débattu</h3>
          <p>Les deux positions sont exposées quand la recherche se contredit. Aucun diagnostic n'est posé sur une personne, et les termes populaires ne sont pas présentés comme des catégories cliniques.</p>
        </section>
      </div>
    </div>
  </section>
"""}
RUB_BANDEAU = {"c-pouvoirs": "dossier-assemblee-sans-majorite.html", "c-economie": "dossier-dette-publique.html", "c-monde": "dossier-russie-sanctions-petrole.html", "c-affaires": "dossier-cour-justice-republique.html", "c-psycho": "dossier-parole-violences-sexuelles.html"}
_onglets = lambda actif: "".join(f'<a href="{p}"{" aria-current=\"page\"" if p == actif else ""}>{n}</a>' for p, n in [("dossiers.html", "Tous")] + NAV_RUBRIQUES)
for h, c, t, d in RUBRIQUES:
    b = INFOS[RUB_BANDEAU[c]]
    lignes_rub = "\n".join(ligne(x[0], f' data-ordre="{n}" data-titre="{_html.escape(_texte_brut(x[1]).lower())}" data-min="{INFOS[x[0]]["min"]}"') for n, x in enumerate(DOSSIERS.get(c, [])))
    corps = f'''  <section class="bandeau-rubrique {c}">
    <img class="bandeau-fond" src="{b["image"]}" alt="" width="1600" height="600">
    <div class="conteneur bandeau-contenu">
      <nav class="ariane" aria-label="Fil d'Ariane"><a href="./">Accueil</a><span aria-hidden="true">›</span><span>Rubriques</span><span aria-hidden="true">›</span><span aria-current="page">{t}</span></nav>
      <h1>{t.split(" &amp; ")[0] if c == "c-pouvoirs" else t}</h1>
      <p>{d}<br>{len(DOSSIERS.get(c, []))} enquête{"s" if len(DOSSIERS.get(c, [])) > 1 else ""} pour comprendre les décisions, les chiffres et les procédures.</p>
    </div>
    <p class="credit-bandeau">{_html.escape(b["meta"].get("image_alt", ""))}. {credit_photo(b["meta"])}</p>
  </section>
  <section class="section section-serree">
    <div class="conteneur">
      <div class="barre-rubrique">
        <nav class="onglets" aria-label="Rubriques">{_onglets(h)}</nav>
        <label class="tri">Trier par :
          <select data-tri="liste-rubrique">
            <option value="ordre">Sélection de la rédaction</option>
            <option value="titre">Titre (A à Z)</option>
            <option value="min">Lecture la plus courte</option>
          </select>
        </label>
      </div>
      <div class="liste-lignes" id="liste-rubrique">
{lignes_rub}
      </div>
    </div>
  </section>
{RUB_METHODE.get(c, "")}{"" if c not in LIVRES else f'''  <section class="section section-claire">
    <div class="conteneur">
      <div class="titre-section"><h2>Pour aller plus loin</h2><a class="lien-fleche" href="livres.html">Toutes les monographies{FLECHE}</a></div>
{grille_livres([c])}
    </div>
  </section>'''}'''
    page(h, t.replace("&amp;", "&"), RUB_SEO[h][1], corps, titre_seo=RUB_SEO[h][0])

# ---------- Accueil ----------
UNE = ["dossier-iran-ormuz-carburants.html", "dossier-russie-sanctions-petrole.html", "dossier-budget-2027.html", "dossier-assemblee-sans-majorite.html", "dossier-delais-justice-penale.html"]
DERNIERES = ["dossier-eau-outre-mer.html", "dossier-strategie-biais-reflexe.html", "dossier-maintien-ordre-manifestations.html", "dossier-detection-mensonge.html"]
_diapos = []
for n, h in enumerate(UNE):
    i = INFOS[h]
    _diapos.append(f'''      <article class="une-diapo" id="une-{n + 1}" aria-roledescription="diapositive" aria-label="{n + 1} sur {len(UNE)}">
        <img class="une-fond" src="{i["image"]}" alt="" width="1600" height="700"{' loading="lazy"' if n else ""}>
        <div class="conteneur une-contenu">
          <p class="une-surtitre">Enquête à la une</p>
          <h2 class="une-titre"><a href="{h}">{i["titre"]}</a></h2>
          <p class="une-chapeau">{i["resume"]}</p>
          <a class="bouton-or" href="{h}" tabindex="-1" aria-hidden="true">Lire l'enquête{FLECHE}</a>
          <p class="une-meta"><span>{RUB_COURTS[i["c"]]}</span><span aria-hidden="true">|</span>{meta_carte(h)}</p>
        </div>
        <p class="une-credit">{credit_photo(i["meta"])}</p>
      </article>''')
_points = "".join(f'<button type="button" class="une-point" data-cible="une-{n + 1}" aria-label="Enquête {n + 1}"{" aria-current=\"true\"" if n == 0 else ""}></button>' for n in range(len(UNE)))
PILIERS = [
    ("Une méthode transparente", "Cinq statuts pour distinguer les faits, les témoignages et les interprétations.",
     '<path d="M12 3 5 6v5c0 4.5 3 8 7 10 4-2 7-5.5 7-10V6z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="m9 12 2.2 2.2L15.5 10" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>'),
    ("Des sources vérifiables", "Documents publics, décisions et rapports, cités avec leur date et un lien.",
     '<path d="M7 3h7l4 4v14H7z M14 3v4h4" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="m9.5 14 2 2 3.5-4" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>'),
    ("Des enquêtes accessibles", "Des sujets complexes expliqués clairement, sans simplification abusive.",
     '<rect x="4" y="4" width="16" height="16" rx="1.5" fill="none" stroke="currentColor" stroke-width="1.5"/><circle cx="11" cy="11" r="3.2" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="m13.4 13.4 3 3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>'),
]
_piliers = "\n".join(f'''        <li><span class="pilier-icone"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true">{ic}</svg></span><span><strong>{t}</strong> {d}</span></li>''' for t, d, ic in PILIERS)
EXPLORER = [
    ("politique-institutions.html", "Politique", "Institutions, élections, vie démocratique", "assets/images/majorite.jpg"),
    ("economie-societe.html", "Économie &amp; Société", "Finances publiques, emploi, services publics", "assets/images/electricite.jpg"),
    ("monde.html", "Monde", "Décisions internationales, énergie, conflits", "assets/images/russie-sanctions-petrole.jpg"),
    ("affaires-enquetes.html", "Affaires &amp; Enquêtes", "Procédures, tribunaux, affaires judiciaires", "assets/images/cjr.jpg"),
    ("psychologie-societe-justice.html", "Psychologie, Société &amp; Justice", "Emprise, témoignage, mémoire, persuasion", "assets/images/parole-violences-sexuelles.jpg"),
    ("livres.html", "Monographies", "Le dossier complet, en un volume", "assets/couverture-comptes.png"),
]
_explorer = "\n".join(f'''        <a class="tuile" href="{h}"><span class="tuile-texte"><strong>{t}</strong> <span>{d}</span>{FLECHE}</span><span class="tuile-image{" tuile-livre" if "couverture" in img else ""}"><img src="{img}" alt="" width="160" height="160" loading="lazy"></span></a>''' for h, t, d, img in EXPLORER)
_nb_rub = {c: len(DOSSIERS.get(c, [])) for c in RUB_INFO}
PRESENTATION = [
    ("dossiers.html", "Des enquêtes documentées", f"{len(_liste)} dossiers qui séparent les faits établis, les témoignages, les débats et les hypothèses. Chaque chiffre est sourcé, avec un lien."),
    ("#rubriques", "Cinq rubriques", f"Politique et institutions ({_nb_rub['c-pouvoirs']}), économie et société ({_nb_rub['c-economie']}), monde ({_nb_rub['c-monde']}), affaires judiciaires ({_nb_rub['c-affaires']}), psychologie, société et justice ({_nb_rub['c-psycho']})."),
    ("livres.html", "Des monographies", "Pour aller plus loin : un sujet traité en profondeur, en un volume."),
    ("methode.html", "Une méthode publique", "Les règles appliquées à chaque dossier, et la liste datée des corrections."),
]
_presentation = "\n".join(f'''        <li><a href="{h}"><strong>{t}</strong> <span>{d}</span>{FLECHE}</a></li>''' for h, t, d in PRESENTATION)
_statuts_bande = "".join(f'<li><span class="statut-icone">{ICONES_STATUTS[k]}</span><strong>{t}</strong></li>' for k, t, d in STATUTS_ACCUEIL)
accueil = f'''  <h1 class="visuellement-cache">Le Petit Monographe : les faits d'abord, l'opinion reste au lecteur</h1>
  <section class="une" aria-roledescription="carrousel" aria-label="Enquêtes à la une">
    <div class="une-diapos" id="une-diapos" tabindex="-1">
{chr(10).join(_diapos)}
    </div>
    <div class="conteneur une-points" role="group" aria-label="Choisir une enquête à la une">{_points}</div>
  </section>

  <section class="presentation" aria-labelledby="presentation-titre">
    <div class="conteneur presentation-grille">
      <div class="presentation-texte">
        <p class="surtitre">Le Petit Monographe</p>
        <h2 id="presentation-titre">L'actualité factuelle</h2>
        <p>Des enquêtes de fond sur la politique, l'économie, l'actualité internationale, les affaires judiciaires et les mécanismes psychologiques et sociaux qui les traversent, fondées sur des sources identifiées et datées : textes officiels, données publiques, décisions de justice, rapports, presse de référence.</p>
        <p>Faits établis, témoignages, débats et hypothèses y sont présentés séparément, selon les mêmes règles pour tous les camps, avec ce qui reste inconnu. Au lecteur d'en tirer ses conclusions.</p>
        <a class="lien-fleche" href="a-propos.html">À propos du Petit Monographe{FLECHE}</a>
      </div>
      <div class="presentation-offre">
        <p class="presentation-sous-titre">Ce que vous trouverez ici</p>
        <ul class="presentation-liste">
{_presentation}
        </ul>
      </div>
    </div>
  </section>

  <section class="piliers-bande">
    <ul class="conteneur piliers">
{_piliers}
    </ul>
  </section>

  <section class="section" id="dernieres">
    <div class="conteneur">
      <div class="titre-section"><h2>Les dernières enquêtes</h2><a class="lien-fleche" href="dossiers.html">Toutes les enquêtes{FLECHE}</a></div>
      <div class="grille-cartes grille-4">
{chr(10).join(carte(h) for h in DERNIERES)}
      </div>
    </div>
  </section>

  <section class="section section-serree" id="rubriques">
    <div class="conteneur">
      <div class="titre-section"><h2>Explorer par rubrique</h2></div>
      <div class="tuiles">
{_explorer}
      </div>
    </div>
  </section>

  <section class="methode-bande">
    <div class="conteneur methode-bande-grille">
      <div>
        <h2>La méthode du Petit Monographe</h2>
        <p>Cinq statuts pour distinguer les faits, les témoignages et les interprétations. Chaque passage décisif porte le sien, écrit en toutes lettres.</p>
        <a class="bouton-or" href="methode.html">Découvrir notre méthode{FLECHE}</a>
      </div>
      <ul class="statuts-bande">{_statuts_bande}</ul>
    </div>
  </section>

  <section class="section" id="monographies">
    <div class="conteneur">
      <div class="titre-section"><h2>Monographies</h2><a class="lien-fleche" href="livres.html">Toutes les monographies{FLECHE}</a></div>
      <p class="intro">Une monographie est un livre consacré à un seul sujet, étudié en détail. Pas un livre de photographies : un dossier complet, sourcé, en un volume. <a href="livres.html#definition">Ce qu'est une monographie</a></p>
{grille_livres(["c-pouvoirs", "c-economie", "c-affaires"])}
    </div>
  </section>

  <section class="lettre-bande" id="lettre">
    <div class="conteneur lettre-bande-grille">
      <div>
        <h2>La Lettre du Petit Monographe</h2>
        <p>Les nouveaux dossiers, les mises à jour et une sélection de sources documentaires. Sans polémique ni surcharge.</p>
      </div>
      <p class="lettre-statut">Lancement prochain : l'inscription ouvrira ici.</p>
    </div>
  </section>'''
page("index.html", "Accueil",
     "Enquêtes indépendantes et dossiers d'actualité sourcés : politique, économie, justice, monde. Faits vérifiés, sources datées, aucune consigne d'opinion.",
     accueil, classe="page-accueil", titre_seo="Le Petit Monographe · Enquêtes et dossiers d'actualité sourcés")

# ---------- Errata : corrections datées, reprises de chaque dossier ----------
_errata = [(m.get("verifie", ""), m["fichier"], m.get("titre_court") or m["titre"], m["corrections"]) for m in _dossiers_simples if m.get("corrections")]
_errata.append(("13 octobre 2026", "dossier-chomage-emploi.html", "Chômage et emploi", "Contribution de la loi pour le plein emploi chiffrée par l'Insee, suspension de la réforme des retraites et dates des sources ajoutées."))
_lignes = "\n".join(f'''          <tr><td>{d}</td><td><a href="{f}">{_inline(t)}</a></td><td>Vérification sur les sources d'origine</td><td>{_inline(c)}</td></tr>''' for d, f, t, c in sorted(_errata, key=lambda e: e[2]))
_m = os.path.join(OUT, "methode.html")
_t = open(_m, encoding="utf-8").read()
_t = _t.replace('          <tr><td colspan="4" class="vide">Les corrections apparaîtront ici au fil des mises à jour.</td></tr>', _lignes)
open(_m, "w", encoding="utf-8").write(_t)

# ---------- Charte V1.1 : l'or réservé aux repères « Dossier » et « Collection » ----------
def _or(mm):
    # idempotent : une page non régénérée (aperçu de maquette) ne doit pas recevoir une balise de plus à chaque passage
    if '<span class="or">' in mm.group(0):
        return mm.group(0)
    return re.sub(r"\b(Dossier|Collection)\b", r'<span class="or">\1</span>', mm.group(0), count=1)
for _f in glob.glob(os.path.join(OUT, "*.html")):
    _t = open(_f, encoding="utf-8").read()
    _n = re.sub(r'<p class="surtitre"[^>]*>(?:(?!</p>).)*</p>', _or, _t)
    if _n != _t:
        open(_f, "w", encoding="utf-8").write(_n)

# ---------- Plan du site (sitemap.xml) et robots.txt ----------
import datetime
_urls = []
for _f in sorted(glob.glob(os.path.join(OUT, "*.html"))):
    _t = open(_f, encoding="utf-8").read()
    if 'name="robots" content="noindex' in _t or os.path.basename(_f) == "404.html" or os.path.basename(_f).startswith("google"):  # fichier de vérification Search Console
        continue
    _b = os.path.basename(_f)
    # date de modification : la dernière vérification pour un dossier ; aucune date inventée pour les autres pages
    _m = INFOS.get(_b, {}).get("meta")
    _urls.append(("https://lepetitmonographe.com/" + ("" if _b == "index.html" else _b), date_iso(_m.get("verifie") or _m["publication"]) if _m else ""))
_urls.sort(key=lambda u: (u[0] != "https://lepetitmonographe.com/", u[0]))
with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as _s:
    _s.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for _u, _d in _urls:
        _s.write(f"  <url><loc>{_u}</loc>" + (f"<lastmod>{_d}</lastmod>" if _d else "") + "</url>\n")
    _s.write("</urlset>\n")
# Flux RSS : les dossiers, du plus récent au plus ancien (date de dernière vérification)
from email.utils import format_datetime as _rfc822
def _date_rss(d):
    a, mo, j = map(int, date_iso(d).split("-"))
    return _rfc822(datetime.datetime(a, mo, j, 8, 0, tzinfo=datetime.timezone.utc))
_items = sorted(INFOS.items(), key=lambda kv: (date_iso(kv[1]["meta"].get("verifie") or kv[1]["date"]), date_iso(kv[1]["date"])), reverse=True)
with open(os.path.join(OUT, "flux.xml"), "w", encoding="utf-8") as _x:
    _x.write('<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n<channel>\n')
    _x.write(f'  <title>Le Petit Monographe</title>\n  <link>{SITE}/</link>\n  <description>Les faits d\'abord. L\'opinion reste au lecteur. Nouveaux dossiers et mises à jour.</description>\n  <language>fr</language>\n')
    _x.write(f'  <atom:link href="{SITE}/flux.xml" rel="self" type="application/rss+xml"/>\n')
    for _h, _i in _items:
        _m = _i["meta"]
        _x.write("  <item>\n"
                 f"    <title>{_html.escape(_texte_brut(_i['titre']))}</title>\n"
                 f"    <link>{SITE}/{_h}</link>\n    <guid isPermaLink=\"true\">{SITE}/{_h}</guid>\n"
                 f"    <pubDate>{_date_rss(_m.get('verifie') or _i['date'])}</pubDate>\n"
                 f"    <category>{_html.escape(_texte_brut(RUB_INFO[_i['c']][0]))}</category>\n"
                 f"    <description>{_html.escape(_texte_brut(_i['resume']))}</description>\n  </item>\n")
    _x.write("</channel>\n</rss>\n")
with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as _r:
    _r.write("User-agent: *\nAllow: /\n\nSitemap: https://lepetitmonographe.com/sitemap.xml\n")
