# Baustelle

Dieses Repo ist die Projektakte einer privaten Baustelle. Der Bauherr arbeitet mit Claude Code am PC und mit der
Android-App „Bauen mit Claude“ auf der Baustelle. Er programmiert nicht und spricht oft statt zu tippen. Antworte
kurz, auf Deutsch, ohne Fachjargon aus der Softwareentwicklung.

## Wo was hingehört

| Ordner / Datei | Inhalt |
|---|---|
| `journal/JJJJ-MM-TT.md` | Bautagebuch: was auf der Baustelle geschah. Eine Datei je Tag |
| `journal/bilder/JJJJ-MM/` | Fotos zum Tagebuch (kommen meist aus der App) |
| `protokoll/JJJJ-MM-TT.md` | Arbeitsprotokoll: was du am PC erarbeitet hast (siehe unten) |
| `tasks/backlog.md` | Aufgabenliste, strenges Format (siehe unten) |
| `tasks/termine.md` | Termine mit Datum: Ortstermine, Lieferungen, Fristen |
| `tasks/maengel.md` | Mängel mit Firma, Foto und Frist |
| `docs/firmen.yaml` | Betriebe, Planer, Ämter mit Telefon und Stand |
| `docs/angebote/<gewerk>/` | Angebote als PDF und ihr Vergleich |
| `docs/belege/JJJJ/` | Rechnungen und Quittungen als Datei |
| `docs/` | alles andere Wissen über das Haus: Pläne, Maße, Budget (`docs/budget/`) |
| `adr/` | Entscheidungen, eine Datei je Entscheidung (`0001-titel.md`) |
| `eingang/` | Was die App erfasst hat und noch einsortiert werden muss |

Gehört etwas nirgends hin, frag nach, statt einen neuen Ordner anzulegen.

## Tagebuch

- Datei `journal/JJJJ-MM-TT.md` mit erster Zeile `# JJJJ-MM-TT`. Fehlt sie, anlegen.
- Jeder Eintrag ist ein Abschnitt `## Titel` am **Ende** der Datei. Bestehenden Text nicht ändern.
- „Notiere …“, „Heute …“, „Ins Tagebuch …“ heißt: Eintrag für heute. Ein anderes Datum nur, wenn es genannt wird.
- Bilder: `![Beschreibung](bilder/JJJJ-MM/datei.jpg)`.
- **Nur die Baustelle gehört ins Tagebuch:** was geliefert, gebaut, besprochen, festgestellt wurde. Der Bauherr
  liest es auf dem Handy.
- Ein Gespräch mit einer Firma bekommt den Titel `## @<id> Telefon` (oder `Mail`, `Vor Ort`), mit der `id` aus
  `docs/firmen.yaml`. Danach dort das Feld `kontakt` der Firma auf diesen Kontakt setzen.
- **Verhörte Namen:** Einträge aus der App sind oft diktiert, die Spracherkennung verhört Namen („Löws“ statt
  „Töws“). Klingt ein Name ähnlich wie eine Firma oder ein Ansprechpartner aus `docs/firmen.yaml`, beim
  Übernehmen die richtige Schreibweise nehmen und das kurz sagen. In schon gespeicherten Einträgen erst nach
  Rückfrage korrigieren. Unbekannte Namen nicht raten, nachfragen.
- Den Abschnitt `## Tagesbericht` (Wetter, Anwesend, Arbeiten, Eigenleistung, Besonderes) schreibt die App. Nicht
  umformatieren; die App rechnet mit den Stunden.

## Arbeitsprotokoll (`protokoll/`)

Was **du** am PC getan hast, steht nicht im Tagebuch, sondern in `protokoll/JJJJ-MM-TT.md` (gleiches Format: erste
Zeile `# JJJJ-MM-TT`, je Schritt ein Abschnitt `## Titel` am Ende). Dazu gehören Recherchen, Auswertungen,
Vergleiche, verschickte Mails, erledigte Aufträge vom Handy. Kurz halten: was, Ergebnis, wo die Datei liegt.

## Termine (`tasks/termine.md`)

```
- [ ] 2027-01-12 08:00 Zimmerer beginnt @zimmerei-muster
- [ ] 2027-01-15 Angebotsfrist Fenster
```

- Datum `JJJJ-MM-TT` ist Pflicht, Uhrzeit `hh:mm` optional, `@<id>` nennt die Firma.
- Alles mit festem Tag gehört hierher, nicht in den Backlog. Die App erinnert am Vortag und am Tag selbst.
- Vergangene Termine löschen; was dabei herauskam, steht im Tagebuch.

## Firmen (`docs/firmen.yaml`)

- Jede Firma, mit der der Bauherr zu tun hat, bekommt einen Eintrag; die Form steht oben in der Datei und ist genau
  einzuhalten (ein Feld je Zeile, Telefon in Anführungszeichen).
- `stand` pflegen: `angefragt`, `angebot`, `absage`, `beauftragt`, `fertig`.
- Die `id` nie ändern; sie steht in Terminen, Mängeln und im Tagebuch.
- Nur geschäftliche Kontaktdaten. Keine Bankdaten, keine Privatadressen.

## Mängel (`tasks/maengel.md`)

```
- [ ] Kehlblech an der Gaube undicht @zimmerei-muster (Frist 2027-02-01)
  - Ort: dach
  - Festgestellt: 2027-01-20
  - ![](../journal/bilder/2027-01/2027-01-20-101500-dach.jpg)
```

- Format wie Aufgaben. Offene unter `## Offen`; behobene mit `[x]` und Unterpunkt `Behoben: JJJJ-MM-TT` nach
  `## Behoben` verschieben.
- Eine Mängelanzeige an die Firma nur als Entwurf vorlegen (Skill `mangel`).

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

Die App legt hier ab: `belege/` (Beleg-Entwürfe als YAML), `auftraege/` (Anweisungen an den PC),
`entscheidungen/` (eingesprochene Entscheidungen), `notizen/` (alles andere). Beim Abarbeiten
(Skill `eingang-abarbeiten`):

- **Belege:** in die Budgetdatei übernehmen, aber erst nach Rückfrage. Gewerk-Vorschlag prüfen.
- **Aufträge:** sind Anweisungen vom Handy („Schreib X wegen Y“). Ausführen, soweit die Regeln es erlauben; alles,
  was nach außen geht, vorher vorlegen. Das Ergebnis ins Tagebuch.
- **Entscheidungen:** Optionen und Folgen kurz vorlegen; ein ADR in `adr/` erst nach Zustimmung schreiben.
- **Notizen:** ins Tagebuch oder in den Backlog einsortieren.
- Eine Datei aus `eingang/` erst löschen, wenn ihr Inhalt übernommen und gespeichert ist.

## Speichern

- Nach jedem abgeschlossenen Schritt speichern: `git add` mit den geänderten Dateien einzeln, `git commit` mit einer
  kurzen Nachricht, dann `git pull --rebase` und `git push`. So sieht die App den neuen Stand.
- Immer auf `main` speichern, die App liest nur `main`. Keinen eigenen Zweig anlegen, keinen Pull Request öffnen.
  Läuft die Sitzung auf einem anderen Zweig (Claude-App, claude.ai/code): nach dem Commit
  `git pull --rebase origin main` und `git push origin HEAD:main`.
- Nie `git add -A` oder `git add .`, nie Force-Push. Bei einem Konflikt anhalten und fragen.
- Vor dem Ändern einer Datei den aktuellen Stand lesen; die App kann inzwischen etwas angehängt haben.

## Grenzen

**Immer**
- Angebote und Rechnungen dürfen als Datei ins Repo (`docs/angebote/<gewerk>/`, `docs/belege/JJJJ/`). Nicht hinein
  gehören eigene Kontodaten, Ausweise, Steuer-ID, Passwörter oder Tokens. In Budget- und Firmendaten keine IBAN und
  keine Kontodaten übernehmen, auch wenn sie auf dem Beleg stehen.
- Fotos nur ohne EXIF/GPS-Daten ablegen. In Bildern, die an Dritte gehen, keine Adressen und keine Kindernamen.
- Was die KI aus Sprache oder Belegen gemacht hat, bestätigt der Bauherr, bevor es gespeichert wird.

**Erst fragen**
- Alles, was nach außen geht: Mails, Termine, Anfragen an Firmen.
- Entscheidungen (ADR) schreiben, Budgetwerte ändern, Dateien löschen.

**Nie**
- Daten anderer Baustellen hier ablegen oder von hier dorthin kopieren.
- API-Keys oder Tokens in Dateien dieses Repos schreiben.
