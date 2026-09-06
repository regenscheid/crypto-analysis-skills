#!/usr/bin/env python3
"""Smoke-check response format; optionally check normalized skill-load evidence."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from trace_evidence import successful_skill_loads


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
        help="offline normalized JSON load events (tests/evaluation-contract.md)",
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
    grounding = section(response, "grounding")
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

    if case.get("requires_grounding"):
        grounding_statuses = ("DISCOVERED", "READ", "PROVIDED", "BLOCKED")
        if grounding and any(status in grounding.upper() for status in grounding_statuses):
            passes.append("grounding:recognized status token present")
        else:
            failures.append("grounding: missing source-grounding section or evidence status")

    if coverage and any(
        status in coverage.upper()
        for status in ("EXAMINED", "CANDIDATE", "FALSIFIED", "NOT_APPLICABLE", "BLOCKED", "DEFERRED", "INCONCLUSIVE")
    ):
        passes.append("coverage:recognized status token present")
    else:
        failures.append("coverage: missing ledger or recognized status")

    if expected_mode == "DISCOVER":
        if "candidate" in folded and ("falsif" in folded or "decisive test" in folded):
            passes.append("discover:candidate and falsification vocabulary present")
        else:
            failures.append("discover: candidates or falsification not addressed")
        if "unchecked" in folded or "blocked" in folded or "deferred" in folded:
            passes.append("discover:limit vocabulary present")
        else:
            failures.append("discover: unchecked or blocked work not visible")

    format_passed = not failures
    trace_status = "not_supplied"
    if args.trace:
        try:
            loaded = successful_skill_loads(args.trace)
            missing_calls = sorted(set(case["expected_skills"]) - loaded)
            if missing_calls:
                failures.append("runtime-trace: no successful load event for " + ", ".join(missing_calls))
                trace_status = "missing_load_events"
            else:
                passes.append("runtime-trace:successful load events recorded")
                trace_status = "recorded_load_events_present"
        except ValueError as exc:
            failures.append(f"runtime-trace: {exc}")
            trace_status = "invalid"

    result = {
        "case_id": case["id"],
        "passed": not failures,
        "checks_passed": passes,
        "failures": failures,
        "trace_checked": bool(args.trace),
        "format_passed": format_passed,
        "trace_evidence": trace_status,
        "evaluation_scope": "report_format_and_optional_recorded_load_events",
        "research_progress": "not_assessed",
        "scientific_correctness": "not_assessed",
    }
    print(json.dumps(result, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
