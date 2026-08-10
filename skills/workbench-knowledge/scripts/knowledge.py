#!/usr/bin/env python3
"""Read and append the workbench's durable knowledge, safely.

    from knowledge import read_all, add_entry, add_gap, add_lesson
    print(read_all())                       # everything, for context
    add_entry("LUOV descent reduces to the subfield.", kind="mechanism",
              evidence=[{"kind": "paper", "ref": "2019/1490", "note": "..."}],
              tags="luov descent")
    add_entry("Candidate C2 establishes ...", kind="derived result",
              evidence=[
                  {"kind": "derivation", "ref": "discovery.md#C2",
                   "note": "Original argument and assumptions."},
                  {"kind": "independent-check", "ref": "verifier-C2.md",
                   "note": "Fresh proof audit checked the exact candidate."},
              ])

Self-test (also the concurrency regression):

    python3 knowledge.py --selftest

WHY THIS FILE EXISTS RATHER THAN "just append to the file"
----------------------------------------------------------
Appending looks trivial and has one non-obvious way to lose data. The obvious
implementation -- read the file, add your text, write it back -- is what
`edit_file` does under the hood (exact-match replacement), and it silently
drops entries when two agents write near-simultaneously. Measured on this
machine, 8 concurrent writers x 150 records:

    open(path, "a") + one write()   kept 1200 / 1200
    read -> append -> write back    kept    7 / 1200   (1193 lost)

POSIX sets the file offset to end-of-file atomically with an O_APPEND write, so
appends from separate processes cannot interleave or clobber. This module only
ever appends, in one `write()` call, and refuses to rewrite these files.

The workbench runs delegated subagents that inherit the same host grant, so
concurrent writers are the normal case, not a corner case.
"""

from __future__ import annotations

import os
import re
import sys
import time

BASE = os.environ.get("CRYPTO_FILES") or os.path.expanduser(
    "~/crypto-workbench-files")

KNOWLEDGE = os.path.join(BASE, "knowledge.md")
GAPS = os.path.join(BASE, "gaps.md")
LESSONS = os.path.join(BASE, "lessons.md")

# One write() at or below the pipe-buffer size is the atomicity guarantee we
# rely on. Records are short by design; a record approaching this is a record
# that should have been two.
MAX_BLOCK = 4096


class GrantMissing(RuntimeError):
    """The host path is not writable from here.

    Raised loudly and never swallowed. The grant on the shared folder is
    per-project: a session in a different project holds no grant and its first
    write fails. Silently skipping would mean the lesson is simply lost, which
    is worse than an error -- the whole point of writing it down is that the
    next session gets it.
    """


def _append(path: str, block: str) -> str:
    if len(block.encode("utf-8")) > MAX_BLOCK:
        raise ValueError(
            "record is %d bytes, over the %d-byte atomic-append limit. Split "
            "it into two records rather than raising the limit -- a partial "
            "interleaved write is unrecoverable."
            % (len(block.encode("utf-8")), MAX_BLOCK))
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(block)          # single write, O_APPEND: atomic
    except OSError as exc:
        raise GrantMissing(
            "cannot append to %s (%s: %s).\n"
            "This is almost certainly the host-path grant: it is per-project, "
            "and this session may not hold read/write on %s. Ask the human to "
            "grant it rather than continuing -- an unrecorded lesson is lost, "
            "not deferred." % (path, type(exc).__name__, exc, BASE)) from exc
    return path


def _read(path: str) -> str:
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except FileNotFoundError:
        return ""


def _next_id(path: str, prefix: str) -> str:
    """Next id, e.g. K25-3f2a. Unique BY CONSTRUCTION, with no coordination.

    The old version returned a bare `K<max+1>`, and its docstring argued the
    resulting collisions were cosmetic. They were not. Measured 2026-08-05 on
    this workbench: EIGHT duplicate ids -- K35 through K41, and K85 -- produced
    by the parallel delegated tracks of one investigation. Entries cross-refer
    by id ("CORRECTION to K28", "Consequence of K27"), so a duplicate does not
    merely look untidy, it makes a reference ambiguous and silently points a
    reader at the wrong record.

    The old docstring was right about the fix it rejected: locking would end the
    atomic append, and the append is the property worth protecting (measured, 8
    concurrent writers: O_APPEND kept 1200/1200, read-modify-write kept 7).

    So do neither. Make the id unique WITHOUT coordination:

        <prefix><sequence>-<16 bits from os.urandom>

    The sequence is still best-effort max+1, because it is what makes the file
    readable and roughly chronological. The suffix is drawn from the OS, so two
    writers computing the same sequence at the same instant still get different
    ids. One write, still atomic, still no lock.

    Bare historical ids keep working: the scan below matches `K85` and
    `K85-3f2a` alike, and a cross-reference to `K28` still resolves whenever
    only one K28 exists.
    """
    nums = [int(m) for m in re.findall(r"(?m)^## %s(\d+)\b" % prefix,
                                       _read(path))]
    return "%s%d-%s" % (prefix, max(nums, default=0) + 1, os.urandom(2).hex())


def prune(ids, path: str = None, dry_run: bool = True) -> dict:
    """Remove entries by id. MAINTENANCE ONLY -- never call this from a session.

    This is the read-modify-write the rest of this module exists to avoid, and it
    cannot be made atomic: anything appended between the read and the rename is
    lost. Measured, 8 concurrent writers: append kept 1200/1200, read-modify-write
    kept 7.

    So it does the next best thing -- it makes the loss DETECTABLE and refuses
    rather than risking it. The file's size and mtime are captured before the
    read and re-checked immediately before the replace; any change at all aborts
    with nothing written. A backup is taken first regardless.

    Run it when nothing else is writing. If it aborts, that is it working.
    """
    path = path or KNOWLEDGE
    want = set(ids)
    before_stat = os.stat(path)
    body = _read(path)

    kept, removed = [], []
    for blk in re.split(r"\n(?=## )", body):
        m = re.match(r"## (\S+)", blk)
        if m and m.group(1) in want:
            removed.append(m.group(1))
        else:
            kept.append(blk)

    missing = sorted(want - set(removed))
    result = {"removed": sorted(removed), "missing": missing,
              "kept_entries": sum(1 for b in kept if b.startswith("## K"))}
    if dry_run or not removed:
        result["dry_run"] = True
        return result

    backup = "%s.bak-%s" % (path, time.strftime("%Y%m%d-%H%M%S"))
    with open(backup, "w", encoding="utf-8") as fh:
        fh.write(body)

    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write("\n".join(kept))

    now = os.stat(path)
    if (now.st_size, now.st_mtime_ns) != (before_stat.st_size,
                                          before_stat.st_mtime_ns):
        os.unlink(tmp)
        raise RuntimeError(
            "ABORTED: %s changed while pruning (size %d->%d). Something is "
            "writing to it. Nothing was modified; backup at %s. Retry when the "
            "file is idle." % (path, before_stat.st_size, now.st_size, backup))

    os.replace(tmp, path)
    result["backup"] = backup
    return result


def duplicates(path: str = None, prefix: str = "K") -> list:
    """Ids appearing more than once. Read-only -- reports, never repairs.

    Repair would mean rewriting the file, which is exactly the read-modify-write
    that loses concurrent records. If you must renumber, do it as a deliberate
    maintenance step with nothing else running, not from inside a session.
    """
    path = path or KNOWLEDGE
    seen, dup = {}, []
    for m in re.findall(r"(?m)^## (%s\d+(?:-[0-9a-f]+)?)\b" % prefix, _read(path)):
        seen[m] = seen.get(m, 0) + 1
    return sorted(k for k, n in seen.items() if n > 1)


def _stamp() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S")


def read_knowledge() -> str:
    return _read(KNOWLEDGE)


def read_gaps() -> str:
    return _read(GAPS)


def read_lessons() -> str:
    return _read(LESSONS)


def read_all() -> str:
    """Everything, for the start of a session. Cheap -- these are small."""
    parts = []
    for label, text in (("KNOWLEDGE", read_knowledge()),
                        ("GAPS", read_gaps()),
                        ("LESSONS", read_lessons())):
        if text.strip():
            parts.append("===== %s =====\n%s" % (label, text))
    return "\n\n".join(parts) or "(no knowledge recorded yet)"


def add_entry(statement, kind="entry", evidence=None, tags="",
              source="", claim=""):
    """Append a knowledge entry. Returns its id.

    `evidence` is a list of {kind, ref, note}. `kind` is the field that decides
    whether something is established: assertion / derivation /
    independent-check / computation / paper / spec / human. **`assertion` is
    not a source.** An entry whose only evidence is an assertion records what
    someone believed, not what is known.

    `derivation` records the original reasoning and is candidate provenance,
    not durable support by itself. Promoting a newly derived result requires a
    separate `independent-check` item naming an independent re-derivation, proof
    audit, computation, or human review. This helper enforces that promotion
    gate while leaving historical and custom evidence kinds readable.
    """
    evidence_kinds = {
        e.get("kind")
        for e in (evidence or [])
        if isinstance(e, dict)
    }
    if ("derivation" in evidence_kinds
            and "independent-check" not in evidence_kinds):
        raise ValueError(
            "derivation evidence is candidate provenance, not durable "
            "knowledge; keep it in the live plan and discovery artifact until "
            "an independent-check exists"
        )

    eid = _next_id(KNOWLEDGE, "K")
    L = ["## %s — %s" % (eid, kind), "", statement.strip(), ""]
    if evidence:
        L.append("- **evidence:**")
        for e in evidence:
            if isinstance(e, dict):
                ref = (" `%s`" % e["ref"]) if e.get("ref") else ""
                L.append("  - `%s`%s — %s" % (e.get("kind", "?"), ref,
                                              str(e.get("note", "")).strip()))
            else:
                L.append("  - %s" % e)
    if tags:
        L.append("- **tags:** %s" % tags)
    if source:
        L.append("- **from:** %s" % source)
    if claim:
        L.append("- **claim:** %s" % claim)
    L.append("- **added:** %s" % _stamp())
    L.append("")
    _append(KNOWLEDGE, "\n".join(L) + "\n")
    return eid


def add_gap(question, looked_in, finding="", tags="", source=""):
    """Append a gap — something looked for and not found. Returns its id.

    `looked_in` is a **channel list**, not a sentence. "searched ePrint" and
    "searched ePrint, NIST, breaks and the web" are different findings, and
    only the second licenses a negative claim.
    """
    if isinstance(looked_in, (list, tuple)):
        looked_in = ", ".join(str(x) for x in looked_in)
    gid = _next_id(GAPS, "G")
    L = ["## %s" % gid, "", question.strip(), "",
         "- **looked in:** %s" % looked_in]
    if finding:
        L.append("- **finding:** %s" % finding)
    if tags:
        L.append("- **tags:** %s" % tags)
    if source:
        L.append("- **from:** %s" % source)
    L.append("- **at:** %s" % _stamp())
    L.append("")
    _append(GAPS, "\n".join(L) + "\n")
    return gid


def add_lesson(text, tags=""):
    """Append a durable cross-session lesson — one line, dated.

    For things a future session would otherwise rediscover the hard way: a
    gotcha, a convention, a correction. Not for findings about cryptography --
    those are `add_entry`.
    """
    line = "- %s — %s%s\n" % (_stamp(), text.strip().replace("\n", " "),
                              ("  *(%s)*" % tags) if tags else "")
    _append(LESSONS, line)
    return line.strip()


def _selftest():
    """Regress atomic append and preservation of derivation provenance."""
    import subprocess
    import tempfile
    global KNOWLEDGE
    tmp = tempfile.mkdtemp()
    child = os.path.join(tmp, "w.py")
    with open(child, "w") as fh:
        fh.write("import sys\n"
                 "p, w, n = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])\n"
                 "for i in range(n):\n"
                 "    open(p, 'a').write('- w%02d e%03d\\n' % (w, i))\n")
    target = os.path.join(tmp, "log.md")
    procs = [subprocess.Popen([sys.executable, child, target, str(w), "150"])
             for w in range(8)]
    for p in procs:
        p.wait()
    kept = len([l for l in open(target).read().splitlines() if l.strip()])
    ok = kept == 1200
    print("  concurrent append: kept %d/1200 -> %s"
          % (kept, "PASS" if ok else "FAIL"))

    original_knowledge = KNOWLEDGE
    try:
        KNOWLEDGE = os.path.join(tmp, "knowledge.md")
        try:
            add_entry(
                "Unchecked candidate.",
                kind="derived result",
                evidence=[
                    {"kind": "derivation", "ref": "discovery.md#C1",
                     "note": "Original reasoning only."},
                ],
            )
            gate_ok = False
        except ValueError:
            gate_ok = not os.path.exists(KNOWLEDGE)

        add_entry(
            "Candidate C2 establishes a toy consequence.",
            kind="derived result",
            evidence=[
                {"kind": "derivation", "ref": "discovery.md#C2",
                 "note": "Original reasoning."},
                {"kind": "independent-check", "ref": "verifier-C2.md",
                 "note": "Fresh computation checked C2."},
            ],
        )
        recorded = _read(KNOWLEDGE)
        provenance_ok = (
            "`derivation` `discovery.md#C2`" in recorded
            and "`independent-check` `verifier-C2.md`" in recorded
        )
    finally:
        KNOWLEDGE = original_knowledge
    print("  derivation provenance: %s"
          % ("PASS" if provenance_ok else "FAIL"))
    print("  derivation-only gate: %s"
          % ("PASS" if gate_ok else "FAIL"))
    print("  base path        : %s (exists=%s, writable=%s)"
          % (BASE, os.path.isdir(BASE), os.access(BASE, os.W_OK)))
    return 0 if ok and provenance_ok and gate_ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(_selftest())
    if "--prune" in sys.argv:
        i = sys.argv.index("--prune")
        ids = [a for a in sys.argv[i + 1:] if not a.startswith("-")]
        if not ids:
            sys.exit("usage: knowledge.py --prune K25 K26 ... [--apply]")
        dup = set(ids) & set(duplicates())
        if dup:
            sys.exit("REFUSING: %s appear more than once, so pruning by id would "
                     "remove records you did not name. Resolve by hand."
                     % ", ".join(sorted(dup)))
        r = prune(ids, dry_run="--apply" not in sys.argv)
        for k_, v in r.items():
            print("  %-14s %s" % (k_, v))
        if r.get("dry_run"):
            print("\n  DRY RUN. Add --apply to write. Run it when no session is "
                  "appending; it aborts rather than risk losing a concurrent write.")
        sys.exit(0)
    if "--fsck" in sys.argv:
        bad = duplicates()
        if bad:
            print("DUPLICATE ids in %s: %s" % (KNOWLEDGE, ", ".join(bad)))
            print("Cross-references to these are ambiguous. New ids carry a "
                  "random suffix and cannot collide; these predate that.")
        else:
            print("no duplicate ids in %s" % KNOWLEDGE)
        sys.exit(1 if bad else 0)
    print(read_all()[:4000])
