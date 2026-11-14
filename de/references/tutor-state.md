# Tutor-Modi und Lernkontinuität

Konsultiere diese Referenz beim Entwurf eines mehrstufigen Tutors, fortsetzbarer Lernaktivitäten oder Prüfungsvorbereitungen. Diese Regeln gelten ebenso für deterministische Offline-Anwendungen; sie erfordern weder Laufzeit-KI noch Benutzerkonten oder dauerhafte Cloud-Speicher.

## Explizite Modi und Übergänge modellieren

Trenne Erklärung, Übung und Leistungsbeurteilung dort, wo die didaktische Aktivität dies erfordert. Eine Erklärung kann ein ausgearbeitetes Lösungsbeispiel zeigen. Die Übung fordert zu einer Antwort auf, wartet, gibt kriterienorientiertes Feedback und bietet Hilfen an. Die Leistungsbeurteilung folgt deklarierten Regeln bezüglich zulässiger Hilfsmittel und Feedback-Zeitpunkten. Erlaube dem Lernenden jederzeit zu pausieren, Hilfe zu erbitten oder die Aktivität zu verlassen; ein restriktiver Testmodus kann den Versuch beenden oder als unterstützt markieren, sobald inhaltliche Hilfen aufgerufen werden. Erhalte Nachteilsausgleiche zur Barrierefreiheit aufrecht, sofern sie keine inhaltlichen Lösungen vorwegnehmen.

Halte bei dialogischen Übungen jeweils nur eine handlungsleitende Frage offen, es sei denn, die didaktische Aufgabe verlangt ausdrücklich eine Aufgabengruppe. Generiere niemals ungefragt die Antwort des Lernenden vorweg und decke die Lösung während des Wartens nicht eigenmächtig auf. Unterscheide im Anwendungszustand sauber zwischen: Leerlauf (Idle), Warten auf Antwort (Awaiting Answer), Auswertung (Evaluating), Feedback und Pausiert. Verhindere doppelte Absendungen oder ordne sie demselben Versuch zu; eine verspätete Serverantwort darf niemals eine Folgeaufgabe bewerten oder einen zwischenzeitlich geänderten Modus überschreiben. Sprachmodell-Ausgaben sind Antwortvorschläge; ausschließlich Lehrkräfte verändern Noten oder Bewertungsregeln.

Verwalte Modus, Lernziel, aktuelle Aufgabe, Versuchs-ID, Status der Lösungsanzeige und Feedbackstatus direkt im Anwendungszustand. Zeige bei Bedarf eine verständliche Fortschrittsanzeige; das Wiederholen einer dekorativen Statuszeile ersetzt kein echtes Zustandsmanagement. Erläutere bei einem Moduswechsel geänderte Unterstützungsbedingungen und halte vorangegangene Lösungsanzeigen fest. Das bloße Ändern einer Beschriftung macht aus einer zuvor aufgedeckten Aufgabe keine selbstständige Prüfungsleistung. Verwende eine neue, vergleichbare Aufgabe, wenn ein frischer Nachweis eigenständiger Leistung erforderlich ist.

## Aus Lernnachweisen wieder aufnehmen, nicht aus Beherrschungsbehauptungen

Implementiere Speicher- oder Exportfunktionen nur dann, wenn das sitzungsübergreifende Fortsetzen den Nutzenden nützt. Eine kurze anonyme Unterrichtsaktivität benötigt beides meist nicht. Halte für fortsetzbare Arbeiten einen minimalistischen Prüfpunkt (Checkpoint) fest:

- Formatversion, Aktivitäts-/Inhaltsversion und relevante Quellen-IDs.
- Lernziel, aktueller Modus, Aufgaben-/Versuchs-ID und anstehender Einzelschritt.
- Beobachtete Lernnachweise mit Bedingungen: selbstständig gelöst, mit Unterstützung gelöst oder Lösung aufgedeckt; ungeklärte Bewertungen bleiben als ungeklärt markiert.
- Konkrete Fehlerschwerpunkte oder Unsicherheiten und der nächste didaktische Handlungsschritt.
- Zeitstempel nur dort, wo sie für zeitlich versetztes Wiederholen (Spaced Review) oder die Interpretation von Nachweisen zwingend nötig sind.

Vermeide vorschnelle Diagnosen, unnötige Identitätsdaten und vollständige Chat-Protokolle. Dokumentiere transparent, wo Daten gespeichert werden, wer Zugriff hat und wie sie gelöscht werden können; Nutzende an Gemeinschaftsgeräten benötigen eine eindeutige Möglichkeit, ihre Sitzung sauber zu beenden und lokale Daten zu bereinigen. Ein exportierter Checkpoint enthält personenbezogene Lerndaten, selbst wenn kein Klarnamenfeld vorhanden ist. Exportiere niemals geheime API-Schlüssel, versteckte Musterlösungen oder vertrauliche Testinhalte.

Behandle importierte Checkpoints stets als nicht vertrauenswürdige Daten. Validiere Schema, Dateigrößen, IDs und Versionskompatibilität; führe niemals eingebetteten Code aus und akzeptiere importierte Punktwerte niemals ungeprüft als offizielle Noten. Bei folgenreichen Bewertungen gleiche Daten mit dem autoritativen Prüfungsregister unter strikter Zugriffskontrolle ab. Wurden Inhalte aktualisiert oder lässt sich eine Aufgabe nicht mehr eindeutig zuordnen, erkläre die Diskrepanz und setze an einem sicheren, geprüften Einstiegspunkt fort; setze Lernstände nicht stillschweigend zurück und bescheinige keine veralteten Nachweise. Das Wiederherstellen eines offenen Versuchs darf diesen nicht automatisch erneut absenden oder doppelte Punkte vergeben.

Eine Übergabe dokumentiert, was der Lernende an welcher Aufgabe und mit welcher Unterstützung gezeigt hat. Sie behauptet niemals nach einer einzigen Sitzung „vollständige Beherrschung“. Eine spätere neue Aufgabe kann Behaltensleistung oder Transfer überprüfen. Vom Lernenden bestätigte Korrekturen und Interventionen von Lehrkräften müssen von der ursprünglichen Systembeobachtung unterscheidbar bleiben.

## Zielgerichtete Korrektur, ohne den Lernenden festzusetzen

Priorisiere Fehler nach ihrer Relevanz für Lernziel und Voraussetzungen, wobei der Schweregrad als vorläufige Arbeitshypothese gilt. Biete einen gezielten Denkanstoß, einen kontrastierenden Beispielfall oder eine Erklärung an, gefolgt von einer neuen Anwendungsaufgabe. Ermögliche das Aufschieben und spätere Wiederholen. Erzwinge keine willkürlichen Schwellenwerte von 8/10 oder 90 %, verbiete Erklärungen nicht dogmatisch und belege nicht jede Interaktion mit Punkten. Wende transparente Kriterien an, wenn Punkte sinnvoll sind; für offizielle Prüfungsbewertungen gilt die verbindliche Prüfungsspezifikation.

## Prüfungen für die Implementierung

Überprüfe die für das Projekt relevanten Pfade: Frage → Antwort → Feedback; Hilfe → dokumentierter unterstützter Nachweis; Moduswechsel nach Offenlegung der Lösung; Pause/Wiederaufnahme ohne Datenverlust oder doppelte Versuche; veralteter oder beschädigter Checkpoint; verspätete Netzwerkantwort nach Aufgabenwechsel; ungeklärtes Feedback nach einem Verbindungsabbruch. Verifiziere, dass gespeicherter und angezeigter Anwendungszustand exakt übereinstimmen. Diese Tests sichern das technische Verhalten ab, nicht die pädagogische Gesamtwirksamkeit.
