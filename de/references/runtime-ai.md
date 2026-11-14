# Laufzeit-KI in Bildungsanwendungen

Konsultiere diese Referenz nur dann, wenn die fertige Anwendung während der Nutzung durch Lernende einen externen KI-Dienst aufruft. Die Nutzung von KI zum Schreiben von Quellcode oder zum Erstellen lehrkraftgeprüfter Inhalte erfordert keine Laufzeit-KI. Belasse Offline-Aktivitäten offline, es sei denn, das didaktische Lernziel erfordert zwingend einen Live-Dienst.

## Eine klar abgegrenzte didaktische Rolle definieren

Lege verbindlich fest, was das Sprachmodell tun darf, welche geprüften Inhalte oder Fachquellen es nutzen darf und wie es mit fehlenden Belegen umgehen soll. Wo fachliche Korrektheit zählt, bestimme geprüfte Unterrichtsmaterialien und wahre die Quellenprovenienz. Generiere niemals plausibel wirkende, aber erfundene Quellenangaben (Halluzinationen). Lasse Unsicherheit und Korrekturen zu; vermeide Diagnosen oder voreilige Behauptungen über die Fähigkeiten eines Lernenden auf Basis kurzer Interaktionen.

Stimme die Unterstützung auf die didaktische Phase ab. Das Üben erlaubt leitende Fragen, gestufte Hinweise, ausgearbeitete Lösungsbeispiele und direkte Erklärungen, wenn diese angefordert werden oder wenn reines Fragen nicht mehr weiterhilft. Ein Testmodus kann Hilfen gemäß den von der Lehrkraft definierten Regeln einschränken. Erzwinge weder endlose sokratische Schleifen noch ein starres Verbot von Lösungen. Gib dem Lernenden jederzeit die Möglichkeit, Hilfe anzufordern, den Dialog zu beenden oder die Lehrkraft hinzuzuziehen.

Gestalte Schnittstellen zu Live-KI so, dass passives Kopieren verhindert wird – das Werkzeug darf nicht anstelle des Lernenden denken. Verlange vor der Übernahme eines generierten Lösungsschritts eine kurze Reflexionshandlung: Absicht vor der Anfrage klären, kognitive Pause über der Ausgabe einlegen, Vollständigkeit und fachliche Richtigkeit prüfen und den nächsten Schritt bewusst wählen (weiterarbeiten, verifizieren, neu formulieren oder die KI-Ausgabe ablehnen).

Verwende transparente Bewertungsraster (Rubrics) für Feedback und Freitext-Antworten. Vergleiche Modellbeurteilungen mit lehrkraftgeprüften Beispielen, bevor du dich im Produktivbetrieb darauf verlässt. Folgenreiche Leistungs-, Einstufungs- oder Disziplinarentscheidungen erfordern zwingend eine verantwortliche menschliche Überprüfung; eine einzelne Modellausgabe darf niemals alleinige Entscheidungsinstanz sein. Dokumentiere Unsicherheiten und gib Lehrkräften die Möglichkeit, automatisierte Bewertungen zu korrigieren.

## Lernendendaten minimieren

Dokumentiere genau, welche Eingaben an den KI-Anbieter übermittelt werden, was dort gespeichert wird, wer Zugriff hat und wie Löschfristen geregelt sind. Erhebe ausschließlich Daten, die für die didaktische Aktivität zwingend erforderlich sind. Richte Benutzerkonten, Klarnamen, dauerhafte Lernprofile oder Gesprächsprotokollierungen nicht automatisch ein. Nutze anonyme oder pseudonyme Sitzungskennungen, wo dies ausreicht, und weise transparent darauf hin, dass Pseudonyme keine absolute Anonymität garantieren.

Kläre vor dem Einsatz mit Minderjährigen die Zielgruppe, schulische Vereinbarungen, Anbieter-Nutzungsbedingungen und Datenschutzvorgaben (wie DSGVO) mit der verantwortlichen Institution. Stelle keine unbegründeten universellen Altersgrenzen oder Rechtsbehauptungen auf. Erkläre die Datenverarbeitung gegenüber Lernenden und Lehrkräften in altersgerechter, verständlicher Sprache.

## Architektonische Sicherheitsvorkehrungen treffen

Verwalte API-Schlüssel und Zugangsdaten in einer geschützten serverseitigen Komponente, wenn ein externer Dienst geheime Tokens erfordert. Lege geheime Schlüssel niemals im clientseitigen Browser-Code offen. Setze Autorisierung, Ratenbegrenzungen (Rate Limits) und Werkzeugberechtigungen strikt außerhalb des Prompts durch. Behandle Nutzereingaben, abgerufene Dokumente und Modellausgaben stets als nicht vertrauenswürdige Daten.

Trenne Systemanweisungen sauber von dynamischen Inhalten, schränke Werkzeugzugriffe und Netzwerkziele ein, validiere strukturierte JSON-Ausgaben deterministisch und bereinige gerendertes HTML (Sanitization). Verhindere, dass generierter Text direkt als ausführbarer Code (z. B. `eval`) interpretiert wird oder privilegierte Systemaktionen auslöst. Ein System-Prompt, der das Modell anweist, Prompt-Injections zu ignorieren, stellt keine Sicherheitsgarantie dar. Führe für die reale Architektur ein dediziertes Sicherheitsaudit durch.

## Kosten, Fehlertoleranz und Kontinuität planen

Definiere ein realistisches Nutzungsbudget, Limits pro Lernsitzung, Timeouts und Abbrechmöglichkeiten. Zeige während der Wartezeit einen verständlichen Ladestatus an. Fange Netzwerkunterbrechungen, Modellfehler, ungültige JSON-Ausgaben und erschöpfte Kontingente ab, ohne den bisherigen Arbeitsstand des Lernenden zu vernichten. Wiederhole Anfragen (Retries) nur kontrolliert und in begrenzter Zahl.

Biete verlässliche Rückfalloptionen (Fallbacks) an, wie vorab geprüfte Hinweise, statische Übungen, lokal gespeicherte Zwischenstände oder den Hinweis auf die Lehrkraft. Kennzeichne nicht verfügbares Feedback transparent, statt unkontrolliert Scheinausgaben zu generieren. Teste vor dem Unterrichtseinsatz den primären Lernpfad, eine falsche Antwort, eine Hilfeanforderung, uneindeutiges Feedback und den kompletten Ausfall des KI-Dienstes. Dokumentiere ungelöste Systemgrenzen und die Kontrollpflichten der Lehrkraft.

## Generierte Inhalte innerhalb definierter Grenzen verifizieren

Wende vor der Freigabe dynamisch generierter Aufgaben fachliche Prüfungen bezüglich Richtigkeit, Lösbarkeit, Zustandsübergängen und Formatierung an. Fordere Einzigartigkeit nur für Aufgabenformate, die dies explizit versprechen. Validiere Berechtigungen und Schemagrenzen außerhalb des Sprachmodells; ein JSON-Schema garantiert noch keinen wahren Inhalt, und deterministische Prüfungen sichern nur jene Eigenschaften ab, die sie tatsächlich testen. Weise ungültige Inhalte ab oder isoliere sie in einer Quarantäne und halte geprüfte Standardaufgaben als Fallback bereit. Wende für Korrekturen an abhängigen Hinweisen, Bewertungen und Lernfortschritten die Korrekturverfahren aus `assessment.md` an.
