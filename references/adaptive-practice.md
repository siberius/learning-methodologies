# Adaptive practice and continued learning

Read when the product needs repeated sessions, scheduling or difficulty selection. Distinguish when to review, which task to present and how much help to offer. They need not use the same model.

| Need | Small implementation | Optional extension and prerequisites |
| --- | --- | --- |
| One activity | Reviewed tasks, explicit sequence, help and session state | Usually no persistent learner model |
| Recall across days | Explicit review schedule and local history | FSRS for stable items and interpretable review events |
| Select difficulty | Reviewed item levels and transparent branching | Elo with suitable response data, uncertainty and calibration |
| Track skill dependencies | Skill map with independent evidence | BKT or IRT only with a defensible model, data and validation |
| Long-term plan | Goal, available time, current phase and next task | Revisable milestones, carry-over questions and review dates |

Explain the function before the algorithm. Preserve the existing stack; do not install a scheduler, backend or account system merely because it is listed here. Simple rules remain legitimate when their limits are explicit. HLR is another trained recall model for suitable data, not a default implementation requirement.

## Conditions before adaptation

Define stable item/skill IDs, content versions, response interpretation and assistance conditions. Separate guessed, assisted, revealed and independent responses. Follow the chosen library's rating semantics; do not silently treat every assisted response as independent recall. Keep game currency outside the learning model. Use minimal data and timestamps only where needed for scheduling.

Specify cold-start behavior and a useful fallback when history is absent, corrupt or outdated. Review assumptions against representative data, including language and access conditions. Permit teacher correction and learner access to help. Predicted success is uncertain; neither a universal 80–90% success target nor two correct answers measures ZPD or proves mastery. Desired recall retention is a workload tradeoff, not a guaranteed learning outcome.

Use a maintained, version-checked implementation if an algorithm is selected. Test updates, time zones/day boundaries, duplicate submissions, content changes, export/resume and invalid data. Compare the extension with the simple baseline; prediction accuracy, engagement and learning are separate outcomes. Do not infer disability or personality from response time.

## End or resume a phase

Record the result, assistance conditions, unresolved questions and feasible next step. Completion of a phase is distinct from demonstrated mastery. Creating a new phase does not complete the previous one automatically. Summaries preserve necessary evidence pointers and uncertainty rather than entire transcripts. On return, verify stale assumptions with a proportionate task; interruptions should not erase progress.

## Sources

[Anki FSRS documentation](https://docs.ankiweb.net/manual/deck-options), [Pelánek on educational Elo](https://www.fi.muni.cz/~xpelanek/publications/CAE-elo.pdf), and [Settles and Meeder on HLR](https://research.duolingo.com/papers/settles.acl16.pdf). These describe particular models and settings; they do not establish the effectiveness of a new app. Check current implementation documentation when integrating a library.
