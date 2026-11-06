from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SkillPackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        cls.readme = (ROOT / "README.md").read_text(encoding="utf-8")
        cls.changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        cls.literature = (ROOT / "references/literature-discovery.md").read_text(encoding="utf-8")
        cls.scorecard = (ROOT / "references/writing-quality-scorecard.md").read_text(encoding="utf-8")

    def test_frontmatter_name_and_version(self):
        match = re.match(r"\A---\s*\n(.*?)\n---", self.skill, re.S)
        self.assertIsNotNone(match, "SKILL.md must start with YAML frontmatter")
        fm = match.group(1)
        self.assertRegex(fm, r"(?m)^name:\s*scientific-literature-english-tutor\s*$")
        self.assertRegex(fm, r"(?m)^license:\s*MIT\s*$")
        self.assertRegex(fm, r"(?m)^metadata:\s*\n(?:[ \t].*\n)*?[ \t]+version:\s*[\"']?2\.0\.0")
        self.assertNotRegex(fm, r"(?m)^version:")

    def test_required_files_exist(self):
        for name in ["README.md", "CHANGELOG.md", "LICENSE", "SKILL.md"]:
            self.assertTrue((ROOT / name).is_file(), name)
        expected_refs = {
            "exam-and-assessment.md", "literature-discovery.md",
            "progress-and-assessment.md", "sentence-analysis.md",
            "training-mechanisms.md", "writing-quality-scorecard.md",
        }
        actual_refs = {p.name for p in (ROOT / "references").glob("*.md")}
        self.assertEqual(actual_refs, expected_refs)

    def test_internal_reference_paths_exist(self):
        corpus = "\n".join(
            p.read_text(encoding="utf-8")
            for p in [ROOT / "SKILL.md", *sorted((ROOT / "references").glob("*.md"))]
        )
        referenced = set(re.findall(r"references/([A-Za-z0-9_-]+\.md)", corpus))
        for name in referenced:
            self.assertTrue((ROOT / "references" / name).is_file(), name)

    def test_markdown_relative_links_resolve(self):
        for source in [ROOT / "README.md", ROOT / "CHANGELOG.md",
                       ROOT / "SKILL.md", *sorted((ROOT / "references").glob("*.md"))]:
            text = source.read_text(encoding="utf-8")
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
                target = target.split("#", 1)[0]
                if not target or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                    continue
                self.assertTrue((source.parent / target).resolve().exists(),
                                f"{source.relative_to(ROOT)} -> {target}")

    def test_readme_and_changelog_version(self):
        self.assertIn("Current version: `2.0.0`", self.readme)
        self.assertIn("## 2.0.0 — 2026-11-06", self.changelog)

    def test_rubric_dimensions_and_total(self):
        dimensions = [
            "Academic vocabulary precision", "Syntax and sentence control",
            "Paragraph logic and argumentation", "Natural academic expression",
            "Scientific reasoning and claim calibration", "Clarity and concision",
        ]
        for dimension in dimensions:
            self.assertIn(dimension, self.scorecard)
        self.assertIn("100 points", self.scorecard)
        self.assertIn("rubric_version: 2.0.0", self.scorecard)

    def test_grade_gates_are_explicit(self):
        self.assertIn("**A:** total ≥ 85 and every dimension at least Good.", self.scorecard)
        self.assertIn("**B:** total ≥ 75 and no Weak dimension.", self.scorecard)
        self.assertIn("**C:** total below 75, or any Weak dimension.", self.scorecard)

    def test_partial_text_screening_and_scoring_align(self):
        self.assertIn("sufficiently substantial `partial_text`", self.literature)
        self.assertIn("partial_text", self.scorecard)
        self.assertIn("never `final`", self.scorecard)
        self.assertIn("too little main text is available", self.scorecard)

    def test_credentials_are_placeholders_only(self):
        corpus = "\n".join(
            p.read_text(encoding="utf-8")
            for p in [ROOT / "README.md", ROOT / "SKILL.md",
                      *sorted((ROOT / "references").glob("*.md"))]
        )
        self.assertNotRegex(corpus, r"\bsk-[A-Za-z0-9_-]{20,}\b")
        self.assertNotRegex(corpus, r"\bgh[pousr]_[A-Za-z0-9]{20,}\b")
        self.assertIn("<your-key>", corpus)
        self.assertIn("name@example.org", corpus)

    def test_no_author_nationality_as_evidence(self):
        self.assertIn("Do not use nationality", self.scorecard)
        self.assertIn("Native-speaker status is not a criterion", self.scorecard)

    def test_license_included_for_standalone_skill_distribution(self):
        self.assertIn("MIT License", (ROOT / "LICENSE").read_text(encoding="utf-8"))
        self.assertIn("license: MIT", self.skill)


if __name__ == "__main__":
    unittest.main()
