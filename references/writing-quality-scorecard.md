# Scientific English writing-quality scorecard

Scope: the paper-level writing-quality rubric (dimension boundaries, anchor bands, scoring procedure with evidence and single attribution, grade gates, evidence scope, evaluation status and finalisation), learner-writing scoring, and author writing-contribution evidence with the cross-paper author profile.
Not here: journal tiers, query construction, screening decisions and corpus selection (references/literature-discovery.md); error-code definitions and the learner feedback steps (references/training-mechanisms.md); verbatim and locator rules (references/sentence-analysis.md); exam construction and readiness (references/exam-and-assessment.md); checkpoints and corpus tracking (references/progress-and-assessment.md).

rubric_id: slet-writing-quality
rubric_version: 2.0.0

## 1. Purpose and limits

Use this scorecard to judge how well the accessible English text of a research paper can serve as a writing model, and to score learner writing on the same dimensions (§7). Apply it the same way to every paper. Judge the text itself, not the journal's reputation or assumptions about the authors.

- The dimensions, bands, gates and second-scoring triggers are internal teaching rules. They have not been externally validated and are not a standardised English-proficiency test.
- A, B and C are instructional categories for building a learning corpus, not ratings of journals, authors or scientific merit.
- Agreement between two scorings shows that the procedure is repeatable under the same conditions. It does not show that the scores are correct.
- Keep writing quality separate from scientific novelty, correctness and journal prestige. Do not reward length, rare vocabulary or complexity for their own sake; simple, direct and well-calibrated writing can reach the top band.

## 2. Dimensions and boundaries

The six dimensions and their maxima are fixed and total 100 points. "Does not count here" names the dimension where a neighbouring issue is scored instead. The error codes are defined in references/training-mechanisms.md §4; this table is the only place that maps them to dimensions.

| Dimension | Max | Counts here | Does not count here | Error codes |
|---|---:|---|---|---|
| Academic vocabulary precision | 20 | Choice of terms, verbs, nouns and modifiers; register; near-synonym choice; terminology and naming conventions | Fixed word partnerships and prepositions (Natural academic expression); hedge or booster strength (Scientific reasoning and claim calibration) | LEX, TRM |
| Syntax and sentence control | 20 | Clause construction; agreement and number; tense, aspect and voice; word order; run-ons, fragments and dangling modifiers; variety where useful; ease of parsing | Articles and determiners, verb complementation patterns (Natural academic expression); links between sentences (Paragraph logic and argumentation) | NUM, TNS, ORD, STR |
| Paragraph logic and argumentation | 20 | Progression from question and evidence to result, interpretation and inference; topic sentences; transitions and connectives between sentences and paragraphs | Strength of a single claim (Scientific reasoning and claim calibration); redundancy inside a sentence (Clarity and concision) | LNK |
| Natural academic expression | 15 | Articles and determiners, prepositions, collocations, verb patterns and complements, idiomatic scholarly phrasing | Wrong word meaning (Academic vocabulary precision); grammatical construction (Syntax and sentence control) | ART, PRP, COL, VPT |
| Scientific reasoning and claim calibration | 15 | Distinguishing observation, result, interpretation, hypothesis and conclusion; hedge and booster strength; scope of generalisation; causal wording | Whether the conclusion is true; the quality of the experiments | HDG, SCI |
| Clarity and concision | 10 | Readability and economy; redundancy and repetition; punctuation and spelling slips; wording that is inconsistent between main text, figure legends and Methods | Problems that fit a higher-priority dimension (§4); the experiments behind an inconsistency | RED, PUN |

SCI is a reasoning error and is counted apart from the language codes in the learner's error log (references/training-mechanisms.md §4). Spelling slips have no code of their own; score them under Clarity and concision.

## 3. Anchor bands

The four bands keep their 1.2.0 descriptions:

- **Excellent:** consistently precise and effective; very few issues.
- **Good:** clear and reliable, with occasional weaknesses.
- **Adequate:** understandable, but with recurring imprecision or awkwardness.
- **Weak:** frequent problems that make the text unsuitable as a primary writing model.

### 3.1 Score ranges

Each band has a fixed point range. The lower bounds of Excellent, Good and Adequate are 90%, 70% and 50% of the dimension maximum, rounded up; Weak starts at 0.

| Max | Excellent | Good | Adequate | Weak |
|---:|---|---|---|---|
| 20 | 18–20 | 14–17 | 10–13 | 0–9 |
| 15 | 14–15 | 11–13 | 8–10 | 0–7 |
| 10 | 9–10 | 7–8 | 5–6 | 0–4 |

### 3.2 Band criteria by dimension

| Dimension | Max | Excellent | Good | Adequate | Weak |
|---|---:|---|---|---|---|
| Academic vocabulary precision | 20 | Terms and verbs exact throughout; register stable | Mostly exact; a few loose or vague word choices | Recurring imprecise words or register slips | Frequent wrong or vague words that blur the meaning |
| Syntax and sentence control | 20 | Sentences controlled and easy to parse; errors rare | Generally controlled; occasional errors or sentences that need rereading | Recurring grammatical errors or hard-to-parse sentences | Frequent errors that obstruct reading |
| Paragraph logic and argumentation | 20 | Each paragraph moves clearly from claim to evidence to interpretation | Clear overall; an occasional weak link or crowded paragraph | Progression often implicit; links missing or misleading | Paragraphs read as lists; the argument is hard to follow |
| Natural academic expression | 15 | Collocations, prepositions and articles idiomatic throughout | Mostly natural; a few non-idiomatic phrases | Recurring article, preposition or collocation errors | Frequent non-idiomatic phrasing throughout |
| Scientific reasoning and claim calibration | 15 | Claim strength matches the paper's own evidence throughout | Mostly calibrated; one or two claims slightly stronger or weaker than the evidence | Several claims over- or under-stated, or result and interpretation blurred | Claims routinely exceed the evidence, or observation and inference are confused |
| Clarity and concision | 10 | Economical and easy to read; no avoidable repetition | Readable; some redundancy or a minor inconsistency | Recurring redundancy, slips or inconsistencies that slow reading | Wordy, repetitive or inconsistent enough to impede understanding |

## 4. Scoring procedure

1. Record what was read: the sections, source_version (references/progress-and-assessment.md §1) and evidence_scope (§6.1).
2. For each dimension, choose the band first (§3.2), then give a whole-number score inside that band's range (§3.1).
3. Evidence: support each dimension with at least 2 verbatim excerpts, each with a locator (references/sentence-analysis.md §2). For Adequate or Weak, at least 1 excerpt must show a problem; for Excellent, at least 1 must show a strength. Quote as the source reads (references/sentence-analysis.md §1) and keep excerpts short.
4. Single attribution: deduct for an issue in one dimension only. When it fits more than one, score it in the first that applies in this order: Scientific reasoning and claim calibration > Paragraph logic and argumentation > Academic vocabulary precision > Syntax and sentence control > Natural academic expression > Clarity and concision. Example: "indicate" where the data only "suggest" is scored once, under Scientific reasoning and claim calibration.
5. Format conversion: do not deduct for a problem you can confirm was introduced by conversion, such as line-break hyphens, lost italics or spaces at JATS inline tags (check against the PDF or publisher page where possible). If you cannot confirm the cause, score the published text as it stands and list the item under limitations.
6. Inconsistency: when the main text, figure legends and Methods disagree (for example, two different treatment durations), score only the inconsistent wording, under Clarity and concision. This fixed placement takes precedence over the order in step 4. Do not judge the experiment itself.
7. Claim calibration: judge only whether the strength of the wording fits the paper's own evidence, not whether the conclusion is right.
8. Add the six scores, apply the grade gates (§5), check the second-scoring triggers (§6.3) and write the report (§9).

## 5. Grade gates

Check assessability first, then apply the gates in order and stop at the first that is met:

- **Not assessable:** evidence_scope is `abstract_only` or `metadata_only`, the available text is too corrupted to score fairly, or too little main text is available to support the minimum evidence required in §4. Give no score and no A, B or C grade, and do not invent one; the paper receives only a screening decision (references/literature-discovery.md §7).
- **A:** total ≥ 85 and every dimension at least Good.
- **B:** total ≥ 75 and no Weak dimension.
- **C:** total below 75, or any Weak dimension.

The 85 and 75 totals are unchanged from 1.2.0. The band conditions are new in 2.0.0: a total of 85 or more with an Adequate dimension is now a B. Worked example: dimension scores of 16, 15, 16, 10, 11 and 7 sum to 75. Natural academic expression (10 of 15) is Adequate and no dimension is Weak, so the grade is B; one point less in any dimension would make it C.

## 6. Evidence scope, status and finalisation

### 6.1 Evidence scope

| evidence_scope | What was read | Scoring |
|---|---|---|
| `full_text` | Abstract, Introduction, Results, and Discussion or Conclusions, each in full; state whether Methods and figure legends were read | Score; may later become `final` |
| `partial_text` | Any of those parts missing | Score and list the missing parts; never `final` |
| `abstract_only` | Abstract only | No score; screening decision only |
| `metadata_only` | Title and bibliographic record only | No score; screening decision only |

A combined "Results and Discussion" section counts as both parts. When a paper's headings differ (for example, a letter whose introduction has no heading), map its parts by function as for locators (references/sentence-analysis.md §2) and state the mapping in the report.

### 6.2 Status

- `preliminary`: every AI score, and any score that a human has not yet confirmed.
- `final`: set only by a human, who records their name and the date, and only when evidence_scope is `full_text`.

### 6.3 Second independent scoring

Recommend a second, independent scoring when the total is 73–77 or 83–87, or when the rater marks any dimension as uncertain. The two raters must not see each other's scores, evidence or notes; for an AI rater, use a separate session that has not seen the first scoring. If the platform cannot provide a second rater, write "second scoring not done" in the report.

Never average two scorings. If they differ, record both per dimension with each rater's evidence, keep the status `preliminary`, and leave the decision to a human.

## 7. Learner writing

Learner paragraphs and exam writing tasks use the six dimensions (§2) and the score ranges (§3.1). Learners receive no A, B or C grade, and the grade gates (§5) do not apply. The feedback steps are in references/training-mechanisms.md §5.

1. Except for routine practice (item 3), report each dimension's band and score, and the total. Name the weakest dimension (lowest score relative to its maximum; on a tie, the one that comes first in the order of §4 step 4) as the next target.
2. Mark a dimension that does not apply to the task as N/A, for example Paragraph logic and argumentation in a single-sentence task. Leave it out of the total and convert the total to a 100-point scale over the remaining maxima, showing the conversion: a learner score of 60 out of 80 applicable points gives 60 / 80 × 100 = 75.
3. Routine single-sentence imitation and Chinglish revision: give the band for each applicable dimension only, with no scores and no total. The weakest dimension is the one with the lowest band, with ties broken as in item 1.
4. Exam writing task: the task score is the converted 100-point total × 15/100, rounded to the nearest whole number with halves rounded up (70 gives 10.5, recorded as 11).

## 8. Author writing-contribution evidence

This evidence is separate from the paper score. Confirm author roles from the article or the publisher record. The comparison workflow is in references/literature-discovery.md §5.

### 8.1 Single-paper label

Give each first and corresponding author exactly one label per paper; the conditions do not overlap.

| Label | Condition |
|---|---|
| `unverified` | The author's first or corresponding role cannot be confirmed |
| `documented-drafting` | Role confirmed; credited with Writing – original draft or equivalent wording such as "wrote the manuscript" |
| `documented-editing` | Role confirmed; credited with Writing – review & editing or equivalent, and not with drafting |
| `role-only` | Role confirmed; no writing credit for this author, because no contribution statement exists, it cannot be read, or it credits no writing role to them |

Quote the contribution statement exactly as published.

### 8.2 Cross-paper author profile

Let n be the number of papers in which the person's first or corresponding role is confirmed (label other than `unverified`) and the paper's writing grade is A or B.

| Profile | Condition |
|---|---|
| `well-supported` | n ≥ 2, and at least one of those papers is `documented-drafting` for this person |
| `partially-supported` | n ≥ 2, and none of those papers is `documented-drafting` |
| `single-paper` | n = 1; report that paper's single-paper label with the profile |
| `insufficient` | n = 0 |

Three or more comparable papers give a firmer basis than two. Report the profile together with the single-paper labels behind it. A profile built on `preliminary` grades is itself provisional. The profile is an evidence summary, not a measurement of a person's English proficiency.

### 8.3 Limits on attribution

- CRediT is a declared contribution taxonomy. It does not prove that one author wrote the paper alone or produced every sentence; never claim that they did.
- Coauthors, professional editors, language-editing services and journal copyediting may all shape the final text. Record coauthor overlap and any stated editing help.
- Do not infer an individual's English ability from one paper.
- Do not use nationality, a person's name, country of employment or presumed native language as a proxy for writing quality. Native-speaker status is not a criterion and is not researched in this workflow.
- Do not exclude an excellent paper because its contribution statement is missing; score the paper and give the authors `role-only` or `unverified` as the evidence allows.
- Use cautious wording such as "documented drafting contribution" or "author-associated writing evidence", not "proven individual writing ability".

## 9. Evaluation report

Write one report per paper and per scoring.

### 9.1 Paper writing quality

- Paper (title, year, DOI, article type):
- rubric_id and rubric_version: slet-writing-quality 2.0.0
- Rater (model and version, or person) and date:
- evidence_scope:
- Sections read, including whether Methods and figure legends were read:
- source_version:

| Dimension | Max | Band | Score | Excerpts with locators |
|---|---:|---|---:|---|
| Academic vocabulary precision | 20 | | | |
| Syntax and sentence control | 20 | | | |
| Paragraph logic and argumentation | 20 | | | |
| Natural academic expression | 15 | | | |
| Scientific reasoning and claim calibration | 15 | | | |
| Clarity and concision | 10 | | | |

- Total (out of 100):
- Grade (A / B / C, or Not assessable):
- Gate result (the §5 condition that decided the grade):
- Dimensions marked uncertain:
- Borderline (total 73–77 or 83–87, or a dimension marked uncertain) and whether a second scoring was done:
- Differences between raters, per dimension, with each rater's evidence:
- Strengths and weaknesses:
- Limitations (missing parts, unconfirmed conversion problems, other):
- Status (`preliminary` or `final`):
- Confirmed by and date (`final` only):

### 9.2 Author-associated evidence

- First author, role confirmation and source:
- Corresponding author, role confirmation and source:
- Contribution statement (quoted exactly) and single-paper label for each author:
- Other papers compared, with their grades:
- Consistency across papers and cross-paper profile:
- Attribution limitations:

## 10. Learning recommendation (qualitative)

Keep this part qualitative: do not give it a score or points.

- Best section for sentence-level study:
- Best paragraph for argument-structure study:
- Most reusable language patterns:
- Cautions against imitation:
- Why the paper is or is not a useful language-learning model:
