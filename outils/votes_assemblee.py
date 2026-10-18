"""Extraction des scrutins de l'Assemblée nationale à partir de ses données ouvertes.

Sources : https://data.assemblee-nationale.fr (scrutins des XIVe à XVIIe législatures,
fichier AMO30 des acteurs, mandats et organes). Les archives sont téléchargées puis
décompressées dans un dossier, passé en argument :

    python3 outils/votes_assemblee.py DOSSIER

DOSSIER contient : 14/ 15/ 16/ 17/ (fichiers JSON des scrutins) et amo30/ (acteurs, organes).
Le script écrit deux fichiers dans outils/donnees/ :
- scrutins-solennels.json : chaque scrutin public solennel et chaque motion de censure
  des XVe, XVIe et XVIIe législatures, avec le vote de chaque groupe ;
- participation.json : le nombre de votants à chaque scrutin public (XIVe à XVIIe
  législature) et, pour les XVe à XVIIe, le nombre de scrutins publics tenus pendant le
  mandat de chaque député et le nombre de ceux auxquels il a pris part.
"""
import glob, json, os, re, sys
from collections import defaultdict

SRC = sys.argv[1]
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "donnees")


def scrutins(leg):
    for f in glob.glob(os.path.join(SRC, str(leg), "**", "*.json"), recursive=True):
        d = json.load(open(f, encoding="utf-8"))
        if "scrutins" in d:  # XIVe législature : un seul fichier
            yield from d["scrutins"]["scrutin"]
        else:
            yield d["scrutin"]


def liste(x):
    return x if isinstance(x, list) else ([x] if x else [])


def n(v):
    return int(v or 0)


# Organes : libellés des groupes politiques
ORGANES = {}
for f in glob.glob(os.path.join(SRC, "amo30", "**", "organe", "*.json"), recursive=True):
    o = json.load(open(f, encoding="utf-8"))["organe"]
    ORGANES[o["uid"]] = (o.get("libelleAbrege") or "", o.get("libelle") or "")


def categorie(code, titre):
    t = titre.lower().replace("’", "'")
    if code == "MOC":
        return "censure"
    if code == "SSG":  # Parlement réuni en Congrès (députés et sénateurs)
        return "congres"
    if "motion de rejet" in t or "motion de renvoi" in t or "motion référendaire" in t:
        return "procedure"
    if "déclaration" in t or "declaration" in t:
        return "declaration"
    if "proposition de résolution" in t and "l'ensemble" not in t:
        return "resolution"
    return "texte"


def decompte(v):
    """Les clés varient selon les législatures (abstention/abstentions, nonVotant/nonVotants)."""
    return {"pour": n(v.get("pour")), "contre": n(v.get("contre")),
            "abstention": n(v.get("abstentions", v.get("abstention"))),
            "non_votants": n(v.get("nonVotants", v.get("nonVotant")))}


# Acteurs : mandats de député, appartenance aux groupes et parti de rattachement déclaré
MANDATS = defaultdict(list)  # (législature, acteur) -> [(début, fin)]
GROUPES = defaultdict(list)  # organe du groupe -> [(acteur, début, fin)]
PARTIS = defaultdict(list)   # acteur -> [(début, fin, organe du parti)]
for f in glob.glob(os.path.join(SRC, "amo30", "**", "acteur", "*.json"), recursive=True):
    a = json.load(open(f, encoding="utf-8"))["acteur"]
    uid = a["uid"]["#text"] if isinstance(a["uid"], dict) else a["uid"]
    for m in liste(a.get("mandats", {}).get("mandat")):
        deb, fin = m.get("dateDebut") or "", m.get("dateFin") or "9999"
        if m.get("typeOrgane") == "ASSEMBLEE" and m.get("legislature") in ("14", "15", "16", "17"):
            MANDATS[(int(m["legislature"]), uid)].append((deb, fin))
        elif m.get("typeOrgane") == "GP":
            GROUPES[m["organes"]["organeRef"]].append((uid, deb, fin))
        elif m.get("typeOrgane") == "PARPOL":
            PARTIS[uid].append((deb, fin, m["organes"]["organeRef"]))


def parti(uid, date):
    """Parti de rattachement déclaré à cette date ; à défaut (déclarations annuelles commencées
    en décembre 2017), la première déclaration faite dans l'année qui suit."""
    for deb, fin, org in PARTIS[uid]:
        if deb <= date <= fin:
            return ORGANES.get(org, ("", ""))[1] or "Non déclaré"
    suivantes = sorted((deb, org) for deb, fin, org in PARTIS[uid] if date < deb <= str(int(date[:4]) + 1) + date[4:])
    return (ORGANES.get(suivantes[0][1], ("", ""))[1] or "Non déclaré") if suivantes else "Non déclaré"


# Les non-inscrits ne forment pas un groupe : on les répartit selon le parti auquel ils se sont
# rattachés (déclaration annuelle). Un parti comptant au moins 3 non-inscrits forme une ligne à part.
COURTS = {"Rassemblement national": "RN"}  # le Front national, renommé en 2018, est compté avec lui


def non_inscrits(organe, g, date):
    membres = [uid for uid, deb, fin in GROUPES[organe] if deb <= date <= fin]
    votes = {}
    nom = g["vote"].get("decompteNominatif") or {}
    for cle, pos in (("pours", "pour"), ("contres", "contre"), ("abstentions", "abstention")):
        for v in liste((nom.get(cle) or {}).get("votant")):
            votes[v["acteurRef"]] = pos
    membres = list(dict.fromkeys(membres + list(votes)))  # un votant absent de la liste des membres à cette date reste compté
    par = defaultdict(list)
    for uid in membres:
        p = parti(uid, date)
        par["Rassemblement national" if p.lower() in ("front national", "rassemblement national") else p].append(uid)
    sous, autres = [], []
    for p, uids in sorted(par.items(), key=lambda x: -len(x[1])):
        if len(uids) >= 3 and p != "Non déclaré":
            sous.append((p, uids))
        else:
            autres += uids
    if autres:
        sous.append(("autres", autres))
    out = []
    for p, uids in sous:
        c = {"pour": 0, "contre": 0, "abstention": 0}
        for uid in uids:
            if uid in votes:
                c[votes[uid]] += 1
        court = COURTS.get(p)
        out.append({"groupe": f"{court} (non-inscrits)" if court else ("Autres non-inscrits" if p == "autres" else f"{p} (non-inscrits)"),
                    "libelle": f"Députés non inscrits rattachés au parti {p}" if p != "autres" else "Autres députés non inscrits",
                    "membres": len(uids), "non_votants": 0, "non_inscrits": True, **c})
    return out


solennels = []
for leg in (15, 16, 17):
    for s in scrutins(leg):
        code = s["typeVote"]["codeTypeVote"]
        if code not in ("SPS", "MOC", "SSG", "SAT"):
            continue
        groupes = []
        for g in liste(s["ventilationVotes"]["organe"]["groupes"]["groupe"]):
            abr, lib = ORGANES.get(g["organeRef"], ("?", "?"))
            if abr == "NI" and code != "SSG":
                groupes += non_inscrits(g["organeRef"], g, s["dateScrutin"])
                continue
            groupes.append({"groupe": abr, "libelle": lib, "membres": n(g["nombreMembresGroupe"]), **decompte(g["vote"]["decompteVoix"])})
        objet = s.get("objet") or {}
        dossier = (objet.get("dossierLegislatif") or {}).get("libelle", "")
        solennels.append({
            "legislature": leg, "numero": int(s["numero"]), "date": s["dateScrutin"],
            "categorie": categorie(code, s["titre"]), "adopte": s["sort"]["code"] == "adopté",
            "titre": re.sub(r"\s+", " ", s["titre"]).strip(), "dossier": dossier,
            "total": decompte(s["syntheseVote"]["decompte"]), "groupes": groupes,
            "lien": f"https://www.assemblee-nationale.fr/dyn/{leg}/scrutins/{s['numero']}",
        })
solennels.sort(key=lambda x: (x["date"], x["legislature"], x["numero"]))

# Participation : un député « participe » à un scrutin public s'il vote pour, contre ou s'abstient.
# Le dénominateur est le nombre de scrutins publics tenus pendant ses mandats de la législature.

# Affluence : nombre de votants (pour, contre, abstention) à chaque scrutin public, XIVe à XVIIe législature.
# Le fichier de la XIVe législature ne détaille pas le vote de chaque député : on n'en tire que ces totaux.
affluence = {}
for leg in (14, 15, 16, 17):
    a = {"SPS": [], "SPO": [], "SPO_ecart_2": 0}
    for s in scrutins(leg):
        code = s["typeVote"]["codeTypeVote"]
        if code not in ("SPS", "SPO"):
            continue
        d = decompte(s["syntheseVote"]["decompte"])
        a[code].append(d["pour"] + d["contre"] + d["abstention"])
        if code == "SPO" and abs(d["pour"] - d["contre"]) <= 2:
            a["SPO_ecart_2"] += 1
    affluence[leg] = a

participation = {}
for leg in (15, 16, 17):
    dates, votes = [], defaultdict(int)
    for s in scrutins(leg):
        if s["typeVote"]["codeTypeVote"] not in ("SPO", "SPS"):
            continue
        dates.append(s["dateScrutin"])
        for g in liste(s["ventilationVotes"]["organe"]["groupes"]["groupe"]):
            nom = g["vote"].get("decompteNominatif") or {}
            for cle in ("pours", "contres", "abstentions"):
                for v in liste((nom.get(cle) or {}).get("votant")):
                    votes[v["acteurRef"]] += 1
    dates.sort()
    deputes = []
    for (l, uid), periodes in MANDATS.items():
        if l != leg:
            continue
        tenus = sum(1 for d in dates if any(deb <= d <= fin for deb, fin in periodes))
        if tenus >= 50:  # mandats trop courts exclus : taux non significatif
            deputes.append({"acteur": uid, "scrutins": tenus, "votes": votes.get(uid, 0)})
    participation[leg] = {"scrutins_publics": len(dates), "premier": dates[0], "dernier": dates[-1], "deputes": deputes}

os.makedirs(OUT, exist_ok=True)
json.dump(solennels, open(os.path.join(OUT, "scrutins-solennels.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
json.dump({"affluence": affluence, "participation": participation}, open(os.path.join(OUT, "participation.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(len(solennels), "scrutins solennels ;", {l: (len(a["SPS"]), len(a["SPO"])) for l, a in affluence.items()})
