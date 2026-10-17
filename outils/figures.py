"""Graphiques et frises des dossiers, en HTML et CSS (sans bibliothèque).

Un graphique s'écrit dans le fichier d'un dossier comme un bloc, sans ligne vide :

    [Figure] barres            (barres verticales : série dans le temps)
    titre: Titre informatif
    unite: Unité, champ, période
    series: Série A | Série B  (seulement pour le type « groupes »)
    donnees:
    - 2019 | 146
    - 2026 | 63,4*             (* = prévision, hachurée)
    source: Organisme, publication, date [1]
    lecture: Une phrase qui explique correctement la figure.
    note: Limite méthodologique, rupture de série (facultatif).

Types : barres, barres-h (horizontales, valeurs négatives possibles), groupes (deux séries
côte à côte), frise (lignes « - date | événement | statut »).
Règles de la charte : barres partant de zéro, une seule échelle, étiquettes directes,
légende dès deux séries, tableau des données, source et date toujours visibles.
"""
import html, re


def _nombre(t):
    return float(t.replace(" ", "").replace(" ", "").replace(",", "."))


def _fr(v, modele):
    """Affiche v avec le même nombre de décimales que la saisie, à la française."""
    dec = len(modele.split(",")[1]) if "," in modele else 0
    s = f"{abs(v):,.{dec}f}".replace(",", " ").replace(".", ",")
    return ("-" if v < 0 else "") + s


def lire(bloc):
    lignes = bloc.split("\n")
    fig = {"type": lignes[0].split("]", 1)[1].strip() or "barres", "donnees": []}
    dans_donnees = False
    for l in lignes[1:]:
        if l.startswith("- ") and dans_donnees:
            fig["donnees"].append([c.strip() for c in l[2:].split("|")])
            continue
        cle, _, val = l.partition(":")
        cle = cle.strip()
        dans_donnees = cle == "donnees"
        if not dans_donnees:
            fig[cle] = val.strip()
    return fig


def rendre(fig, numero, inline):
    t = fig["type"]
    titre = inline(fig.get("titre", ""))
    unite = inline(fig.get("unite", ""))
    corps, tableau, legende = "", "", ""
    prevision = any(c.endswith("*") for r in fig["donnees"] for c in r[1:])

    if t == "frise":
        items = []
        for r in fig["donnees"]:
            date, evt = r[0], r[1] if len(r) > 1 else ""
            statut = r[2] if len(r) > 2 else ""
            cls = " fait-etabli" if statut.lower() == "fait établi" else ""
            badge = f'<span class="frise-statut{cls}">{html.escape(statut)}</span>' if statut else ""
            items.append(f'<li><span class="frise-date">{html.escape(date)}</span><span class="frise-texte">{inline(evt)}</span>{badge}</li>')
        corps = f'<ol class="frise">{"".join(items)}</ol>'
    else:
        series = [s.strip() for s in fig.get("series", "").split("|") if s.strip()] or [fig.get("titre", "")]
        rangs = [(r[0], r[1:]) for r in fig["donnees"]]
        valeurs = [_nombre(v.rstrip("*")) for _, vs in rangs for v in vs]
        vmax = max([abs(v) for v in valeurs] + [1e-9])
        negatif = min(valeurs) < 0

        def barre(v_txt, k):
            v = _nombre(v_txt.rstrip("*"))
            p = abs(v) / vmax * (50 if negatif else 100)
            cls = f"barre serie-{k}" + (" prevision" if v_txt.endswith("*") else "") + (" negative" if v < 0 else "")
            return v, p, cls, _fr(v, v_txt.rstrip("*"))

        if t == "barres":
            cols = []
            for lab, vs in rangs:
                v, p, cls, aff = barre(vs[0], 1)
                cols.append(f'<div class="col" title="{html.escape(lab)} : {aff}">'
                            f'<span class="col-piste"><span class="col-valeur">{aff}</span><span class="{cls}" style="height:{p * 1.6:.0f}px"></span></span>'
                            f'<span class="col-label">{html.escape(lab)}</span></div>')
            corps = f'<div class="barres-v" style="--n:{len(rangs)}">{"".join(cols)}</div>'
        else:  # barres-h et groupes
            lignes = []
            for lab, vs in rangs:
                bars = []
                for k, v_txt in enumerate(vs, 1):
                    v, p, cls, aff = barre(v_txt, k)
                    nom = f"{series[k-1]} : " if len(series) > 1 else ""
                    style = f"width:{p:.1f}%" + (f";margin-left:{50 - p:.1f}%" if negatif and v < 0 else (";margin-left:50%" if negatif else ""))
                    bars.append(f'<div class="h-ligne" title="{html.escape(lab)}, {html.escape(nom)}{aff}"><span class="h-piste{" h-centre" if negatif else ""}"><span class="{cls}" style="{style}"></span></span><span class="h-valeur">{aff}</span></div>')
                lignes.append(f'<div class="h-groupe"><span class="h-label">{html.escape(lab)}</span><div class="h-barres">{"".join(bars)}</div></div>')
            corps = f'<div class="barres-h">{"".join(lignes)}</div>'

        cles = []
        if len(series) > 1:
            cles += [f'<li><span class="cle serie-{k}"></span>{html.escape(s)}</li>' for k, s in enumerate(series, 1)]
        if prevision:
            cles.append('<li><span class="cle prevision"></span>Prévision</li>')
        if cles:
            legende = f'<ul class="graphique-legende">{"".join(cles)}</ul>'
        entetes = "".join(f"<th>{html.escape(s)}</th>" for s in (series if len(series) > 1 else [fig.get("unite", "Valeur")]))
        lignes_t = "".join(f'<tr><th scope="row">{html.escape(lab)}</th>' + "".join(
            f'<td>{_fr(_nombre(v.rstrip("*")), v.rstrip("*"))}{" (prévision)" if v.endswith("*") else ""}</td>' for v in vs) + "</tr>"
            for lab, vs in rangs)
        tableau = (f'<details class="graphique-donnees"><summary>Voir les données</summary><div class="tableau-defilant">'
                   f'<table class="tableau-donnees"><thead><tr><th></th>{entetes}</tr></thead><tbody>{lignes_t}</tbody></table></div></details>')

    pied = []
    if fig.get("lecture"):
        pied.append(f'<p><strong>Lecture :</strong> {inline(fig["lecture"])}</p>')
    if fig.get("note"):
        pied.append(f'<p><strong>Note :</strong> {inline(fig["note"])}</p>')
    if fig.get("source"):
        pied.append(f'<p><strong>Source :</strong> {inline(fig["source"])}</p>')
    classe = "graphique graphique-frise" if t == "frise" else "graphique"
    return f'''        <figure class="{classe}">
          <figcaption class="graphique-tete"><span class="graphique-num">{"Chronologie" if t == "frise" else "Figure"} {numero:02d}</span><span class="graphique-titre">{titre}</span>{f'<span class="graphique-unite">{unite}</span>' if unite else ""}</figcaption>
          {legende}{corps}
          <div class="graphique-pied">{"".join(pied)}</div>
          {tableau}
        </figure>'''
