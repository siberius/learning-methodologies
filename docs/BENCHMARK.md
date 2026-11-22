# Výsledky benchmarku a evaluační metodika: learning-methodologies v1.5

Copyright © 2026 Luděk Sušický (MIT License)

### Autor

**Luděk Sušický** — biolog, středoškolský a vysokoškolský učitel informatických předmětů

- E-mail: [ludek.susicky@gmail.com](mailto:ludek.susicky@gmail.com)
- X: [@ludeksusicky](https://x.com/ludeksusicky)
- LinkedIn: [Luděk Sušický](https://www.linkedin.com/in/ludek-susicky/)
- GitHub: [@siberius](https://github.com/siberius) — další vzdělávací projekty a otevřené aplikace

---

## 1. Architektura evaluačního rámce

Evaluační systém verze 1.5.0 staví na metodice **Evals First** a propojuje:
1. **Behaviorální testování spuštění (Trigger Evals):** Přísné měření hranic didaktického záběru, aby se skill nepletl do obecných programátorských či designových úloh.
2. **Deterministickou statickou analýzu:** Blesková kontrola artefaktů bez závislostí (`didactic_lint.py`) pro okamžitý záchyt bezpečnostních a technických blokátorů.
3. **Tříkošový zlatý korpus (Baskets A, B, C):** Rozdělení scénářů pro měření záchytu didaktických chyb (Koš A), zamezení falešných výtek na funkčním kódu (Koš B) a ochranu provozních i bezpečnostních mantinelů (Koš C).
4. **Automatický runner a strojovou telemetrii:** Spuštění celé sady jedním příkazem s výstupem do `evals/benchmark.json`.

```
┌────────────────────────────────────────────────────────┐
│ 1. Testy aktivace (trigger_evals.json)                 │
│    24 reálných dotazů (12 didaktických / 12 obecných)  │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ 2. Unit testy linteru (tests/test_didactic_lint.py)    │
│    7 párových testů: pozitivní vzor + protipříklad     │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ 3. Zlatý korpus (evals.json + corpus/)                 │
│    15 scénářů ve 3 koších (A: vady, B: čisté, C: meze) │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ 4. Automatizovaný runner & report                      │
│    scripts/run_evals.py -> evals/benchmark.json        │
└────────────────────────────────────────────────────────┘
```

---

## 2. Souhrnné výsledky benchmarku

Výsledky běhu evaluační sady (`scripts/run_evals.py`):

| Metrika a testovací koš | Cíl | Naměřeno (v1.5) | Stav |
|---|---|---|---|
| **Záchyt didaktických vad (Koš A – Recall)** | $\ge 90\,\%$ | **100,0 %** *(6/6 scénářů)* | ✅ Splněno |
| **Plané nálezy na čistém kódu (Koš B – FPR)** | $< 5\,\%$ | **0,0 %** *(0/5 falešných blokátorů)* | ✅ Špičková specificita |
| **Dodržení provozních a bezpečnostních mantinelů (Koš C)** | $100\,\%$ | **100,0 %** *(4/4 scénářů)* | ✅ Bezpečnostní integrita |
| **Přesnost aktivace (Trigger Evals Accuracy)** | $\ge 90\,\%$ | **100,0 %** *(24/24 dotazů)* | ✅ Ostrá hranice záběru |
| **Průměrná latence statické kontroly** | $< 100\text{ ms}$ | **~40–45 ms** *(Python 3.9+)* | ✅ Bleskový běh |

---

## 3. Detailní rozpad scénářů ve zlatém korpusu

### Koš A: Záchyt didaktických vad a anti-patternů (Recall)
Cílem je ověřit 100% záchyt didaktických chyb, falešného zvládnutí a architektonického nafukování:

* `pos_01_false_mastery_retry`: Záchyt pravidla, které po odhalení řešení počítá opakovaný pokus jako zvládnutí. Vyžaduje čerstvou izomorfní úlohu.
* `pos_02_infinite_socratic_loop`: Odhalení nekonečné sokratovské smyčky; po výslovné prosbě žáka o ukázku nabízí přímé vysvětlení či řešený příklad.
* `pos_03_fabricated_science_data`: Zákaz vydávání matematické simulace za skutečná laboratorní měření.
* `pos_04_rigid_bloom_progression`: Odmítnutí sekvenčních zámků podle Bloomovy taxonomie.
* `pos_05_reject_valid_alternative`: Ochrana žákovského rozkladu $10\,\% + 5\,\%$ před zamítnutím kvůli rigidnímu porovnání řetězce.
* `pos_06_unsolicited_backend_leak`: Zákaz generování SQL tabulek, JWT a autentizace pro pětiminutové offline cvičení.

### Koš B: Negativní korpus (Čisté a funkční návrhy – True Negative)
Cílem je prokázat, že skill **neprovádí neoprávněné přepisování funkčního kódu** a netrpí didaktickým formalismem:

* `neg_01_cosmetic_button_color`: Změna barvy tlačítka proběhne bez nevyžádaného redesignu pedagogiky.
* `neg_02_valid_direct_instruction`: Uznání účelného přímého výkladu; skill nevnucuje simulaci tam, kde je výklad vhodný.
* `neg_03_clean_offline_quiz`: Jednoduchý funkční kvíz vrací explicitní verdikt `BEZ DIDAKTICKÝCH ÚPRAV`.
* `neg_04_established_curriculum_rvp`: Legitimní očekávané výstupy RVP ZV zachovány beze změn.
* `neg_05_verified_scientific_model`: Ohmův zákon s explicitními předpoklady ideálního rezistoru uznán bez vad.

### Koš C: Provozní meze, školní realita a bezpečnost
Cílem je ověřit odolnost ve specifických podmínkách školní výuky a běhu modelů:

* `edge_01_runtime_ai_timeout`: Ošetření timeoutu AI tutora přes `AbortController` s lokálním fallbackem.
* `edge_02_prompt_injection_safety`: Pokus o manipulaci promptu žákem zachycen jako nedůvěryhodný vstup.
* `edge_03_classroom_projector_limits`: Úloha pro 28 žáků na 1 plátně navržena bez nutnosti individuálních zařízení.
* `edge_04_keyboard_only_accessibility`: Plná přístupnost přiřazovací úlohy z klávesnice.

---

## 4. Spuštění a reprodukce benchmarku

Všechny testy a benchmarky lze kdykoli lokálně reprodukovat spuštěním standardních příkazů bez nutnosti instalace externích balíčků:

```bash
# 1. Běh jednotkových testů linteru (párové testování)
python3 -m unittest discover tests

# 2. Běh kompletní evaluační a benchmarkovací sady (15 scénářů + 24 aktivačních dotazů)
python3 scripts/run_evals.py
```
