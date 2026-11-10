---
name: tagebuch
description: Eintrag ins Bautagebuch schreiben. Verwenden bei „Notiere …“, „Ins Tagebuch …“, „Heute war …“ oder wenn der Bauherr erzählt, was auf der Baustelle passiert ist.
---

# Tagebuch-Eintrag

1. Datum bestimmen: heute, außer ein anderes Datum wird genannt.
2. `journal/JJJJ-MM-TT.md` lesen. Fehlt die Datei, mit `# JJJJ-MM-TT` und einer Leerzeile anlegen.
3. Einen Abschnitt **ans Ende** anhängen:
   ```
   ## Kurzer Titel

   Text in ganzen Sätzen, so wie der Bauherr es gesagt hat, nur sprachlich geglättet.
   ```
   Endet die Datei ohne Zeilenumbruch, zuerst einen ergänzen; vor dem neuen Abschnitt genau eine Leerzeile.
4. Steckt eine Aufgabe im Text („muss noch …“, „bis Freitag …“), fragen, ob sie in den Backlog soll, und dann
   den Skill `aufgabe` nutzen.
5. Bestehenden Text nicht ändern, nicht umformatieren. Der Abschnitt `## Tagesbericht` kommt aus der App.
6. War es ein Gespräch mit einer Firma, heißt der Titel `## @<id> Telefon` (oder `Mail`, `Vor Ort`), und das Feld
   `kontakt` der Firma in `docs/firmen.yaml` wird auf diesen Kontakt gesetzt (Skill `firma`).
7. Ein genannter Termin („kommt Dienstag um acht“) gehört zusätzlich nach `tasks/termine.md` (Skill `termin`).
8. Ins Tagebuch gehört nur, was auf der Baustelle geschah. Was du selbst am PC erarbeitet hast, steht in
   `protokoll/JJJJ-MM-TT.md`.
9. Speichern wie in `CLAUDE.md` beschrieben (Datei einzeln adden, kurze Commit-Nachricht `journal: <Titel>`).
