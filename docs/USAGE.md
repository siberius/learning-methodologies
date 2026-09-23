# USAGE

How the `learning-methodologies` skill works, how to install it per agent, and
how the decision matrix guides which methods to offer.

## How it works

The skill is a single portable Markdown file with a frontmatter block:

```yaml
---
name: learning-methodologies
description: General educational methodologies for learning-focused projects ...
---
```

The agent **loads the file only when a task matches the description**
(progressive disclosure). When loaded, it:

1. Elicits the **audience** (learners, age, subject/domain) and the target
   **generation & tone** (Z / Alpha / casual / informal / formal) — never a
   generic "for everyone".
2. Offers **teaching modes and assessment forms** mapped to product type —
   it does not implement them without your consent.
3. Applies the pedagogic methods when you agree.

## Decision matrix (what gets offered per product type)

| Product type | Methods offered |
|---|---|
| Quiz / test | Bloom gradation, Socratic error explanations, ZPD hints |
| Interactive lesson / tutorial | Socratic tutoring, Feynman technique, ZPD scaffolding |
| Simulation / game | Inquiry-based learning, role-play, Bloom creation |
| Exam prep | Feynman technique, Bloom analysis & evaluation |
| Group learning | Peer teaching, role-play, inquiry projects |

## Installation

The skill file is deliberately plain Markdown so it runs in any agent.

### OpenCode / Big Pickle / general task runner

Store `learning-methodologies.md` somewhere stable, e.g.:

- this project folder — reference it directly: `Read learning-methodologies.md and follow it.`
- or any skills/ index you already use; give the agent the path.

### Claude Code / Claude

Native skill install — copy the file into your skills folder:

```sh
mkdir -p ~/.claude/skills/learning-methodologies
cp learning-methodologies.md ~/.claude/skills/learning-methodologies/SKILL.md
```

Or, in MD/prompt mode, just reference the file as instructions.

### Astra, Muse, Spark, Gemini, Copilot

Load the file as a system instruction / prompt reference. The content has no
build step, no packages, no tool-specific syntax, so it carries over unchanged.

## Workflow

1. **Trigger:** you create or substantially extend a learning project
   (school app, quiz, interactive lesson, simulation, trainer, exam-prep).
2. **Load:** the agent reads this skill and answers with 2–3 questions
   (audience, tone, which methods you want). Answer them.
3. **Build:** the agent implements the chosen methods in the app.
4. **Review:** check the generated questions/hints via the method that was
   chosen (see TEACHERS.md for what each mode should feel like from the
   student's side).