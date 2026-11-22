#!/usr/bin/env python3
"""
didactic_lint.py - Deterministický statický kontrolor vzdělávacích softwarových artefaktů.

Autor: Luděk Sušický (MIT License)
Popis: Autorský nástroj pro rychlou kontrolu didaktických, přístupnostních
a bezpečnostních parametrů vzdělávacího softwaru (HTML, JS, JSON, MD).
Běží v čistém Pythonu 3.9+ bez externích závislostí.

Návratové kódy:
  0 - Artefakt je čistý (žádné blokátory ani podezřelí kandidáti -> BEZ DIDAKTICKÝCH ÚPRAV)
  1 - Nalezeny tvrdé deterministické blokátory (hard_lint)
  2 - Nalezeny pouze měkké didaktické podněty k posouzení (soft_candidates)
  3 - Chyba vstupu nebo parametrů
"""

import argparse
import json
import os
import re
import sys
from typing import Any, Dict, List, Optional, Tuple

# Tvrdé blokátory (hard_lint)
RE_HARDCODED_AI_SECRET = re.compile(
    r"""(?i)(?:sk-[a-zA-Z0-9_\-]{20,}|(?:api[_-]?key|secret[_-]?token)\s*[:=]\s*["'][a-zA-Z0-9_\-]{16,}["'])"""
)
RE_DRAGGABLE_ELEMENT = re.compile(r"""draggable\s*=\s*["']true["']|addEventListener\s*\(\s*["']drag(?:start|over|drop)["']""", re.IGNORECASE)
RE_KEYBOARD_LISTENER = re.compile(r"""addEventListener\s*\(\s*["']key(?:down|up|press)["']|onkeydown|onkeyup|role\s*=\s*["']button["']\s+tabindex|tabindex\s*=\s*["']0["']""", re.IGNORECASE)

RE_UNHANDLED_AI_FETCH = re.compile(
    r"""fetch\s*\([^)]*(?:api\.openai\.com|/api/ai|/v1/chat|/v1/completions)[^)]*\)""",
    re.IGNORECASE
)
RE_ABORT_SIGNAL = re.compile(r"""(?:AbortController|signal\s*:|timeout\s*:)""", re.IGNORECASE)

RE_RIGID_BLOOM_LEVELS = re.compile(
    r"""(?:BLOOM_LEVELS\s*=\s*\[|const\s+BLOOM_STAGES|currentBloomLevel\s*<=\s*requiredLevel)""",
    re.IGNORECASE
)

RE_FALSE_MASTERY_RETRY = re.compile(
    r"""(?:solutionRevealed|hintGiven|answerShown)\s*&&\s*[^;]*(?:isMastered\s*=\s*true|masteryStatus\s*=\s*["']mastered["']|recordSuccess\(item\))""",
    re.IGNORECASE
)

RE_STRICT_STRING_MATCH = re.compile(
    r"""(?:input|answer|val)(?:\.trim\(\))?\s*===\s*["'][^"']+["'](?!\s*\|\|\s*(?:input|answer|val))""",
    re.IGNORECASE
)

# Měkcí kandidáti k posouzení (soft_candidates)
SOFT_PATTERNS: List[Tuple[str, str, str, str]] = [
    (
        "unverified_efficacy_claim",
        r"\b(?:zdvojnásobuje\s+paměť|vědecky\s+prokázané\s+učení|garantuje\s+naučení|100%\s+úspěšnost\s+přijetí|doubles\s+retention|scientifically\s+proven\s+learning)\b",
        "efficacy_claim",
        "Neověřené tvrzení o účinnosti: doložte konkrétní studii, jinak tvrzení zjemněte na popis funkčnosti."
    ),
    (
        "invented_scientific_data",
        r"\b(?:reálná\s+naměřená\s+data|skutečné\s+laboratorní\s+výsledky|real\s+measured\s+data|actual\s+experimental\s+results)\b",
        "scientific_integrity",
        "Ověřte původ dat: pokud jde o matematický/simulační model, explicitně jej označte jako ilustrační model."
    ),
    (
        "unsolicited_account_infra",
        r"\b(?:CREATE\s+TABLE\s+users|jwt\.sign|bcrypt\.hash|POST\s+/api/auth/register|user_password_hash)\b",
        "architecture_bloat",
        "Nafouknutí architektury: pro krátké classroom či offline cvičení nevyžadujte uživatelské účty ani autentizaci."
    ),
    (
        "unbounded_questioning",
        r"(?:nerozumím|ukažte\s+mi|prosím\s+ukažte|don't\s+understand|please\s+show\s+me)[\s\S]{1,250}\?[^?]*$",
        "pedagogical_loop",
        "Riziko nekonečné sokratovské smyčky: po neúspěchu a prosbě o ukázku nabídněte přímé vysvětlení nebo vzorový příklad místo další otázky."
    )
]


def lint_text(content: str, filename: str = "") -> Dict[str, Any]:
    """Provede deterministickou statickou analýzu obsahu."""
    hard_lint: List[Dict[str, Any]] = []
    soft_candidates: List[Dict[str, Any]] = []

    lines = content.splitlines()

    # 1. Hard Check: Vystavené API klíče
    for idx, line in enumerate(lines, 1):
        match = RE_HARDCODED_AI_SECRET.search(line)
        if match:
            val = match.group(0)
            if not any(dummy in val for dummy in ["sk-test", "sk-proj-0000", "dummy", "placeholder", "YOUR_API_KEY"]):
                hard_lint.append({
                    "rule": "HARDCODED_AI_SECRET",
                    "severity": "BLOCKER",
                    "line": idx,
                    "evidence": val[:30] + "...",
                    "message": "Nalezen klientsky vystavený API klíč. API klíč musí zůstat na zabezpečeném serveru."
                })

    # 2. Hard Check: Drag-and-drop bez klávesové obsluhy
    if RE_DRAGGABLE_ELEMENT.search(content):
        if not RE_KEYBOARD_LISTENER.search(content):
            hard_lint.append({
                "rule": "DRAG_DROP_NO_KEYBOARD",
                "severity": "BLOCKER",
                "line": 1,
                "evidence": "draggable=true / drag events present without keydown handlers",
                "message": "Interaktivní prvek drag-and-drop postrádá plnohodnotné ovládání z klávesnice (WCAG 2.2.1.1)."
            })

    # 3. Hard Check: Nekontrolované volání AI API bez timeoutu
    for idx, line in enumerate(lines, 1):
        if RE_UNHANDLED_AI_FETCH.search(line):
            start_ctx = max(0, idx - 4)
            end_ctx = min(len(lines), idx + 5)
            context_block = "\n".join(lines[start_ctx:end_ctx])
            if not RE_ABORT_SIGNAL.search(context_block):
                hard_lint.append({
                    "rule": "UNHANDLED_AI_FETCH",
                    "severity": "BLOCKER",
                    "line": idx,
                    "evidence": line.strip()[:60],
                    "message": "Volání runtime AI postrádá timeout (AbortController) a záložní offline cestu."
                })

    # 4. Hard Check: Falešné zvládnutí (False mastery retry)
    for idx, line in enumerate(lines, 1):
        if RE_FALSE_MASTERY_RETRY.search(line):
            hard_lint.append({
                "rule": "RETRY_EXPOSURE_FALSE_MASTERY",
                "severity": "BLOCKER",
                "line": idx,
                "evidence": line.strip()[:60],
                "message": "Pravidlo započítává opakovaný pokus po zobrazení nápovědy/řešení jako samostatné zvládnutí."
            })

    # 5. Hard Check: Rigidní sekvence Bloomovy taxonomie
    for idx, line in enumerate(lines, 1):
        if RE_RIGID_BLOOM_LEVELS.search(line):
            hard_lint.append({
                "rule": "RIGID_BLOOM_PROGRESSION",
                "severity": "BLOCKER",
                "line": idx,
                "evidence": line.strip()[:60],
                "message": "V kódu je implementován rigidní postup Bloomovy taxonomie jako povinných odemykacích zámků."
            })

    # 6. Hard Check: Naivní striktní rovnost odpovědi bez ošetření alternativních zápisů
    for idx, line in enumerate(lines, 1):
        match = RE_STRICT_STRING_MATCH.search(line)
        if match:
            # Ignorovat bezpečné případy s boolean nebo normalizovaným porovnáním
            if not any(safe in line for safe in ["normalized ===", "isCorrect === true", "status ==="]):
                hard_lint.append({
                    "rule": "NAIVE_STRING_EQUALITY",
                    "severity": "BLOCKER",
                    "line": idx,
                    "evidence": line.strip()[:60],
                    "message": "Striktní porovnání řetězce (===) ignoruje alternativní zápis jednotek či ekvivalentní didaktické vyjádření."
                })

    # Kontrola měkkých kandidátů (Soft candidates)
    for rule_id, pattern, category, guidance in SOFT_PATTERNS:
        regex = re.compile(pattern, re.IGNORECASE)
        match = regex.search(content)
        if match:
            soft_candidates.append({
                "rule": rule_id,
                "category": category,
                "line": 1,
                "evidence": match.group(0)[:80],
                "guidance": guidance
            })

    exit_code = 0
    if hard_lint:
        exit_code = 1
    elif soft_candidates:
        exit_code = 2

    return {
        "file": filename,
        "exit_code": exit_code,
        "status": "BEZ DIDAKTICKÝCH ÚPRAV" if exit_code == 0 else ("BLOKÁTORY NALEZENY" if exit_code == 1 else "KANDIDÁTI K POSOUZENÍ"),
        "hard_count": len(hard_lint),
        "soft_count": len(soft_candidates),
        "hard_lint": hard_lint,
        "soft_candidates": soft_candidates
    }


def main():
    parser = argparse.ArgumentParser(description="Deterministický didaktický linter vzdělávacího softwaru.")
    parser.add_argument("file", help="Cesta k souboru (HTML, JS, JSON, MD)")
    parser.add_argument("--json", action="store_true", help="Výstup ve formátu JSON")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Chyba: Soubor '{args.file}' neexistuje.", file=sys.stderr)
        sys.exit(3)

    try:
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Chyba při čtení souboru: {e}", file=sys.stderr)
        sys.exit(3)

    result = lint_text(content, filename=args.file)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Soubor: {result['file']}")
        print(f"Stav: {result['status']} (Kód: {result['exit_code']})")
        print(f"Tvrdé blokátory: {result['hard_count']} | Měkcí kandidáti: {result['soft_count']}")
        if result["hard_lint"]:
            print("\n--- Tvrdé blokátory ---")
            for h in result["hard_lint"]:
                print(f"  [Řádek {h['line']}] {h['rule']}: {h['message']}")
                print(f"    Důkaz: {h['evidence']}")
        if result["soft_candidates"]:
            print("\n--- Didaktické podněty k posouzení ---")
            for s in result["soft_candidates"]:
                print(f"  [Řádek {s['line']}] {s['rule']}: {s['guidance']}")
                print(f"    Výskyt: \"{s['evidence']}\"")

    sys.exit(result["exit_code"])


if __name__ == "__main__":
    main()
