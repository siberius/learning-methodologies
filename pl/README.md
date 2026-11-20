# Metodyki nauczania: projektowanie dydaktyczne dla aplikacji AI

[![Skills.sh](https://img.shields.io/badge/skills.sh-Install-blue)](https://skills.sh/siberius/learning-methodologies)

[English](../README.md) · [Čeština](../cs/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md)

Przenośny skill AI do projektowania, wdrażania i ewaluacji aplikacji edukacyjnych. Łączy cele kształcenia, aktywność uczniów, informację zwrotną i dowody uczenia się, pomagając przekładać te decyzje na obserwowalne zachowanie aplikacji.

Polska edycja dzieli międzynarodową bazę metodologiczną skilla, nie narzucając z góry jednego sztywnego programu nauczania, zewnętrznych usług AI, kont użytkowników ani konkretnego modelu.

## Autor

**Luděk Sušický** — biolog, nauczyciel przedmiotów informatycznych w szkole średniej i na uczelni wyższej

- E-mail: [ludek.susicky@gmail.com](mailto:ludek.susicky@gmail.com)
- X: [@ludeksusicky](https://x.com/ludeksusicky)
- LinkedIn: [Luděk Sušický](https://www.linkedin.com/in/ludek-susicky/)
- GitHub: [@siberius](https://github.com/siberius) — więcej projektów edukacyjnych i otwartych aplikacji

Licencja MIT. Wersja: **1.6.0**. Wszystkie wersje językowe zawierają zwięzłą ścieżkę pracy, przykłady decyzji projektowych, tryby tutora i ciągłość nauki, mapy pojęciowe, wytyczne tworzenia tekstów dla uczniów bez żargonu AI oraz jawne reguły doboru modelu i eskalacji rozumowania. Wskazane konfiguracje modeli są punktem wyjścia, a nie wynikiem formalnego benchmarku.

Skill oferuje kilka adekwatnych opcji dydaktycznych przy każdym nowym istotnym wyborze: krótkie wyjaśnienie, konkretny przykład i rekomendację. Pamięta wybory i łączy je z implementacją oraz testami. Poleceniem „wybierz rutynowe decyzje za mnie” możesz przekazać wybory agentowi lub w dowolnym momencie poprosić o ponowne zestawienie alternatyw. Niewielkie pomoce offline zachowują prosty charakter. Karty metod, wytyczne dotyczące interfejsu poznawczego i opcjonalna praktyka adaptacyjna wspierają ten proces.

## Do czego służy

- Dobór metod dydaktycznych do konkretnej potrzeby edukacyjnej i warunków w klasie.
- Wspieranie samoregulacji poznawczej uczniów we wspólnej przestrzeni z AI (ramy FALR: Focus, Action, Learn, Reflect), przeciwdziałające bezrefleksyjnemu kopiowaniu odpowiedzi.
- Projektowanie użytecznej pomocy, informacji zwrotnej po błędach i samodzielnych ćwiczeń.
- Rozdzielanie celów, trudności zadań, wymagań wstępnych i dowodów opanowania wiedzy.
- Budowa wiarygodnych symulacji i kontrolowanego tutoringu AI tam, gdzie jest to uzasadnione.
- Uwzględnianie dostępności cyfrowej (WCAG 2.2), kontroli nauczyciela, ochrony danych uczniów i ograniczeń operacyjnych.
- Wyraźne odróżnianie działającej aplikacji technicznej, poprawnego projektu dydaktycznego i rzeczywistych efektów uczenia się.
- Dobór modelu, nakładu pracy (effort/thinking) i szybkości na podstawie aktualnych wskazówek OpenAI, Claude i Gemini, z jawnym określeniem stanu weryfikacji.

Omawiane metody obejmują dialog sokratejski, technikę Feynmana, strefę najbliższego rozwoju (ZPD) i rusztowanie poznawcze (scaffolding), przykłady z rozwiązaniem (worked examples), praktykę przypominania i powtórki rozłożone w czasie, metapoznanie, dociekanie (inquiry), odgrywanie ról, uczenie się rówieśnicze i kooperatywne, metodę projektów oraz klasę odwróconą. Są to opcje dobierane do zadania; instalacja skilla nie nakłada obowiązku ich stosowania we wszystkich projektach.

## Instalacja i szybki start

Zainstaluj wersję językową za pomocą narzędzia [Skills CLI](https://github.com/vercel-labs/skills). Flaga `-g` oznacza instalację dla użytkownika, a `-a codex` wybiera klienta Codex. Dla Claude Code użyj `-a claude-code` lub pomiń opcję agenta, aby wybrać go interaktywnie. Instaluj tylko te wersje, z których korzystasz.

```bash
npx skills add siberius/learning-methodologies@v1.6.0 --skill metodyki-nauczania --full-depth -g -a codex
```

Tag instaluje zawartość tego wydania; domyślna gałąź może być nowsza. CLI zapisuje w `skills-lock.json` rozwiązany commit i hash zainstalowanych plików, a `npx skills check` zgłasza zmiany lokalne.

Aby wypróbować skill w jednym projekcie, pomiń `-g`, a potem usuń kopię przez `npx skills remove metodyki-nauczania`. Klienci czytający Markdown bezpośrednio mogą użyć [pliku autonomicznego](metodyki-nauczania.md) bez instalatora; [instrukcja użycia](docs/USAGE.md) opisuje ręczny układ pakietu.

## Wybór formatu

- [SKILL.md](SKILL.md) i katalog `references/`: pakiet natywny z referencjami ładowanymi warunkowo według potrzeb. Utrzymuj pliki w jednym katalogu.
- [metodyki-nauczania.md](metodyki-nauczania.md): wygenerowany plik autonomiczny dla agentów przyjmujących bezpośrednio instrukcje w formacie Markdown. Zawiera rdzeń i wszystkie referencje.

Oba formaty powstają z tych samych źródeł autorskich. Edytuj `SKILL.md` oraz odpowiednie referencje, a następnie wygeneruj wersję autonomiczną. Nie modyfikuj wygenerowanego pliku oddzielnie.

## Przykładowe polecenie

> Użyj skilla metodyki-nauczania, aby zbudować aktywność offline o obwodach elektrycznych dla uczniów w wieku 16 lat. Uczniowie powinni przewidywać, jak opór zmienia natężenie prądu i uzasadniać swoje rozumowanie. Aktywność posłuży dyskusji kierowanej przez nauczyciela i musi być w pełni obsługiwana z klawiatury. Bez kont użytkowników i zewnętrznych wywołań AI.

Agent wykorzysta ten kontekst, dobierze wsparcie proporcjonalne do zadania i określi, w jaki sposób aktywność uwidoczni zrozumienie tematu. Zapyta tylko o brakujące informacje zmieniające projekt.

## Dokumentacja

- [Użycie i instalacja](docs/USAGE.md)
- [Przewodnik dla nauczyciela i przykładowe briefy](docs/TEACHERS.md)
- [Ewaluacja modeli (protokół 8 zadań)](docs/MODEL-EVALUATION.md)
- [Historia wersji](../CHANGELOG.md)

## Edycje językowe

| Język | Pakiet natywny i dokumentacja | Plik autonomiczny |
|---|---|---|
| Angielski | [English](../README.md) | [learning-methodologies.md](../learning-methodologies.md) |
| Czeski | [Čeština](../cs/README.md) | [vzdelavaci-metodiky.md](../cs/vzdelavaci-metodiky.md) |
| Rosyjski | [Русский](../ru/README.md) | [metodiki-obucheniya.md](../ru/metodiki-obucheniya.md) |
| Hiszpański | [Español](../es/README.md) | [metodologias-de-aprendizaje.md](../es/metodologias-de-aprendizaje.md) |
| Polski | [Polski](README.md) | [metodyki-nauczania.md](metodyki-nauczania.md) |

Wersje polska, hiszpańska i rosyjska tłumaczą międzynarodową bazę bez narzucania programu nauczania jednego państwa. Wersja czeska zawiera warunkowe odniesienia do RVP/ŠVP. Wybierz jedną wersję właściwą dla danego zadania.

Sam proces projektowy stanowi wsparcie dydaktyczne. Nie certyfikuje on dostępności, poprawności merytorycznej ani skuteczności kształcenia. Stosuj testy i weryfikację adekwatne do przedmiotu, uczniów i wagi decyzji.

## Licencja

MIT, copyright 2026 Luděk Sušický. Zobacz [LICENSE](LICENSE). Zachowaj informacje o prawach autorskich i licencji przy redystrybucji dowolnego formatu.

## Dlaczego te metody kierują tworzeniem aplikacji z AI

Zastosowane metody dydaktyczne pozwalają przełożyć zamierzenia edukacyjne na działania uczniów i reakcje systemu. Praktyka przypominania decyduje o momencie odsłonięcia odpowiedzi, rusztowanie poznawcze organizuje pomoc, ocenianie wyznacza granice wnioskowania z wyników, a ramy samoregulacji (FALR) chronią aktywny udział ucznia w pracy z AI. Zobacz [uzasadnienie dydaktyczne](references/didactic-rationale.md), aby zapoznać się z przykładami i granicami poszczególnych metod.
