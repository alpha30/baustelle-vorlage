"""Budget-Export: docs/budget/positionen.yaml -> docs/budget/uebersicht.json.

App und Web-App rechnen nicht selbst, sie zeigen nur diese Datei an (Architekturentscheidung 2 in
tasks/plan.md). Damit stimmen alle Zahlen überein.

Rechenregeln wie bauplanung/src/budget/report.py:
- Ist      = Summe der Positionen mit art rechnung/gebuehr.
- Obligo   = offene Aufträge (status beauftragt/teilbezahlt) minus der darauf schon abgerechneten
             Rechnungen (Verknüpfung über `bezug`); nie negativ.
- Prognose = max(Budget, Ist + Obligo) je Topf; ohne Budget Ist + Obligo.
- Abweichung = Prognose - Budget; null ohne Budget.
Zusätzlich: Angebote und Aufträge als Summen der Positionen mit art angebot bzw. auftrag.
Positionen ohne Budgettopf landen im Topf "ohne-topf", damit die Summen der Töpfe die Gesamtsummen ergeben.

Für bauplanung (mit OpenProject-Overlay und Gewerke-Prüfung gegen plan.ts) wird report.py selbst geladen:
    python export.py <baustelle> --report <baustelle>/src/budget/report.py
Ohne --report gelten die eingebauten Regeln (Vorlage).
"""
import argparse
import importlib.util
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import yaml

IST_ARTEN = {"rechnung", "gebuehr"}
OHNE_TOPF = "ohne-topf"


def report_laden(baustelle: Path):
    """report.py aus einer Baustelle laden (nur Funktionen, main() wird nicht ausgeführt)."""
    pfad = Path(baustelle) / "src/budget/report.py"
    sys.path.insert(0, str(Path(baustelle) / "src"))
    spec = importlib.util.spec_from_file_location("baustelle_report", pfad)
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


def _normalisieren(budgets):
    out = []
    for b in budgets:
        keys = b.get("gewerke")
        if keys is None:
            einzel = b.get("gewerk") or b.get("kategorie")
            keys = [einzel] if einzel else []
        bid = b.get("id") or (keys[0] if keys else "<ohne id>")
        out.append({"id": bid, "name": b.get("name") or bid, "keys": list(keys), "betrag": b.get("betrag"),
                    "quelle": b.get("quelle"), "stand": b.get("stand"), "unsicherheit": b.get("unsicherheit")})
    return out


def _auswerten(positionen):
    koepfe = defaultdict(lambda: {"ist": 0.0, "obligo": 0.0, "n_ohne_betrag": 0, "n": 0})
    abgerechnet = defaultdict(float)
    for p in positionen:
        if p.get("art") in IST_ARTEN and p.get("bezug") and p.get("betrag_brutto"):
            abgerechnet[p["bezug"]] += float(p["betrag_brutto"])
    for p in positionen:
        t = koepfe[p.get("gewerk") or p.get("kategorie")]
        t["n"] += 1
        if p.get("betrag_brutto") is None:
            t["n_ohne_betrag"] += 1
            continue
        betrag = float(p["betrag_brutto"])
        if p["art"] in IST_ARTEN:
            t["ist"] += betrag
        elif p["art"] == "auftrag" and p.get("status") in ("beauftragt", "teilbezahlt"):
            t["obligo"] += max(betrag - abgerechnet.get(p["id"], 0.0), 0.0)
    return koepfe


def _prognose(budget, ist, obligo):
    basis = ist + obligo
    return max(budget, basis) if budget is not None else basis


def _summe_art(positionen, keys, art):
    return sum(float(p["betrag_brutto"]) for p in positionen
               if p.get("art") == art and p.get("betrag_brutto") is not None
               and (p.get("gewerk") or p.get("kategorie")) in keys)


def _runden(x):
    return None if x is None else round(float(x), 2)


def exportieren(daten: dict, quelle: str, report=None, jetzt: datetime | None = None) -> dict:
    positionen = daten.get("positionen") or []
    budgets = daten.get("budgets") or []
    if report is not None:
        gewerk_ids = {g for _, _, gs in report.read_plan() for g, _ in gs}
        toepfe = report.normalisieren(budgets)
        fehler = report.validate(positionen, toepfe, gewerk_ids)
        if fehler:
            raise ValueError("Budgetdatei ungültig:\n  - " + "\n  - ".join(fehler))
        koepfe, prognose = report.auswerten(positionen), report.prognose
    else:
        toepfe, koepfe, prognose = _normalisieren(budgets), _auswerten(positionen), _prognose

    belegt = {k for t in toepfe for k in t["keys"]}
    rest = sorted(k for k in koepfe if k not in belegt and k is not None)
    if rest:
        toepfe = list(toepfe) + [{"id": OHNE_TOPF, "name": "Ohne Budgettopf", "keys": rest, "betrag": None,
                                  "quelle": None, "stand": None, "unsicherheit": None}]

    aus = []
    for t in toepfe:
        ist = sum(koepfe[k]["ist"] for k in t["keys"] if k in koepfe)
        obligo = sum(koepfe[k]["obligo"] for k in t["keys"] if k in koepfe)
        prog = prognose(t["betrag"], ist, obligo)
        aus.append({
            "id": t["id"], "name": t["name"], "gewerke": list(t["keys"]),
            "budget": _runden(t["betrag"]),
            "angebote": _runden(_summe_art(positionen, t["keys"], "angebot")),
            "auftraege": _runden(_summe_art(positionen, t["keys"], "auftrag")),
            "ist": _runden(ist), "obligo": _runden(obligo), "prognose": _runden(prog),
            "abweichung": _runden(prog - t["betrag"]) if t["betrag"] is not None else None,
            "quelle": t.get("quelle"), "stand": None if t.get("stand") is None else str(t.get("stand")),
            "unsicherheit": t.get("unsicherheit"),
        })

    summen = {f: _runden(sum(t[f] for t in aus)) for f in ("angebote", "auftraege", "ist", "obligo", "prognose")}
    summen["budget"] = _runden(sum(t["budget"] for t in aus if t["budget"] is not None))
    return {
        "version": 1,
        "erzeugt": (jetzt or datetime.now(timezone.utc)).astimezone().isoformat(timespec="seconds"),
        "quelle": quelle,
        "summen": summen,
        "toepfe": aus,
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("baustelle", type=Path, help="Wurzel des Baustellen-Repos")
    ap.add_argument("--report", type=Path, help="report.py der Baustelle verwenden (bauplanung)")
    args = ap.parse_args(argv)
    quelle = "docs/budget/positionen.yaml"
    daten = yaml.safe_load((args.baustelle / quelle).read_text(encoding="utf-8")) or {}
    report = report_laden(args.report.parents[2]) if args.report else None
    ergebnis = exportieren(daten, quelle, report)
    ziel = args.baustelle / "docs/budget/uebersicht.json"
    ziel.write_text(json.dumps(ergebnis, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    s = ergebnis["summen"]
    print(f"{ziel} geschrieben: Budget {s['budget']:.2f} €, Ist {s['ist']:.2f} €, Prognose {s['prognose']:.2f} €")
    return 0


if __name__ == "__main__":
    sys.exit(main())
