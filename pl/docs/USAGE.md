# Użycie i instalacja

## Wybór właściwego punktu wejścia

Stosuj ten skill przy projektowaniu nowej aplikacji edukacyjnej, istotnej zmianie jej struktury dydaktycznej lub ewaluacji projektu pedagogicznego. Zmiana czysto wizualna lub zwykła poprawka techniczna nie wymaga przebudowy dydaktycznej.

Podaj znane informacje o uczniach, celu, kontekście i ograniczeniach praktycznych. Agent powinien wykorzystać istniejące informacje i zapytać wyłącznie o istotne luki w kontekście oraz nierozstrzygnięte wybory pedagogiczne. Nie powinien powtarzać sztywnego wywiadu o odbiorcach i tonie ani żądać zatwierdzania rutynowych decyzji projektowych objętych już Twoim poleceniem.

## Prowadzenie przez decyzje w trakcie tworzenia

Skill oferuje kilka adekwatnych opcji dydaktycznych, gdy pojawia się nowy istotny wybór: zwięzłe wyjaśnienie, konkretny przykład i rekomendację. Pamięta Twoje wybory i łączy je z implementacją oraz weryfikacją. Możesz powiedzieć: „wybierz rutynowe decyzje za mnie”, aby przekazać decyzje agentowi, lub poprosić o ponowne porównanie alternatyw. Niewielkie aktywności offline zachowują swój zwarty charakter. Karty metod, wytyczne dotyczące interfejsu poznawczego i opcjonalna praktyka adaptacyjna wspierają ten proces.

## Instalacja przez skills.sh CLI

Wybierz jedną wersję językową za pomocą narzędzia [Skills CLI](https://github.com/vercel-labs/skills). Flaga `-g` oznacza instalację na poziomie użytkownika, a `-a codex` wybiera klienta Codex. Zastąp ją `-a claude-code` dla Claude Code lub pomiń opcję agenta, aby dokonać wyboru interaktywnie. Instaluj tylko te wersje, z których faktycznie korzystasz.

```bash
npx skills add siberius/learning-methodologies --skill metodyki-nauczania --full-depth -g -a codex
```

Bez flagi `--agent` polecenie `skills use` wyświetla przygotowany prompt. Aby uruchomić obsługiwanego agenta tymczasowo z tym skillem:

```bash
npx skills use siberius/learning-methodologies --skill metodyki-nauczania --full-depth --agent codex
```

## Pakiet natywny skilla

Utrzymuj pliki `SKILL.md`, `LICENSE` i katalog `references/` w jednym folderze skilla, standardowo o nazwie `metodyki-nauczania`. Skorzystaj z mechanizmu instalacji skilli obsługiwanego przez Twojego klienta. Samo umieszczenie pliku Markdown na dysku nie gwarantuje automatycznego wykrycia.

W przypadku klientów korzystających z katalogu `~/.agents/skills` przykładową ścieżką docelową jest:

```text
~/.agents/skills/metodyki-nauczania/
  SKILL.md
  references/
  LICENSE
```

W przypadku Claude Code odpowiadającym katalogiem jest zazwyczaj `~/.claude/skills/metodyki-nauczania/`. Zachowaj istniejące pliki użytkownika; sprawdź potencjalne konflikty przed instalacją. Potwierdź wykrycie skilla w docelowym kliencie. Sam fakt instalacji nie dowodzi, że agent faktycznie użył skilla.

## Autonomiczny Markdown

Przekaż agentowi zdolnemu do wykonywania instrukcji wygenerowany plik `metodyki-nauczania.md` i wyraźnie poproś o jego użycie w danym zadaniu. Zawiera on warunkowe referencje jako wbudowane sekcje i nie zależy od plików względnych. Ścieżka ta wczytuje więcej tekstu na początku, ale wymaga tylko jednego pliku z instrukcjami.

Nazwy modeli nie są mechanizmami instalacji. Zgodność zależy od zdolności środowiska nadrzędnego do wczytywania i stosowania instrukcji w formacie Markdown, jego narzędzi i uprawnień.

## Praca według potrzeb

| Potrzeba | Właściwe wytyczne |
|---|---|
| Tryby tutora, wznawianie nauki i punkty kontrolne | `references/tutor-state.md` |
| Dlaczego metoda jest odpowiednia i jak zmienia aplikację | `references/didactic-rationale.md` |
| Ogólny projekt, audyt lub zakres | Rdzeń w `SKILL.md` |
| Niejasna pomoc, alternatywne odpowiedzi lub roszczenia programowe | `references/decision-examples.md` |
| Wybór metody, pomoc lub progresja | `references/methods.md` |
| Punktacja, rubryki, adaptacyjność lub dowody uczenia się | `references/assessment.md` |
| Model naukowy, eksperyment lub odgrywanie ról | `references/simulations.md` |
| Usługa AI w gotowej aplikacji (runtime) | `references/runtime-ai.md` |
| Model, nakład pracy, szybkość lub adaptacja do klienta | `references/model-profiles.md` |
| Wybory twórcy i ciągłość decyzji | `references/design-dialogue.md` |
| Reprezentacje, multimedia i uwaga | `references/cognitive-ux.md` |
| Harmonogram powtórek i dobór trudności | `references/adaptive-practice.md` |
| Mechaniki gry, motywacja i transfer | `references/learning-games.md` |

Nie ładuj wszystkich referencji automatycznie w trybie natywnym. Quiz offline może zapewniać informację zwrotną i wskazówki bez użycia runtime AI. Pokaz prowadzony przez nauczyciela może wymagać pytań do dyskusji zamiast indywidualnych rejestrów. Stosuj jedną lub kilka perspektyw w zależności od zadania, bez automatycznego uruchamiania wielu agentów.

## Utrzymanie edycji językowych

Źródłami autorskimi są `SKILL.md` i powiązane referencje warunkowe. Plik autonomiczny jest wygenerowanym artefaktem dystrybucyjnym. W kopii roboczej maintainera przebudujesz go za pomocą:

```sh
python3 testing/build_portable.py --edition pl
python3 testing/build_portable.py --edition pl --check
python3 testing/build_portable.py --edition all --check
```

Skrypt budujący znajduje się w lokalnych narzędziach deweloperskich. Użytkownicy dystrybucji mogą korzystać z gotowych wydań bez konieczności jego uruchamiania. Osadza on referencje z unikalnymi kotwicami, dzięki czemu powtarzające się nagłówki pozostają jednoznaczne.

Dbaj o spójność plików README i przykładów nauczycielskich z rdzeniem skilla. Zachowaj informacje o autorze, wersji, pochodzeniu i licencji MIT. Dostępne są edycje: angielska (`en`), czeska (`cs`), rosyjska (`ru`), hiszpańska (`es`) oraz polska (`pl`). Każda zachowuje wspólne zasady dydaktyczne; lokalne wskazówki programowe pozostają warunkowe. Generuj wybraną edycję za pomocą `--edition` z kodem języka lub wszystkie naraz za pomocą `--edition all`.

## Recenzja i ocena rezultatu

Sprawdź zamierzone działanie ucznia i dowód uczenia się, poprawność merytoryczną, informację zwrotną, pomoc, dostępność i ograniczenia operacyjne właściwe dla Twojej aplikacji. Odróżniaj działanie techniczne, poprawność dydaktyczną i rzeczywiste efekty uczenia się. Jasno określ, co zostało zweryfikowane, a co pozostaje nieznane.

Opublikowany [protokół ewaluacji modeli obejmujący osiem zadań](MODEL-EVALUATION.md) zawiera porównywalne zadania i kryteria oceny. Nie umieszczaj tych kryteriów w prompcie testowanego modelu. Pakiet jest przygotowany, a nie z góry wykonany; wcześniejsze testy eksploracyjne nie gwarantują niezawodności u różnych dostawców. Raportuj tylko te ewaluacje, które faktycznie przeprowadzono, oddzielając wyniki początkowe od poprawek.

Dobieraj model według złożoności zadania, a nie jego nazwy handlowej. Jeśli istotne kryterium nadal nie jest spełnione po ukierunkowanej poprawce, postępuj zgodnie z regułami eskalacji i zatrzymania w referencji modeli. Brakujących źródeł ani narzędzi nie naprawi samo zwiększenie nakładu pracy (effort). Standardowa szybkość obsługi to punkt wyjścia; płatna akceleracja wymaga odrębnej autoryzacji.
