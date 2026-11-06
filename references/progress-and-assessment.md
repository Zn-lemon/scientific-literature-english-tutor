# Progress tracking, learner records and the learning portfolio

Scope: the checkpoint (core block and corpus block), the learner profile, continuity rules, the error log and expression bank, the review queue, exercise status, the final learning portfolio and corpus tracking.
Not here: error-code definitions (references/training-mechanisms.md §4); sentence locators (references/sentence-analysis.md §2); exam scoring and readiness decisions (references/exam-and-assessment.md §4); writing-quality scores and evaluation records (references/writing-quality-scorecard.md).

## 1. Checkpoint

End every round with a compact checkpoint: the current position, the next sentence, the exercises and any line that changed in this round. 保存进度 / Save checkpoint gives the full checkpoint, with every line that applies, including the learner profile and, in corpus mode, the corpus block; the learner can paste it into a new session. Leave out fields that do not apply yet.

```text
Paper: <title, year, DOI>
source_version: <pdf | jats-xml | html | plain-text>
Mode: <close reading | corpus building | paper rating | assessment | review>
Learner profile: L1 <...>; English level <...>; goal <...>; explanation language <...>; pace <...>
Depth preference: <by signals | full | light>
Current position: <section> | completed up to <locator> ("<opening words>")
Next sentence: <locator>
Exercises: <item id> <mechanism> <status>; ...
New vocabulary / collocations / sentence patterns: ...
Error codes so far: <code> ×<count>; ...; SCI ×<count>
Review queue: <item or code>; ...
Stage exam: <stage> <score>/100 <band> <readiness decision>
Next improvement target: <weakest dimension or competency>; <most frequent code>
Writing-quality evaluation: <where the evaluation record is, or "none">
```

`source_version` is one of:

| Value | Meaning |
|---|---|
| `pdf` | The publisher PDF; page numbers can be given |
| `jats-xml` | JATS full text, for example from PubMed Central or Europe PMC; no page numbers |
| `html` | A publisher web page; no page numbers |
| `plain-text` | Pasted or extracted text; formatting cannot be checked |

Exercise status is one of:

| Status | Meaning |
|---|---|
| `pending` | Shown and awaiting the learner's answer |
| `attempted` | Answered; feedback given |
| `shown-without-attempt` | The answer was shown before an attempt (references/exam-and-assessment.md §5); not counted as mastered |
| `skipped` | The learner chose not to answer; not counted as mastered |

Do not copy writing-quality scores into the checkpoint. When a paper has an evaluation record, the checkpoint says where it is.

In corpus mode, add a corpus block:

```text
Corpus: <n> selected / target <n>; reserve pool <n>
This paper: rank <n>; <direct match | adjacent field | methods>; <journal tier>
Papers studied: <n>; stage exams completed: <n>
Next paper: <rank and title>
```

## 2. Learner profile

Fill the profile once, at the first session; afterwards update it only when the learner changes something. The full checkpoint carries it into a new session (§1).

| Field | Content |
|---|---|
| First language (L1) | Decides which transfer errors to expect; "Chinglish" practice assumes Chinese |
| English level | The learner's own description, or an estimate marked as an estimate |
| Learning goal | For example reading papers, writing a manuscript, or an exam |
| Explanation language | Default Chinese |
| Pace preference | Depth preference and practice load |
| Research field | Used for practice scenarios; the corpus profile card is in references/literature-discovery.md §1 |

Do not guess these fields. Use the defaults in SKILL.md, Start a paper, and say which values are defaults.

## 3. Continuity rules

- Continue from the first uncompleted sentence. Do not repeat completed analysis unless the learner asks for review.
- Do not claim to remember progress across sessions unless it is present in this conversation, a memory source or a saved progress file.
- If progress is missing, state what is known and ask for the checkpoint or the relevant file. Do not guess.
- A short opening phrase of the last completed sentence can confirm the position; it never replaces the locator.
- In 复习 / Review, put weak items, the review queue and recurring errors first, not only the most recent material.

## 4. Error log and expression bank

Log each error found in learner writing:

```text
<locator or task id> | learner's original | <code> | corrected version | reason | reusable rule or collocation | seen before: <yes, count | no>
```

Count `SCI` separately from the language codes. The expression bank collects vocabulary, collocations, near-synonym contrasts and sentence patterns by category, each with its source locator. 查看错误档案 / Error log and 查看表达库 / Expression bank display these records.

## 5. Review queue

Add to the queue:

- items answered wrongly;
- items with status `shown-without-attempt`;
- error codes logged again after an earlier occurrence.

When the queue is not empty, each round takes its extra item from it (references/training-mechanisms.md §6.1), and stage exams cover queue items first (references/exam-and-assessment.md §2.2). An entry leaves the queue when the learner answers an equivalent item correctly in a later round.

## 6. Final learning portfolio

When the paper is complete, consolidate:

1. academic vocabulary list;
2. collocation bank;
3. near-synonym comparison bank;
4. reusable sentence-pattern bank;
5. paragraph-structure examples;
6. personal error log, by code;
7. imitation exercises and revised versions;
8. writing-performance summary;
9. field-specific writing templates;
10. comprehensive review exercises with an answer key;
11. the cumulative stage-score trend (references/exam-and-assessment.md §7).

Cite section, page, paragraph or sentence identifiers only when the document supports them. Do not invent source locations.

## 7. Corpus tracking

For each paper in a corpus, track:

- rank and DOI;
- direct match, adjacent field, or methods;
- journal tier and the JCR edition, category and quartile, or unverified;
- the sections assessed and the evidence_scope;
- the six dimension scores, the grade and the status (`preliminary` or `final`), or not assessable;
- first-author and corresponding-author roles, single-paper labels and the cross-paper profile, with their limitations;
- learning status and stage-exam scores.

Author nationality and native language are not criteria and are not recorded.
