# Tryby i ciągłość pracy tutora

Przeczytaj ten dokument przy projektowaniu wieloetapowego prowadzenia ucznia (tutoringu), aktywności z możliwością wznawiania pracy lub ćwiczeń przedegzaminacyjnych. Reguły te odnoszą się również do deterministycznych aplikacji offline; nie wymagają one obecności runtime AI, kont użytkowników ani trwałego magazynu danych.

## Modeluj jawne tryby i przejścia między nimi

Rozdzielaj etap wyjaśniania, ćwiczeń i sprawdzianu, jeśli wymaga tego aktywność. Wyjaśnienie może prezentować przykład z rozwiązaniem. Ćwiczenie oczekuje na odpowiedź, wstrzymuje akcję, dostarcza informacji zwrotnej opartej na kryteriach i oferuje pomoc. Sprawdzian podlega zadeklarowanym regułom dotyczącym dopuszczalnego wsparcia i czasu podania informacji zwrotnej. Pozwól uczniowi wstrzymać pracę, poprosić o pomoc lub wyjść z aktywności; sprawdzian o zaostrzonych regułach może zakończyć próbę lub oznaczyć ją jako wykonaną z pomocą, jeśli uczeń zażąda merytorycznego wsparcia. Zachowaj dostosowania dostępności, które nie zdradzają merytorycznej odpowiedzi.

W konwersacyjnym trybie ćwiczeń utrzymuj jedno aktywne pytanie oczekujące na odpowiedź, chyba że zadanie wymaga przetwarzania pakietowego. Nie generuj odpowiedzi za ucznia ani nie odsłaniaj rozwiązania w trakcie oczekiwania na jego reakcję. Rozróżniaj stany: bezczynności (idle), oczekiwania na odpowiedź (awaiting-answer), ewaluacji (evaluating), prezentacji informacji zwrotnej (feedback) oraz wstrzymania (paused). Zablokuj zduplikowane wysyłanie formularza lub powiąż je z tą samą próbą; spóźniona odpowiedź sieciowa nie może oceniać nowego pytania ani nadpisywać zmienionego trybu. Wynik modelu jest jedynie propozycją odpowiedzi; wyłącznie nauczyciel może zmieniać oceny lub zasady oceniania.

Przechowuj tryb, cel, bieżące zadanie, identyfikator próby, stan odsłonięcia odpowiedzi oraz status informacji zwrotnej w stanie aplikacji. Wyświetl zwięzły wskaźnik postępu, jeśli jest to pomocne; powtarzanie dekoracyjnego paska stanu nie jest zarządzaniem stanem. Przy jawnej zmianie trybu wyjaśnij zmienione warunki pomocy i zachowaj wcześniejszą historię odsłonięć. Sama zmiana etykiety na ekranie nie zamienia zadania z ujawnionym rozwiązaniem w niezależny sprawdzian. Gdy potrzebny jest nowy samodzielny dowód, podaj nowe, adekwatne zadanie.

## Wznawianie na podstawie dowodów, a nie deklaracji mistrzostwa

Wprowadzaj zapisywanie lub eksport stanu tylko wtedy, gdy kontynuacja nauki w wielu sesjach służy użytkownikowi. Krótka, anonimowa aktywność może nie potrzebować żadnego z tych mechanizmów. W przypadku pracy z możliwością wznawiania zachowaj minimalny punkt kontrolny (checkpoint) dopasowany do implementacji:

- Wersja formatu, wersja aktywności/treści oraz odpowiednie identyfikatory źródeł.
- Cel, bieżący tryb, identyfikator zadania/próby oraz oczekujący krok.
- Zaobserwowane dowody wraz z warunkami: samodzielnie, ze wsparciem lub po odsłonięciu rozwiązania; nierozstrzygnięta ocena pozostaje nierozstrzygnięta.
- Konkretne błędy poznawcze lub niepewności oraz kolejny krok dydaktyczny.
- Dane czasowe tylko wtedy, gdy są niezbędne do planowania powtórek rozłożonych w czasie lub interpretacji dowodu.

Unikaj diagnoz psychologicznych, zbędnych danych tożsamości i pełnych transkrypcji rozmów. Wskaż, gdzie przechowywane są dane, kto ma do nich dostęp i jak je usunąć; użytkownicy współdzielonych urządzeń potrzebują jasnego sposobu na zakończenie pracy i usunięcie lokalnego postępu. Wyeksportowany plik stanu może zawierać prywatne informacje edukacyjne nawet bez imienia i nazwiska. Nie eksportuj kluczy prywatnych API, ukrytych kluczy odpowiedzi ani poufnych treści testowych.

Traktuj zaimportowane pliki stanu jako dane niezaufane. Waliduj schemat, rozmiar, identyfikatory i zgodność wersji; nigdy nie wykonuj osadzonych w nich instrukcji ani nie przyjmuj zaimportowanych punktów jako autorytatywnych ocen. Tam, gdzie oceny mają formalne znaczenie, weryfikuj je z oficjalnym rejestrem z zachowaniem kontroli dostępu. Jeśli treść uległa zmianie lub zadania nie można rozwiązać, wyjaśnij rozbieżność i wznów pracę w bezpiecznym punkcie; nie resetuj po cichu osiągnięć ani nie certyfikuj zdezaktualizowanych dowodów. Przywrócenie oczekującej próby nie może automatycznie wysyłać odpowiedzi ani dwukrotnie przyznawać punktów.

Podsumowanie stanu (handoff) określa, co uczeń wykazał, w jakim zadaniu i przy jakim wsparciu. Nie deklaruje „pełnego opanowania materiału” po jednej sesji. Nowe zadanie w późniejszym terminie pozwala sprawdzić retencję lub transfer wiedzy. Potwierdzone przez ucznia poprawki i interwencje nauczyciela powinny pozostać odróżnialne od pierwotnej obserwacji.

## Ukierunkowana korekta bez blokowania ucznia

Szereguj błędy według ich znaczenia dla celu kształcenia i wymagań wstępnych, traktując wagę błędu jako interpretację roboczą. Zaproponuj ukierunkowaną wskazówkę, przypadek kontrastowy lub wyjaśnienie, a następnie nowe zadanie aplikacyjne. Pozwól na odłożenie zadania i powrót do niego w późniejszym czasie. Nie wprowadzaj arbitralnych progów typu 8/10 lub 90%, nie zakazuj podawania wyjaśnień ani nie przypisuj punktów do każdej drobnej interakcji. Stosuj jawne kryteria, gdy punktacja jest celowa; oficjalne ocenianie egzaminacyjne wymaga rzeczywistej specyfikacji egzaminu.

## Testy weryfikacyjne implementacji

Sprawdzaj tylko istotne ścieżki: pytanie → odpowiedź → informacja zwrotna; pomoc → dowód wykonania ze wsparciem; zmiana trybu po odsłonięciu odpowiedzi; pauza/wznowienie bez utraty lub podwójnego zaliczenia próby; nieaktualny lub uszkodzony plik stanu; spóźniona odpowiedź sieciowa po przełączeniu zadań; nierozstrzygnięta informacja zwrotna po błędzie technicznym. Upewnij się, że stan zapisany w pamięci i stan widoczny na ekranie są zgodne. Testy te weryfikują działanie techniczne, a nie skuteczność pedagogiczną.
