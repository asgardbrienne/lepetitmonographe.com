"""Tableaux et graphiques de votes à partir de outils/donnees/scrutins-solennels.json
(produit par outils/votes_assemblee.py).

Dans le fichier d'un dossier, un bloc sur une ligne :

    [Scrutins] synthese 15      (position de chaque groupe sur les textes, XVe législature)
    [Scrutins] liste 15         (chaque vote solennel sur un texte, groupe par groupe)
    [Scrutins] censures         (toutes les motions de censure 2017-2026)
    [Scrutins] autres           (déclarations du Gouvernement, résolutions, motions de procédure, Congrès)

Couleurs : bleu nuit = pour, or = contre, gris = abstention. Aucune couleur de parti.
"""
import html, json, os, re
from collections import Counter, defaultdict

_F = os.path.join(os.path.dirname(os.path.abspath(__file__)), "donnees", "scrutins-solennels.json")
S = json.load(open(_F, encoding="utf-8")) if os.path.exists(_F) else []

LEG = {15: "XVe législature (2017-2022)", 16: "XVIe législature (2022-2024)", 17: "XVIIe législature (depuis 2024)"}
MOIS = ["janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc."]
POS = {"pour": "Pour", "contre": "Contre", "abstention": "Abstention"}


def _date(d):
    a, m, j = d.split("-")
    return f"{int(j)} {MOIS[int(m) - 1]} {a}"


def _e(t):
    return html.escape(t, quote=True)


def position(g):
    """Position du groupe : le choix le plus fréquent parmi ses membres qui ont voté."""
    c = {k: g[k] for k in POS}
    return max(c, key=c.get) if sum(c.values()) else "absent"


def _pct(x, tot):
    return 0 if not tot else round(100 * x / tot)


def barre(p, c, a, etiquette=""):
    tot = p + c + a
    seg = "".join(f'<span class="vb-{k}" style="width:{100 * v / tot:.2f}%"></span>' for k, v in (("pour", p), ("contre", c), ("abstention", a)) if v and tot)
    titre = f"{etiquette} : " if etiquette else ""
    return f'<span class="vote-barre" role="img" aria-label="{_e(titre)}{p} pour, {c} contre, {a} abstentions">{seg}</span>'


LEGENDE = ('<ul class="vote-legende"><li><span class="vb-pour"></span>Pour</li><li><span class="vb-contre"></span>Contre</li>'
           '<li><span class="vb-abstention"></span>Abstention</li></ul>')


def _textes(leg):
    return [s for s in S if s["legislature"] == leg and s["categorie"] == "texte"]


def synthese(leg):
    textes = _textes(leg)
    agg, libelles = defaultdict(Counter), {}
    for s in textes:
        for g in s["groupes"]:
            if g["groupe"] == "NI":  # les non-inscrits ne forment pas un groupe
                continue
            agg[g["groupe"]][position(g)] += 1
            libelles[g["groupe"]] = g["libelle"]
    lignes = []
    for grp, c in sorted(agg.items(), key=lambda x: (-sum(x[1].values()), x[0])):
        n = c["pour"] + c["contre"] + c["abstention"]
        if n < 5:
            continue
        lignes.append(f'''<li class="vote-ligne"><span class="vote-groupe"><abbr title="{_e(libelles[grp])}">{_e(grp)}</abbr><span class="vote-nb">{n} textes</span></span>{barre(c["pour"], c["contre"], c["abstention"], grp)}<span class="vote-chiffres"><b class="t-pour">{_pct(c["pour"], n)} %</b> · <b class="t-contre">{_pct(c["contre"], n)} %</b> · <b class="t-abstention">{_pct(c["abstention"], n)} %</b></span></li>''')
    noms = "".join(f"<li><b>{_e(g)}</b> : {_e(libelles[g])}</li>" for g in sorted(agg, key=lambda x: -sum(agg[x].values())) if sum(agg[g][k] for k in POS) >= 5)
    return f'''        <figure class="graphique graphique-votes">
          <figcaption class="graphique-tete"><span class="graphique-num">Votes</span><span class="graphique-titre">{LEG[leg]} : position de chaque groupe sur les {len(textes)} textes soumis à un vote solennel</span><span class="graphique-unite">Part des textes sur lesquels la majorité des membres votants du groupe a voté pour, contre ou s'est abstenue</span></figcaption>
          {LEGENDE}
          <ol class="vote-lignes">{"".join(lignes)}</ol>
          <div class="graphique-pied"><p><strong>Lecture :</strong> la barre d'un groupe se lit de gauche à droite : part des textes votés pour, contre, puis en s'abstenant. Les groupes ayant voté sur moins de cinq textes ne sont pas affichés, ni les députés non inscrits, qui ne forment pas un groupe. Un groupe peut avoir changé de nom ou de composition en cours de législature.</p><p><strong>Source :</strong> Assemblée nationale, données ouvertes des scrutins, calcul Le Petit Monographe.</p></div>
          <details class="graphique-donnees"><summary>Noms complets des groupes</summary><ul class="vote-noms">{noms}</ul></details>
        </figure>'''


def _lecture(titre):
    m = re.search(r"\(([^()]*(lecture|paritaire|définitive|Congrès)[^()]*)\)", titre, re.I)
    return m.group(1) if m else ""


def _intitule(s):
    t = s["dossier"] or re.sub(r"^l[’']ensemble (du|de la|des) ", "", s["titre"])
    t = re.sub(r"\s*\([^()]*\)\.?$", "", t).rstrip(".")
    return t[:1].upper() + t[1:]


def _puces(s):
    out = []
    for g in sorted(s["groupes"], key=lambda g: -g["membres"]):
        p = position(g)
        if p == "absent" or g["groupe"] == "NI":
            continue
        out.append(f'<span class="puce p-{p}" title="{_e(g["libelle"])} : {g["pour"]} pour, {g["contre"]} contre, {g["abstention"]} abstentions">{_e(g["groupe"])}<span class="visuellement-cache"> : {POS[p].lower()}</span></span>')
    return "".join(out)


def _ligne(s):
    t = s["total"]
    lecture = _lecture(s["titre"])
    return f'''<li class="scrutin">
            <div class="scrutin-tete"><time datetime="{s["date"]}">{_date(s["date"])}</time><span class="scrutin-sort {"adopte" if s["adopte"] else "rejete"}">{"Adopté" if s["adopte"] else "Rejeté"}</span></div>
            <p class="scrutin-titre"><a href="{s["lien"]}" target="_blank" rel="noopener">{_e(_intitule(s))}</a>{f'<span class="scrutin-lecture">{_e(lecture)}</span>' if lecture else ""}</p>
            <div class="scrutin-total">{barre(t["pour"], t["contre"], t["abstention"], "Ensemble des votants")}<span class="vote-chiffres">{t["pour"]} pour · {t["contre"]} contre · {t["abstention"]} abst.</span></div>
            <div class="scrutin-puces">{_puces(s)}</div>
          </li>'''


def liste(leg):
    textes = _textes(leg)
    par_an = defaultdict(list)
    for s in textes:
        par_an[s["date"][:4]].append(s)
    blocs = "".join(f'''
        <details class="scrutins-annee"{" open" if i == 0 else ""}><summary>{an} <span>{len(v)} vote{"s" if len(v) > 1 else ""}</span></summary>
          <ol class="scrutins">{"".join(_ligne(s) for s in v)}</ol>
        </details>''' for i, (an, v) in enumerate(sorted(par_an.items())))
    return f'''        <!--scrutins--><div class="scrutins-bloc">
          <p class="scrutins-aide">{LEGENDE}Sous chaque texte, chaque groupe est coloré selon le vote de la majorité de ses membres votants (les non-inscrits ne sont pas représentés) ; le détail des voix s'affiche au survol et sur la page officielle du scrutin.</p>{blocs}
        </div><!--/scrutins-->'''


def censures():
    cs = [s for s in S if s["categorie"] == "censure"]
    lignes = []
    for s in cs:
        pour = s["total"]["pour"]
        soutiens = ", ".join(f'{_e(g["groupe"])} ({g["pour"]})' for g in sorted(s["groupes"], key=lambda g: -g["pour"]) if g["pour"])
        lignes.append(f'<tr><td class="date"><a href="{s["lien"]}" target="_blank" rel="noopener">{"/".join(reversed(s["date"].split("-")))}</a></td><td class="nb">{pour}</td><td>{"<strong>Adoptée</strong>" if s["adopte"] else "Rejetée"}</td><td>{soutiens}</td></tr>')
    return f'''        <div class="tableau-defilant">
          <table class="tableau-donnees tableau-censures"><caption>Les {len(cs)} motions de censure votées depuis 2017 (XVe à XVIIe législature)</caption>
            <thead><tr><th>Date</th><th>Voix pour</th><th>Résultat</th><th>Voix pour, par groupe</th></tr></thead>
            <tbody>{"".join(lignes)}</tbody></table>
        </div>'''


AUTRES = {"declaration": "Déclarations du Gouvernement", "resolution": "Propositions de résolution", "procedure": "Motions de procédure", "congres": "Parlement réuni en Congrès"}


def autres():
    blocs = []
    for cat, nom in AUTRES.items():
        v = [s for s in S if s["categorie"] == cat]
        if v:
            blocs.append(f'''
        <details class="scrutins-annee"><summary>{nom} <span>{len(v)} vote{"s" if len(v) > 1 else ""}</span></summary>
          <ol class="scrutins">{"".join(_ligne(s) for s in v)}</ol>
        </details>''')
    return f'        <!--scrutins--><div class="scrutins-bloc">{"".join(blocs)}\n        </div><!--/scrutins-->'


def compter(leg=None, categorie=None):
    return sum(1 for s in S if (leg is None or s["legislature"] == leg) and (categorie is None or s["categorie"] == categorie))


def rendre(bloc):
    p = bloc.split()[1:]
    if p[0] == "synthese":
        return synthese(int(p[1]))
    if p[0] == "liste":
        return liste(int(p[1]))
    if p[0] == "censures":
        return censures()
    if p[0] == "autres":
        return autres()
    raise ValueError(bloc)
