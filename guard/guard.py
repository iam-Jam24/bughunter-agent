"""Check a proposed bug fix against the stop rules before a PR is opened.

Usage: python guard.py <original_dir> <fixed_dir>
Prints JSON: {"verdict": "OK" | "STOP", "reasons": [...], "changed_files": [...]}
"""
import json
import re
import sys
from pathlib import Path

MAX_CHANGED_SOURCE_FILES = 2


def read_py_files(root):
    return {p.relative_to(root).as_posix(): p.read_text() for p in Path(root).rglob("*.py")}


def test_names(source):
    return set(re.findall(r"^def (test_\w+)", source, re.MULTILINE))


def is_test_file(path):
    return Path(path).name.startswith("test_")


def check(original, fixed):
    reasons = []

    changed_source = [f for f in fixed if not is_test_file(f) and original.get(f) != fixed[f]]
    if len(changed_source) > MAX_CHANGED_SOURCE_FILES:
        reasons.append(
            f"Fix changes {len(changed_source)} source files (limit {MAX_CHANGED_SOURCE_FILES}): {changed_source}"
        )

    for f, source in original.items():
        if not is_test_file(f):
            continue
        if f not in fixed:
            reasons.append(f"Existing test file deleted: {f}")
            continue
        removed = test_names(source) - test_names(fixed[f])
        if removed:
            reasons.append(f"Existing tests removed from {f}: {sorted(removed)}")
        if fixed[f].count("assert") < source.count("assert"):
            reasons.append(f"Fewer assertions in {f} than before")

    new_tests = sum(
        len(test_names(src) - test_names(original.get(f, "")))
        for f, src in fixed.items()
        if is_test_file(f)
    )
    if new_tests == 0:
        reasons.append("No new test was added to prove the bug")

    return ("STOP" if reasons else "OK"), reasons, changed_source


if __name__ == "__main__":
    verdict, reasons, changed = check(read_py_files(sys.argv[1]), read_py_files(sys.argv[2]))
    print(json.dumps({"verdict": verdict, "reasons": reasons, "changed_files": changed}, indent=2))
