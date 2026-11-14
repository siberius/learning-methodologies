# Praktyka adaptacyjna i kontynuacja uczenia się

Przeczytaj ten dokument, gdy produkt wymaga wielokrotnych sesji, harmonogramowania powtórek lub doboru poziomu trudności. Rozróżniaj: kiedy powtórzyć materiał, jakie zadanie przedstawić i ile pomocy zaoferować. Poszczególne elementy nie muszą korzystać z tego samego modelu.

| Potrzeba | Prosta implementacja | Opcjonalne rozszerzenie i wymagania wstępne |
| --- | --- | --- |
| Pojedyncza aktywność | Zweryfikowane zadania, jawna sekwencja, pomoc i stan sesji | Zazwyczaj brak trwałego modelu ucznia |
| Przypominanie w odstępie dni | Jawny harmonogram powtórek i lokalna historia | FSRS dla stabilnych elementów i przejrzystych zdarzeń powtórkowych |
| Dobór trudności | Zweryfikowane poziomy zadań i przejrzyste rozgałęzienia | Ranking Elo przy odpowiednich danych o odpowiedziach, niepewności i kalibracji |
| Śledzenie zależności umiejętności | Mapa umiejętności z niezależnymi dowodami | BKT lub IRT wyłącznie przy uzasadnionym modelu, danych i walidacji |
| Plan długoterminowy | Cel, dostępny czas, bieżący etap i kolejne zadanie | Modyfikowalne kamienie milowe, pytania przeniesione i terminy powtórek |

Najpierw wyjaśnij funkcję dydaktyczną, a dopiero potem algorytm. Zachowaj istniejący stos technologiczny; nie instaluj harmonogramu, backendu ani systemu kont tylko dlatego, że zostały tu wymienione. Proste reguły zachowują pełną wartość, o ile ich ograniczenia są jawne. Model HLR to kolejny wytrenowany model przypominania dla odpowiednich danych, a nie domyślny wymóg implementacyjny.

## Warunki wstępne adaptacji

Zdefiniuj stabilne identyfikatory zadań i umiejętności, wersje treści, interpretację odpowiedzi oraz warunki udzielenia pomocy. Rozdzielaj odpowiedzi zgadnięte, udzielone z pomocą, po odsłonięciu rozwiązania oraz w pełni samodzielne. Przestrzegaj semantyki oceniania wybranej biblioteki; nie traktuj po cichu każdej odpowiedzi ze wsparciem jako samodzielnego przypomnienia. Przechowuj walutę gry poza modelem uczenia się. Stosuj minimalny zestaw danych i znaczniki czasu tylko tam, gdzie są niezbędne do planowania powtórek.

Określ zachowanie w stanie początkowym (cold-start) oraz bezpieczny mechanizm awaryjny (fallback), gdy historia jest niedostępna, uszkodzona lub nieaktualna. Zbadaj założenia na reprezentatywnych danych, uwzględniając język i warunki dostępu. Umożliw nauczycielowi wprowadzanie korekt, a uczniowi dostęp do pomocy. Przewidywany sukces jest obarczony niepewnością; ani arbitralny cel 80–90% sukcesu, ani dwie poprawne odpowiedzi nie wyznaczają strefy najbliższego rozwoju (ZPD) ani nie dowodzą mistrzostwa. Pożądany wskaźnik retencji to kompromis dotyczący nakładu pracy, a nie gwarantowany efekt kształcenia.

W przypadku wyboru algorytmu używaj utrzymywanej, zweryfikowanej pod kątem wersji biblioteki. Przetestuj aktualizacje, strefy czasowe i granice dni, zduplikowane odpowiedzi, zmiany w treści zadań, eksport/wznawianie sesji oraz nieprawidłowe dane wejściowe. Porównaj zaawansowane rozszerzenie z prostą wersją bazową; trafność predykcji, zaangażowanie i faktyczne uczenie się to odrębne rezultaty. Nie wnioskuj o niepełnosprawności ani cechach osobowości na podstawie samego czasu reakcji.

## Zakończenie lub wznowienie etapu nauki

Zarejestruj wynik, warunki udzielenia pomocy, nierozstrzygnięte pytania i wykonalny kolejny krok. Ukończenie etapu różni się od wykazania się opanowaniem wiedzy. Utworzenie nowego etapu nie kończy automatycznie poprzedniego. Podsumowania powinny zachowywać niezbędne wskaźniki dowodowe i stopień niepewności, a nie pełne transkrypcje rozmów. Po powrocie zweryfikuj zdezaktualizowane założenia za pomocą proporcjonalnego zadania; przerwy w nauce nie powinny kasować dotychczasowych postępów.

## Źródła

[Dokumentacja Anki FSRS](https://docs.ankiweb.net/manual/deck-options), [Pelánek o edukacyjnym rankingu Elo](https://www.fi.muni.cz/~xpelanek/publications/CAE-elo.pdf) oraz [Settles i Meeder o HLR](https://research.duolingo.com/papers/settles.acl16.pdf). Źródła te opisują konkretne modele i ustawienia; nie dowodzą skuteczności nowo powstającej aplikacji. Przy integracji biblioteki należy sprawdzić jej aktualną dokumentację implementacyjną.
