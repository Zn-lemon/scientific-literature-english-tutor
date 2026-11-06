# Sentence analysis: source, locators, depth tiers and templates

Scope: verbatim quoting and formatting notes, sentence locators, the depth tiers `full` / `standard` / `light`, the sentence template, the paragraph template and the section summary.
Not here: the round loop, round size, length target and content labels (SKILL.md, Round loop and Content labels); practice items, practice load and error codes (references/training-mechanisms.md); checkpoints, `source_version` and learner records (references/progress-and-assessment.md); stage exams (references/exam-and-assessment.md).

## 1. Verbatim source and formatting

### 1.1 Source and scope

- Teach from the document the learner supplied. If there is none, ask the learner to upload or paste the paper. Do not teach from memory or from search snippets.
- Start where the learner asks; otherwise follow SKILL.md, Start instruction.
- Default scope: the main text in its original order. Leave out author lists, affiliations, disclaimers and references unless the learner asks for them. Figure legends are optional extra lessons (`FIG` locators, §2).
- Teach a long paper in rounds. Never translate or analyze the whole paper in one response.
- Note which version of the text is being read (`source_version`, references/progress-and-assessment.md §1). The version decides whether page numbers and formatting can be checked.
- Quote only the sentence being analyzed. For papers found by search, the copyright limits in references/literature-discovery.md §9 also apply.

### 1.2 Quoting rules

1. Quote the sentence exactly under 【原文 Source】: the same words, spelling, symbols, numbers, units and punctuation as the source version.
2. The source version is the document itself (the printed PDF page, or the text content of the JATS or HTML markup), not the raw output of an extraction tool. Where the two differ (OCR errors, line-end hyphens, spacing left by stripped tags, garbled equations or table text), check the page image or the markup and quote what the document says. If it cannot be checked, quote the extracted text, mark the doubtful span and say why. Never fill a gap by guessing.
3. Formatting that plain text cannot carry (italics, bold, superscripts, subscripts, small capitals) is described in a note directly under the quote, for example "The published version italicizes *X* and *Y*." Do not add it silently inside the quote, and do not drop it without a note. If the source version is `plain-text`, say that formatting could not be checked.
4. Inconsistencies in the author's own text (a name written two ways, a value that differs between the main text and a legend) are quoted as published and noted as the author's own inconsistency, not a transcription error. Do not correct them. Use them as a writing lesson; do not judge the experiment.
5. A convention that explains such a note (for example, why gene symbols are italic) is general knowledge, not something the paper states: label it 【背景知识·非原文 Background】.

## 2. Sentence locators

Every quote, practice item, error-log entry and checkpoint names its sentence with a locator `<SEC>-P<n>-S<m>`.

| SEC | Section |
|---|---|
| `ABS` | Abstract |
| `INT` | Introduction |
| `MET` | Methods |
| `RES` | Results; a combined "Results and Discussion" section is also `RES` |
| `DIS` | Discussion |
| `CON` | Conclusions |
| `FIG` | Figure legends, numbered by figure with no paragraph number: `FIG3-S2` is sentence 2 of the Figure 3 legend |
| `SUP` | Supplementary material |

Examples: `ABS-P1-S2`, `INT-P2-S3`, `RES-P7-S1 (Ethylene response)`, `DIS-P1-S2 p.9`.

- Paragraphs are numbered continuously within each top-level section, across its subsections. A subsection title may be added in parentheses after the locator.
- Sentences are numbered from 1 within each paragraph. A sentence ends at terminal punctuation that closes a grammatical sentence; the full stops in abbreviations, initials, species names and decimal numbers do not end a sentence.
- Add a page number (` p.4`) only when `source_version` is `pdf`. JATS XML, HTML and plain text have no pages: the paragraph and sentence numbers are the locator. Never invent a page number.
- A heading outside the list above takes the code of its function (for example, "Background" is `INT` and "Experimental procedures" is `MET`). State the mapping once, in the first checkpoint.
- If a paragraph or sentence boundary is unclear, check the page image or markup. If it stays unclear, give the locator and say it is uncertain. Do not invent source locations.
- A few opening words of the sentence may follow the locator as a check. They never replace it.

## 3. Depth tiers

Each sentence is taught at one of three depth tiers. The tiers help keep each round within the length target in SKILL.md, Round loop. They are internal teaching rules, not a validated difficulty measure.

| Tier | Typical signals |
|---|---|
| `full` | Several signals at once: a long sentence whose main clause is hard to find because of embedded or nested clauses, dense nominalization, or long parenthetical insertions |
| `standard` | The default: moderate length and one subordinate or non-finite structure; the main clause is easy to find |
| `light` | A short sentence with one clause, few nominalizations and no insertion |

1. Judge the tier from four signals: sentence length, clause nesting, nominalization density, and parenthetical insertions. Length alone does not make a sentence `full`.
2. When the signals are mixed, use `standard`.
3. The learner can change the tier. 详细 / Full detail re-teaches the current sentence at `full`; 精简 / Brief re-teaches it at `light`. The choice is saved as the depth preference in the checkpoint and applies to later sentences until the learner changes it or asks to return to tiering by signals.
4. The tier changes how much is explained, never fidelity: the quote stays exact, and the translation always keeps qualifiers, tense, scope and certainty.
5. Show the tier in each sentence heading so the learner knows what to ask for.

## 4. Sentence template

The template has nine parts. `full` teaches all nine; `standard` and `light` keep only the parts marked below.

| Part | `full` | `standard` | `light` |
|---|---|---|---|
| 1. Original sentence | yes | yes | yes |
| 2. Translation | yes | yes | yes |
| 3. Sentence structure | yes | yes | no |
| 4. Academic vocabulary | yes | yes, merged with part 5 in one short table | no |
| 5. Collocations and natural expressions | yes | merged with part 4 | no |
| 6. Author's writing choices | yes | one point only | no |
| 7. Transferable pattern | yes | yes | optional |
| 8. Likely learner pitfalls | yes | no | no |
| 9. Takeaway | full list | one sentence | one point |

### 4.1 Guidance for each part

1. **Original sentence.** The exact quote with its locator and any formatting note (§1.2).
2. **Translation.** Accurate and natural, in the explanation language from the learner profile (default Chinese). Keep qualifiers, tense, scope and logical relations. Do not add detail the author left general.
3. **Sentence structure.** A short table of the main units (subject, verb, object or complement, modifiers, clauses and non-finite phrases) and their functions. Then explain the clause relations, non-finite forms, parallel structures, appositives and insertions, and how the syntax orders the information. Do not force labels that do not apply.
4. **Academic vocabulary.** Content words worth learning, with part of speech, meaning in this sentence, academic collocations, and the near-synonym difference that matters here. Skip basic function words.
5. **Collocations and natural expressions.** For each expression: meaning in context, grammatical pattern, typical academic use, an alternative and how it differs.
6. **Author's writing choices.** Why this word or construction fits; the sentence's rhetorical role (background, method, result, comparison, interpretation, inference, qualification or conclusion); how it signals evidence strength; how it links to the surrounding argument. Write this as textual analysis, not as knowledge of the author's private intention.
7. **Transferable pattern.** The abstract structure, a reusable template with X / Y / Z placeholders, and one new example labeled 【教学示例·非原文 Teaching example】. The example uses a different scenario from the round's practice items, so it does not give away an answer, and it never presents invented data as the paper's.
8. **Likely learner pitfalls.** Only the errors this sentence invites, tagged with the error codes in references/training-mechanisms.md §4: for example, word order carried over from the learner's first language, a wrong preposition or verb pattern, number agreement across an inserted clause, overstated evidence, or a result confused with its interpretation.
9. **Takeaway.** `full`: three words, two collocations, one sentence pattern and one writing lesson. `standard`: one sentence. `light`: the single most useful point.

General knowledge the sentence does not state is labeled 【背景知识·非原文 Background】; information found by search in this session is labeled 【外部资料 External】 with its source. Neither is presented as a claim of the paper.

### 4.2 Output skeleton

Drop the parts the tier leaves out and keep the order.

```text
### Sentence <locator> (<tier>)

【原文 Source】
> <exact sentence>
<formatting or inconsistency note, if any>

【讲解 Explanation】
Translation: ...
Structure: <table of units and functions>, then a short explanation
Vocabulary and collocations: <table>
Writing choices: ...
Pattern: <abstract structure>; template: <with X / Y / Z>
【教学示例·非原文 Teaching example】 <new sentence>
Pitfalls: <error code> ...
Takeaway: ...
```

## 5. Paragraph template

When the last sentence of a paragraph has been taught, add a paragraph analysis in that round, after the sentence lessons and before the practice items. Heading: `### Paragraph <SEC>-P<n>`.

1. **Central point:** what the paragraph establishes.
2. **Sentence roles:** the function of each sentence, by locator.
3. **Logical links:** contrast, addition, cause, evidence, qualification, interpretation or transition, and the words that signal them.
4. **Evidence and inference:** how evidence, comparison, interpretation and inference are organized.
5. **Argument structure:** the sequence the author actually uses. Do not force every paragraph into one structure such as background → question → evidence → finding → interpretation.
6. **Reusable language:** the most useful expressions and sentence patterns, with locators.

If a paragraph spans several rounds, earlier rounds may add a one-line note on how their sentences connect; the full analysis waits for the last sentence. The next sentence to study is recorded in the checkpoint (references/progress-and-assessment.md §1).

## 6. Section summary

At the end of each subsection (or of a section without subsections), give a short summary. It is not scored.

1. The scientific question and main claims.
2. The types of evidence used.
3. The order of the argument.
4. Five useful expressions, with locators.
5. Three useful sentence patterns.
6. The section's most important writing lesson.
7. A short integrated check covering the subsection: vocabulary and collocation choice, translation of a sentence from the learner's first language into English, Chinglish revision and imitation, plus the paragraph task (references/training-mechanisms.md §3.2). When the subsection also ends a stage, the stage exam's writing task replaces the paragraph task (references/exam-and-assessment.md §1).

The summary itself carries no score; the paragraph task still gets writing feedback (references/training-mechanisms.md §5). Keep interpretation grounded in the paper, and do not present the authors' hypotheses as established facts. The handoffs at the end of a section, stage or paper are in SKILL.md, Round loop.
