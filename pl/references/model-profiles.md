# Modele, nakład pracy, szybkość i adaptacja do środowiska

Skorzystaj z tego dokumentu, rekomendując model, dobierając ustawienia szybkości/nakładu pracy (effort/thinking) lub dostosowując sposób ładowania skilla przez środowisko nadrzędne. Zachowaj identyczne wytyczne edukacyjne dla wszystkich dostawców modeli.

## Czego ten dokument nie deklaruje

Rekomendacje stanowią konfiguracje wyjściowe dla tego procesu projektowego, a nie benchmark czy pomierzony ranking. Nie dowodzą, że dana rodzina modeli uczy lepiej, ani nie przewidują opóźnień sieciowych (latencji). Nazwy modeli, dostępne ustawienia, plany i ceny ulegają ciągłym zmianom. Przed użyciem wskazanego modelu sprawdź listę modeli rzeczywiście dostępnych dla użytkownika oraz aktualną oficjalną dokumentację dostawcy. Etykieta w interfejsie nie zawsze odpowiada identyfikatorowi modelu w API. Potwierdź poprawność konfiguracji na reprezentatywnych zadaniach przed uznaniem jej za zweryfikowaną.

Stan dokumentacji sprawdzono: 2026-11-04.

## Dobieraj model do zadania przed wyborem nazwy

Stosuj mniejszy model do precyzyjnie określonych edycji treści według jawnych kryteriów, model średniej klasy do standardowego projektowania i implementacji, a model najwyższej klasy do sprzecznych źródeł, złożonych symulacji lub audytów o wysokiej stawce. Są to kategorie zadań, a nie gwarantowane możliwości technologiczne. Zachowaj dotychczasowy wybór użytkownika, jeśli spełnia on kryteria.

Poniższa tabela stanowi **nieprzetestowaną rekomendację wyjściową dla tego skilla**, opartą na dokumentacji producentów.

## Reguły eskalacji i zatrzymania

W przypadku jednoznacznego zadania zacznij od domyślnego nakładu pracy (effort/thinking) lub ustawienia, które sprawdziło się wcześniej. W przypadku sprzecznych źródeł lub złożonego modelu rozważ wyższy nakład pracy od samego początku. Jeśli odpowiedź pomija jawne ograniczenie, przeczy własnej punktacji, nie przechodzi testu obliczeniowego lub generuje błędne zadania, najpierw sprawdź, czy model miał dostęp do danych wejściowych i odpowiedniej referencji. Skoryguj brakujące dane wejściowe lub niejednoznaczne kryterium przed zmianą modelu.

Gdy po jednej ukierunkowanej poprawce odpowiedź nadal nie spełnia tego samego istotnego kryterium, zarekomenduj wyższy obsługiwany poziom nakładu pracy i ponownie oceń to kryterium. Jeśli błąd nie ustępuje, zarekomenduj mocniejszy dostępny model lub niezależną recenzję w zależności od wagi problemu. Nie ponawiaj prób w nieskończoność ani nie przekraczaj uzgodnionego budżetu. Brak źródeł, niedostępność narzędzi i awarie usług wymagają rozwiązania zależności lub wskazania ograniczenia; większy nakład rozumowania nie zastąpi brakujących dowodów. Raportuj nierozstrzygnięte błędy. Zmieniaj ustawienia wyłącznie za pomocą autoryzowanych kontrolek środowiska.

Zmniejszaj nakład pracy lub przechodź na mniejszy model dopiero po pomyślnym zaliczeniu odpowiednich testów; zachowaj dowody uzasadniające kompromis. Szybkość obsługi traktuj odrębnie: standardowa szybkość to punkt wyjścia, a płatna akceleracja wymaga uzasadnienia czasem/kosztem i wyraźnej autoryzacji.

## Utrzymanie aktualności rekomendacji

Sprawdź wytyczne ponownie, gdy zmieni się wersja modelu lub środowiska, zabraknie określonego ustawienia, dostawca zmieni dostępność lub udokumentowane zachowanie jest sprzeczne z obserwacją. Do czasu weryfikacji oznacz takie połączenie jako niezweryfikowane i stosuj kategorie zadań oraz domyślne ustawienia środowiska. Nie wymyślaj sztucznych odpowiedników dla nieznanych modeli. Dodawaj obejścia specyficzne dla danego dostawcy tylko wtedy, gdy powtarzalny błąd dowiedzie ich konieczności; odnotuj wersję i usuń obejście, gdy straci uzasadnienie.

## Dopasowanie zadania i kontrolek

| Zadanie | Punkt wyjścia OpenAI | Punkt wyjścia Claude | Punkt wyjścia Gemini |
|---|---|---|---|
| Drobne, precyzyjne edycje treści lub przegląd ustrukturyzowanych zadań | GPT-6 Luna, High; redukuj nakład dopiero po pomyślnych testach | Haiku 5.5, Medium | Gemini 3.5 Flash-Lite, Low tam gdzie obsługiwane |
| Projekt i implementacja zwartej aktywności edukacyjnej | GPT-6.1 Sol, domyślny nakład lub Medium | Sonnet 5.5, Medium dla precyzyjnych zadań agentowych | Gemini 3.8 Flash, Medium |
| Złożony audyt dydaktyczny, sprzeczne źródła, zaawansowana symulacja lub architektura | GPT-6 Astra, Light/Low lub Medium; zwiększ w razie potrzeby | Opus 5.5, Medium, następnie High w razie potrzeby | Gemini 4 Argon, Medium, następnie High w razie potrzeby |

Powyższe zestawienia to zalecenia autora skilla wyprowadzone z dokumentacji producentów. Jeśli wybrany model jest niedostępny, zarekomenduj dostępną alternatywę i poinformuj o zmianie; nie modyfikuj wyboru użytkownika bez autoryzacji. Na przykład istniejący proces oparty na Gemini 3.1 Pro może zachować ten model i obsługiwane poziomy rozumowania. Zmierz czas wykonania reprezentatywnego zadania w rzeczywistym środowisku, aby określić latencję.

Rozróżniaj trzy decyzje: model, głębokość rozumowania (effort/thinking) oraz płatny poziom przyspieszonej obsługi (Fast tier). Mniejszy nakład pracy może zredukować tokeny rozumowania; usługa typu Fast to inna kontrolka, która może wiązać się z wyższym kosztem. Nazwa Flash określa rodzinę modeli, a nie uniwersalny przełącznik trybu szybkiego. Identyczne słowa, takie jak Low, Medium i High, nie gwarantują równego poziomu rozumowania ani latencji u różnych dostawców.

Rozpoczynaj od standardowej szybkości. Rekomenduj płatny tryb Fast tylko wtedy, gdy czas oczekiwania jest krytyczny, a bieżący dostęp i stawki to uzasadniają. Nie włączaj go ani nie dokupuj limitów bez autoryzacji. Strumieniowanie (streaming) poprawia widoczność postępu; nie stanowi dowodu szybszego ukończenia pracy ani wyższej jakości. Oceniaj łączny czas procesu, w tym weryfikację, wywołania narzędzi i poprawki.

## OpenAI i Codex

Stosuj pakiet natywny, gdy środowisko obsługuje skille i potrafi odczytywać referencje. W Codex bezpośrednie wywołanie może odwoływać się do `$metodyki-nauczania` lub `$learning-methodologies`. Nie zakładaj wykrywania plików w zwykłym czacie; przekaż autonomiczny plik Markdown jako dostępne dane wejściowe.

Aktualne wytyczne zalecają Sol do prac zasadniczych, Luna do zadań precyzyjnych i Astra do procesów wymagających; Luna High i Astra Light/Low to udokumentowane ustawienia wyjściowe. W Codex tryb Fast to wybór szybkości obsługi, odrębny od nakładu rozumowania. Dostępność i limity zależą od modelu, konta i klienta. Sprawdź obsługiwane wartości przed zaproponowaniem konfiguracji; etykieta w UI nie zawsze jest identyfikatorem w API.

Podawaj konkretny oczekiwany rezultat, zakres, odpowiednie pliki i obserwowalne kryteria akceptacji. Oczekuj zwięzłych decyzji i dowodów, a nie ujawniania wewnętrznego toku myślenia (chain-of-thought). Wykorzystuj narzędzia i uprawnienia środowiska; nie przypisuj modelowi dostępu do powłoki czy przeglądarki na podstawie samej nazwy.

Źródła: [modele](https://learn.chatgpt.com/docs/models), [szybkość](https://learn.chatgpt.com/docs/agent-configuration/speed), [skille](https://developers.openai.com/plugins/concepts/skills).

## Claude i Claude Code

Claude Code obsługuje pakiety `SKILL.md` wraz z plikami pomocniczymi. Jawne wywołanie po wykryciu skilla może wykorzystywać polecenie `/metodyki-nauczania` lub `/learning-methodologies`. W innym środowisku Claude sprawdź mechanizm obsługi skilli lub dostarcz edycję autonomiczną. Nie dodawaj specyficznych dla Claude skryptów hooks, podstawień powłoki ani nadpisań modelu do wspólnego frontmattera.

Dla zadań agentowych w Sonnet 5.5 dokumentacja rekomenduje poziom Medium dla zadań dobrze zdefiniowanych i wyższy dla trudniejszych. Opus 5.5 domyślnie przyjmuje Medium; starsze modele i klienci mogą się różnić. Parametr effort w API i tryb myślenia (thinking mode) to odrębne pojęcia. Nie wszystkie generacje obsługują te same kombinacje. Preferuj obsługiwane kontrolki środowiska zamiast kopiowania parametrów API do promptu w czacie. Tryb Fast w Claude to odrębna funkcja zależna od modelu, objęta wyższym cennikiem.

Precyzyjnie wyznaczaj granice zadania, materiały i pożądany wynik. Wskaż, w których obszarach agent może decydować samodzielnie, a co wymaga dowodów. Podaj jeden trafny przykład, jeśli rozwiązuje on niejednoznaczność; unikaj powtarzania całego skilla lub narzucania długiej transkrypcji myśli. Taki sposób pakowania sprzyja przenośności i nie jest twierdzeniem o unikalnych cechach poznawczych Claude.

Źródła: [skille](https://code.claude.com/docs/en/skills), [modele](https://platform.claude.com/docs/en/models/overview), [nakład pracy (effort)](https://platform.claude.com/docs/en/build-with-claude/effort), [tryb Fast](https://platform.claude.com/docs/en/build-with-claude/fast-mode).

## Gemini i Gemini CLI

Gemini CLI wykrywa skille natywne w obsługiwanych katalogach, w tym w aliasie `.agents/skills`. Sprawdź dostępność poleceniem `/skills list` i w razie potrzeby przeładuj za pomocą `/skills reload`. Zaufanie do przestrzeni roboczej i zgody na aktywację należą do środowiska; nie omijaj ich. W AI Studio lub innym czacie należy użyć pliku autonomicznego, jeśli ładowanie natywne jest niedostępne.

Aktualny przewodnik po myśleniu (thinking) wymienia poziomy Low, Medium i High dla Gemini 4 Argon oraz Gemini 3.8 Flash. Inne wersje Gemini mają odmienne wartości domyślne i poziomy. Stosuj wyłącznie poziomy obsługiwane przez dany model i API/klienta; nie tłumacz dosłownie parametrów z OpenAI lub Claude. Nazwa wersji zapoznawczej (preview) i nazwa stabilna nie są tożsame.

Dla punktu końcowego `gemini-3.1-pro-preview` tabela API wymienia poziomy Low, Medium i High, z High jako wartością domyślną. Dla tego endpointu wypróbuj Medium do standardowego projektowania i High do trudnego audytu (jako rekomendację autora), o ile środowisko udostępnia te kontrolki. Etykieta taka jak Gemini 3.1 Pro nie przesądza o tym, z jakiego endpointu lub kontrolek korzysta dany klient.

Formułuj instrukcje zwięźle i precyzuj cel, ograniczenia oraz dowody wyjściowe. Dołączaj wskazywane materiały, aby model miał do nich rzeczywisty dostęp; sama ścieżka wpisana w czacie nie daje dostępu do pliku. Zachowaj wymagany stan konwersacji narzędziowej przy tworzeniu aplikacji z API Gemini, zgodnie z bieżącą dokumentacją API. Ten skill nie wdraża tej warstwy API ani nie autoryzuje jej dodawania.

Źródła: [modele](https://ai.google.dev/gemini-api/docs/models), [myślenie (thinking)](https://ai.google.dev/gemini-api/docs/thinking), [skille w Gemini CLI](https://geminicli.com/docs/cli/tutorials/skills-getting-started/).

## Zastosowanie uniwersalne i weryfikacja

Utrzymuj proste, standardowe metadane: `name` i `description`, a po nich zwykły Markdown. Opcjonalne metadane opisują edycję; nie polegaj na polach specyficznych dla danego hosta w celu egzekwowania granic bezpieczeństwa. Stosuj powiązane względne referencje w agencie z dostępem do plików lub kompletną edycję autonomiczną w oknie czatu. Domyślnie nie ładuj obu edycji językowych naraz. Ponownie dołączaj kluczowy zakres i niedokończoną pracę po utracie kontekstu przez środowisko, zamiast zakładać, że każdy host zachowuje pełną pamięć.

Emoji mogą nieść znaczenie, lecz nie powinny być jedynym nośnikiem poleceń ani sygnałem priorytetu. Zachowaj jednoznaczne etykiety tekstowe. Badania nad [semantyką emoji](https://arxiv.org/abs/2409.10760) oraz [niejednoznacznością kontekstową](https://arxiv.org/abs/2511.07193) nie wykazują, by ozdabianie skilla ikonami poprawiało stosowanie się do instrukcji. Przetestuj taką zmianę na rzeczywistych modelach i zadaniach przed ogłoszeniem korzyści.

Zanim uznasz kombinację modelu i środowiska za przetestowaną, zweryfikuj wykrywanie skilla lub pomyślne załadowanie edycji autonomicznej, dostęp do odpowiednich referencji, reprezentatywny rezultat pracy oraz kluczowe granice bezpieczeństwa. Zapisz dokładny identyfikator modelu lub widoczną etykietę, środowisko/wersję, język, nakład pracy, szybkość obsługi, narzędzia, datę, artefakty i błędy. Odróżniaj deklarowaną w dokumentacji kompatybilność od zaobserwowanego wykonania. Nigdy nie przenoś pozytywnego wyniku jednego testu na wszystkie modele z danej rodziny.

Do celów porównawczych stosuj to samo zadanie i materiały wyjściowe, a recenzent powinien oceniać rzeczywiste wyniki według tych samych kryteriów dydaktycznych. Uwzględnij ponowne wykorzystanie znanego kontekstu, kontrolowaną pomoc, poprawną odpowiedź alternatywną, niepoparte dowodami roszczenia programowe, granice modelu/danych oraz awarie narzędzi i usług. Zmniejszaj nakład pracy lub wybieraj mniejszy model tylko wtedy, gdy kluczowe testy stale kończą się sukcesem. Jeśli bezpośredni dostęp do dostawcy jest niemożliwy, oznacz go jako nieprzetestowany zamiast wymyślać wyniki.
