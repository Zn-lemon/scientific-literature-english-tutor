# Scientific Literature English Tutor
# 科研英语精读与写作教练

An open Agent Skill for sentence-by-sentence scientific-paper reading, academic-English training, and research-writing practice.

一个开放的科研英语学习 Skill，帮助研究生和科研人员通过高质量英文论文，训练逐句阅读、学术表达、主动仿写与科研写作能力。

## What this Skill does

- **Research-direction-matched literature discovery:** identify a learning corpus of up to 20 relevant papers, prioritizing Cell, Nature, Science, PNAS, Nature Communications, and other verified JCR Q1 journals.
- **Sentence-by-sentence close reading:** explain meaning, grammar, syntax, vocabulary, collocations, rhetorical function, and the author's writing choices.
- **Three focused training mechanisms:** academic near-synonym discrimination, Chinglish diagnosis and revision, and active sentence imitation / writing transfer.
- **Stage-based examinations:** assess learning after sections such as Abstract, Introduction, Results, Discussion, and Conclusions.
- **Diagnostic learning reports:** provide scores, error analysis, targeted improvement advice, and progress checkpoints.
- **Baseline paper-writing rubric:** evaluate scientific English writing quality using a transparent six-dimension, 100-point instructional rubric.
- **Author-contribution evidence:** record first/corresponding-author roles and available CRediT writing contributions without overstating individual authorship.

The default teaching language is Chinese, but the Skill can follow the learner's language preference. It is suitable for biology, medicine, life sciences, and other research fields.

## Package structure

```text
scientific-literature-english-tutor/
├── SKILL.md
├── README.md
├── CHANGELOG.md
└── references/
    ├── exam-and-assessment.md
    ├── literature-discovery.md
    ├── progress-and-assessment.md
    ├── sentence-analysis.md
    ├── training-mechanisms.md
    └── writing-quality-scorecard.md
```

## Installation

Copy the complete `scientific-literature-english-tutor` directory into the skills directory supported by your AI agent. Keep `SKILL.md` and the `references/` directory together.

Common locations include:

- Codex-compatible setups: project-level `.agents/skills/` or the configured user-level skills directory.
- Claude Code: `.claude/skills/`.
- Other Agent Skills-compatible tools: follow the application's documented skills directory.

## Using the Skill

1. Upload a scientific-paper PDF or provide a research direction.
2. Ask the agent to use this Skill and begin with the Abstract.
3. Work through the paper sentence by sentence and complete the exercises.
4. Complete the stage examination after each learning stage.
5. Save the progress checkpoint, personal error log, and vocabulary / expression notes between sessions.

Example prompt:

> Use Scientific Literature English Tutor to study this paper sentence by sentence. Start with the Abstract, explain each sentence's academic vocabulary, grammar, collocations, and rhetorical function, then give me the exercises without revealing the answers first.

## Baseline writing-quality rubric

The public Skill includes a baseline instructional rubric with six dimensions:

1. Academic vocabulary precision — 20 points.
2. Syntax and sentence control — 20 points.
3. Paragraph logic and argumentation — 20 points.
4. Natural academic expression — 15 points.
5. Scientific reasoning and claim calibration — 15 points.
6. Clarity and concision — 10 points.

The rubric is an instructional framework, not a standardized or externally validated measure of English proficiency or scientific merit. Journal prestige, citation counts, and author nationality are not substitutes for direct evaluation of the paper's text.

## Open-source scope and project boundary

This repository is the **public learning-entry layer** of a broader product roadmap. It contains the open Skill instructions, baseline teaching workflows, and baseline writing-quality rubric.

The MIT License applies to the files distributed in this repository. It does not grant access to, or license, separate materials that are not included here. Planned separate components may include:

- proprietary literature-evaluation datasets and curated database services;
- advanced scoring, calibration, ranking, and anti-abuse systems;
- private user-feedback datasets and operational analytics;
- hosted backend services, commercial APIs, account systems, and subscription features;
- future application code that is maintained and licensed in a separate repository.

Those separate components are not included in this public Skill repository and will have their own access and licensing terms. The public baseline rubric remains available under this repository's MIT License; improvements to the private service do not retroactively change the license on already published MIT-licensed files.

## Feedback and contributions

Feedback and pull requests are welcome for improving the public Skill, documentation, teaching clarity, and baseline exercises. Please do not submit private user data, copyrighted full-text PDFs without permission, API keys, credentials, or confidential datasets.

User feedback can inform future revisions, but a single user rating does not automatically change a paper's score or the public rubric. Any future score revisions should be evidence-based, versioned, and documented.

## Version

Current version: `1.2.0`

See [CHANGELOG.md](CHANGELOG.md).

## Important evaluation notes

- Evaluate the actual accessible text of each paper; do not infer writing quality from the journal name alone.
- Verify JCR quartiles against a named JCR edition and subject category. JCR and Chinese Academy of Sciences quartiles are not interchangeable.
- CRediT contribution statements document declared roles; they do not prove that one author wrote every sentence.
- Coauthors, editors, language-editing services, and journal copyediting may affect the final text.
- If the full text or evidence is unavailable, state the limitation instead of inventing a score or contribution claim.
