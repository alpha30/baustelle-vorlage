---
name: termin
description: Termin mit festem Datum anlegen, verschieben oder absagen. Verwenden bei „Termin am …“, „Der Elektriker kommt Dienstag“, „Lieferung am …“, „Angebotsfrist …“, „Welche Termine habe ich?“.
---

# Termine pflegen

Datei: `tasks/termine.md`. Erst `git pull --rebase`, dann lesen, dann ändern.

```
- [ ] 2027-01-12 08:00 Zimmerer beginnt mit dem Abbund @zimmerei-muster
  - Schlüssel für das Tor mitbringen
- [ ] 2027-01-15 Angebotsfrist Fenster
```

- Datum `JJJJ-MM-TT` Pflicht, Uhrzeit `hh:mm` nur, wenn genannt. Datum ohne Jahr: das nächste kommende.
- `@<id>` nennt die Firma aus `docs/firmen.yaml`. Fehlt sie dort, zuerst anlegen (Skill `firma`).
- Neue Zeile ans Ende. Details als eingerückte Unterpunkte. Sonst nur Überschriften und Leerzeilen in der Datei.
- Verschieben: Datum in der Zeile ändern. Absagen oder erledigt: Zeile löschen; ein Ergebnis gehört ins Tagebuch.
- Etwas ohne festen Tag ist eine Aufgabe (Skill `aufgabe`).
- Einen Termin mit einer Firma nur eintragen, nicht selbst vereinbaren: Mails und Anrufe erst nach Zustimmung.

**„Welche Termine habe ich?“:** offene Termine nach Datum, dazu Fristen aus `tasks/backlog.md` und `tasks/maengel.md`.

Speichern wie in `CLAUDE.md` (Commit-Nachricht `termine: <kurz>`).
