---
name: eingang-abarbeiten
description: Was die App in eingang/ abgelegt hat, einsortieren. Verwenden bei „Eingang abarbeiten“, „Was kam aus der App?“ oder wenn eingang/ Dateien enthält.
---

# Eingang abarbeiten

1. `git pull --rebase`, dann `eingang/` auflisten. Ist er leer, das kurz sagen und aufhören.
2. Je Datei, älteste zuerst:
   - **`notizen/*.md`:** Inhalt als Tagebuch-Eintrag für das Erfassungsdatum (Skill `tagebuch`) oder als
     Aufgabe (Skill `aufgabe`) übernehmen. Bei Unklarheit fragen.
   - **`entscheidungen/*.md`:** Entscheidung in zwei, drei Sätzen zusammenfassen, Optionen und Folgen nennen und
     fragen, ob daraus ein ADR werden soll. Erst nach „ja“ `adr/NNNN-titel.md` schreiben (nächste freie Nummer).
   - **`belege/*.yaml`:** mit dem Skill `belege-uebernehmen` in die Budgetdatei übernehmen.
3. Erst wenn der Inhalt übernommen ist, die Eingangsdatei löschen. Übernahme und Löschung in **einem** Commit
   speichern, Dateien einzeln adden.
4. Am Ende kurz zusammenfassen, was wohin gegangen ist.
