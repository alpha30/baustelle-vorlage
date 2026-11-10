---
name: mangel
description: Mangel festhalten, als behoben markieren oder eine Mängelanzeige an die Firma entwerfen. Verwenden bei „Mangel: …“, „Das ist schief/undicht/falsch“, „Mangel behoben“, „Schreib dem … wegen des Mangels“.
---

# Mängel pflegen

Datei: `tasks/maengel.md`. Erst `git pull --rebase`, dann lesen, dann ändern. Die App legt dort Mängel mit Foto an.

```
- [ ] Kehlblech an der Gaube undicht @zimmerei-muster (Frist 2027-02-01)
  - Ort: dach
  - Festgestellt: 2027-01-20
  - ![](../journal/bilder/2027-01/2027-01-20-101500-dach.jpg)
```

- Neuer Mangel ans Ende von `## Offen`. `@<id>` ist die Firma aus `docs/firmen.yaml`. Frist nur, wenn genannt.
- Unterpunkte: `Ort:`, `Festgestellt:`, Fotos; weitere Unterpunkte sind freier Text. Bestehende Fotozeilen nie ändern.
- Behoben: `[x]` setzen, Unterpunkt `Behoben: JJJJ-MM-TT` ergänzen, den Block nach `## Behoben` verschieben.
- Sonst nur Überschriften und Leerzeilen in der Datei.

**Mängelanzeige:** Nur als Entwurf vorlegen, nie selbst verschicken. Inhalt: Was, wo, seit wann, Foto nennen,
Aufforderung zur Beseitigung bis zu einem Datum (üblich 10 bis 14 Tage), Bitte um Rückmeldung. Sachlich, ohne
Rechtsbelehrung. Nach dem Versand durch den Bauherrn: Frist in der Mangelzeile nachtragen und im Tagebuch einen
Abschnitt `## @<id> Mail` anlegen.

Speichern wie in `CLAUDE.md` (Commit-Nachricht `maengel: <kurz>`).
