---
name: angebote-vergleichen
description: Angebote positionsweise gegen das LV vergleichen und als Tabelle ablegen. Verwenden bei „Angebote vergleichen“, „Preisspiegel“, „Welches Angebot ist günstiger?“.
---

# Angebote vergleichen

Ein Los (Vergabepaket, z. B. `dach`) hat einen Ordner `docs/angebote/<los>/`.

1. **LV übertragen** nach `docs/angebote/<los>/lv.yaml` (falls noch nicht da):
   ```yaml
   los: dach
   titel: Dachneubau
   positionen:
     - nr: "01.01"
       text: Kurztext der Position
       menge: 120
       einheit: m2
   ```
2. **Jedes Angebot übertragen** nach `docs/angebote/<los>/angebot-<firma-kurz>.yaml`:
   ```yaml
   firma: Zimmerei Muster GmbH
   datum: "2026-11-10"
   anmerkung: kurz, was auffällt (optional)
   preise:
     "01.01": 18.50      # Einheitspreis netto in Euro, Positionsnummer wie im LV
   ```
   Nicht angebotene Positionen weglassen. Keine Bankdaten, keine Personennamen übernehmen. Das Angebot selbst
   (PDF) nicht ins Repo legen. Bei Pauschalen oder abweichenden Mengen in `anmerkung` notieren und nachfragen.
3. **Vergleich rechnen** (nicht selbst rechnen):
   `python werkzeuge/angebote_vergleich.py docs/angebote/<los> --ausgabe docs/angebote`
   Das schreibt `docs/angebote/vergleich-<los>.json` (für App und Web-App) und `vergleich-<los>.md`.
4. Ergebnis kurz zusammenfassen: günstigstes vollständiges Angebot, fehlende Positionen, auffällige
   Einheitspreise (mehr als 30 % über dem Mittel). Keine Vergabe-Empfehlung ohne Rückfrage.
5. YAML-Dateien und Vergleich in einem Commit speichern, Dateien einzeln adden.
