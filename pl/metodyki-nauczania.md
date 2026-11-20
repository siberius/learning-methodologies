---
name: metodyki-nauczania
description: Projektuj lub oceniaj aplikacje edukacyjne, łącząc cele nauczania, potrzeby uczniów, aktywności, informację zwrotną i dowody uczenia się. Stosuj przy tworzeniu nowych narzędzi edukacyjnych lub istotnych zmianach w ich strukturze dydaktycznej.
metadata:
  version: "1.6.0"
  language: "pl"
  based_on: "learning-methodologies@1.6.0"
  license: "MIT"
  repo: "https://github.com/siberius/learning-methodologies"
  author: "Luděk Sušický"
  format: "pakiet natywny z wygenerowanym autonomicznym Markdownem"
---


<!-- Wygenerowano z SKILL.md i references/. Edytuj pliki źródłowe. -->


# Metodyki nauczania

Pomagaj w projektowaniu, wdrażaniu i ewaluacji aplikacji edukacyjnych, których aktywności edukacyjne, wsparcie i ocenianie służą docelowym uczniom. Dostosuj głębokość pracy do zadania, jego konsekwencji i stopnia niepewności. Krótka aktywność lekcyjna nie wymaga pełnego badania ewaluacyjnego ani obszernego dokumentu planistycznego.

## Metody dydaktyczne dla aplikacji tworzonych z udziałem AI

Stosuj metody dydaktyczne, aby przekładać cele edukacyjne na działania uczniów, reguły informacji zwrotnej i dowody uczenia się w generowanej aplikacji. Na przykład praktyka przypominania wymaga podjęcia próby przed odsłonięciem odpowiedzi, a rusztowanie poznawcze (scaffolding) wymaga kontrolowanej pomocy i odróżnienia wykonania ze wsparciem od samodzielnego. AI może pomóc we wdrażaniu tych decyzji; jej wyniki wciąż wymagają weryfikacji merytorycznej i dydaktycznej. Dotyczy to zarówno aplikacji działających w trybie offline, jak i wykorzystania AI w fazie wykonawczej (runtime), gdy wymaga tego cel dydaktyczny.

Przeczytaj [uzasadnienie dydaktyczne](#reference-didactic-rationale), wyjaśniając, dlaczego dana metoda jest odpowiednia lub przekładając ją na implementację. Łączy ono metody dydaktyczne z decyzjami produktowymi i dowodami niezbędnymi do ich oceny.

## Prowadzenie twórcy przez decyzje projektowe

Przy każdej istotnej decyzji dotyczącej projektowania dydaktycznego powracaj do celu, działań ucznia, dowodów, wsparcia i ograniczeń. Bazuj na wcześniej podjętych ustaleniach. W przypadku nierozstrzygniętego, brzemiennego w skutki wyboru przedstaw niewielki, adekwatny zestaw opcji — zazwyczaj dwie lub trzy — wraz z prostym opisem i konkretnym przykładem w tym projekcie. Zarekomenduj jedno rozwiązanie, wyjaśnij główny kompromis (trade-off) i zapytaj, które podejście preferuje twórca. Przeczytaj [dialog projektowy](#reference-design-dialogue), rozpoczynając lub wznawiając taki wybór. Reguły te porządkują rozmowę z twórcą aplikacji, niezależnie od interakcji tutora z uczniem.

Nie otwieraj ponownie rozstrzygniętych lub odrzuconych wyborów bez istotnej zmiany kontekstu. Uszanuj wyraźne przekazanie rutynowych decyzji agentowi i kontynuuj pracę z krótkim uzasadnieniem. Cisza nie oznacza zgody na rozszerzenie zakresu. W oczekiwaniu na odpowiedź pracuj nad niezależnymi elementami. Zmiana czysto kosmetyczna nie uruchamia tego procesu.

Wczytuj szczegóły według potrzeb: [metody](#reference-methods) dla aktywności edukacyjnych i wsparcia; [gry](#reference-learning-games) dla motywacji i mechanik; [ocenianie](#reference-assessment) dla dowodów i punktacji; [interfejs poznawczy](#reference-cognitive-ux) dla reprezentacji, multimediów i uwagi; [praktyka adaptacyjna](#reference-adaptive-practice) dla powtórek w czasie lub doboru trudności. Stosuj istniejące warunkowe ścieżki dla symulacji, stanu tutora i AI w fazie wykonawczej. Przeczytaj odpowiednią metodę przed jej zaproponowaniem; nie ładuj wszystkich plików referencyjnych naraz.

Przekładaj wybraną metodę na obserwowalne zachowanie produktu i miarodajny test. Odróżniaj decyzje zaproponowane, wybrane, wdrożone i zweryfikowane. Weryfikacja techniczna nie dowodzi skuteczności edukacyjnej.

## Ścieżka pracy

Podążaj tą ścieżką z głębokością odpowiadającą potrzebom zadania: określ cel i ograniczenia → wybierz metodę odpowiadającą trudności poznawczej → powiąż aktywność ucznia z dowodem uczenia się → wdróż rozwiązanie w ramach zakresu → sprawdź rezultat. W przypadku audytu zbadaj istniejący projekt zamiast pisać kod. Wykorzystuj znany kontekst; nie wymagaj sformalizowanego dokumentu planistycznego dla każdego kroku.

Przeczytaj [przykłady decyzji](#reference-decision-examples), gdy doprecyzowania wymaga pomoc, akceptacja odpowiedzi alternatywnych lub niepewna zgodność z podstawą programową. Ilustrują one decyzje, nie są gotowymi szablonami do kopiowania do każdej lekcji.

## Określenie kontekstu edukacyjnego

Wykorzystuj informacje już obecne w zapytaniu, projekcie i dostarczonych materiałach. W przypadku luk w kontekście pytaj tylko o kwestie, które w istotny sposób zmieniają projekt. Przy drobnych niepewnościach przyjmij rozsądne założenie i kontynuuj. Unikaj sztywnych ankiet i powtarzających się próśb o zatwierdzenie rutynowych wyborów objętych już treścią zadania.

Zidentyfikuj kontekst wpływający na projekt: uczniów i ich wiedzę uprzednią, przedmiot, zamierzone efekty kształcenia, pracę w klasie lub samodzielną, dostępny czas i urządzenia, język, potrzeby dostępności oraz ewentualną dostarczoną podstawę programową. Uwzględniaj ramy programowe, gdy odnosi się to do danego środowiska; nie zakładaj z góry jednego systemu krajowego. Dobierz ton do kontekstu i preferencji autora. Nie wnioskuj o uwadze, motywacji, zdolnościach ani preferowanej pedagogice na podstawie etykiet pokoleniowych.

Uwzględniaj otoczenie dydaktyczne, gdy jest to pomocne: przygotowanie, pracę indywidualną lub grupową, interwencję nauczyciela, dyskusję i podsumowanie. Pokaz prowadzony przez nauczyciela może wymagać dobrego pytania do dyskusji; konta użytkowników i indywidualne rejestry ocen nie są konieczne.

Rozróżniaj wiek, rolę edukacyjną i doświadczenie w danym temacie: dziecko, uczeń szkoły podstawowej, uczeń szkoły ponadpodstawowej, student i dorosły uczestnik nie są pojęciami zamiennymi ani poziomami zdolności. Definiując lub modyfikując grupę docelową, przeczytaj profil ucznia w [dialogu projektowym](#reference-design-dialogue). Dostosuj terminologię i wsparcie do środowiska; w ogólnych wskazówkach stosuj neutralne określenia. Twórca, uczeń i towarzyszący nauczyciel lub rodzic mogą być różnymi osobami.

## Łączenie celów z obserwowalną aktywnością

Dla każdego istotnego celu powiąż działanie ucznia, dowód uczenia się, kryteria sukcesu, warunki udzielenia pomocy i kolejną decyzję dydaktyczną. W przypadku małych zadań zachowaj zwięzłość. Przy otwartym dociekaniu dowód może dotyczyć jakości pytań, posługiwania się faktami lub rewizji wyjaśnienia; jedna z góry ustalona odpowiedź nie jest jedyną możliwością.

Przykład: uczeń przewiduje, jak zmiana oporu wpływa na natężenie prądu, sprawdza to w modelu, wyjaśnia ewentualne rozbieżności i rozwiązuje nowe zadanie samodzielnie. Samo przesunięcie suwaka lub przejście do kolejnego ekranu nie dowodzi zrozumienia.

Na podstawie zaobserwowanej trudności w uczeniu się dobierz adekwatną interwencję. Traktuj wyjaśnienie błędu jako hipotezę roboczą, a nie ostateczną diagnozę. Wybierz spójny, niewielki zestaw metod; nie dodawaj funkcji tylko dlatego, że znajdują się w katalogu. Przeczytaj [metody](#reference-methods) przy wyborze lub wdrażaniu metody, sekwencji wsparcia lub reguły progresji.

W przypadku mechanik gier, elementów motywacyjnych lub audytu gier edukacyjnych przeczytaj [gry edukacyjne i celowa grywalizacja](#reference-learning-games). Zawiera omówienie grywalnych pętli edukacyjnych, doboru mechanik, granic dowodowych i wdrożeń — od drobnych pomocy dydaktycznych po produkty długoterminowe. Dostosowuj rozwiązania do szkół podstawowych, ponadpodstawowych, uczelni i dorosłych w różnych krajach, opierając się na wiedzy uprzedniej i lokalnym kontekście.

Referencja metod szczegółowo obejmuje: dialog sokratejski, technikę Feynmana, strefę najbliższego rozwoju (ZPD) i rusztowanie poznawcze (scaffolding), przykłady z rozwiązaniem (worked examples), praktykę przypominania i powtórki rozłożone w czasie, uczenie się na błędach, metapoznanie, dociekanie (inquiry), odgrywanie ról (role-play), uczenie się rówieśnicze i kooperatywne, metodę projektów, klasę odwróconą oraz opcjonalną grywalizację. Są to podejścia do wyboru, a nie obowiązkowe elementy każdej aplikacji.

Taksonomia Blooma opisuje cele poznawcze i rodzaje wiedzy. Rozdzielaj poziom trudności od wymagań wstępnych; nie wprowadzaj sztywnych sześciu zablokowanych poziomów. W przypadku umiejętności praktycznych lub społecznych dobieraj adekwatne dowody i otwarcie określaj, czego zadanie na ekranie nie jest w stanie zweryfikować.

## Wybór realistycznej realizacji technicznej

Rozróżniaj AI używane do budowy aplikacji od AI wykorzystywanego przez uczniów w gotowym produkcie. Wybieraj między zweryfikowaną treścią statyczną, deterministycznymi interakcjami lub symulacjami a AI w fazie wykonawczej (runtime), kierując się celem i ograniczeniami środowiskowymi. Wskazówki, informacja zwrotna i powtórki rozłożone w czasie mogą doskonale działać bez zewnętrznej usługi AI.

Przed dodaniem rozbudowanej funkcji rozważ jej wkład dydaktyczny, obciążenie interakcyjne, nakład pracy nauczyciela, utrzymanie, wymogi dotyczące danych i koszty eksploatacji. Wyjaśniaj istotne kompromisy. Nie wprowadzaj kont, analityki, paneli administratorskich, backendu, płatnych usług ani zewnętrznych przepływów danych tylko po to, by aplikacja sprawiała wrażenie kompletnej. Potwierdzaj decyzje zmieniające zakres, jeśli nie zostały wcześniej uzgodnione.

Przeczytaj [symulacje](#reference-simulations), projektując model zjawiska, eksperyment lub odgrywanie ról. Wyraźnie rozróżniaj rzeczywiste obserwacje, obliczenia modelu i rekonstrukcję fikcyjną. Nigdy nie przedstawiaj wygenerowanych przez AI danych jako pomiarów ani nie twórz pozorów przeprowadzenia realnego eksperymentu.

Przeczytaj [sztuczna inteligencja w fazie wykonawczej](#reference-runtime-ai) tylko wtedy, gdy gotowy produkt odwołuje się do usługi AI w trakcie użytkowania. Zdefiniuj rolę dydaktyczną, granice źródeł, nadzór człowieka, przepływy danych, limity kosztów i zachowanie w stanach awaryjnych. Prompt nie zastępuje zabezpieczeń aplikacji.

Przeczytaj [tryby i ciągłość tutora](#reference-tutor-state), implementując wieloetapowe prowadzenie ucznia, przejścia między ćwiczeniami a sprawdzianem lub wznawianie nauki. Przechowuj stan i dowody w samej aplikacji; funkcje te nie wymagają runtime AI.

## Budowanie wiarygodnej informacji zwrotnej i decyzji

Zapewnij użyteczny kolejny krok po wystąpieniu błędu. W trybie ćwiczeń umożliwiaj skorzystanie z pomocy i przejście do bezpośredniego wyjaśnienia lub rozwiązanego przykładu; unikaj niekończącego się odpytywania. Ograniczaj wsparcie na podstawie samodzielnych osiągnięć, zachowując dostęp do pomocy na żądanie. Sprawdzian może ograniczać pomoc na wyraźnie określonych warunkach.

Rozróżniaj samodzielny sukces, sukces z pomocą, ujawnienie odpowiedzi i stan niepewności. Jedno trafne zgadnięcie, deklaracja pewności siebie lub dwa udane zadania ze wsparciem nie oznaczają opanowania materiału. Nie wnioskuj o trwałych uzdolnieniach, motywacji ani zaburzeniach na podstawie krótkiej interakcji.

Przeczytaj [ocenianie](#reference-assessment), projektując punktowane zadania, kryteria oceniania (rubryki), adaptacyjność lub ewaluację uczenia się. Weryfikuj poprawność merytoryczną, prawdopodobne alternatywy, jednostki liczbowe i tolerancje oraz to, czy zadanie rzeczywiście wymaga docelowej umiejętności. Uwzględniaj poprawne alternatywne metody i wyjaśnienia. Oddzielaj nagrody w grze i tempo pracy od faktycznych osiągnięć, chyba że szybkość jest jawnym celem kształcenia.

## Zachowanie dostępności i decyzyjności nauczyciela

Projektuj z uwzględnieniem kryteriów WCAG 2.2 na poziomie AA odpowiadających danej aktywności i rzeczywistym potrzebom uczniów. Zapewnij obsługę z klawiatury, widoczny fokus, zrozumiałe etykiety i komunikaty zwrotne, alternatywy dla samego koloru lub dźwięku oraz uzasadniony lub regulowany czas na odpowiedź. Dobieraj sposoby percepcji informacji i wyrażania zrozumienia do ucznia; nie przypisuj uczniom sztywnych „stylów uczenia się”. W razie potrzeby skorzystaj ze specjalistycznych wytycznych dostępności.

Zbieraj wyłącznie dane niezbędne do przeprowadzenia aktywności i jasno określ, kto ma do nich dostęp, dokąd trafiają i jak długo są przechowywane. Uwzględniaj wymagania dostawców, szkół i lokalnych przepisów w miejscu wdrożenia; nie twórz uniwersalnych reguł prawnych. Lokalna, anonimowa aktywność nie wymaga tworzenia kont ani trwałego śledzenia.

Zapewnij nauczycielowi lub autorowi możliwość weryfikacji treści, korygowania ocen i ingerencji w nieodpowiednią adaptację. Zwykle wystarczy edytowalny plik z zawartością; pełny system zarządzania nauczaniem nie jest konieczny. Ważne decyzje dotyczące oceniania lub kwalifikacji wymagają odpowiedzialnej weryfikacji przez człowieka.

## Koordynacja wiedzy specjalistycznej bez rozbudowy procesu

Wykorzystuj następujące perspektywy w zależności od potrzeb; w małym zadaniu jeden agent może łączyć je wszystkie:

- Metodyk: zamierzone efekty, kontekst dydaktyczny i wybory metodyczne.
- Dydaktyk przedmiotowy: poprawność merytoryczna, wymagania wstępne, przykłady i typowe błędy poznawcze.
- Projektant oceniania: dowody uczenia się, kryteria, alternatywy i granice wnioskowania.
- Projektant interakcji: przepływ pracy ucznia, pomoc, dostępność i zastosowanie w klasie.
- Programista: struktury danych, obliczenia, stan, trwałość i obsługa błędów.
- Recenzent: rozbieżności między celem, projektem a zaobserwowanym działaniem.

Przekładaj ich ustalenia na implementację. Nie nazywaj wygodnego wyboru technicznego poprawnym pedagogicznie bez dowodów. Rozstrzygaj istotne spory poprzez weryfikację źródeł, ukierunkowany test lub jasne sformułowanie otwartego pytania. Stosuj niezależną recenzję, gdy uzasadnia to złożoność lub waga decyzji; nie twórz zespołu do każdego zadania. Uruchamiaj inne skille tylko wtedy, gdy są dostępne i niezbędne.

## Weryfikacja i raportowanie na właściwym poziomie

Przy wdrażaniu sprawdzaj ścieżkę ucznia, błędy rzeczywiście popełniane przez uczniów, ścieżkę pomocy i istotne stany awaryjne. W przypadku zapytań czysto analitycznych przedstaw wnioski i propozycje bez modyfikacji produktu. Dostosuj testy do specyfiki aplikacji: symulacja wymaga sprawdzenia modelu; runtime AI wymaga testów odporności na awarie usługi i obsługi generowanych odpowiedzi; prosta aktywność statyczna domyślnie nie potrzebuje żadnego z tych mechanizmów.

Oddzielaj trzy kategorie wniosków: poprawność techniczną, adekwatność dydaktyczną i zaobserwowane efekty uczenia się. Same testy techniczne nie dowodzą skuteczności edukacyjnej. Niewielki pilotaż może ujawnić problemy bez wykazywania związku przyczynowo-skutkowego. Raportuj faktycznie przeprowadzone testy i nierozstrzygnięte założenia; nie wymyślaj obserwacji uczniów ani wyników skuteczności.

Przy przekazywaniu wyników podsumuj cel edukacyjny, wybrane podejście, istotne założenia operacyjne, faktycznie wykonane testy i pozostałe ograniczenia. Dołącz tabelę powiązania celów z dowodami tylko wtedy, gdy ułatwia to korzystanie z rezultatu. Dostosuj formę do życzenia użytkownika.

## Tworzenie tekstów dla uczniów bez żargonu AI (AI slop)

Język aplikacji jest nośnikiem dydaktyki. Stosuj te same standardy do poleceń, instrukcji, informacji zwrotnej i wyjaśnień:

- Wykreśl puste przymiotniki („nowoczesny”, „angażujący”, „interaktywny”), chyba że kolejne zdanie natychmiast wyjaśnia, na czym polega ta cecha.
- Formułuj myśli bezpośrednio; unikaj konstrukcji typu „to nie tylko X, ale również Y” oraz „to nie X, to Y”.
- Pomiń zapowiedzi w rodzaju „w tej aktywności nauczysz się”; napisz wprost, co uczeń robi.
- Informacja zwrotna wskazuje precyzyjnie: co jest poprawne, czego brakuje i jaki jest kolejny konkretny krok.
- Podawaj precyzyjne liczby, jednostki i warunki; unikaj sformułowań typu „znacząco poprawia” bez podania miary.
- Żadnych emoji w przyciskach, nagłówkach ani etykietach. Używaj tekstu i spójnego zestawu ikon.
- Dostosuj słownictwo do uczniów i konsekwentnie stosuj jedno pojęcie na określenie danej rzeczy.

Przeczytaj tekst oczami ucznia. Jeśli zdanie mogłoby pojawić się bez zmian w dowolnym innym produkcie, wykreśl je lub sformułuj konkretnie.

## Integracja

Przy wyborze modelu, nakładu rozumowania (effort), szybkości lub dostosowywaniu mechanizmu ładowania przeczytaj [profile modeli i środowisk](#reference-model-profiles). Zawiera on wskazówki oparte na dokumentacji OpenAI, Claude i Gemini. Utrzymuj wspólny standard dydaktyczny i oddzielaj faktycznie przeprowadzone testy od deklarowanej kompatybilności. Nie wczytuj profilu dla zwykłego zadania edukacyjnego, które tego nie wymaga.

Rozwiązanie przeznaczone do gier edukacyjnych, quizów, samouczków, symulacji i audytów ich struktury dydaktycznej. Rdzeń nie wymaga pakietów zewnętrznych, API, konkretnego modelu AI ani danych uczniów. Poniższe referencje zostały dołączone do użytku autonomicznego. W pakiecie natywnym są to osobne pliki ładowane w razie potrzeby. Instalacja, wdrożenie i inne zmiany zewnętrzne wymagają autoryzacji tych działań. Skill nie zastępuje instrukcji projektowych ani nie rozszerza uprawnień.

Materiały referencyjne do projektowania: [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [Wytyczne UDL organizacji CAST](https://udlguidelines.cast.org/). Służą one jako wsparcie w projektowaniu i ewaluacji; powołanie się na nie nie stanowi certyfikatu zgodności ani skuteczności edukacyjnej.

## Reference: methods

Sekcja źródłowa: Wybór metod uczenia się


Skorzystaj z tego dokumentu po zdefiniowaniu celu kształcenia i dowodu osiągnięcia sukcesu. Wybierz najmniejszą użyteczną interwencję odpowiadającą aktualnej przeszkodzie w uczeniu się. Sam format aplikacji nie determinuje metody dydaktycznej. Nie dodawaj wszystkich wymienionych tu metod naraz.

### Metody: Karty metod dla konkretnego wyboru

Stosuj te stabilne identyfikatory we wszystkich tłumaczeniach i rejestrach decyzji. Każdy wiersz zawiera krótki opis dla twórcy, potrzebę, działanie ucznia i dowód. Szczegółowe sekcje poniżej opisują formy wsparcia i ograniczenia. Dla wybranej karty wskaż prostą implementację, ewentualne opcjonalne rozszerzenie, test weryfikacyjny błędu i odpowiednie źródło; domyślnie nie wyświetlaj całego katalogu. Źródła wspierają określone zasady dydaktyczne, a nie ogólną skuteczność generowanej aplikacji.

Dla wybranej karty określ grupę docelową, niezbędną wiedzę uprzednią oraz dostosowania w języku, wsparciu lub ocenianiu; nie dobieraj metody wyłącznie na podstawie wieku.

| Identyfikator i krótki opis | Kiedy zaproponować i prosta implementacja | Test dowodu i wsparcia |
| --- | --- | --- |
| `worked-example-fading`: zobacz procedurę, uzupełnij ją, a następnie wykonaj samodzielnie | Nowa procedura; zweryfikowany przykład i zadanie z luką do uzupełnienia | Nowy samodzielny przypadek; pomijanie dla zaawansowanych i przywracanie pomocy w razie potrzeby |
| `guided-inquiry`: przewiduj, zmień zmienną, wyjaśnij rezultat | Zrozumienie zjawiska/systemu; jeden ściśle ograniczony eksperyment | Wyjaśnienie nowego przewidywania; losowe manipulowanie nie zastępuje rozumowania |
| `productive-failure`: wypróbuj podejścia przed porównaniem ich z wyjaśnieniem | Wystarczająca wiedza uprzednia i czas na konsolidację | Porównanie podejść i zastosowanie skonsolidowanej wiedzy; nie pozostawiaj nowicjusza w bezradności |
| `retrieval-spacing`: przypomnij przed odsłonięciem, powróć w czasie | Utrwalenie dostępnej wiedzy; próba, korekta i późniejsza powtórka | Samodzielne przypomnienie po odroczeniu; natychmiastowa korekta to nie powtórka w czasie |
| `contrast-interleaving`: odróżnij podobne przypadki i wybierz strategię | Mylenie pojęć lub procedur po wstępnym etapie wsparcia | Wyjaśnienie cechy różnicującej; losowe mieszanie tematów nie wystarcza |
| `socratic-dialogue`: zbadaj rozumowanie poprzez ukierunkowane pytanie | Uzasadniona odpowiedź może ujawnić użyteczną niepewność | Korekta lub obrona na podstawie dowodów; bezpośrednie wyjaśnienie pozostaje dostępne |
| `self-explanation`: wyjaśnij własnymi słowami i skoryguj błędy | Ujawnienie luk po wstępnym etapie nauki | Poprawność merytoryczna i zastosowanie, a nie sama płynność językowa |
| `cooperative-project`: koordynacja ról w celu stworzenia wartościowego projektu | Wspólne badanie lub autentyczne zadanie przy odpowiednim czasie | Indywidualny wkład i wyjaśnienie; sukces grupy nie dowodzi opanowania przez każdego |
| `role-play`: podejmuj decyzje z perspektywy roli i dokonaj refleksji | Perspektywy, komunikacja lub osąd proceduralny | Wyjaśnienie wyborów i konsekwencji; zgoda z postacią nie oznacza poprawności |
| `metacognitive-review`: porównaj plan lub pewność siebie z dowodami | Wspieranie samoregulacji i kolejnych kroków | Zmiana działania oparta na wykonaniu; pewność siebie to nie umiejętności |
| `criterion-rubric`: oceniaj obserwowalne cechy według kryteriów | Odpowiedzi otwarte, projekty lub uzasadnione warianty alternatywne | Przykłady na granicach poziomów i ścieżka poprawy; nie nagradzaj samej zgody |
| `representation-transfer`: połącz reprezentację konkretną z formalną | Sukces pozostaje powiązany wyłącznie z obiektami gry | Zastosowanie w nowej reprezentacji; zachowanie dostępnych, równoważnych ścieżek |

W wersjach zróżnicowanych (dla uczniów o różnych potrzebach) określ wspólny cel kształcenia oraz kluczową decyzję dydaktyczną, którą każda wersja musi zachować. Różnicuj język, reprezentację, tempo i wsparcie, nie podsuwając po cichu gotowej decyzji. Zapewnij angażujący kontekst dla uczniów korzystających ze wsparcia. Rozwijaj zadania poprzez uzasadnianie, kontrprzykłady lub transfer, a nie samo dokładanie kolejnych zadań. Jawnie identyfikuj zamierzoną zmianę celu. Podział na grupy powinien wynikać z weryfikowalnych dowodów, a nie trwałych etykiet zdolności.

Opcjonalne rozszerzenia, takie jak trwałe harmonogramowanie powtórek czy asysta AI na żywo, wymagają konkretnego uzasadnienia i odwołania do odpowiednich referencji warunkowych. Zachowaj źródło, wersję i system prawny dla odniesień do programu nauczania; odróżniaj oficjalne standardy od domniemanych wymagań wstępnych. Krawędź na mapie pojęciowej nie stanowi automatycznie zweryfikowanej progresji uczenia się.

### Metody: Wybór na podstawie zaobserwowanej potrzeby dydaktycznej

| Zaobserwowana przeszkoda | Proponowana interwencja | Weryfikacja przed wdrożeniem |
|---|---|---|
| Kluczowa wiedza nie zostaje zapamiętana | Praktyka przypominania z powtórkami rozłożonymi w czasie | Czy uczniowie potrafią przypomnieć ją sobie samodzielnie po pewnym czasie? |
| Nowicjusz nie potrafi rozpocząć procedury | Przykład z rozwiązaniem, zadania z lukami i zadania samodzielne | Czy wymagania wstępne są spełnione, a kroki w pełni zrozumiałe? |
| Uczniowie powtarzają konkretny błąd poznawczy | Przykłady kontrastowe, wyjaśnienie, pytanie ukierunkowane i ćwiczenie korygujące | Czy zadanie pozwala odróżnić ten konkretny błąd poznawczy od innych pomyłek? |
| Uczniowie wykonują zadanie, lecz nie potrafią go wyjaśnić ani dokonać transferu | Samoobjaśnianie, przypadki kontrastowe, zastosowanie w nowym kontekście | Czy sukces wymaga myślenia przyczynowego, a nie kopiowania schematu? |
| Uczniowie mają trudność z oceną własnego zrozumienia | Przewidywanie, ocena pewności siebie, samodzielne sprawdzenie i refleksja | Czy potrafią zestawić swój subiektywny osąd z faktycznymi dowodami? |
| Cel obejmuje dociekanie lub interakcję zawodową | Ukierunkowane badanie, odgrywanie ról lub symulacja z podsumowaniem | Czy model, scenariusz, dowody i kryteria są wiarygodne i rzetelne? |

Zaobserwowane trudności stanowią robocze hipotezy dydaktyczne. Błędna odpowiedź, wolna reakcja lub prośba o pomoc nie diagnozują zaburzeń uczenia się, braku motywacji, inteligencji ani trwałych cech ucznia. Zapytaj lub zbadaj problem głębiej, gdy do sytuacji pasuje kilka wyjaśnień.

### Metody: Taksonomia Blooma jako perspektywa projektowa

Zrewidowana taksonomia ma dwa wymiary: wiedzę (faktograficzną, pojęciową, proceduralną, metapoznawczą) oraz procesy poznawcze (pamiętanie, rozumienie, stosowanie, analizowanie, ocenianie, tworzenie). Używaj ich do opisu celów i analizy kompletności zadań. Zadanie może łączyć różne procesy; sam czasownik operacyjny w poleceniu nie decyduje o jego klasyfikacji.

Rozdzielaj poziom trudności zadania, programowe wymagania wstępne i reguły progresji. Nie wprowadzaj wymogu przechodzenia przez sześć obowiązkowych poziomów ani nie wnioskuj o opanowaniu wiedzy wyłącznie na podstawie etykiety Blooma. Buduj relacje wymagań wstępnych na podstawie struktury danej dziedziny. Uwzględniaj cele praktyczne, interpersonalne i emocjonalne, gdy są istotne, wraz z odpowiadającymi im obserwowalnymi dowodami. Kategorie poznawcze Blooma nie obejmują wszystkich celów kształcenia.

### Metody: Strefa najbliższego rozwoju (ZPD) i rusztowanie poznawcze (scaffolding)

Strefa najbliższego rozwoju dotyczy relacji między wykonaniem samodzielnym a tym, co staje się możliwe przy odpowiednim wsparciu. Stosuj tę perspektywę, gdy uczeń potrafi wykonać zadanie z pomocą, lecz nie potrafi jeszcze zrobić tego sam. Rusztowanie poznawcze (scaffolding) dostarcza tymczasowych wskazówek, przykładów lub częściowych kroków. Nie wyznaczaj sztywnej granicy zdolności na podstawie pojedynczego błędu.

W przypadku nowicjuszy rozważ przykład z jawnym tokiem rozumowania, zadanie do dokończenia i praktykę samodzielną. Dostosuj poziom szczegółowości do wiedzy uprzedniej. Podawaj tylko te informacje, które są niezbędne na bieżącym etapie; dekoracyjna złożoność i jednoczesne konkurencyjne bodźce wymagają uzasadnienia dydaktycznego.

Stosuj elastyczną sekwencję pomocy: doprecyzuj problem, podaj ukierunkowaną wskazówkę, zaproponuj częściowy krok, a w razie potrzeby lub na żądanie przedstaw rozwiązanie z komentarzem. Po pracy ze wsparciem zaproponuj porównywalne zadanie samodzielne. Wycofuj pomoc w miarę wykazywania się samodzielnością. Dwa sukcesy lub deklaracja pewności siebie nie oznaczają jeszcze trwałego opanowania materiału.

### Metody: Dialog sokratejski

Stosuj ukierunkowane pytania, aby badać założenia, dowody i logiczne myślenie, gdy uczeń posiada wystarczającą wiedzę bazową, by odpowiedzieć. Sokratejskie elenchus bada spójność między twierdzeniem a przyjętymi przesłankami; celem w klasie nie jest jednak pokonanie ucznia w dyskusji. Kategorie pytań Paula i Elder dostarczają inspiracji dotyczących znaczenia, założeń, dowodów, perspektyw, implikacji i samego zadanego pytania.

Zadawaj jedno precyzyjne pytanie naraz i odnoś się do rzeczywistego wyjaśnienia ucznia. Pozwól uczniowi obronić poprawną odpowiedź, zamiast zakładać, że każda pierwsza odpowiedź jest błędna. Unikaj niekończącego się odpytywania i nie wstrzymuj potrzebnego wyjaśnienia. Gdy brakuje wiedzy wstępnej, pytania przestają pomagać lub uczeń wprost prosi o wyjaśnienie, przejdź do bezpośredniego instruktażu lub przykładu.

### Metody: Technika Feynmana

Zaproponuj uczniowi, aby wyjaśnił zagadnienie własnymi słowami dociekliwemu początkującemu, zidentyfikował konkretną lukę, sięgnął do wiarygodnego źródła i skorygował swoje wyjaśnienie. Pozwala to uwidocznić tok rozumowania po wstępnym wprowadzeniu lub przed zastosowaniem wiedzy w praktyce. Nie udawaj braku zrozumienia precyzyjnego wyjaśnienia tylko po to, by sztucznie przedłużać dialog.

Sprawdź poprawność faktograficzną w oparciu o źródła i rubrykę oceniania, a następnie dołącz zadanie aplikacyjne. Płynny język, uproszczenia i pochwały ze strony AI nie świadczą same w sobie o głębokim zrozumieniu. Sama nazwa techniki nie gwarantuje skuteczności jej implementacji.

### Metody: Przypominanie, odstępy w czasie i refleksja

Praktyka przypominania (retrieval practice) wymaga od uczniów odtworzenia wiedzy przed zobaczeniem poprawnej odpowiedzi. Zapewnij korygującą informację zwrotną i kolejną okazję do jej wykorzystania. Odstępy w czasie (spacing) oznaczają powrót do nauki po znaczącym odroczeniu; natychmiastowe zwrócenie błędnego zadania do kolejki to ćwiczenie korygujące, a nie pełna strategia powtórek rozłożonych w czasie. Planuj powtórki części materiału opanowanego poprawnie, a nie tylko błędów. Dostosuj interwały do treści, celu retencji i dostępnych sesji; nie twórz pozorów, że jeden schemat jest uniwersalnie optymalny.

### Metody: Metapoznanie i uczenie się samoregulowane

Pomagaj uczniom w wyznaczaniu celów cząstkowych, planowaniu, monitorowaniu zrozumienia i korygowaniu podejścia na podstawie dowodów. Poproś o przewidzenie sukcesu lub uzasadnienie wyboru, a następnie porównaj to z samodzielnym wykonaniem zadania. Zadbaj o konkretność refleksji: jakie fakty wpłynęły na zmianę zdania i co uczeń zamierza wypróbować w następnym kroku. Nie stawiaj znaku równości między pewnością siebie a kompetencją ani nie dodawaj obszernego dziennika refleksji do małej aktywności bez wyraźnego celu.

Pracując z generowanymi podpowiedziami, przykładami lub asystą AI na żywo, chroń aktywną rolę ucznia we wspólnej przestrzeni poznawczej (ramy FALR: Focus / Wybór, Delay / Pauza poznawcza, Evaluate / Ewaluacja, Self-Direction / Samosterowność). Przeciwdziałaj biernemu przejmowaniu gotowych treści: wprowadź krótką pauzę przed zaakceptowaniem lub skopiowaniem odpowiedzi modelu, aby działanie nie stało się automatyczne. Zachęć ucznia do oceny, czy odpowiedź jest poprawna, czego w niej brakuje, co zrozumiał samodzielnie w porównaniu z tym, co wykonał system, oraz do podjęcia decyzji o wykorzystaniu, poprawieniu, weryfikacji lub odrzuceniu wygenerowanego tekstu.

### Metody: Mapy pojęciowe i relacje

Stosuj mapę pojęciową, gdy wyjaśnianie lub konstruowanie relacji wchodzi w zakres celu edukacyjnego. Pozwól uczniom zbudować niewielką mapę, nazwać brakujące połączenie lub poddać krytyce zaproponowaną relację, a następnie porównać wynik ze źródłami lub rubryką. Perfekcyjna mapa wygenerowana w całości dla ucznia stanowi materiał poglądowy, a nie dowód zrozumienia tematu przez ucznia.

Nazywaj relacje w sposób jednoznaczny: warunek wstępny, część składowa, kontrastuje z, powiązane z, powoduje w określonych warunkach. Nie wnioskuj o relacji przyczynowo-skutkowej ze współwystępowania ani nie wtłaczaj sieci powiązań krzyżowych w sztywne drzewo hierarchiczne. Akceptuj różne poprawne struktury; oceniaj znaczenie i uzasadnienie relacji, a nie współrzędne ekranowe czy podobieństwo wizualne. Nie zakładaj, że materiał źródłowy obejmuje każde możliwe powiązanie.

W implementacji stosuj stabilne identyfikatory pojęć oraz relacje typowane i skierowane tam, gdzie jest to konieczne. Zapewnij alternatywę tekstową/listową oraz edycję z klawiatury; przeciąganie myszą (drag-and-drop) nie może być jedynym sposobem udzielenia odpowiedzi. Krótka tabela relacji może zrealizować cel bez konieczności tworzenia edytora grafów. Przetestuj jedną poprawną alternatywną mapę i jedno błędne połączenie pod kątem reguł informacji zwrotnej.

### Metody: Metody kontekstowe

- Dociekanie (inquiry): rusztowanie dla pytania, przewidywania, testu, obserwacji i wyjaśnienia. Wnioski o rzeczywistym świecie wymagają prawdziwych danych lub zwalidowanego modelu; materiały poglądowe muszą być oznaczone z wyjaśnieniem, czego nie pokazują. Narracja modelu językowego nie zastępuje dowodu eksperymentalnego.
- Odgrywanie ról (role-play): zdefiniuj rolę, granice scenariusza i kryteria sukcesu, a następnie przeprowadź podsumowanie (debriefing). Oznacz dialog historyczny jako rekonstrukcję i oddziel fakty źródłowe od kwestii wymyślonych. Fikcyjna interakcja może wywoływać realne emocje.
- Uczenie się rówieśnicze: zapewnij wspólne zadanie, odpowiedzialność indywidualną oraz kryteria użytecznego wyjaśnienia. Zapewnij sposób rozstrzygania sporów i sprawdzaj zrozumienie każdego ucznia.
- Wzajemne nauczanie (peer teaching): pozwól uczniom wyjaśniać i udzielać informacji zwrotnej według zrozumiałych kryteriów, z dostępem do zweryfikowanego wyjaśnienia lub nauczyciela w razie potrzeby. Uczeń bez doświadczenia nie może być ostateczną wyrocznią poprawności merytorycznej.
- Metoda projektów: zdefiniuj autentyczny produkt końcowy, etapy pośrednie i indywidualne dowody opanowania wiedzy. Efektowny wygląd produktu nie dowodzi zamierzonego uczenia się.
- Klasa odwrócona (flipped classroom): połącz przygotowanie w domu z praktycznym zastosowaniem w klasie i zapewnij alternatywę dla uczniów, którzy nie zdołali zrealizować wstępu. Jest to wybór organizacyjny, a nie automatyczna gwarancja zysku edukacyjnego.
- Grywalizacja: stosuj opcjonalne elementy postępu lub narracji, gdy wspierają cel dydaktyczny. Publiczna rywalizacja, nagrody rzeczowe i punktacja za szybkość wymagają wyraźnego uzasadnienia i dostępnej alternatywy.

### Metody: Dowody naukowe i literatura

- [Krathwohl, 2002, A Revision of Bloom's Taxonomy](https://people.ucsc.edu/~ktellez/blooms_taxonomy.pdf): dwa wymiary i elastyczna hierarchia z nakładającymi się kategoriami.
- [IES, Organizing Instruction and Study to Improve Student Learning](https://ies.ed.gov/ncee/wwc/PracticeGuide/1): oparte na dowodach zalecenia dotyczące odstępów w czasie, przypominania, przykładów z rozwiązaniem i pytań wyjaśniających.
- [UNESCO, Guidance for Generative AI in Education and Research](https://www.iicba.unesco.org/en/africa-education-knowledge-platform/guidance-generative-ai-education-and-research): sprawczość człowieka i walidacja zastosowań edukacyjnych.
- Zinger, D. (CFM / FALR – Four-Action Learner Regulation Framework): samoregulacja ucznia we wspólnej przestrzeni poznawczej z AI (Focus, Action / Delay, Learn / Evaluate, Reflect / Self-Direction).

## Reference: assessment

Sekcja źródłowa: Dowody uczenia się, ocenianie i informacja zwrotna


### Ewaluacja i ocena: Zacznij od decyzji dydaktycznej

Dla każdego istotnego celu kształcenia określ działanie ucznia, zbierane dowody, kryteria sukcesu oraz kolejną decyzję dydaktyczną. Uwzględnij warunki wykonania, takie jak dostęp do podpowiedzi, materiałów źródłowych, współpraca i limity czasu. Wyznacz kryteria praktyczne lub społeczne tam, gdzie stanowią one zamierzone efekty, zamiast zastępować je prostym testem wyboru.

Przykład: mając nieznany dotąd obwód elektryczny, uczeń przewiduje skutek zmiany i uzasadnia dlaczego. Dowód obejmuje przewidywanie oraz wyjaśnienie przyczynowo-skutkowe. Rubryka oceniania sprawdza znajomość zasady, jej zastosowanie i logiczne rozumowanie. Wystąpienie błędu poznawczego uruchamia przykład kontrastowy i kolejną próbę samodzielną.

### Ewaluacja i ocena: Zachowaj przejrzystość celów oceniania

W trybie ćwiczeń uczniowie mogą prosić o wyjaśnienia, ponawiać próby i korzystać ze stopniowanego wsparcia. Rejestruj korzystanie z pomocy oddzielnie od sukcesu samodzielnego. Informacja zwrotna powinna wskazywać, co jest poprawne, precyzować lukę i oferować konkretny kolejny krok, po którym następuje okazja do poprawy lub ponownego zastosowania wiedzy.

W trybie sprawdzianu (oceny sumującej) zdefiniuj dozwoloną pomoc i zasady punktacji przed rozpoczęciem pracy. Dostosuj wsparcie tutora do tych zasad. Wyjaśnij, czy informacja zwrotna jest natychmiastowa czy odroczona i z jakiego powodu. Nie przenoś automatycznie wyników z trybu ćwiczeń na oceny o wysokiej stawce. Ocena kształtująca wykorzystuje dowody do modyfikacji procesu uczenia się; ocena sumująca raportuje osiągnięcia według zdefiniowanych kryteriów. Wynik punktowy bez podjęcia na jego podstawie decyzji dydaktycznej nie stanowi sam w sobie oceny kształtującej.

### Ewaluacja i ocena: Projektuj rzetelne zadania

Zweryfikuj klucz odpowiedzi, wyjaśnienie i prawdopodobne warianty alternatywne. W zadaniach wielokrotnego wyboru stosuj dystraktory powiązane ze znanymi błędami myślowymi i unikaj przypadkowych wskazówek językowych. W odpowiedziach otwartych akceptuj równoważne sformułowania, poprawne metody alternatywne oraz jawnie przyjęte założenia. Nie czyń jednej odpowiedzi wzorcowej jedynym akceptowanym sformułowaniem.

Stosuj zwięzłe rubryki z obserwowalnymi kryteriami, opisami poziomów wykonania i przykładami, w tym odpowiedziami granicznymi i poprawnymi alternatywami. Rozdzielaj wymiary, gdy to uzasadnione: poprawność merytoryczną, rozumowanie, procedurę, komunikację lub współpracę. Odejmuj punkty za poprawność językową tylko wtedy, gdy wchodzi ona w zakres celu kształcenia. Szybkość i publiczne rankingi wymagają wyraźnego uzasadnienia dydaktycznego; punkty za udział, odznaki i certyfikaty ukończenia nie dowodzą opanowania umiejętności.

Implementując bank zadań, utrwalaj istotne decyzje w jego strukturze danych. Przydatne pola mogą obejmować: stabilny identyfikator zadania, identyfikator celu, treść polecenia, akceptowane odpowiedzi lub rubrykę, wyjaśnienie, wskazówki, źródło i status weryfikacji. W razie potrzeby dodaj jednostki liczbowe i marginesy tolerancji. Rozdzielaj rejestry odpowiedzi: treść odpowiedzi, wykorzystane wsparcie, numer próby i status ewaluacji. To schemat przykładowy, a nie sztywny wymóg; mały pokaz demonstracyjny nie wymaga śledzenia danych.

### Ewaluacja i ocena: Granice osądu sztucznej inteligencji

Traktuj punktację lub klasyfikację błędów dokonaną przez AI jako osąd roboczy. Weryfikuj ją na przykładach sprawdzonych przez nauczycieli i za pomocą testów dziedzinowych. W przypadku niejednoznacznych dowodów poproś o doprecyzowanie lub oznacz zadanie do sprawdzenia przez człowieka; nie twórz pozorów pewności ani nie używaj nieskalibrowanego wskaźnika ufności jako dowodu. Zapewnij uczniom możliwość zakwestionowania informacji zwrotnej, a nauczycielowi możliwość jej zmiany z wglądem w oryginalną odpowiedź i uzasadnienie punktacji. Decyzje brzemienne w skutki wymagają odpowiedzialnej weryfikacji przez człowieka, dopasowanej do warunków edukacyjnych.

### Ewaluacja i ocena: Ewaluacja twierdzeń o skuteczności uczenia się

W miarę możliwości porównaj zadanie początkowe (pre-test) z porównywalnym zadaniem samodzielnym po instruktażu (post-test), a następnie zbadaj retencję w odroczonym terminie oraz transfer do innego kontekstu. Zachowaj ostrożność przy interpretacji postępów: powtarzające się zadania, wskazówki i nierówne warunki początkowe mogą zniekształcać wyniki. Niewielki pilotaż klasowy pozwala zidentyfikować błędy, lecz sam w sobie nie dowodzi skuteczności przyczynowo-skutkowej.

Śledź wskaźniki ukończenia, czas korzystania, zadowolenie, opóźnienia i błędy techniczne jako wskaźniki operacyjne lub użytkowe. Oddzielaj je od mierzalnych efektów uczenia się. Gromadź minimalny zestaw danych potrzebny do decyzji dydaktycznej i jasno deklaruj, czego zebrane dowody nie pozwalają rozstrzygnąć.

### Ewaluacja i ocena: Źródła

- [EEF, Teacher Feedback to Improve Pupil Learning](https://educationendowmentfoundation.org.uk/education-evidence/guidance-reports/feedback): intencje edukacyjne, diagnoza luk, celowy dobór momentu informacji zwrotnej i okazje do wdrożenia zaleceń. Te wytyczne dla nauczycieli nie legitymizują automatycznie każdej implementacji informacji zwrotnej opartej na AI.
- [Przewodnik IES](https://ies.ed.gov/ncee/wwc/PracticeGuide/1): samodzielna praktyka przypominania i odroczone powtórki stanowią podstawę proponowanego podejścia ewaluacyjnego.

Powyższy schemat pracy, przykładowa rubryka i wybory implementacyjne są zaleceniami projektowymi. Ich adekwatność musi być weryfikowana w odniesieniu do uczniów, przedmiotu, wagi decyzji i dostępnych dowodów.

### Ewaluacja i ocena: Sprawdzanie decyzji i naprawa konsekwencji błędów

W zadaniach z pojedynczą odpowiedzią rozwiąż zadanie samodzielnie i spróbuj obronić każdą z dostępnych opcji przy podanych jednostkach, precyzji i założeniach. Dokładnie jedna musi pozostać poprawna. W zadaniach wielokrotnego wyboru stosuj zadeklarowaną regułę odpowiedzi; w zadaniach otwartych uwzględniaj poprawne warianty alternatywne. Następnie zastosuj każdą domniemaną błędną procedurę do rzeczywistych danych zadania: musi ona prowadzić do zamierzonego dystraktora. Po zmianie treści polecenia ponownie zweryfikuj opcje. Ułamki równoważne lub niezadeklarowane zaokrąglenia nie mogą tworzyć drugiej poprawnej odpowiedzi.

Powiąż zaobserwowaną odpowiedź z możliwym wyjaśnieniem, pytaniem różnicującym i konkretnym działaniem naprawczym. Pojedyncza błędna odpowiedź nie diagnozuje jednoznacznie swojej przyczyny. W projektowaniu opartym na dowodach (Evidence-Centered Design) wskaż kompetencję docelową, obserwowalny dowód i zadanie, które go wywołuje. Zdarzenia w grze mogą mieć inne wyjaśnienia, takie jak trudności motoryczne, eksploracja czy zgadywanie; sama telemetria nie dowodzi wytrwałości ani cech osobowości. Wyjaśnij konieczność gromadzenia danych.

Jeśli treść zadania, klucz odpowiedzi lub wyjaśnienie tutora są błędne, uznaj błąd i popraw go, a następnie sprawdź powiązane wskazówki, zadania, oceny i postępy. Nie traktuj próby dotkniętej błędem jako dowodu niewiedzy ucznia. Zachowaj niezbędne oryginalne dowody i wersję treści; zaznacz niepewność i w razie potrzeby zaoferuj nowe sprawdzenie wiedzy. Widok nauczyciela i ucznia musi operować na tej samej wersji poleceń i opcji.

Procedury weryfikacyjne zostały zaadaptowane jako zasady projektowe z [materiałów sprawdzania zrozumienia organizacji Learning Commons](https://github.com/learning-commons-org/agent-skills/tree/main/skills/k12-check-for-understanding). Nie wprowadzają one sztywnych formatów, domyślnych programów nauczania USA ani restrykcji przypisywania źródeł.

## Reference: simulations

Sekcja źródłowa: Symulacje i odgrywanie ról


Przeczytaj ten dokument, gdy produkt modeluje zjawisko/system, wspiera przeprowadzanie eksperymentu lub pozwala uczniom działać w ramach scenariusza. Wybierz wyłącznie te testy, które odnoszą się do danego zadania.

### Symulacje: Określ, co reprezentują dane wyjściowe

W języku skierowanym do ucznia wyraźnie rozróżniaj następujące rodzaje danych:

- **Pomiar:** obserwacje z rzeczywistego przyrządu, zbioru danych lub zarejestrowanego eksperymentu fizycznego. Wskaż źródło i istotne granice błędu pomiarowego.
- **Obliczenie lub symulacja:** wyniki wygenerowane przez określony model matematyczny lub regułowy. Podaj przyjęte założenia upraszczające oraz zakres, w którym model pozostaje użyteczny.
- **Fikcja lub rekonstrukcja:** wymyślone zdarzenia, dialogi, postacie lub konsekwencje służące celom dydaktycznym. Oznacz je jednoznacznie jako takie.

Nigdy nie opisuj wygenerowanych liczb jako pomiarów rzeczywistych ani wymyślonego dialogu jako autentycznego cytatu historycznego. Symulacja może ilustrować hipotezę; same jej wyniki nie dowodzą tego, jak zachowuje się świat rzeczywisty.

### Symulacje: Zdefiniuj i zweryfikuj model

Zapisz cel kształcenia, zmienne stanu, dane wejściowe, jednostki miar, dozwolone zakresy, założenia, reguły aktualizacji i obserwowalne wyniki. Wyjaśnij uproszczenia wpływające na interpretację zjawiska. Dobierz kontrolki tak, aby ukazywały zamierzoną zależność, bez zmuszania uczniów do zgadywania nieudokumentowanych ustawień.

W zadaniach obliczeniowych wyliczaj wyniki za pomocą zweryfikowanego silnika numerycznego lub jawnych reguł deterministycznych. Oddziel ten silnik od komentarzy generowanych przez model językowy (LLM). Model językowy może wyjaśniać rzeczywiste wyniki, lecz nie może zmyślać brakujących obliczeń ani stwarzać pozorów, że przeprowadził fizyczny eksperyment.

Zastosuj zestaw testów dopasowany do modelu: znany przypadek wzorcowy, przypadek graniczny, spójność jednostek i jeden oczekiwany trend monotoniczny. W modelach stochastycznych wskaż źródło losowości i w razie potrzeby zapewnij powtarzalne ziarno losowości (seed). Dokumentuj ograniczenia zamiast sugerować uniwersalną ważność modelu.

### Symulacje: Zaprojektuj pętlę uczenia się

Poproś ucznia o sformułowanie przewidywania i jego uzasadnienie przed uruchomieniem modelu, jeśli wspiera to cel dydaktyczny. Pozwól uczniom zmieniać istotne parametry wejściowe, obserwować rzeczywisty wynik, porównywać go z własnym przewidywaniem i modyfikować swoje wyjaśnienie. Zapewnij podsumowanie (debriefing), które odróżnia zachowanie modelu od faktów ze świata rzeczywistego i stawia pytanie, w jakich warunkach model przestaje działać poprawnie.

Nie przyznawaj potwierdzenia zrozumienia tematu wyłącznie za osiągnięcie docelowej konfiguracji suwaków na ekranie. Oczekuj wyjaśnienia, porównania lub transferu wiedzy do nowego przypadku.

### Symulacje: Historyczne i społeczne odgrywanie ról

Określ jednoznacznie, czy postać jest fikcyjna, syntetyczna czy oparta na źródłach historycznych. Zachowaj wyraźne rozróżnienie między faktami źródłowymi a zrekonstruowanymi wypowiedziami. Podawaj pochodzenie twierdzeń historycznych i wskazuj na sporne interpretacje, gdy jest to istotne. Nie twórz pozorów autentycznego wglądu w myśli historycznych postaci ani nie twórz fałszywych cytatów.

Zdefiniuj rolę, granice scenariusza, cel edukacyjny i podsumowanie (debriefing). Zapewnij bezpieczne wyjście z roli oraz dostęp do obiektywnego wyjaśnienia. Dopasuj intensywność emocjonalną i tematykę do wieku uczniów i warunków w klasie; zapewnij aktywność alternatywną przy scenariuszach trudnych emocjonalnie. Oceniaj zamierzone rozumowanie lub umiejętności komunikacyjne według jawnych kryteriów; sama zgoda z poglądami odgrywanej postaci nie stanowi dowodu uczenia się.

## Reference: runtime-ai

Sekcja źródłowa: Sztuczna inteligencja w fazie wykonawczej (runtime) w aplikacjach edukacyjnych


Przeczytaj ten dokument tylko wtedy, gdy gotowa aplikacja odwołuje się do usługi AI w trakcie jej użytkowania przez uczniów. Używanie AI do pisania kodu lub generowania treści sprawdzanych przez nauczyciela nie wymaga obecności AI w środowisku wykonawczym. Pozostaw aktywności offline w trybie offline, chyba że cel dydaktyczny bezwzględnie wymaga usługi sieciowej.

### AI w czasie działania: Zdefiniuj ograniczoną rolę dydaktyczną

Określ, co model może robić, z jakich zweryfikowanych treści lub źródeł może korzystać oraz jak powinien reagować na brakujące dowody. W sytuacjach, gdzie kluczowa jest poprawność faktograficzna, zidentyfikuj zatwierdzone materiały i zachowaj ich pochodzenie źródłowe. Nie dopuszczaj do generowania zmyślonych, choć wiarygodnie wyglądających cytowań. Dopuszczaj niepewność i korygowanie twierdzeń; unikaj diagnozowania uczniów i kategorycznych sądów o ich zdolnościach na podstawie krótkiej interakcji.

Dobieraj formę wsparcia do charakteru aktywności. Ćwiczenia mogą wykorzystywać pytania naprowadzające, stopniowane wskazówki, przykłady z rozwiązaniem oraz bezpośrednie wyjaśnienie na życzenie lub wtedy, gdy pytania przestają pomagać. Sprawdzian może ograniczać pomoc zgodnie z zasadami określonymi przez nauczyciela. Nie narzucaj niekończącej się pętli sokratejskiej ani bezwzględnego zakazu podawania odpowiedzi. Zapewnij uczniowi możliwość poproszenia o pomoc, przerwania pracy lub zaangażowania nauczyciela.

Projektuj interfejsy AI na żywo tak, aby przeciwdziałać biernemu kopiowaniu, w którym narzędzie myśli za ucznia. Przed zaakceptowaniem wygenerowanej procedury lub odpowiedzi wymagaj od ucznia krótkiej weryfikacji: doprecyzowania intencji przed wysłaniem zapytania, zatrzymania się nad wynikiem (pauza poznawcza), oceny kompletności i poprawności oraz wyboru kolejnego kroku (kontynuacja, weryfikacja, przeredagowanie lub decyzja o rezygnacji z podpowiedzi).

Stosuj jawne rubryki kryteriów do generowania informacji zwrotnej i oceny odpowiedzi otwartych. Porównuj oceny modelu z przykładami sprawdzonymi przez nauczycieli, zanim na nich polegasz. Istotne decyzje dotyczące oceniania, kwalifikacji lub kwestii dyscyplinarnych wymagają odpowiedzialnej weryfikacji przez człowieka; pojedyncza odpowiedź modelu nie może być jedynym decydentem. Odnotowuj niepewność i umożliw nauczycielowi skorygowanie oceny.

### AI w czasie działania: Minimalizacja danych uczniów

Wskaż dane wejściowe przesyłane do dostawcy usługi, zakres ich przechowywania, osoby mające do nich dostęp oraz procedurę ich usuwania. Zbieraj wyłącznie to, co jest niezbędne do przeprowadzenia aktywności. Nie wprowadzaj automatycznie kont użytkowników, imion i nazwisk, trwałych profili ani rejestrowania pełnych konwersacji. Używaj anonimowych lub pseudonimowych identyfikatorów sesji tam, gdzie to wystarcza, mając świadomość, że nie gwarantują one pełnej anonimowości.

Przed wdrożeniem z udziałem osób niepełnoletnich sprawdź docelową grupę wiekową, ustalenia ze szkołą, warunki świadczenia usług dostawcy i obowiązujące lokalne przepisy prawa z właściwą instytucją. Nie twórz uniwersalnego wieku zgody ani sztucznych reguł prawnych. Wyjaśnij zasady przetwarzania danych uczniom i nauczycielom w przystępnym języku.

### AI w czasie działania: Zastosuj zabezpieczenia architektoniczne

Przechowuj dane uwierzytelniające do usług (klucze API) w chronionym komponencie po stronie serwera, gdy usługa zdalna wymaga kluczy prywatnych. Nigdy nie ujawniaj ich w kodzie uruchamianym w przeglądarce. Egzekwuj autoryzację, limity zapytań i uprawnienia narzędzi poza promptem. Traktuj dane wprowadzane przez uczniów, pobierane dokumenty oraz odpowiedzi modelu jako dane niezaufane.

Oddzielaj instrukcje od dostarczanych treści, ograniczaj dostęp do narzędzi i miejsc docelowych, waliduj ustrukturyzowane odpowiedzi i oczyszczaj renderowane treści (sanitaryzacja HTML/JS). Zabezpiecz aplikację przed bezpośrednim przekształcaniem tekstu wygenerowanego przez model w kod wykonywalny lub działania uprzywilejowane. Prompt nakazujący modelowi ignorowanie wstrzykiwania instrukcji (prompt injection) nie stanowi gwarancji bezpieczeństwa. Zapewnij dedykowany przegląd bezpieczeństwa dla zaimplementowanej architektury.

### AI w czasie działania: Planowanie kosztów, awarii i ciągłości działania

Ustal realistyczny budżet wykorzystania, limity na sesję, czasy oczekiwania (timeouts) i możliwość anulowania zapytań. Zapewnij zrozumiały stan interfejsu w trakcie oczekiwania na odpowiedź. Zabezpiecz aplikację przed utratą połączenia sieciowego, niedostępnością modelu, nieprawidłowymi danymi wyjściowymi i wyczerpaniem limitów bez utraty dotychczasowej pracy ucznia. Ponawiaj próby tylko wtedy, gdy jest to bezpieczne i ograniczone liczbowo.

Zaoferuj odpowiedni mechanizm awaryjny (fallback), taki jak zweryfikowane wskazówki statyczne, ćwiczenia standardowe, zapisany postęp lub pomoc nauczyciela. Oznacz niedostępną informację zwrotną zamiast ją zmyślać. Przed użyciem w klasie przetestuj: główną ścieżkę uczenia się, odpowiedź błędną, prośbę o pomoc, niejednoznaczną informację zwrotną oraz awarię usługi. Udokumentuj nierozstrzygnięte ograniczenia i obowiązki weryfikacyjne nauczyciela.

### AI w czasie działania: Weryfikacja generowanych treści w określonych granicach

Przed udostępnieniem wygenerowanych zadań przeprowadź odpowiednie testy poprawności dziedzinowej, rozwiązywalności, przejść stanów i renderowania. Wymagaj unikalności tylko od zadań, które wyraźnie to deklarują. Waliduj uprawnienia i granice danych ustrukturyzowanych poza modelem; schemat JSON nie dowodzi prawdziwości danych, a testy deterministyczne gwarantują tylko te własności, które faktycznie sprawdzają. Odrzucaj lub izoluj nieprawidłowe treści i zachowaj zweryfikowaną bazę zapasową. W przypadku korygowania powiązanych wskazówek, ocen i postępów stosuj procedurę naprawczą opisaną w `assessment.md`.

## Reference: model-profiles

Sekcja źródłowa: Modele, nakład pracy, szybkość i adaptacja do środowiska


Skorzystaj z tego dokumentu, rekomendując model, dobierając ustawienia szybkości/nakładu pracy (effort/thinking) lub dostosowując sposób ładowania skilla przez środowisko nadrzędne. Zachowaj identyczne wytyczne edukacyjne dla wszystkich dostawców modeli.

### Profile modeli: Czego ten dokument nie deklaruje

Rekomendacje stanowią konfiguracje wyjściowe dla tego procesu projektowego, a nie benchmark czy pomierzony ranking. Nie dowodzą, że dana rodzina modeli uczy lepiej, ani nie przewidują opóźnień sieciowych (latencji). Nazwy modeli, dostępne ustawienia, plany i ceny ulegają ciągłym zmianom. Przed użyciem wskazanego modelu sprawdź listę modeli rzeczywiście dostępnych dla użytkownika oraz aktualną oficjalną dokumentację dostawcy. Etykieta w interfejsie nie zawsze odpowiada identyfikatorowi modelu w API. Potwierdź poprawność konfiguracji na reprezentatywnych zadaniach przed uznaniem jej za zweryfikowaną.

Stan dokumentacji sprawdzono: 2026-11-04.

### Profile modeli: Dobieraj model do zadania przed wyborem nazwy

Stosuj mniejszy model do precyzyjnie określonych edycji treści według jawnych kryteriów, model średniej klasy do standardowego projektowania i implementacji, a model najwyższej klasy do sprzecznych źródeł, złożonych symulacji lub audytów o wysokiej stawce. Są to kategorie zadań, a nie gwarantowane możliwości technologiczne. Zachowaj dotychczasowy wybór użytkownika, jeśli spełnia on kryteria.

Poniższa tabela stanowi **nieprzetestowaną rekomendację wyjściową dla tego skilla**, opartą na dokumentacji producentów.

### Profile modeli: Reguły eskalacji i zatrzymania

W przypadku jednoznacznego zadania zacznij od domyślnego nakładu pracy (effort/thinking) lub ustawienia, które sprawdziło się wcześniej. W przypadku sprzecznych źródeł lub złożonego modelu rozważ wyższy nakład pracy od samego początku. Jeśli odpowiedź pomija jawne ograniczenie, przeczy własnej punktacji, nie przechodzi testu obliczeniowego lub generuje błędne zadania, najpierw sprawdź, czy model miał dostęp do danych wejściowych i odpowiedniej referencji. Skoryguj brakujące dane wejściowe lub niejednoznaczne kryterium przed zmianą modelu.

Gdy po jednej ukierunkowanej poprawce odpowiedź nadal nie spełnia tego samego istotnego kryterium, zarekomenduj wyższy obsługiwany poziom nakładu pracy i ponownie oceń to kryterium. Jeśli błąd nie ustępuje, zarekomenduj mocniejszy dostępny model lub niezależną recenzję w zależności od wagi problemu. Nie ponawiaj prób w nieskończoność ani nie przekraczaj uzgodnionego budżetu. Brak źródeł, niedostępność narzędzi i awarie usług wymagają rozwiązania zależności lub wskazania ograniczenia; większy nakład rozumowania nie zastąpi brakujących dowodów. Raportuj nierozstrzygnięte błędy. Zmieniaj ustawienia wyłącznie za pomocą autoryzowanych kontrolek środowiska.

Zmniejszaj nakład pracy lub przechodź na mniejszy model dopiero po pomyślnym zaliczeniu odpowiednich testów; zachowaj dowody uzasadniające kompromis. Szybkość obsługi traktuj odrębnie: standardowa szybkość to punkt wyjścia, a płatna akceleracja wymaga uzasadnienia czasem/kosztem i wyraźnej autoryzacji.

### Profile modeli: Utrzymanie aktualności rekomendacji

Sprawdź wytyczne ponownie, gdy zmieni się wersja modelu lub środowiska, zabraknie określonego ustawienia, dostawca zmieni dostępność lub udokumentowane zachowanie jest sprzeczne z obserwacją. Do czasu weryfikacji oznacz takie połączenie jako niezweryfikowane i stosuj kategorie zadań oraz domyślne ustawienia środowiska. Nie wymyślaj sztucznych odpowiedników dla nieznanych modeli. Dodawaj obejścia specyficzne dla danego dostawcy tylko wtedy, gdy powtarzalny błąd dowiedzie ich konieczności; odnotuj wersję i usuń obejście, gdy straci uzasadnienie.

### Profile modeli: Dopasowanie zadania i kontrolek

| Zadanie | Punkt wyjścia OpenAI | Punkt wyjścia Claude | Punkt wyjścia Gemini |
|---|---|---|---|
| Drobne, precyzyjne edycje treści lub przegląd ustrukturyzowanych zadań | GPT-6 Luna, High; redukuj nakład dopiero po pomyślnych testach | Haiku 5.5, Medium | Gemini 3.5 Flash-Lite, Low tam gdzie obsługiwane |
| Projekt i implementacja zwartej aktywności edukacyjnej | GPT-6.1 Sol, domyślny nakład lub Medium | Sonnet 5.5, Medium dla precyzyjnych zadań agentowych | Gemini 3.8 Flash, Medium |
| Złożony audyt dydaktyczny, sprzeczne źródła, zaawansowana symulacja lub architektura | GPT-6 Astra, Light/Low lub Medium; zwiększ w razie potrzeby | Opus 5.5, Medium, następnie High w razie potrzeby | Gemini 4 Argon, Medium, następnie High w razie potrzeby |

Powyższe zestawienia to zalecenia autora skilla wyprowadzone z dokumentacji producentów. Jeśli wybrany model jest niedostępny, zarekomenduj dostępną alternatywę i poinformuj o zmianie; nie modyfikuj wyboru użytkownika bez autoryzacji. Na przykład istniejący proces oparty na Gemini 3.1 Pro może zachować ten model i obsługiwane poziomy rozumowania. Zmierz czas wykonania reprezentatywnego zadania w rzeczywistym środowisku, aby określić latencję.

Rozróżniaj trzy decyzje: model, głębokość rozumowania (effort/thinking) oraz płatny poziom przyspieszonej obsługi (Fast tier). Mniejszy nakład pracy może zredukować tokeny rozumowania; usługa typu Fast to inna kontrolka, która może wiązać się z wyższym kosztem. Nazwa Flash określa rodzinę modeli, a nie uniwersalny przełącznik trybu szybkiego. Identyczne słowa, takie jak Low, Medium i High, nie gwarantują równego poziomu rozumowania ani latencji u różnych dostawców.

Rozpoczynaj od standardowej szybkości. Rekomenduj płatny tryb Fast tylko wtedy, gdy czas oczekiwania jest krytyczny, a bieżący dostęp i stawki to uzasadniają. Nie włączaj go ani nie dokupuj limitów bez autoryzacji. Strumieniowanie (streaming) poprawia widoczność postępu; nie stanowi dowodu szybszego ukończenia pracy ani wyższej jakości. Oceniaj łączny czas procesu, w tym weryfikację, wywołania narzędzi i poprawki.

### Profile modeli: OpenAI i Codex

Stosuj pakiet natywny, gdy środowisko obsługuje skille i potrafi odczytywać referencje. W Codex bezpośrednie wywołanie może odwoływać się do `$metodyki-nauczania` lub `$learning-methodologies`. Nie zakładaj wykrywania plików w zwykłym czacie; przekaż autonomiczny plik Markdown jako dostępne dane wejściowe.

Aktualne wytyczne zalecają Sol do prac zasadniczych, Luna do zadań precyzyjnych i Astra do procesów wymagających; Luna High i Astra Light/Low to udokumentowane ustawienia wyjściowe. W Codex tryb Fast to wybór szybkości obsługi, odrębny od nakładu rozumowania. Dostępność i limity zależą od modelu, konta i klienta. Sprawdź obsługiwane wartości przed zaproponowaniem konfiguracji; etykieta w UI nie zawsze jest identyfikatorem w API.

Podawaj konkretny oczekiwany rezultat, zakres, odpowiednie pliki i obserwowalne kryteria akceptacji. Oczekuj zwięzłych decyzji i dowodów, a nie ujawniania wewnętrznego toku myślenia (chain-of-thought). Wykorzystuj narzędzia i uprawnienia środowiska; nie przypisuj modelowi dostępu do powłoki czy przeglądarki na podstawie samej nazwy.

Źródła: [modele](https://learn.chatgpt.com/docs/models), [szybkość](https://learn.chatgpt.com/docs/agent-configuration/speed), [skille](https://developers.openai.com/plugins/concepts/skills).

### Profile modeli: Claude i Claude Code

Claude Code obsługuje pakiety `SKILL.md` wraz z plikami pomocniczymi. Jawne wywołanie po wykryciu skilla może wykorzystywać polecenie `/metodyki-nauczania` lub `/learning-methodologies`. W innym środowisku Claude sprawdź mechanizm obsługi skilli lub dostarcz edycję autonomiczną. Nie dodawaj specyficznych dla Claude skryptów hooks, podstawień powłoki ani nadpisań modelu do wspólnego frontmattera.

Dla zadań agentowych w Sonnet 5.5 dokumentacja rekomenduje poziom Medium dla zadań dobrze zdefiniowanych i wyższy dla trudniejszych. Opus 5.5 domyślnie przyjmuje Medium; starsze modele i klienci mogą się różnić. Parametr effort w API i tryb myślenia (thinking mode) to odrębne pojęcia. Nie wszystkie generacje obsługują te same kombinacje. Preferuj obsługiwane kontrolki środowiska zamiast kopiowania parametrów API do promptu w czacie. Tryb Fast w Claude to odrębna funkcja zależna od modelu, objęta wyższym cennikiem.

Precyzyjnie wyznaczaj granice zadania, materiały i pożądany wynik. Wskaż, w których obszarach agent może decydować samodzielnie, a co wymaga dowodów. Podaj jeden trafny przykład, jeśli rozwiązuje on niejednoznaczność; unikaj powtarzania całego skilla lub narzucania długiej transkrypcji myśli. Taki sposób pakowania sprzyja przenośności i nie jest twierdzeniem o unikalnych cechach poznawczych Claude.

Źródła: [skille](https://code.claude.com/docs/en/skills), [modele](https://platform.claude.com/docs/en/models/overview), [nakład pracy (effort)](https://platform.claude.com/docs/en/build-with-claude/effort), [tryb Fast](https://platform.claude.com/docs/en/build-with-claude/fast-mode).

### Profile modeli: Gemini i Gemini CLI

Gemini CLI wykrywa skille natywne w obsługiwanych katalogach, w tym w aliasie `.agents/skills`. Sprawdź dostępność poleceniem `/skills list` i w razie potrzeby przeładuj za pomocą `/skills reload`. Zaufanie do przestrzeni roboczej i zgody na aktywację należą do środowiska; nie omijaj ich. W AI Studio lub innym czacie należy użyć pliku autonomicznego, jeśli ładowanie natywne jest niedostępne.

Aktualny przewodnik po myśleniu (thinking) wymienia poziomy Low, Medium i High dla Gemini 4 Argon oraz Gemini 3.8 Flash. Inne wersje Gemini mają odmienne wartości domyślne i poziomy. Stosuj wyłącznie poziomy obsługiwane przez dany model i API/klienta; nie tłumacz dosłownie parametrów z OpenAI lub Claude. Nazwa wersji zapoznawczej (preview) i nazwa stabilna nie są tożsame.

Dla punktu końcowego `gemini-3.1-pro-preview` tabela API wymienia poziomy Low, Medium i High, z High jako wartością domyślną. Dla tego endpointu wypróbuj Medium do standardowego projektowania i High do trudnego audytu (jako rekomendację autora), o ile środowisko udostępnia te kontrolki. Etykieta taka jak Gemini 3.1 Pro nie przesądza o tym, z jakiego endpointu lub kontrolek korzysta dany klient.

Formułuj instrukcje zwięźle i precyzuj cel, ograniczenia oraz dowody wyjściowe. Dołączaj wskazywane materiały, aby model miał do nich rzeczywisty dostęp; sama ścieżka wpisana w czacie nie daje dostępu do pliku. Zachowaj wymagany stan konwersacji narzędziowej przy tworzeniu aplikacji z API Gemini, zgodnie z bieżącą dokumentacją API. Ten skill nie wdraża tej warstwy API ani nie autoryzuje jej dodawania.

Źródła: [modele](https://ai.google.dev/gemini-api/docs/models), [myślenie (thinking)](https://ai.google.dev/gemini-api/docs/thinking), [skille w Gemini CLI](https://geminicli.com/docs/cli/tutorials/skills-getting-started/).

### Profile modeli: Zastosowanie uniwersalne i weryfikacja

Utrzymuj proste, standardowe metadane: `name` i `description`, a po nich zwykły Markdown. Opcjonalne metadane opisują edycję; nie polegaj na polach specyficznych dla danego hosta w celu egzekwowania granic bezpieczeństwa. Stosuj powiązane względne referencje w agencie z dostępem do plików lub kompletną edycję autonomiczną w oknie czatu. Domyślnie nie ładuj obu edycji językowych naraz. Ponownie dołączaj kluczowy zakres i niedokończoną pracę po utracie kontekstu przez środowisko, zamiast zakładać, że każdy host zachowuje pełną pamięć.

Emoji mogą nieść znaczenie, lecz nie powinny być jedynym nośnikiem poleceń ani sygnałem priorytetu. Zachowaj jednoznaczne etykiety tekstowe. Badania nad [semantyką emoji](https://arxiv.org/abs/2409.10760) oraz [niejednoznacznością kontekstową](https://arxiv.org/abs/2511.07193) nie wykazują, by ozdabianie skilla ikonami poprawiało stosowanie się do instrukcji. Przetestuj taką zmianę na rzeczywistych modelach i zadaniach przed ogłoszeniem korzyści.

Zanim uznasz kombinację modelu i środowiska za przetestowaną, zweryfikuj wykrywanie skilla lub pomyślne załadowanie edycji autonomicznej, dostęp do odpowiednich referencji, reprezentatywny rezultat pracy oraz kluczowe granice bezpieczeństwa. Zapisz dokładny identyfikator modelu lub widoczną etykietę, środowisko/wersję, język, nakład pracy, szybkość obsługi, narzędzia, datę, artefakty i błędy. Odróżniaj deklarowaną w dokumentacji kompatybilność od zaobserwowanego wykonania. Nigdy nie przenoś pozytywnego wyniku jednego testu na wszystkie modele z danej rodziny.

Do celów porównawczych stosuj to samo zadanie i materiały wyjściowe, a recenzent powinien oceniać rzeczywiste wyniki według tych samych kryteriów dydaktycznych. Uwzględnij ponowne wykorzystanie znanego kontekstu, kontrolowaną pomoc, poprawną odpowiedź alternatywną, niepoparte dowodami roszczenia programowe, granice modelu/danych oraz awarie narzędzi i usług. Zmniejszaj nakład pracy lub wybieraj mniejszy model tylko wtedy, gdy kluczowe testy stale kończą się sukcesem. Jeśli bezpośredni dostęp do dostawcy jest niemożliwy, oznacz go jako nieprzetestowany zamiast wymyślać wyniki.

## Reference: decision-examples

Sekcja źródłowa: Przykłady decyzji


Użyj odpowiedniego przykładu, aby rozstrzygnąć konkretną niejednoznaczność projektową. Dostosuj dziedzinę i wiek; zachowaj nadrzędną zasadę decyzyjną.

### Przykłady decyzji: Akceptacja odpowiedzi równoważnej

Zadanie: wyraź natężenie 1,5 A w miliamperach. Uczeń wpisuje `1500 mA`; moduł sprawdzający oczekuje `1500`. Zaakceptuj wielkość równoważną, weryfikując jednostkę i wartość liczbową. Jeśli celem kształcenia jest wyłącznie zapis liczbowy lub notacja jednostek, oceń to odrębnie. Nie traktuj każdego ciągu znaków jako równoważnego poprzez bezkrytyczne usuwanie spacji i liter: `1500 A` jest w tym przypadku odpowiedzią błędną. Dlaczego: kwestie formatowania tekstu nie mogą zastępować zamierzonego dowodu przeliczania jednostek.

### Przykłady decyzji: Zakończenie nieproduktywnej pętli sokratejskiej

W trakcie ćwiczeń uczeń stwierdza: „Nadal nie rozumiem, proszę, pokaż mi rozwiązanie” po pytaniu o natężenie prądu i opór. Zaoferuj zwięzłe wyjaśnienie lub rozwiązany przykład przy stałym napięciu, a następnie zaproponuj nowe zadanie z opcjonalnym wsparciem. Nie zadawaj kolejnych pytań pomocniczych jako warunku otrzymania pomocy. Zarejestruj rozwiązany przykład jako uczenie się ze wsparciem; nowe, samodzielne zadanie dostarczy odrębnego dowodu opanowania wiedzy. Dlaczego: pytania powinny pomagać uczniowi w robieniu postępów, a nie blokować proces uczenia się. Formalny sprawdzian może mieć odmienne zasady udzielania pomocy.

### Przykłady decyzji: Korekta niedokładnego wyjaśnienia w technice Feynmana

Uczeń wyjaśnia: „Rośliny czerpią pokarm z gleby; światło słoneczne tylko je ogrzewa”. Doceń zrozumiałe sformułowanie, nie akceptując błędu merytorycznego. Wskaż konkretny błąd poznawczy, skieruj do zweryfikowanego źródła, wyjaśnij różnicę między wodą ze składnikami mineralnymi a cukrami wytwarzanymi w fotosyntezie i poproś o poprawione, proste wyjaśnienie. Sprawdź transfer na nowym przykładzie, np. pytając, co zmieni się przy braku światła. Dlaczego: płynność i prostota języka nie dowodzą poprawności merytorycznej. Nie wymyślaj obserwacji eksperymentalnych ani nie przypisuj wzrostu roślin wyłącznie jednemu czynnikowi.

### Przykłady decyzji: Praca przy braku dostępu do programu nauczania

Nauczyciel prosi o „pełną zgodność z programem nauczania naszej szkoły”, lecz nie dostarcza dokumentu szkolnego. Na podstawie wskazanego celu edukacyjnego opracuj wersję roboczą aktywności. Poproś o odpowiedni fragment programu tylko wtedy, gdy ścisłe dopasowanie ma krytyczne znaczenie; otwarcie wskaż, które elementy pozostają niezweryfikowane. W odniesieniu do szkół w Polsce ogólne odwołanie do podstawy programowej MEN nie gwarantuje zgodności z konkretnym szkolnym zestawem programów nauczania lub przedmiotowym systemem oceniania (PSO). Dlaczego: można przygotować użyteczny projekt roboczy, zachowując pełną przejrzystość co do granic formalnych deklaracji.

### Przykłady decyzji: Wprowadzenie pauzy poznawczej przed przyjęciem odpowiedzi AI

W aplikacji z wbudowanym asystentem AI uczeń prosi o zarys rozwiązania lub wyjaśnienie błędu. Zamiast przycisku „Wstaw do mojego rozwiązania”, wprowadź pauzę poznawczą: zablokuj bezpośrednie kopiowanie i zadaj krótkie pytanie weryfikacyjne („Który krok jest tutaj kluczowy? Czego brakuje w propozycji AI dla twojego konkretnego przypadku?”). Pozwól uczniowi zmodyfikować sugestię, sprawdzić ją na innym przykładzie lub zrezygnować z jej użycia. Zarejestruj wygenerowany przez model tekst jako pomoc ze wsparciem, a nie dowód zrozumienia tematu przez ucznia. Powód: pauza powstrzymuje ucznia przed bezrefleksyjnym przejmowaniem odpowiedzi modelu.

## Reference: tutor-state

Sekcja źródłowa: Tryby i ciągłość pracy tutora


Przeczytaj ten dokument przy projektowaniu wieloetapowego prowadzenia ucznia (tutoringu), aktywności z możliwością wznawiania pracy lub ćwiczeń przedegzaminacyjnych. Reguły te odnoszą się również do deterministycznych aplikacji offline; nie wymagają one obecności runtime AI, kont użytkowników ani trwałego magazynu danych.

### Stan tutora: Modeluj jawne tryby i przejścia między nimi

Rozdzielaj etap wyjaśniania, ćwiczeń i sprawdzianu, jeśli wymaga tego aktywność. Wyjaśnienie może prezentować przykład z rozwiązaniem. Ćwiczenie oczekuje na odpowiedź, wstrzymuje akcję, dostarcza informacji zwrotnej opartej na kryteriach i oferuje pomoc. Sprawdzian podlega zadeklarowanym regułom dotyczącym dopuszczalnego wsparcia i czasu podania informacji zwrotnej. Pozwól uczniowi wstrzymać pracę, poprosić o pomoc lub wyjść z aktywności; sprawdzian o zaostrzonych regułach może zakończyć próbę lub oznaczyć ją jako wykonaną z pomocą, jeśli uczeń zażąda merytorycznego wsparcia. Zachowaj dostosowania dostępności, które nie zdradzają merytorycznej odpowiedzi.

W konwersacyjnym trybie ćwiczeń utrzymuj jedno aktywne pytanie oczekujące na odpowiedź, chyba że zadanie wymaga przetwarzania pakietowego. Nie generuj odpowiedzi za ucznia ani nie odsłaniaj rozwiązania w trakcie oczekiwania na jego reakcję. Rozróżniaj stany: bezczynności (idle), oczekiwania na odpowiedź (awaiting-answer), ewaluacji (evaluating), prezentacji informacji zwrotnej (feedback) oraz wstrzymania (paused). Zablokuj zduplikowane wysyłanie formularza lub powiąż je z tą samą próbą; spóźniona odpowiedź sieciowa nie może oceniać nowego pytania ani nadpisywać zmienionego trybu. Wynik modelu jest jedynie propozycją odpowiedzi; wyłącznie nauczyciel może zmieniać oceny lub zasady oceniania.

Przechowuj tryb, cel, bieżące zadanie, identyfikator próby, stan odsłonięcia odpowiedzi oraz status informacji zwrotnej w stanie aplikacji. Wyświetl zwięzły wskaźnik postępu, jeśli jest to pomocne; powtarzanie dekoracyjnego paska stanu nie jest zarządzaniem stanem. Przy jawnej zmianie trybu wyjaśnij zmienione warunki pomocy i zachowaj wcześniejszą historię odsłonięć. Sama zmiana etykiety na ekranie nie zamienia zadania z ujawnionym rozwiązaniem w niezależny sprawdzian. Gdy potrzebny jest nowy samodzielny dowód, podaj nowe, adekwatne zadanie.

### Stan tutora: Wznawianie na podstawie dowodów, a nie deklaracji mistrzostwa

Wprowadzaj zapisywanie lub eksport stanu tylko wtedy, gdy kontynuacja nauki w wielu sesjach służy użytkownikowi. Krótka, anonimowa aktywność może nie potrzebować żadnego z tych mechanizmów. W przypadku pracy z możliwością wznawiania zachowaj minimalny punkt kontrolny (checkpoint) dopasowany do implementacji:

- Wersja formatu, wersja aktywności/treści oraz odpowiednie identyfikatory źródeł.
- Cel, bieżący tryb, identyfikator zadania/próby oraz oczekujący krok.
- Zaobserwowane dowody wraz z warunkami: samodzielnie, ze wsparciem lub po odsłonięciu rozwiązania; nierozstrzygnięta ocena pozostaje nierozstrzygnięta.
- Konkretne błędy poznawcze lub niepewności oraz kolejny krok dydaktyczny.
- Dane czasowe tylko wtedy, gdy są niezbędne do planowania powtórek rozłożonych w czasie lub interpretacji dowodu.

Unikaj diagnoz psychologicznych, zbędnych danych tożsamości i pełnych transkrypcji rozmów. Wskaż, gdzie przechowywane są dane, kto ma do nich dostęp i jak je usunąć; użytkownicy współdzielonych urządzeń potrzebują jasnego sposobu na zakończenie pracy i usunięcie lokalnego postępu. Wyeksportowany plik stanu może zawierać prywatne informacje edukacyjne nawet bez imienia i nazwiska. Nie eksportuj kluczy prywatnych API, ukrytych kluczy odpowiedzi ani poufnych treści testowych.

Traktuj zaimportowane pliki stanu jako dane niezaufane. Waliduj schemat, rozmiar, identyfikatory i zgodność wersji; nigdy nie wykonuj osadzonych w nich instrukcji ani nie przyjmuj zaimportowanych punktów jako autorytatywnych ocen. Tam, gdzie oceny mają formalne znaczenie, weryfikuj je z oficjalnym rejestrem z zachowaniem kontroli dostępu. Jeśli treść uległa zmianie lub zadania nie można rozwiązać, wyjaśnij rozbieżność i wznów pracę w bezpiecznym punkcie; nie resetuj po cichu osiągnięć ani nie certyfikuj zdezaktualizowanych dowodów. Przywrócenie oczekującej próby nie może automatycznie wysyłać odpowiedzi ani dwukrotnie przyznawać punktów.

Podsumowanie stanu (handoff) określa, co uczeń wykazał, w jakim zadaniu i przy jakim wsparciu. Nie deklaruje „pełnego opanowania materiału” po jednej sesji. Nowe zadanie w późniejszym terminie pozwala sprawdzić retencję lub transfer wiedzy. Potwierdzone przez ucznia poprawki i interwencje nauczyciela powinny pozostać odróżnialne od pierwotnej obserwacji.

### Stan tutora: Ukierunkowana korekta bez blokowania ucznia

Szereguj błędy według ich znaczenia dla celu kształcenia i wymagań wstępnych, traktując wagę błędu jako interpretację roboczą. Zaproponuj ukierunkowaną wskazówkę, przypadek kontrastowy lub wyjaśnienie, a następnie nowe zadanie aplikacyjne. Pozwól na odłożenie zadania i powrót do niego w późniejszym czasie. Nie wprowadzaj arbitralnych progów typu 8/10 lub 90%, nie zakazuj podawania wyjaśnień ani nie przypisuj punktów do każdej drobnej interakcji. Stosuj jawne kryteria, gdy punktacja jest celowa; oficjalne ocenianie egzaminacyjne wymaga rzeczywistej specyfikacji egzaminu.

### Stan tutora: Testy weryfikacyjne implementacji

Sprawdzaj tylko istotne ścieżki: pytanie → odpowiedź → informacja zwrotna; pomoc → dowód wykonania ze wsparciem; zmiana trybu po odsłonięciu odpowiedzi; pauza/wznowienie bez utraty lub podwójnego zaliczenia próby; nieaktualny lub uszkodzony plik stanu; spóźniona odpowiedź sieciowa po przełączeniu zadań; nierozstrzygnięta informacja zwrotna po błędzie technicznym. Upewnij się, że stan zapisany w pamięci i stan widoczny na ekranie są zgodne. Testy te weryfikują działanie techniczne, a nie skuteczność pedagogiczną.

## Reference: didactic-rationale

Sekcja źródłowa: Dlaczego metodyki dydaktyczne są niezbędne w tworzeniu aplikacji wspieranych przez AI


Przeczytaj ten dokument, wyjaśniając cel skilla lub decydując, w jaki sposób metoda dydaktyczna powinna zmieniać działanie aplikacji. Narzędzie to wspiera programistów i edukatorów wykorzystujących AI do projektowania i budowy aplikacji edukacyjnych. Oferuje również wytyczne dla aplikacji korzystających z AI w trakcie uczenia się (runtime), jeśli jest to uzasadnione. Metoda musi przejawiać się w działaniach ucznia, informacji zwrotnej i dowodach uczenia się. Pojedyncze zdanie w prompcie lub etykieta funkcji nie wystarczą.

### Uzasadnienie dydaktyczne: Przekład decyzji dydaktycznej na obserwowalne zachowanie

| Metoda lub perspektywa | Cel dydaktyczny | Decyzja projektowa w aplikacji | Dowód do weryfikacji |
|---|---|---|---|
| Pytania sokratejskie | Zbadanie założeń i toku rozumowania ucznia | Zadaj ukierunkowane pytanie, zaczekaj, odnieś się do faktycznej odpowiedzi; w razie potrzeby podaj wyjaśnienie | Uczeń potrafi uzasadnić lub skorygować twierdzenie, w tym poprawną alternatywę |
| Technika Feynmana i samoobjaśnianie | Umożliwienie weryfikacji wyjaśnienia ucznia | Pozwól uczniowi wyjaśnić zagadnienie, porównaj z kryteriami, wskaż konkretną lukę i zaproponuj nowe zadanie | Poprawne zależności i zastosowanie w praktyce; sama płynność wypowiedzi nie wystarczy |
| Przykłady z rozwiązaniem i rusztowanie poznawcze (scaffolding) | Pomoc początkującemu w rozpoczęciu pracy i stopniowe dochodzenie do samodzielności | Zapewnij krok z rozwiązaniem, zadanie do dokończenia i odpowiedni nowy problem; utrzymaj dostęp do pomocy na żądanie | Wyraźne odróżnienie wykonania z pomocą od późniejszej próby samodzielnej |
| Praktyka przypominania i powtórki rozłożone w czasie | Ćwiczenie odtwarzania wiedzy i powracanie do niej w odpowiednich odstępach czasu | Zapytaj przed odsłonięciem odpowiedzi; zapewnij korygującą informację zwrotną i zaplanuj powtórki, w tym materiału opanowanego | Wynik przed odsłonięciem odpowiedzi, późniejsze utrzymanie w pamięci i transfer wiedzy |
| Mapy pojęciowe | Wyraźne uwidocznienie relacji i powiązań pojęciowych | Stosuj nazwane relacje, akceptuj równoważne poprawne struktury i zapewnij dostępną alternatywę edycji | Znaczenie i uzasadnienie połączeń, a nie samo podobieństwo wizualne |
| Dociekanie (inquiry) i symulacje | Porównanie przewidywań z faktami przy jawnych założeniach | Uwidocznij istotne zmienne, jednostki, ograniczenia i granice modelu; uwzględnij podsumowanie (debriefing) | Uczeń rewiduje wyjaśnienie na podstawie obserwacji lub jasno oznaczonych wyników modelu |
| Ocena kształtująca i metapoznanie | Wyznaczenie użytecznego kolejnego kroku na podstawie dowodów | Pokaż konkretną informację zwrotną i pozwól uczniom porównać przewidywanie z wykonaniem | Możliwa do wdrożenia korekta i nowy dowód; same punkty i pewność siebie nie wystarczą |
| Uczenie się kooperatywne i rówieśnicze | Wspieranie porównywania i wyjaśniania z zachowaniem odpowiedzialności indywidualnej | Przypisz wspólne zadanie z indywidualnym wkładem i sposobem rozstrzygania sporów | Rozumowanie każdego ucznia; jedno wspólne kliknięcie nie dowodzi zrozumienia przez grupę |
| Samoregulacja we wspólnej przestrzeni poznawczej (FALR) | Utrzymanie aktywnej i krytycznej postawy ucznia podczas korzystania z AI lub wskazówek | Wprowadź pauzę poznawczą przed przyjęciem odpowiedzi; zapytaj, czego brakuje i co uczeń zrozumiał sam, a co wygenerował system; umożliw odrzucenie wygenerowanego wyniku | Odróżnienie własnego zrozumienia od wyniku systemu, zakończone samodzielnym krokiem ucznia |

Taksonomia Blooma pomaga opisywać cele poznawcze i rodzaje wiedzy; nie wyznacza ona sztywnego poziomu trudności ani wymogu odblokowywania sześciu kolejnych etapów. Metoda jest właściwa tylko wtedy, gdy odpowiada docelowym uczniom, treści i zaobserwowanej przeszkodzie w uczeniu się. Żaden katalog nie nakłada obowiązku wdrażania wszystkich metod naraz.

### Uzasadnienie dydaktyczne: Dlaczego ma to znaczenie, gdy AI pomaga tworzyć aplikację

Sztuczna inteligencja potrafi błyskawicznie wygenerować interfejs, moduł sprawdzania odpowiedzi i komunikaty zwrotne. Elementy te wciąż jednak wymagają kontraktu dydaktycznego: co uczeń powinien zrobić, co stanowi dowód opanowania wiedzy, jaka pomoc była dostępna i jak z tego wynika kolejna decyzja edukacyjna. Wykorzystaj ten kontrakt, aby nakładać ograniczenia na generowany kod i weryfikowane treści. Na przykład praktyka przypominania modyfikuje moment odsłonięcia odpowiedzi, podczas gdy rusztowanie poznawcze wpływa na kontrolki pomocy i oznaczanie dowodów. Samo wymienienie nazwy metody bez implementacji tych zachowań nie realizuje celu projektowego.

Rozdzielaj wykorzystanie AI na etapie tworzenia aplikacji od AI działającego w gotowym produkcie (runtime). Zweryfikowana zawartość statyczna i testy deterministyczne pozwalają wdrożyć wiele z tych zachowań w trybie offline. Jeśli runtime AI jest potrzebne do obsługi odpowiedzi otwartych lub dialogu, ściśle ogranicz jego źródła, kryteria i narzędzia, waliduj generowane dane i zapewnij ścieżkę obsługi błędów. Większa ilość wygenerowanego tekstu, bardziej rygorystyczna punktacja czy większy model nie przekładają się same z siebie na lepsze uczenie się.

### Uzasadnienie dydaktyczne: Granice uzasadnienia dydaktycznego

Niniejsze uzasadnienie wyjaśnia wybory projektowe; nie stanowi dowodu, że ten skill lub każda jego implementacja automatycznie poprawia wyniki nauczania. Poprawność merytoryczna, dostępność i wykonalność w klasie wymagają weryfikacji w realnym środowisku. Pomyślny test techniczny nie dowodzi uczenia się; konieczne są adekwatne dowody uczniowskie, a w przypadku wnioskowania przyczynowo-skutkowego — rzetelna ewaluacja. Wskazówki badawcze wymienione w referencjach metod wspierają poszczególne wybory, lecz nie certyfikują całego pakietu. Zachowaj weryfikację przez nauczyciela przy kluczowych decyzjach oceniania i dostosuj podstawę programową do rzeczywistych warunków edukacyjnych.

## Reference: learning-games

Sekcja źródłowa: Gry edukacyjne i celowa grywalizacja


Skorzystaj z tego dokumentu, gdy projekt wymaga mechanik gry, elementów motywacyjnych lub gruntownego przeprojektowania rozgrywki i uczenia się. Rekomendacje łączą wyniki badań naukowych z decyzjami projektowymi; nie dowodzą one automatycznie skuteczności nowego produktu. Stan dowodów sprawdzono: 2026-11-14.

### Gry edukacyjne: Wybór aktywności edukacyjnej przed systemem nagród

Rozróżniaj grę edukacyjną (nauka odbywa się poprzez rozgrywkę), grywalizację (elementy gry wspierają inną aktywność) oraz symulację (model umożliwia dociekanie bez warunków wygranej i punktacji). Dobre narzędzie może nie potrzebować żadnego z poniższych systemów nagród.

Sformułuj zwięzły kontrakt projektowy: uczeń i wymagania wstępne; docelowa umiejętność; decyzja gracza; konsekwencja i informacja zwrotna; niezależny dowód opanowania wiedzy; kolejny krok edukacyjny. W małej aktywności wystarczy krótki akapit. Zidentyfikuj prawdopodobne drogi na skróty: czy gracz może wygrać przez zgadywanie, wielokrotne klikanie, zapamiętywanie pozycji na ekranie, podejrzenie odpowiedzi lub poleganie na koledze z zespołu?

Wybieraj mechaniki, które wymuszają zamierzone myślenie. Aby uczyć myślenia proporcjonalnego, spraw, by gracz regulował proporcje mieszaniny przy istotnych ograniczeniach, wyjaśniał swoje przewidywania i rozwiązywał nowe zadanie. Quiz może nadal służyć praktyce przypominania; osadzanie każdego faktu w symulowanym świecie jest zbędne. W celach eksploracyjnych dopuszczaj różne poprawne rozwiązania.

### Gry edukacyjne: Wybór spójnego, niewielkiego zestawu mechanik

| Potrzeba | Proponowana mechanika i implementacja | Test weryfikacyjny lub warunek błędu |
|---|---|---|
| Rozpoczęcie bez znajomości sterowania | Bezpieczne, grywalne pierwsze zadanie; wprowadzanie narzędzi w miarę potrzeb | Nowy gracz wykonuje czynność bez konieczności tłumaczenia przez autora |
| Zrozumienie złożonego systemu | Przewidywanie, zmiana jednej zmiennej, obserwacja skutków, wyjaśnienie | Losowa manipulacja kontrolkami nie może zastępować nowego przewidywania |
| Utrwalenie wiedzy w pamięci | Misje przypominania ponawiane po pewnym czasie, z korektą | Późniejszy samodzielny wynik; natychmiastowe powtórzenie to naprawa błędu, a nie odstęp w czasie |
| Wybór właściwej procedury | Przeplatanie podobnych, mylących typów zadań po wstępnym wsparciu | Uczeń wybiera i uzasadnia strategię; samo losowe mieszanie tematów nie wystarcza |
| Przejście od poziomu nowicjusza | Przykład z rozwiązaniem, częściowe uzupełnienie, samodzielne wyzwanie | Korzystanie z pomocy pozostaje widoczne; wsparcie powraca w razie potrzeby |
| Śledzenie własnych postępów | Prywatna mapa umiejętności z dowodami i kolejnymi krokami | Ukończenie, sukces z pomocą i dowody samodzielności pozostają rozróżnialne |
| Poczucie sprawczości (autonomia) | Znaczący wybór ścieżki, kontekstu lub metody w ramach celu | Wybory zmieniają doświadczenie; wymagania wstępne i ścieżki alternatywne są jasne |
| Ciekawość poznawcza | Zagadka, w której wskazówkami są dowody z danej dyscypliny wiedzy | Odkrycie rozwiązuje problem poznawczy; czytanie fabuły nie dominuje nad ćwiczeniem |
| Współpraca w grupie | Komplementarne role, wspólny rezultat, rotacja odpowiedzialności | Każdy uczestnik wyjaśnia lub stosuje wiedzę samodzielnie |
| Uznanie osiągnięć | Opcjonalne odznaki powiązane z przejrzystymi osiągnięciami | Odznaka opisuje konkretny dowód; nigdy nie zastępuje oceny mistrzostwa |
| Rywalizacja | Opcjonalne porównywalne wyzwania lub pobijanie własnych rekordów | Kontrola zniechęcenia, rezygnacji i pośpiechu; ścieżka bez publicznych rankingów |
| Powracanie do nauki w czasie | Cele wybrane przez ucznia, wznawianie sesji, przypomnienia na życzenie | Nieobecność nie kasuje historii nauki ani nie blokuje dostępu do pomocy |

Powyższe punkty to hipotezy projektowe, a nie ranking bezwzględnie sprawdzonych funkcji. Punkty, serie dni (streaks), awatary i tabele wyników nie mają uniwersalnego wpływu na uczenie się. Przechowuj walutę gry oddzielnie od dowodów edukacyjnych. Zwykłe błędy w nauce nie mogą odbierać dostępu do materiałów dydaktycznych. Unikaj presji wygasających nagród, płatnego odzyskiwania szans, losowych nagród (lootboxów) i publicznego zawstydzania. Są to zobowiązania projektowe, a nie deklaracja, że każdy wariant został porównany eksperymentalnie.

Trudność powinna wynikać z docelowej decyzji dydaktycznej. Obciążenie tekstem, precyzja motoryczna i presja czasu mogą zniekształcać pomiar. Stosuj ograniczenia czasowe tylko wtedy, gdy płynność lub szybkość reakcji należą do celów kształcenia; rozdzielaj poprawność i tempo pracy. Nie istnieje uniwersalny, optymalny odsetek sukcesów. Dostosowuj wsparcie na podstawie wielu obserwacji i pozwól uczniom lub nauczycielom korygować niewłaściwy poziom trudności.

### Gry edukacyjne: Kształtowanie sekwencji uczenia się

Wprowadź jeden grywalny problem przed rozbudowaniem mechaniki ekonomicznej. Po każdym działaniu zapewnij zrozumiałą konsekwencję, użyteczną informację zwrotną, kolejną szansę i naturalny punkt przerwania sesji. Wyjaśniaj błąd na poziomie zadania lub strategii. Sama animacja sukcesu nie koryguje błędnego przekonania poznawczego.

Zastosuj przykład z rozwiązaniem, gdy brak wiedzy uniemożliwia podjęcie sensownej próby. Początkowy problem eksploracyjny może przygotować uczniów na późniejsze wyjaśnienie, ale produktywna porażka (productive failure) wymaga etapu konsolidacji wiedzy. Nie uzasadnia pozostawiania nowicjusza w bezradności. Oddzielaj wstępną naukę, ćwiczenia ze wsparciem i samodzielny sprawdzian. Odsłonięcie rozwiązania oznacza próbę ze wsparciem; odrębne zadanie należy ocenić później.

Planuj przypominanie, powtórki w czasie i przeplatanie zadań zgodnie z celem edukacyjnym. Planuj powroty zarówno do materiału wcześniej opanowanego, jak i błędów. Wymagaj odtworzenia wiedzy przed ujawnieniem odpowiedzi, gdy celem jest przypominanie. Mieszaj przypadki wymagające rozróżniania, z informacją zwrotną dostosowaną do aktywności. Nie deklaruj sztywnego harmonogramu powtórek jako optymalnego dla każdego przedmiotu i okresu retencji.

### Gry edukacyjne: Adaptacja do wieku i kontekstu międzynarodowego

Opieraj się na zaobserwowanej wiedzy i potrzebach wsparcia, a nie stereotypach pokoleniowych. Uczniowie szkół podstawowych mogą potrzebować reprezentacji konkretnych i wsparcia w czytaniu; uczniowie szkół ponadpodstawowych zyskują na kontrastowych wyjaśnieniach; studenci i dorośli wymagają autentyczności dyscyplinarnej i elastycznego tempa. Są to hipotezy wyjściowe. Dorosły nowicjusz może wymagać znacznego rusztowania poznawczego, podczas gdy doświadczone dziecko potrzebuje większego wyzwania.

Weryfikuj lokalną terminologię, formaty liczb i jednostek, kierunek czytania, odniesienia kulturowe, strukturę szkolnictwa i dostępne urządzenia. Odnoś program nauczania wyłącznie do zidentyfikowanego systemu i wersji dokumentu. Nigdy nie wnioskuj o krajowej podstawie programowej na podstawie języka interfejsu. Uwzględniaj korzystanie ze wspólnych urządzeń i lekcje prowadzone przez nauczyciela. Symulacja czynności zawodowej nie certyfikuje praktycznych uprawnień.

Zapewnij obsługę z klawiatury i pojedynczego wskaźnika jako alternatywę dla przeciągania, czytelny tekst stanu poza samym kolorem lub dźwiękiem, widoczny fokus, kontrolę ruchu i odpowiedni czas. Zachowaj ocenianą umiejętność przy oferowaniu alternatywnych form odpowiedzi. Dostępność i adekwatność wiekowa wymagają testów z użytkownikami; samo powołanie się na UDL lub WCAG niczego nie dowodzi.

### Gry edukacyjne: Wdrażanie we właściwej skali

Dla krótkiej aktywności zacznij od zweryfikowanej treści, deterministycznych reguł i stanu sesji. Dodaj lokalny zapis stanu tylko wtedy, gdy wznowienie pracy ma znaczenie. W produkcie długoterminowym uwzględnij wersje umiejętności i zadań, próby samodzielne i ze wsparciem, planowe powtórki, eksport/usuwanie danych i korektę nauczycielską. Konta, serwery i telemetria behawioralna wymagają konkretnego uzasadnienia.

Jeśli dowody są zapisywane, użyteczny minimalny rekord próby może zawierać: `skill_id`, `item_version`, `mode`, `support_used`, `response`, `result` i `feedback_version`. Przechowuj tylko rzeczywiście potrzebne pola; surowe odpowiedzi i znaczniki czasu nie muszą opuszczać urządzenia. Trzymaj walutę gry i elementy kosmetyczne w odrębnym stanie gry. Awaria sieci lub ponowne wysłanie formularza nie mogą dublować nagród ani zmieniać zarejestrowanej oceny.

W przypadku runtime AI zdefiniuj dozwolone źródła, granice oceniania, zachowanie awaryjne i ścieżkę weryfikacji przez człowieka. Przetestuj wiarygodne, lecz błędne wyjaśnienia, poprawne odpowiedzi równoważne i niedostępność usługi. Ocenę uczenia się przeprowadzaj po wycofaniu asysty AI. Badania nad konkretnymi tutorami nie oznaczają, że każdy chatbot pomaga lub że przymusowe czekanie na pomoc jest korzystne. Wykorzystanie AI do budowy aplikacji nie oznacza konieczności wywołań AI w gotowym produkcie.

Koordynując pracę specjalistów lub agentów, zapewnij im wspólny cel, przykłady zadań i reguły dowodowe. Rozdzielaj poprawność merytoryczną, projekt dydaktyczny, grywalność i testy implementacji. Rozstrzygaj spory na podstawie przykładu lub źródła. Wiele ról w jednym prompcie nie stanowi niezależnej walidacji; korzystaj z niezależnych agentów tylko wtedy, gdy jest to uzgodnione i uzasadnione.

### Gry edukacyjne: Walidacja trzech różnych rezultatów

1. Działanie techniczne: poprawne i alternatywne odpowiedzi, błędy poznawcze, wielokrotne zgadywanie, odsłonięcie rozwiązania, ponowienie próby, wznawianie sesji i awaria sieci. Upewnij się, że sukces ze wsparciem nigdy nie jest po cichu zaliczany jako samodzielne opanowanie materiału.
2. Użyteczność i rozgrywka: obserwuj docelowych użytkowników podejmujących pierwsze zadanie i wychodzących z błędu. Zwróć uwagę na dezorientację, wybory strategiczne i możliwość przerwania gry. Niewielki pilotaż diagnozuje problemy; nie pozwala określić efektu populacyjnego.
3. Efekty uczenia się: oceń nowe zadanie bez asysty, odroczoną retencję oraz transfer wiedzy poza powierzchowne elementy gry. Do wnioskowania porównawczego użyj wiarygodnej alternatywy o porównywalnej treści i czasie; uwzględnij wiedzę uprzednią, rezygnację uczestników i nierówne zaangażowanie. Raportuj niepewność i unikaj traktowania czasu spędzonego w grze lub zadowolenia jako dowodu uczenia się.

W małych projektach udokumentuj hipotezę edukacyjną i wykonalny pilotaż. Przy produktach o wysokiej stawce zdefiniuj wskaźniki i grupę odniesienia przed zebraniem danych. Oddzielaj metryki gry od metryk uczenia się. Usuń lub zmodyfikuj mechanikę, jeśli zachęca do chodzenia na skróty, zniechęca do korzystania z pomocy lub dokłada wysiłku bez wartości dydaktycznej.

### Gry edukacyjne: Dowody naukowe i ich granice

- [Sailer i Homner, 2020](https://doi.org/10.1007/s10648-019-09498-w): metaanaliza wskazuje na umiarkowane średnie korzyści z grywalizacji przy dużej heterogeniczności wyników; efekty motywacyjne i behawioralne były mniej stabilne przy rygorystycznej kontroli jakości badań. Nie stanowi to gwarancji sukcesu dla konkretnej odznaki czy tabeli wyników.
- [Clark i in., 2016](https://doi.org/10.3102/0034654315582065): porównania gier i ulepszeń projektowych potwierdzają wagę projektu dydaktycznego i rusztowania poznawczego. Samo medium nie decyduje o uczeniu się.
- [Li i in., 2024](https://doi.org/10.1007/s11423-023-10337-7): niewielka średnia korzyść w motywacji wewnętrznej w 35 interwencjach. Poczucie własnej kompetencji różni się od zmierzonego opanowania przedmiotu.
- [Habgood i Ainsworth, 2011](https://doi.org/10.1080/10508406.2010.508029): dwa badania jednej gry matematycznej potwierdzają integrację nauki z głównymi mechanikami gry. Małe, specyficzne próby nie tworzą uniwersalnej formuły gry.
- [Agarwal i in., 2021](https://doi.org/10.1007/s10648-021-09595-9) oraz [Ruitenburg i in., 2026](https://doi.org/10.1007/s10648-026-10225-5): dowody klasowe na korzyść przypominania i zależnych od kontekstu harmonogramów powtórek. Drugie badanie rozróżnia przypominanie, powtórki w czasie i przeplatanie.
- [Wisniewski i in., 2020](https://doi.org/10.3389/fpsyg.2019.03087): efekty informacji zwrotnej są zróżnicowane; kluczowe są informacje ukierunkowane na działanie. [Sinha i Kapur, 2021](https://doi.org/10.3102/00346543211019105): rozwiązywanie problemów przed instruktażem może pomagać w określonych warunkach, z istotnymi granicami dotyczącymi uczniów i implementacji.
- [Almeida i in., 2023](https://doi.org/10.1016/j.infsof.2022.107142): mapowanie wskazuje zgłaszane negatywne skutki uboczne i chodzenie na skróty. Liczba zgłoszeń nie określa częstości występowania szkód.
- [MIT / Learning Games Network, 2015](https://education.mit.edu/wp-content/uploads/2018/10/BalancedDesignGuide2015.pdf): model projektowy łączący cele, działania i dowody. [George Fan, GDC 2012](https://media.gdcvault.com/gdc2012/slides/Design%20Track/Fan_George_How%20I%20Got.pdf): doświadczenia praktyczne z grywalnym wdrażaniem gracza (onboarding). Oba źródła wspierają projektowanie; żadne nie dostarcza przyczynowo-skutkowego oszacowania efektywności kształcenia.
- [Bastani i in., 2025](https://doi.org/10.1073/pnas.2422633122) oraz [Kestin i in., 2025](https://doi.org/10.1038/s41598-025-97652-6): różne eksperymenty pokazują, dlaczego konstrukcja tutora i samodzielne wyniki mają kluczowe znaczenie. Populacje, przedmioty i interwencje różnią się między sobą.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) określa kryteria dostępności; [CAST UDL 3.0](https://udlguidelines.cast.org/) dostarcza ramy projektowe. Mają one inny charakter dowodowy niż eksperymenty dydaktyczne.

### Gry edukacyjne: Łączenie doświadczenia, mechanik i transferu wiedzy

Stosuj model MDA (Mechanics, Dynamics, Aesthetics) jako perspektywę projektową: opisz zamierzone doświadczenie (estetykę), oczekiwane zachowanie gracza (dynamikę) oraz reguły, które je wywołują (mechaniki). Na przykład odkrywanie może wymagać sterowalnego modelu i miarodajnych obserwacji; ekspresja może wymagać wielu poprawnych konstrukcji. Nie ograniczaj każdego przedmiotu do jednego gatunku gry. Teoria autodeterminacji (SDT) kieruje uwagę na autonomię, kompetencję i relacyjność; ani MDA, ani etykieta z modelu Octalysis nie dowodzą skuteczności edukacyjnej.

W otwartej łamigłówce inżynieryjnej zdefiniuj ograniczenia i weryfikowalny warunek sukcesu, nie narzucając jedynego rozwiązania wymyślonego przez autora. Zaoferuj porównanie własnych poprawnych projektów ucznia pod kątem konkurujących kryteriów, takich jak zużycie zasobów czy precyzja. Histogram społeczności wymaga rzeczywistych danych i dobrowolnego udostępniania; nie wymyślaj sztucznego rozkładu. Optymalizacja nie musi wiązać się z dodatkową walutą gry.

Połącz reprezentacje w grze z notacją dziedzinową lub realnymi decyzjami, a następnie sprawdź nowe zadanie poza powierzchownymi wskazówkami gry. Nie narzucaj dzielonego ekranu ani trzech etapów każdemu uczniowi. Doświadczenie gry (game feel) powinno komunikować znaczącą zmianę bez zaciemniania logicznego myślenia. Zachowaj serie i nagrody jako opcjonalne i niestosujące kar; przerwa w grze nie może usuwać dowodów nauki ani pomocy. Publiczne pokazywanie postępów wymaga wyraźnej zgody ucznia.

[MDA autorstwa Hunicke, LeBlanca i Zubeka](https://www.cs.northwestern.edu/~hunicke/MDA.pdf) to ramy projektowe. Przytoczone badania nad grami edukacyjnymi dotyczą specyficznych populacji i rezultatów; wskaźników retencji produktu nie należy utożsamiać z przyrostem wiedzy.

## Reference: design-dialogue

Sekcja źródłowa: Dialog podczas projektowania edukacyjnego


Stosuj te reguły przy pierwszym istotnym wyborze pedagogicznym oraz wtedy, gdy nowe dowody lub zmienione wymagania otwierają go ponownie. Zasady te stanowią schemat pracy projektowej, a nie twierdzenia eksperymentalne o uczeniu się.

### Dialog projektowy: Identyfikacja ucznia i warunków uczenia się

Wiek, rola edukacyjna i doświadczenie w danym temacie to różne atrybuty. Słowo „dziecko” odnosi się do wieku; określenia „uczeń” czy „student” opisują role edukacyjne, których zakres różni się w zależności od kraju. Kategorie te nakładają się na siebie. W ogólnym projekcie używaj określeń „uczeń” lub „uczestnik”, a w samym produkcie stosuj sformułowania adekwatne lokalnie. Przykłady szkolne nie ograniczają skilla wyłącznie do dzieci. Bezpośrednie instrukcje mogą po prostu brzmieć: „Spróbuj”, „Wyjaśnij” lub „Porównaj”.

Przed wyborem metody stwórz krótki profil roboczy odbiorców na podstawie znanego kontekstu: grupa wiekowa i środowisko; wiedza uprzednia z tego tematu; umiejętność czytania i język; stopień samodzielności i dostępne wsparcie; cel i konsekwencje oceniania; urządzenia oraz funkcjonalne potrzeby dostępności. Są to fakty projektowe, a nie obowiązkowa ewidencja danych osobowych. Nie wymagaj podawania daty urodzenia, diagnoz medycznych ani pełnej historii szkolnej. Zaznacz niewiadome lub założenia; samo słowo „uczeń” ich nie definiuje.

| Kontekst i przydatne określenie | Co ustalić | Możliwa adaptacja w razie potrzeby |
| --- | --- | --- |
| Dziecko w wieku przedszkolnym, na życzenie | Umiejętność czytania, sterowanie, asysta dorosłego i cel korzystania z ekranu | Krótkie konkretne instrukcje, wspólna zabawa i aktywności poza ekranem; nie zakładaj samodzielnego czytania |
| Uczeń szkoły podstawowej (klasy I–VIII) | Pojęcia, notacja, czytanie poleceń ze zrozumieniem i urządzenia | Połącz reprezentację konkretną z pojęciem, zademonstruj interfejs i zapewnij wsparcie |
| Uczeń szkoły ponadpodstawowej (liceum, technikum, szkoła branżowa) | Wymagania wstępne, zróżnicowanie w klasie i praca grupowa | Porównywanie strategii, wyjaśnianie i dobór wsparcia w dążeniu do wspólnego celu |
| Uczeń szkoły zawodowej lub profilowanej | Kierunek kształcenia, doświadczenie praktyczne i cel egzaminacyjny | Rzeczywisty problem branżowy, argumentacja lub scenariusz zawodowy; symulacja nie zastępuje sprawdzianu praktycznego |
| Student uczelni wyższej | Wymagania dyscypliny i dotychczasowe doświadczenie w temacie | Autentyczne zadania badawcze, dowody i wielość rozwiązań; przykłady z rozwiązaniem dostępne przy nowych tematach |
| Dorosły uczestnik, osoba ucząca się samodzielnie lub pracownik | Cel osobisty/zawodowy, doświadczenie, czas i realne zastosowanie | Sytuacje adekwatne do życia zawodowego, pomijanie znanego materiału, elastyczne tempo i wznawianie nauki |
| Osoba starsza, gdy dotyczy | Indywidualne doświadczenie, język, obsługa interfejsu i dostępność | Dostosowanie wielkości tekstu, czasu reakcji lub kontrolek; wiek nie oznacza braku biegłości cyfrowej |
| Grupa zróżnicowana | Potrzeby wspólne oraz wymagające wariantowości | Wspólny cel kształcenia, opcjonalne wsparcie, zróżnicowane zadania wejściowe i indywidualne dowody uczenia się |

Są to opcje projektowe, a nie diagnozy rozwojowe czy sztywne przypisania metod do wieku. Etapy edukacyjne i nazwy klas różnią się w poszczególnych krajach. Dziecko może być zaawansowane w danej dziedzinie, a dorosły zupełnie początkujący. Wsparcie językowe, dostępność i zróżnicowane tempo mogą dotyczyć każdej grupy. Nie przypisuj uczniom sztywnych „stylów uczenia się” (wzrokowiec, słuchowiec itp.).

Rozróżniaj, kto się uczy, kto obsługuje aplikację i kto widzi wyniki. Nauczyciel może operować wspólnym ekranem, rodzic towarzyszyć dziecku, a twórca nie musi być żadnym z nich. Grupa dziecięca nie decyduje automatycznie o tym, kto ma dostęp do wyników. Zdefiniuj role i uprawnienia dla rzeczywistego wdrożenia.

Gdy brakujący fakt zmienia projekt, zapytaj na przykład: „Czy jest to aplikacja dla uczniów szkoły podstawowej, starszych uczniów czy dorosłych początkujących? Co potrafią już zrobić w tym temacie?”. Dopasuj pytania do sytuacji; nie powtarzaj listy wszystkich grup ani informacji już podanych. Doprecyzuj niejednoznaczne pojęcie „uczniowie” tylko wtedy, gdy środowisko wpływa na rezultat.

Wyjaśnij, kto i dlaczego zyskuje na proponowanej metodzie: „Dla tych dorosłych początkujących rekomenduję przykład z rozwiązaniem oparty na ich pracy zawodowej, a następnie redukcję wsparcia w miarę postępów w samodzielnych próbach”. Zmiana grupy odbiorców otwiera ponowną analizę języka, treści, wsparcia, oceniania i kontrolek, ale nie oznacza automatycznego resetu całego projektu.

### Dialog projektowy: Oferowanie pomocy w punkcie potrzeby

Pobierz znaną grupę odbiorców, wiedzę uprzednią, cel, uwarunkowania prawne, urządzenia, czas i ograniczenia z projektu. Zapytaj o brakujący fakt tylko wtedy, gdy zmienia on decyzję. Domyślnym trybem jest prowadzony dialog. Twórca może przekazać agentowi pojedynczy wybór lub kolejne rutynowe decyzje, a później powrócić do dialogu.

| Moment wyzwalający | Istotne wybory do wyjaśnienia |
| --- | --- |
| Cel i pierwsza aktywność | Przykład z rozwiązaniem i stopniowym wycofywaniem wsparcia (fading), ukierunkowane dociekanie, przypominanie, konstruowanie wiedzy lub autentyczny projekt |
| Motywacja i uczestnictwo | Osobisty postęp, znaczący wybór, role w pracy kooperatywnej, opcjonalne mechaniki gry |
| Projekt błędu i pomocy | Ukierunkowana wskazówka, przykład kontrastowy, bezpośrednie wyjaśnienie i kolejna próba |
| Ocenianie | Informacja zwrotna kształtująca, rubryka kryteriów, sprawdzian samodzielny, portfolio lub recenzja koleżeńska ze wsparciem |
| Kontynuacja nauki | Stan wyłącznie w sesji, lokalne wznawianie pracy, powtórki rozłożone w czasie lub skalibrowana trudność |
| Wnioski z prototypu | Poprawa mylącej reprezentacji, redukcja wsparcia, dodanie transferu lub usunięcie nadużywanej nagrody |

Są to okazje do podjęcia decyzji, a nie obowiązkowe punkty kontrolne. W małym projekcie połącz powiązane wybory. Przedstawiaj wyłącznie wykonalne opcje, z krótkim opisem, przykładem w tym produkcie oraz związanymi z nimi kosztami, zapotrzebowaniem na dane lub ograniczeniami. Zarekomenduj jedną opcję i zadaj jedno precyzyjne pytanie. Zapewnij prostą wersję lub możliwość odłożenia decyzji; nie wymagaj od twórcy znajomości akademickich nazw teorii. Dodatkowe metody są dostępne na życzenie.

### Dialog projektowy: Pamiętanie ustaleń i decyzji

W przypadku małych zadań wykorzystuj bieżącą konwersację; przy dłuższych projektach stosuj istniejący w projekcie rejestr decyzji architektonicznych lub projektowych. Zapisuj cel, ograniczenia, identyfikator metody, powód, status, odrzucone alternatywy i nierozstrzygnięte pytania. Sugerowane statusy: `offered` (zaproponowano), `selected` (wybrano), `implemented` (wdrożono), `verified` (zweryfikowano), `deferred` (odłożono), `declined` (odrzucono). Oddzielaj te zapisy od rejestrów danych uczniów. Nowe wymaganie otwiera ponownie tylko te decyzje, na które wpływa; wyjaśnij dlaczego. Nie traktuj braku odpowiedzi jako wyboru opcji. Kontynuuj niezależne prace, gdy ważna decyzja oczekuje na odpowiedź.

### Dialog projektowy: Od wyboru do działającego produktu

Wykorzystuj działanie ucznia, dowód, wsparcie i test określone w karcie metody. Zachowaj jedną spójną sekwencję uczenia się; wyjaśniaj sprzeczne wybory. Przykład z rozwiązaniem może poprzedzać późniejszą praktykę przypominania; produktywna porażka (productive failure) wymaga późniejszej konsolidacji wiedzy. Żadne z tych podejść nie oznacza konieczności testowania na każdym ekranie.

Dla aktywności offline z ułamkami: „Rekomenduję łączenie elementów graficznych i pokazywanie odpowiadającego ułamka, ponieważ celem jest równoważność. Oś liczbowa kładzie natomiast nacisk na jednakowe położenie; uzupełnienie rozwiązanego przykładu zapewnia większe wsparcie początkowe. Które podejście ma być główną aktywnością?”. W późniejszym etapie zaproponuj nowe zadanie bez elementów graficznych lub zadanie analizy błędu, aby sprawdzić transfer wiedzy. Nie powtarzaj wstępnego wywiadu.

Twórca zamawia działającą aplikację. Nie zamieniaj tego dialogu w przymusowe korepetycje, zadanie domowe z programowania ani listę niedokończonych TODO. Przy przekazywaniu projektu wskaż, gdzie działa każda wybrana metoda, co zostało zweryfikowane i co pozostaje niepewne. Automatyczne wykrywanie skilla zależy od środowiska uruchomieniowego; przetestuj wykrywanie odrębnie od zachowania po wywołaniu.

## Reference: cognitive-ux

Sekcja źródłowa: Interfejs poznawczy i reprezentacje wiedzy


Przeczytaj ten dokument przy projektowaniu diagramów, multimediów, instrukcji, rozmieszczenia informacji zwrotnej lub interfejsu, który mógłby przesłaniać zadanie edukacyjne. Stosuj go do docelowych uczniów i urządzeń, a nie jako sztywny szablon wizualny.

### Interfejs poznawczy: Skupienie uwagi na decyzji dydaktycznej

Wycisz zbędny, konkurujący o uwagę ruch i dźwięk podczas wymagających zadań poznawczych; zachowaj użyteczny kontekst i kontrolki. Umieszczaj powiązane etykiety i wyjaśnienia blisko obiektów, do których się odnoszą, nie zasłaniając ich. Na małych ekranach stosuj powiązane wyróżnienia, dostępny opis tekstowy lub widok sekwencyjny, gdy bezpośrednie sąsiedztwo jest niewykonalne. Sam kolor nie może być jedynym nośnikiem znaczenia.

Dziel złożone procedury na etapy kontrolowane przez ucznia. Wprowadzaj nowe kontrolki i terminy pojedynczo, zanim połączysz je w całość. Zapewnij bezpośrednią ścieżkę dla zaawansowanych uczniów oraz łatwy powrót do pomocy. Animacja powinna wyjaśniać zmianę lub działanie; zapewnij opcję ograniczenia ruchu (reduced-motion) i równoważny, zrozumiały stan statyczny.

### Interfejs poznawczy: Łączenie reprezentacji i sprawdzanie transferu wiedzy

Gdy obiekty konkretne wspierają pojęcie abstrakcyjne, pokaż, jak ta sama zależność wyraża się w obiektach manipulacyjnych, na diagramach i w formalnym zapisie dziedzinowym. Wyjaśnij tę odpowiedniość, a następnie zaproponuj nowe zadanie z mniejszym wsparciem reprezentacji konkretnej. Podzielony widok (split view) to tylko jedna z możliwych implementacji, a nie sztywny wymóg. Zapewnij pełną obsługę z klawiatury i alternatywy dla przeciągania elementów (drag-and-drop). Upewnij się, że uczeń nie może odnieść sukcesu, kierując się wyłącznie dopasowywaniem kolorów lub pozycji na ekranie.

Przykład: uczeń manipuluje równoważnymi wielkościami, widzi odpowiadające im równanie matematyczne i wyjaśnia, dlaczego pozostaje prawdziwe; w kolejnym kroku rozwiązuje nowe równanie bez obiektów manipulacyjnych. Zaawansowani uczniowie mogą od razu zacząć od notacji formalnej. Przywróć reprezentację konkretną, jeśli okaże się pomocna. W zadaniach pozamatematycznych transfer może polegać na ocenie nowego źródła lub zastosowaniu procedury w innym scenariuszu.

### Interfejs poznawczy: Zachowanie dostępności i miarodajnych dowodów

Unikaj niepotrzebnych równoległych strumieni informacji, lecz zachowaj napisy, transkrypcje, możliwość ponownego odtworzenia, wsparcie językowe i dostępność dla czytników ekranowych. Zasada redundancji nie oznacza zakazu wyświetlania tekstu obok dźwięku. Nie ukrywaj kluczowych instrukcji w etykietach dostępnych wyłącznie po najechaniu myszą (hover-only). Jeśli dźwięk lub czas odpowiedzi jest ocenianą umiejętnością, jasno określ warunki i zaplanuj dostosowania dla osób ze szczególnymi potrzebami.

W kluczowych punktach pojęciowych opcjonalna ocena pewności siebie (confidence judgment) pozwala porównać własne przekonanie z faktycznym wynikiem. Nie traktuj deklarowanej pewności siebie jako dowodu opanowania materiału ani nie wymagaj jej po każdej czynności. Informacja zwrotna powinna wyjaśniać istotny kontrast i stwarzać okazję do jego wykorzystania; nie wywołuj sztucznego zaskoczenia ani wątpliwości przy poprawnie wykonanej pracy.

Sprawdzaj czytelność etykiet, kolejność fokusu klawiatury, skalowanie tekstu, układy na wąskich ekranach, redukcję ruchu oraz pełną ścieżkę pomocy i ponawiania prób. Badaj rzeczywiste zadanie ucznia, a nie tylko estetykę komponentów. Jawnie wskazuj niewykonane testy.

### Interfejs poznawczy: Źródła i ograniczenia

[Waxman i Goldie, 2023](https://media.repository.chds.hsph.harvard.edu/static/filer_public/ca/62/ca625803-3d73-4855-b3e1-765870ce3772/2023_jwaxman_monograph_cogtheory_multimed.pdf) stanowi punkt odniesienia dla wyborów projektowych, a nie uniwersalnych zakazów układu strony. [Matlen i Devlin, 2020](https://web.stanford.edu/~kdevlin/Papers/Matlen-Devlin_CHI2020.pdf) opisuje koncepcję wczesnego transferu, a nie bezwzględną walidację każdego układu z dzielonym ekranem. [Wytyczne W3C dotyczące napisów](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html) definiują warunki dostępności. Należy sprawdzić aktualne wymogi normatywne dla docelowej wersji wdrożeniowej.

## Reference: adaptive-practice

Sekcja źródłowa: Praktyka adaptacyjna i kontynuacja uczenia się


Przeczytaj ten dokument, gdy produkt wymaga wielokrotnych sesji, harmonogramowania powtórek lub doboru poziomu trudności. Rozróżniaj: kiedy powtórzyć materiał, jakie zadanie przedstawić i ile pomocy zaoferować. Poszczególne elementy nie muszą korzystać z tego samego modelu.

| Potrzeba | Prosta implementacja | Opcjonalne rozszerzenie i wymagania wstępne |
| --- | --- | --- |
| Pojedyncza aktywność | Zweryfikowane zadania, jawna sekwencja, pomoc i stan sesji | Zazwyczaj brak trwałego modelu ucznia |
| Przypominanie w odstępie dni | Jawny harmonogram powtórek i lokalna historia | FSRS dla stabilnych elementów i przejrzystych zdarzeń powtórkowych |
| Dobór trudności | Zweryfikowane poziomy zadań i przejrzyste rozgałęzienia | Ranking Elo przy odpowiednich danych o odpowiedziach, niepewności i kalibracji |
| Śledzenie zależności umiejętności | Mapa umiejętności z niezależnymi dowodami | BKT lub IRT wyłącznie przy uzasadnionym modelu, danych i walidacji |
| Plan długoterminowy | Cel, dostępny czas, bieżący etap i kolejne zadanie | Modyfikowalne kamienie milowe, pytania przeniesione i terminy powtórek |

Najpierw wyjaśnij funkcję dydaktyczną, a dopiero potem algorytm. Zachowaj istniejący stos technologiczny; nie instaluj harmonogramu, backendu ani systemu kont tylko dlatego, że zostały tu wymienione. Proste reguły zachowują pełną wartość, o ile ich ograniczenia są jawne. Model HLR to kolejny wytrenowany model przypominania dla odpowiednich danych, a nie domyślny wymóg implementacyjny.

### Praktyka adaptacyjna: Warunki wstępne adaptacji

Zdefiniuj stabilne identyfikatory zadań i umiejętności, wersje treści, interpretację odpowiedzi oraz warunki udzielenia pomocy. Rozdzielaj odpowiedzi zgadnięte, udzielone z pomocą, po odsłonięciu rozwiązania oraz w pełni samodzielne. Przestrzegaj semantyki oceniania wybranej biblioteki; nie traktuj po cichu każdej odpowiedzi ze wsparciem jako samodzielnego przypomnienia. Przechowuj walutę gry poza modelem uczenia się. Stosuj minimalny zestaw danych i znaczniki czasu tylko tam, gdzie są niezbędne do planowania powtórek.

Określ zachowanie w stanie początkowym (cold-start) oraz bezpieczny mechanizm awaryjny (fallback), gdy historia jest niedostępna, uszkodzona lub nieaktualna. Zbadaj założenia na reprezentatywnych danych, uwzględniając język i warunki dostępu. Umożliw nauczycielowi wprowadzanie korekt, a uczniowi dostęp do pomocy. Przewidywany sukces jest obarczony niepewnością; ani arbitralny cel 80–90% sukcesu, ani dwie poprawne odpowiedzi nie wyznaczają strefy najbliższego rozwoju (ZPD) ani nie dowodzą mistrzostwa. Pożądany wskaźnik retencji to kompromis dotyczący nakładu pracy, a nie gwarantowany efekt kształcenia.

W przypadku wyboru algorytmu używaj utrzymywanej, zweryfikowanej pod kątem wersji biblioteki. Przetestuj aktualizacje, strefy czasowe i granice dni, zduplikowane odpowiedzi, zmiany w treści zadań, eksport/wznawianie sesji oraz nieprawidłowe dane wejściowe. Porównaj zaawansowane rozszerzenie z prostą wersją bazową; trafność predykcji, zaangażowanie i faktyczne uczenie się to odrębne rezultaty. Nie wnioskuj o niepełnosprawności ani cechach osobowości na podstawie samego czasu reakcji.

### Praktyka adaptacyjna: Zakończenie lub wznowienie etapu nauki

Zarejestruj wynik, warunki udzielenia pomocy, nierozstrzygnięte pytania i wykonalny kolejny krok. Ukończenie etapu różni się od wykazania się opanowaniem wiedzy. Utworzenie nowego etapu nie kończy automatycznie poprzedniego. Podsumowania powinny zachowywać niezbędne wskaźniki dowodowe i stopień niepewności, a nie pełne transkrypcje rozmów. Po powrocie zweryfikuj zdezaktualizowane założenia za pomocą proporcjonalnego zadania; przerwy w nauce nie powinny kasować dotychczasowych postępów.

### Praktyka adaptacyjna: Źródła

[Dokumentacja Anki FSRS](https://docs.ankiweb.net/manual/deck-options), [Pelánek o edukacyjnym rankingu Elo](https://www.fi.muni.cz/~xpelanek/publications/CAE-elo.pdf) oraz [Settles i Meeder o HLR](https://research.duolingo.com/papers/settles.acl16.pdf). Źródła te opisują konkretne modele i ustawienia; nie dowodzą skuteczności nowo powstającej aplikacji. Przy integracji biblioteki należy sprawdzić jej aktualną dokumentację implementacyjną.

## Informacja o licencji

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
