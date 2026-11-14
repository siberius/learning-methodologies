---
name: learning-methodologies
description: Design or review educational applications by connecting learning goals, learner needs, activities, feedback and evidence of learning. Use for new learning tools or substantive changes to their teaching design. Do not apply to cosmetic changes or ordinary bug fixes without a learning-design issue.
metadata:
  version: "1.4.0"
  license: "MIT"
  repo: "https://github.com/siberius/learning-methodologies"
  author: "Luděk Sušický"
  format: "native bundle with generated standalone Markdown"
---


<!-- Generated from SKILL.md and references/. Edit those sources. -->


# Learning methodologies

Help design, implement or review educational applications whose learning activities, support and assessment serve the intended learners. Adapt the depth of work to the request, consequences and uncertainty. A small classroom activity does not need a full evaluation study or a new planning document.

## Didactic methods for applications built with AI

Use the methods to turn educational goals into learner actions, feedback rules and evidence in the generated application. For example, retrieval requires an attempt before revealing the answer, while scaffolding requires controllable help and a distinction between assisted and independent performance. AI can help implement these decisions; its output still needs subject and teaching review. This applies to offline applications and to runtime AI when the learning goal needs it.

Read [didactic rationale](#reference-didactic-rationale) when explaining why a method fits or tracing it into implementation. It connects methods to product decisions and the evidence needed to assess them.

## Guide the creator through decisions

At each substantive learning-design decision, revisit the goal, learner action, evidence, support and constraints. Use existing choices. For an unresolved consequential choice, offer a small relevant selection, usually two or three options, each with a plain-language description and a concrete application here. Recommend one and explain the main tradeoff; ask which approach the creator wants. Read [design dialogue](#reference-design-dialogue) when starting or revisiting such a choice. This governs the creator conversation, separately from the learner's tutor interaction.

Do not reopen settled or declined choices without a relevant change. Honor explicit delegation of routine decisions and continue with a short rationale. Silence does not approve a scope expansion. While waiting, work on independent parts. A cosmetic change does not trigger this process.

Load details by need: [methods](#reference-methods) for learning activities and support; [games](#reference-learning-games) for motivation and mechanics; [assessment](#reference-assessment) for evidence and scoring; [cognitive interface](#reference-cognitive-ux) for representations, multimedia and attention; [adaptive practice](#reference-adaptive-practice) for repeated sessions or difficulty selection. Use the existing conditional routes below for simulation, tutor state and runtime AI. Read the relevant method before offering it; do not load every reference.

Translate the chosen method into observable product behavior and a meaningful check. Distinguish offered, selected, implemented and verified decisions. Technical verification does not establish learning effectiveness.

## Working route

Use this route at the depth the task needs: establish the goal and constraints, choose a method for the learning obstacle, connect the learner's activity to evidence, implement within scope and check the result. For a review, inspect the existing design instead of implementing. Reuse known context; do not require a planning document for every step.

Read [decision examples](#reference-decision-examples) when help, alternative answers or uncertain curriculum alignment needs clarification. They illustrate decisions, not scripts to copy into every lesson.

## Establish the learning context

Use information already present in the request, project and supplied materials. For context gaps, ask only about information that materially changes the design. For minor uncertainties, state a reasonable assumption and proceed. Avoid a fixed questionnaire or repeated approval for ordinary choices already covered by the request.

Identify the context that changes the design: learners and prior knowledge, subject, intended outcomes, classroom or independent use, available time and devices, language, accessibility needs, and any supplied curriculum. Follow a curriculum when relevant to the setting; do not assume one national framework. Choose tone from the context and author preference. Do not infer attention, motivation, ability or preferred pedagogy from generation labels.

Include the surrounding teaching activity where useful: preparation, individual or group work, teacher intervention, discussion and follow-up. A teacher-led demonstration may need a good discussion prompt; accounts and individual scores are not required.

Separate age, educational role and experience with the topic; child, pupil, student and adult participant are neither interchangeable categories nor ability levels. When establishing or changing the audience, read the learner profile in [design dialogue](#reference-design-dialogue). Adapt terminology and support to the setting; use neutral terms in general guidance. The creator, learner and accompanying teacher or parent can be different people.

## Connect goals to observable activity

For each important goal, connect the learner's action, evidence, success criteria, assistance conditions and next instructional decision. Keep this concise for small tasks. For open inquiry, the evidence may concern question quality, use of evidence or revision of an explanation; one predetermined answer is not the only option.

Example: the learner predicts how changing resistance affects current, checks a model, explains any discrepancy, and solves a new case independently. Moving a slider or completing a screen alone does not establish understanding.

Use the observed learning obstacle to choose an intervention that fits it. Treat an explanation of an error as a provisional hypothesis, not a diagnosis. Select a small coherent set of methods; do not add features merely because they appear in the catalog. Read [methods](#reference-methods) when selecting or implementing a method, support sequence or progression rule.

For game mechanics, motivational features or educational-game reviews, read [learning games and purposeful gamification](#reference-learning-games). It covers playable learning loops, mechanic selection, evidence limits and implementation from small tools to longitudinal products. Adapt to primary, secondary, university and adult learners across countries using prior knowledge and local context.

The method reference explicitly covers Socratic learning, the Feynman technique, the Zone of Proximal Development and scaffolding, worked examples, retrieval and spaced practice, error-based learning, metacognition, inquiry, role-play, peer and cooperative learning, projects, flipped teaching and optional gamification. These are selectable approaches, not required features of every application.

Bloom's taxonomy describes cognitive goals and knowledge types. Keep difficulty and prerequisites separate; do not require six locked levels. For practical, interpersonal or other outcomes, choose evidence that fits the outcome and acknowledge what an on-screen task cannot establish.

## Choose a realistic realization

Distinguish AI used to build the application from AI used by learners in the finished product. Choose among reviewed static content, deterministic interactions or simulations, and runtime AI according to the goal and operating constraints. Hints, feedback and spaced practice can work without an AI service.

Before adding a substantial feature, consider its learning contribution, interaction burden, teacher workload, maintenance, data needs and running cost. Explain material tradeoffs. Do not add accounts, analytics, dashboards, a backend, paid services or external data flows merely to make the product appear complete. Confirm scope-changing decisions when not already authorized.

Read [simulations](#reference-simulations) when modeling a system, running an experiment or designing role-play. Clearly distinguish real observations, model calculations and fictional reconstruction. Never present invented AI output as a measurement or pretend an experiment ran.

Read [runtime AI](#reference-runtime-ai) only when the finished product calls an AI service. Define the teaching role, source boundaries, human oversight, data flows, cost limits and failure behavior. A prompt is not a substitute for application security.

Read [tutor modes and continuity](#reference-tutor-state) when implementing multi-step tutoring, practice/assessment transitions or resuming learning. Keep state and evidence in the application; these features do not require runtime AI.

## Make feedback and decisions trustworthy

Provide a useful next step after an error. In practice, allow help and a route to direct explanation or a worked solution when needed; avoid endless questioning. Reduce assistance based on independent performance, while keeping requested support available. An assessment may restrict assistance under explicit conditions.

Distinguish independent success, supported success, exposure to the answer and uncertainty. One correct guess, a confidence statement or two supported successes do not automatically establish mastery. Do not infer stable ability, motivation or a disorder from a short interaction.

Read [assessment](#reference-assessment) when designing scored tasks, rubrics, adaptivity or learning evaluation. Check subject correctness, plausible alternatives, numerical units and tolerances, and whether the task really requires the intended performance. Preserve valid alternative explanations and methods. Keep game rewards and speed separate from achievement unless they serve an explicit goal.

## Preserve access and teacher agency

Design for the WCAG 2.2 AA criteria that apply to the activity and the learners' actual needs. Check keyboard operation, visible focus, understandable labels and feedback, alternatives to color or sound alone, and justified or adjustable timing. Choose ways to perceive information and express understanding that fit the learner; do not assign learners fixed learning styles. Seek specialist accessibility help when the implementation warrants it.

Collect only data needed for the activity and identify who sees it, where it goes and how it is retained. Check provider, school and local requirements for the actual deployment; do not invent universal legal rules. A local anonymous activity need not acquire accounts or persistent tracking.

Give the teacher or responsible author a way to review content, correct judgments and intervene in inappropriate adaptation. An editable content file is enough; a management system is not required. Significant grading or placement decisions need accountable human review.

## Coordinate expertise without inflating the workflow

Use these perspectives as needed; one agent can cover them for a small task:

- Methodologist: intended outcomes, teaching context and instructional choices.
- Subject didactician: content accuracy, prerequisites, examples and misconceptions.
- Assessment designer: evidence, criteria, alternatives and limits of inference.
- Interaction designer: learner flow, help, accessibility and classroom use.
- Developer: data contracts, calculations, state, persistence and failure behavior.
- Reviewer: discrepancies between the goal, design and observed behavior.

Carry their decisions into implementation. Do not label a convenient technical choice pedagogically correct without evidence. Resolve material disagreements through source checking, a targeted check or an explicit unresolved question. Use independent review when complexity or consequences justify it; do not start a team for every task. Invoke other skills only for relevant work and when available.

## Verify and report at the right level

For implementation, check the affected learner path, the errors learners actually make, the help route and the failure states that matter. For analysis-only requests, report findings and proposals without changing the product. Adapt checks to the application: a simulation needs model checks; runtime AI needs service-failure and output-handling checks; a simple static activity needs neither by default.

Keep three conclusions separate: functional correctness, didactic suitability and observed learning outcomes. Technical checks alone do not establish educational effectiveness. A small pilot can reveal problems without proving causal benefit. Report actual checks and unresolved assumptions; do not invent learner observations or efficacy results.

At handoff, summarize the learning goal, selected approach, important operating assumptions, checks actually completed and remaining limits. Include a goal-to-evidence table only when it makes the result easier to use. Match the form to the user's request.

## Write learner-facing text without AI slop

The application's text carries the teaching. Apply the same standard to prompts, instructions, feedback and explanations:

- Cut empty adjectives ("modern", "engaging", "interactive") unless the next sentence shows what makes them true.
- State the claim directly; avoid "it is not just X, but Y" and "this is not X, it is Y".
- Skip announcements such as "in this activity you will learn"; say what the learner does.
- Feedback names what is correct, what is missing and the next concrete step.
- Keep numbers, units and conditions specific; no "significantly improves" without a measure.
- No emoji in buttons, headings or labels. Use text and a consistent icon set.
- Match the vocabulary to the learners and keep one term for one thing.

Read the text as a learner would. If a sentence could sit unchanged in another product, cut it or make it specific.

## Integration

When selecting a model, effort or speed, or adapting the loading mechanism, read [model and host profiles](#reference-model-profiles). This includes documentation-based guidance for OpenAI, Claude and Gemini. Keep one shared educational contract and report actual testing separately from intended compatibility. Do not load the profile for an ordinary educational task that does not need it.

Use it for educational games, quizzes, tutorials, simulations and reviews of their teaching design. The core requires no packages, API, specific AI model or student data. The references below are embedded for standalone use. In a native bundle they are separate conditional files. Installation, deployment and other external changes require authorization for those actions. This skill does not replace project instructions or authorize additional scope.

Design references: [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [CAST UDL Guidelines](https://udlguidelines.cast.org/). These guide design and review; citing them does not certify conformance or educational effectiveness.

## Reference: methods

Source section: Choosing learning methods


Use this reference after defining the learning goal and evidence of success. Choose the smallest useful intervention for the learner's current obstacle. An app format alone does not determine a teaching method. Do not add every method listed here.

### Methods: Method cards for a concrete choice

Use these stable IDs across translations and decision records. Each row supplies a short creator-facing description, the need, learner action and evidence. The detailed sections below supply support and limits. For the selected card, state the small implementation, any optional extension, a failure check and the relevant source; do not display the full catalogue by default. Sources support particular learning principles, not the effectiveness of the generated application.

For the selected card, state the target audience, necessary prior knowledge and adaptations to language, support or assessment; do not select a method by age alone.

| ID and short description | When to offer and small implementation | Evidence and support check |
| --- | --- | --- |
| `worked-example-fading`: see a procedure, complete it, then use it independently | New procedure; reviewed example and completion task | New independent case; allow experts to skip and restore help when needed |
| `guided-inquiry`: predict, change a variable, explain the result | Understand a system; one bounded experiment | Explain a new prediction; random manipulation cannot substitute for reasoning |
| `productive-failure`: try approaches before comparing them with an explanation | Adequate prior knowledge and time for consolidation | Compare approaches and use the consolidated idea; do not strand a novice |
| `retrieval-spacing`: recall before revealing, return later | Retain accessible knowledge; attempt, correction and later review | Independent recall after delay; immediate repair alone is not spacing |
| `contrast-interleaving`: distinguish similar cases and choose a strategy | Confused categories or procedures after initial support | Explain the distinguishing feature; a random topic mixture is insufficient |
| `socratic-dialogue`: examine reasoning through a focused question | A reasoned answer can expose a useful uncertainty | Revise or defend with evidence; direct explanation remains available |
| `self-explanation`: explain in one's own words and revise | Surface gaps after initial learning | Content accuracy and application, not fluency alone |
| `cooperative-project`: coordinate roles to create a meaningful product | Shared investigation or authentic task with enough time | Individual contribution and explanation; group success is not everyone's mastery |
| `role-play`: decide from a situated role and reflect | Perspectives, communication or procedural judgment | Explain choices and consequences; agreement with a character is not correctness |
| `metacognitive-review`: compare a plan or confidence with evidence | Guide self-regulation and next steps | A revised action based on performance; confidence is not ability |
| `criterion-rubric`: assess observable qualities against criteria | Open responses, projects or justified alternatives | Examples at boundaries and a revision route; do not reward agreement |
| `representation-transfer`: connect concrete and formal representations | Success remains tied to game objects | Apply in a new representation; preserve accessible equivalent paths |

For differentiated versions, name the common learning goal and the decision every version must retain. Vary language, representation, pace and support without silently supplying that decision. Keep an engaging context for supported learners. Extend with justification, counterexamples or transfer rather than only more items. Explicitly identify an intentional goal change. Grouping follows revisable evidence, not permanent ability labels.

Optional extensions such as persistent review or live AI need a concrete reason and their conditional references. Preserve source/version/jurisdiction for curriculum links; distinguish official standards, components and inferred prerequisites. A concept-map edge is not automatically a verified learning progression.


### Methods: Choose from an observed learning need

| Observed obstacle | Candidate intervention | Check before adopting |
|---|---|---|
| Essential knowledge is not retained | Retrieval practice with spaced review | Can learners recall it independently after a delay? |
| A novice cannot begin a procedure | Worked example, then partially completed and independent tasks | Are prerequisites available and steps comprehensible? |
| Learners repeat a specific misconception | Contrast cases, explanation, targeted question and corrective practice | Does the task distinguish that misconception from other errors? |
| Learners can execute but cannot explain or transfer | Self-explanation, contrasting cases, application in a new context | Does success require reasoning rather than copying a pattern? |
| Learners struggle to judge their understanding | Prediction, confidence judgment, independent check and reflection | Can they compare their judgment with evidence? |
| The goal involves inquiry or professional interaction | Guided investigation, role-play or simulation with debrief | Are the model, scenario, evidence and criteria trustworthy? |

These observations are provisional instructional hypotheses. A wrong answer, slow response or request for help does not diagnose a learning disorder, motivation, intelligence or a stable learner trait. Ask or inspect further when several explanations fit.

### Methods: Bloom as a design lens

The revised taxonomy has two dimensions: knowledge (factual, conceptual, procedural, metacognitive) and cognitive process (remember, understand, apply, analyze, evaluate, create). Use them to describe goals and inspect task coverage. A task may combine processes; its verb alone does not establish its classification.

Keep task difficulty, curricular prerequisites and progression rules separate. Do not unlock six compulsory levels or infer mastery from a Bloom label. Build prerequisite relationships from the domain. Include practical, interpersonal or affective goals when relevant, with their own observable evidence. Bloom's cognitive categories do not cover every educational goal.

### Methods: Zone of Proximal Development and scaffolding

The Zone of Proximal Development concerns the relationship between independent performance and what becomes possible with appropriate support. Use this lens when a learner can complete a task with help but not yet independently. Scaffolding provides temporary cues, examples or partial steps. Do not infer an exact ability boundary from a single error.

For novices, consider a worked example with the reasoning visible, a completion task and independent practice. Adjust detail to prior knowledge. Provide only information needed for the current step; decorative complexity and simultaneous demands need a learning purpose.

Use a flexible help sequence: clarify the obstacle, give a targeted cue, offer a partial step, then provide a commented solution when needed or requested. Follow supported work with a comparable independent task. Reduce support based on demonstrated independent performance. Two successes or self-reported confidence alone do not establish mastery.

### Methods: Socratic learning

Use targeted questions to inspect assumptions, evidence and reasoning when the learner has enough background to respond. Elenchus examines consistency between a claim and accepted premises; the classroom purpose is not to defeat the learner. Paul and Elder's questioning categories offer prompts about meaning, assumptions, evidence, perspectives, implications and the question itself.

Ask one useful question at a time and respond to the learner's actual explanation. Let a learner defend a correct answer rather than assuming every initial answer is mistaken. Avoid endless questioning or withholding needed explanation. When prerequisites are missing, questioning stops helping or the learner asks to be shown, provide direct instruction or an example.

### Methods: Feynman technique

Invite the learner to explain a topic in their own words to a curious beginner, identify a specific gap, return to a reliable source and revise the explanation. This can reveal reasoning after an initial introduction or before application. Do not pretend not to understand a precise explanation merely to prolong dialogue.

Check factual accuracy against sources and a suitable rubric, then include an application task. Fluent language, simplification and AI praise alone do not establish deep understanding. The technique's name does not guarantee that an implementation is effective.

### Methods: Retrieval, spacing and reflection

Retrieval practice asks learners to reconstruct knowledge before seeing the answer. Provide corrective feedback and another opportunity to use it. Spacing revisits learning after a meaningful delay; immediately returning an error to the queue is corrective practice, not a complete spacing strategy. Review some previously correct material as well as errors. Configure intervals for the content, retention goal and available sessions; do not claim one schedule is universally optimal.

### Methods: Metacognition and self-regulated learning

Help learners set a useful subgoal, plan, monitor understanding and revise their approach using evidence. Ask them to predict success or explain their choice, then compare with independent performance. Keep reflection specific: what evidence changed their view and what they will try next. Do not equate confidence with competence or add a lengthy mandatory journal to a small activity without a purpose.

When working with generated hints, worked examples, or live AI, protect the learner's active role within the Shared Cognitive Space (FALR framework: Choice, Delay / Cognitive Pause, Evaluation, Self-Direction). Prevent passive acceptance: insert a short pause before the learner adopts or copies the model's answer, so the step does not become automatic. Prompt the learner to evaluate whether the output is valid, what is missing, what they actually understood themselves compared with what the system did for them, and whether to use, revise, verify, or reject the output.

### Methods: Concept maps and relationships

Use a concept map when explaining or constructing relationships is part of the goal. Let learners build a small map, label a missing relationship or critique a proposed connection, then compare it with reviewed sources or a rubric. A polished map generated entirely for the learner is a resource, not evidence of the learner's understanding.

Label links explicitly: prerequisite, part of, contrasts with, associated with or causes under stated conditions. Do not infer causation from co-occurrence or force a network of cross-links into a tree. Accept different valid structures; assess the meaning and justification of relationships rather than screen coordinates or visual similarity. Do not assume the source covers every connection.

For implementation, use stable concept identifiers and typed, directed relationships where needed. Provide a text/list alternative and keyboard editing if manipulation is required; dragging must not be the only way to answer. A short relationship table may serve the goal without a graph editor. Check one valid alternative map and one incorrect link against the feedback rules.

### Methods: Contextual methods

- Inquiry: scaffold question, prediction, test, observation and explanation. Claims about real-world behavior need appropriate real data or an adequately validated model; illustrative outputs must be labeled, with a note on what they do not show. Language-model narration cannot stand in for experimental evidence.
- Role-play: define the role, scenario boundaries and success criteria, then debrief. Mark historical dialogue as a reconstruction and distinguish sourced facts from invented speech. Fictional interaction can still have emotional or social consequences.
- Peer learning: provide a shared task, accountable individual contribution and criteria for useful explanation. Include a way to resolve disagreements and check each learner's understanding.
- Peer teaching: let learners explain and give feedback against understandable criteria, with access to a reviewed explanation or teacher when needed. Do not make an inexperienced peer the final authority on subject accuracy.
- Project learning: define an authentic product, intermediate milestones and individual evidence. Attractive output alone does not establish the intended learning.
- Flipped teaching: connect preparation to classroom application and provide an alternative for learners who could not complete preparation. It is an organizational choice, not an automatic learning benefit.
- Gamification: use optional progress or narrative features when they support the goal. Public competition, rewards and speed scoring need a reason and an accessible alternative.

### Methods: Evidence and further reading

- [Krathwohl, 2002, A Revision of Bloom's Taxonomy](https://people.ucsc.edu/~ktellez/blooms_taxonomy.pdf): two dimensions and a relaxed hierarchy with overlapping categories.
- [IES, Organizing Instruction and Study to Improve Student Learning](https://ies.ed.gov/ncee/wwc/PracticeGuide/1): evidence-informed recommendations for spacing, retrieval, worked examples and explanatory questions. Evidence strength varies by recommendation.
- [UNESCO, Guidance for Generative AI in Education and Research](https://www.iicba.unesco.org/en/africa-education-knowledge-platform/guidance-generative-ai-education-and-research): human agency and validation of educational uses.
- Zinger, D. (CFM / FALR – Four-Action Learner Regulation Framework): learner regulation within a Shared Cognitive Space with AI (Choice, Delay / Cognitive Pause, Evaluation, Self-Direction).

## Reference: assessment

Source section: Evidence, assessment and feedback


### Assessment: Start with the decision

For each important learning goal, specify the learner's action, evidence collected, success criteria and the next instructional decision. Include conditions such as access to hints, reference material, collaboration and time limits. Set practical or social criteria where those are the intended outcomes, rather than substituting a recall quiz.

Example: given an unfamiliar circuit, the learner predicts the effect of a change and explains why. Evidence includes the prediction and causal explanation. A rubric checks the relevant principle, application and reasoning. A misconception triggers a contrasting example and another independent attempt.

### Assessment: Keep purposes explicit

In practice mode, learners may request explanations, retry and use graduated support. Record support use separately from independent success. Feedback should name what is correct, identify the relevant gap and give an actionable next step followed by an opportunity to revise or apply it.

In an assessment mode, define permitted assistance and scoring before the attempt. Keep tutoring assistance consistent with those conditions. Explain whether feedback is immediate or deferred and why. Do not silently transfer practice scores into consequential grades. Formative assessment uses evidence to adjust learning; summative assessment reports achievement against defined criteria. A score without a subsequent decision does not itself constitute formative assessment.

### Assessment: Design trustworthy tasks

Check the answer key, explanation and plausible alternatives. For multiple-choice tasks, prefer meaningful distractors linked to known errors and avoid accidental clues. For open responses, accept equivalent wording, valid alternative methods and stated assumptions. Do not make one model answer the only correct formulation.

Use a short rubric with observable criteria, performance descriptions and examples, including borderline and alternative correct responses. Keep dimensions separate when useful: factual accuracy, reasoning, procedure, communication or collaboration. Penalize language mechanics only when they belong to the goal. Speed and public rank need an explicit educational purpose; participation points, badges and completion certificates do not demonstrate mastery.

When implementing a task bank, make the relevant decisions explicit in its existing data format. Useful fields may include a stable task ID, goal ID, prompt, accepted answers or rubric, explanation, hints, source and review state. Add numeric units and tolerances where needed. Keep response records separate: answer, assistance used, attempt and evaluation state. This is an example, not a required schema; a small shared demonstration does not need tracking.

### Assessment: Limits of AI judgment

Treat an AI score or error classification as a provisional judgment. Validate against teacher-reviewed examples and domain checks where available. When evidence is ambiguous, request clarification or mark it for review; do not manufacture certainty or use an uncalibrated confidence number as proof. Give learners a way to challenge feedback and give teachers an override with the original response and scoring rationale visible. Consequential decisions require an accountable human review process that fits the setting.

### Assessment: Evaluate the learning claim

Where feasible, compare an initial task with a comparable independent task after instruction, then sample retention after a delay and transfer to a different context. Interpret improvement cautiously: repeated items, hints and unequal starting conditions can change scores. A small classroom pilot can identify problems but does not by itself establish causal efficacy.

Track completion, usage, time, enjoyment, latency and errors as operational or experience indicators. Keep them separate from learning outcomes. Choose the least data needed for the instructional decision, and state what the evidence cannot establish.

### Assessment: Sources

- [EEF, Teacher Feedback to Improve Pupil Learning](https://educationendowmentfoundation.org.uk/education-evidence/guidance-reports/feedback): learning intentions, evidence of gaps, purposeful timing and opportunities to act on feedback. This teacher-feedback guidance does not validate every AI feedback implementation.
- [IES practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/1): independent retrieval and delayed review inform the proposed evaluation approach.

The workflow, example rubric and implementation choices above are design recommendations. Their suitability must be checked against the learners, subject, stakes and available evidence.

### Assessment: Check decisions and repair consequences

For a single-answer item, solve the actual prompt independently and try to defend every option under its stated units, precision and assumptions. Exactly one must remain defensible. For multiple-answer items use the declared answer rule; for open tasks retain valid alternatives. Then apply each claimed erroneous procedure to the actual item data: it must produce the intended distractor. Recheck affected options after changing the prompt. Equivalent fractions or unstated rounding must not create a second correct answer.

Map observed response to possible explanation, a distinguishing follow-up and a concrete next action. One wrong answer does not diagnose its cause. In evidence-centered design, identify the target competence, observable evidence and task that elicits it. Game events may have alternative explanations such as motor difficulty, exploration or guessing; telemetry alone does not establish persistence or personality. Explain necessary data collection.

If the content, answer key or tutor explanation is wrong, acknowledge and correct it, then inspect dependent hints, tasks, scores and progress. Do not treat an affected attempt as evidence of learner ignorance. Preserve the needed original evidence and content version; mark uncertainty and offer a fresh check where necessary. Teacher and learner views must use the same version of prompts and choices.

These verification procedures are adapted as design principles from [Learning Commons' check-for-understanding resources](https://github.com/learning-commons-org/agent-skills/tree/main/skills/k12-check-for-understanding). They do not import its fixed formats, US curriculum defaults or source-attribution restrictions.

## Reference: simulations

Source section: Simulations and role-play


Read this reference when a product models a system, supports an experiment, or lets learners act within a scenario. Select only the relevant checks.

### Simulations: Identify what the output represents

Distinguish these kinds of evidence in learner-facing language:

- **Measurement:** observations from an actual instrument, dataset, or recorded experiment. Identify the source and relevant measurement limits.
- **Calculation or simulation:** results produced by a specified mathematical or rule-based model. State assumptions and the range within which the model is useful.
- **Fiction or reconstruction:** invented events, dialogue, characters, or consequences used for learning. Identify them as such.

Never describe generated numbers as measurements or invented dialogue as an authentic quotation. A simulation can illustrate a hypothesis; its output alone does not establish how the real world behaves.

### Simulations: Define and check the model

Record the learning objective, state variables, inputs, units, allowed ranges, assumptions, update rules, and observable outputs. Explain simplifications that affect interpretation. Choose controls that expose the intended relationship without requiring learners to discover undocumented settings.

For numerical work, calculate outputs with a verified numerical engine or explicit rules. Keep this engine separate from any LLM commentary. The LLM may explain actual results but must not invent missing calculations or pretend an experiment ran.

Use a few checks that fit the model: a known example, a boundary case, unit consistency and one expected trend. For stochastic models, specify the source of randomness and support a reproducible seed when useful. Document limitations rather than implying universal validity.

### Simulations: Design the learning loop

Ask the learner to make a prediction and explain it before running the model when that supports the objective. Let them change meaningful inputs, observe the actual output, compare it with their prediction, and revise their explanation. Provide a debrief that distinguishes model behavior from real-world claims and asks where the model might fail.

Do not award understanding solely for reaching a target configuration. Seek an explanation, comparison, or transfer to a new case.

### Simulations: Historical and social role-play

State whether a character is fictional, composite, or based on documented history. Keep sourced facts distinguishable from reconstructed speech. Give provenance for historical claims and acknowledge disputed interpretations when relevant. Do not claim authentic access to a person's thoughts or fabricate citations.

Define the role, scenario boundaries, learning objective, and debrief. Offer a clear exit from the role and access to an explanation. Match emotional intensity and subject matter to learners and classroom context; provide an alternative activity for sensitive scenarios. Assess the intended reasoning or communication against explicit criteria; agreement with the character is not evidence by itself.

## Reference: runtime-ai

Source section: Runtime AI in educational applications


Read this reference only when the finished application calls an AI service during use. Using AI to write code or generate teacher-reviewed content does not require runtime AI. Keep offline activities offline unless the learning goal needs a service.

### Runtime Ai: Define a bounded teaching role

Specify what the model may do, which reviewed content or sources it can use, and how it should handle missing evidence. Where factual grounding matters, identify approved materials and preserve source provenance. Do not generate plausible-looking citations. Allow uncertainty and correction; avoid diagnoses or confident claims about a learner's abilities from a short interaction.

Choose assistance by activity. Practice can use guiding questions, progressive hints, worked examples, and direct explanation when requested or when questioning stops helping. An assessment may restrict assistance according to the teacher's stated rules. Do not impose an endless Socratic loop or a universal ban on answers. Give the learner a way to ask for help, stop, or involve the teacher.

Design live AI interfaces to prevent passive copying, where the tool thinks instead of the learner. Before adopting a generated procedure or response, require a brief check from the learner: clarify intent before querying, pause over the output, evaluate completeness and validity, and choose the next step (continue, verify, reformulate, or decide not to use the output).

Use explicit rubrics for feedback and open responses. Compare model judgments with teacher-reviewed examples before relying on them. Significant grading, placement, or disciplinary decisions require accountable human review; a single model response must not be the sole decision-maker. Record uncertainty and let the teacher correct a judgment.

### Runtime Ai: Minimize learner data

List the inputs sent to the provider, what is retained, who can access it, and how deletion works. Collect only what the activity needs. Do not add accounts, real names, persistent profiles, or conversation logging automatically. Use anonymous or pseudonymous activity identifiers where sufficient, while recognizing that these do not guarantee anonymity.

Before deployment with minors, check the intended age group, school arrangements, provider terms and settings, and applicable local requirements with the responsible institution. Do not invent a universal consent age or legal rule. Explain data handling to learners and teachers in suitable language.

### Runtime Ai: Use architectural safeguards

Keep service credentials in a protected server-side component when a remote service needs secret keys. Never expose them in browser code. Enforce authorization, request limits, and tool permissions outside the prompt. Treat learner input, retrieved documents, and model output as untrusted data.

Separate instructions from supplied content, restrict tool access and destinations, validate structured outputs, and sanitize rendered content. Prevent generated text from directly becoming executable code or privileged actions. A prompt telling the model to ignore injection is not a security guarantee. Use a dedicated security review for the implemented architecture.

### Runtime Ai: Plan cost, failure, and continuity

Set a realistic usage budget, per-session limits, timeouts, and cancellation. Show an understandable state while waiting. Handle network loss, unavailable models, invalid output, and exhausted quota without losing learner work. Retry only when safe and bounded.

Offer an appropriate fallback such as reviewed hints, static exercises, saved progress, or teacher help. Label unavailable feedback rather than fabricating it. Before classroom use, exercise the main learning path, an incorrect answer, a help request, uncertain feedback, and a service failure. Document unresolved limitations and the teacher's review responsibilities.

### Runtime Ai: Verify generated content within defined limits

Before releasing generated exercises, use applicable checks for domain correctness, solvability, state transitions and rendering. Require uniqueness only for tasks that promise it. Validate permission and structured-output boundaries outside the model; a schema does not prove truth and deterministic checks guarantee only the properties they actually check. Reject or quarantine invalid content and retain a reviewed fallback. For correction of dependent hints, assessment and progress, apply the correction procedure in `assessment.md`.

## Reference: model-profiles

Source section: Models, effort, speed and host adaptation


Use this reference when recommending a model, choosing a speed/effort setting, or adapting how the host loads this skill. Keep the educational instructions identical across providers.

### Model Profiles: What this reference does not claim

The recommendations are starting configurations for this workflow, not a benchmark or a measured ranking. They do not prove that one model family teaches better and do not predict latency. Model names, available settings, plans and prices change. Before using a named model, check the user's actual model list and the current official documentation. A UI label is not necessarily an API model ID. Confirm a configuration with representative tasks before calling it validated.

Documentation checked: 2026-11-04.

### Model Profiles: Choose by task before choosing a name

Use a smaller model for bounded edits with explicit criteria, a midrange model for ordinary design and implementation, and a stronger model for conflicting evidence, complex simulations or consequential review. These are task categories, not guaranteed capabilities. Keep the user's existing choice when it meets the criteria.

The named table below is an **untested starting recommendation for this skill**, derived from documentation.

### Model Profiles: Escalation and stopping rules

For a clear task, begin with the supported default effort or a previously successful setting. For conflicting sources or a complex model, consider higher effort from the outset. If the output misses an explicit constraint, contradicts its own scoring, fails a meaningful calculation check or repeatedly produces invalid tasks, first check that the relevant input and reference were accessible. Correct a missing input or ambiguous criterion before changing models.

After one focused repair still fails the same important criterion, recommend a supported higher effort level and reassess that criterion. If the failure persists, recommend a stronger available model or an independent review according to impact. Do not retry indefinitely or spend beyond the agreed budget. Missing sources, unavailable tools and service outages require resolving the dependency or stating the limit; more reasoning cannot supply the missing evidence. Report unresolved failures. Change settings only through authorized host controls.

Reduce effort or use a smaller model only after relevant checks pass; retain evidence of the tradeoff. Treat serving speed separately: standard is the starting point, paid acceleration needs a time/cost reason and authorization.

### Model Profiles: Keep recommendations current

Recheck named guidance when the model or host version changes, a setting is absent, the provider changes availability, or the documented behavior conflicts with observation. Until checked, mark that pairing unverified and use task categories plus the actual host's supported defaults. Do not invent an equivalent setting for an unknown model. Add provider-specific instructional workarounds only after a repeatable failure demonstrates their need; record the affected version and remove the workaround when no longer justified.

### Model Profiles: Match the task and control

| Work | OpenAI starting point | Claude starting point | Gemini starting point |
|---|---|---|---|
| Small, well-specified content edits or review of structured items | GPT-6 Luna, High; reduce effort only after checks hold | Haiku 5.5, Medium | Gemini 3.5 Flash-Lite, Low where supported |
| Design and implementation of a bounded learning activity | GPT-6.1 Sol, default effort or Medium | Sonnet 5.5, Medium for well-specified agentic work | Gemini 3.8 Flash, Medium |
| Difficult didactic audit, conflicting sources, complex simulation or architecture | GPT-6 Astra, Light/Low or Medium; increase if needed | Opus 5.5, Medium, then High if needed | Gemini 4 Argon, Medium, then High if needed |

These pairings are the skill author's recommendations inferred from vendor guidance. If a selected model is unavailable, recommend an available alternative and disclose the change; do not change a user selection without authorization. For example, an existing Gemini 3.1 Pro workflow can retain that model and its supported thinking levels. Measure a representative task in the actual environment for latency.

Distinguish three choices: the model, the amount of reasoning, and any premium serving-speed tier. Lower effort can reduce reasoning work; a vendor's Fast service tier is a different control and may cost more. A model named Flash is a model family, not a universal fast-mode switch. Equal words such as Low, Medium and High do not promise equal reasoning or latency across products.

Start with standard serving speed. Recommend a paid Fast tier only when waiting time matters and current access/rates justify it. Do not enable it or buy capacity without authorization. Streaming improves the visibility of progress; it is not evidence of earlier completion or higher quality. Judge end-to-end time including review, tool calls and repairs.

### Model Profiles: OpenAI and Codex

Use the native bundle where the host supports skills and can read references. In Codex, explicit invocation can name `$learning-methodologies` or `$vzdelavaci-metodiky`. Do not assume the same filesystem discovery in a regular chat; provide the standalone Markdown as accessible input instead.

The current guide recommends Sol for substantial work, Luna for focused work and Astra for demanding workflows; Luna High and Astra Light/Low are documented starting settings. In Codex, Fast is a serving-speed choice distinct from reasoning effort. Availability and usage rates depend on the model, account and client. Check supported values before proposing configuration; a UI label is not necessarily an API model ID.

Give a concrete deliverable, scope, relevant files and observable acceptance criteria. Ask for concise decisions and evidence, not disclosure of private chain of thought. Use the host's tools and permissions; do not invent shell or browser access from the model name.

Sources: [models](https://learn.chatgpt.com/docs/models), [speed](https://learn.chatgpt.com/docs/agent-configuration/speed), [skills](https://developers.openai.com/plugins/concepts/skills).

### Model Profiles: Claude and Claude Code

Claude Code supports `SKILL.md` bundles and supporting files. Explicit invocation can use `/learning-methodologies` or `/vzdelavaci-metodiky` after discovery. In another Claude host, verify its skill mechanism or supply the standalone edition. Do not add Claude-only hooks, shell substitutions or model overrides to the common frontmatter.

For Sonnet 5.5 agentic work, the effort documentation recommends Medium for well-defined tasks and higher effort for harder ones. Opus 5.5 defaults to Medium; older models and clients can differ. The API effort control and thinking mode are separate concepts. Not all generations support the same combinations. Prefer supported host controls rather than copying an API parameter into a chat instruction. Claude's Fast mode is a separate, model-dependent feature with premium pricing.

Keep the task, materials and desired result explicitly delimited. State where the agent may decide and what requires evidence. Provide one useful example when it resolves ambiguity; avoid repeating the entire skill or prescribing a long thought transcript. This packaging choice helps portability and is not a claim about a Claude-specific cognitive trait.

Sources: [skills](https://code.claude.com/docs/en/skills), [models](https://platform.claude.com/docs/en/models/overview), [effort](https://platform.claude.com/docs/en/build-with-claude/effort), [Fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode).

### Model Profiles: Gemini and Gemini CLI

Gemini CLI discovers native skills in its supported skills locations, including the `.agents/skills` alias. Verify with `/skills list` and reload with `/skills reload` when needed. Workspace trust and activation approvals belong to the host; do not bypass them. AI Studio or another chat should receive the standalone file when native skill loading is unavailable.

The checked thinking guide lists Low, Medium and High for Gemini 4 Argon and Gemini 3.8 Flash. Other Gemini versions have different defaults and levels. Use only those supported by the actual model and API/client; do not translate an OpenAI or Claude effort parameter literally. A preview name and a stable name are not interchangeable.

For `gemini-3.1-pro-preview`, the checked API table lists Low, Medium and High, with High as the default. For that endpoint, try Medium for ordinary design and High for a difficult audit as an author recommendation, if the host exposes those controls. A displayed label such as Gemini 3.1 Pro does not prove which endpoint or controls a client uses.

Keep instructions concise and specify the goal, constraints and output evidence. Attach referenced materials so the model can actually access them; a path in a chat is not file access. Preserve required tool-conversation state when implementing a Gemini API application, following the current API documentation. This skill does not implement that API layer and does not authorize adding one.

Sources: [models](https://ai.google.dev/gemini-api/docs/models), [thinking](https://ai.google.dev/gemini-api/docs/thinking), [Gemini CLI skills](https://geminicli.com/docs/cli/tutorials/skills-getting-started/).

### Model Profiles: Portable use and verification

Keep required metadata plain: `name` and `description`, followed by ordinary Markdown. Optional metadata describes the edition; do not rely on a host-specific field to enforce a safety boundary. Use the bundled relative references in a file-capable agent or the complete standalone edition in a chat. Do not load both language editions by default. Reattach essential scope and unfinished work after host context loss rather than assuming every host retains it.

Emoji can carry meaning but should not be the sole instruction or priority signal. Preserve explicit text labels. Research on [emoji semantics](https://arxiv.org/abs/2409.10760) and [contextual ambiguity](https://arxiv.org/abs/2511.07193) does not establish that decorating this skill improves compliance. Test such a change on the actual models and tasks before claiming a benefit.

Before calling a model/host combination tested, verify discovery or successful standalone loading, relevant-reference access, a representative deliverable and the critical boundaries. Record exact model ID or visible label, host/version, language, effort, serving speed, tools, date, artifacts and failures. Distinguish documentation-based compatibility from an observed execution. Never transfer a pass from one model to every model in its family.

For comparison, use the same task and raw materials, and have a reviewer assess actual outputs against the same educational criteria. Include known-context reuse, bounded help, an alternative correct answer, unsupported curriculum claims, a model/data boundary and a tool/service failure where relevant. Reduce effort or choose a smaller model only while important checks keep passing. If direct access to a provider is unavailable, mark it untested instead of inventing results.

## Reference: decision-examples

Source section: Decision examples


Use the relevant example to resolve a concrete ambiguity. Adapt the subject and age; preserve the decision principle.

### Decision Examples: Accept an equivalent answer

Task: express 1.5 A in milliamperes. The learner enters `1500 mA`; a checker expects `1500`. Accept the equivalent quantity, checking the unit and numeric value. If the learning goal specifically tests unit notation, assess that separately. Do not treat every string as equivalent by removing characters: `1500 A` is wrong here. Why: formatting should not replace the intended evidence of unit conversion.

### Decision Examples: End an unproductive Socratic loop

During practice, a learner says “I still do not understand; please show me” after a question about current and resistance. Give a short explanation or worked example at constant voltage, then offer a new prediction with optional support. Do not keep asking questions as a condition for receiving help. Record the worked example as supported learning; a fresh independent problem can supply separate evidence. Why: questions should help the learner progress, not block instruction. A declared assessment can have different assistance rules.

### Decision Examples: Correct an inaccurate Feynman explanation

A learner explains: “Plants get their food from soil; sunlight warms it up.” Acknowledge the understandable wording without accepting the science. Identify the specific misconception, provide or consult a suitable verified source, distinguish water/minerals from sugars produced in photosynthesis, and invite a revised simple explanation. Check transfer with a new case, such as what changes without light. Why: fluency and simplicity do not establish correctness. Do not invent experimental observations or attribute all plant growth to one factor.

### Decision Examples: Work with an unavailable curriculum

A teacher requests “full alignment with our school curriculum” but supplies no school document. Use the stated learning goal to produce a provisional activity. Request the relevant excerpt only when exact alignment matters; identify what remains unverified. Never invent local outcome codes or certify coverage. For Czech schools, a general RVP reference does not establish alignment with the particular ŠVP. Why: useful drafting can proceed, and the limits of the documentary claims stay visible.

### Decision Examples: Insert a Cognitive Pause Before Adopting AI Output

In an app with an embedded AI assistant, a learner asks for a solution outline or error explanation. Instead of an "Apply to my solution" button, insert a cognitive pause: prevent direct copying and ask a brief verification question ("Which step is central here? What is missing from the AI suggestion for your specific case?"). Allow the learner to revise the suggestion, verify it on another example, or decide not to use it. Record the model's generated text as supported assistance, not as evidence of the learner's understanding. Reason: a pause stops the learner from copying the model's answer without thinking it through.

## Reference: tutor-state

Source section: Tutor modes and learning continuity


Read when designing a multi-step tutor, resumable activity or exam practice. These rules also apply to deterministic offline applications; they do not require runtime AI, accounts or persistent storage.

### Tutor State: Model explicit modes and transitions

Separate explanation, practice and assessment where the activity needs them. Explanation can show a worked example. Practice asks for a response, waits, gives criterion-based feedback and offers help. Assessment follows declared rules for assistance and feedback timing. Let the learner pause, request help or leave; a restricted assessment may end or mark the attempt supported when content help is requested. Preserve accessibility accommodations that do not reveal content.

For conversational practice, keep one actionable question pending unless the task calls for a batch. Do not generate the learner's answer or reveal the solution while waiting. Distinguish idle, awaiting-answer, evaluating, feedback and paused states as needed. Disable duplicate submissions or associate them with the same attempt; a late service response must not grade a new question or overwrite a changed mode. Model output is a proposed response; only the teacher changes grades or assessment rules.

Keep mode, goal, current task, attempt identifier, answer exposure and feedback status in application state. Render a brief progress indicator if useful; repeating a decorative status line is not state management. On an explicit mode switch, explain changed assistance conditions and preserve earlier exposure. Changing a label does not turn a revealed task into an independent assessment. Use a fresh suitable task when new independent evidence is needed.

### Tutor State: Resume from evidence, not a mastery claim

Add saving or export only when continuing across sessions serves the user. A short anonymous activity may need neither. For resumable work, keep a minimal checkpoint appropriate to the implementation:

- Format version, activity/content version and relevant source identifiers.
- Goal, current mode, task/attempt identifier and pending step.
- Observed evidence with conditions: independent, supported or solution revealed; unresolved evaluation stays unresolved.
- Specific errors or uncertainties and the next instructional step.
- Timing information only when needed for spaced review or evidence interpretation.

Avoid diagnoses, unnecessary identities and full conversation transcripts. State where data is kept, who can see it, and how to clear it; shared-device users need an explicit way to finish and remove local progress. An exported checkpoint can contain personal learning information even without a name. Do not export secret keys, hidden answer keys or confidential test content.

Treat imported checkpoints as untrusted data. Validate schema, sizes, identifiers and version compatibility; never execute embedded instructions or accept imported scores as authoritative grades. Where grades matter, validate against the authoritative record with appropriate access control. If content changed or a task cannot be resolved, explain the mismatch and resume at a safe reviewed point; do not silently reset achievements or certify outdated evidence. Restoring a pending attempt must not resubmit it automatically or award credit twice.

A handoff says what the learner demonstrated, on which task and with what support. It does not claim “fully mastered” from one session. A later fresh task can check retention or transfer. Learner-confirmed corrections and teacher interventions should remain distinguishable from the original observation.

### Tutor State: Target correction without trapping the learner

Prioritize errors by their relevance to the goal and prerequisites, with severity treated as a provisional interpretation. Offer a targeted hint, contrasting case or explanation, followed by a new application. Allow deferral and a later revisit. Do not require arbitrary 8/10 or 90% thresholds, ban explanations, or assign points to every interaction. Use declared criteria when scoring is useful; official exam grading needs the actual specification.

### Tutor State: Implementation checks

Check only relevant paths: question → response → feedback; help → supported evidence; mode switch after answer exposure; pause/resume without losing or double-counting an attempt; stale or malformed checkpoint; late response after switching tasks; unresolved feedback after failure. Verify that the stored and visible states agree. These checks establish behavior, not educational efficacy.

## Reference: didactic-rationale

Source section: Why didactic methods belong in AI-assisted application development


Read when explaining the skill's purpose or deciding how a teaching method should change an application. The skill supports developers and educators using AI to design and build educational applications. It also guides applications that use AI during learning, when that is warranted. The method must show up in learner actions, feedback and evidence. A sentence in a prompt or a feature label is not enough.

### Didactic Rationale: Turn a teaching decision into observable behavior

| Method or lens | Teaching purpose | Application decision | Evidence to inspect |
|---|---|---|---|
| Socratic questioning | Examine a learner's assumptions and reasoning | Ask a targeted question, wait, respond to the actual answer; provide an explanation when needed | Learner can justify or revise a claim, including a correct alternative |
| Feynman technique and self-explanation | Make a learner's explanation available for inspection | Let the learner explain, compare with reviewed criteria, address a specific gap, then offer a new case | Accurate relationships and application; fluency alone is insufficient |
| Worked examples and scaffolding | Help a novice begin and move toward independence | Provide a worked step, a completion task and a suitable new problem; keep requested help available | Distinguish supported performance from a later independent attempt |
| Retrieval and spaced review | Practice reconstructing knowledge and revisit it after a delay | Ask before revealing; provide corrective feedback and schedule appropriate revisits, including previously correct material | Performance before exposure, later retention and transfer when checked |
| Concept maps | Make relationships and prerequisites explicit | Use labeled relations, accept equivalent valid structures and provide an accessible editing alternative | Meaning and justification of links, not visual similarity |
| Inquiry and simulations | Compare predictions with evidence under explicit assumptions | Expose relevant variables, units, constraints and model boundaries; include debrief | Learner revises an explanation using observations or clearly labeled model results |
| Formative assessment and metacognition | Decide a useful next step from evidence | Show specific feedback and let learners compare a prediction with performance | An actionable correction and new evidence; scores and confidence are insufficient by themselves |
| Cooperative and peer learning | Support comparison and explanation with accountability | Assign a shared task with individual contributions and a way to resolve disagreement | Each learner's reasoning; one shared click does not establish group understanding |
| Regulation in Shared Cognitive Space (FALR) | Keep the learner active and critical when using AI or hints | Insert a cognitive pause before adopting output; ask what is missing and what the learner understood vs. what the system did; allow rejecting the output | Distinction between self-understanding and system output, followed by an independent learner step |

Bloom's taxonomy helps describe cognitive goals and knowledge types; it does not prescribe difficulty or a six-stage unlocking system. A method is appropriate only if it addresses the target learners, content and observed obstacle. No catalog is a requirement to implement all methods.

### Didactic Rationale: Why this matters when AI helps write the application

AI can produce an interface, answer checker and feedback quickly. Those artifacts still need a teaching contract: what learners should do, what counts as evidence, what assistance was available, and how the next decision follows. Use that contract to constrain generated code and reviewed content. For example, retrieval practice changes answer-reveal timing, while scaffolding changes help controls and evidence labels. Naming the method without implementing those behaviors does not meet the design goal.

Separate AI at authoring time from AI at runtime. Reviewed static content and deterministic checks can implement many of these behaviors offline. If runtime AI is useful for open responses or dialogue, bound its sources, criteria and tools, validate output and provide a failure path. More generated conversation, stricter scoring or a larger model does not by itself establish better learning.

### Didactic Rationale: State the limits of the rationale

This explains design choices; it does not prove that this skill or every implementation improves outcomes. Subject correctness, accessibility and classroom feasibility require checks in the actual setting. A technical pass does not demonstrate learning; suitable learner evidence and, for causal claims, an appropriate evaluation are needed. Research guidance linked in the methods reference informs particular choices and does not certify the whole package. Retain teacher review for consequential judgments and adapt curriculum to the actual setting.

## Reference: learning-games

Source section: Learning games and purposeful gamification


Use this reference when a project needs game mechanics, motivational features, or a substantial redesign of play and learning. The recommendations combine research with design judgments; they do not establish the effectiveness of a new product. Evidence checked: 2026-11-14.

### Learning Games: Choose the learning activity before the reward

Distinguish a learning game (learning happens through playing), gamification (game elements support another activity), and a simulation (a model can support inquiry without winning or scoring). A good tool may need none of the reward systems below.

Write one compact design contract: learner and prerequisites; target performance; player decision; consequence and feedback; independent evidence; next learning step. For a small activity, a paragraph suffices. Identify the plausible shortcut: can a player win through guessing, repeated clicking, memorizing positions, reading the answer, or relying on a teammate?

Prefer mechanics that require the intended thinking. To teach proportional reasoning, make the player adjust a mixture under meaningful constraints, explain a prediction, and solve a fresh case. A quiz can still serve retrieval practice; embedding every fact in a simulated world is unnecessary. For exploratory goals, allow alternative defensible solutions.

### Learning Games: Select a small coherent set

| Need | Candidate mechanic and implementation | Check or failure condition |
|---|---|---|
| Starting without knowing the controls | A safe playable first task; introduce a tool when needed | A newcomer completes the action without the author explaining it |
| Understanding a system | Predict, manipulate one variable, inspect consequences, explain | Random manipulation cannot substitute for a new prediction |
| Retaining knowledge | Retrieval missions revisited after a delay, with correction | Later unaided performance; replaying immediately is repair, not spacing |
| Choosing the right procedure | Mix confusable problem types after initial support | Learner selects and explains a strategy; random topic shuffling is insufficient |
| Progressing from novice performance | Worked example, partial completion, independent challenge | Help use stays visible; assistance can return when needed |
| Seeing progress | A private map of skills with evidence and next steps | Completion, supported success and independent evidence remain distinguishable |
| Having agency | Meaningful choice of route, context or method within the goal | Choices change the experience; prerequisites and alternative routes remain clear |
| Curiosity | A mystery whose clues are disciplinary evidence | Reveal resolves a learning question; story reading does not dominate practice |
| Working together | Complementary roles, shared outcome, rotating responsibilities | Each participant explains or applies something independently |
| Recognition | Optional badges tied to transparent accomplishments | A badge describes evidence; it never substitutes for mastery judgment |
| Competition | Optional comparable challenges or personal improvement | Check disadvantage, withdrawal and rushing; provide a route without public ranking |
| Returning over time | Learner-chosen goals, resumable sessions, reminders if requested | Absence does not erase learning records or block access to help |

These are design hypotheses, not a ranked list of proven features. Points, streaks, avatars and leaderboards have no universal learning effect. Keep game currency separate from educational evidence. Do not make ordinary learning errors consume access to instruction. Avoid pressure from expiring rewards, paid recovery, random reward purchases or public humiliation. These are product-design commitments, not claims that every instance has been experimentally compared.

Let difficulty come from the target decision. Reading load, motor precision and time pressure can contaminate its measurement. Use speed only when fluency or response time belongs to the goal; keep accuracy and speed interpretable separately. There is no universal optimal success percentage. Adjust support from multiple observations and let learners or teachers correct an inappropriate placement.

### Learning Games: Shape the learning sequence

Introduce one playable problem before an elaborate economy. Follow an action with a consequence the learner can interpret, useful feedback, another opportunity and a natural stopping point. Explain an error at the level of the task or strategy. A celebration alone cannot correct a misconception.

Use a worked example when missing knowledge prevents useful attempts. An initial exploratory problem can prepare learners for subsequent explanation, but productive failure requires consolidation. It does not justify leaving a beginner stuck. Separate initial learning, practice with support, and independent assessment. A reveal marks an assisted attempt; assess a different instance later.

Build retrieval, spacing and interleaving according to the learning task. Schedule returns to previously correct material as well as errors. Ask for reconstruction before revealing an answer when retrieval is intended. Mix cases that require discrimination, with feedback suited to the activity. Do not advertise a fixed interval schedule as optimal for every subject or retention period.

### Learning Games: Adapt across ages and countries

Use observed knowledge and support needs rather than generational stereotypes. Primary learners may need concrete representations and supported reading; secondary learners may benefit from contrasting explanations; university and adult learners may need disciplinary authenticity and flexible pacing. These are starting hypotheses. An adult novice can need substantial scaffolding, while an experienced child can need greater challenge.

Check local terminology, number and unit formats, reading direction, cultural references, school structure and available devices. Map curriculum only against an identified jurisdiction and version. Never infer a national curriculum from interface language. Include shared-device and teacher-led use where relevant. A simulation of a professional action does not certify practical competence.

Provide keyboard and single-pointer alternatives to dragging, readable status text beyond color or sound, visible focus, controllable motion and suitable timing. Preserve the assessed skill when offering alternative responses. Accessibility and age suitability require testing with intended users; invoking UDL or WCAG alone proves neither.

### Learning Games: Implement at the right scale

For a short activity, start with reviewed content, deterministic rules and session state. Add local persistence only if resuming matters. For a longitudinal product, consider skill and item versions, supported versus independent attempts, scheduled review, export/deletion and teacher correction. Accounts, servers and behavioral telemetry require a concrete need.

If evidence is stored, a useful minimal attempt record can contain `skill_id`, `item_version`, `mode`, `support_used`, `response`, `result` and `feedback_version`. Store only fields actually needed; raw responses and timestamps need not leave the device. Keep currency and cosmetics in separate game state. A network failure or repeated submission must not duplicate rewards or change a recorded assessment.

For runtime AI, define allowed sources, grading boundaries, fallback behavior and a route to human review. Test plausible but wrong explanations, equivalent correct answers and unavailable service. Evaluate learning after assistance is removed. Research on particular tutors does not establish that every chatbot helps, or that compulsory waiting before help is beneficial. AI used to build the application does not imply AI calls in the finished product.

When coordinating specialists or agents, give them the same goal, task examples and evidence rules. Separate content correctness, learning design, playability and implementation checks. Resolve disagreements using an example or source. Multiple personas in one prompt are not independent validation; use independent agents only when authorized and useful.

### Learning Games: Validate three different outcomes

1. Technical behavior: correct and alternative answers, misconception, repeated guessing, reveal, retry, resume and applicable network failure. Check that supported success never silently becomes independent mastery.
2. Usability and play: observe intended users attempting the first task and recovering from an error. Note confusion, strategic choices and whether they can stop. A small pilot diagnoses problems; it cannot establish a population effect.
3. Learning: assess a new unaided task, delayed retention where relevant, and transfer beyond the game's surface. For a comparative claim, use a credible alternative with comparable content and time; account for prior knowledge, attrition and unequal participation. Report uncertainty and avoid treating time-on-site or enjoyment as learning.

For small projects, document the learning hypothesis and a feasible pilot. For consequential products, specify outcomes and comparison before collecting data. Keep play metrics and learning metrics separate. Remove or revise a mechanic when it encourages shortcuts, discourages help, or adds effort without a useful learning role.

### Learning Games: Evidence and its limits

- [Sailer & Homner, 2020](https://doi.org/10.1007/s10648-019-09498-w): meta-analysis supports average benefits of gamification, with heterogeneous results; motivational and behavioral effects were less stable under stricter study-quality analysis. This is no guarantee for a particular badge or leaderboard.
- [Clark et al., 2016](https://doi.org/10.3102/0034654315582065): game comparisons and design-enhancement comparisons support attention to instructional design and scaffolding. A medium alone does not determine learning.
- [Li et al., 2024](https://doi.org/10.1007/s11423-023-10337-7): small average intrinsic-motivation benefit across 35 interventions. Perceived competence is distinct from measured subject mastery.
- [Habgood & Ainsworth, 2011](https://doi.org/10.1080/10508406.2010.508029): two studies of one mathematics game support integrating learning into core actions. The small, specific samples do not establish a universal game formula.
- [Agarwal et al., 2021](https://doi.org/10.1007/s10648-021-09595-9) and [Ruitenburg et al., 2026](https://doi.org/10.1007/s10648-026-10225-5): classroom evidence for retrieval and context-dependent practice schedules. The latter distinguishes retrieval, spacing and interleaving; sparse moderator groups limit generalization.
- [Wisniewski et al., 2020](https://doi.org/10.3389/fpsyg.2019.03087): feedback effects vary; actionable information matters. [Sinha & Kapur, 2021](https://doi.org/10.3102/00346543211019105): problem solving before instruction can help under designed conditions, with important learner and implementation boundaries.
- [Almeida et al., 2023](https://doi.org/10.1016/j.infsof.2022.107142): mapping identifies reported adverse effects and shortcuts. Counts of negative reports do not estimate how often a mechanic harms users.
- [MIT / Learning Games Network, 2015](https://education.mit.edu/wp-content/uploads/2018/10/BalancedDesignGuide2015.pdf): a design framework linking goals, actions and evidence. [George Fan, GDC 2012](https://media.gdcvault.com/gdc2012/slides/Design%20Track/Fan_George_How%20I%20Got.pdf): practitioner experience with playable onboarding. Both inform design; neither supplies a causal estimate of educational effectiveness.
- [Bastani et al., 2025](https://doi.org/10.1073/pnas.2422633122) and [Kestin et al., 2025](https://doi.org/10.1038/s41598-025-97652-6): different experiments show why tutor design and unaided outcomes matter. Populations, subjects and interventions differ.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) supplies accessibility criteria; [CAST UDL 3.0](https://udlguidelines.cast.org/) supplies a design framework. These have a different evidential role from learning experiments.

### Learning Games: Connect experience, mechanics and transfer

Use MDA as a design lens: describe the intended experience, expected player behavior and rules that produce it. For example, discovery may need a controllable model and meaningful observations; expression may need multiple valid constructions. Do not restrict every subject to one game genre. SDT can guide attention to autonomy, competence and relatedness; neither MDA nor an Octalysis label proves effectiveness.

For an open engineering puzzle, define constraints and a verifiable success condition without requiring the author's one solution. Offer comparison of the learner's own valid designs along relevant competing criteria, such as resource use and accuracy. A community histogram needs actual suitable data and optional sharing; do not invent a distribution. Optimization need not earn extra currency.

Connect game representations to domain notation or real decisions, then check a new case outside the game's surface cues. Do not impose a split screen or three stages on every learner. Game feel should communicate meaningful change without obscuring reasoning. Keep streaks and rewards optional and nonpunitive; interruption must not remove learning evidence or help. Public progress requires a sharing choice.

[MDA by Hunicke, LeBlanc and Zubek](https://www.cs.northwestern.edu/~hunicke/MDA.pdf) is a design framework. The cited learning-game studies above have distinct populations and outcomes; do not use product retention numbers as learning gains.

## Reference: design-dialogue

Source section: Dialogue during educational design


Use at the first substantive pedagogical choice and when new evidence or changed requirements reopen it. These rules are a design workflow, not experimental claims about learning.

### Design Dialogue: Identify the learner and learning conditions

Age, educational role and subject experience are different attributes. “Child” describes an age context; “pupil” and “student” describe educational roles whose usage varies across countries. Categories overlap. Use “learner” or “participant” in general design and locally appropriate language in the product. School examples do not restrict the skill to children. Direct instructions can simply say “Try”, “Explain” or “Compare”.

Before selecting a method, build a brief working audience profile from known context: age group and setting; prior knowledge of this topic; reading and language; independence and available support; goal and assessment consequences; devices and functional access needs. These are audience design facts, not a mandatory personal record. Do not require a birth date, diagnosis or complete school history. Mark unknowns or assumptions; the word “student” does not establish them.

| Context and useful term | What to establish | Possible adaptation when needed |
| --- | --- | --- |
| Preschool child, when requested | Reading, controls, adult accompaniment and purpose of screen activity | Concrete short instructions, shared play and off-screen activity; do not assume independent reading |
| Primary-school pupil or local equivalent | Concepts, notation, reading the task and devices | Link concrete representation to concept, demonstrate controls and provide support |
| Lower-secondary learner or local equivalent | Prerequisites, classroom variation and group work | Compare strategies, explain and choose support toward a common goal |
| Upper-secondary or vocational student | Academic or vocational field, experience and assessment purpose | Subject problem, argument or professional scenario; simulation does not replace practical assessment |
| University student | Discipline prerequisites and experience with this topic | Authentic tasks, evidence and multiple solutions; examples remain available for new topics |
| Adult participant, independent learner or worker | Personal goal, experience, time and real use | Relevant situations, skip known material, flexible pace and resumption |
| Older adult, when relevant | Individual experience, language, controls and access needs | Adjust text, time or controls as needed; age does not imply poor digital experience |
| Mixed group | Shared needs and needs requiring variants | Common goal, optional support, varied entry tasks and individual evidence |

These are design options, not developmental diagnoses or required age-to-method mappings. School stages and grade names vary internationally. A child may be advanced in the subject and an adult a beginner. Language support, accessibility and pace differences can apply to any group. Do not assign fixed visual, auditory or other learning styles.

Distinguish who learns, who operates the application and who sees results. A teacher may run a shared display, a parent accompany a child, and the creator may be neither. A child audience does not automatically determine who can see results. Define roles and access for actual use.

When a missing fact changes the design, ask, for example: “Is this for primary-school children, older school learners or adult beginners? What can they already do in this topic?” Tailor the options; do not repeat every group or known information. Clarify an ambiguous “students” only when the setting affects the result.

Explain who benefits from a proposed method here and why: “For these adult beginners, I recommend a worked example from their work, then less support as independent attempts improve.” Experienced children may instead benefit from an open challenge. An audience change reopens affected language, content, support, assessment and controls, not automatically the entire project.


### Design Dialogue: Offer at the point of need

Take known audience, prior knowledge, goal, jurisdiction, devices, time and constraints from the project. Ask for a missing fact only if it changes the decision. The default is a guided conversation. The creator can delegate one choice or subsequent routine choices, then resume guidance later.

| Trigger | Relevant choices to explain |
| --- | --- |
| Goal and first activity | Worked example with fading, guided inquiry, retrieval, construction or authentic project |
| Motivation and participation | Personal progress, meaningful choice, cooperative roles, optional game mechanics |
| Error and help design | Targeted hint, contrasting example, direct explanation and another attempt |
| Assessment | Formative feedback, criterion rubric, independent check, portfolio or supported peer review |
| Continued use | Session-only state, local continuation, spaced review or calibrated difficulty |
| Prototype evidence | Repair a misleading representation, reduce support, add transfer or remove an exploited reward |

These are opportunities, not mandatory stops. Combine related choices in a small project. Present only viable options, with a short description, an example in this product and the consequential cost, data need or limitation. Recommend an option and ask one focused question. Allow a simple version or deferral where useful; do not require the creator to know theory names. Additional methods are available on request.

### Design Dialogue: Remember decisions

Reuse the conversation for small tasks; for longer work use the project's existing design record. Keep goal, constraints, method ID, reason, status, declined alternatives and unresolved questions. Suggested statuses: `offered`, `selected`, `implemented`, `verified`, `deferred`, `declined`. Keep this separate from learner records. A new requirement reopens only affected decisions; explain why. Do not equate lack of response with selection. Continue independent work while a material choice is pending.

### Design Dialogue: From a choice to a product

Use the method card's learner action, evidence, support and check. Keep one coherent learning sequence; explain incompatible choices. A worked example can precede later retrieval; productive failure needs subsequent consolidation. Neither implies testing on every screen.

For an offline fractions activity: “I recommend combining pieces and showing the matching fraction because the goal is equivalence. A number line instead emphasizes equal position; completing a worked example provides more initial support. Which should be the main activity?” Later, offer a new task without pieces or an error-analysis task to check transfer. Do not repeat the initial interview.

The creator is commissioning an application. Do not turn this conversation into mandatory tutoring, coding homework or unfinished TODOs. At handoff show where each selected method works, what was checked and what remains uncertain. Automatic skill discovery depends on the host; test discovery separately from behavior after invocation.

## Reference: cognitive-ux

Source section: Cognitive interface and representations


Read when designing diagrams, multimedia, instructions, feedback placement or an interface that may obscure the learning task. Apply to the intended learners and devices, not to a fixed visual style.

### Cognitive Ux: Keep attention on the decision

Remove irrelevant competing motion and sound during demanding work; retain useful context and controls. Put related labels and explanations close to their referents without obscuring the object. On small screens use a linked highlight, accessible description or sequential view when adjacent placement is impractical. Color alone cannot carry the distinction.

Segment complex operations into learner-controlled steps. Introduce unfamiliar controls and terms before combining them. Preserve a direct route for experienced learners and a way back to help. Animation should clarify a change or action; provide reduced-motion behavior and an equivalent understandable static state.

### Cognitive Ux: Link representations and check transfer

When concrete objects support an abstract concept, show how the same relationship appears in objects, diagrams and domain notation. Explain the correspondence, then ask for a new application with less surface support. A split view is one implementation, not a requirement. Keep equivalent keyboard and non-drag paths. Verify that learners cannot succeed merely by matching colors or positions.

Example: manipulate equal quantities, show the corresponding equality and ask why it stays true; later solve a new equality without the manipulative. Experienced learners may start with notation. Restore the representation if it helps. For nonmathematical tasks, transfer may mean evaluating a new source or applying a procedure in another scenario.

### Cognitive Ux: Preserve access and meaningful evidence

Avoid unnecessary simultaneous streams, but preserve captions, transcripts, replay, language support and screen-reader access. A redundancy principle is not a ban on text alongside audio. Do not hide essential instructions in hover-only tips. If audio or time is the assessed skill, state the conditions and review accommodations explicitly.

For a conceptual checkpoint, an optional confidence judgment can help compare belief with performance. Do not treat confidence as mastery or require it after every action. Feedback should explain the relevant contrast and provide an opportunity to use it; do not manufacture surprise or doubt about correct work.

Check label readability, focus order, zoom, narrow layouts, reduced motion and the complete help/retry path. Inspect the learner's actual task, not only component appearance. State unperformed checks.

### Cognitive Ux: Sources and limits

[Waxman & Goldie, 2023](https://media.repository.chds.hsph.harvard.edu/static/filer_public/ca/62/ca625803-3d73-4855-b3e1-765870ce3772/2023_jwaxman_monograph_cogtheory_multimed.pdf) informs design choices, not universal layout prohibitions. [Matlen and Devlin, 2020](https://web.stanford.edu/~kdevlin/Papers/Matlen-Devlin_CHI2020.pdf) describes an early transfer-oriented concept, not validation of every split-screen design. [W3C captions](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html) explains accessibility conditions. Verify current normative requirements for the target release.

## Reference: adaptive-practice

Source section: Adaptive practice and continued learning


Read when the product needs repeated sessions, scheduling or difficulty selection. Distinguish when to review, which task to present and how much help to offer. They need not use the same model.

| Need | Small implementation | Optional extension and prerequisites |
| --- | --- | --- |
| One activity | Reviewed tasks, explicit sequence, help and session state | Usually no persistent learner model |
| Recall across days | Explicit review schedule and local history | FSRS for stable items and interpretable review events |
| Select difficulty | Reviewed item levels and transparent branching | Elo with suitable response data, uncertainty and calibration |
| Track skill dependencies | Skill map with independent evidence | BKT or IRT only with a defensible model, data and validation |
| Long-term plan | Goal, available time, current phase and next task | Revisable milestones, carry-over questions and review dates |

Explain the function before the algorithm. Preserve the existing stack; do not install a scheduler, backend or account system merely because it is listed here. Simple rules remain legitimate when their limits are explicit. HLR is another trained recall model for suitable data, not a default implementation requirement.

### Adaptive Practice: Conditions before adaptation

Define stable item/skill IDs, content versions, response interpretation and assistance conditions. Separate guessed, assisted, revealed and independent responses. Follow the chosen library's rating semantics; do not silently treat every assisted response as independent recall. Keep game currency outside the learning model. Use minimal data and timestamps only where needed for scheduling.

Specify cold-start behavior and a useful fallback when history is absent, corrupt or outdated. Review assumptions against representative data, including language and access conditions. Permit teacher correction and learner access to help. Predicted success is uncertain; neither a universal 80–90% success target nor two correct answers measures ZPD or proves mastery. Desired recall retention is a workload tradeoff, not a guaranteed learning outcome.

Use a maintained, version-checked implementation if an algorithm is selected. Test updates, time zones/day boundaries, duplicate submissions, content changes, export/resume and invalid data. Compare the extension with the simple baseline; prediction accuracy, engagement and learning are separate outcomes. Do not infer disability or personality from response time.

### Adaptive Practice: End or resume a phase

Record the result, assistance conditions, unresolved questions and feasible next step. Completion of a phase is distinct from demonstrated mastery. Creating a new phase does not complete the previous one automatically. Summaries preserve necessary evidence pointers and uncertainty rather than entire transcripts. On return, verify stale assumptions with a proportionate task; interruptions should not erase progress.

### Adaptive Practice: Sources

[Anki FSRS documentation](https://docs.ankiweb.net/manual/deck-options), [Pelánek on educational Elo](https://www.fi.muni.cz/~xpelanek/publications/CAE-elo.pdf), and [Settles and Meeder on HLR](https://research.duolingo.com/papers/settles.acl16.pdf). These describe particular models and settings; they do not establish the effectiveness of a new app. Check current implementation documentation when integrating a library.

## License notice

```text
MIT License

Copyright (c) 2026 Luděk Sušický

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
