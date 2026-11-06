#!/usr/bin/env python3
"""Build a reproducible Agent Skill archive from the repository root."""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "scientific-literature-english-tutor"
CORE_FILES = ["SKILL.md", "README.md", "CHANGELOG.md", "LICENSE"]


def source_files() -> list[Path]:
    paths = [ROOT / name for name in CORE_FILES]
    paths.extend(sorted((ROOT / "references").glob("*.md")))
    missing = [str(p.relative_to(ROOT)) for p in paths if not p.is_file()]
    if missing:
        raise FileNotFoundError(f"Missing Skill files: {missing}")
    return paths


def archive_name(path: Path) -> str:
    return f"{SKILL_NAME}/{path.relative_to(ROOT).as_posix()}"


def verify_archive(path: Path) -> tuple[int, str]:
    expected = {archive_name(p) for p in source_files()}
    with zipfile.ZipFile(path, "r") as zf:
        bad = zf.testzip()
        if bad:
            raise ValueError(f"Corrupt ZIP member: {bad}")
        actual = set(zf.namelist())
        if actual != expected:
            raise ValueError(
                f"Archive member mismatch. Missing={sorted(expected-actual)}; "
                f"extra={sorted(actual-expected)}"
            )
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return len(expected), digest


def build(path: Path) -> tuple[int, str]:
    path.parent.mkdir(parents=True, exist_ok=True)
    files = source_files()
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for src in files:
            info = zipfile.ZipInfo(archive_name(src), date_time=(2026, 11, 6, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            zf.writestr(info, src.read_bytes())
    return verify_archive(path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=f"dist/{SKILL_NAME}.skill")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    count, digest = build(output)
    print(f"Built: {output}")
    print(f"Files: {count}")
    print(f"SHA-256: {digest}")
    if args.verify:
        verified_count, verified_digest = verify_archive(output)
        print(f"Verified: {verified_count} files; SHA-256 {verified_digest}")


if __name__ == "__main__":
    main()
