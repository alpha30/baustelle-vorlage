---
name: firma
description: Firma, Planer oder Amt in docs/firmen.yaml anlegen oder ihren Stand ändern. Verwenden bei „Neue Firma …“, „Der Zimmerer hat abgesagt“, „Wir beauftragen …“, „Wer ist …?“, „Nummer von …“.
---

# Firmen pflegen

Datei: `docs/firmen.yaml`. Erst `git pull --rebase`, dann lesen, dann ändern. Die App ändert dort Stand und Kontakt.

**Form genau einhalten** (die App liest zeilenweise):

```yaml
firmen:
  - id: zimmerei-muster
    name: Zimmerei Muster GmbH
    gewerk: zimmerer
    ansprechpartner: Herr Muster
    telefon: "02421 000000"
    mail: info@zimmerei-muster.example
    stand: angebot
    kontakt: "2026-12-03 Telefon: Angebot kommt bis Freitag"
    notiz: Empfehlung vom Nachbarn
```

- Zwei Leerzeichen vor `- id:`, vier vor jedem Feld. Ein Feld je Zeile, keine mehrzeiligen Werte.
- `telefon`, `kontakt` und jeder Wert mit Doppelpunkt immer in doppelten Anführungszeichen.
- Steht in der Datei noch `firmen: []`, daraus `firmen:` machen und den ersten Block darunter setzen.
- `id`: aus dem Namen, klein, nur `a-z0-9` und Bindestrich, eindeutig. Eine bestehende `id` nie ändern.
- `stand`: `angefragt`, `angebot`, `absage`, `beauftragt`, `fertig`. Weglassen, wenn unbekannt.
- `kontakt`: nur der letzte Kontakt, `JJJJ-MM-TT <Art>: <kurz>`. Der Verlauf steht im Tagebuch unter `## @<id> …`.
- Nur geschäftliche Kontaktdaten. Keine Bankdaten, keine Privatadressen.

**„Wer ist …?“ / „Nummer von …“:** Eintrag nennen, dazu den letzten Kontakt und offene Termine und Mängel mit `@<id>`.

Speichern wie in `CLAUDE.md` (Commit-Nachricht `firmen: <kurz>`).
