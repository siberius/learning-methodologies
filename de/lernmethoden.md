---
name: lernmethoden
description: Gestalte oder überprüfe Bildungsanwendungen durch die Verknüpfung von Lernzielen, Lernbedürfnissen, Aktivitäten, Feedback und Lernnachweisen. Verwende diesen Skill für neue Lernwerkzeuge oder wesentliche Änderungen ihres didaktischen Designs.
metadata:
  version: "1.5.0"
  language: "de"
  based_on: "learning-methodologies@1.5.0"
  license: "MIT"
  repo: "https://github.com/siberius/learning-methodologies"
  author: "Luděk Sušický"
  format: "natives Paket mit generiertem eigenständigen Markdown"
---


<!-- Generiert aus SKILL.md und references/. Diese Quelldateien bearbeiten. -->


# Lernmethoden

Unterstütze die Konzeption, Umsetzung oder Begutachtung von Bildungsanwendungen, deren Lernaktivitäten, Scaffolding und Leistungsbeurteilung den Bedürfnissen der Zielgruppe entsprechen. Passe die Bearbeitungstiefe an Anfrage, Tragweite und Unsicherheit an. Eine kurze Unterrichtsaktivität benötigt weder eine vollständige Evaluationsstudie noch ein neues Planungsdokument.

## Didaktische Methoden für mit KI erstellte Anwendungen

Nutze diese Methoden, um pädagogische Ziele in konkrete Lernendenhandlungen, Feedbackregeln und Lernnachweise in der erstellten Anwendung zu übersetzen. So erfordert aktiver Abruf (Retrieval Practice) einen eigenständigen Antwortversuch vor der Auflösung; Scaffolding erfordert dosierbare Hilfestellungen und die Unterscheidung zwischen unterstützter und selbstständiger Leistung. KI kann bei der Umsetzung dieser Entscheidungen helfen; ihre Ausgabe bedarf stets der fachlichen und fachdidaktischen Prüfung. Dies gilt sowohl für Offline-Anwendungen als auch für den begründeten Einsatz von Laufzeit-KI.

Konsultiere die [Didaktische Begründung](#reference-didactic-rationale), um die Wahl einer Methode zu begründen oder in die Implementierung zu überführen. Sie verknüpft didaktische Methoden mit Produktentscheidungen und den erforderlichen Lernnachweisen.

## Den Ersteller durch didaktische Entscheidungen führen

Prüfe bei jeder wesentlichen didaktischen Entscheidung Lernziel, Lernendenhandlung, Lernnachweis, Unterstützungsmaßnahmen und Rahmenbedingungen. Baue auf getroffenen Entscheidungen auf. Biete bei einer offenen, folgenreichen Entscheidung eine kleine, relevante Auswahl an – meist zwei bis drei Optionen – jeweils mit einer verständlichen Beschreibung und dem konkreten Bezug zum vorliegenden Projekt. Empfehle eine Option, erläutere den zentralen Kompromiss und frage, welchen Ansatz der Ersteller bevorzugt. Lies den [Entwurfsdialog](#reference-design-dialogue), wenn eine solche Entscheidung begonnen oder wieder aufgegriffen wird. Dieser Dialog steuert die Abstimmung mit dem Ersteller, getrennt von der späteren Interaktion zwischen Tutor und Lernendem.

Bereits getroffene oder abgelehnte Entscheidungen werden ohne neue sachliche Gründe nicht erneut aufgerollt. Respektiere die ausdrückliche Delegation von Routineentscheidungen und fahre mit einer kurzen Begründung fort. Schweigen gilt nicht als Zustimmung zur Erweiterung des Projektumfangs. Arbeite während eventueller Wartezeiten an unabhängigen Komponenten weiter. Kosmetische Änderungen lösen diesen Prozess nicht aus.

Referenzen nach Bedarf laden: [Methoden](#reference-methods) für Lernaktivitäten und Scaffolding; [Lernspiele](#reference-learning-games) für Motivation und Spielmechaniken; [Leistungsbeurteilung](#reference-assessment) für Lernnachweise und Bewertung; [Kognitive Benutzeroberfläche](#reference-cognitive-ux) für Repräsentationen, Multimedia und Aufmerksamkeit; [Adaptives Üben](#reference-adaptive-practice) für wiederholte Lerneinheiten und adaptive Schwierigkeitsgrade. Nutze die nachstehenden Pfade für Simulationen, Tutor-Zustände und Laufzeit-KI. Lies die jeweilige Referenz vor dem Vorschlag einer Methode; lade nicht alle Dateien auf einmal.

Übertrage die gewählte Methode in beobachtbares Anwendungsverhalten und aussagekräftige Tests. Unterscheide sauber zwischen vorgeschlagenen, ausgewählten, implementierten und verifizierten Entscheidungen. Technische Funktionstests belegen noch keinen Lernerfolg.

## Arbeitsablauf

Durchlaufe diesen Pfad in der für die Aufgabe angemessenen Tiefe: Ziel und Rahmenbedingungen klären → Methode passend zum Lernhindernis wählen → Handlung des Lernenden mit Lernnachweisen verknüpfen → im vereinbarten Umfang umsetzen → Ergebnis überprüfen. Untersuche bei einem didaktischen Review den bestehenden Entwurf, statt neu zu implementieren. Nutze bekannten Kontext; verlange nicht für jeden Schritt ein Planungsdokument.

Konsultiere die [Entscheidungsbeispiele](#reference-decision-examples), wenn Hilfestellungen, alternative Lösungswege oder unklare Lehrplanbezüge verdeutlicht werden müssen. Sie dienen als Orientierung, nicht als starre Schablone für jede Unterrichtseinheit.

## Lernkontext erfassen

Verwende bereits vorliegende Informationen aus der Anfrage, dem Projekt und bereitgestellten Materialien. Frage bei Lücken nur nach Angaben, die das didaktische Design wesentlich beeinflussen. Bei geringfügigen Unsicherheiten formuliere eine nachvollziehbare Annahme und fahre fort. Vermeide starre Fragebögen oder wiederholte Freigabeschleifen für Standardentscheidungen, die durch den Auftrag bereits abgedeckt sind.

Erfasse den handlungsleitenden Kontext: Lernende und Vorwissen, Fachgebiet, angestrebte Kompetenzen, Einsatz im Unterricht oder Selbststudium, verfügbare Zeit und Endgeräte, Sprache, Barrierefreiheitsanforderungen und vorgegebene Lehrpläne. Berücksichtige Lehrpläne dort, wo sie für das Einsatzszenario relevant sind; setze kein einzelnes nationales Bildungssystem voraus. Wähle den Tonfall passend zum Kontext und den Wünschen des Autors. Schließe nicht aus pauschalen Generationenbegriffen auf Aufmerksamkeit, Motivation, Leistungsvermögen oder bevorzugte Lernstile.

Beziehe das unterrichtliche Umfeld ein, sofern nützlich: Vorbereitung, Einzel- oder Gruppenarbeit, Lehrkräfteintervention, Plenumsdiskussion und Nachbereitung. Eine lehrkraftzentrierte Demonstration benötigt oft nur einen durchdachten Diskussionsimpuls statt Benutzerkonten und individueller Punkteerfassung.

Trenne Alter, Bildungsrolle und thematische Vorerfahrung; Kind, Schüler, Studierender und erwachsener Teilnehmer sind weder austauschbare Bezeichnungen noch Leistungsstufen. Lies beim Festlegen oder Ändern der Zielgruppe das Lernendenprofil im [Entwurfsdialog](#reference-design-dialogue). Passe Begrifflichkeiten und Unterstützung an das Setting an; nutze in allgemeiner Dokumentation neutrale Begriffe. Entwickler, Lernende und begleitende Lehrkräfte oder Eltern können verschiedene Personen sein.

## Lernziele mit beobachtbaren Aktivitäten verknüpfen

Verknüpfe für jedes wesentliche Lernziel die Handlung des Lernenden, den Lernnachweis, die Erfolgskriterien, die Bedingungen für Hilfestellungen und die nächste didaktische Entscheidung. Halte dies bei kleinen Aufgaben kompakt. Bei forschend-entdeckendem Lernen kann der Nachweis in der Qualität der Fragestellung, der Nutzung von Belegen oder der Überarbeitung einer Erklärung bestehen; eine einzige vorbestimmte Musterantwort ist nicht zwingend.

Beispiel: Der Lernende stellt eine Hypothese auf, wie sich ein veränderter Widerstand auf die Stromstärke auswirkt, überprüft diese an einem Modell, erklärt Abweichungen und löst eigenständig eine Transferaufgabe. Das bloße Verschieben eines Schiebereglers oder Durchklicken von Bildschirmen belegt noch kein Verständnis.

Wähle die didaktische Intervention passend zum beobachteten Lernhindernis. Behandle Erklärungen für Fehler als vorläufige Hypothesen, nicht als gesicherte Diagnosen. Wähle ein kleines, in sich stimmiges Methodenset; überfrachte die Anwendung nicht mit didaktischen Bausteinen, nur weil sie im Katalog existieren. Konsultiere die [Methoden](#reference-methods), wenn eine Methode, Unterstützungssequenz oder Progressionsregel ausgewählt oder implementiert wird.

Lies [Lernspiele und zielgerichtete Gamification](#reference-learning-games) für Spielmechaniken, motivationale Elemente oder Reviews von Lernspielen. Die Referenz behandelt spielbare Lernschleifen, Mechanik-Auswahl, Grenzen der Nachweisbarkeit und Umsetzungen von Minispielen bis hin zu komplexen Lernanwendungen. Berücksichtige Vorwissen und lokalen Kontext für Primarstufe, Sekundarstufe, Hochschule und Erwachsenenbildung.

Die Methodenreferenz behandelt explizit Sokratischen Dialog, Feynman-Methode, Zone der nächsten Entwicklung und Scaffolding, ausgearbeitete Lösungsbeispiele (Worked Examples), aktiven Abruf und zeitlich versetztes Üben (Spaced Practice), Lernen aus Fehlern, Metakognition, forschendes Lernen, Rollenspiele, Peer- und kooperatives Lernen, Projektarbeit, Flipped Classroom und optionale Gamification. Dies sind wählbare Ansätze, keine Pflichtbestandteile jeder Anwendung.

Blooms Taxonomie beschreibt kognitive Zielstufen und Wissensarten. Trenne Schwierigkeitsgrad und Voraussetzungen sauber; erzwinge keine sechs sequentiell gesperrten Stufen. Wähle für praktische oder überfachliche Kompetenzen passende Nachweise und benenne klar, was eine softwarebasierte Aufgabe nicht erfassen kann.

## Eine realistische Umsetzung wählen

Unterscheide zwischen KI, die zur Erstellung der Anwendung dient, und KI, die während der Nutzung durch Lernende aufgerufen wird. Wähle zwischen geprüften statischen Inhalten, deterministischer Interaktionslogik oder Simulationen und Laufzeit-KI anhand von Lernziel und Betriebsrahmen. Hinweise, Feedback und zeitlich versetztes Wiederholen funktionieren hervorragend ohne externe KI-Dienste.

Prüfe vor dem Hinzufügen umfangreicher Funktionen deren didaktischen Mehrwert, Interaktionsaufwand, Betreuungsaufwand für Lehrkräfte, Wartung, Datenbedarf und Betriebskosten. Lege wesentliche Kompromisse offen dar. Ergänze Benutzerkonten, Analytik, Dashboards, Backend-Dienste, Bezahlfunktionen oder externe Datenflüsse nicht nur, um das Produkt vollständiger wirken zu lassen. Hole für weitreichende Architekturentscheidungen die Freigabe ein, sofern sie nicht vorab autorisiert wurden.

Konsultiere [Simulationen](#reference-simulations), wenn Systeme modelliert, Experimente durchgeführt oder Rollenspiele gestaltet werden. Trenne reale Beobachtungen, Modellberechnungen und fiktive Rekonstruktionen eindeutig. Gib erfundene KI-Ausgaben niemals als reale Messwerte aus und täusche kein reales Experiment vor.

Konsultiere [Laufzeit-KI](#reference-runtime-ai) nur dann, wenn das fertige Produkt externe KI-Dienste aufruft. Definiere die pädagogische Rolle, Quellengrenzen, menschliche Aufsicht, Datenflüsse, Kostenlimits und das Verhalten bei Systemausfällen. Ein System-Prompt ersetzt keine Anwendungssicherheit.

Konsultiere [Tutor-Modi und Kontinuität](#reference-tutor-state) bei mehrstufigen Tutoringsystemen, Übergängen zwischen Übungs- und Testmodus oder der Wiederaufnahme von Lernsitzungen. Verwalte Zustand und Lernnachweise direkt in der Anwendung; diese Funktionen erfordern keine Laufzeit-KI.

## Feedback und Entscheidungen verlässlich gestalten

Biete nach Fehlern einen konstruktiven nächsten Schritt an. Ermögliche in Übungsphasen Hilfestellungen und bei Bedarf den Weg zu einer direkten Erklärung oder einem Lösungsbeispiel; vermeide endlose Frageschleifen. Baue Hilfen mit zunehmender Selbstständigkeit ab (Fading), halte angeforderte Unterstützung jedoch zugänglich. Prüfungs- und Testmodi können Hilfen unter transparenten Bedingungen einschränken.

Unterscheide zwischen selbstständigem Erfolg, Erfolg mit Unterstützung, bloßem Betrachten der Lösung und Unsicherheit. Ein erratener Treffer, eine Zuversichtsbekundung oder zwei unterstützte Erfolge begründen noch keine gesicherte Beherrschung. Schließe aus einer kurzen Interaktion weder auf dauerhafte Begabungen noch auf mangelnde Motivation oder Lernstörungen.

Konsultiere die [Leistungsbeurteilung](#reference-assessment) beim Entwurf von bewerteten Aufgaben, Bewertungsrastern (Rubrics), Adaptivität oder Lernerfolgsmessungen. Prüfe fachliche Richtigkeit, plausible Alternativen, Maßeinheiten und Toleranzen sowie die Frage, ob die Aufgabe tatsächlich die Zielkompetenz abprüft. Erkenne fachlich gültige Alternativwege und Begründungen an. Trenne spielerische Belohnungen und Bearbeitungsgeschwindigkeit von fachlicher Leistung, es sei denn, Tempo ist ein explizites Lernziel.

## Zugänglichkeit und Handlungsfähigkeit der Lehrkraft wahren

Orientiere dich an den für die Aktivität und die Lernendenbedürfnisse relevanten WCAG 2.2 AA-Kriterien. Überprüfe Tastaturbedienbarkeit, sichtbaren Fokus, verständliche Beschriftungen und Rückmeldungen, Alternativen zu reiner Farb- oder Tonkodierung sowie begründete oder anpassbare Zeitlimits. Ermögliche flexible Zugangs- und Ausdrucksweisen gemäß UDL; weise Lernenden keine starren Lerntypen zu. Ziehe bei komplexen Anforderungen Fachleute für Barrierefreiheit hinzu.

Erhebe nur Daten, die für die Durchführung der Lernaktivität zwingend erforderlich sind. Dokumentiere, wer Zugriff hat, wohin Daten übertragen und wie lange sie gespeichert werden. Beachte rechtliche Vorgaben von Schule, Träger und Region; stelle keine unbegründeten universellen Rechtsbehauptungen auf. Eine lokale, anonyme Unterrichtsaktivität benötigt weder Benutzerregistrierung noch dauerhaftes Tracking.

Gib Lehrkräften oder Autoren einfache Möglichkeiten an die Hand, Inhalte zu prüfen, automatisierte Bewertungen zu korrigieren und in unpassende Adaptionen einzugreifen. Eine editierbare Inhaltsdatei genügt oft; ein komplexes Verwaltungssystem ist selten nötig. Weitreichende Beurteilungs- oder Einstufungsentscheidungen erfordern stets eine verantwortliche menschliche Überprüfung.

## Fachkompetenzen koordinieren, ohne den Arbeitsablauf aufzublähen

Binde folgende Perspektiven nach Bedarf ein; bei kleineren Aufgaben kann ein einzelner Agent diese Rollen vereinen:

- Fachdidaktiker / Methodiker: Angestrebte Kompetenzen, Unterrichtskontext und didaktische Methodenwahl.
- Fachwissenschaftler / Fachlehrer: Inhaltliche Korrektheit, Voraussetzungen, didaktische Beispiele und typische Fehlvorstellungen.
- Test- und Bewertungsdesigner: Lernnachweise, Kriterienraster, alternative Lösungswege und Grenzen der Diagnostik.
- Interaktionsdesigner: Lernendenführung, Hilfesystem, Barrierefreiheit und Praxistauglichkeit im Unterricht.
- Softwareentwickler: Datenmodelle, Berechnungen, Zustandsverwaltung, Persistenz und Fehlerbehandlung.
- Reviewer / Prüfer: Diskrepanzen zwischen Lernziel, Entwurf und tatsächlichem Anwendungsverhalten.

Übertrage diese Perspektiven verbindlich in die Implementierung. Deklariere eine bequeme technische Lösung niemals ohne didaktische Belege als pädagogisch wertvoll. Kläre fachliche Uneinigkeiten durch Quellenabgleich, gezielte Tests oder eine offene Frage an den Auftraggeber. Setze unabhängige Reviews ein, wenn Komplexität oder Tragweite es erfordern; bilde nicht für jede Routineaufgabe ein großes Team. Binde andere Skills nur für relevante Arbeitsschritte und bei tatsächlicher Verfügbarkeit ein.

## Auf angemessener Ebene überprüfen und berichten

Überprüfe bei Implementierungen den betroffenen Lernpfad, typische reale Lernendenfehler, das Hilfesystem und kritische Fehlerzustände. Berichte bei reinen Analyseaufträgen über Befunde und Vorschläge, ohne das Produkt unaufgefordert zu verändern. Passe Prüfungen an die Anwendung an: Eine Simulation benötigt mathematisch-fachliche Modellprüfungen; Laufzeit-KI benötigt Tests für Verbindungsausfälle und unpassende Modellantworten; einfache statische Aktivitäten benötigen beides standardmäßig nicht.

Halte drei Bewertungen strikt auseinander: funktionale Korrektheit, didaktische Eignung und tatsächlich beobachteter Lernerfolg. Reine Funktionstests beweisen keine didaktische Wirksamkeit. Ein kleiner Unterrichtstest kann Schwachstellen aufdecken, belegt jedoch keine kausale Leistungssteigerung. Berichte reale Testergebnisse und offene Annahmen; erfinde keine Nutzerbeobachtungen oder Wirksamkeitsnachweise.

Fasse bei der Übergabe Lernziel, gewählten Ansatz, wichtige Betriebsannahmen, tatsächlich durchgeführte Tests und verbleibende Grenzen prägnant zusammen. Ergänze eine Tabelle zur Verknüpfung von Zielen und Nachweisen nur dann, wenn sie den praktischen Nutzen erhöht. Stimme das Format auf die Vorgaben des Nutzers ab.

## An Lernende gerichtete Texte ohne KI-Floskeln verfassen

Die Texte der Anwendung tragen den didaktischen Prozess. Wende denselben Maßstab auf Prompts, Arbeitsanweisungen, Feedback und Erklärungen an:

- Streiche inhaltsleere Adjektive („modern“, „ansprechend“, „interaktiv“), es sei denn, der folgende Satz belegt die Eigenschaft konkret.
- Formuliere Aussagen direkt; vermeide Phrasen wie „es ist nicht nur X, sondern auch Y“ oder „dies ist kein X, sondern Y“.
- Verzichte auf formelhafte Ankündigungen wie „In dieser Lerneinheit lernst du...“; benenne direkt die Handlung des Lernenden.
- Feedback benennt präzise, was korrekt ist, was fehlt und welcher konkrete nächste Schritt folgt.
- Halte Zahlen, Einheiten und Bedingungen exakt; kein „verbessert deutlich“ ohne messbare Bezugsgröße.
- Keine Emojis in Schaltflächen, Überschriften oder UI-Beschriftungen. Verwende Text und ein konsistentes Icon-Set.
- Stimme den Wortschatz auf die Zielgruppe ab und verwende einheitliche Fachbegriffe für dieselbe Sache.

Lies Texte aus der Perspektive der Lernenden. Könnte ein Satz wortgleich in einem beliebigen anderen Produkt stehen, streiche ihn oder formuliere ihn fachspezifisch aus.

## Integration

Konsultiere bei der Auswahl von Modell, Denkaufwand (Reasoning Effort) oder Arbeitsgeschwindigkeit sowie bei der Anpassung des Lademechanismus die [Modell- und Host-Profile](#reference-model-profiles). Sie enthalten dokumentierte Leitfäden für OpenAI, Claude und Gemini. Halte an einem einheitlichen didaktischen Kern fest und trenne reale Testergebnisse von theoretischer Kompatibilität. Lade dieses Profil nicht für Standardaufgaben, die es nicht erfordern.

Geeignet für Lernspiele, Quizze, Tutorials, Simulationen, Trainingsanwendungen und Reviews didaktischer Entwürfe. Der Kern benötigt weder externe Pakete, APIs noch spezifische KI-Modelle oder schülerbezogene Daten. Die folgenden Referenzen sind für die eigenständige Nutzung eingebettet. Im nativen Paket sind dies separate Dateien, die nach Bedarf geladen werden. Installation, Deployment und andere externe Dateiänderungen erfordern eine entsprechende Autorisierung. Dieser Skill ersetzt keine projektspezifischen Anweisungen und autorisiert keine eigenmächtige Erweiterung des Projektumfangs.

Gestaltungsreferenzen: [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [CAST UDL-Richtlinien](https://udlguidelines.cast.org/). Diese dienen als Orientierung für Entwurf und Begutachtung; ihre Erwähnung stellt keine Zertifizierung von Konformität oder Bildungswirksamkeit dar.

## Reference: methods

Quellabschnitt: Didaktische Methoden auswählen


Konsultiere diese Referenz, nachdem Lernziel und Erfolgskriterien definiert wurden. Wähle die kleinstmögliche didaktische Intervention, die das aktuelle Lernhindernis wirksam adressiert. Ein Software- oder App-Format bestimmt für sich genommen noch keine Unterrichtsmethode. Überfrachte die Anwendung nicht mit didaktischen Bausteinen, nur weil sie hier verzeichnet sind.

### Methoden: Methodenkarten für die konkrete Auswahl

Verwende diese stabilen Methoden-IDs durchgängig über Übersetzungen und Entscheidungsdokumentationen hinweg. Jede Zeile liefert eine kurze Beschreibung für Ersteller, den Anwendungsbedarf, die Handlung des Lernenden und den Lernnachweis. Die nachfolgenden Abschnitte vertiefen Unterstützungsformen und Grenzen. Benenne für die ausgewählte Karte die einfache Umsetzung, optionale Erweiterungen, eine Fehlerprüfung und die fachliche Quelle; zeige standardmäßig nicht den gesamten Katalog an. Die Quellen belegen didaktische Prinzipien, nicht die Wirksamkeit einer beliebigen generierten Software.

Benenne für die gewählte Karte stets Zielgruppe, nötiges Vorwissen sowie Anpassungen an Sprache, Hilfesystem oder Leistungsbeurteilung; wähle eine Methode niemals rein nach dem Lebensalter aus.

| ID und Kurzbeschreibung | Wann anbieten und einfache Umsetzung | Nachweis und Hilfeprüfung |
| --- | --- | --- |
| `worked-example-fading`: Vorgehensweise sehen, schrittweise vervollständigen, selbstständig anwenden | Neues Verfahren; geprüftes Beispiel und Lückenschritte | Neuer selbstständiger Fall; Fortgeschrittene überspringen lassen, Hilfe bei Bedarf reaktivieren |
| `guided-inquiry`: Hypothese aufstellen, Variable ändern, Ergebnis erklären | Systemverständnis vertiefen; ein abgegrenztes Experiment | Neue Vorhersage begründen; blindes Herumprobieren ersetzt kein logisches Schließen |
| `productive-failure`: Eigene Ansätze erproben, bevor sie mit einer fundierten Erklärung verglichen werden | Ausreichendes Vorwissen und genügend Zeit zur Konsolidierung | Ansätze vergleichen und die konsolidierte Idee anwenden; Anfänger nicht hilflos stranden lassen |
| `retrieval-spacing`: Wissen vor dem Aufdecken aktiv abrufen, später wiederholen | Festigung verfügbaren Wissens; Abrufversuch, Korrektur und spätere Wiederholung | Selbstständiger Abruf nach Zeitabstand; sofortige Fehlerkorrektur ist noch kein Spacing |
| `contrast-interleaving`: Ähnliche Fälle unterscheiden und die passende Lösungsstrategie wählen | Verwechslung von Kategorien oder Verfahren nach erster Übung | Unterscheidungsmerkmal begründen; rein zufälliges Mischen von Themen reicht nicht aus |
| `socratic-dialogue`: Gedankengänge durch gezielte, sequenzierte Fragen hinterfragen | Eine begründete Antwort kann eine fruchtbare Unsicherheit aufdecken | Mit Argumenten verteidigen oder revidieren; direkte Erklärung bleibt jederzeit zugänglich |
| `self-explanation`: In eigenen Worten erklären, Lücken aufdecken und überarbeiten | Lücken nach der ersten Einführung sichtbar machen | Fachliche Korrektheit und Anwendung, nicht bloße sprachliche Gewandtheit |
| `cooperative-project`: Rollen koordinieren, um ein bedeutsames Produkt zu erstellen | Gemeinsame Erkundung oder authentische Aufgabe mit ausreichend Zeit | Individueller Beitrag und Erklärung; Gruppenerfolg belegt nicht individuelle Meisterschaft |
| `role-play`: Aus einer situierten Rolle heraus entscheiden und reflektieren | Perspektivenwechsel, Kommunikation oder berufsbezogenes Urteilsvermögen | Entscheidungen und Konsequenzen begründen; Zustimmung zu einer Spielfigur ist kein Richtigkeitsbeweis |
| `metacognitive-review`: Einen Handlungsplan oder die eigene Zuversicht mit Belegen abgleichen | Selbstregulation und nächste Lernschritte anleiten | Überarbeiteter Handlungsschritt auf Basis von Feedback; Zuversicht ist keine Fachkompetenz |
| `criterion-rubric`: Beobachtbare Qualitätsmerkmale anhand klarer Kriterien beurteilen | Offene Aufgaben, Projekte oder begründete Lösungsalternativen | Grenzbeispiele und Überarbeitungsmöglichkeit; keine bloße Konformität belohnen |
| `representation-transfer`: Konkrete Anschauung und formale Fachnotation verknüpfen | Erfolg bleibt an oberflächliche Spielobjekte gebunden | Anwendung in neuer Repräsentation; barrierefreie, gleichwertige Eingabepfade wahren |

Benenne bei differenzierenden Varianten das gemeinsame Kernlernziel und die didaktische Kernentscheidung, die jede Version beibehalten muss. Variiere Sprache, Repräsentationsformate, Tempo und Hilfestellungen, ohne dem Lernenden diese Kernentscheidung stillschweigend abzunehmen. Bewahre einen motivierenden Kontext auch für Lernende mit hohem Unterstützungsbedarf. Differenziere nach oben durch Begründungen, Gegenbeispiele oder Transferaufgaben statt durch bloße Mengenerhöhung. Kennzeichne eine bewusste Zieländerung explizit. Differenzierung folgt veränderbaren Lernnachweisen, keinen dauerhaften Begabungs-Etiketten.

Optionale Erweiterungen wie Langzeit-Wiederholungsalgorithmen oder Laufzeit-KI bedürfen einer konkreten Begründung und ihrer spezifischen Referenzen. Halte bei Lehrplanbezügen Quelle, Version und Geltungsbereich transparent fest; unterscheide offizielle Bildungsstandards von abgeleiteten Voraussetzungen. Eine Kante in einer Concept-Map ist nicht automatisch eine empirisch geprüfte Lernprogression.

### Methoden: Auswahl nach beobachtetem Lernhindernis

| Beobachtetes Lernhindernis | Didaktische Intervention | Prüfung vor der Umsetzung |
|---|---|---|
| Grundlegendes Wissen wird nicht behalten | Aktiver Abruf mit zeitlich versetztem Wiederholen (Retrieval & Spacing) | Können Lernende das Wissen nach einer zeitlichen Verzögerung selbstständig abrufen? |
| Ein Novize weiß nicht, wie er eine Aufgabe beginnen soll | Ausgearbeitetes Lösungsbeispiel, dann Vervollständigungsaufgaben und freie Übungen | Sind Voraussetzungen erfüllt und Einzelschritte nachvollziehbar? |
| Lernende wiederholen hartnäckig dieselbe Fehlvorstellung | Kontrastierende Fälle, Erklärung, gezielte Frage und korrigierende Übung | Unterscheidet die Aufgabe diese Fehlvorstellung trennscharf von anderen Fehlern? |
| Lernende können Schritte ausführen, aber nicht begründen oder übertragen | Selbsterklärung, Kontrastierungsbeispiele, Transferaufgaben in neuem Kontext | Erfordert der Erfolg echtes logisches Denken statt reines Musternachahmen? |
| Lernende können ihr eigenes Verständnis kaum realistisch einschätzen | Vorhersage formulieren, Zuversicht einschätzen, unabhängiger Test und Reflexion | Können Lernende ihr eigenes Urteil mit objektiver Evidenz abgleichen? |
| Lernziel erfordert forschendes Entdecken oder professionelles Handeln | Angeleitetes forschendes Lernen, Rollenspiel oder Simulation mit Debriefing | Sind Fachmodell, Szenariogrenzen, Belege und Kriterien verlässlich und valide? |

Diese Beobachtungen sind vorläufige didaktische Hypothesen. Eine falsche Antwort, eine lange Reaktionszeit oder eine Bitte um Hilfe diagnostizieren weder eine Lernstörung noch mangelnde Intelligenz oder Persönlichkeitsmerkmale. Frage nach oder untersuche genauer, wenn mehrere Erklärungen infrage kommen.

### Methoden: Bloom als didaktisches Raster

Die revidierte Taxonomie nach Anderson und Krathwohl umfasst zwei Dimensionen: Wissensarten (Faktenwissen, konzeptionelles Wissen, prozedurales Wissen, metakognitives Wissen) und kognitive Prozesse (Erinnern, Verstehen, Anwenden, Analysieren, Evaluieren/Beurteilen, Erschaffen). Nutze sie, um Lernziele präzise zu beschreiben und Aufgabenabdeckungen zu prüfen. Eine Lernaufgabe kann mehrere Prozesse kombinieren; das bloße Verb der Aufgabenstellung belegt noch keine taxonomische Stufe.

Halte Aufgabenschwierigkeit, curriculare Voraussetzungen und Progressionsregeln getrennt. Zwinge Lernende nicht durch sechs starr gesperrte Stufen und schließe nicht aus einer Bloom-Einstufung auf gesicherte Beherrschung. Leite Voraussetzungen aus der Fachstruktur ab. Ergänze praktische, motorische, soziale oder affektive Lernziele mit eigenen beobachtbaren Nachweisen. Blooms kognitive Kategorien erfassen nicht jedes pädagogische Bildungsziel.

### Methoden: Zone der nächsten Entwicklung (ZPD) und Scaffolding

Das Konzept der Zone der nächsten Entwicklung (Wygotski) beschreibt den Bereich zwischen der aktuellen selbstständigen Leistung des Lernenden und dem Leistungsniveau, das er mit kompetenter Unterstützung erreichen kann. Wende diesen Blickwinkel an, wenn ein Lernender eine Aufgabe mit Hilfestellung bewältigen kann, jedoch noch nicht vollkommen selbstständig. Scaffolding bietet temporäre Denkanstöße, Beispiele oder Lösungsfragmente. Schließe aus einem einzelnen Fehler niemals auf eine feste Leistungsgrenze.

Ziehe für Einsteiger ein ausgearbeitetes Lösungsbeispiel mit offenem Denkprozess, eine Lückenaufgabe und anschließendes freies Üben in Betracht. Passe den Detaillierungsgrad an das Vorwissen an. Liefere nur jene Informationen, die für den aktuellen Schritt unverzichtbar sind; rein dekorative Komplexität und kognitive Überlastung schaden dem Lernen.

Nutze ein abgestuftes Hilfesystem: Kläre zunächst das Hindernis, gib einen gezielten Denkanstoß, biete einen Teilschritt an und stelle erst bei anhaltendem Bedarf oder ausdrücklicher Anforderung eine kommentierte Musterlösung bereit. Schließe an jede unterstützte Bearbeitung eine vergleichbare, selbstständig zu lösende Transferaufgabe an. Baue Hilfestellungen schrittweise ab (Fading), sobald sich selbstständiger Erfolg zeigt. Zwei Erfolge oder eine bekundete Zuversicht belegen noch keine dauerhafte Beherrschung.

### Methoden: Sokratischer Dialog

Nutze gezielte Fragen, um Prämissen, Belege und Schlussfolgerungen des Lernenden zu untersuchen, wenn dieser über ausreichendes Grundlagenwissen verfügt, um sinnvoll zu antworten. Der sokratische Elenchos deckt Widersprüche zwischen einer Behauptung und anerkannten Grundannahmen auf; im Bildungskontext dient er niemals dazu, den Lernenden bloßzustellen oder rhetorisch zu besiegen. Die Fragenkategorien nach Paul und Elder bieten Impulse zu Begriffsklärung, Annahmen, Belegen, Perspektiven, Konsequenzen und der Fragestellung selbst.

Stelle jeweils nur eine präzise Frage und gehe auf die tatsächliche Antwort des Lernenden ein. Gib dem Lernenden Raum, eine richtige Antwort zu begründen, statt automatisch jeden ersten Antwortversuch als fehlerhaft anzunehmen. Vermeide endlose Frageschleifen oder das Zurückhalten dringend benötigter Erklärungen. Fehlen wesentliche Voraussetzungen, hilft reines Fragen nicht mehr weiter; bittet der Lernende ausdrücklich um Aufklärung, gehe zu direkter Instruktion oder einem Lösungsbeispiel über.

### Methoden: Feynman-Methode

Lade den Lernenden ein, ein Konzept in eigenen, einfachen Worten so zu erklären, als würde er es einem interessierten Anfänger vermitteln, Verständnislücken präzise zu identifizieren, eine zuverlässige Quelle zu Rate zu ziehen und die Erklärung anschließend zu verfeinern. Dies deckt das tatsächliche Verständnis nach einer ersten Einführung oder vor einer Transferaufgabe auf. Täusche nicht künstlich Unverständnis bei einer präzisen fachlichen Formulierung vor, nur um einen Dialog in die Länge zu ziehen.

Prüfe die fachliche Korrektheit anhand verlässlicher Quellen und eines Kriterienrasters; schließe immer eine praktische Transferaufgabe an. Flüssige Sprache, einfache Analogien und KI-Lob belegen allein noch kein tiefes Fachverständnis. Der Name der Methode garantiert nicht automatisch ihre Wirksamkeit.

### Methoden: Aktiver Abruf, zeitlich versetzte Wiederholung und Reflexion

Aktiver Wissensabruf (Retrieval Practice) fordert Lernende auf, Wissen aktiv aus dem Gedächtnis zu rekonstruieren, bevor die Musterlösung sichtbar wird. Biete korrigierendes Feedback und eine unmittelbare Gelegenheit zur Anwendung. Zeitlich versetzte Wiederholung (Spaced Practice) reaktiviert Inhalte nach einem sinnvollen zeitlichen Abstand; das sofortige Wiedervorlegen eines Fehlers in derselben Sitzung ist reine Fehlerkorrektur, noch kein Spacing. Binde in Wiederholungsphasen auch zuvor korrekt beantwortete Inhalte ein. Kalibriere Wiederholungsintervalle passend zum Lernstoff, zum Behaltensziel und zu den verfügbaren Sitzungen; deklariere keinen Algorithmus als universell perfekt.

### Methoden: Metakognition und selbstreguliertes Lernen

Unterstütze Lernende dabei, sich realistische Teilziele zu setzen, ihre Vorgehensweise zu planen, ihr Text- und Aufgabenverständnis zu überwachen und ihre Strategie anhand von Rückmeldungen anzupassen. Bitte sie, den eigenen Erfolg vorherzusagen oder ihre Entscheidung zu begründen, und gleiche dies anschließend mit ihrer realen Leistung ab. Halte Reflexionsphasen handlungsorientiert: Welche Evidenz hat ihre Ansicht verändert und was probieren sie als Nächstes aus? Setze Selbstvertrauen nicht mit Kompetenz gleich und belaste kleine Lernaktivitäten nicht mit überdimensionierten Pflichttagebüchern.

Schütze bei der Arbeit mit generierten Hinweisen, Lösungsbeispielen oder Live-KI die aktive Rolle des Lernenden im gemeinsamen kognitiven Raum (FALR-Rahmenwerk: Choice, Delay / Kognitive Pause, Evaluation, Self-Direction). Verhindere passive Konsumhaltung: Schalte eine kurze Pause vor der Übernahme einer Modellantwort, damit das Einfügen kein gedankenloser Reflex wird. Fordere den Lernenden auf zu prüfen, ob die Ausgabe fachlich stimmt, was fehlt, was er selbst verstanden hat im Vergleich zu dem, was das System für ihn erledigt hat, und ob er den Vorschlag nutzen, überarbeiten, verifizieren oder ablehnen möchte.

### Methoden: Begriffsnetze und Wissensstrukturen (Concept-Maps)

Setze Begriffsnetze ein, wenn das Erkennen oder Konstruieren von Zusammenhängen expliziter Teil des Lernziels ist. Lass Lernende ein kompaktes Netz erstellen, fehlende Relationen beschriften oder vorgeschlagene Verknüpfungen kritisch beurteilen und mit geprüften Fachquellen oder Rubrics abgleichen. Eine rein von der KI generierte, fertige Concept-Map ist ein Anschauungsmaterial, kein Beleg für das Verständnis des Lernenden.

Kennzeichne Relationen eindeutig: ist Voraussetzung für, ist Teil von, steht im Gegensatz zu, ist assoziiert mit oder verursacht unter bestimmten Bedingungen. Schließe nicht aus bloßer Kookkurrenz auf Kausalität und zwinge vernetzte Wissensstrukturen nicht in eine starre Baumhierarchie. Akzeptiere unterschiedliche fachlich gültige Netzwerkstrukturen; beurteile die Bedeutung und Begründung der Relationen, nicht Bildschirmkoordinaten oder grafische Anordnung.

Nutze für die Implementierung stabile Begriffs-IDs und typisierte, gerichtete Kanten. Stelle barrierefreie text- oder listenbasierte Alternativen sowie Tastaturbedienung bereit; Drag-and-Drop darf nicht die einzige Interaktionsform sein. Eine präzise Beziehungstabelle erfüllt oft denselben didaktischen Zweck ohne aufwendigen Graphen-Editor. Teste mindestens eine alternative korrekte Struktur und eine fehlerhafte Verknüpfung gegen die Feedbackregeln.

### Methoden: Kontextgebundene Methoden

- Forschend-entdeckendes Lernen (Inquiry): Scaffolding für Fragestellung, Hypothese, Test, Beobachtung und Erklärung. Aussagen über reale Phänomene erfordern echte Messdaten oder ein validiertes Modell; illustrative Näherungen müssen als solche gekennzeichnet sein. Sprachmodell-Texte können reale Experimentaldaten nicht ersetzen.
- Rollenspiel: Rollen, Szenariogrenzen und Kriterien für gelungene Interaktion definieren, gefolgt von einer Reflexionsphase (Debriefing). Kennzeichne historische Dialoge als pädagogische Rekonstruktion und trenne belegte Quellen von erfundener Sprache. Fiktionale Interaktionen können reale soziale oder emotionale Wirkungen entfalten.
- Kooperatives Lernen (Peer Learning): Klare gemeinsame Aufgabenstellung, individuelle Verantwortlichkeit jedes Gruppenmitglieds und Kriterien für gegenseitige Erklärungen. Strukturierten Pfad zur Schlichtung von Meinungsverschiedenheiten vorsehen und den Lernerfolg jedes Einzelnen prüfen.
- Lernen durch Lehren (Peer Teaching): Lernende erklären einander Inhalte und geben Kriterienfeedback; verlässliche Fachquellen oder die Lehrkraft bleiben bei Unklarheiten ansprechbar. Unerfahrene Lernende dürfen nicht zur letzten fachlichen Instanz werden.
- Projektorientiertes Lernen: Authentisches Endprodukt, überprüfbare Zwischenmeilensteine und individuelle Lernnachweise. Ein ästhetisch ansprechendes Projektergebnis belegt noch keinen Zuwachs an Fachkompetenz.
- Flipped Classroom / Inverted Classroom: Vorbereitungsphase verbindlich mit der gemeinsamen Präsenzphase verzahnen; didaktische Auffanglösung für Lernende vorsehen, die die Vorbereitung nicht durchführen konnten. Ein Organisationsmodell garantiert nicht automatisch besseres Lernen.
- Gamification: Optionale Fortschritts- oder narrative Elemente nutzen, wenn sie das didaktische Ziel direkt unterstützen. Öffentlicher Wettbewerb, Belohnungssysteme und Tempowertungen erfordern eine didaktische Begründung und barrierefreie Alternativen.

### Methoden: Wissenschaftliche Evidenz und weiterführende Literatur

- [Krathwohl, 2002, A Revision of Bloom's Taxonomy](https://people.ucsc.edu/~ktellez/blooms_taxonomy.pdf): Zweidimensionales Modell und gelockerte Hierarchie mit überlappenden Kategorien.
- [IES, Organizing Instruction and Study to Improve Student Learning](https://ies.ed.gov/ncee/wwc/PracticeGuide/1): Evidenzbasierte Empfehlungen für Spaced Practice, Retrieval Practice, ausgearbeitete Lösungsbeispiele und tiefergehende Erklärungsfragen.
- [UNESCO, Guidance for Generative AI in Education and Research](https://www.iicba.unesco.org/en/africa-education-knowledge-platform/guidance-generative-ai-education-and-research): Menschliche Handlungsmacht (Human Agency) und Validierung didaktischer KI-Nutzung.
- Zinger, D. (CFM / FALR – Four-Action Learner Regulation Framework): Lernenden-Selbstregulation im geteilten kognitiven Raum mit KI (Choice, Delay / Kognitive Pause, Evaluation, Self-Direction).

## Reference: assessment

Quellabschnitt: Lernnachweise, Leistungsbeurteilung und Feedback


### Leistungsbeurteilung: Mit der didaktischen Entscheidung beginnen

Spezifiziere für jedes wesentliche Lernziel die Handlung des Lernenden, die erhobenen Lernnachweise, die Erfolgskriterien und die daraus folgende didaktische Entscheidung. Berücksichtige Rahmenbedingungen wie den Zugriff auf Hinweise, Nachschlagewerke, Zusammenarbeit und Zeitlimits. Definiere handlungsorientierte, praktische oder soziale Kriterien, wenn diese den eigentlichen Kompetenzzielen entsprechen, statt sie durch ein reines Abfragequiz zu ersetzen.

Beispiel: Anhand eines unbekannten Schaltkreises sagt der Lernende die Auswirkung einer Bauteiländerung voraus und begründet diese. Der Lernnachweis umfasst die Vorhersage und die kausale Erklärung. Ein Bewertungsraster (Rubric) prüft das zugrundeliegende physikalische Prinzip, dessen Anwendung und die Argumentation. Eine Fehlvorstellung löst ein kontrastierendes Beispiel und einen weiteren eigenständigen Lösungsversuch aus.

### Leistungsbeurteilung: Zwecke transparent trennen

Im Übungsmodus dürfen Lernende Erklärungen anfordern, Aufgaben wiederholen und abgestufte Hilfen nutzen. Dokumentiere die Nutzung von Hilfestellungen getrennt von selbstständigen Erfolgen. Feedback sollte benennen, was bereits richtig ist, welche Lücke besteht und welcher konkrete nächste Handlungsschritt folgt, unmittelbar verbunden mit der Gelegenheit zur Überarbeitung oder Anwendung.

Lege im Prüfungs- oder Testmodus die zulässigen Hilfsmittel und Bewertungskriterien vor dem ersten Versuch transparent fest. Halte das Verhalten des automatisierten Tutors mit diesen Vorgaben konsistent. Erkläre, ob Feedback sofort oder zeitversetzt erfolgt und warum. Übertrage Übungspunkte niemals stillschweigend in versetzungs- oder notenrelevante Beurteilungen. Formative Leistungsbeurteilung nutzt Nachweise, um den laufenden Lernprozess anzupassen; summative Leistungsbeurteilung dokumentiert den Leistungsstand anhand definierter Kriterien. Ein Punktwert ohne didaktische Folgeentscheidung stellt für sich genommen noch keine formative Beurteilung dar.

### Leistungsbeurteilung: Zuverlässige Aufgaben gestalten

Prüfe Musterlösungen, Erklärungen und plausible Alternativen. Bevorzuge bei Multiple-Choice-Aufgaben didaktisch fundierte Distraktoren, die auf bekannten Fehlvorstellungen beruhen, und vermeide unbeabsichtigte Lösungshinweise im Aufgabentext. Akzeptiere bei offenen Antwortformaten gleichwertige Formulierungen, fachlich gültige Alternativmethoden und offengelegte Prämissen. Erhebe eine einzelne Musterantwort nicht zur einzig gültigen Formulierung.

Nutze ein kompaktes Bewertungsraster mit beobachtbaren Kriterien, deskriptiven Niveaustufen und Beispielen für Grenzfälle sowie alternative Lösungswege. Halte Dimensionen bei Bedarf getrennt: fachliche Korrektheit, Argumentationsgang, methodisches Vorgehen, fachsprachlicher Ausdruck oder Kooperation. Bewerte Rechtschreibung und Grammatik nur dann, wenn sie expliziter Bestandteil des Lernziels sind. Zeitdruck und öffentliche Ranglisten bedürfen einer klaren didaktischen Begründung; Fleißpunkte, Abzeichen (Badges) und Teilnahmebescheinigungen sind keine Nachweise für Fachkompetenz.

Mache bei der Implementierung einer Aufgabenbank die relevanten didaktischen Entscheidungen im bestehenden Datenformat explizit. Sinnvolle Datenfelder können sein: stabile Aufgaben-ID, Ziel-ID, Aufgabenstellung, akzeptierte Antworten oder Rubric, Mustererklärung, abgestufte Hinweise, Quelle und Prüfstatus. Ergänze bei Bedarf physikalische/mathematische Einheiten und Toleranzbereiche. Verwalte Antwortdatensätze getrennt: Antwort des Lernenden, genutzte Hilfen, Versuchszähler und Bewertungsstatus. Dies ist ein illustratives Datenmodell, kein starres Schema; eine einfache gemeinsame Unterrichtsdemonstration benötigt kein individuelles Tracking.

### Leistungsbeurteilung: Grenzen automatisierter KI-Beurteilung

Behandle eine KI-basierte Bewertung oder Fehlerklassifikation stets als vorläufige Einschätzung. Validiere sie anhand von lehrkraftgeprüften Beispielen und deterministischen Fachprüfungen, wo immer möglich. Ist ein Lernnachweis mehrdeutig, fordere eine Präzisierung an oder markiere den Fall zur manuellen Prüfung; täusche keine Scheingenauigkeit vor und nutze unkalibrierte Konfidenzwerte nicht als Beweis. Ermögliche Lernenden, Einspruch gegen automatisiertes Feedback zu erheben, und gib Lehrkräften die Möglichkeit zur manuellen Übersteuerung, wobei die ursprüngliche Antwort und die Begründung der KI sichtbar bleiben müssen. Folgenreiche Leistungsentscheidungen erfordern immer ein verantwortliches menschliches Prüfverfahren, das dem institutionellen Kontext angemessen ist.

### Leistungsbeurteilung: Den Lernerfolgsanspruch überprüfen

Vergleiche nach Möglichkeit eine Eingangsaufgabe (Prätest) mit einer vergleichbaren, selbstständig gelösten Transferaufgabe nach der Instruktion (Posttest), gefolgt von einer zeitverzögerten Stichprobe zur Behaltensleistung und einem Transfer auf einen neuen Kontext. Interpretiere Leistungssteigerungen vorsichtig: Wiederholte identische Aufgaben, Zwischenhinweise und ungleiche Ausgangsbedingungen können Testergebnisse verzerren. Ein kleiner Unterrichtstest deckt praktische Hürden auf, beweist jedoch für sich genommen noch keinen kausalen Lernerfolg.

Erfasse Bearbeitungsquoten, Verweildauer, subjektive Zufriedenheit, Latenzzeiten und Fehlerraten als Betriebs- oder UX-Indikatoren. Trenne sie strikt von tatsächlichen Lernergebnissen. Erhebe nur die für die didaktische Entscheidung zwingend notwendigen Daten und benenne klar, was die vorliegenden Nachweise nicht belegen können.

### Leistungsbeurteilung: Quellen

- [EEF, Teacher Feedback to Improve Pupil Learning](https://educationendowmentfoundation.org.uk/education-evidence/guidance-reports/feedback): Lernabsichten, Erkennung von Verständnislücken, zielgerichtetes Timing und Gelegenheiten zur Umsetzung von Feedback. Dieser Leitfaden für Lehrkräfte-Feedback legitimiert nicht automatisch jede beliebige KI-Feedback-Implementierung.
- [IES Practice Guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/1): Eigenständiger Wissensabruf und zeitverzögerte Wiederholung bilden das Fundament des hier vorgeschlagenen Evaluationsansatzes.

Der Arbeitsablauf, das Beispielraster und die Umsetzungshinweise oben sind Gestaltungsempfehlungen. Ihre Eignung muss stets an Zielgruppe, Fachdisziplin, Tragweite und verfügbaren Nachweisen geprüft werden.

### Leistungsbeurteilung: Aufgabenentscheidungen prüfen und Fehlerfolgen korrigieren

Löse bei Aufgaben mit eindeutiger Antwort die Aufgabenstellung selbstständig und prüfe, ob sich die Distraktoren unter den angegebenen Einheiten, Rundungsregeln und Annahmen widerlegen lassen. Genau eine Antwortoption darf fachlich haltbar sein. Wende bei Multiple-Select-Aufgaben die deklarierte Regel an; erhalte bei offenen Formaten gültige Alternativen. Wende anschließend typische Fehlrechenwege oder Fehlannahmen auf die Aufgabendaten an: Sie müssen exakt den beabsichtigten Distraktor erzeugen. Prüfe nach Änderungen an der Aufgabenstellung alle Antwortoptionen erneut. Gleichwertige Brüche oder uneinheitliche Rundungen dürfen keine ungewollte zweite korrekte Lösung schaffen.

Ordne eine beobachtete Lernendenantwort einer plausiblen Hypothese, einer differenzierenden Folgefrage und einer konkreten didaktischen Anschlussaktion zu. Eine falsche Antwort diagnostiziert noch nicht deren Ursache. Bestimme im Sinne des Evidence-Centered Design die Zielkompetenz, die beobachtbaren Nachweise und die Aufgabe, die diese Nachweise evoziert. Spielhandlungen können triviale Ursachen wie motorische Bedienprobleme, exploratives Ausprobieren oder blindes Raten haben; Telemetriedaten allein belegen weder Ausdauer noch Persönlichkeitseigenschaften. Begründe jede Datenerhebung.

Wenn fachliche Inhalte, die Musterlösung oder die Erklärung des Tutors fehlerhaft sind, korrigiere den Fehler transparent und überprüfe abhängige Hinweise, Folgeaufgaben, Punktwerte und Lernfortschritte. Werte einen dadurch beeinträchtigten Lösungsversuch nicht als Unwissenheit des Lernenden. Sichere die ursprünglichen Nachweisdaten und die Inhaltsversion; kennzeichne Unsicherheiten und biete eine faire Nachprüfung an. Lehrkräfte- und Lernendenansichten müssen stets auf denselben Versionen von Aufgabenstellungen und Antwortoptionen basieren.

Diese Prüfverfahren basieren als didaktische Gestaltungsprinzipien auf den [Check-for-Understanding-Ressourcen der Learning Commons](https://github.com/learning-commons-org/agent-skills/tree/main/skills/k12-check-for-understanding). Sie übernehmen nicht deren starre Formate, US-Lehrplanstandards oder Quellenzuschreibungsbeschränkungen.

## Reference: simulations

Quellabschnitt: Simulationen und Rollenspiele


Konsultiere diese Referenz, wenn eine Anwendung ein System modelliert, ein virtuelles Experiment ermöglicht oder Lernende in einem Szenario handeln lässt. Wende nur die Prüfungen an, die für das konkrete Vorhaben relevant sind.

### Simulationen: Eindeutig kennzeichnen, was die Ausgabe darstellt

Unterscheide für Lernende transparent zwischen folgenden Arten von Ausgaben:

- **Reale Messung:** Beobachtungsdaten eines realen Messinstruments, Datensatzes oder aufgezeichneten Experiments. Benenne Quelle und relevante Messungenauigkeiten.
- **Berechnung oder Modellsimulation:** Ergebnisse, die durch ein definiertes mathematisches oder regelbasiertes Modell erzeugt werden. Lege Modellannahmen und den Gültigkeitsbereich des Modells offen.
- **Fiktion oder didaktische Rekonstruktion:** Didaktisch erfundene Ereignisse, Dialoge, Charaktere oder Konsequenzen. Kennzeichne diese unmissverständlich als solche.

Deklariere generierte Zahlenwerte niemals als reale Messungen und erfundene Dialoge niemals als historische Originalzitate. Eine Simulation kann eine wissenschaftliche Hypothese veranschaulichen; ihre Ausgaben allein beweisen nicht, wie sich die reale Welt verhält.

### Simulationen: Das Fachmodell definieren und überprüfen

Dokumentiere Lernziel, Zustandsvariablen, Eingabeparameter, Maßeinheiten, zulässige Wertebereiche, Annahmen, Übergangsregeln und beobachtbare Ausgaben. Erläutere didaktische Vereinfachungen, die die Interpretation beeinflussen. Wähle Steuerelemente so, dass sie den intendierten Zusammenhang offenlegen, ohne dass Lernende versteckte Einstellungen erraten müssen.

Berechne bei quantitativen Modellen alle Ausgaben über eine deterministische, geprüfte Berechnungslogik oder explizite Fachregeln. Trenne diese mathematische Engine strikt von textuellen Sprachmodell-Erklärungen. Die KI darf reale Modellberechnungen erläutern, darf jedoch keine fehlenden Berechnungen frei erfinden oder vortäuschen, ein reales Experiment habe stattgefunden.

Führe wenige, zum Modell passende Plausibilitätsprüfungen durch: ein bekanntes Standardbeispiel, einen Rand- oder Extremfall, die Einheitenkonsistenz und einen theoretisch erwarteten Trend. Lege bei stochastischen Modellen die Quelle des Zufalls offen und ermögliche reproduzierbare Simulationsläufe (Seed). Dokumentiere Modellgrenzen transparent, statt universelle Gültigkeit zu suggerieren.

### Simulationen: Die didaktische Lernschleife gestalten

Fordere den Lernenden auf, vor dem Start der Simulation eine begründete Vorhersage (Hypothese) aufzustellen, wenn dies das Lernziel unterstützt. Lass ihn relevante Parameter verändern, die tatsächliche Ausgabe beobachten, diese mit der eigenen Vorhersage vergleichen und seine Erklärung überarbeiten. Schließe stets eine Reflexionsphase (Debriefing) an, die zwischen dem Verhalten des Modells und der realen Welt unterscheidet und fragt, an welchen Grenzen das Modell versagt.

Bewerte das Erreichen eines bestimmten Zielzustands auf dem Bildschirm für sich genommen noch nicht als Verständnis. Verlange eine Erklärung, einen Vergleich oder den Transfer auf eine neue Problemstellung.

### Simulationen: Historische und soziale Rollenspiele

Kennzeichne, ob eine Figur fiktiv ist, einen Idealtypus darstellt oder auf einer realen historischen Persönlichkeit beruht. Halte historisch belegte Fakten strikt unterscheidbar von didaktisch rekonstruierter Sprache. Gib Quellenbelege für historische Behauptungen an und weise auf umstrittene Deutungen hin. Täusche niemals einen authentischen Zugang zu den inneren Gedanken einer realen Person vor und erfinde keine Quellen.

Definiere Rolle, Szenariogrenzen, pädagogisches Lernziel und die abschließende Reflexionsphase. Biete einen klaren Ausstieg aus der Rolle und Zugang zu neutralen Facherklärungen. Stimme emotionale Intensität und Thematik auf die Zielgruppe und den Unterrichtskontext ab; halte bei sensiblen Themen alternative Aufgaben bereit. Beurteile das intendierte Argumentations- oder Kommunikationsvermögen anhand transparenter Kriterien; bloße Übereinstimmung mit der Spielfigur ist kein Kompetenznachweis.

## Reference: runtime-ai

Quellabschnitt: Laufzeit-KI in Bildungsanwendungen


Konsultiere diese Referenz nur dann, wenn die fertige Anwendung während der Nutzung durch Lernende einen externen KI-Dienst aufruft. Die Nutzung von KI zum Schreiben von Quellcode oder zum Erstellen lehrkraftgeprüfter Inhalte erfordert keine Laufzeit-KI. Belasse Offline-Aktivitäten offline, es sei denn, das didaktische Lernziel erfordert zwingend einen Live-Dienst.

### Laufzeit-KI: Eine klar abgegrenzte didaktische Rolle definieren

Lege verbindlich fest, was das Sprachmodell tun darf, welche geprüften Inhalte oder Fachquellen es nutzen darf und wie es mit fehlenden Belegen umgehen soll. Wo fachliche Korrektheit zählt, bestimme geprüfte Unterrichtsmaterialien und wahre die Quellenprovenienz. Generiere niemals plausibel wirkende, aber erfundene Quellenangaben (Halluzinationen). Lasse Unsicherheit und Korrekturen zu; vermeide Diagnosen oder voreilige Behauptungen über die Fähigkeiten eines Lernenden auf Basis kurzer Interaktionen.

Stimme die Unterstützung auf die didaktische Phase ab. Das Üben erlaubt leitende Fragen, gestufte Hinweise, ausgearbeitete Lösungsbeispiele und direkte Erklärungen, wenn diese angefordert werden oder wenn reines Fragen nicht mehr weiterhilft. Ein Testmodus kann Hilfen gemäß den von der Lehrkraft definierten Regeln einschränken. Erzwinge weder endlose sokratische Schleifen noch ein starres Verbot von Lösungen. Gib dem Lernenden jederzeit die Möglichkeit, Hilfe anzufordern, den Dialog zu beenden oder die Lehrkraft hinzuzuziehen.

Gestalte Schnittstellen zu Live-KI so, dass passives Kopieren verhindert wird – das Werkzeug darf nicht anstelle des Lernenden denken. Verlange vor der Übernahme eines generierten Lösungsschritts eine kurze Reflexionshandlung: Absicht vor der Anfrage klären, kognitive Pause über der Ausgabe einlegen, Vollständigkeit und fachliche Richtigkeit prüfen und den nächsten Schritt bewusst wählen (weiterarbeiten, verifizieren, neu formulieren oder die KI-Ausgabe ablehnen).

Verwende transparente Bewertungsraster (Rubrics) für Feedback und Freitext-Antworten. Vergleiche Modellbeurteilungen mit lehrkraftgeprüften Beispielen, bevor du dich im Produktivbetrieb darauf verlässt. Folgenreiche Leistungs-, Einstufungs- oder Disziplinarentscheidungen erfordern zwingend eine verantwortliche menschliche Überprüfung; eine einzelne Modellausgabe darf niemals alleinige Entscheidungsinstanz sein. Dokumentiere Unsicherheiten und gib Lehrkräften die Möglichkeit, automatisierte Bewertungen zu korrigieren.

### Laufzeit-KI: Lernendendaten minimieren

Dokumentiere genau, welche Eingaben an den KI-Anbieter übermittelt werden, was dort gespeichert wird, wer Zugriff hat und wie Löschfristen geregelt sind. Erhebe ausschließlich Daten, die für die didaktische Aktivität zwingend erforderlich sind. Richte Benutzerkonten, Klarnamen, dauerhafte Lernprofile oder Gesprächsprotokollierungen nicht automatisch ein. Nutze anonyme oder pseudonyme Sitzungskennungen, wo dies ausreicht, und weise transparent darauf hin, dass Pseudonyme keine absolute Anonymität garantieren.

Kläre vor dem Einsatz mit Minderjährigen die Zielgruppe, schulische Vereinbarungen, Anbieter-Nutzungsbedingungen und Datenschutzvorgaben (wie DSGVO) mit der verantwortlichen Institution. Stelle keine unbegründeten universellen Altersgrenzen oder Rechtsbehauptungen auf. Erkläre die Datenverarbeitung gegenüber Lernenden und Lehrkräften in altersgerechter, verständlicher Sprache.

### Laufzeit-KI: Architektonische Sicherheitsvorkehrungen treffen

Verwalte API-Schlüssel und Zugangsdaten in einer geschützten serverseitigen Komponente, wenn ein externer Dienst geheime Tokens erfordert. Lege geheime Schlüssel niemals im clientseitigen Browser-Code offen. Setze Autorisierung, Ratenbegrenzungen (Rate Limits) und Werkzeugberechtigungen strikt außerhalb des Prompts durch. Behandle Nutzereingaben, abgerufene Dokumente und Modellausgaben stets als nicht vertrauenswürdige Daten.

Trenne Systemanweisungen sauber von dynamischen Inhalten, schränke Werkzeugzugriffe und Netzwerkziele ein, validiere strukturierte JSON-Ausgaben deterministisch und bereinige gerendertes HTML (Sanitization). Verhindere, dass generierter Text direkt als ausführbarer Code (z. B. `eval`) interpretiert wird oder privilegierte Systemaktionen auslöst. Ein System-Prompt, der das Modell anweist, Prompt-Injections zu ignorieren, stellt keine Sicherheitsgarantie dar. Führe für die reale Architektur ein dediziertes Sicherheitsaudit durch.

### Laufzeit-KI: Kosten, Fehlertoleranz und Kontinuität planen

Definiere ein realistisches Nutzungsbudget, Limits pro Lernsitzung, Timeouts und Abbrechmöglichkeiten. Zeige während der Wartezeit einen verständlichen Ladestatus an. Fange Netzwerkunterbrechungen, Modellfehler, ungültige JSON-Ausgaben und erschöpfte Kontingente ab, ohne den bisherigen Arbeitsstand des Lernenden zu vernichten. Wiederhole Anfragen (Retries) nur kontrolliert und in begrenzter Zahl.

Biete verlässliche Rückfalloptionen (Fallbacks) an, wie vorab geprüfte Hinweise, statische Übungen, lokal gespeicherte Zwischenstände oder den Hinweis auf die Lehrkraft. Kennzeichne nicht verfügbares Feedback transparent, statt unkontrolliert Scheinausgaben zu generieren. Teste vor dem Unterrichtseinsatz den primären Lernpfad, eine falsche Antwort, eine Hilfeanforderung, uneindeutiges Feedback und den kompletten Ausfall des KI-Dienstes. Dokumentiere ungelöste Systemgrenzen und die Kontrollpflichten der Lehrkraft.

### Laufzeit-KI: Generierte Inhalte innerhalb definierter Grenzen verifizieren

Wende vor der Freigabe dynamisch generierter Aufgaben fachliche Prüfungen bezüglich Richtigkeit, Lösbarkeit, Zustandsübergängen und Formatierung an. Fordere Einzigartigkeit nur für Aufgabenformate, die dies explizit versprechen. Validiere Berechtigungen und Schemagrenzen außerhalb des Sprachmodells; ein JSON-Schema garantiert noch keinen wahren Inhalt, und deterministische Prüfungen sichern nur jene Eigenschaften ab, die sie tatsächlich testen. Weise ungültige Inhalte ab oder isoliere sie in einer Quarantäne und halte geprüfte Standardaufgaben als Fallback bereit. Wende für Korrekturen an abhängigen Hinweisen, Bewertungen und Lernfortschritten die Korrekturverfahren aus `assessment.md` an.

## Reference: model-profiles

Quellabschnitt: Modelle, Denkaufwand, Ausführungsgeschwindigkeit und Host-Anpassung


Konsultiere diese Referenz, wenn ein Modell empfohlen, eine Stufe für Denkaufwand (Reasoning Effort) oder Ausführungsgeschwindigkeit gewählt oder das Ladeverhalten der Host-Umgebung angepasst werden soll. Die didaktischen Kernanweisungen bleiben über alle Modellanbieter hinweg identisch.

### Modellprofile: Was diese Referenz nicht beansprucht

Die Empfehlungen sind praxisorientierte Ausgangskonfigurationen für diesen Arbeitsablauf, kein empirischer Benchmark und keine Rangliste. Sie belegen nicht, dass eine bestimmte Modellfamilie per se didaktisch überlegen ist, und prognostizieren keine exakten Latenzzeiten. Modellbezeichnungen, verfügbare Parameter, Tarife und Preise ändern sich fortlaufend. Überprüfe vor der Verwendung eines Modells die tatsächliche Modellliste des Nutzers und die aktuelle offizielle Dokumentation des Anbieters. Ein Name in der Benutzeroberfläche entspricht nicht zwingend der exakten API-Modell-ID. Deklariere eine Konfiguration erst dann als verifiziert, wenn sie an repräsentativen didaktischen Aufgaben erfolgreich getestet wurde.

Dokumentationsstand geprüft: 04.11.2026.

### Modellprofile: Nach Aufgabe wählen vor der Wahl des Modellnamens

Nutze ein kleineres Modell für eng umrissene Textkorrekturen mit eindeutigen Vorgaben, ein mittelgroßes Modell für Standardkonzeption und Implementierung und ein leistungsstärkeres Spitzenmodell bei widersprüchlichen Quellenbelegen, komplexen Simulationen oder folgenreichen Begutachtungen. Dies sind funktionale Aufgabenkategorien, keine garantierten Modellfähigkeiten. Behalte die bestehende Modellauswahl des Nutzers bei, wenn sie die didaktischen Anforderungen erfüllt.

Die folgende Tabelle enthält **ungetestete Startempfehlungen für diesen Skill**, abgeleitet aus den Herstellerdokumentationen.

### Modellprofile: Eskalations- und Abbruchregeln

Starte bei einer klar umrissenen Aufgabe mit dem standardmäßigen Denkaufwand des Systems oder einer zuvor erfolgreichen Konfiguration. Ziehe bei widersprüchlichen Quellen oder komplexen Fachmodellen von Beginn an ein höheres Denkniveau in Betracht. Wenn die Modellausgabe eine explizite Vorgabe ignoriert, ihrer eigenen Punktevergabe widerspricht, fachliche Rechenprüfungen verfehlt oder wiederholt unbrauchbare Aufgabenstellungen erzeugt, prüfe zuerst, ob die relevanten Eingabedateien und Referenzen für das Modell tatsächlich zugänglich waren. Korrigiere fehlende Eingaben oder uneindeutige Kriterien, bevor das Modell gewechselt wird.

Scheitert nach einer gezielten Fehlerkorrektur derselbe wesentliche Prüfpunkt erneut, empfehle eine höhere Stufe des Denkaufwands (Reasoning Effort) und evaluiere dieses Kriterium neu. Bleibt der Fehler bestehen, empfehle ein stärkeres verfügbares Modell oder ein unabhängiges didaktisches Review entsprechend der Tragweite. Wiederhole Versuche nicht endlos und überschreite nicht das vereinbarte Budget. Fehlende Fachquellen, nicht verfügbare Softwarewerkzeuge oder Serverausfälle erfordern die Behebung der Ursache oder die transparente Benennung der Grenze; zusätzlicher Denkaufwand kann fehlende empirische Evidenz nicht herbeizaubern. Berichte ungelöste Probleme offen. Ändere Konfigurationen nur über autorisierte Bedienelemente des Hosts.

Reduziere den Denkaufwand oder wechsle zu einem kleineren Modell erst, nachdem alle wesentlichen didaktischen Prüfungen erfolgreich bestanden wurden; dokumentiere den Abwägungskompromiss. Behandle die Ausführungsgeschwindigkeit getrennt: Standard-Serving ist der Ausgangspunkt; kostenpflichtige Beschleunigungstarife (Fast Tiers) bedürfen einer sachlichen Begründung und Autorisierung.

### Modellprofile: Empfehlungen aktuell halten

Prüfe die namentlichen Empfehlungen erneut, wenn sich Modell- oder Host-Versionen ändern, ein Konfigurationsparameter entfällt, der Anbieter die Verfügbarkeit ändert oder das dokumentierte Verhalten von realen Beobachtungen abweicht. Kennzeichne eine Paarung bis zur Verifikation als ungeprüft und nutze Aufgabenkategorien sowie die Standardwerte des jeweiligen Hosts. Erfinde keine Äquivalenzparameter für unbekannte Modelle. Ergänze anbieterspezifische didaktische Workarounds erst, wenn ein reproduzierbarer Fehler deren Notwendigkeit belegt; dokumentiere die betroffene Version und entferne Workarounds, sobald sie hinfällig werden.

### Modellprofile: Aufgabe und Steuerungsoptionen abstimmen

| Aufgabe | OpenAI Ausgangspunkt | Claude Ausgangspunkt | Gemini Ausgangspunkt |
|---|---|---|---|
| Kleine, klar spezifizierte Text- und Inhaltsanpassungen, Review strukturierter Aufgaben | GPT-6 Luna, High; Denkaufwand erst reduzieren, wenn Prüfungen stabil halten | Haiku 5.5, Medium | Gemini 3.5 Flash-Lite, Low wo unterstützt |
| Didaktische Konzeption und Implementierung einer abgegrenzten Lernaktivität | GPT-6.1 Sol, Standard-Denkaufwand oder Medium | Sonnet 5.5, Medium für klar umrissene agentische Aufgaben | Gemini 3.8 Flash, Medium |
| Schwieriges didaktisches Audit, widersprüchliche Quellen, komplexe Simulation oder Architektur | GPT-6 Astra, Light/Low oder Medium; bei Bedarf erhöhen | Opus 5.5, Medium, dann High falls erforderlich | Gemini 4 Argon, Medium, dann High falls erforderlich |

Diese Zuordnungen sind Empfehlungen des Autors, abgeleitet aus den Herstellerleitfäden. Ist ein ausgewähltes Modell nicht verfügbar, schlage eine erreichbare Alternative vor und lege den Wechsel offen; verändere Nutzerauswahlen nicht eigenmächtig ohne Autorisierung. Ein bestehender Workflow auf Gemini 3.1 Pro kann beispielsweise dieses Modell und dessen Thinking-Stufen beibehalten. Miss die Latenz für repräsentative Aufgaben in der tatsächlichen Zielumgebung.

Unterscheide stets drei Ebenen: das Sprachmodell, die Tiefe des Denkaufwands (Reasoning Effort) und eventuelle priorisierte Ausführungsgeschwindigkeiten (Fast Mode). Ein geringerer Denkaufwand reduziert Rechenschritte; die Fast-Option eines Anbieters ist ein separater Infrastrukturparameter und kann zusätzliche Kosten verursachen. Die Modellbezeichnung Flash steht für eine Modellfamilie, nicht für einen allgemeinen Turboschalter. Gleiche Begriffe wie Low, Medium und High versprechen zwischen unterschiedlichen Produkten keineswegs identische Denktiefe oder Antwortzeiten.

Starte mit Standard-Ausführungsgeschwindigkeit. Empfehle einen kostenpflichtigen Fast-Modus nur, wenn Wartezeiten kritisch sind und der Zugriffstarif dies rechtfertigt. Aktiviere keine Zusatzoptionen und buche keine Kapazitäten ohne ausdrückliche Freigabe. Streaming verbessert die visuelle Rückmeldung des Fortschritts; es ist kein Beleg für frühere Fertigstellung oder höhere inhaltliche Qualität. Beurteile die Gesamtdauer immer einschließlich didaktischem Review, Werkzeugaufrufen und Korrekturschleifen.

### Modellprofile: OpenAI und Codex

Verwende das native Paket dort, wo die Entwicklungsumgebung Skills unterstützt und Referenzdateien einlesen kann. In Codex kann der Skill explizit über `$learning-methodologies` oder `$vzdelavaci-metodiky` (bzw. `$lernmethoden`) aufgerufen werden. Gehe in einfachen Chat-Schnittstellen nicht von einer automatischen Erkennung im Dateisystem aus; stelle dort stattdessen die zusammenhängende eigenständige Markdown-Datei als Kontext bereit.

Der aktuelle Leitfaden empfiehlt Sol für umfangreiche Entwicklungsarbeiten, Luna für fokussierte Routineaufgaben und Astra für besonders anspruchsvolle didaktische Workflows; Luna High und Astra Light/Low sind dokumentierte Startwerte. In Codex ist Fast eine Infrastrukturwahl für Antwortzeiten, unabhängig vom didaktischen Denkaufwand. Verfügbarkeit und Kontingente hängen vom Modell, Account und Client ab. Prüfe unterstützte Parameter vor der Konfiguration; ein UI-Label ist nicht automatisch eine API-Modell-ID.

Definiere ein konkretes Arbeitsergebnis, den Projektumfang, relevante Dateien und beobachtbare Akzeptanzkriterien. Verlange präzise didaktische Entscheidungen und Nachweise, nicht die Offenlegung interner Gedankengänge (CoT). Nutze die Werkzeuge und Berechtigungen des Hosts; leite aus dem bloßen Modellnamen keine Shell- oder Browserberechtigungen ab.

Quellen: [Modelle](https://learn.chatgpt.com/docs/models), [Geschwindigkeit](https://learn.chatgpt.com/docs/agent-configuration/speed), [Skills](https://developers.openai.com/plugins/concepts/skills).

### Modellprofile: Claude und Claude Code

Claude Code unterstützt `SKILL.md`-Pakete und begleitende Referenzdateien. Nach der Erkennung kann der Skill explizit über `/learning-methodologies`, `/vzdelavaci-metodiky` oder `/lernmethoden` aufgerufen werden. Prüfe in anderen Claude-Umgebungen den Lademechanismus oder binde die eigenständige Distribution ein. Füge dem gemeinsamen Frontmatter keine Claude-spezifischen Hooks, Shell-Substituierungen oder Modellüberschreibungen hinzu.

Für agentische Aufgaben mit Sonnet 5.5 empfiehlt die Dokumentation Medium für gut definierte Aufgaben und höhere Werte für komplexe Probleme. Opus 5.5 nutzt standardmäßig Medium; ältere Modelle und Schnittstellen weichen ab. Der API-Parameter für Effort und der interaktive Denkmodus sind unterschiedliche Konzepte. Nicht alle Modellgenerationen unterstützen dieselben Kombinationen. Bevorzuge integrierte Host-Einstellungen, statt API-Parameter manuell in Chat-Prompts zu kopieren. Claudes Fast-Modus ist eine separate, modellabhängige Funktion mit abweichender Bepreisung.

Grenze Aufgabe, didaktische Materialien und das angestrebte Ergebnis präzise ein. Mache deutlich, wo der Agent eigenständig entscheiden darf und wo didaktische Belege zwingend sind. Ein gut gewähltes Aufgabenbeispiel klärt Unklarheiten oft besser als die Wiederholung des gesamten Skills. Diese modulare Struktur sichert Portabilität und stellt keine Behauptung über Claude-spezifische kognitive Merkmale dar.

Quellen: [Skills](https://code.claude.com/docs/en/skills), [Modelle](https://platform.claude.com/docs/en/models/overview), [Effort](https://platform.claude.com/docs/en/build-with-claude/effort), [Fast-Modus](https://platform.claude.com/docs/en/build-with-claude/fast-mode).

### Modellprofile: Gemini und Gemini CLI

Gemini CLI erkennt native Skills in den dafür vorgesehenen Verzeichnissen, einschließlich des `.agents/skills`-Pfads. Überprüfe die Erkennung mit `/skills list` und aktualisiere bei Bedarf mit `/skills reload`. Workspace-Vertrauensstellungen und Berechtigungsfreigaben unterliegen dem Host; umgehe diese Sicherheitsmechanismen nicht. Binde in Google AI Studio oder allgemeinen Web-Chats die eigenständige Datei ein, wenn kein natives Skill-Laden unterstützt wird.

Die geprüfte Dokumentation führt für Gemini 4 Argon und Gemini 3.8 Flash die Stufen Low, Medium und High auf. Andere Gemini-Versionen besitzen abweichende Standardwerte und Stufen. Verwende ausschließlich Parameter, die vom realen Modell und API-Client unterstützt werden; übersetze Denkaufwandsparameter von OpenAI oder Claude nicht blind 1:1. Eine Vorschau-Bezeichnung (Preview) und ein stabiler Release-Name sind nicht austauschbar.

Für `gemini-3.1-pro-preview` verzeichnet die API-Tabelle Low, Medium und High, mit High als Standardwert. Für diesen Endpunkt empfiehlt der Autor Medium für Standardaufgaben und High für schwierige didaktische Audits, sofern der Host diese Steuerung bereitstellt. Ein in der UI angezeigtes Label wie Gemini 3.1 Pro belegt noch nicht, welchen genauen Endpunkt die Anwendung nutzt.

Halte Arbeitsanweisungen prägnant und benenne Lernziel, Rahmenbedingungen und zu liefernde Lernnachweise. Hänge referenzierte Unterrichtsmaterialien direkt an, damit das Modell tatsächlichen Zugriff hat; eine bloße Pfadangabe im Text gewährt keinen Dateizugriff. Halte bei der Entwicklung von Anwendungen auf Basis der Gemini API den vorgeschriebenen Zustand von Werkzeugdialogen gemäß offizieller Dokumentation ein. Dieser Skill implementiert diesen API-Layer nicht selbst und autorisiert keine unaufgeforderte Einbindung.

Quellen: [Modelle](https://ai.google.dev/gemini-api/docs/models), [Thinking](https://ai.google.dev/gemini-api/docs/thinking), [Gemini CLI Skills](https://geminicli.com/docs/cli/tutorials/skills-getting-started/).

### Modellprofile: Portabler Einsatz und Verifikation

Halte die erforderlichen Metadaten standardkonform: `name` und `description`, gefolgt von gewöhnlichem Markdown. Optionale Metadaten beschreiben die Edition; verlasse dich niemals auf ein hosts-spezifisches Metadatenfeld, um eine Sicherheitsgrenze durchzusetzen. Verwende die gebündelten relativen Referenzen in dateifähigen Agentenumgebungen oder die vollständige eigenständige Markdown-Datei in einfachen Chats. Lade standardmäßig nicht mehrere Sprachversionen gleichzeitig. Führe nach einem Kontextverlust des Hosts wesentliche Vorgaben und offene Aufgaben erneut ein, statt vorauszusetzen, dass jeder Host den vollständigen Verlauf behält.

Emojis können Bedeutungen unterstützen, dürfen jedoch niemals der einzige Instruktions- oder Prioritätsträger sein. Bewahre stets explizite Textbeschriftungen. Forschung zu [Emoji-Semantik](https://arxiv.org/abs/2409.10760) und [kontextueller Mehrdeutigkeit](https://arxiv.org/abs/2511.07193) zeigt, dass dekorative Emojis die Regeltreue von Sprachmodellen nicht verlässlich verbessern. Teste solche Änderungen an realen Modellen und Aufgaben, bevor ein didaktischer Nutzen behauptet wird.

Bevor eine Modell-/Host-Kombination als getestet gilt, verifiziere: erfolgreiche Erkennung oder fehlerfreies Laden der eigenständigen Datei, Zugriff auf relevante Referenzen, ein repräsentatives didaktisches Arbeitsergebnis und das Einhalten kritischer Systemgrenzen. Dokumentiere die exakte Modell-ID oder das sichtbare Label, Host und Version, Sprache, Denkaufwand, Ausführungsgeschwindigkeit, Werkzeuge, Datum, erzeugte Artefakte und aufgetretene Fehler. Trenne rein dokumentationsbasierte Kompatibilität strikt von beobachteter Ausführung. Übertrage einen erfolgreichen Test eines Modells niemals pauschal auf die gesamte Modellfamilie.

Nutze für Vergleiche identische Aufgabenstellungen und Ausgangsmaterialien. Lass die generierten Ergebnisse durch einen fachkundigen Prüfer anhand einheitlicher didaktischer Kriterien bewerten. Prüfe die Wiederverwendung bekannten Kontexts, kontrollierte Hilfestellungen, alternative korrekte Lösungen, den Umgang mit nicht belegten Lehrplanansprüchen, Modell-/Datengrenzen sowie Fehlerzustände bei Werkzeug- oder Dienstausfällen. Reduziere den Denkaufwand oder wechsle zu kleineren Modellen nur so lange, wie alle wesentlichen Prüfungen stabil bestanden werden. Ist der direkte Zugriff auf ein System nicht möglich, kennzeichne es transparent als ungetestet, statt Testergebnisse zu fingieren.

## Reference: decision-examples

Quellabschnitt: Entscheidungsbeispiele


Nutze diese Beispiele, um konkrete Zweifelsfälle im didaktischen Design zu lösen. Passe Fachgebiet und Altersstufe an; behalte das didaktische Entscheidungsprinzip bei.

### Entscheidungsbeispiele: Eine gleichwertige Antwort anerkennen

Aufgabe: Drücke 1,5 A in Milliampere aus. Der Lernende gibt `1500 mA` ein; der automatisierte Test erwartet die Zahl `1500`. Akzeptiere die physikalisch gleichwertige Größe unter Prüfung von Zahlenwert und Maßeinheit. Wenn das Lernziel explizit die reine Zahleneingabe oder Konventionen der Einheitennotation prüft, erfasse dies gesondert. Behandle nicht jede Zeichenkette durch unüberlegtes Zeichenlöschen als gleichwertig: `1500 A` ist hier eindeutig falsch. Didaktischer Grund: Formale Formatierungsfragen dürfen den eigentlichen Nachweis des Einheitenverständnisses nicht verdecken.

### Entscheidungsbeispiele: Eine unproduktive sokratische Schleife beenden

Während einer Übung sagt der Lernende nach einer Frage zu Stromstärke und Widerstand: „Ich verstehe es immer noch nicht; bitte zeig es mir.“ Biete eine kurze Erklärung oder ein ausgearbeitetes Lösungsbeispiel bei konstanter Spannung an und stelle anschließend eine neue Vorhersageaufgabe mit optionaler Hilfestellung. Stelle nicht endlos weitere Gegenfragen als Vorbedingung für Unterstützung. Dokumentiere das Lösungsbeispiel als unterstütztes Lernen; eine neue, eigenständig gelöste Aufgabe liefert den separaten Kompetenznachweis. Didaktischer Grund: Fragen sollen den Lernfortschritt fördern, nicht die Instruktion blockieren. Für explizite Testmodi können abweichende Hilferegeln gelten.

### Entscheidungsbeispiele: Eine fachlich unzutreffende Feynman-Erklärung korrigieren

Ein Lernender erklärt: „Pflanzen holen sich ihre Nahrung aus dem Boden; das Sonnenlicht wärmt sie nur auf.“ Würdige die verständliche Formulierung, ohne den fachlichen Fehler zu akzeptieren. Benenne die konkrete Fehlvorstellung, konsultiere eine fachlich geprüfte Quelle, unterscheide Wasser/Mineralstoffe von den bei der Photosynthese gebildeten Zuckern und lade zu einer überarbeiteten einfachen Erklärung ein. Überprüfe den Transfer mit einem neuen Fall, z. B. was bei Lichtentzug geschieht. Didaktischer Grund: Sprachliche Flüssigkeit und Einfachheit belegen noch keine fachliche Korrektheit. Erfinde keine experimentellen Daten und führe Pflanzenwachstum nicht monokausal auf einen einzelnen Faktor zurück.

### Entscheidungsbeispiele: Mit einem nicht verfügbaren Lehrplan arbeiten

Eine Lehrkraft fordert eine „vollständige Ausrichtung an unserem schulinternen Lehrplan“, stellt jedoch kein Dokument zur Verfügung. Nutze das formulierte Lernziel, um einen vorläufigen Unterrichtsentwurf zu erstellen. Fordere den relevanten Lehrplanauszug nur an, wenn eine exakte curriculare Deckung zwingend ist; benenne transparent, was ungeprüft bleibt. Erfinde niemals lokale Kompetenzcodes und zertifiziere keine curriculare Vollständigkeit. Ein allgemeiner Verweis auf nationale oder regionale Rahmenlehrpläne (wie Bildungsstandards oder Kerncurricula) belegt noch keine Passung zum konkreten Schulcurriculum. Didaktischer Grund: Die didaktische Konzeption kann konstruktiv voranschreiten, während die Grenzen der formalen Abdeckung klar sichtbar bleiben.

### Entscheidungsbeispiele: Eine kognitive Pause vor der Übernahme von KI-Ausgaben einfügen

In einer Anwendung mit integriertem KI-Assistenten bittet ein Lernender um einen Lösungsweg oder eine Fehlererklärung. Biete anstelle einer Schaltfläche „In meine Lösung übernehmen“ eine bewusste kognitive Pause an: Verhindere direktes Einfügen und stelle eine kurze Reflexionsfrage („Welcher Denkschritt ist hier zentral? Was fehlt dem KI-Vorschlag für deinen spezifischen Fall?“). Ermögliche dem Lernenden, den Vorschlag zu überarbeiten, an einem anderen Beispiel zu verifizieren oder ihn ganz zu verwerfen. Werte den generierten Text des Modells als in Anspruch genommene Unterstützung, nicht als Beleg für eigenes Verständnis. Didaktischer Grund: Eine kognitive Pause verhindert das gedankenlose Kopieren von Modellantworten ohne tiefere mentale Verarbeitung.

## Reference: tutor-state

Quellabschnitt: Tutor-Modi und Lernkontinuität


Konsultiere diese Referenz beim Entwurf eines mehrstufigen Tutors, fortsetzbarer Lernaktivitäten oder Prüfungsvorbereitungen. Diese Regeln gelten ebenso für deterministische Offline-Anwendungen; sie erfordern weder Laufzeit-KI noch Benutzerkonten oder dauerhafte Cloud-Speicher.

### Tutor-Zustand: Explizite Modi und Übergänge modellieren

Trenne Erklärung, Übung und Leistungsbeurteilung dort, wo die didaktische Aktivität dies erfordert. Eine Erklärung kann ein ausgearbeitetes Lösungsbeispiel zeigen. Die Übung fordert zu einer Antwort auf, wartet, gibt kriterienorientiertes Feedback und bietet Hilfen an. Die Leistungsbeurteilung folgt deklarierten Regeln bezüglich zulässiger Hilfsmittel und Feedback-Zeitpunkten. Erlaube dem Lernenden jederzeit zu pausieren, Hilfe zu erbitten oder die Aktivität zu verlassen; ein restriktiver Testmodus kann den Versuch beenden oder als unterstützt markieren, sobald inhaltliche Hilfen aufgerufen werden. Erhalte Nachteilsausgleiche zur Barrierefreiheit aufrecht, sofern sie keine inhaltlichen Lösungen vorwegnehmen.

Halte bei dialogischen Übungen jeweils nur eine handlungsleitende Frage offen, es sei denn, die didaktische Aufgabe verlangt ausdrücklich eine Aufgabengruppe. Generiere niemals ungefragt die Antwort des Lernenden vorweg und decke die Lösung während des Wartens nicht eigenmächtig auf. Unterscheide im Anwendungszustand sauber zwischen: Leerlauf (Idle), Warten auf Antwort (Awaiting Answer), Auswertung (Evaluating), Feedback und Pausiert. Verhindere doppelte Absendungen oder ordne sie demselben Versuch zu; eine verspätete Serverantwort darf niemals eine Folgeaufgabe bewerten oder einen zwischenzeitlich geänderten Modus überschreiben. Sprachmodell-Ausgaben sind Antwortvorschläge; ausschließlich Lehrkräfte verändern Noten oder Bewertungsregeln.

Verwalte Modus, Lernziel, aktuelle Aufgabe, Versuchs-ID, Status der Lösungsanzeige und Feedbackstatus direkt im Anwendungszustand. Zeige bei Bedarf eine verständliche Fortschrittsanzeige; das Wiederholen einer dekorativen Statuszeile ersetzt kein echtes Zustandsmanagement. Erläutere bei einem Moduswechsel geänderte Unterstützungsbedingungen und halte vorangegangene Lösungsanzeigen fest. Das bloße Ändern einer Beschriftung macht aus einer zuvor aufgedeckten Aufgabe keine selbstständige Prüfungsleistung. Verwende eine neue, vergleichbare Aufgabe, wenn ein frischer Nachweis eigenständiger Leistung erforderlich ist.

### Tutor-Zustand: Aus Lernnachweisen wieder aufnehmen, nicht aus Beherrschungsbehauptungen

Implementiere Speicher- oder Exportfunktionen nur dann, wenn das sitzungsübergreifende Fortsetzen den Nutzenden nützt. Eine kurze anonyme Unterrichtsaktivität benötigt beides meist nicht. Halte für fortsetzbare Arbeiten einen minimalistischen Prüfpunkt (Checkpoint) fest:

- Formatversion, Aktivitäts-/Inhaltsversion und relevante Quellen-IDs.
- Lernziel, aktueller Modus, Aufgaben-/Versuchs-ID und anstehender Einzelschritt.
- Beobachtete Lernnachweise mit Bedingungen: selbstständig gelöst, mit Unterstützung gelöst oder Lösung aufgedeckt; ungeklärte Bewertungen bleiben als ungeklärt markiert.
- Konkrete Fehlerschwerpunkte oder Unsicherheiten und der nächste didaktische Handlungsschritt.
- Zeitstempel nur dort, wo sie für zeitlich versetztes Wiederholen (Spaced Review) oder die Interpretation von Nachweisen zwingend nötig sind.

Vermeide vorschnelle Diagnosen, unnötige Identitätsdaten und vollständige Chat-Protokolle. Dokumentiere transparent, wo Daten gespeichert werden, wer Zugriff hat und wie sie gelöscht werden können; Nutzende an Gemeinschaftsgeräten benötigen eine eindeutige Möglichkeit, ihre Sitzung sauber zu beenden und lokale Daten zu bereinigen. Ein exportierter Checkpoint enthält personenbezogene Lerndaten, selbst wenn kein Klarnamenfeld vorhanden ist. Exportiere niemals geheime API-Schlüssel, versteckte Musterlösungen oder vertrauliche Testinhalte.

Behandle importierte Checkpoints stets als nicht vertrauenswürdige Daten. Validiere Schema, Dateigrößen, IDs und Versionskompatibilität; führe niemals eingebetteten Code aus und akzeptiere importierte Punktwerte niemals ungeprüft als offizielle Noten. Bei folgenreichen Bewertungen gleiche Daten mit dem autoritativen Prüfungsregister unter strikter Zugriffskontrolle ab. Wurden Inhalte aktualisiert oder lässt sich eine Aufgabe nicht mehr eindeutig zuordnen, erkläre die Diskrepanz und setze an einem sicheren, geprüften Einstiegspunkt fort; setze Lernstände nicht stillschweigend zurück und bescheinige keine veralteten Nachweise. Das Wiederherstellen eines offenen Versuchs darf diesen nicht automatisch erneut absenden oder doppelte Punkte vergeben.

Eine Übergabe dokumentiert, was der Lernende an welcher Aufgabe und mit welcher Unterstützung gezeigt hat. Sie behauptet niemals nach einer einzigen Sitzung „vollständige Beherrschung“. Eine spätere neue Aufgabe kann Behaltensleistung oder Transfer überprüfen. Vom Lernenden bestätigte Korrekturen und Interventionen von Lehrkräften müssen von der ursprünglichen Systembeobachtung unterscheidbar bleiben.

### Tutor-Zustand: Zielgerichtete Korrektur, ohne den Lernenden festzusetzen

Priorisiere Fehler nach ihrer Relevanz für Lernziel und Voraussetzungen, wobei der Schweregrad als vorläufige Arbeitshypothese gilt. Biete einen gezielten Denkanstoß, einen kontrastierenden Beispielfall oder eine Erklärung an, gefolgt von einer neuen Anwendungsaufgabe. Ermögliche das Aufschieben und spätere Wiederholen. Erzwinge keine willkürlichen Schwellenwerte von 8/10 oder 90 %, verbiete Erklärungen nicht dogmatisch und belege nicht jede Interaktion mit Punkten. Wende transparente Kriterien an, wenn Punkte sinnvoll sind; für offizielle Prüfungsbewertungen gilt die verbindliche Prüfungsspezifikation.

### Tutor-Zustand: Prüfungen für die Implementierung

Überprüfe die für das Projekt relevanten Pfade: Frage → Antwort → Feedback; Hilfe → dokumentierter unterstützter Nachweis; Moduswechsel nach Offenlegung der Lösung; Pause/Wiederaufnahme ohne Datenverlust oder doppelte Versuche; veralteter oder beschädigter Checkpoint; verspätete Netzwerkantwort nach Aufgabenwechsel; ungeklärtes Feedback nach einem Verbindungsabbruch. Verifiziere, dass gespeicherter und angezeigter Anwendungszustand exakt übereinstimmen. Diese Tests sichern das technische Verhalten ab, nicht die pädagogische Gesamtwirksamkeit.

## Reference: didactic-rationale

Quellabschnitt: Warum didaktische Methoden in die KI-gestützte Anwendungsentwicklung gehören


Konsultiere diese Referenz, wenn der Zweck dieses Skills erläutert werden soll oder geklärt werden muss, wie eine didaktische Methode das Verhalten einer Anwendung konkret verändern soll. Der Skill unterstützt Entwickler und Lehrkräfte, die mithilfe von KI Bildungsanwendungen konzipieren und programmieren. Er leitet ebenso Anwendungen an, die begründet Laufzeit-KI während des Lernens einsetzen. Die didaktische Methode muss sich direkt in den Handlungen der Lernenden, den Feedbackregeln und den erhobenen Lernnachweisen niederschlagen. Ein bloßer Satz in einem Prompt oder ein Schlagwort auf der Benutzeroberfläche genügen nicht.

### Didaktische Begründung: Didaktische Entscheidungen in beobachtbares Verhalten übersetzen

| Didaktische Methode oder Perspektive | Pädagogischer Zweck | Entscheidung im Anwendungsdesign | Zu prüfender Lernnachweis |
|---|---|---|---|
| Sokratischer Dialog | Prämissen und Gedankengänge des Lernenden hinterfragen | Gezielte Frage stellen, Denkzeit einräumen, auf die tatsächliche Antwort eingehen; bei Bedarf direkte Erklärung anbieten | Lernender kann Behauptung begründen oder revidieren, einschließlich gültiger Alternativen |
| Feynman-Methode und Selbsterklärung | Die eigene Erklärung des Lernenden überprüfbar machen | Lernenden in eigenen Worten erklären lassen, mit fachlichen Kriterien abgleichen, Lücken adressieren, neuen Transferfall anbieten | Fachliche Korrektheit der Zusammenhänge; sprachliche Gewandtheit allein belegt kein Verständnis |
| Ausgearbeitete Beispiele und Scaffolding | Novizen den Einstieg erleichtern und schrittweise in die Selbstständigkeit führen | Gelösten Schritt vorgeben, Vervollständigungsaufgabe stellen, neue Transferaufgabe anbieten; Hilfen zugänglich halten | Unterstützte Bearbeitung sauber von einem späteren selbstständigen Lösungsversuch unterscheiden |
| Aktiver Abruf und zeitlich versetztes Wiederholen | Rekonstruktion von Wissen üben und nach zeitlichem Abstand reaktivieren | Vor dem Aufdecken der Lösung abfragen; korrigierendes Feedback geben und Wiederholungen terminieren | Leistung vor Aufdeckung der Lösung; spätere Behaltensleistung und Transferfähigkeit |
| Begriffsnetze (Concept-Maps) | Beziehungen und Wissensstrukturen explizit machen | Beschriftete Relationen fordern, alternative korrekte Strukturen akzeptieren, barrierefreie Alternativen bieten | Fachliche Bedeutung und Begründung der Verknüpfungen, nicht bloße visuelle Ähnlichkeit |
| Forschendes Lernen und Simulationen | Hypothesen unter expliziten Modellannahmen mit Evidenz abgleichen | Relevante Variablen, Einheiten und Modellgrenzen offenlegen; Reflexionsphase (Debriefing) einbetten | Lernender überarbeitet Hypothese anhand von Beobachtungen oder transparenten Modellberechnungen |
| Formative Beurteilung und Metakognition | Den nächsten didaktischen Schritt aus Lernnachweisen ableiten | Spezifisches Feedback geben, Lernende eigene Vorhersagen mit tatsächlichen Resultaten vergleichen lassen | Umsetzbare Korrektur und neuer Nachweis; Punkte und Zuversichtswerte reichen allein nicht aus |
| Kooperatives Lernen und Peer-Feedback | Vergleichen und Erklären mit individueller Verantwortlichkeit fördern | Gemeinsame Aufgabe mit individuellen Beiträgen und strukturierter Klärung von Meinungsverschiedenheiten | Individuelle Argumentation; ein gemeinsamer Klick belegt kein Gruppenverständnis |
| Ko-Regulation im geteilten kognitiven Raum (FALR) | Lernende bei der Nutzung von KI oder Hinweisen aktiv und kritisch halten | Kognitive Pause vor Übernahme von Ausgaben erzwingen; fragen, was verstanden wurde vs. was das System tat | Unterscheidung zwischen eigenem Verständnis und Systemausgabe, gefolgt von eigenem Handlungsschritt |

Blooms Taxonomie dient der präzisen Beschreibung kognitiver Zielstufen und Wissensarten; sie schreibt weder lineare Schwierigkeitsgrade noch eine starre Freischaltung in sechs Stufen vor. Eine Methode ist nur dann angemessen, wenn sie zur Zielgruppe, zum fachlichen Inhalt und zum beobachteten Lernhindernis passt. Kein Katalog verlangt die gleichzeitige Umsetzung aller Methoden.

### Didaktische Begründung: Warum dies bei der KI-gestützten Programmierung entscheidend ist

Moderne KI generiert Benutzeroberflächen, Antwortprüfungen und Feedback in Sekundenschnelle. Diese Software-Artefakte benötigen jedoch einen didaktischen Vertrag: Was genau soll der Lernende tun, was gilt als valider Lernnachweis, welche Hilfen standen zur Verfügung und wie leitet sich daraus die nächste didaktische Entscheidung ab? Nutze diesen Vertrag, um den generierten Code und die Inhalte verbindlich zu steuern. Aktiver Abruf verändert beispielsweise den Zeitpunkt, zu dem eine Lösung aufgedeckt werden darf; Scaffolding verändert Hilfebuttons und Fortschrittslogiken. Eine Methode bloß im Code-Kommentar zu benennen, ohne ihr didaktisches Verhalten zu implementieren, verfehlt das Ziel.

Trenne KI während der Entwicklung strikt von KI zur Laufzeit. Geprüfte statische Inhalte und deterministische Programmierlogik genügen für die allermeisten dieser didaktischen Verhaltensweisen völlig offline. Falls Laufzeit-KI für offene Antworten oder Freitext-Dialoge unverzichtbar ist, begrenze Quellen, Prüfkriterien und Werkzeuge, validiere Ausgaben deterministisch und baue eine klare Fallback-Ebene für Ausfälle ein. Mehr generierter Chat, strengere Punktevergabe oder ein größeres Sprachmodell bedeuten keineswegs automatisch besseres Lernen.

### Didaktische Begründung: Grenzen der didaktischen Begründung benennen

Dieser Leitfaden begründet Gestaltungsentscheidungen; er beweist nicht, dass dieser Skill oder jede daraus entstandene Implementierung automatisch Lernergebnisse verbessert. Fachliche Richtigkeit, Barrierefreiheit und Praxistauglichkeit im Schulalltag erfordern Vor-Ort-Prüfungen im tatsächlichen Nutzungskontext. Funktionierende Software belegt noch keinen Bildungserfolg; hierfür sind geeignete Lernnachweise und für kausale Wirksamkeitsaussagen kontrollierte Evaluationsstudien nötig. Die in den Methodenreferenzen verlinkten Forschungsergebnisse stützen konkrete Gestaltungsprinzipien, zertifizieren aber nicht automatisch die Gesamtanwendung. Behalte die Überprüfung durch Lehrkräfte bei folgenreichen Leistungsentscheidungen stets bei und passe Inhalte an den realen Lehrplan an.

## Reference: learning-games

Quellabschnitt: Lernspiele und zielgerichtete Gamification


Konsultiere diese Referenz, wenn ein Projekt Spielmechaniken, motivationale Elemente oder ein substanzielles Redesign von Spiel und Lernen erfordert. Die Empfehlungen verbinden empirische Forschung mit didaktischen Entwurfsentscheidungen; sie garantieren nicht automatisch den Lernerfolg eines neuen Produkts. Evidenzstand geprüft: 14.11.2026.

### Lernspiele: Die Lernaktivität vor der Belohnung wählen

Unterscheide klar zwischen einem Lernspiel (Lernen geschieht durch das Spielen selbst), Gamification (Spielelemente unterstützen eine eigenständige Lernaktivität) und einer Simulation (ein Modell ermöglicht forschendes Erkunden ohne zwingendes Punktesystem oder Siegbedingungen). Ein didaktisch hervorragendes Werkzeug benötigt oft keines der unten genannten Belohnungssysteme.

Formuliere einen kompakten didaktischen Entwurfsvertrag: Lernende und Vorwissen; angestrebte Kompetenz; Entscheidung der Spielenden; Konsequenz und Feedback; unabhängiger Lernnachweis; nächster didaktischer Schritt. Für eine kleine Übung genügt ein Absatz. Identifiziere typische Abkürzungen und Fehlanreize: Kann ein Spieler durch blindes Raten, schnelles Durchklicken, Auswendiglernen von Positionen, sofortiges Ablesen der Lösung oder Verlassen auf Teammitglieder gewinnen?

Bevorzuge Spielmechaniken, die exakt das intendierte Denkhandeln erfordern. Um proportionales Denken zu fördern, lasse die Spielenden ein Gemisch unter sinnvollen physikalischen/chemischen Randbedingungen justieren, eine Vorhersage begründen und anschließend einen neuen Transferfall lösen. Ein einfaches Quiz kann weiterhin hervorragend dem aktiven Abruf dienen; nicht jeder Fakt muss künstlich in eine komplexe Spielwelt eingebettet werden. Erlaube bei offenen Lernzielen alternative, fachlich begründbare Lösungswege.

### Lernspiele: Eine kleine, in sich stimmige Auswahl treffen

| Bedarf | Mögliche Spielmechanik und Umsetzung | Prüfkriterium oder Fehlerbedingung |
|---|---|---|
| Einstieg ohne Vorkenntnisse der Steuerung | Eine sichere, direkt spielbare Einstiegsaufgabe; Werkzeuge erst bei Bedarf einführen | Ein neuer Nutzer bewältigt die Interaktion ohne mündliche Erklärung des Autors |
| Systemverständnis aufbauen | Vorhersage treffen, eine Variable gezielt verändern, Konsequenzen beobachten, erklären | Willkürliches Ausprobieren darf die neue Hypothesenbildung nicht ersetzen |
| Wissen dauerhaft behalten | Zeitverzögerte Abruf-Missionen mit korrigierendem Feedback | Spätere ungestützte Leistung; sofortiges Weiterspielen ist Fehlerkorrektur, kein Spacing |
| Das richtige Lösungsverfahren wählen | Typen verwechselbarer Aufgaben nach erster Übung mischen (Interleaving) | Lernender wählt und begründet eine Strategie; reines Mischen von Themen reicht nicht aus |
| Fortschritt vom Anfänger zum Könner | Ausgearbeitetes Beispiel, teilweise Vervollständigung, selbstständige Challenge | Hilfenutzung bleibt transparent; Unterstützung kann bei Bedarf zurückkehren |
| Eigenen Lernfortschritt sehen | Individuelles Kompetenzraster mit Nachweisen und nächsten Schritten | Aufgabenerledigung, unterstützter Erfolg und eigenständige Nachweise bleiben trennbar |
| Selbstbestimmung und Handlungsspielraum | Sinnvolle Wahlmöglichkeiten bei Lernweg, Kontext oder Methode im Rahmen des Ziels | Entscheidungen verändern das Lernerleben; Voraussetzungen und Alternativen bleiben klar |
| Neugier wecken | Ein Rätsel oder Fall, dessen Hinweise aus fachlichen Belegen bestehen | Die Enthüllung beantwortet eine didaktische Frage; Textlesen darf das Üben nicht ersticken |
| Kooperatives Lernen | Komplementäre Rollen, gemeinsames Gruppenergebnis, rotierende Aufgaben | Jedes Gruppenmitglied erklärt oder wendet Teilaspekte eigenständig an |
| Anerkennung | Optionale Auszeichnungen (Badges), gekoppelt an transparente Leistungen | Ein Badge beschreibt einen Nachweis; er ersetzt niemals das didaktische Urteil |
| Wettbewerb | Optionale, faire Herausforderungen oder Vergleich mit dem eigenen Fortschritt | Benachteiligung, Frustration und Hektik prüfen; immer einen Pfad ohne Rangliste bieten |
| Langfristige Motivation | Selbstgewählte Lernziele, fortsetzbare Sitzungen, optionale Erinnerungen | Pausen dürfen weder Lernergebnisse löschen noch den Zugang zu Hilfen sperren |

Dies sind didaktische Hypothesen, keine Rangliste universell wirksamer Features. Punkte, Streaks (Tagesserien), Avatare und Bestenlisten besitzen für sich genommen keinen garantierten Lerneffekt. Halte spielinterne Währungen strikt getrennt von bildungsbezogenen Lernnachweisen. Gewöhnliche Lernfehler dürfen niemals den Zugang zum Unterricht oder zu weiteren Lerninhalten sperren. Vermeide Druck durch verfallende Belohnungen, bezahlte Wiederbelebungen, zufallsbasierte Belohnungskäufe oder öffentliche Bloßstellung. Dies sind professionelle Leitplanken für das Produktdesign, keine Behauptung, jede Variante sei bereits isoliert empirisch getestet.

Lass die Schwierigkeit aus der fachlichen Kernentscheidung erwachsen. Hohe Textlast, motorische Hürden oder künstlicher Zeitdruck verfälschen die Leistungsmessung. Setze Zeitlimits nur dann ein, wenn Reaktionsgeschwindigkeit oder Geläufigkeit (Fluency) explizite Lernziele sind; halte Genauigkeit und Geschwindigkeit getrennt interpretierbar. Es gibt keine universell optimale Erfolgsquote. Passe den Unterstützungsgrad anhand mehrerer Beobachtungen an und ermögliche es Lernenden sowie Lehrkräften, unpassende Einstufungen manuell zu korrigieren.

### Lernspiele: Die didaktische Lernsequenz gestalten

Führe zunächst eine spielbare, didaktisch fokussierte Aufgabe ein, bevor ein komplexes Belohnungssystem aufgebaut wird. Auf jede Handlung muss eine für den Lernenden interpretierbare Konsequenz, nützliches Feedback, eine neue Gelegenheit zur Erprobung und ein natürlicher Ausstiegspunkt folgen. Erkläre Fehler auf der Ebene der Aufgabenstrategie. Ein bloßer Glückwunsch-Jubelschirm kann Fehlvorstellungen nicht korrigieren.

Nutze ein ausgearbeitetes Lösungsbeispiel (Worked Example), wenn fehlendes Vorwissen sinnvolle Lösungsversuche blockiert. Eine initiale Erkundungsaufgabe kann auf die anschließende Instruktion vorbereiten; produktives Scheitern (Productive Failure) erfordert jedoch eine fundierte Konsolidierungsphase. Es rechtfertigt keineswegs, Anfänger frustriert feststecken zu lassen. Trenne Erstinstruktion, gestütztes Üben und selbstständige Leistungsbeurteilung. Das Aufdecken einer Lösung markiert einen unterstützten Versuch; prüfe die Kompetenz später an einer neuen Aufgabe.

Gestalte aktiven Abruf (Retrieval Practice), zeitlich versetztes Wiederholen (Spaced Repetition) und Aufgabenmischung (Interleaving) passend zum Lerngegenstand. Plane Wiederholungen sowohl für früher korrekte Inhalte als auch für Fehlerschwerpunkte ein. Fordere vor der Offenlegung der Antwort die aktive Rekonstruktion ein. Mische Aufgabentypen, die eine Unterscheidung erfordern, mit aufgabenspezifischem Feedback. Deklariere keinen festen Wiederholungsintervall-Algorithmus als pauschales Allheilmittel für jedes Schulfach.

### Lernspiele: An Altersstufen und Kontexte anpassen

Orientiere dich am realen Vorwissen und Unterstützungsbedarf statt an stereotypen Generationszuschreibungen. Kinder in der Primarstufe benötigen oft konkrete Anschauungsmodelle und Lesehilfen; Jugendliche in der Sekundarstufe profitieren häufig von kontrastierenden Erklärungen; Studierende und Erwachsene benötigen fachwissenschaftliche Authentizität, berufliche Relevanz und flexible Zeiteinteilung. Dies sind Ausgangshypothesen. Ein erwachsener Anfänger kann massives Scaffolding benötigen, während ein fachlich versiertes Kind anspruchsvolle Herausforderungen braucht.

Prüfe lokale Fachterminologie, Zahlen- und Einheitenformate, Leserichtung, kulturelle Bezüge, Schulstrukturen und verfügbare Endgeräte. Gleiche Bildungsstandards nur mit konkreten, benannten Lehrplänen und Versionen ab. Schließe niemals aus der Sprache der Benutzeroberfläche auf einen nationalen Lehrplan. Berücksichtige die gemeinsame Gerätenutzung und den lehrkräftegeführten Unterricht. Die Simulation einer beruflichen Handlung zertifiziert noch keine reale Handlungskompetenz.

Biete Tastatur- und Ein-Klick-Alternativen zu Drag-and-Drop, barrierefreie Statustexte jenseits von reiner Farb- oder Tonkodierung, sichtbaren Tastaturfokus, reduzierbare Bewegung und anpassbare Zeitvorgaben. Gewährleiste, dass alternative Eingabemethoden das eigentliche Lernziel nicht untergraben. Barrierefreiheit und Zielgruppeneignung erfordern reale Praxistests mit den betroffenen Nutzern; die bloße Erwähnung von UDL oder WCAG beweist beides noch nicht.

### Lernspiele: Im angemessenen Umfang implementieren

Beginne bei einer kurzen Aktivität mit geprüften Inhalten, deterministischen Regeln und reinem Sitzungsstatus. Ergänze lokale Persistenz (z. B. LocalStorage) nur dann, wenn das Fortsetzen von Sitzungen einen echten Mehrwert bietet. Berücksichtige bei umfangreicheren Lernanwendungen Aufgabenversionen, die Unterscheidung zwischen unterstützten und selbstständigen Versuchen, geplante Wiederholungen, Datenexport/-löschung und Korrekturrechte für Lehrkräfte. Benutzerkonten, Server-Backends und Telemetrie bedürfen einer konkreten Begründung.

Werden Lernnachweise gespeichert, genügt oft ein minimalistischer Datensatz: `skill_id`, `item_version`, `mode`, `support_used`, `response`, `result` und `feedback_version`. Speichere nur zwingend erforderliche Felder; Rohantworten und Zeitstempel müssen das Gerät oft gar nicht verlassen. Verwalte Spielwährungen und visuelle Anpassungen strikt getrennt von fachlichen Lernnachweisen. Ein Netzwerkfehler oder ein versehentlicher Mehrfachklick darf weder Belohnungen unkontrolliert vervielfachen noch gespeicherte Beurteilungen verfälschen.

Definiere bei Laufzeit-KI zulässige Quellen, Bewertungsgrenzen, Ausfallsicherungen (Fallbacks) und Wege zur menschlichen Überprüfung. Teste plausible, aber falsche Erklärungen, gleichwertige korrekte Formulierungen und den Umgang mit Serverausfällen. Überprüfe den Lernerfolg erst nach dem Ausblenden der KI-Unterstützung. Forschung zu einzelnen Tutorensystemen belegt nicht, dass jeder Chatbot lernförderlich ist oder dass künstliche Wartezeiten vor Hilfestellungen nützen. Der Einsatz von KI bei der Softwareerstellung impliziert keineswegs KI-Aufrufe im fertigen Lernspiel.

Koordiniere Fachdisziplinen und Agenten anhand eines gemeinsamen Lernziels, konkreter Aufgabenbeispiele und einheitlicher Bewertungsregeln. Trenne fachliche Korrektheit, didaktisches Design, Spielbarkeit und technische Umsetzung. Löse Uneinigkeiten anhand konkreter fachlicher Quellen. Mehrere Personas in einem einzigen Prompt stellen keine unabhängige Validierung dar; setze unabhängige Agenten nur gezielt und bei Bedarf ein.

### Lernspiele: Drei verschiedene Ergebnisse validieren

1. Technisches Verhalten: Korrekte und alternative Antworten, Fehlvorstellungen, wiederholtes Raten, Lösungsanzeige, Wiederholungsversuche, Sitzungsfortsetzung und Verbindungsabbrüche. Stelle sicher, dass unterstützter Erfolg niemals stillschweigend als selbstständige Beherrschung verbucht wird.
2. Benutzerfreundlichkeit und Spielbarkeit: Beobachte reale Nutzende bei der ersten Aufgabe und bei der Korrektur nach einem Fehler. Notiere Verwirrung, Strategiewahl und ob ein selbstbestimmtes Beenden der Sitzung möglich ist. Ein kleiner Usability-Test deckt Hürden auf, beweist jedoch keinen Bevölkerungseffekt.
3. Lernerfolg: Prüfe den Transfer anhand einer neuen ungestützten Aufgabe, verzögerter Behaltensleistung und Transferaufgaben außerhalb der Benutzeroberfläche des Spiels. Ziehe für Wirksamkeitsaussagen eine adäquate Vergleichsgruppe mit vergleichbarem Inhalt und Zeitaufwand heran; berücksichtige Vorwissen, Drop-out-Raten und ungleiche Teilnahme. Berichte Unsicherheiten offen und setze Verweildauer oder Spielfreude niemals mit tatsächlichem Lernerfolg gleich.

Dokumentiere bei kleinen Projekten die didaktische Lernhypothese und einen machbaren Praxistest. Definiere bei folgenreichen Produkten Zielkriterien und Vergleichsstandards vor der Datenerhebung. Halte Spielmetriken und Lernmetriken strikt auseinander. Überarbeite oder entferne eine Spielmechanik, sobald sie unproduktive Abkürzungen provoziert, das Einholen von Hilfen stigmatisiert oder kognitive Belastung ohne didaktischen Mehrwert erzeugt.

### Lernspiele: Wissenschaftliche Evidenz und ihre Grenzen

- [Sailer & Homner, 2020](https://doi.org/10.1007/s10648-019-09498-w): Metaanalyse belegt durchschnittliche Vorteile von Gamification bei heterogenen Einzelbefunden; motivationale und verhaltensbezogene Effekte erwiesen sich unter strengeren methodischen Qualitätskriterien als weniger stabil. Dies ist kein Freibrief für beliebige Badges oder Bestenlisten.
- [Clark et al., 2016](https://doi.org/10.3102/0034654315582065): Vergleichsstudien zu Lernspielen betonen die entscheidende Rolle von Instruktionsdesign und Scaffolding. Das Medium allein bestimmt nicht den Lernerfolg.
- [Li et al., 2024](https://doi.org/10.1007/s11423-023-10337-7): Kleiner durchschnittlicher Zuwachs an intrinsischer Motivation über 35 Interventionen. Subjektiv wahrgenommene Kompetenz unterscheidet sich von gemessenem Fachwissen.
- [Habgood & Ainsworth, 2011](https://doi.org/10.1080/10508406.2010.508029): Zwei Studien zu einem mathematischen Lernspiel belegen die Vorteile der Integration von Lerninhalten direkt in die Spielmechanik (Intrinsic Integration). Die spezifische Stichprobe begründet keine universelle Erfolgsformel.
- [Agarwal et al., 2021](https://doi.org/10.1007/s10648-021-09595-9) und [Ruitenburg et al., 2026](https://doi.org/10.1007/s10648-026-10225-5): Unterrichtsevidenz für aktiven Abruf und kontextabhängige Wiederholungspläne. Letztere differenziert zwischen Abruf, Spacing und Interleaving; begrenzte Moderatorgruppen schränken die Generalisierbarkeit ein.
- [Wisniewski et al., 2020](https://doi.org/10.3389/fpsyg.2019.03087): Feedback-Wirkungen variieren stark; handlungsleitende Information ist entscheidend. [Sinha & Kapur, 2021](https://doi.org/10.3102/00346543211019105): Problemlösen vor der Instruktion kann unter definierten Bedingungen nützen, mit klaren Grenzen bezüglich Vorwissen und Umsetzung.
- [Almeida et al., 2023](https://doi.org/10.1016/j.infsof.2022.107142): Systematische Übersicht identifiziert unerwünschte Nebeneffekte und manipulative Muster von Gamification. Die bloße Anzahl negativer Berichte erlaubt jedoch keine Schätzung der tatsächlichen Schadenshäufigkeit.
- [MIT / Learning Games Network, 2015](https://education.mit.edu/wp-content/uploads/2018/10/BalancedDesignGuide2015.pdf): Balanced Design Framework zur Verknüpfung von Lernzielen, Spielhandlungen und Nachweisen. [George Fan, GDC 2012](https://media.gdcvault.com/gdc2012/slides/Design%20Track/Fan_George_How%20I%20Got.pdf): Praxiserfahrungen für spielerisches Onboarding. Beide liefern wertvolle Entwurfsmuster, jedoch keine kausalen Nachweise für Lernerfolge.
- [Bastani et al., 2025](https://doi.org/10.1073/pnas.2422633122) und [Kestin et al., 2025](https://doi.org/10.1038/s41598-025-97652-6): Experimente zeigen, warum Tutordesign und ungestützte Leistungsüberprüfungen entscheidend sind. Zielgruppen, Fachbereiche und Interventionen unterscheiden sich dabei erheblich.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) liefert Kriterien für Barrierefreiheit; [CAST UDL 3.0](https://udlguidelines.cast.org/) liefert ein pädagogisches Gestaltungsframework. Beide haben eine andere Funktion als experimentelle Lernstudien.

### Lernspiele: Spielerleben, Mechaniken und didaktischen Transfer verknüpfen

Nutze das MDA-Framework (Mechanics, Dynamics, Aesthetics) als Entwurfswerkzeug: Beschreibe das beabsichtigte Spielerleben (Aesthetics), das erwartete Spielverhalten (Dynamics) und die zugrundeliegenden Regeln (Mechanics). So erfordert forschendes Entdecken ein steuerbares Modell mit aussagekräftigen Beobachtungen; kreativer Ausdruck benötigt mehrere fachlich gültige Konstruktionswege. Presse nicht jedes Schulfach in dasselbe Spielgenre. Die Selbstbestimmungstheorie (SDT) sensibilisiert für Autonomie, Kompetenzerleben und soziale Eingebundenheit; weder ein MDA-Diagramm noch ein Octalysis-Etikett beweisen per se didaktische Wirksamkeit.

Definiere bei offenen Konstruktionsaufgaben Rahmenbedingungen und überprüfbare Erfolgskriterien, ohne eine einzige Musterlösung des Autors zu erzwingen. Ermögliche den Vergleich eigener valider Entwürfe anhand konkurrierender Zielkriterien wie Ressourceneinsatz und Präzision. Ein Community-Histogramm benötigt echte, repräsentative Daten und eine freiwillige Freigabe; erfinde keine Vergleichsverteilung. Optimierungsrunden müssen nicht mit Extrawährungen belohnt werden.

Verknüpfe Darstellungen im Spiel stets mit formaler Fachnotation oder realen Entscheidungen und überprüfe den Lernerfolg anschließend an einer neuen Aufgabe außerhalb des Spielkontexts. Zwinge nicht jedem Lernenden geteilte Bildschirme oder starre Dreistufenmodelle auf. Spielgefühl (Game Feel) und Sound sollten bedeutsame Rückmeldungen geben, ohne das Nachdenken zu stören. Halte Streaks und Belohnungen optional und frei von Bestrafungslogiken; Pausen dürfen weder Lernnachweise noch den Zugang zu Hilfen löschen. Die Veröffentlichung des eigenen Fortschritts erfordert stets eine bewusste, freiwillige Entscheidung des Lernenden.

Das [MDA-Modell von Hunicke, LeBlanc & Zubek](https://www.cs.northwestern.edu/~hunicke/MDA.pdf) ist ein theoretisches Entwurfsframework. Die zitierten Lernspielstudien basieren auf unterschiedlichen Zielgruppen und Erhebungsmethoden; setze Engagement- oder Verweildauer-Kennzahlen aus Produkten niemals mit echtem Lernzuwachs gleich.

## Reference: design-dialogue

Quellabschnitt: Entwurfsdialog bei der didaktischen Konzeption


Nutze diesen Leitfaden bei der ersten wesentlichen didaktischen Gestaltungsentscheidung sowie dann, wenn neue Erkenntnisse oder veränderte Anforderungen eine Entscheidung wiedereröffnen. Diese Regeln beschreiben einen praktischen Arbeitsablauf für den Entwurf, keine experimentellen Hypothesen über Lernprozesse.

### Entwurfsdialog: Zielgruppe und Lernbedingungen erfassen

Lebensalter, Bildungsrolle und thematische Vorerfahrung sind unterschiedliche Merkmale. „Kind“ beschreibt ein Alter; „Schüler“ und „Studierender“ bezeichnen Bildungsrollen, deren Bedeutungen sich je nach Schulsystem unterscheiden. Kategorien überschneiden sich. Verwende in der didaktischen Konzeption neutrale Begriffe wie „Lernende“ oder „Teilnehmende“ und im fertigen Produkt den für den Kontext passenden Tonfall. Schulbezogene Beispiele schränken den Skill keineswegs auf Kinder ein. Direkte Arbeitsanweisungen lauten schlicht: „Probiere aus“, „Erkläre“ oder „Vergleiche“.

Erstelle vor der Methodenauswahl aus dem bekannten Kontext ein kompaktes Zielgruppenprofil: Altersgruppe und Setting; thematisches Vorwissen; Lesekompetenz und Sprache; Grad der Selbstständigkeit und verfügbare Unterstützung; Lernziel und Konsequenzen der Leistungsbeurteilung; Endgeräte und Anforderungen an die Barrierefreiheit. Dies sind didaktische Entwurfsdaten, kein Pflichtfragebogen zur Person. Verlange weder Geburtsdatum noch Diagnosen oder lückenlose Schulbiografien. Kennzeichne offene Punkte als Annahmen; die bloße Bezeichnung „Schüler“ klärt diese Faktoren nicht.

| Kontext und treffender Begriff | Was geklärt werden sollte | Mögliche Differenzierung bei Bedarf |
| --- | --- | --- |
| Vorschulkind (Kindergarten / Vorschule) | Lesefähigkeit, Bedienung, Begleitung durch Erwachsene und Zweck der Bildschirmzeit | Konkrete, kurze Audio-/Bildanweisungen, gemeinsames Spiel und Aktivitäten außerhalb des Bildschirms; kein eigenständiges Lesen voraussetzen |
| Grundschulkind (Primarstufe) | Begriffsbildung, Notation, Aufgabenverständnis und Endgeräte | Konkrete Anschauung mit abstrakten Konzepten verknüpfen, Bedienung vormachen und Hilfestellungen anbieten |
| Lernende der Sekundarstufe I | Fachliche Voraussetzungen, Leistungsheterogenität und Gruppenarbeit | Lösungsstrategien vergleichen, Begründungen einfordern und Hilfen auf ein gemeinsames Ziel hin dosieren |
| Lernende der Sekundarstufe II oder beruflichen Bildung | Fachdisziplin oder Berufsfeld, Vorerfahrung und Prüfungsbezug | Authentische Fachprobleme, Argumentationen oder Berufsszenarien; Simulationen ersetzen keine praktischen Prüfungen |
| Studierende an Hochschulen | Fachwissenschaftliche Voraussetzungen und Vorkenntnisse | Authentische Aufgaben, Belegführung und multiple Lösungswege; Beispiele bei neuen Themen zugänglich halten |
| Erwachsene Lernende, Selbstlernende oder Beschäftigte | Persönliches Lernziel, Praxiserfahrung, Zeitbudget und realer Anwendungsbezug | Praxisrelevante Situationen, Überspringen von Bekanntem, flexibles Lerntempo und Wiederaufnahmemöglichkeit |
| Ältere Erwachsene (Seniorinnen und Senioren) | Individuelle Vorerfahrung, Sprache, Bedienung und Zugänglichkeitsbedürfnisse | Textgröße, Reaktionszeiten und Steuerung bei Bedarf anpassen; höheres Alter bedeutet keineswegs fehlende Digitalkompetenz |
| Gemischte Lerngruppen | Gemeinsame Kernbedürfnisse und Bereiche mit Differenzierungsbedarf | Gemeinsames Kernziel, optionale Vertiefungen, gestufte Einstiegsaufgaben und individuelle Lernnachweise |

Dies sind didaktische Entwurfsoptionen, keine Entwicklungsdiagnosen oder starre Zuordnungen von Methoden zu Altersstufen. Schulformen und Jahrgangsstufen unterscheiden sich international. Ein Kind kann im Fachgebiet weit fortgeschritten sein, ein Erwachsener absoluter Anfänger. Sprachförderung, Barrierefreiheit und Tempounterschiede können jede Zielgruppe betreffen. Weise niemals feste visuelle, auditive oder sonstige „Lerntypen“ zu.

Unterscheide klar: Wer lernt, wer bedient das Programm und wer sieht die Ergebnisse? Eine Lehrkraft kann eine gemeinsame Beamer-Präsentation steuern, ein Elternteil ein Kind begleiten, und der Auftraggeber der Software ist oft weder das eine noch das andere. Eine kindliche Zielgruppe legt nicht automatisch fest, wer Auswertungen einsehen darf. Definiere Rollen und Rechte für das reale Einsatzszenario.

Frage bei fehlenden Angaben nur nach, wenn die Antwort das didaktische Design wesentlich verändert: „Ist diese Aktivität für Grundschulkinder, Jugendliche der Sekundarstufe oder erwachsene Einsteiger gedacht? Welches Vorwissen bringen sie mit?“ Passe die Optionen an; wiederhole keine bereits bekannten Informationen. Kläre vage Angaben nur dann, wenn das konkrete Setting das Ergebnis beeinflusst.

Begründe stets, wer hier von einer vorgeschlagenen Methode profitiert und warum: „Für diese erwachsenen Einsteiger empfehle ich ein ausgearbeitetes Lösungsbeispiel aus ihrer Arbeitswelt und anschließend den schrittweisen Abbau der Hilfen bei selbstständigen Versuchen.“ Erfahrene Jugendliche profitieren dagegen möglicherweise eher von einer offenen Problemstellung. Eine Änderung der Zielgruppe öffnet betroffene Aspekte wie Sprache, Inhalt, Hilfen, Bewertung und Steuerung erneut, jedoch nicht automatisch das gesamte Projekt.

### Entwurfsdialog: Angebote am Punkt des Bedarfs unterbreiten

Entnimm bekannte Angaben zu Zielgruppe, Vorwissen, Lernziel, Rechtsraum, Geräten, Zeitbudget und Rahmenbedingungen direkt dem Projektkontext. Frage nur nach fehlenden Fakten, wenn sie die Entscheidung verändern. Standard ist ein partnerschaftlich geführter Dialog. Der Ersteller kann einzelne Entscheidungen oder nachfolgende Routineentscheidungen delegieren und die Steuerung später wieder übernehmen.

| Auslöser | Relevante didaktische Optionen zur Erläuterung |
| --- | --- |
| Lernziel und Einstiegsaktivität | Ausgearbeitetes Lösungsbeispiel mit Fading, geleitete Entdeckung, aktiver Abruf, Konstruktionsaufgabe oder authentisches Projekt |
| Motivation und Partizipation | Persönlicher Lernfortschritt, bedeutsame Wahlmöglichkeiten, kooperative Rollen, optionale Spielmechaniken |
| Fehlerkultur und Hilfesystem | Gestufte Hinweise, kontrastierende Beispiele, direkte Erklärung mit erneutem Anwendungsversuch |
| Leistungsbeurteilung | Formatives Feedback, kriterienorientiertes Bewertungsraster, unabhängige Überprüfung, Portfolio oder gestützte Peer-Beurteilung |
| Fortführung und Kontinuität | Nur Sitzungsstatus, lokales Fortsetzen, zeitlich versetztes Wiederholen (Spaced Review) oder kalibrierte Aufgabenschwierigkeit |
| Erkenntnisse aus Prototypentests | Irreführende Repräsentationen korrigieren, Hilfen abbauen, Transferaufgaben ergänzen oder spielerische Fehlanreize entfernen |

Dies sind didaktische Gelegenheiten, keine Pflichtstopps. Führe zusammenhängende Entscheidungen bei kleinen Projekten gebündelt durch. Präsentiere nur tragfähige Optionen mit kurzer Beschreibung, konkretem Bezug zum Projekt und den damit verbundenen Konsequenzen wie Kosten, Datenbedarf oder Einschränkungen. Empfehle eine Option und stelle eine präzise Frage. Ermögliche einfache Vorabversionen oder das Zurückstellen von Entscheidungen; verlange vom Ersteller kein Fachchinesisch. Zusätzliche Methoden stehen auf Nachfrage bereit.

### Entwurfsdialog: Entscheidungen dokumentieren

Nutze bei kleinen Aufgaben den Gesprächsverlauf; greife bei größeren Vorhaben auf die bestehende Projektdokumentation zurück. Halte Lernziel, Rahmenbedingungen, Methoden-ID, didaktische Begründung, Status, verworfene Alternativen und offene Fragen fest. Empfohlene Statuswerte: `offered` (vorgeschlagen), `selected` (ausgewählt), `implemented` (implementiert), `verified` (verifiziert), `deferred` (zurückgestellt), `declined` (abgelehnt). Führe diese Dokumentation getrennt von Lernerdaten. Eine neue Anforderung öffnet nur direkt betroffene Entscheidungen erneut; begründe dies nachvollziehbar. Schweigen gilt niemals als Zustimmung. Setze unabhängige Arbeiten fort, während eine wesentliche Entscheidung offen ist.

### Entwurfsdialog: Von der Auswahl zum fertigen Produkt

Nutze die Bausteine der jeweiligen Methodenkarte: Lernendenhandlung, Lernnachweis, Unterstützungsmaßnahmen und Überprüfung. Konstruiere eine in sich geschlossene Lernsequenz; weise auf didaktisch inkompatible Kombinationen hin. Ein ausgearbeitetes Lösungsbeispiel kann einem späteren Abruf vorangehen; produktives Scheitern benötigt eine anschließende Konsolidierungsphase. Keiner dieser Ansätze bedeutet, dass auf jedem Bildschirm ein Test stattfinden muss.

Beispiel für eine Offline-Aktivität zum Bruchrechnen: „Ich empfehle, Bruchteile zusammenzulegen und den passenden Bruch anzuzeigen, da das Ziel das Verständnis der Gleichwertigkeit ist. Ein Zahlenstrahl betont stattdessen die gleiche Position; das Vervollständigen eines ausgearbeiteten Beispiels bietet anfangs mehr Unterstützung. Welcher Ansatz soll die Hauptaktivität sein?“ Biete später eine neue Aufgabe ohne visuelle Bruchteile oder eine Fehleranalyse-Aufgabe an, um den Transfer zu prüfen. Wiederhole nicht das Eingangsgespräch.

Der Ersteller beauftragt eine funktionierende Anwendung. Verwandle diesen Dialog nicht in erzwungenen Nachhilfeunterricht, Programmier-Hausaufgaben oder endlose TODO-Listen. Zeige bei der Übergabe auf, wo jede ausgewählte Methode wirkt, was überprüft wurde und welche Annahmen offenbleiben. Die automatische Erkennung des Skills hängt von der Plattform ab; teste die Auffindbarkeit getrennt vom Ausführungsverhalten nach dem Aufruf.

## Reference: cognitive-ux

Quellabschnitt: Kognitive Benutzeroberfläche und Repräsentationen


Konsultiere diese Referenz beim Entwurf von Diagrammen, Multimedia-Elementen, Instruktionen, der Platzierung von Feedback oder Benutzeroberflächen, die von der eigentlichen Lernaufgabe ablenken könnten. Richte die Gestaltung an den Zielgruppen und Endgeräten aus, nicht an einem starren visuellen Stil.

### Kognitive Benutzeroberfläche: Aufmerksamkeit auf die didaktische Kernentscheidung lenken

Entferne irrelevante, konkurrierende Animationen und Töne während anspruchsvoller kognitiver Prozesse (Extraneous Cognitive Load minimieren); behalte nützlichen Kontext und Bedienelemente bei. Platziere zusammenhängende Beschriftungen und Erklärungen in unmittelbarer räumlicher Nähe zum Bezugsobjekt (Prinzip der räumlichen Kontiguität), ohne das Objekt zu verdeckten. Nutze auf kleinen Bildschirmen verknüpfte Hervorhebungen, barrierefreie Beschreibungen oder sequentielle Ansichten, wenn eine nebeneinanderliegende Darstellung unpraktisch ist. Farbe allein darf niemals der einzige Informationsträger sein.

Teile komplexe Abläufe in lernendengesteuerte Schritte ein (Segmentierungsprinzip). Führe unbekannte Bedienelemente und Fachbegriffe ein, bevor sie kombiniert angewendet werden. Erhalte für fortgeschrittene Lernende eine direkte Abkürzung und jederzeit einen einfachen Rückweg zu Hilfestellungen. Animationen sollten Veränderungen oder Abläufe verdeutlichen; stelle eine Option für reduzierte Bewegung (prefers-reduced-motion) sowie einen gleichwertigen, verständlichen statischen Zustand bereit.

### Kognitive Benutzeroberfläche: Repräsentationen verknüpfen und Transfer prüfen

Wenn konkrete Anschauungsobjekte (Manipulativa) ein abstraktes Konzept stützen, zeige auf, wie dieselbe Beziehung in Objekten, grafischen Diagrammen und formaler Fachnotation erscheint (Darstellungsvernetzung). Erläutere die Entsprechung und fordere anschließend eine neue Anwendung mit geringerer visueller Unterstützung ein (Fading). Eine geteilte Bildschirmansicht (Split-View) ist eine mögliche Umsetzung, aber kein Dogma. Stelle gleichwertige Tastatur- und klickbasierte Alternativen zu Drag-and-Drop bereit. Verifiziere, dass Lernende Aufgaben nicht rein durch Zuordnen von Farben oder Bildschirmpositionen oberflächlich lösen können.

Beispiel: Der Lernende manipuliert Mengendarstellungen, sieht die entsprechende mathematische Gleichung und erklärt, warum die Gleichheit bestehen bleibt; später löst er eine neue Gleichung rein symbolisch ohne Anschauungsobjekt. Fortgeschrittene Lernende können direkt mit der Notation beginnen. Die Anschauungsebene kann bei Bedarf jederzeit wieder eingeblendet werden. Bei nicht-mathematischen Aufgaben bedeutet Transfer beispielsweise, eine neue Quelle zu bewerten oder ein Verfahren in einem veränderten Szenario anzuwenden.

### Kognitive Benutzeroberfläche: Zugänglichkeit und aussagekräftige Lernnachweise wahren

Vermeide unnötige simultane Informationskanäle, erhalte jedoch Untertitel, Transkripte, Wiederholungsfunktionen, Sprachunterstützung und Screenreader-Zugänglichkeit aufrecht. Das Redundanzprinzip verbietet keineswegs Text neben Audio, wenn dies dem Textverständnis oder der Barrierefreiheit dient. Verstecke essenzielle Anweisungen nicht in reinen Hover-Tooltips. Wenn Hörverstehen oder Zeitdruck die explizit geprüfte Kompetenz darstellen, lege die Bedingungen offen und definiere Nachteilsausgleiche transparent.

An konzeptionellen Meilensteinen kann eine optionale Selbsteinschätzung der Zuversicht (Confidence Judgment) helfen, Selbstwahrnehmung und tatsächliche Leistung abzugleichen. Behandle Zuversicht nicht als Kompetenznachweis und fordere sie nicht nach jeder Aktion ein. Feedback sollte den didaktisch relevanten Kontrast erklären und eine Gelegenheit bieten, das Gelernte sofort anzuwenden; verunsichere Lernende bei korrekten Lösungen nicht künstlich.

Überprüfe Lesbarkeit von Beschriftungen, Fokus-Reihenfolge, Zoomfunktion, schmale Bildschirmlayouts, reduzierte Bewegung und den vollständigen Pfad für Hilfe und Wiederholungsversuche. Begutachte die reale Lernhandlung, nicht nur das Aussehen der Komponenten. Lege nicht durchgeführte Prüfungen transparent dar.

### Kognitive Benutzeroberfläche: Quellen und Grenzen

[Waxman & Goldie, 2023](https://media.repository.chds.hsph.harvard.edu/static/filer_public/ca/62/ca625803-3d73-4855-b3e1-765870ce3772/2023_jwaxman_monograph_cogtheory_multimed.pdf) liefert Kriterien für Gestaltungsentscheidungen, keine universellen Verbote für Layouts. [Matlen & Devlin, 2020](https://web.stanford.edu/~kdevlin/Papers/Matlen-Devlin_CHI2020.pdf) beschreibt ein transferorientiertes Konzept, belegt aber nicht jedes Split-Screen-Design pauschal. [W3C Captions](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html) erläutert Anforderungen an Barrierefreiheit. Prüfe stets die aktuellen normativen Anforderungen für die Zielplattform.

## Reference: adaptive-practice

Quellabschnitt: Adaptives Üben und kontinuierliches Lernen


Konsultiere diese Referenz, wenn die Anwendung wiederholte Lerneinheiten, Zeitpläne (Spaced Repetition) oder eine adaptive Aufgabenauswahl nach Schwierigkeitsgrad erfordert. Unterscheide klar: Wann wird wiederholt, welche Aufgabe wird vorgelegt und wie viel Hilfestellung wird angeboten? Diese drei Aspekte müssen nicht über dasselbe Modell gesteuert werden.

| Bedarf | Einfache Umsetzung | Optionale Erweiterung und Voraussetzungen |
| --- | --- | --- |
| Einzelne Aktivität | Geprüfte Aufgaben, explizite Abfolge, Hilfesystem und Sitzungsstatus | In der Regel kein persistentes Lernendenmodell erforderlich |
| Wiederholen über Tage | Fester Wiederholungsplan und lokaler Verlauf | FSRS bei stabilen Lernobjekten und interpretierbaren Wiederholungsereignissen |
| Schwierigkeit wählen | Geprüfte Aufgabenniveaus und transparente Verzweigungslogik | Elo-Algorithmus bei geeigneten Antwortdaten, Unsicherheitsmodellierung und Kalibrierung |
| Kompetenzabhängigkeiten | Kompetenzraster mit unabhängigen Nachweisen | BKT oder IRT nur mit fundiertem Modell, ausreichenden Daten und Validierung |
| Langzeit-Lernplan | Lernziel, Zeitbudget, aktuelle Phase und nächste Aufgabe | Anpassbare Meilensteine, offene Transferfragen und Wiederholungstermine |

Erkläre die didaktische Funktion vor der algorithmischen Umsetzung. Bewahre den bestehenden Software-Stack; installiere keinen Scheduler, Backend-Dienst oder Kontensystem nur deshalb, weil sie hier aufgeführt sind. Einfache Heuristiken bleiben legitim, wenn ihre Grenzen transparent sind. HLR ist ein weiteres trainiertes Wiederholungsmodell für passende Datensätze, jedoch keine standardmäßige Implementierungspflicht.

### Adaptives Üben: Voraussetzungen vor der Adaption

Definiere stabile IDs für Aufgaben und Kompetenzen, Inhaltsversionen, Antwortinterpretationen und Bedingungen für Hilfestellungen. Trenne erratene, unterstützte, aufgelöste und selbstständig gelöste Antworten sauber voneinander. Halte dich an die Bewertungssemantik der gewählten Bibliothek; werte eine unterstützte Antwort nicht stillschweigend als eigenständige Gedächtnisleistung. Halte spielerische Währungen strikt außerhalb des didaktischen Lernmodells. Nutze minimale Daten und Zeitstempel nur dort, wo sie für die Terminierung zwingend nötig sind.

Definiere das Verhalten bei Kaltstart und eine verlässliche Rückfallebene, falls der Verlauf fehlt, fehlerhaft oder veraltet ist. Prüfe Annahmen anhand repräsentativer Daten, einschließlich Sprach- und Zugangsbedingungen. Ermögliche Korrekturen durch Lehrkräfte sowie den Zugriff der Lernenden auf Hilfen. Vorhergesagte Erfolgswahrscheinlichkeiten sind mit Unsicherheit behaftet; weder eine pauschale Erfolgsquote von 80–90 % noch zwei richtige Antworten messen verlässlich die Zone der nächsten Entwicklung (ZPD) oder beweisen Meisterschaft. Eine angestrebte Behaltensquote (Target Retention) ist ein Abwägungskompromiss bezüglich des Lernaufwands, keine garantierte Lernausbeute.

Verwende bei der Wahl eines Algorithmus eine gepflegte, versionsgeprüfte Implementierung. Teste Updates, Zeitzonen und Tagesgrenzen, doppelte Absendungen, Inhaltsänderungen, Export/Wiederaufnahme und ungültige Eingaben. Vergleiche die algorithmische Erweiterung mit einer einfachen Baseline; Vorhersagegenauigkeit, Engagement und tatsächlicher Lernerfolg sind getrennte Kriterien. Schließe aus Reaktionszeiten niemals auf Beeinträchtigungen oder Persönlichkeitsmerkmale.

### Adaptives Üben: Phasen abschließen oder wiederaufnehmen

Dokumentiere Ergebnis, Unterstützungsbedingungen, offene Fragen und den nächsten erreichbaren Schritt. Das Abschließen einer Phase ist nicht gleichbedeutend mit nachgewiesener Kompetenz. Das Erstellen einer neuen Phase schließt die vorherige nicht automatisch ab. Zusammenfassungen halten notwendige Nachweis-Zeiger und Unsicherheiten fest, statt vollständige Verlaufsprotokolle zu archivieren. Überprüfe bei einer Rückkehr veraltete Annahmen durch eine angemessene diagnostische Aufgabe; Unterbrechungen dürfen den bisherigen Fortschritt nicht löschen.

### Adaptives Üben: Quellen

[Anki FSRS-Dokumentation](https://docs.ankiweb.net/manual/deck-options), [Pelánek zu pädagogischem Elo](https://www.fi.muni.cz/~xpelanek/publications/CAE-elo.pdf) und [Settles & Meeder zu HLR](https://research.duolingo.com/papers/settles.acl16.pdf). Diese Quellen beschreiben spezifische Modelle und Konfigurationen; sie belegen nicht die Wirksamkeit einer neu erstellten Anwendung. Prüfe bei der Integration von Bibliotheken stets deren aktuelle Dokumentation.

## Lizenzhinweis

```text
MIT License

Copyright (c) 2026 Luděk Sušický

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
