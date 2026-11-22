#!/usr/bin/env python3
"""
Unit testy deterministického didaktického linteru (didactic_lint.py).

Autor: Luděk Sušický (MIT License)
Princip: Párové testování (povinný pozitivní vzor + čistý protipříklad).
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from didactic_lint import lint_text


class TestDidacticLint(unittest.TestCase):

    def test_clean_artifact_passes(self):
        """Čistý výukový artefakt musí projít s kódem 0 (BEZ DIDAKTICKÝCH ÚPRAV)."""
        content = """
        function checkAnswer(val) {
            const normalized = val.trim().toLowerCase();
            return normalized === "75" || normalized === "75 cm" || normalized === "0.75 m";
        }
        """
        res = lint_text(content, "clean.js")
        self.assertEqual(res["exit_code"], 0)
        self.assertEqual(res["hard_count"], 0)
        self.assertEqual(res["soft_count"], 0)

    def test_hardcoded_ai_secret_pair(self):
        """Pozitivní vzor odhalí API klíč, maskovaný klíč projde."""
        bad = 'const API_KEY = "sk-1234567890abcdef1234567890abcdef123456";'
        res_bad = lint_text(bad)
        self.assertEqual(res_bad["exit_code"], 1)
        self.assertTrue(any(x["rule"] == "HARDCODED_AI_SECRET" for x in res_bad["hard_lint"]))

        clean = 'const API_KEY = process.env.OPENAI_API_KEY || "YOUR_API_KEY";'
        res_clean = lint_text(clean)
        self.assertEqual(res_clean["hard_count"], 0)

    def test_drag_drop_keyboard_accessibility_pair(self):
        """Drag-and-drop bez klávesnice je blokátor; s obsluhou klávesnice projde."""
        bad = '<div draggable="true" ondragstart="handleDrag(event)">Položka</div>'
        res_bad = lint_text(bad)
        self.assertEqual(res_bad["exit_code"], 1)
        self.assertTrue(any(x["rule"] == "DRAG_DROP_NO_KEYBOARD" for x in res_bad["hard_lint"]))

        clean = """
        <div draggable="true" ondragstart="handleDrag(event)" tabindex="0" onkeydown="handleKey(event)">
            Položka
        </div>
        """
        res_clean = lint_text(clean)
        self.assertFalse(any(x["rule"] == "DRAG_DROP_NO_KEYBOARD" for x in res_clean["hard_lint"]))

    def test_unhandled_ai_fetch_timeout_pair(self):
        """Volání AI bez timeoutu je blokátor; s AbortController projde."""
        bad = 'const resp = await fetch("https://api.openai.com/v1/chat/completions", { method: "POST" });'
        res_bad = lint_text(bad)
        self.assertEqual(res_bad["exit_code"], 1)
        self.assertTrue(any(x["rule"] == "UNHANDLED_AI_FETCH" for x in res_bad["hard_lint"]))

        clean = """
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 5000);
        const resp = await fetch("https://api.openai.com/v1/chat/completions", {
            method: "POST",
            signal: controller.signal
        });
        """
        res_clean = lint_text(clean)
        self.assertFalse(any(x["rule"] == "UNHANDLED_AI_FETCH" for x in res_clean["hard_lint"]))

    def test_false_mastery_retry_pair(self):
        """Započtení zvládnutí po odhalení nápovědy/řešení je blokátor."""
        bad = "if (solutionRevealed && userRetrySuccess) { item.isMastered = true; }"
        res_bad = lint_text(bad)
        self.assertEqual(res_bad["exit_code"], 1)
        self.assertTrue(any(x["rule"] == "RETRY_EXPOSURE_FALSE_MASTERY" for x in res_bad["hard_lint"]))

        clean = """
        if (solutionRevealed) {
            item.assisted = true;
            nextItem = generateIsomorphicVariant(item);
        }
        """
        res_clean = lint_text(clean)
        self.assertFalse(any(x["rule"] == "RETRY_EXPOSURE_FALSE_MASTERY" for x in res_clean["hard_lint"]))

    def test_rigid_bloom_pair(self):
        """Rigidní sekvence Bloomovy taxonomie je blokátor."""
        bad = "const BLOOM_LEVELS = ['remember', 'understand', 'apply', 'analyze', 'evaluate', 'create'];"
        res_bad = lint_text(bad)
        self.assertEqual(res_bad["exit_code"], 1)
        self.assertTrue(any(x["rule"] == "RIGID_BLOOM_PROGRESSION" for x in res_bad["hard_lint"]))

        clean = "const cognitiveTags = ['debugging', 'creative_synthesis', 'recall'];"
        res_clean = lint_text(clean)
        self.assertFalse(any(x["rule"] == "RIGID_BLOOM_PROGRESSION" for x in res_clean["hard_lint"]))

    def test_unverified_efficacy_claim_soft_candidate(self):
        """Neověřená tvrzení o účinnosti vyvolají varování (kód 2)."""
        content = "Naše aplikace zaručuje vědecky prokázané učení a zdvojnásobuje paměť u každého žáka."
        res = lint_text(content)
        self.assertEqual(res["exit_code"], 2)
        self.assertTrue(any(x["rule"] == "unverified_efficacy_claim" for x in res["soft_candidates"]))


if __name__ == "__main__":
    unittest.main()
