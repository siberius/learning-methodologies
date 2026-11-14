#!/usr/bin/env python3
"""
Compile all project markdown files into a single structured, AI-optimized working text file.
"""
from pathlib import Path
import datetime

OUTPUT_FILE = "learning-methodologies-vsechny-md.txt"

# File organization structure
CATEGORIES = [
    {
        "id": "project_overview",
        "title": "PROJECT OVERVIEW & CHANGELOG (Root)",
        "files": [
            "README.md",
            "CHANGELOG.md"
        ]
    },
    {
        "id": "cs_core",
        "title": "ČESKÁ EDICE — SKILL & DOKUMENTACE (cs/)",
        "files": [
            "cs/README.md",
            "cs/SKILL.md",
            "cs/docs/POUZITI.md",
            "cs/docs/PRO-UCITELE.md",
            "cs/docs/OVERENI-MODELU.md"
        ]
    },
    {
        "id": "cs_references",
        "title": "ČESKÁ EDICE — DIDAKTICKÉ REFERENCE (cs/references/)",
        "files": [
            "cs/references/dialog-navrhu.md",
            "cs/references/didakticke-zduvodneni.md",
            "cs/references/ceske-skolstvi.md",
            "cs/references/metody.md",
            "cs/references/hodnoceni.md",
            "cs/references/adaptivni-procvicovani.md",
            "cs/references/vzdelavaci-hry.md",
            "cs/references/simulace.md",
            "cs/references/kognitivni-rozhrani.md",
            "cs/references/stav-tutora.md",
            "cs/references/ai-provoz.md",
            "cs/references/modely-a-prostredi.md",
            "cs/references/priklady-rozhodovani.md"
        ]
    },
    {
        "id": "cs_standalone",
        "title": "ČESKÁ EDICE — KOMPLETNÍ SAMOSTATNÁ DISTRIBUCE (cs/vzdelavaci-metodiky.md)",
        "files": [
            "cs/vzdelavaci-metodiky.md"
        ]
    },
    {
        "id": "en_core",
        "title": "ENGLISH EDITION — SKILL & DOCUMENTATION (docs/)",
        "files": [
            "SKILL.md",
            "docs/USAGE.md",
            "docs/TEACHERS.md",
            "docs/MODEL-EVALUATION.md"
        ]
    },
    {
        "id": "en_references",
        "title": "ENGLISH EDITION — DIDACTIC REFERENCES (references/)",
        "files": [
            "references/design-dialogue.md",
            "references/didactic-rationale.md",
            "references/methods.md",
            "references/assessment.md",
            "references/adaptive-practice.md",
            "references/learning-games.md",
            "references/simulations.md",
            "references/cognitive-ux.md",
            "references/tutor-state.md",
            "references/runtime-ai.md",
            "references/model-profiles.md",
            "references/decision-examples.md"
        ]
    },
    {
        "id": "en_standalone",
        "title": "ENGLISH EDITION — STANDALONE BUNDLE (learning-methodologies.md)",
        "files": [
            "learning-methodologies.md"
        ]
    },
    {
        "id": "es_core",
        "title": "SPANISH EDITION — SKILL & DOCUMENTATION (es/)",
        "files": [
            "es/README.md",
            "es/SKILL.md",
            "es/docs/USAGE.md",
            "es/docs/TEACHERS.md",
            "es/docs/MODEL-EVALUATION.md"
        ]
    },
    {
        "id": "es_references",
        "title": "SPANISH EDITION — REFERENCES (es/references/)",
        "files": [
            "es/references/design-dialogue.md",
            "es/references/didactic-rationale.md",
            "es/references/methods.md",
            "es/references/assessment.md",
            "es/references/adaptive-practice.md",
            "es/references/learning-games.md",
            "es/references/simulations.md",
            "es/references/cognitive-ux.md",
            "es/references/tutor-state.md",
            "es/references/runtime-ai.md",
            "es/references/model-profiles.md",
            "es/references/decision-examples.md"
        ]
    },
    {
        "id": "es_standalone",
        "title": "SPANISH EDITION — STANDALONE BUNDLE (es/metodologias-de-aprendizaje.md)",
        "files": [
            "es/metodologias-de-aprendizaje.md"
        ]
    },
    {
        "id": "ru_core",
        "title": "RUSSIAN EDITION — SKILL & DOCUMENTATION (ru/)",
        "files": [
            "ru/README.md",
            "ru/SKILL.md",
            "ru/docs/USAGE.md",
            "ru/docs/TEACHERS.md",
            "ru/docs/MODEL-EVALUATION.md"
        ]
    },
    {
        "id": "ru_references",
        "title": "RUSSIAN EDITION — REFERENCES (ru/references/)",
        "files": [
            "ru/references/design-dialogue.md",
            "ru/references/didactic-rationale.md",
            "ru/references/methods.md",
            "ru/references/assessment.md",
            "ru/references/adaptive-practice.md",
            "ru/references/learning-games.md",
            "ru/references/simulations.md",
            "ru/references/cognitive-ux.md",
            "ru/references/tutor-state.md",
            "ru/references/runtime-ai.md",
            "ru/references/model-profiles.md",
            "ru/references/decision-examples.md"
        ]
    },
    {
        "id": "ru_standalone",
        "title": "RUSSIAN EDITION — STANDALONE BUNDLE (ru/metodiki-obucheniya.md)",
        "files": [
            "ru/metodiki-obucheniya.md"
        ]
    },
    {
        "id": "testing_research_plans",
        "title": "TESTING & RESEARCH — NÁVRHY, PŘESTAVBA A VÝZKUM (testing/)",
        "files": [
            "testing/navrh-prestavby-skillu-2026-11-14.md",
            "testing/vyzkum-vzdelavaci-hry-2026-11-14.md",
            "testing/provereni-claude-skillu-2026-11-14.md",
            "testing/provereni-skills-sh-aktualizace.md",
            "testing/edition-parity.md"
        ]
    },
    {
        "id": "testing_verification_reports",
        "title": "TESTING & VERIFICATION — PROTOKOLY OVĚŘENÍ A VYDÁNÍ (testing/)",
        "files": [
            "testing/overeni-prestavby-1.4.0.md",
            "testing/overeni-vzdelavaci-hry-2026-11-14.md",
            "testing/verification.md",
            "testing/czech-verification.md",
            "testing/cross-model-verification.md",
            "testing/evaluation-cases.md",
            "testing/czech-evaluation-cases.md",
            "testing/finished.md",
            "testing/vydani-1.4.0.md",
            "testing/release-notes-1.4.0.md"
        ]
    },
    {
        "id": "testing_forward_runs",
        "title": "TESTING — FORWARD RUNS & BENCHMARK TRANSCRIPTS (testing/forward-runs/)",
        "files": [
            "testing/redesign-forward-dialogue.md",
            "testing/redesign-forward-assessment.md",
            "testing/redesign-forward-delegated.md",
            "testing/forward-runs/climate-review.md",
            "testing/forward-runs/HANDOFF.md",
            "testing/czech-forward-runs/dialogue.md",
            "testing/czech-forward-runs/assessment.md",
            "testing/czech-forward-runs/model-profiles.md",
            "testing/forward-runs-240/ru.md",
            "testing/forward-runs-240/es.md"
        ]
    }
]

def get_file_metadata(filepath):
    p = Path(filepath)
    if not p.is_file():
        raise FileNotFoundError(f"File missing: {filepath}")
    text = p.read_text(encoding="utf-8")
    lines = text.splitlines()
    title = ""
    for line in lines:
        if line.startswith("#"):
            title = line.lstrip("#").strip()
            break
    if not title:
        title = p.name
    return {
        "path": filepath,
        "size": p.stat().st_size,
        "lines_count": len(lines),
        "title": title,
        "content": text
    }

def main():
    root = Path(".")
    
    # Collect and verify all files
    all_files_in_categories = []
    for cat in CATEGORIES:
        for f in cat["files"]:
            all_files_in_categories.append(f)
            
    print(f"Configured files in categories: {len(all_files_in_categories)}")
    
    # Verify no duplicates
    assert len(all_files_in_categories) == len(set(all_files_in_categories)), "Duplicate file in categories list!"
    
    # Verify exact match with filesystem
    actual_files = set(
        str(p.relative_to(root)) for p in root.rglob("*.md")
        if "catalog-install-verification" not in str(p) and "redesign-baseline" not in str(p)
    )
    diff_missing = actual_files - set(all_files_in_categories)
    diff_extra = set(all_files_in_categories) - actual_files
    if diff_missing:
        print("Missing from categories:", diff_missing)
    if diff_extra:
        print("Extra in categories:", diff_extra)
    assert not diff_missing and not diff_extra, "Files mismatch!"

    print("All 99 markdown files accounted for and verified.")

    # Read all files
    file_data = {}
    for filepath in all_files_in_categories:
        file_data[filepath] = get_file_metadata(filepath)

    total_bytes = sum(d["size"] for d in file_data.values())
    total_lines = sum(d["lines_count"] for d in file_data.values())

    out = []
    
    # Header block
    out.append("=" * 80)
    out.append("KOMPLETNÍ PRACOVNÍ DOKUMENTACE PROJEKTU: LEARNING METHODOLOGIES")
    out.append("Všechny Markdown (.md) soubory repozitáře ve strukturovaném formátu pro AI")
    out.append("=" * 80)
    out.append("")
    out.append(f"Vygenerováno: {datetime.date.today().isoformat()}")
    out.append(f"Celkem zahrnuto souborů: {len(all_files_in_categories)}")
    out.append(f"Celkový objem zdrojových dat: {total_bytes:,} bajtů (~{total_bytes/1024:.1f} KB)")
    out.append(f"Celkový počet zdrojových řádků: {total_lines:,}")
    out.append("")
    out.append("### AUTOR PROJEKTU")
    out.append("Luděk Sušický — biolog, středoškolský a vysokoškolský učitel informatických předmětů")
    out.append("- E-mail: ludek.susicky@gmail.com")
    out.append("- GitHub: @siberius (https://github.com/siberius)")
    out.append("- LinkedIn: https://www.linkedin.com/in/ludek-susicky/")
    out.append("- X (Twitter): @ludeksusicky")
    out.append("")
    out.append("=" * 80)
    out.append("INSTRUKCE PRO AI AGENTA / MODEL (JAK TENTO SOUBOR POUŽÍVAT)")
    out.append("=" * 80)
    out.append("""Tento soubor obsahuje ucelený kontext repozitáře `learning-methodologies` — didaktického
a pedagogického skillu pro vývojáře a AI agenty, kteří navrhují vzdělávací software, hry,
tutory, adaptivní procvičování a simulace.

Architektura projektu:
1. Čtyřjazyčná distribuce:
   - Čeština (cs/): Skill `vzdelavaci-metodiky` (obsahuje i specifika RVP/ŠVP a českého školství).
   - Angličtina (kořen): Skill `learning-methodologies` (univerzální anglický originál).
   - Španělština (es/): Skill `metodologias-de-aprendizaje`.
   - Ruština (ru/): Skill `metodiki-obucheniya`.
2. Dvě formy skillu:
   - Modulární balíček: `SKILL.md` + složka `references/*.md` (načítané podmíněně podle potřeby).
   - Samostatná distribuce: Jeden soubor (např. `cs/vzdelavaci-metodiky.md`), který v sobě
     spojuje instrukce skillu i všechny jeho reference do jediného přenosného souboru.
3. Testovací, výzkumná a validační vrstva (`testing/`):
   - Návrhy přestavby na verzi 1.4.0 (výzkum herních mechanik, evaluace, modely).
   - Testovací scénáře, verifikační protokoly a srovnání mezi modely (Claude, GPT, Gemini).
   - Skutečné běhy (forward-runs) a přepisy chování modelů při aplikaci skillu.

Každý soubor je uvozen vizuálním oddělovačem a zabalen do XML elementu:
<document path="cesta/k/souboru.md" category="kategorie" title="nadpis">
... obsah ...
</document>

Vyloučené dočasné složky (pro zamezení 4násobné redundance):
- `testing/catalog-install-verification/.agents/` (pouze dočasná instalační mezipaměť z npx testu)
- `testing/redesign-baseline-2026-11-14/` (stará historická záloha před verzí 1.4.0)
Všechny aktuální a platné soubory jsou níže v plném znění.""")
    out.append("")
    out.append("=" * 80)
    out.append("STRUKTURÁLNÍ OBSAH A SEZNAM SOUBORŮ (TABLE OF CONTENTS)")
    out.append("=" * 80)
    out.append("")
    
    file_index = 1
    for cat in CATEGORIES:
        out.append(f"## {cat['title']} ({len(cat['files'])} souborů)")
        for filepath in cat["files"]:
            meta = file_data[filepath]
            out.append(f"  {file_index:02d}. [{filepath}] — {meta['title']} ({meta['lines_count']} řádků, {meta['size']:,} B)")
            file_index += 1
        out.append("")

    out.append("=" * 80)
    out.append("TĚLO DOKUMENTACE — VŠECHNY ZDROJOVÉ SOUBORY")
    out.append("=" * 80)
    out.append("")

    file_index = 1
    for cat in CATEGORIES:
        out.append("")
        out.append("#" * 80)
        out.append(f"### KATEGORIE: {cat['title']}")
        out.append("#" * 80)
        out.append("")
        
        for filepath in cat["files"]:
            meta = file_data[filepath]
            out.append("=" * 80)
            out.append(f"POLOŽKA {file_index:02d} / {len(all_files_in_categories)}")
            out.append(f"SOUBOR: {filepath}")
            out.append(f"KATEGORIE: {cat['title']}")
            out.append(f"NADPIS: {meta['title']}")
            out.append(f"ROZSAH: {meta['lines_count']} řádků | {meta['size']:,} bajtů")
            out.append("=" * 80)
            out.append(f'<document path="{filepath}" category="{cat["id"]}" title="{meta["title"]}">')
            out.append(meta["content"].rstrip())
            out.append("</document>")
            out.append("")
            file_index += 1

    final_content = "\n".join(out)
    Path(OUTPUT_FILE).write_text(final_content, encoding="utf-8")
    print(f"Generated successfully: {OUTPUT_FILE}")
    print(f"Total output size: {len(final_content):,} characters | {Path(OUTPUT_FILE).stat().st_size:,} bytes")

if __name__ == "__main__":
    main()
