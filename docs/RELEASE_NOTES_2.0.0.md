# SLET 2.0.0 — Release notes

**Release date:** 2026-11-06

Scientific Literature English Tutor 2.0.0 restructures the Skill into a concise routing layer and
six focused reference modules. It also makes the writing-quality rubric more explicit and the
learning records more reproducible.

## Highlights

- Short teaching rounds of no more than four sentences, with `full`, `standard` and `light` depth tiers.
- Three recurring practice mechanisms: near-synonym discrimination, Chinglish diagnosis and revision,
  and active sentence imitation.
- Sentence locators tied to the supplied source version; page numbers are used only for PDF sources.
- A coded learner error log, review queue, exercise states and portable progress checkpoints.
- A transparent six-dimension, 100-point paper-writing rubric with fixed score bands and grade gates.
- AI evaluations remain `preliminary`; only a human may set `final`, and only for `full_text`.
- Corpus discovery records screening counts and per-source failures instead of treating failed requests as zero hits.
- Optional API credentials are read from environment variables or a dotenv file outside the repository.

## Breaking changes from 1.2.0

- Scores from 1.2.0 and 2.0.0 are not directly comparable. Store both `rubric_id` and `rubric_version`.
- A paper with a total of at least 85 but an Adequate dimension is now grade B, not A.
- Any Weak dimension results in grade C.
- Learner writing uses the same six dimensions without an A/B/C grade; the previous five-part learner rubric is retired.
- Author-contribution labels and cross-paper profile rules have been revised.
- The Agent Skills version field is now `metadata.version`.

## Limitations

The rubric and teaching thresholds are internal instructional rules, not an externally validated
English-proficiency test or measure of scientific merit. Author contribution statements do not prove
who wrote every sentence. JCR data may be unavailable and must then be marked unverified.
