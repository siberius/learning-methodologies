# Symulacje i odgrywanie ról

Przeczytaj ten dokument, gdy produkt modeluje zjawisko/system, wspiera przeprowadzanie eksperymentu lub pozwala uczniom działać w ramach scenariusza. Wybierz wyłącznie te testy, które odnoszą się do danego zadania.

## Określ, co reprezentują dane wyjściowe

W języku skierowanym do ucznia wyraźnie rozróżniaj następujące rodzaje danych:

- **Pomiar:** obserwacje z rzeczywistego przyrządu, zbioru danych lub zarejestrowanego eksperymentu fizycznego. Wskaż źródło i istotne granice błędu pomiarowego.
- **Obliczenie lub symulacja:** wyniki wygenerowane przez określony model matematyczny lub regułowy. Podaj przyjęte założenia upraszczające oraz zakres, w którym model pozostaje użyteczny.
- **Fikcja lub rekonstrukcja:** wymyślone zdarzenia, dialogi, postacie lub konsekwencje służące celom dydaktycznym. Oznacz je jednoznacznie jako takie.

Nigdy nie opisuj wygenerowanych liczb jako pomiarów rzeczywistych ani wymyślonego dialogu jako autentycznego cytatu historycznego. Symulacja może ilustrować hipotezę; same jej wyniki nie dowodzą tego, jak zachowuje się świat rzeczywisty.

## Zdefiniuj i zweryfikuj model

Zapisz cel kształcenia, zmienne stanu, dane wejściowe, jednostki miar, dozwolone zakresy, założenia, reguły aktualizacji i obserwowalne wyniki. Wyjaśnij uproszczenia wpływające na interpretację zjawiska. Dobierz kontrolki tak, aby ukazywały zamierzoną zależność, bez zmuszania uczniów do zgadywania nieudokumentowanych ustawień.

W zadaniach obliczeniowych wyliczaj wyniki za pomocą zweryfikowanego silnika numerycznego lub jawnych reguł deterministycznych. Oddziel ten silnik od komentarzy generowanych przez model językowy (LLM). Model językowy może wyjaśniać rzeczywiste wyniki, lecz nie może zmyślać brakujących obliczeń ani stwarzać pozorów, że przeprowadził fizyczny eksperyment.

Zastosuj zestaw testów dopasowany do modelu: znany przypadek wzorcowy, przypadek graniczny, spójność jednostek i jeden oczekiwany trend monotoniczny. W modelach stochastycznych wskaż źródło losowości i w razie potrzeby zapewnij powtarzalne ziarno losowości (seed). Dokumentuj ograniczenia zamiast sugerować uniwersalną ważność modelu.

## Zaprojektuj pętlę uczenia się

Poproś ucznia o sformułowanie przewidywania i jego uzasadnienie przed uruchomieniem modelu, jeśli wspiera to cel dydaktyczny. Pozwól uczniom zmieniać istotne parametry wejściowe, obserwować rzeczywisty wynik, porównywać go z własnym przewidywaniem i modyfikować swoje wyjaśnienie. Zapewnij podsumowanie (debriefing), które odróżnia zachowanie modelu od faktów ze świata rzeczywistego i stawia pytanie, w jakich warunkach model przestaje działać poprawnie.

Nie przyznawaj potwierdzenia zrozumienia tematu wyłącznie za osiągnięcie docelowej konfiguracji suwaków na ekranie. Oczekuj wyjaśnienia, porównania lub transferu wiedzy do nowego przypadku.

## Historyczne i społeczne odgrywanie ról

Określ jednoznacznie, czy postać jest fikcyjna, syntetyczna czy oparta na źródłach historycznych. Zachowaj wyraźne rozróżnienie między faktami źródłowymi a zrekonstruowanymi wypowiedziami. Podawaj pochodzenie twierdzeń historycznych i wskazuj na sporne interpretacje, gdy jest to istotne. Nie twórz pozorów autentycznego wglądu w myśli historycznych postaci ani nie twórz fałszywych cytatów.

Zdefiniuj rolę, granice scenariusza, cel edukacyjny i podsumowanie (debriefing). Zapewnij bezpieczne wyjście z roli oraz dostęp do obiektywnego wyjaśnienia. Dopasuj intensywność emocjonalną i tematykę do wieku uczniów i warunków w klasie; zapewnij aktywność alternatywną przy scenariuszach trudnych emocjonalnie. Oceniaj zamierzone rozumowanie lub umiejętności komunikacyjne według jawnych kryteriów; sama zgoda z poglądami odgrywanej postaci nie stanowi dowodu uczenia się.
