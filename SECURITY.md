# Security policy

This repository publishes an instruction-only skill for AI agents that design educational applications. The security surface is the text an agent reads.

## What the repository contains

- Markdown: `SKILL.md`, `references/`, `docs/`, one generated standalone edition per language and one README per edition.
- One Python utility, `compile_ai_docs.py`, which concatenates the Markdown sources into a single working text file for authoring. The output is ignored by Git. The script makes no network requests and is not called by the skill, by an installation step or by a client.
- No `package.json`, so the skill has no install hooks of its own.
- No GitHub Actions workflow, no build step required to use the skill, no server component, no database.

## Runtime behaviour

The skill files contain no code that opens a network connection or starts a process. Links in `references/` and `docs/` identify published sources for a human reader; the skill does not instruct an agent to download them. `SKILL.md` declares no pre-approved tools.

The instructions still shape what an agent does with the tools you have already granted. Review `SKILL.md` before use, as with any skill.

## Installation and verification

- Install a published tag rather than the default branch. The exact command is in the [README](README.md); `@v1.6.0` is the current one.
- The Skills CLI records the resolved commit and a hash of the installed files in `skills-lock.json`. `npx skills list` and `npx skills check` compare the installed copy with that record.
- The manual route needs no installer: copy `SKILL.md`, `references/` and `LICENSE` into the skill directory of your client. See [usage and installation](docs/USAGE.md).
- The generated standalone Markdown is a single file for agents that accept Markdown instructions directly.

Only this repository and its tags are maintained sources. A copy taken from a fork or a mirror is outside this policy.

## Known third-party findings

Snyk reports `W012: Unverifiable external dependency detected` at risk level MEDIUM for the English edition, audited on 14 November 2026. The report points at the installation commands in the README, which refer to this repository, a repository owned by an individual author, and states that it found no concrete warning signs. The finding involves no payload, no download at runtime and no access to credentials.

Current report: <https://skills.sh/siberius/learning-methodologies/learning-methodologies/security/snyk>

## Reporting

Send reports to [ludek.susicky@gmail.com](mailto:ludek.susicky@gmail.com). Include the affected file and the version or tag. Do not open a public issue for an unpatched problem.
