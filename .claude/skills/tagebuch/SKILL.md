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
5. Bestehenden Text nicht ändern, nicht umformatieren.
6. Speichern wie in `CLAUDE.md` beschrieben (Datei einzeln adden, kurze Commit-Nachricht `journal: <Titel>`).
