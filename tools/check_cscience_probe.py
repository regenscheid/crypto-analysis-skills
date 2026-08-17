#!/usr/bin/env python3
"""Check a captured CScience skill-probe response and optional call trace."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("response", type=Path, help="file containing the raw model response")
    parser.add_argument(
        "--trace",
        type=Path,
        help="optional runtime trace that should contain a cscience-skill-probe call",
    )
    parser.add_argument(
        "--cases",
        type=Path,
        default=REPOSITORY_ROOT / "tests" / "cscience-skill-probe-cases.json",
    )
    args = parser.parse_args()

    expected = json.loads(args.cases.read_text(encoding="utf-8"))["expected"]
    raw_response = args.response.read_text(encoding="utf-8").strip()
    try:
        actual = json.loads(raw_response)
    except json.JSONDecodeError as error:
        print(f"FAIL adherence: response is not exact JSON ({error})", file=sys.stderr)
        return 1

    failures = []
    if actual != expected:
        failures.append("load/adherence: response does not match the body-only record")
    if args.trace:
        trace = args.trace.read_text(encoding="utf-8", errors="replace")
        if "cscience-skill-probe" not in trace:
            failures.append("discovery: runtime trace does not name cscience-skill-probe")

    if failures:
        for failure in failures:
            print(f"FAIL {failure}", file=sys.stderr)
        return 1

    if args.trace:
        print("PASS discovery, body loading, and adherence")
    else:
        print("PASS body loading and adherence; discovery trace not checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
