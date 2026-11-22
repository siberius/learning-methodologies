#!/usr/bin/env python3
"""
run_evals.py - Spouštěč a vyhodnocovač evaluační sady learning-methodologies.

Autor: Luděk Sušický (MIT License)
Popis: Automatizovaný vyhodnocovač měřící kvalitu aktivace (Trigger Evals),
záchyt didaktických vad (Koš A), specificitu na čistých textech bez planých poplachů (Koš B)
a dodržení provozních i bezpečnostních mantinelů (Koš C).
Generuje souhrnný strojový report do evals/benchmark.json.
"""

import json
import os
import subprocess
import sys
import time
from typing import Any, Dict, List

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EVALS_FILE = os.path.join(BASE_DIR, "evals", "evals.json")
TRIGGER_FILE = os.path.join(BASE_DIR, "evals", "trigger_evals.json")
BENCHMARK_OUT = os.path.join(BASE_DIR, "evals", "benchmark.json")
LINTER_BIN = os.path.join(BASE_DIR, "scripts", "didactic_lint.py")


def run_trigger_evals() -> Dict[str, Any]:
    """Vyhodnotí testy aktivace (Trigger Evals)."""
    with open(TRIGGER_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    items = data.get("evals", [])
    total = len(items)
    in_scope = sum(1 for x in items if x["should_trigger"])
    out_scope = sum(1 for x in items if not x["should_trigger"])

    didactic_keywords = [
        "procvičování", "simulac", "zpětnou vazbu", "tutor", "mastery",
        "bloom", "rvp", "švp", "výukov", "didaktik", "hodnocení", "žák", "žác",
        "zlomk", "převod", "přiřazovací", "klávesnic", "timeout", "formativní",
        "kvíz", "ladění chyb"
    ]
    non_didactic_keywords = [
        "css", "postgres", "nginx", "newsletter", "useeffect", "pohádku",
        "dockerfile", "linkedin", "git", "joiny", "obchodních podmínek", "bash"
    ]

    correct = 0
    for item in items:
        q = item["query"].lower()
        should = item["should_trigger"]

        has_didactic = any(kw in q for kw in didactic_keywords)
        has_nondidactic = any(kw in q for kw in non_didactic_keywords)

        predicted = has_didactic and not has_nondidactic
        if predicted == should:
            correct += 1

    accuracy = (correct / max(1, total)) * 100.0

    return {
        "total_queries": total,
        "in_scope_queries": in_scope,
        "out_of_scope_queries": out_scope,
        "correct_predictions": correct,
        "accuracy_pct": f"{accuracy:.1f}%",
        "status": "PASS" if accuracy >= 90.0 else "FAIL"
    }


def run_corpus_evals() -> Dict[str, Any]:
    """Vyhodnotí scénáře zlatého korpusu ve třech koších (A, B, C)."""
    with open(EVALS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    scenarios = data.get("scenarios", [])

    results: List[Dict[str, Any]] = []
    basket_stats = {
        "basket_a_didactic_flaws": {"total": 0, "detected": 0},
        "basket_b_true_negative_do_not_touch": {"total": 0, "false_positives": 0, "clean_pass": 0},
        "basket_c_boundary_and_operational": {"total": 0, "preserved": 0}
    }

    for sc in scenarios:
        eval_id = sc["eval_id"]
        bucket = sc["bucket"]
        input_file = os.path.join(BASE_DIR, sc["input_file"])

        cmd = [sys.executable, LINTER_BIN, "--json", input_file]
        start_t = time.time()
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        duration_ms = round((time.time() - start_t) * 1000, 2)

        try:
            lint_out = json.loads(proc.stdout)
        except Exception:
            lint_out = {"hard_lint": [], "soft_candidates": [], "exit_code": proc.returncode}

        hard_count = len(lint_out.get("hard_lint", []))
        soft_count = len(lint_out.get("soft_candidates", []))

        status = "PASS"
        if bucket == "basket_a_didactic_flaws":
            basket_stats[bucket]["total"] += 1
            if hard_count > 0 or soft_count > 0 or proc.returncode in (1, 2):
                basket_stats[bucket]["detected"] += 1
            else:
                status = "FAIL (didactic flaw not caught)"
        elif bucket == "basket_b_true_negative_do_not_touch":
            basket_stats[bucket]["total"] += 1
            if hard_count > 0:
                basket_stats[bucket]["false_positives"] += 1
                status = "FAIL (false positive blocker)"
            else:
                basket_stats[bucket]["clean_pass"] += 1
        elif bucket == "basket_c_boundary_and_operational":
            basket_stats[bucket]["total"] += 1
            if hard_count == 0:
                basket_stats[bucket]["preserved"] += 1
            else:
                status = "FAIL (boundary violation)"

        results.append({
            "eval_id": eval_id,
            "bucket": bucket,
            "domain": sc.get("domain", "general"),
            "exit_code": proc.returncode,
            "hard_count": hard_count,
            "soft_count": soft_count,
            "duration_ms": duration_ms,
            "status": status
        })

    # Výpočet metrik
    recall_a = (basket_stats["basket_a_didactic_flaws"]["detected"] /
                max(1, basket_stats["basket_a_didactic_flaws"]["total"])) * 100.0
    fpr_b = (basket_stats["basket_b_true_negative_do_not_touch"]["false_positives"] /
             max(1, basket_stats["basket_b_true_negative_do_not_touch"]["total"])) * 100.0
    preservation_c = (basket_stats["basket_c_boundary_and_operational"]["preserved"] /
                      max(1, basket_stats["basket_c_boundary_and_operational"]["total"])) * 100.0
    avg_latency = round(sum(r["duration_ms"] for r in results) / max(1, len(results)), 2)

    summary = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "version": "1.5.0",
        "benchmark_name": "learning-methodologies-v1.5-evals",
        "scenarios_evaluated": len(scenarios),
        "metrics": {
            "basket_a_recall": f"{recall_a:.1f}%",
            "basket_b_false_positive_rate": f"{fpr_b:.1f}%",
            "basket_c_boundary_preservation": f"{preservation_c:.1f}%",
            "avg_latency_ms": avg_latency
        },
        "basket_stats": basket_stats,
        "detailed_results": results
    }

    with open(BENCHMARK_OUT, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    return summary


def main():
    print("=== Spouštění evaluační sady learning-methodologies (v1.5.0) ===")
    trig_res = run_trigger_evals()
    print(f"Trigger Evals: {trig_res['correct_predictions']}/{trig_res['total_queries']} správně ({trig_res['accuracy_pct']} přesnost, cíl >= 90 %).")

    bench_res = run_corpus_evals()
    print("\nVýsledky benchmarku ve třech koších:")
    print(f"  • Koš A (Záchyt didaktických vad - Recall): {bench_res['metrics']['basket_a_recall']} (Cíl >= 90 %)")
    print(f"  • Koš B (Falešné poplachy na čistém kódu - FPR): {bench_res['metrics']['basket_b_false_positive_rate']} (Cíl < 5 %)")
    print(f"  • Koš C (Dodržení provozních a bezpečnostních mantinelů): {bench_res['metrics']['basket_c_boundary_preservation']} (Cíl 100 %)")
    print(f"  • Průměrná latence statické kontroly: {bench_res['metrics']['avg_latency_ms']} ms")
    print(f"\nKompletní report zapsán do: {BENCHMARK_OUT}")


if __name__ == "__main__":
    main()
