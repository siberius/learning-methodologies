# Sztuczna inteligencja w fazie wykonawczej (runtime) w aplikacjach edukacyjnych

Przeczytaj ten dokument tylko wtedy, gdy gotowa aplikacja odwołuje się do usługi AI w trakcie jej użytkowania przez uczniów. Używanie AI do pisania kodu lub generowania treści sprawdzanych przez nauczyciela nie wymaga obecności AI w środowisku wykonawczym. Pozostaw aktywności offline w trybie offline, chyba że cel dydaktyczny bezwzględnie wymaga usługi sieciowej.

## Zdefiniuj ograniczoną rolę dydaktyczną

Określ, co model może robić, z jakich zweryfikowanych treści lub źródeł może korzystać oraz jak powinien reagować na brakujące dowody. W sytuacjach, gdzie kluczowa jest poprawność faktograficzna, zidentyfikuj zatwierdzone materiały i zachowaj ich pochodzenie źródłowe. Nie dopuszczaj do generowania zmyślonych, choć wiarygodnie wyglądających cytowań. Dopuszczaj niepewność i korygowanie twierdzeń; unikaj diagnozowania uczniów i kategorycznych sądów o ich zdolnościach na podstawie krótkiej interakcji.

Dobieraj formę wsparcia do charakteru aktywności. Ćwiczenia mogą wykorzystywać pytania naprowadzające, stopniowane wskazówki, przykłady z rozwiązaniem oraz bezpośrednie wyjaśnienie na życzenie lub wtedy, gdy pytania przestają pomagać. Sprawdzian może ograniczać pomoc zgodnie z zasadami określonymi przez nauczyciela. Nie narzucaj niekończącej się pętli sokratejskiej ani bezwzględnego zakazu podawania odpowiedzi. Zapewnij uczniowi możliwość poproszenia o pomoc, przerwania pracy lub zaangażowania nauczyciela.

Projektuj interfejsy AI na żywo tak, aby przeciwdziałać biernemu kopiowaniu, w którym narzędzie myśli za ucznia. Przed zaakceptowaniem wygenerowanej procedury lub odpowiedzi wymagaj od ucznia krótkiej weryfikacji: doprecyzowania intencji przed wysłaniem zapytania, zatrzymania się nad wynikiem (pauza poznawcza), oceny kompletności i poprawności oraz wyboru kolejnego kroku (kontynuacja, weryfikacja, przeredagowanie lub decyzja o rezygnacji z podpowiedzi).

Stosuj jawne rubryki kryteriów do generowania informacji zwrotnej i oceny odpowiedzi otwartych. Porównuj oceny modelu z przykładami sprawdzonymi przez nauczycieli, zanim na nich polegasz. Istotne decyzje dotyczące oceniania, kwalifikacji lub kwestii dyscyplinarnych wymagają odpowiedzialnej weryfikacji przez człowieka; pojedyncza odpowiedź modelu nie może być jedynym decydentem. Odnotowuj niepewność i umożliw nauczycielowi skorygowanie oceny.

## Minimalizacja danych uczniów

Wskaż dane wejściowe przesyłane do dostawcy usługi, zakres ich przechowywania, osoby mające do nich dostęp oraz procedurę ich usuwania. Zbieraj wyłącznie to, co jest niezbędne do przeprowadzenia aktywności. Nie wprowadzaj automatycznie kont użytkowników, imion i nazwisk, trwałych profili ani rejestrowania pełnych konwersacji. Używaj anonimowych lub pseudonimowych identyfikatorów sesji tam, gdzie to wystarcza, mając świadomość, że nie gwarantują one pełnej anonimowości.

Przed wdrożeniem z udziałem osób niepełnoletnich sprawdź docelową grupę wiekową, ustalenia ze szkołą, warunki świadczenia usług dostawcy i obowiązujące lokalne przepisy prawa z właściwą instytucją. Nie twórz uniwersalnego wieku zgody ani sztucznych reguł prawnych. Wyjaśnij zasady przetwarzania danych uczniom i nauczycielom w przystępnym języku.

## Zastosuj zabezpieczenia architektoniczne

Przechowuj dane uwierzytelniające do usług (klucze API) w chronionym komponencie po stronie serwera, gdy usługa zdalna wymaga kluczy prywatnych. Nigdy nie ujawniaj ich w kodzie uruchamianym w przeglądarce. Egzekwuj autoryzację, limity zapytań i uprawnienia narzędzi poza promptem. Traktuj dane wprowadzane przez uczniów, pobierane dokumenty oraz odpowiedzi modelu jako dane niezaufane.

Oddzielaj instrukcje od dostarczanych treści, ograniczaj dostęp do narzędzi i miejsc docelowych, waliduj ustrukturyzowane odpowiedzi i oczyszczaj renderowane treści (sanitaryzacja HTML/JS). Zabezpiecz aplikację przed bezpośrednim przekształcaniem tekstu wygenerowanego przez model w kod wykonywalny lub działania uprzywilejowane. Prompt nakazujący modelowi ignorowanie wstrzykiwania instrukcji (prompt injection) nie stanowi gwarancji bezpieczeństwa. Zapewnij dedykowany przegląd bezpieczeństwa dla zaimplementowanej architektury.

## Planowanie kosztów, awarii i ciągłości działania

Ustal realistyczny budżet wykorzystania, limity na sesję, czasy oczekiwania (timeouts) i możliwość anulowania zapytań. Zapewnij zrozumiały stan interfejsu w trakcie oczekiwania na odpowiedź. Zabezpiecz aplikację przed utratą połączenia sieciowego, niedostępnością modelu, nieprawidłowymi danymi wyjściowymi i wyczerpaniem limitów bez utraty dotychczasowej pracy ucznia. Ponawiaj próby tylko wtedy, gdy jest to bezpieczne i ograniczone liczbowo.

Zaoferuj odpowiedni mechanizm awaryjny (fallback), taki jak zweryfikowane wskazówki statyczne, ćwiczenia standardowe, zapisany postęp lub pomoc nauczyciela. Oznacz niedostępną informację zwrotną zamiast ją zmyślać. Przed użyciem w klasie przetestuj: główną ścieżkę uczenia się, odpowiedź błędną, prośbę o pomoc, niejednoznaczną informację zwrotną oraz awarię usługi. Udokumentuj nierozstrzygnięte ograniczenia i obowiązki weryfikacyjne nauczyciela.

## Weryfikacja generowanych treści w określonych granicach

Przed udostępnieniem wygenerowanych zadań przeprowadź odpowiednie testy poprawności dziedzinowej, rozwiązywalności, przejść stanów i renderowania. Wymagaj unikalności tylko od zadań, które wyraźnie to deklarują. Waliduj uprawnienia i granice danych ustrukturyzowanych poza modelem; schemat JSON nie dowodzi prawdziwości danych, a testy deterministyczne gwarantują tylko te własności, które faktycznie sprawdzają. Odrzucaj lub izoluj nieprawidłowe treści i zachowaj zweryfikowaną bazę zapasową. W przypadku korygowania powiązanych wskazówek, ocen i postępów stosuj procedurę naprawczą opisaną w `assessment.md`.
