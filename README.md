# learning-methodologies

A portable AI skill for designing and reviewing educational applications. It connects learning goals, learner activity, feedback and evidence, then helps turn those decisions into application behavior.

Author: Luděk Sušický. MIT licensed. The English edition is independent of any national curriculum and does not require runtime AI, accounts or a particular model.

Current version: **2.2.0**. Both language editions include a short working route, decision examples and explicit rules for model choice and escalation. Named model configurations are starting recommendations, not cross-provider test results.

## What it helps you do

- Choose methods from a concrete learning need and classroom context.
- Design useful help, error feedback and independent practice.
- Separate goals, task difficulty, prerequisites and evidence of achievement.
- Build trustworthy simulations and bounded AI tutoring when appropriate.
- Consider accessibility, teacher control, learner data and operating constraints.
- Distinguish a working app, a defensible teaching design and observed learning outcomes.
- Choose a task-appropriate model, effort and serving speed using dated OpenAI, Claude and Gemini guidance, with verification status kept explicit.

Methods include Socratic learning, the Feynman technique, the Zone of Proximal Development and scaffolding, worked examples, retrieval and spaced practice, metacognition, inquiry, role-play, peer and cooperative learning, projects and flipped teaching. They are options selected for the task; installing the skill does not make them mandatory features.

## Choose an edition

- [SKILL.md](SKILL.md) and `references/`: native bundle with conditional detail. Keep the files together.
- [learning-methodologies.md](learning-methodologies.md): generated standalone file for agents accepting Markdown instructions directly. It contains the core and all references.

Both editions come from the same maintained sources. Edit `SKILL.md` and the relevant reference, then regenerate the standalone edition. Do not edit the generated copy separately.

## Example request

> Use learning-methodologies to build an offline circuit activity for 16-year-olds. Learners should predict how resistance changes current and explain their reasoning. It will support a teacher-led discussion and must work by keyboard. Use no accounts or external AI calls.

The agent should reuse this context, choose proportionate support and identify how the activity can reveal understanding. It should ask only about missing information that changes the design.

## Documentation

- [Usage and installation](docs/USAGE.md)
- [Teacher guide and example briefs](docs/TEACHERS.md)
- [Version history](CHANGELOG.md)

## Czech edition

[Vzdělávací metodiky](cs/README.md) adapts the same methodological foundation for Czech-language work and, where relevant, Czech schools, RVP/ŠVP, classroom conditions and answer formats. It has its own native [SKILL.md](cs/SKILL.md) and generated [standalone Markdown](cs/vzdelavaci-metodiky.md). Use one suitable language edition; loading both is not normally necessary. Shared principles are maintained together, while Czech curriculum guidance stays conditional.

The workflow is a design aid. It does not certify accessibility, subject accuracy or educational effectiveness. Use checks appropriate to the subject, learners and consequences.

## License

MIT, copyright 2026 Luděk Sušický. See [LICENSE](LICENSE). Preserve the copyright and license notice when redistributing either edition. Linked publications retain their own rights.

## Model evaluation

Use the [eight-task evaluation protocol](docs/MODEL-EVALUATION.md) to compare configurations. The protocol is prepared, not an executed benchmark.
