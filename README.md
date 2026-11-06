# Scientific Literature English Tutor · 科研英语精读与写作教练

An open Agent Skill for sentence-by-sentence scientific-paper reading, academic-English training and research-writing practice.

一个开放的科研英语学习 Skill，帮助研究生和科研人员通过高质量英文论文，训练逐句阅读、学术表达、主动仿写与科研写作能力。

## What this Skill does

- **Close reading in short rounds:** at most four sentences per round, each taught at a `full`, `standard` or `light` depth tier, covering meaning, grammar, vocabulary, collocations, rhetorical function and the author's writing choices.
- **Three training mechanisms every round:** academic near-synonym discrimination, Chinglish diagnosis and revision, and active sentence imitation, with answers held back until the learner attempts them.
- **Stage exams and diagnostic reports:** after the Abstract, Introduction, Results subsections, Discussion and Conclusions, with a 100-point blueprint, the answer key written before the exam, and a readiness decision.
- **Learner records:** sentence locators, a coded error log, a review queue, an expression bank and a checkpoint the learner can save between sessions.
- **Research-direction-matched corpus (optional):** a default target of 20 papers, prioritizing Cell, Nature, Science, PNAS, Nature Communications and other verified JCR Q1 journals, with a screening funnel and a per-source status log.
- **Writing-quality rubric:** a six-dimension, 100-point instructional rubric with fixed score bands and grade gates. AI scores stay preliminary until a human confirms them.
- **Author-contribution evidence:** first and corresponding authors' roles and CRediT writing credits, recorded without overstating individual authorship.

The default teaching language is Chinese, and the Skill follows the learner's language preference. It suits biology, medicine, the life sciences and other research fields.

## Package structure

```text
scientific-literature-english-tutor/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── LICENSE
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

You can obtain the Skill from the repository source or from the GitHub Releases page:
[GitHub Releases](https://github.com/Zn-lemon/scientific-literature-english-tutor/releases).
If your client does not import `.skill` files directly, extract the archive and copy the complete
`scientific-literature-english-tutor` folder into the supported skills directory.

## Using the Skill

1. Upload a scientific-paper PDF or provide a research direction.
2. Ask the agent to use this Skill and begin with the Abstract.
3. Work through the paper round by round and complete the practice items.
4. Complete the stage exam after each learning stage.
5. Save the checkpoint (保存进度) between sessions.

Example prompt:

> Use Scientific Literature English Tutor to study this paper sentence by sentence. Start with the Abstract, explain each sentence's academic vocabulary, grammar, collocations and rhetorical function, then give me the exercises without revealing the answers first.

## Writing-quality rubric

| Dimension | Points | Excellent | Good | Adequate | Weak |
|---|---:|---|---|---|---|
| Academic vocabulary precision | 20 | 18–20 | 14–17 | 10–13 | 0–9 |
| Syntax and sentence control | 20 | 18–20 | 14–17 | 10–13 | 0–9 |
| Paragraph logic and argumentation | 20 | 18–20 | 14–17 | 10–13 | 0–9 |
| Natural academic expression | 15 | 14–15 | 11–13 | 8–10 | 0–7 |
| Scientific reasoning and claim calibration | 15 | 14–15 | 11–13 | 8–10 | 0–7 |
| Clarity and concision | 10 | 9–10 | 7–8 | 5–6 | 0–4 |

Grades: A needs a total of at least 85 with every dimension at least Good; B needs at least 75 with no Weak dimension; otherwise C. A paper read only as an abstract or as metadata gets a screening decision and no score. The full rules are in `references/writing-quality-scorecard.md`.

The rubric is an instructional framework, not a standardized or externally validated measure of English proficiency or scientific merit. Journal prestige, citation counts and author nationality are not substitutes for direct evaluation of the paper's text.

## Optional API credentials

Corpus building works without credentials. With them, OpenAlex, NCBI E-utilities and Crossref allow more requests. The Skill refers to these variable names only; the agent reads their values from environment variables or from a local dotenv file kept outside any git repository and outside the skill directory:

```text
SLET_OPENALEX_API_KEY=<your-key>
SLET_NCBI_API_KEY=<your-key>
SLET_CROSSREF_MAILTO=name@example.org
```

Never put real values in this repository. See `references/literature-discovery.md` §10.

## Upgrading from 1.2.0

2.0.0 changes how papers and learners are scored, so 1.2.0 and 2.0.0 scores are not directly comparable.

- The writing-quality rubric (`rubric_version` 2.0.0) keeps the six dimensions, the maxima and the 85 / 75 totals, and adds fixed score bands and grade gates: a total of 85 or more with an Adequate dimension is now a B, and any Weak dimension gives a C.
- Every AI score is `preliminary`; only a human can make it `final`, and only on full text.
- Author-evidence labels are renamed: single-paper `documented-drafting`, `documented-editing`, `role-only`, `unverified`; cross-paper `well-supported`, `partially-supported`, `single-paper`, `insufficient`.
- Learner writing uses the same six dimensions without grades; the five-part learner rubric is retired.
- `version` moved into `metadata.version`, as the Agent Skills specification requires.

Tools that store SLET scores should record `rubric_id` and `rubric_version` and keep 1.2.0 and 2.0.0 scores apart. Details are in `CHANGELOG.md`.

## Open-source scope and project boundary

This repository is the **public learning-entry layer** of a broader product roadmap. It contains the open Skill instructions, baseline teaching workflows and the baseline writing-quality rubric.

The MIT License applies to the files distributed in this repository. It does not grant access to, or license, separate materials that are not included here. Planned separate components may include:

- proprietary literature-evaluation datasets and curated database services;
- advanced scoring, calibration, ranking and anti-abuse systems;
- private user-feedback datasets and operational analytics;
- hosted backend services, commercial APIs, account systems and subscription features;
- future application code that is maintained and licensed in a separate repository.

Those separate components are not included in this public Skill repository and will have their own access and licensing terms. The public baseline rubric remains available under this repository's MIT License; improvements to the private service do not retroactively change the license on already published MIT-licensed files.

## Feedback and contributions

Feedback and pull requests are welcome for improving the public Skill, documentation, teaching clarity and baseline exercises. Please do not submit private user data, copyrighted full-text PDFs without permission, API keys, credentials or confidential datasets.

User feedback can inform future revisions, but a single user rating does not automatically change a paper's score or the public rubric. Any future score revisions should be evidence-based, versioned and documented.

## Development checks

This repository includes lightweight structural and packaging regression tests.
Run them from the repository root:

```bash
python -m unittest discover -s tests -v
python tools/package_skill.py --output dist/scientific-literature-english-tutor.skill --verify
```

These checks protect package structure and key invariants; they do not establish pedagogical validity
or external validity of the scoring rubric.

## Version

Current version: `2.0.0`

See [CHANGELOG.md](CHANGELOG.md).

## Important evaluation notes

- Evaluate the actual accessible text of each paper; do not infer writing quality from the journal name alone.
- Verify JCR quartiles against a named JCR edition and subject category. JCR and Chinese Academy of Sciences quartiles are not interchangeable.
- CRediT contribution statements document declared roles; they do not prove that one author wrote every sentence.
- Coauthors, editors, language-editing services and journal copyediting may affect the final text.
- If the full text or evidence is unavailable, state the limitation instead of inventing a score or contribution claim.
