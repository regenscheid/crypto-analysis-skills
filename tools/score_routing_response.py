#!/usr/bin/env python3
"""Score a captured model response against a cryptanalysis routing case."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
HEADING_PATTERN = re.compile(r"(?m)^#{1,6}\s+(.+?)\s*$")


def section(text: str, heading: str) -> str:
    matches = list(HEADING_PATTERN.finditer(text))
    for index, match in enumerate(matches):
        if heading.casefold() in match.group(1).casefold():
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            return text[match.end() : end]
    return ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("case_id")
    parser.add_argument("response", type=Path)
    parser.add_argument(
        "--trace",
        type=Path,
        help="optional raw runtime trace used to confirm skill calls",
    )
    parser.add_argument(
        "--cases",
        type=Path,
        default=REPOSITORY_ROOT / "tests" / "routing-cases.json",
    )
    args = parser.parse_args()

    cases = json.loads(args.cases.read_text(encoding="utf-8"))["cases"]
    try:
        case = next(item for item in cases if item["id"] == args.case_id)
    except StopIteration:
        print(f"unknown routing case: {args.case_id}", file=sys.stderr)
        return 2

    response = args.response.read_text(encoding="utf-8", errors="replace")
    folded = response.casefold()
    skill_trace = section(response, "skill trace")
    coverage = section(response, "coverage")
    failures: list[str] = []
    passes: list[str] = []

    expected_mode = case["expected_mode"]
    if expected_mode.casefold() in folded:
        passes.append(f"mode:{expected_mode}")
    else:
        failures.append(f"mode: expected {expected_mode}")

    if skill_trace:
        passes.append("skill-trace:present")
    else:
        failures.append("skill-trace: missing Skill trace section")

    missing_skills = [
        name for name in case["expected_skills"] if name.casefold() not in skill_trace.casefold()
    ]
    if missing_skills:
        failures.append("skill-trace: missing " + ", ".join(missing_skills))
    else:
        passes.append("skill-trace:expected skills named")

    if coverage and any(
        status in coverage.upper()
        for status in ("EXAMINED", "CANDIDATE", "FALSIFIED", "NOT_APPLICABLE", "BLOCKED", "DEFERRED", "INCONCLUSIVE")
    ):
        passes.append("coverage:status ledger present")
    else:
        failures.append("coverage: missing ledger or recognized status")

    if expected_mode == "DISCOVER":
        if "candidate" in folded and ("falsif" in folded or "decisive test" in folded):
            passes.append("discover:candidates and falsification addressed")
        else:
            failures.append("discover: candidates or falsification not addressed")
        if "unchecked" in folded or "blocked" in folded or "deferred" in folded:
            passes.append("discover:limits visible")
        else:
            failures.append("discover: unchecked or blocked work not visible")

    if args.trace:
        trace = args.trace.read_text(encoding="utf-8", errors="replace").casefold()
        missing_calls = [
            name for name in case["expected_skills"] if name.casefold() not in trace
        ]
        if missing_calls:
            failures.append("runtime-trace: missing " + ", ".join(missing_calls))
        else:
            passes.append("runtime-trace:expected skills named")

    result = {
        "case_id": case["id"],
        "passed": not failures,
        "checks_passed": passes,
        "failures": failures,
        "trace_checked": bool(args.trace),
    }
    print(json.dumps(result, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
