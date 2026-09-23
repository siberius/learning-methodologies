# TEACHERS — guide for educators who vibe-code

You want to build apps for your students that **actually teach** — not just
quiz them. This skill encodes the methods below. For each one: what it is,
what it looks like in an app, and a ready-to-copy prompt.

## 1. Socratic tutoring (active discovery)

**What it is.** The AI leads the student with guiding questions until they find
the error in their own reasoning — it never just states the answer (maieutics).

**In the app.** A "tutor" mode where the student answers and AI pushes back
with the next question.

**Prompt.** `Make a "tutor" mode for the math topic. Use Socratic tutoring:
when a student answers wrong, ask a guiding question instead of giving the
answer; only after 3 failed attempts give a hint.`

## 2. Feynman technique (explain to a layperson)

**What it is.** The student explains the topic to AI playing a layperson. AI
protests wherever the explanation is shallow — verifying *depth* of
understanding, not recitation.

**In the app.** A "teach me" mode: the student is the teacher, AI the beginner.

**Prompt.** `Add a "teach me" mode. The student teaches the topic to the AI,
which plays a curious beginner and asks "why / I don't get it / how does that
work?" whenever the student glosses over something. Give feedback on which
parts were explained well vs. vaguely.`

## 3. Zone of Proximal Development (Vygotsky)

**What it is.** Tasks sit slightly above the student's level; hints are given
and **faded** as confidence grows.

**In the app.** Adaptive hints: minimal lead first, broaden when stuck, fade
again with success.

**Prompt.** `Make hints adaptive in ZPD style: start with a tiny lead; if the
student is stuck, give a broader hint; once they succeed twice in a row, stop
showing hints.`

## 4. Bloom's taxonomy gradation

**What it is.** Tasks progress remember → understand → apply → analyze →
evaluate → create. Higher levels come only after lower ones are mastered.

**In the app.** Quiz difficulty levels map to the Bloom scale.

**Prompt.** `Grade the quiz by Bloom's taxonomy: level 1 recall, 2
understanding, 3 application, 4 analysis, 5 evaluation, 6 creation. Unlock
higher levels only after passing the previous one.`

## 5. Inquiry-based learning

**What it is.** Students test hypotheses in a safe simulation; AI does not spoil
the answer but guides the scientific process.

**In the app.** A sandbox where the student changes inputs and AI simulates
consequences.

**Prompt.** `Build an inquiry sandbox on [topic]. The student states a
hypothesis, AI lets them run the experiment by changing inputs, and guides the
scientific process — question → hypothesis → test → evaluate — without giving
the result away.`

## 6. Role-play and simulations

**What it is.** AI plays a historical/professional character; the student
negotiates, argues, tries strategies in a safe environment.

**In the app.** A chat with a predefined character that stays in role and
evaluates argumentation.

**Prompt.** `Create a role-play scenario: the AI plays [character/role]. The
student negotiates with it; score the quality of argumentation, not the
outcome.`

## Combining modes: a worked mini-brief

> Build a physics training app for 17-year-olds.
> Load the learning-methodologies skill.
> Audience: Czech high school, students feel confident on math but hate theory.
> Use an energetic, informal tone (Gen Z, but clear).
> Features: quiz (Bloom-graded), "teach me" mode (Feynman), adaptive hints (ZPD),
> and one role-play scenario where AI plays an engineer reviewing their design.

This one prompt gives the AI everything it needs to build an app that teaches
rather than tests.

## Assessment & feedback

The skill also encodes assessment forms — summative, formative, portfolio,
self-assessment/reflection, adaptive difficulty, time bonuses, leaderboards.
Offer the ones that fit your class; formative + self-assessment are usually
the most effective for learning, summative for grades.