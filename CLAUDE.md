# Baustelle

Dieses Repo ist die Projektakte einer privaten Baustelle. Der Bauherr arbeitet mit Claude Code am PC und mit der
Android-App „Bauen mit Claude“ auf der Baustelle. Er programmiert nicht und spricht oft statt zu tippen. Antworte
kurz, auf Deutsch, ohne Fachjargon aus der Softwareentwicklung.

## Wo was hingehört

| Ordner / Datei | Inhalt |
|---|---|
| `journal/JJJJ-MM-TT.md` | Bautagebuch, eine Datei je Tag |
| `journal/bilder/` | Fotos zum Tagebuch (kommen meist aus der App) |
| `tasks/backlog.md` | Aufgabenliste, strenges Format (siehe unten) |
| `docs/` | Wissen über das Haus: Pläne, Maße, Firmen, Budget (`docs/budget/`), Angebote (`docs/angebote/`) |
| `adr/` | Entscheidungen, eine Datei je Entscheidung (`0001-titel.md`) |
| `eingang/` | Was die App erfasst hat und noch einsortiert werden muss |

Gehört etwas nirgends hin, frag nach, statt einen neuen Ordner anzulegen.

## Tagebuch

- Datei `journal/JJJJ-MM-TT.md` mit erster Zeile `# JJJJ-MM-TT`. Fehlt sie, anlegen.
- Jeder Eintrag ist ein Abschnitt `## Titel` am **Ende** der Datei. Bestehenden Text nicht ändern.
- „Notiere …“, „Heute …“, „Ins Tagebuch …“ heißt: Eintrag für heute. Ein anderes Datum nur, wenn es genannt wird.
- Bilder: `![Beschreibung](bilder/datei.jpg)`.

## Aufgaben (`tasks/backlog.md`)

Eine Zeile je Aufgabe, ganz links, sonst nichts auf oberster Ebene:

```
- [ ] Text der Aufgabe (Frist JJJJ-MM-TT)
  - Detail als eingerückter Unterpunkt
- [x] Erledigte Aufgabe
```

- Frist nur, wenn eine genannt ist. „bis 20.11.“ ist das nächste kommende 20.11.
- Neue Aufgaben unter `## Offen`, erledigte nach `## Erledigt` verschieben und `[x]` setzen.
- Kein Fließtext, keine Tabellen, keine Listen ohne Kästchen in dieser Datei. Erklärungen gehören ins Tagebuch
  oder nach `docs/`. Die App kann Aufgaben nur in diesem Format anzeigen und abhaken.

## Eingang (`eingang/`)

Die App legt hier ab: `belege/` (Beleg-Entwürfe als YAML), `entscheidungen/` (eingesprochene Entscheidungen),
`notizen/` (alles andere). Beim Abarbeiten (Skill `eingang-abarbeiten`):

- **Belege:** in die Budgetdatei übernehmen, aber erst nach Rückfrage. Gewerk-Vorschlag prüfen.
- **Entscheidungen:** Optionen und Folgen kurz vorlegen; ein ADR in `adr/` erst nach Zustimmung schreiben.
- **Notizen:** ins Tagebuch oder in den Backlog einsortieren.
- Eine Datei aus `eingang/` erst löschen, wenn ihr Inhalt übernommen und gespeichert ist.

## Speichern

- Nach jedem abgeschlossenen Schritt speichern: `git add` mit den geänderten Dateien einzeln, `git commit` mit einer
  kurzen Nachricht, dann `git pull --rebase` und `git push`. So sieht die App den neuen Stand.
- Nie `git add -A` oder `git add .`, nie Force-Push. Bei einem Konflikt anhalten und fragen.
- Vor dem Ändern einer Datei den aktuellen Stand lesen; die App kann inzwischen etwas angehängt haben.

## Grenzen

**Immer**
- Originalbelege (Rechnungen, Angebote als PDF/Foto) nie ins Repo. Keine IBAN, keine Kontodaten, keine
  Ausweisnummern, keine Passwörter oder Tokens.
- Fotos nur ohne EXIF/GPS-Daten ablegen. In Bildern, die an Dritte gehen, keine Adressen und keine Kindernamen.
- Was die KI aus Sprache oder Belegen gemacht hat, bestätigt der Bauherr, bevor es gespeichert wird.

**Erst fragen**
- Alles, was nach außen geht: Mails, Termine, Anfragen an Firmen.
- Entscheidungen (ADR) schreiben, Budgetwerte ändern, Dateien löschen.

**Nie**
- Daten anderer Baustellen hier ablegen oder von hier dorthin kopieren.
- API-Keys oder Tokens in Dateien dieses Repos schreiben.
