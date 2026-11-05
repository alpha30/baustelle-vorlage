---
name: aufgabe
description: Aufgabe im Backlog anlegen, ändern oder abhaken. Verwenden bei „Neue Aufgabe …“, „Ich muss noch …“, „Erledigt: …“, „Was steht an?“.
---

# Aufgaben pflegen

Datei: `tasks/backlog.md`. Erst lesen, dann ändern.

**Format, streng:**

```
- [ ] Text der Aufgabe (Frist JJJJ-MM-TT)
  - Detail
```

- Neue Aufgabe als eigene Zeile ans Ende des Abschnitts `## Offen`.
- Frist nur, wenn eine genannt ist. Datum ohne Jahr: das nächste kommende Datum dieses Tages.
- Details als eingerückte Unterpunkte (zwei Leerzeichen, `- `).
- Abhaken: `[ ]` durch `[x]` ersetzen und die Zeile samt Unterpunkten unter `## Erledigt` verschieben.
- Kein Fließtext, keine Tabellen, keine Listen ohne Kästchen auf oberster Ebene.

**„Was steht an?“:** offene Aufgaben nach Frist sortiert nennen, überfällige zuerst.

Danach speichern wie in `CLAUDE.md` beschrieben (Commit-Nachricht `aufgaben: <kurz>`).
