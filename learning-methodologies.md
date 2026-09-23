---
name: learning-methodologies
description: General educational methodologies for learning-focused projects — brief elicitation (audience, tone), communication tone and generation targeting, Socratic method (elenchus, Paul & Elder question taxonomy, AI-guided discovery of errors), Bloom's taxonomy (gradation memorization→creation), AI-assisted learning modes (Feynman technique, Zone of Proximal Development with fading scaffolds, inquiry-based learning, role-play/simulations), further pedagogic tools (gamification, spaced repetition, scaffolding, error-based learning…) and assessment forms (summative, formative, portfolio, adaptive…). Use when creating or substantially extending a learning/training project (quiz, interactive lesson, simulation, demo). Not tied to any national curriculum.
metadata:
  version: "1.0.0"
  license: "MIT"
  repo: "https://github.com/siberius/learning-methodologies"
  format: "single-file (portable)"
  author: "Luděk Sušický"
---

# Learning methodologies — Socratic method, Bloom's taxonomy, AI-assisted learning

When **creating or substantially extending a learning project**, at the task start:

1. **Ask for the audience/target:** who are the learners (age, background, domain or
   subject area)? Adapt content, difficulty and examples to that audience — not a
   generic "everyone".
2. **Ask for target generation and tone of voice:** which generation the project
   targets (Z, Alpha, mix…) and what language/vocabulary to use (see „Tone of
   communication and generation targeting" below). Wording, examples, humor and
   difficulty follow that choice.
3. **Offer pedagogic methodologies and assessment forms** (below) when they could
   enrich the project. Do not implement them without the user's awareness and
   consent — ask and offer.

## Tone of communication and generation targeting

Before creating content, find out which generation the project targets and pick
language, vocabulary, humor and format accordingly. Generation targeting changes
**style**, not content quality. If the user doesn't specify a tone, **ask**;
avoid a generic "for everyone", which feels unnatural.

Age ranges (2026):

- **Generation Z** — born roughly **1997–2012** (today about **14–29**).
  Digital natives: grew up on social media, short formats (TikTok, Reels) and
  memes. Expect authenticity, irony, fast and visual content; dislike corporate
  and preachy tone.
- **Generation Alpha** — born roughly **2010–2024** (today about **2–16**, school
  age roughly **6–16**). Growing up with tablets, video and AI. Less text, more
  images, interactivity and playfulness; short attention span (reward fast, clear
  micro-goals).

Offered communication tones (pick per targeting, combine if desired):

- **Generation (Z/Alpha)** — speaks their language: abbreviations, memes, quirky
  humor, direct address, authenticity. Fits a casual web app, quiz, mobile app.
  Choose only if the user confirms the vocabulary suits them.
- **Casual / friendly** — warm, lively, witty, close, but without extreme
  generation-specific outtakes; understandable to a broader audience.
- **Informal** — natural, personal, no office formality, still cultivated.
- **Formal** — professional, factual, standard; fits official briefs, portfolios,
  documentation, exam and career prep.

When choosing, consider: project format (game vs. textbook vs. test), learner
age, the user's vision, and whether content should entertain or prepare for an
exam. Keep **inclusivity** — generational slang must never obscure content
clarity or exclude learners outside the target generation.

## Socratic method

- **Elenchus** (refutation): partner states thesis P, Socratic elicits agreement
  on premises Q, R, shows Q and R logically exclude P — the thesis falls by its
  own contradiction. Related terms: aporia, maieutics (giving birth to knowledge),
  Socratic irony, questions after universal definition („What is X?"), Meno's paradox.
- **Socratic question taxonomy** (Paul & Elder): (1) questions of clarification,
  (2) of assumptions, (3) of reasons and evidence, (4) of viewpoints, (5) of
  implications and consequences, (6) of the question itself. Three asking modes:
  spontaneous, exploratory, targeted.

**How to project it into the product:**
- As **content topic** (factual material about the method itself).
- As **question-building method**: questions aimed at mistaken assumptions;
  `explanation` written as Socratic refutation (a wrong answer falls because it
  contradicts an agreed premise); distractors = typical wrong premises; returning
  wrong answers repeatedly (spaced repetition) mirrors repeated elenchus.

## Bloom's taxonomy

- Levels of cognitive goals: **remember → understand → apply → analyze →
  evaluate → create** (revised version, Anderson & Krathwohl, 2001).
- Use: include higher-order questions (apply, analyze, evaluate), not only rote
  recall; grade quiz difficulty across levels; build a balanced set of goals;
  optionally map a task's level.

## AI-assisted learning modes (active dialogue, verification, simulation)

For teachers/facilitators who want to put AI effectively into learning, combine
methods of **active dialogue**, **structured assessment** and **practical
simulations**. When assembling a learning product (vibecoding), offer these modes
by product type — find out what is being built and [offer the matching modes](#how-to-offer-by-project-type); do not implement them without the user's awareness and consent.

### Socratic tutoring with AI (active discovery)
Using guiding questions, AI leads the learner to **discover the error on their
own**, instead of telling the answer. This complements the Socratic method above
as a **dialog mode** learner↔AI: the learner answers, AI asks further guiding
questions until the learner finds the contradiction in their own reasoning. In
the product: a "tutor" mode that never states the answer directly but leads to
it maieutically (by questions).

### Feynman technique (explain to AI as a layperson)
The learner explains the topic to AI, which plays the **layperson**: asks naive
questions and flags gaps that betray shallow understanding. The worse the
explanation, the more AI pushes back with „why", „I don't get it", „so how does
it work?". This verifies **depth of understanding**, not the ability to repeat.
In the product: a "teach me" mode — AI plays the beginner, the learner becomes
the teacher.

### Zone of Proximal Development (Vygotsky) with fading scaffolds
AI works in the ZPD: task **slightly above the learner's level** plus
**scaffolding** — hints are given and **gradually removed**. The learner gets a
minimal hint first; if stuck, AI broadens it (from general lead to concrete
answer), and as confidence grows it fades hints again. In the product: adaptive
hints in quizzes/tasks (from light leads to detailed steps).

### Gradation per Bloom's taxonomy
Tasks progress from **remembering** through **understanding, applying, analyzing,
evaluating** to **creating** (revised Bloom's, see above). AI ensures gradation:
the learner advances by levels; higher levels (analyze, evaluate, create) come
only after the lower ones are mastered. In the product: quiz difficulty levels
map to the Bloom scale, not just randomly increased hardness.

### Inquiry-based learning
In a **safe digital environment**, learners solve complex simulations and
**test hypotheses**: ask a question, form a hypothesis, use AI to design
verification, and evaluate the result. AI does not "spoil" the answer but walks
the learner through the scientific process. In the product: a sandbox where the
learner changes inputs and AI simulates consequences (or reacts as if the
experiment ran).

### Role-play and simulations
AI takes the role of a **historical or professional character** (scientist,
diplomat, customer, captain…) and holds an authentic dialogue or scenario with
the learner. The learner **negotiates, argues, tries strategies** and learns
from consequences in a safe digital environment with no real risk. In the
product: a chat/substory with a predefined character where AI stays in role and
evaluates the argumentation.

### How to offer by project type

| Product type | Methods to offer |
|---|---|
| Quiz / test | Bloom gradation, Socratic error explanations (elenchus), ZPD hints |
| Interactive lesson / tutorial | Socratic tutoring with AI, Feynman technique, ZPD scaffolding |
| Simulation / game | Inquiry-based learning, role-play, Bloom creation |
| Exam prep | Feynman technique, Bloom analysis and evaluation |
| Group learning | Peer teaching, role-play, inquiry projects (multiple AI roles) |

**When to offer:** suitable for learning products where AI talks directly with
the learner (dialogue, simulation, hints, role-play). Use together with the
Socratic method and Bloom's taxonomy above; the user decides which method to
integrate.

## Further pedagogic methods for learning products

- **Flipped classroom** — self-study of theory before class, application in the
  lesson; quiz as pre-work.
- **Gamification** — points, levels, badges, leaderboards, story arcs
  (sci-fi motif), guided repetition.
- **Spaced repetition** — automatic return of missed questions to the queue;
  supports recall.
- **Scaffolding** — derive difficulty, hints, progressive reveal of explanation.
- **Modeling & demonstration** — show a worked example before practice.
- **Connectivism / project-based learning** — connect content to a real task/story.
- **Peer teaching / cooperative learning** — collaboration tasks, shared
  solutions, shared assessment (suits group modes).
- **Metacognitive reflection** — questions like „Why did I pick this answer?",
  self-assessment after submission.
- **Error-based learning** — explain *why* the wrong answer is wrong, not just
  print the correct one.

## Assessment forms usable in a project

- **Summative** — overall grade/points at the end (classic 1–5, percentages).
- **Formative** — ongoing feedback without grade pressure; shows progress.
- **Self-assessment / reflection** — learner rates own confidence and progress.
- **Portfolio / certificates** — export results, completion certificate.
- **Adaptive difficulty** — assess by mastery level, not just score.
- **Story/scenario involvement** — score by mission/chapter (sci-fi motif).
- **Time and speed bonuses** — add time-based scoring.
- **Leaderboards** — competition motivation; clarify whether personal or class-level.

**When to offer:** especially for school/learning quizzes, training material,
interactive lessons and demo learning projects. Offer both when starting a new
project and when extending an existing one with content. The user decides whether
and how much of the methodology to apply.