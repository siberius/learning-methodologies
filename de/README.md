# Lernmethoden: Didaktische Methoden für KI-Entwicklung

[![Skills.sh](https://img.shields.io/badge/skills.sh-Install-blue)](https://skills.sh/siberius/learning-methodologies)

> [English documentation](../README.md) | [Čeština](../cs/README.md) | [Español](../es/README.md) | [Русский](../ru/README.md)

Ein portabler KI-Skill zur Konzeption, Implementierung und Begutachtung von Bildungsanwendungen. Er verknüpft Bildungsziele, Handlungen der Lernenden, Feedbackregeln und Lernnachweise und hilft dabei, diese didaktischen Entscheidungen in konkretes Anwendungsverhalten zu übersetzen.

## Author

**Luděk Sušický** — biologist, secondary-school and university teacher of computing subjects

- E-mail: [ludek.susicky@gmail.com](mailto:ludek.susicky@gmail.com)
- X: [@ludeksusicky](https://x.com/ludeksusicky)
- LinkedIn: [Luděk Sušický](https://www.linkedin.com/in/ludek-susicky/)
- GitHub: [@siberius](https://github.com/siberius) — more educational projects and open-source applications

---

Unter MIT-Lizenz. Die deutsche Edition teilt das internationale methodische Fundament und setzt kein einzelnes nationales Schulcurriculum, keine Laufzeit-KI, keine Benutzerkonten und kein bestimmtes KI-Modell voraus.

Aktuelle Version: **1.6.0**. Alle Sprachentwicklungen enthalten einen kompakten Arbeitsablauf, Entscheidungsbeispiele, Tutor-Modi und kontinuierliches Lernen, kognitive Benutzeroberflächen, evidenzbasierte Leitplanken für Lernspiele sowie explizite Regeln für Modellauswahl und Eskalationsstufen.

## Was dieser Skill leistet

- Didaktische Methoden passend zu realen Lernhindernissen und dem Unterrichtskontext auswählen.
- Selbstregulation der Lernenden im geteilten kognitiven Raum mit KI unterstützen (FALR-Rahmenwerk: Choice, kognitive Pause, Evaluation und Selbststeuerung), damit Antworten nicht gedankenlos kopiert werden.
- Gestufte Hilfestellungen (Scaffolding), konstruktives Feedback und selbstständige Übungsphasen konzipieren.
- Lernziele, Aufgabenschwierigkeit, curriculare Voraussetzungen und Kompetenznachweise sauber trennen.
- Verlässliche wissenschaftliche Simulationen und klar begrenzte KI-Tutoren realisieren.
- Barrierefreiheit (WCAG 2.2 / UDL), Kontrollmöglichkeiten für Lehrkräfte, Datenschutz und Betriebsaufwand mitdenken.
- Zwischen funktionsfähiger Software, didaktischer Eignung und tatsächlich beobachtetem Lernerfolg unterscheiden.
- Passende Sprachmodelle, Denkaufwand (Reasoning Effort) und Ausführungsgeschwindigkeiten anhand dokumentierter Profile für OpenAI, Claude und Gemini wählen.

Unterstützte Methoden umfassen u. a. Sokratischen Dialog, Feynman-Methode, Zone der nächsten Entwicklung (ZPD) und Scaffolding, ausgearbeitete Lösungsbeispiele (Worked Examples), aktiven Abruf (Retrieval Practice), zeitlich versetztes Wiederholen (Spaced Practice), forschendes Lernen, Rollenspiele, Peer- und kooperatives Lernen, Projektarbeit und Flipped Classroom.

## Installation und Schnellstart

Installiere die deutsche Edition mit der [Skills CLI](https://github.com/vercel-labs/skills). `-g` installiert global für den Benutzer; `-a codex` wählt Codex. Ersetze es durch `-a claude-code` für Claude Code oder wähle interaktiv:

```bash
npx skills add siberius/learning-methodologies@v1.6.0 --skill lernmethoden --full-depth -g -a codex
```

Der Tag installiert den Inhalt dieser Veröffentlichung; der Standardbranch kann neuer sein. Die CLI trägt den aufgelösten Commit und einen Hash der installierten Dateien in `skills-lock.json` ein, und `npx skills check` meldet lokale Änderungen.

Zum Ausprobieren in einem Projekt lass `-g` weg und entferne die Kopie danach mit `npx skills remove lernmethoden`. Clients, die Markdown direkt lesen, können die [eigenständige Datei](lernmethoden.md) ohne Installer verwenden; die [Nutzungsanleitung](docs/USAGE.md) beschreibt die manuelle Paketablage.

## Formate wählen

- [SKILL.md](SKILL.md) und [references/](references/): Natives Paket mit bedarfsgerecht geladenen Referenzdateien.
- [lernmethoden.md](lernmethoden.md): Generierte, eigenständige Markdown-Datei (Standalone) für Chat-Modelle und Agenten, die eine einzelne Anweisungsdatei erfordern.

Beide Formate stammen aus denselben gepflegten Quellen. Bei inhaltlichen Anpassungen werden `SKILL.md` und die Dateien in `references/` bearbeitet und anschließend `lernmethoden.md` über das Build-Skript aktualisiert.

## Beispiel-Prompt

> Nutze lernmethoden, um eine 15-minütige Offline-Aktivität zum Stromkreis für 16-jährige Lernende zu entwickeln. Die Lernenden sollen vorhersagen, wie sich der Widerstand auf die Stromstärke auswirkt, und ihre Überlegung begründen. Die Aktivität dient einer lehrkraftgeleiteten Diskussion und muss vollständig per Tastatur bedienbar sein. Keine Benutzerkonten oder externen KI-Aufrufe.

## Dokumentation

- [Nutzung und Installation](docs/USAGE.md)
- [Leitfaden für Lehrkräfte](docs/TEACHERS.md)
- [Gemeinsame Modell-Evaluation](docs/MODEL-EVALUATION.md)
- [Lizenz](LICENSE)

## Sprachausgaben

| Sprache | Natives Paket und Dokumentation | Eigenständige Datei |
|---|---|---|
| Deutsch | [Deutsch](README.md) | [lernmethoden.md](lernmethoden.md) |
| English | [English](../README.md) | [learning-methodologies.md](../learning-methodologies.md) |
| Čeština | [Čeština](../cs/README.md) | [vzdelavaci-metodiky.md](../cs/vzdelavaci-metodiky.md) |
| Español | [Español](../es/README.md) | [metodologias-de-aprendizaje.md](../es/metodologias-de-aprendizaje.md) |
| Русский | [Русский](../ru/README.md) | [metodiki-obucheniya.md](../ru/metodiki-obucheniya.md) |
