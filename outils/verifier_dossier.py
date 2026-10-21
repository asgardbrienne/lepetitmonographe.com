"""Contrôle automatique d'un ou plusieurs fichiers de dossier, sans générer le site.

Usage : python3 outils/verifier_dossier.py outils/dossiers/01-dette-publique.txt [...]
Vérifie : champs d'en-tête, appels de note hors liste, sources jamais citées, sources sans lien,
tirets cadratins, « vraiment » ou « réellement » dans les titres, étiquettes inconnues.
"""
import re, sys

CHAMPS = ["fichier", "rubrique", "format", "titre", "titre_court", "chapeau", "resume", "arret",
          "publication", "image", "image_alt", "image_credit", "image_lien"]
ETIQUETTES = {"Fait établi", "Témoignage", "Interprétation", "Hypothèse", "Proposition", "Estimation", "Débat",
              "Expertise", "Allégation", "Élément matériel", "État de la procédure", "À noter", "Livre", "Figure", "Scrutins"}
FORMATS = {"Explicatif", "Analyse", "Enquête documentaire"}


def verifier(chemin):
    pb = []
    brut = open(chemin, encoding="utf-8").read()
    if "\n---\n" not in brut:
        return ["séparateur --- absent"]
    tete, corps = brut.split("\n---\n", 1)
    meta = {}
    for l in tete.strip().split("\n"):
        if ": " not in l:
            pb.append(f"ligne d'en-tête illisible : {l[:60]}")
            continue
        k, v = l.split(": ", 1)
        meta[k] = v
    for c in CHAMPS:
        if not meta.get(c):
            pb.append(f"champ manquant : {c}")
    if meta.get("format") and meta["format"] not in FORMATS:
        pb.append(f"format inconnu : {meta['format']}")
    for c in ("titre", "titre_court", "titre_seo"):
        if re.search(r"\b(vraiment|réellement)\b", meta.get(c, ""), re.I):
            pb.append(f"mot interdit dans {c}")
    if "—" in brut:
        pb.append(f"tiret cadratin : {brut.count('—')} occurrence(s)")
    if "## Sources" not in corps:
        return pb + ["section ## Sources absente"]
    texte, sources = corps.split("## Sources", 1)
    lignes = [l for l in sources.strip().split("\n") if l.startswith("- ")]
    for n, l in enumerate(lignes, 1):
        if " | " not in l or not re.search(r"\|\s*https?://\S+", l):
            pb.append(f"source {n} sans lien")
    appels = {int(x) for x in re.findall(r"\[(\d+)\]", texte)}
    hors = sorted(a for a in appels if a < 1 or a > len(lignes))
    if hors:
        pb.append(f"appels de note sans source : {hors}")
    non_citees = sorted(set(range(1, len(lignes) + 1)) - appels)
    if non_citees:
        pb.append(f"sources jamais citées : {non_citees}")
    for m in re.finditer(r"^\[([^\]\d][^\]]*)\]", texte, re.M):
        if m.group(1) not in ETIQUETTES:
            pb.append(f"étiquette inconnue : [{m.group(1)}]")
    if "## Ce qu'on ne sait pas" not in texte:
        pb.append("section « Ce qu'on ne sait pas » absente")
    return pb


if __name__ == "__main__":
    total = 0
    for chemin in sys.argv[1:]:
        pb = verifier(chemin)
        total += len(pb)
        print(f"{chemin} : {'OK' if not pb else ''}")
        for p in pb:
            print(f"  - {p}")
    sys.exit(1 if total else 0)
