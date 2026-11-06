# Changelog

## 2.0.0 — 2026-11-06

Scores from 1.2.0 and 2.0.0 are not directly comparable. Record `rubric_id` and `rubric_version` with every stored score.

### Breaking

- Writing-quality rubric `slet-writing-quality` is now `rubric_version` 2.0.0. The six dimensions, their maxima and the 85 / 75 totals are unchanged. New: each band has a fixed score range (lower bounds at 90%, 70% and 50% of the maximum, rounded up); each dimension needs at least two located excerpts; an issue is scored in one dimension only, in a fixed order; confirmed format-conversion problems are not penalized; inconsistencies between text, legends and Methods are scored under Clarity and concision only.
- Grade gates: A needs a total of at least 85 and every dimension at least Good; B needs at least 75 and no Weak dimension; otherwise C. A total of 85 or more with an Adequate dimension, which was an A in 1.2.0, is now a B.
- Evaluation status: every AI score is `preliminary`; only a human can set `final`, and only when evidence_scope is `full_text`. `abstract_only` and `metadata_only` records get a screening decision (`advance`, `reserve`, `exclude`) and no score. A second independent scoring is recommended for totals of 73–77 or 83–87, or when a dimension is marked uncertain; two scorings are never averaged.
- Author-evidence labels renamed. Single-paper: Strong → `documented-drafting`; Moderate → `documented-editing` (the "repeated strong papers" part of 1.2.0 Moderate now belongs to the cross-paper profile); Limited / unclear → `role-only`; Unverified → `unverified`. Cross-paper: Strong → `well-supported`; Moderate → `partially-supported`, which now needs at least two A/B papers, so one paper with documented drafting is `single-paper`; Limited → `single-paper` or `insufficient`; Insufficient evidence → `insufficient`.
- Learner writing is scored on the same six dimensions and bands, with no A/B/C grade and no gates. The five-part 20-point learner rubric is retired.
- Round structure: at most four sentences per round; depth tiers `full`, `standard` and `light`; one practice item per mechanism plus one extra item, from the review queue when it has entries; about 6,000 characters per round.
- Frontmatter: `version` moved to `metadata.version`, as the Agent Skills specification requires; `license: MIT` added.

### Added

- Content label 【背景知识·非原文 Background】 for the tutor's general knowledge.
- Sentence locators `<SEC>-P<n>-S<m>`, with page numbers only for PDF sources.
- `source_version` and a learner profile (first language, English level, goal, explanation language, pace) in the checkpoint.
- Error-code table (15 codes, with `SCI` counted apart from language errors) and its mapping to the six dimensions.
- Review queue and exercise status, including `shown-without-attempt` for answers shown before an attempt.
- Exams: answer key and item map written before the exam; readiness decisions; a competency below 60% of its points means at least `reinforce-then-advance`.
- Corpus building: screening funnel with counts at each layer; per-source status log in which failures are never recorded as zero hits; journal restriction by field or ISSN, tested once in PubMed, Europe PMC and Crossref.
- Optional API credential variables `SLET_OPENALEX_API_KEY`, `SLET_NCBI_API_KEY` and `SLET_CROSSREF_MAILTO`, with rules for never printing or storing values.
- Commands: 详细 / Full detail, 精简 / Brief, 强化 / Intensive practice, 显示答案 / Show answer, 保存进度 / Save checkpoint.

### Changed

- SKILL.md is now a router plus the round loop; each rule is written in one reference file only, and the other files point to it.
- The research-profile card uses fields that fit any discipline.
- Practice scenarios come from the learner profile instead of fixed research topics.
- The 70–79 band uses one rule: a short reinforcement set, then the next stage.
- The stage exam's writing task replaces the paragraph task that would have closed the stage.
- The suggest / indicate / imply contrast describes different kinds of link instead of a fixed strength scale.

### Fixed

- The empty `## Workflow` heading, which placed the core workflow inside the corpus module.
- A quality-checklist item that still asked for evidence of author language and nationality, which 1.2.0 had dropped as a criterion.
- The corpus selection table, whose header had 10 columns and whose separator row had 9.
- Query templates that used journal names as free-text terms.
- Screening eligibility now aligns with `partial_text` scoring: a sufficiently substantial partial text may proceed, but insufficient evidence remains not assessable.
- Rules duplicated between SKILL.md and the reference files that had started to differ.
- Two consecutive top-level headings in README and a heading-level jump in the exam report template.

## 1.2.0 — 2026-11-02

- Replaced foreign/native-English-speaker filtering with evidence-based scientific writing-quality evaluation.
- Added a six-dimension, 100-point paper-level writing rubric and A/B/C/not-assessable classifications.
- Added separate first/corresponding-author writing-contribution evidence, including CRediT roles.
- Added cross-paper comparison of the same author's writing consistency, with explicit attribution limitations.
- Added a writing-quality scorecard reference and expanded corpus progress tracking.
- Retained the 20-paper research-direction-matched corpus, top-journal priority, stage exams, and diagnostic reports.

## 1.1.0 — 2026-11-02

- Added a research-direction-matched 20-paper discovery and screening workflow.
- Added journal prioritization: Cell, Nature, Science; then PNAS, Nature Communications, and verified JCR Q1 journals.
- Added initial author-role and language-evidence checks; these language/nationality filters were retired in v1.2.0 in favor of direct writing-quality evaluation.
- Added JCR edition/category verification and safeguards against confusing JCR and CAS quartiles.
- Added stage-based exams after each completed paper section, with a 100-point rubric, performance bands, diagnostic report, and adaptive improvement plan.
- Expanded progress tracking for literature corpora and stage exam results.

## 1.0.0 — 2026-11-02

- Initial release.
- Added sentence-by-sentence source-based reading and grammar analysis.
- Added academic vocabulary, collocation, and authorial writing-choice analysis.
- Added three mandatory training mechanisms:
  - academic near-synonym discrimination;
  - Chinglish diagnosis and revision;
  - active imitation and writing transfer.
- Added paragraph- and section-level analysis.
- Added progress checkpoints, personal error logs, and final learning portfolio.
- Packaged as a portable Agent Skills directory for GitHub and compatible SkillHub registries.
