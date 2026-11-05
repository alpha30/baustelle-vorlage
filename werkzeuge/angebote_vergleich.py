"""Angebotsvergleich: LV und Angebote (YAML) -> docs/angebote/vergleich-<los>.json und .md.

Claude Code überträgt das LV und jedes Angebot in einfache YAML-Dateien in einem Ordner je Los:
    lv.yaml            los, titel, positionen: [{nr, text, menge, einheit}]
    angebot-*.yaml     firma, datum, anmerkung (optional), preise: {nr: Einheitspreis netto}
Dieses Skript rechnet daraus den Vergleich (schema/angebotsvergleich.schema.json). Gerechnet wird nur hier.

    python vergleich.py docs/angebote/dach --ausgabe docs/angebote
"""
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml


def _lesen(pfad: Path) -> dict:
    return yaml.safe_load(pfad.read_text(encoding="utf-8")) or {}


def vergleichen(ordner: Path, jetzt: datetime | None = None) -> dict:
    lv = _lesen(ordner / "lv.yaml")
    positionen = lv.get("positionen") or []
    angebote = [_lesen(p) for p in sorted(ordner.glob("angebot-*.yaml"))]

    firmen = []
    for a in angebote:
        preise = {str(k): v for k, v in (a.get("preise") or {}).items()}
        fehlend = [str(p["nr"]) for p in positionen if preise.get(str(p["nr"])) is None]
        summe = sum(float(p["menge"]) * float(preise[str(p["nr"])]) for p in positionen
                    if preise.get(str(p["nr"])) is not None)
        firmen.append({
            "firma": a["firma"],
            "summe_netto": round(summe, 2),
            "fehlende_positionen": fehlend,
            "vollstaendig": not fehlend,
            "datum": None if a.get("datum") is None else str(a["datum"]),
            "anmerkung": a.get("anmerkung"),
        })
    firmen.sort(key=lambda f: (not f["vollstaendig"], f["summe_netto"]))

    aus_pos = []
    for p in positionen:
        nr = str(p["nr"])
        preise = {}
        for a in angebote:
            wert = (a.get("preise") or {}).get(nr, (a.get("preise") or {}).get(p["nr"]))
            preise[a["firma"]] = None if wert is None else float(wert)
        angeboten = {f: v for f, v in preise.items() if v is not None}
        aus_pos.append({
            "nr": nr, "text": p["text"], "menge": float(p["menge"]), "einheit": p["einheit"],
            "preise": preise,
            "guenstigste": min(angeboten, key=angeboten.get) if angeboten else None,
        })

    return {
        "version": 1,
        "los": lv.get("los") or ordner.name,
        "titel": lv.get("titel") or ordner.name,
        "erzeugt": (jetzt or datetime.now(timezone.utc)).astimezone().isoformat(timespec="seconds"),
        "firmen": firmen,
        "positionen": aus_pos,
    }


def als_markdown(v: dict) -> str:
    def eur(x):
        return f"{x:,.2f} €".replace(",", " ").replace(".", ",", 1).replace(" ", ".")

    zeilen = [f"# Angebotsvergleich {v['titel']}", "",
              f"Erzeugt von `generatoren/angebote/vergleich.py` am {v['erzeugt'][:10]}. Nicht von Hand bearbeiten.", "",
              "| Firma | Summe netto | Vollständig |", "|---|---:|---|"]
    for f in v["firmen"]:
        voll = "ja" if f["vollstaendig"] else "fehlt: " + ", ".join(f["fehlende_positionen"])
        zeilen.append(f"| {f['firma']} | {eur(f['summe_netto'])} | {voll} |")
    namen = [f["firma"] for f in v["firmen"]]
    zeilen += ["", "## Einheitspreise", "", "| Pos. | Text | Menge | " + " | ".join(namen) + " |",
               "|---|---|---:|" + "---:|" * len(namen)]
    for p in v["positionen"]:
        preise = [("**" if n == p["guenstigste"] else "") + (eur(p["preise"][n]) if p["preise"][n] is not None else "—")
                  + ("**" if n == p["guenstigste"] else "") for n in namen]
        zeilen.append(f"| {p['nr']} | {p['text']} | {p['menge']:g} {p['einheit']} | " + " | ".join(preise) + " |")
    return "\n".join(zeilen) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("ordner", type=Path, help="Ordner mit lv.yaml und angebot-*.yaml")
    ap.add_argument("--ausgabe", type=Path, help="Zielordner (Standard: übergeordneter Ordner)")
    args = ap.parse_args(argv)
    v = vergleichen(args.ordner)
    ziel = args.ausgabe or args.ordner.parent
    (ziel / f"vergleich-{v['los']}.json").write_text(
        json.dumps(v, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    (ziel / f"vergleich-{v['los']}.md").write_text(als_markdown(v), encoding="utf-8", newline="\n")
    for f in v["firmen"]:
        print(f"{f['firma']}: {f['summe_netto']:.2f} € netto" + ("" if f["vollstaendig"] else " (unvollständig)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
