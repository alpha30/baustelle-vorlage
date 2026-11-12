---
name: belege-uebernehmen
description: Beleg-Entwürfe aus eingang/belege/ in die Budgetdatei übernehmen und die Budget-Übersicht neu erzeugen. Verwenden bei „Belege übernehmen“, „Budget aktualisieren“ oder wenn eingang/belege/ Dateien enthält.
---

# Belege übernehmen

1. `git pull --rebase`, dann `eingang/belege/*.yaml` auflisten. Leer: kurz sagen und aufhören.
2. Je Entwurf (älteste zuerst) dem Bauherrn zeigen: Firma, Datum, Art, Netto, Brutto, Gewerk-Vorschlag.
   Steht `betrag_quelle: ki`, darauf hinweisen, dass die KI gelesen hat. Bei `ki-summe` hat die KI den Betrag
   aus Positionspreisen zusammengezählt: ausdrücklich prüfen lassen, das Original liegt meist unter
   `docs/angebote/` oder `docs/belege/`. Eine `notiz` im Entwurf vorlesen.
3. **Erst nach Zustimmung** eine Position in `docs/budget/positionen.yaml` unter `positionen:` anlegen:
   - `id`: kurz und eindeutig, z. B. `zimmerei-rechnung-2`
   - `firma`, `datum`, `art`, `betrag_brutto` aus dem Entwurf
   - `gewerk`: ein Gewerk, das in einem Topf unter `budgets:` vorkommt; passt keins, nachfragen
   - `status`: bei Rechnungen `bezahlt` nur, wenn der Bauherr das sagt, sonst `beauftragt`; Angebote `geplant`
   - `bezug`: bei einer Rechnung auf einen Auftrag dessen `id` (nachfragen)
   - `beleg`: der Wert von `datei` aus dem Entwurf (das Original liegt unter `docs/belege/JJJJ/`)
   Keine IBAN, keine Kontodaten übernehmen, auch wenn sie versehentlich im Entwurf stehen.
4. Den Entwurf aus `eingang/belege/` löschen.
5. Übersicht neu erzeugen: `python werkzeuge/budget_export.py .` (schreibt `docs/budget/uebersicht.json`).
6. Positionen, gelöschte Entwürfe und Übersicht in **einem** Commit speichern, Dateien einzeln adden,
   Nachricht `budget: <n> Belege übernommen`.
7. Zum Schluss Budget, Ist und Prognose aus der Ausgabe von Schritt 5 nennen.
