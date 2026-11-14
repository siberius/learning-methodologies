# Modelle, Denkaufwand, Ausführungsgeschwindigkeit und Host-Anpassung

Konsultiere diese Referenz, wenn ein Modell empfohlen, eine Stufe für Denkaufwand (Reasoning Effort) oder Ausführungsgeschwindigkeit gewählt oder das Ladeverhalten der Host-Umgebung angepasst werden soll. Die didaktischen Kernanweisungen bleiben über alle Modellanbieter hinweg identisch.

## Was diese Referenz nicht beansprucht

Die Empfehlungen sind praxisorientierte Ausgangskonfigurationen für diesen Arbeitsablauf, kein empirischer Benchmark und keine Rangliste. Sie belegen nicht, dass eine bestimmte Modellfamilie per se didaktisch überlegen ist, und prognostizieren keine exakten Latenzzeiten. Modellbezeichnungen, verfügbare Parameter, Tarife und Preise ändern sich fortlaufend. Überprüfe vor der Verwendung eines Modells die tatsächliche Modellliste des Nutzers und die aktuelle offizielle Dokumentation des Anbieters. Ein Name in der Benutzeroberfläche entspricht nicht zwingend der exakten API-Modell-ID. Deklariere eine Konfiguration erst dann als verifiziert, wenn sie an repräsentativen didaktischen Aufgaben erfolgreich getestet wurde.

Dokumentationsstand geprüft: 04.11.2026.

## Nach Aufgabe wählen vor der Wahl des Modellnamens

Nutze ein kleineres Modell für eng umrissene Textkorrekturen mit eindeutigen Vorgaben, ein mittelgroßes Modell für Standardkonzeption und Implementierung und ein leistungsstärkeres Spitzenmodell bei widersprüchlichen Quellenbelegen, komplexen Simulationen oder folgenreichen Begutachtungen. Dies sind funktionale Aufgabenkategorien, keine garantierten Modellfähigkeiten. Behalte die bestehende Modellauswahl des Nutzers bei, wenn sie die didaktischen Anforderungen erfüllt.

Die folgende Tabelle enthält **ungetestete Startempfehlungen für diesen Skill**, abgeleitet aus den Herstellerdokumentationen.

## Eskalations- und Abbruchregeln

Starte bei einer klar umrissenen Aufgabe mit dem standardmäßigen Denkaufwand des Systems oder einer zuvor erfolgreichen Konfiguration. Ziehe bei widersprüchlichen Quellen oder komplexen Fachmodellen von Beginn an ein höheres Denkniveau in Betracht. Wenn die Modellausgabe eine explizite Vorgabe ignoriert, ihrer eigenen Punktevergabe widerspricht, fachliche Rechenprüfungen verfehlt oder wiederholt unbrauchbare Aufgabenstellungen erzeugt, prüfe zuerst, ob die relevanten Eingabedateien und Referenzen für das Modell tatsächlich zugänglich waren. Korrigiere fehlende Eingaben oder uneindeutige Kriterien, bevor das Modell gewechselt wird.

Scheitert nach einer gezielten Fehlerkorrektur derselbe wesentliche Prüfpunkt erneut, empfehle eine höhere Stufe des Denkaufwands (Reasoning Effort) und evaluiere dieses Kriterium neu. Bleibt der Fehler bestehen, empfehle ein stärkeres verfügbares Modell oder ein unabhängiges didaktisches Review entsprechend der Tragweite. Wiederhole Versuche nicht endlos und überschreite nicht das vereinbarte Budget. Fehlende Fachquellen, nicht verfügbare Softwarewerkzeuge oder Serverausfälle erfordern die Behebung der Ursache oder die transparente Benennung der Grenze; zusätzlicher Denkaufwand kann fehlende empirische Evidenz nicht herbeizaubern. Berichte ungelöste Probleme offen. Ändere Konfigurationen nur über autorisierte Bedienelemente des Hosts.

Reduziere den Denkaufwand oder wechsle zu einem kleineren Modell erst, nachdem alle wesentlichen didaktischen Prüfungen erfolgreich bestanden wurden; dokumentiere den Abwägungskompromiss. Behandle die Ausführungsgeschwindigkeit getrennt: Standard-Serving ist der Ausgangspunkt; kostenpflichtige Beschleunigungstarife (Fast Tiers) bedürfen einer sachlichen Begründung und Autorisierung.

## Empfehlungen aktuell halten

Prüfe die namentlichen Empfehlungen erneut, wenn sich Modell- oder Host-Versionen ändern, ein Konfigurationsparameter entfällt, der Anbieter die Verfügbarkeit ändert oder das dokumentierte Verhalten von realen Beobachtungen abweicht. Kennzeichne eine Paarung bis zur Verifikation als ungeprüft und nutze Aufgabenkategorien sowie die Standardwerte des jeweiligen Hosts. Erfinde keine Äquivalenzparameter für unbekannte Modelle. Ergänze anbieterspezifische didaktische Workarounds erst, wenn ein reproduzierbarer Fehler deren Notwendigkeit belegt; dokumentiere die betroffene Version und entferne Workarounds, sobald sie hinfällig werden.

## Aufgabe und Steuerungsoptionen abstimmen

| Aufgabe | OpenAI Ausgangspunkt | Claude Ausgangspunkt | Gemini Ausgangspunkt |
|---|---|---|---|
| Kleine, klar spezifizierte Text- und Inhaltsanpassungen, Review strukturierter Aufgaben | GPT-6 Luna, High; Denkaufwand erst reduzieren, wenn Prüfungen stabil halten | Haiku 5.5, Medium | Gemini 3.5 Flash-Lite, Low wo unterstützt |
| Didaktische Konzeption und Implementierung einer abgegrenzten Lernaktivität | GPT-6.1 Sol, Standard-Denkaufwand oder Medium | Sonnet 5.5, Medium für klar umrissene agentische Aufgaben | Gemini 3.8 Flash, Medium |
| Schwieriges didaktisches Audit, widersprüchliche Quellen, komplexe Simulation oder Architektur | GPT-6 Astra, Light/Low oder Medium; bei Bedarf erhöhen | Opus 5.5, Medium, dann High falls erforderlich | Gemini 4 Argon, Medium, dann High falls erforderlich |

Diese Zuordnungen sind Empfehlungen des Autors, abgeleitet aus den Herstellerleitfäden. Ist ein ausgewähltes Modell nicht verfügbar, schlage eine erreichbare Alternative vor und lege den Wechsel offen; verändere Nutzerauswahlen nicht eigenmächtig ohne Autorisierung. Ein bestehender Workflow auf Gemini 3.1 Pro kann beispielsweise dieses Modell und dessen Thinking-Stufen beibehalten. Miss die Latenz für repräsentative Aufgaben in der tatsächlichen Zielumgebung.

Unterscheide stets drei Ebenen: das Sprachmodell, die Tiefe des Denkaufwands (Reasoning Effort) und eventuelle priorisierte Ausführungsgeschwindigkeiten (Fast Mode). Ein geringerer Denkaufwand reduziert Rechenschritte; die Fast-Option eines Anbieters ist ein separater Infrastrukturparameter und kann zusätzliche Kosten verursachen. Die Modellbezeichnung Flash steht für eine Modellfamilie, nicht für einen allgemeinen Turboschalter. Gleiche Begriffe wie Low, Medium und High versprechen zwischen unterschiedlichen Produkten keineswegs identische Denktiefe oder Antwortzeiten.

Starte mit Standard-Ausführungsgeschwindigkeit. Empfehle einen kostenpflichtigen Fast-Modus nur, wenn Wartezeiten kritisch sind und der Zugriffstarif dies rechtfertigt. Aktiviere keine Zusatzoptionen und buche keine Kapazitäten ohne ausdrückliche Freigabe. Streaming verbessert die visuelle Rückmeldung des Fortschritts; es ist kein Beleg für frühere Fertigstellung oder höhere inhaltliche Qualität. Beurteile die Gesamtdauer immer einschließlich didaktischem Review, Werkzeugaufrufen und Korrekturschleifen.

## OpenAI und Codex

Verwende das native Paket dort, wo die Entwicklungsumgebung Skills unterstützt und Referenzdateien einlesen kann. In Codex kann der Skill explizit über `$learning-methodologies` oder `$vzdelavaci-metodiky` (bzw. `$lernmethoden`) aufgerufen werden. Gehe in einfachen Chat-Schnittstellen nicht von einer automatischen Erkennung im Dateisystem aus; stelle dort stattdessen die zusammenhängende eigenständige Markdown-Datei als Kontext bereit.

Der aktuelle Leitfaden empfiehlt Sol für umfangreiche Entwicklungsarbeiten, Luna für fokussierte Routineaufgaben und Astra für besonders anspruchsvolle didaktische Workflows; Luna High und Astra Light/Low sind dokumentierte Startwerte. In Codex ist Fast eine Infrastrukturwahl für Antwortzeiten, unabhängig vom didaktischen Denkaufwand. Verfügbarkeit und Kontingente hängen vom Modell, Account und Client ab. Prüfe unterstützte Parameter vor der Konfiguration; ein UI-Label ist nicht automatisch eine API-Modell-ID.

Definiere ein konkretes Arbeitsergebnis, den Projektumfang, relevante Dateien und beobachtbare Akzeptanzkriterien. Verlange präzise didaktische Entscheidungen und Nachweise, nicht die Offenlegung interner Gedankengänge (CoT). Nutze die Werkzeuge und Berechtigungen des Hosts; leite aus dem bloßen Modellnamen keine Shell- oder Browserberechtigungen ab.

Quellen: [Modelle](https://learn.chatgpt.com/docs/models), [Geschwindigkeit](https://learn.chatgpt.com/docs/agent-configuration/speed), [Skills](https://developers.openai.com/plugins/concepts/skills).

## Claude und Claude Code

Claude Code unterstützt `SKILL.md`-Pakete und begleitende Referenzdateien. Nach der Erkennung kann der Skill explizit über `/learning-methodologies`, `/vzdelavaci-metodiky` oder `/lernmethoden` aufgerufen werden. Prüfe in anderen Claude-Umgebungen den Lademechanismus oder binde die eigenständige Distribution ein. Füge dem gemeinsamen Frontmatter keine Claude-spezifischen Hooks, Shell-Substituierungen oder Modellüberschreibungen hinzu.

Für agentische Aufgaben mit Sonnet 5.5 empfiehlt die Dokumentation Medium für gut definierte Aufgaben und höhere Werte für komplexe Probleme. Opus 5.5 nutzt standardmäßig Medium; ältere Modelle und Schnittstellen weichen ab. Der API-Parameter für Effort und der interaktive Denkmodus sind unterschiedliche Konzepte. Nicht alle Modellgenerationen unterstützen dieselben Kombinationen. Bevorzuge integrierte Host-Einstellungen, statt API-Parameter manuell in Chat-Prompts zu kopieren. Claudes Fast-Modus ist eine separate, modellabhängige Funktion mit abweichender Bepreisung.

Grenze Aufgabe, didaktische Materialien und das angestrebte Ergebnis präzise ein. Mache deutlich, wo der Agent eigenständig entscheiden darf und wo didaktische Belege zwingend sind. Ein gut gewähltes Aufgabenbeispiel klärt Unklarheiten oft besser als die Wiederholung des gesamten Skills. Diese modulare Struktur sichert Portabilität und stellt keine Behauptung über Claude-spezifische kognitive Merkmale dar.

Quellen: [Skills](https://code.claude.com/docs/en/skills), [Modelle](https://platform.claude.com/docs/en/models/overview), [Effort](https://platform.claude.com/docs/en/build-with-claude/effort), [Fast-Modus](https://platform.claude.com/docs/en/build-with-claude/fast-mode).

## Gemini und Gemini CLI

Gemini CLI erkennt native Skills in den dafür vorgesehenen Verzeichnissen, einschließlich des `.agents/skills`-Pfads. Überprüfe die Erkennung mit `/skills list` und aktualisiere bei Bedarf mit `/skills reload`. Workspace-Vertrauensstellungen und Berechtigungsfreigaben unterliegen dem Host; umgehe diese Sicherheitsmechanismen nicht. Binde in Google AI Studio oder allgemeinen Web-Chats die eigenständige Datei ein, wenn kein natives Skill-Laden unterstützt wird.

Die geprüfte Dokumentation führt für Gemini 4 Argon und Gemini 3.8 Flash die Stufen Low, Medium und High auf. Andere Gemini-Versionen besitzen abweichende Standardwerte und Stufen. Verwende ausschließlich Parameter, die vom realen Modell und API-Client unterstützt werden; übersetze Denkaufwandsparameter von OpenAI oder Claude nicht blind 1:1. Eine Vorschau-Bezeichnung (Preview) und ein stabiler Release-Name sind nicht austauschbar.

Für `gemini-3.1-pro-preview` verzeichnet die API-Tabelle Low, Medium und High, mit High als Standardwert. Für diesen Endpunkt empfiehlt der Autor Medium für Standardaufgaben und High für schwierige didaktische Audits, sofern der Host diese Steuerung bereitstellt. Ein in der UI angezeigtes Label wie Gemini 3.1 Pro belegt noch nicht, welchen genauen Endpunkt die Anwendung nutzt.

Halte Arbeitsanweisungen prägnant und benenne Lernziel, Rahmenbedingungen und zu liefernde Lernnachweise. Hänge referenzierte Unterrichtsmaterialien direkt an, damit das Modell tatsächlichen Zugriff hat; eine bloße Pfadangabe im Text gewährt keinen Dateizugriff. Halte bei der Entwicklung von Anwendungen auf Basis der Gemini API den vorgeschriebenen Zustand von Werkzeugdialogen gemäß offizieller Dokumentation ein. Dieser Skill implementiert diesen API-Layer nicht selbst und autorisiert keine unaufgeforderte Einbindung.

Quellen: [Modelle](https://ai.google.dev/gemini-api/docs/models), [Thinking](https://ai.google.dev/gemini-api/docs/thinking), [Gemini CLI Skills](https://geminicli.com/docs/cli/tutorials/skills-getting-started/).

## Portabler Einsatz und Verifikation

Halte die erforderlichen Metadaten standardkonform: `name` und `description`, gefolgt von gewöhnlichem Markdown. Optionale Metadaten beschreiben die Edition; verlasse dich niemals auf ein hosts-spezifisches Metadatenfeld, um eine Sicherheitsgrenze durchzusetzen. Verwende die gebündelten relativen Referenzen in dateifähigen Agentenumgebungen oder die vollständige eigenständige Markdown-Datei in einfachen Chats. Lade standardmäßig nicht mehrere Sprachversionen gleichzeitig. Führe nach einem Kontextverlust des Hosts wesentliche Vorgaben und offene Aufgaben erneut ein, statt vorauszusetzen, dass jeder Host den vollständigen Verlauf behält.

Emojis können Bedeutungen unterstützen, dürfen jedoch niemals der einzige Instruktions- oder Prioritätsträger sein. Bewahre stets explizite Textbeschriftungen. Forschung zu [Emoji-Semantik](https://arxiv.org/abs/2409.10760) und [kontextueller Mehrdeutigkeit](https://arxiv.org/abs/2511.07193) zeigt, dass dekorative Emojis die Regeltreue von Sprachmodellen nicht verlässlich verbessern. Teste solche Änderungen an realen Modellen und Aufgaben, bevor ein didaktischer Nutzen behauptet wird.

Bevor eine Modell-/Host-Kombination als getestet gilt, verifiziere: erfolgreiche Erkennung oder fehlerfreies Laden der eigenständigen Datei, Zugriff auf relevante Referenzen, ein repräsentatives didaktisches Arbeitsergebnis und das Einhalten kritischer Systemgrenzen. Dokumentiere die exakte Modell-ID oder das sichtbare Label, Host und Version, Sprache, Denkaufwand, Ausführungsgeschwindigkeit, Werkzeuge, Datum, erzeugte Artefakte und aufgetretene Fehler. Trenne rein dokumentationsbasierte Kompatibilität strikt von beobachteter Ausführung. Übertrage einen erfolgreichen Test eines Modells niemals pauschal auf die gesamte Modellfamilie.

Nutze für Vergleiche identische Aufgabenstellungen und Ausgangsmaterialien. Lass die generierten Ergebnisse durch einen fachkundigen Prüfer anhand einheitlicher didaktischer Kriterien bewerten. Prüfe die Wiederverwendung bekannten Kontexts, kontrollierte Hilfestellungen, alternative korrekte Lösungen, den Umgang mit nicht belegten Lehrplanansprüchen, Modell-/Datengrenzen sowie Fehlerzustände bei Werkzeug- oder Dienstausfällen. Reduziere den Denkaufwand oder wechsle zu kleineren Modellen nur so lange, wie alle wesentlichen Prüfungen stabil bestanden werden. Ist der direkte Zugriff auf ein System nicht möglich, kennzeichne es transparent als ungetestet, statt Testergebnisse zu fingieren.
