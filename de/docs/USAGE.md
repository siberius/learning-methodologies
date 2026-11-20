# Nutzung und Installation

## Den richtigen Einstiegspunkt wählen

Nutze diesen Skill bei der Neuentwicklung einer Bildungsanwendung, bei einer wesentlichen didaktischen Überarbeitung oder bei der Begutachtung eines bestehenden didaktischen Entwurfs. Reine kosmetische Anpassungen oder gewöhnliche Fehlerkorrekturen erfordern keine didaktische Neukonzeption.

Gib bekannte Informationen zu Zielgruppe, Lernziel, unterrichtlichem Kontext und praktischen Rahmenbedingungen direkt im Prompt an. Der Agent baut auf vorhandenen Angaben auf und fragt gezielt nach wesentlichen Lücken und noch offenen didaktischen Weichenstellungen. Er wiederholt keinen starren Zielgruppen-Fragebogen und fordert keine wiederholte Bestätigung für Standardentscheidungen ein, die durch den Auftrag bereits abgedeckt sind.

## Begleitete Entscheidungen während des Entwurfs

Der Skill schlägt bei einer offenen, folgenreichen Entscheidung wenige relevante didaktische Optionen vor: eine prägnante Erklärung, ein konkretes Beispiel und eine begründete Empfehlung. Er merkt sich deine Entscheidungen und verknüpft sie mit der Implementierung und Verifikation. Formulierungen wie „Triff Routineentscheidungen für mich“ delegieren Standardfragen; Alternativen können jederzeit erneut verglichen werden. Kleine Offline-Übungen bleiben kompakt. Methodenkarten, Leitfäden für kognitive Schnittstellen und adaptives Üben unterstützen diesen Ablauf.

## Installation über die skills.sh CLI

Installiere die deutsche Edition mit der [Skills CLI](https://github.com/vercel-labs/skills). `-g` wählt die globale Installation für den Benutzer; `-a codex` wählt Codex. Ersetze es durch `-a claude-code` für Claude Code oder lasse die Agenten-Option weg, um interaktiv auszuwählen:

```bash
npx skills add siberius/learning-methodologies@v1.6.0 --skill lernmethoden --full-depth -g -a codex
```

Der Versions-Tag hält die Installation auf einer veröffentlichten Fassung; der Standardbranch kann neuer sein. Die CLI trägt den aufgelösten Commit und einen Hash der installierten Dateien in `skills-lock.json` ein, sodass `npx skills list` und `npx skills check` Abweichungen auf der Festplatte melden.

Für ein einzelnes Projekt lass `-g` weg und entferne die Kopie danach mit `npx skills remove lernmethoden`. Die CLI bietet außerdem einen temporären Ausführungsmodus, der ein Skill beim Start eines Agenten herunterlädt. Dieses Repository dokumentiert ihn nicht: prüfbar ist die gepinnte Kopie auf der Festplatte.

## Natives Skill-Paket

Platziere `SKILL.md`, `LICENSE` und das Verzeichnis `references/` im selben Skill-Ordner, üblicherweise benannt als `lernmethoden` (oder `learning-methodologies`). Nutze den vom jeweiligen Client unterstützten Installationsmechanismus. Das bloße Vorhandensein einer Markdown-Datei irgendwo auf der Festplatte garantiert noch keine automatische Erkennung.

Für Clients, die `~/.agents/skills` verwenden, lautet ein typischer Zielpfad:

```text
~/.agents/skills/lernmethoden/
  SKILL.md
  references/
  LICENSE
```

Für Claude Code lautet das äquivalente Verzeichnis typischerweise `~/.claude/skills/lernmethoden/`. Bewahre bestehende Benutzerdateien und prüfe Versionskonflikte vor dem Überschreiben. Bestätige die Erkennung im realen Client. Eine erfolgreiche Installation belegt noch nicht automatisch, dass der Agent den Skill im konkreten Fall auch angewendet hat.

## Eigenständiges Markdown (Standalone)

Übergib einem sprachmodellbasierten Agenten die generierte Datei `lernmethoden.md` und weise ihn explizit an, diese Datei als Handlungsanweisung zu nutzen. Sie enthält alle Referenzen als eingebettete Abschnitte und benötigt keine relativen Dateizugriffe. Dieser Weg lädt mehr Text auf einmal in den Kontext, erfordert dafür jedoch nur eine einzige Datei.

Modellnamen sind keine Installationsmechanismen. Die Kompatibilität hängt davon ab, ob die Host-Anwendung Markdown-Instruktionen einlesen und befolgen kann, sowie von ihren Werkzeugen und Berechtigungen.

## Bedarfsorientiert arbeiten

| Bedarf | Relevanter Leitfaden |
|---|---|
| Tutor-Modi, fortsetzbares Lernen und Checkpoints | `references/tutor-state.md` |
| Warum eine Methode passt und wie sie das Anwendungsverhalten steuert | `references/didactic-rationale.md` |
| Gesamtkonzeption, didaktisches Audit oder Projektumfang | Kern in `SKILL.md` |
| Mehrdeutige Hilfen, alternative Antworten oder Lehrplanansprüche | `references/decision-examples.md` |
| Methodenauswahl, Scaffolding und Progression | `references/methods.md` |
| Benotung, Bewertungsraster (Rubrics), Adaptivität oder Lernnachweise | `references/assessment.md` |
| Fachmodelle, Experimente oder Rollenspiele | `references/simulations.md` |
| Externe KI-Dienste im fertigen Produkt | `references/runtime-ai.md` |
| Modellwahl, Denkaufwand (Reasoning), Geschwindigkeit oder Client-Anpassung | `references/model-profiles.md` |
| Erstellerentscheidungen und Entscheidungskontinuität | `references/design-dialogue.md` |
| Repräsentationen, Multimedia und Aufmerksamkeit | `references/cognitive-ux.md` |
| Wiederholungsplanung (Spaced Repetition) und adaptive Aufgabenschwierigkeit | `references/adaptive-practice.md` |
| Spielmechaniken, Motivation und didaktischer Transfer | `references/learning-games.md` |

Lade im nativen Modus nicht alle Referenzen automatisch. Ein Offline-Quiz kann Feedback und Hilfen ohne Laufzeit-KI bereitstellen. Eine Unterrichtsdemonstration der Lehrkraft benötigt oft nur Diskussionsimpulse statt individueller Schülerkonten. Binde Fachperspektiven nach Aufgabenbedarf ein, ohne automatisch mehrere Agenten parallel zu starten.

## Pflege der Editionen

Die primären Quelldateien sind `SKILL.md` und die zugehörigen Referenzen in `references/`. Die eigenständige Markdown-Datei ist ein generiertes Distributionsartefakt. Im Repository-Maintainer-Modus wird sie wie folgt neu gebaut:

```sh
python3 testing/build_portable.py --edition de
python3 testing/build_portable.py --edition de --check
python3 testing/build_portable.py --edition all --check
```

Der Generator befindet sich in den internen Entwicklerwerkzeugen (`testing/`). Anwender können beide Formate direkt nutzen, ohne den Builder selbst auszuführen. Er bettet Referenzen mit eindeutigen Ankern ein, sodass Überschriften kollisionsfrei bleiben.

Halte README und didaktische Beispiele konsistent mit dem Kern. Bewahre Autor, Version, Herkunft und MIT-Lizenz. Für die Nutzung in weiteren Umgebungen registriere das gepflegte Paket, statt getrennte Kopien zu erstellen. Die [englische Originalausgabe](../../README.md) und weitere Sprachversionen teilen dieselben didaktischen Prinzipien. Achte bei Änderungen an gemeinsamen Prinzipien auf die Parität aller Editionen; übertrage spezifische nationale Lehrplanvorgaben nicht ungeprüft auf internationale Projekte.

## Arbeitsergebnisse überprüfen

Prüfe die intendierten Handlungen und Lernnachweise der Lernenden, fachliche Richtigkeit, Feedback, Hilfesystem, Barrierefreiheit und Betriebsbedingungen deiner Anwendung. Halte funktionales Verhalten, didaktische Eignung und tatsächlichen Lernerfolg strikt auseinander. Dokumentiere transparent, was geprüft wurde und was ungeprüft bleibt.

Das publizierte [Acht-Aufgaben-Modell-Evaluationsprotokoll](MODEL-EVALUATION.md) liefert vergleichbare Testaufgaben und Bewertungskriterien. Halte diese Kriterien getrennt von den Eingabeprompts der getesteten Modelle. Das Protokoll definiert ein Testverfahren; frühere Vorabtests stellen keine Pauschalbestätigung dar. Berichte nur über tatsächlich durchgeführte Prüfungen und unterscheide erste Entwürfe von nachträglichen Korrekturen.

Entscheide nach Aufgabenkomplexität vor der Wahl eines Modellnamens. Scheitert ein wichtiges Kriterium nach einer gezielten Reparatur erneut, folge den Eskalations- und Abbruchregeln im Modellprofil. Fehlende Quellen oder Werkzeuge lassen sich nicht durch höheren Denkaufwand ersetzen. Standard-Serving ist der Ausgangspunkt; kostenpflichtige Geschwindigkeitsmodi sind eine separat zu autorisierende Entscheidung.

Die weiteren Sprachpakete sind: Tschechisch (`cs/`, ID `vzdelavaci-metodiky`), Spanisch (`es/`, ID `metodologias-de-aprendizaje`), Russisch (`ru/`, ID `metodiki-obucheniya`) und Englisch (Root, ID `learning-methodologies`). Wähle die jeweils benötigte Sprache, statt mehrere Übersetzungen gleichzeitig in den Kontext zu laden.
