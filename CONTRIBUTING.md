# Contributing

Thank you for helping improve Scientific Literature English Tutor.

## Scope

Contributions are welcome for:
- teaching clarity and source-faithful analysis;
- exercise quality and learner-facing examples;
- documentation, accessibility and compatibility notes;
- reproducible tests for the public Skill.

The public repository contains the baseline learning Skill. Do not submit private datasets,
commercial backend code, user-feedback records, API credentials or confidential research material.

## Before opening a pull request

1. Explain the learner problem the change addresses.
2. Keep source-derived content distinct from teaching examples and external information.
3. Do not introduce unsupported scientific claims or author-attribution claims.
4. Run the tests:

   ```bash
   python -m unittest discover -s tests -v
   python tools/package_skill.py --output dist/scientific-literature-english-tutor.skill --verify
   ```

5. Update `CHANGELOG.md` when behavior changes.

Changes to the six-dimension writing rubric must update `rubric_version` in
`references/writing-quality-scorecard.md` and explain score comparability in the changelog.
Do not silently change thresholds or historical scoring semantics.
