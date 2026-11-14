# Adaptives Üben und kontinuierliches Lernen

Konsultiere diese Referenz, wenn die Anwendung wiederholte Lerneinheiten, Zeitpläne (Spaced Repetition) oder eine adaptive Aufgabenauswahl nach Schwierigkeitsgrad erfordert. Unterscheide klar: Wann wird wiederholt, welche Aufgabe wird vorgelegt und wie viel Hilfestellung wird angeboten? Diese drei Aspekte müssen nicht über dasselbe Modell gesteuert werden.

| Bedarf | Einfache Umsetzung | Optionale Erweiterung und Voraussetzungen |
| --- | --- | --- |
| Einzelne Aktivität | Geprüfte Aufgaben, explizite Abfolge, Hilfesystem und Sitzungsstatus | In der Regel kein persistentes Lernendenmodell erforderlich |
| Wiederholen über Tage | Fester Wiederholungsplan und lokaler Verlauf | FSRS bei stabilen Lernobjekten und interpretierbaren Wiederholungsereignissen |
| Schwierigkeit wählen | Geprüfte Aufgabenniveaus und transparente Verzweigungslogik | Elo-Algorithmus bei geeigneten Antwortdaten, Unsicherheitsmodellierung und Kalibrierung |
| Kompetenzabhängigkeiten | Kompetenzraster mit unabhängigen Nachweisen | BKT oder IRT nur mit fundiertem Modell, ausreichenden Daten und Validierung |
| Langzeit-Lernplan | Lernziel, Zeitbudget, aktuelle Phase und nächste Aufgabe | Anpassbare Meilensteine, offene Transferfragen und Wiederholungstermine |

Erkläre die didaktische Funktion vor der algorithmischen Umsetzung. Bewahre den bestehenden Software-Stack; installiere keinen Scheduler, Backend-Dienst oder Kontensystem nur deshalb, weil sie hier aufgeführt sind. Einfache Heuristiken bleiben legitim, wenn ihre Grenzen transparent sind. HLR ist ein weiteres trainiertes Wiederholungsmodell für passende Datensätze, jedoch keine standardmäßige Implementierungspflicht.

## Voraussetzungen vor der Adaption

Definiere stabile IDs für Aufgaben und Kompetenzen, Inhaltsversionen, Antwortinterpretationen und Bedingungen für Hilfestellungen. Trenne erratene, unterstützte, aufgelöste und selbstständig gelöste Antworten sauber voneinander. Halte dich an die Bewertungssemantik der gewählten Bibliothek; werte eine unterstützte Antwort nicht stillschweigend als eigenständige Gedächtnisleistung. Halte spielerische Währungen strikt außerhalb des didaktischen Lernmodells. Nutze minimale Daten und Zeitstempel nur dort, wo sie für die Terminierung zwingend nötig sind.

Definiere das Verhalten bei Kaltstart und eine verlässliche Rückfallebene, falls der Verlauf fehlt, fehlerhaft oder veraltet ist. Prüfe Annahmen anhand repräsentativer Daten, einschließlich Sprach- und Zugangsbedingungen. Ermögliche Korrekturen durch Lehrkräfte sowie den Zugriff der Lernenden auf Hilfen. Vorhergesagte Erfolgswahrscheinlichkeiten sind mit Unsicherheit behaftet; weder eine pauschale Erfolgsquote von 80–90 % noch zwei richtige Antworten messen verlässlich die Zone der nächsten Entwicklung (ZPD) oder beweisen Meisterschaft. Eine angestrebte Behaltensquote (Target Retention) ist ein Abwägungskompromiss bezüglich des Lernaufwands, keine garantierte Lernausbeute.

Verwende bei der Wahl eines Algorithmus eine gepflegte, versionsgeprüfte Implementierung. Teste Updates, Zeitzonen und Tagesgrenzen, doppelte Absendungen, Inhaltsänderungen, Export/Wiederaufnahme und ungültige Eingaben. Vergleiche die algorithmische Erweiterung mit einer einfachen Baseline; Vorhersagegenauigkeit, Engagement und tatsächlicher Lernerfolg sind getrennte Kriterien. Schließe aus Reaktionszeiten niemals auf Beeinträchtigungen oder Persönlichkeitsmerkmale.

## Phasen abschließen oder wiederaufnehmen

Dokumentiere Ergebnis, Unterstützungsbedingungen, offene Fragen und den nächsten erreichbaren Schritt. Das Abschließen einer Phase ist nicht gleichbedeutend mit nachgewiesener Kompetenz. Das Erstellen einer neuen Phase schließt die vorherige nicht automatisch ab. Zusammenfassungen halten notwendige Nachweis-Zeiger und Unsicherheiten fest, statt vollständige Verlaufsprotokolle zu archivieren. Überprüfe bei einer Rückkehr veraltete Annahmen durch eine angemessene diagnostische Aufgabe; Unterbrechungen dürfen den bisherigen Fortschritt nicht löschen.

## Quellen

[Anki FSRS-Dokumentation](https://docs.ankiweb.net/manual/deck-options), [Pelánek zu pädagogischem Elo](https://www.fi.muni.cz/~xpelanek/publications/CAE-elo.pdf) und [Settles & Meeder zu HLR](https://research.duolingo.com/papers/settles.acl16.pdf). Diese Quellen beschreiben spezifische Modelle und Konfigurationen; sie belegen nicht die Wirksamkeit einer neu erstellten Anwendung. Prüfe bei der Integration von Bibliotheken stets deren aktuelle Dokumentation.
