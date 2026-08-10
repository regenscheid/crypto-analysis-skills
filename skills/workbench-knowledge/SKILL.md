---
name: workbench-knowledge
description: Read and extend the crypto workbench's durable knowledge — what has been established and how, what was looked for and not found, and lessons worth carrying between sessions. Use at the start of any substantive work to check what is already known, and whenever an investigation settles something, fails to find something, or teaches a gotcha worth not rediscovering.
license: Apache-2.0
---

# Workbench knowledge

Three files, in a folder you can open. The location is **`CRYPTO_FILES`**,
defaulting to `~/crypto-workbench-files`. Set it to somewhere the running
session can write, and grant that path if the host sandboxes writes:

| | |
|---|---|
| `knowledge.md` | what has been established, and **how** |
| `gaps.md` | what was looked for and **not** found |
| `lessons.md` | gotchas and conventions worth carrying forward |

They used to be an MCP connector. They are files now because this is storage,
not search: 24 entries and 8 gaps do not need an index, and a connector needs an
app restart to pick up changes, hides its own failures from `tools/list`, and
cannot be opened by a person.

---

## Read it first

```python
import sys, os
# knowledge.py ships with the workbench-knowledge skill. Find it whether this
# repo is the CWD, the skills are published as flat siblings, or CRYPTO_SKILLS
# names the checkout. Set CRYPTO_SKILLS if none of these resolve.
for _p in (os.environ.get("CRYPTO_SKILLS", ""),
           "skills/workbench-knowledge/scripts",
           "../workbench-knowledge/scripts",
           os.path.expanduser("~/crypto-analysis-skills/skills/workbench-knowledge/scripts")):
    _c = os.path.join(_p, "scripts") if _p and _p.endswith("workbench-knowledge") else _p
    if _c and os.path.isfile(os.path.join(_c, "knowledge.py")):
        sys.path.insert(0, _c); break
from knowledge import read_all, add_entry, add_gap, add_lesson
print(read_all())
```

All three files at once, and they are small enough that reading everything is
the right move. **Do this before deriving anything.**

That instruction is load-bearing rather than polite. The measured failure of
this workbench has never been an inability to compute — it is re-deriving what
it already held. One pilot run spent 603 seconds on a parameter sweep to settle
a question the estimator has no model for, when a recorded gap said so; another
re-derived facts sitting unfetched in the corpus and recalled them wrongly
twice. **A file is only consulted if you consult it**, and nothing will prompt
you.

**A gap is an answer about that door.** It says what is known to be closed and
which channels were checked. In VALIDATE, if it covers the exact question, cite
it and stop — that is the system working, not a dead end. In DISCOVER, use it to
prune that candidate or search route and continue with structurally different
directions; it is not an answer to the whole discovery investigation.

---

## First: does this even belong here?

**These files do not ship.** They live outside the repo, on one machine, and
someone who clones this workbench gets none of them. So before writing, ask:

> **Would this still be true on someone else's machine?**

- **Yes — it is a property of the tool.** How the sandbox behaves, what a kernel
  can reach, how a connector fails, what a subagent cannot do. That belongs in
  the **repo**, where it ships: the relevant skill, or that skill's `reference/`.
  Environment-wide facts go in `investigate`'s `reference/environment.md`.
- **No — it is what *this* investigation found.** A cost, what a paper actually
  claims, a refuted attack, a parameter checked against its source. That is what
  these files are for.

This was got wrong at scale and is worth not repeating. About a dozen entries
here are Claude Science truths, not findings — that a connector cannot bind a
port, that `host.mcp()` discards binary, that a subagent has no route to a
human. Every one is true for anyone who clones this repo, and none of them
shipped. They were rediscovered instead, expensively, more than once.

The test is not about importance. A finding can matter enormously and still
belong here; an environment quirk can be trivial and still belong in the repo.
It is only ever: **does it stay true somewhere else?**

## Write it back

```python
add_entry(statement, kind="mechanism", evidence=[...], tags="luov descent",
          source="<investigation or session>", claim="C7")
add_gap(question, looked_in=["ePrint", "NIST", "breaks", "web"], finding="...")
add_lesson("Magma exits 0 on user errors; require a final done marker.")
```

**`evidence` decides whether something is knowledge.** Each item is
`{kind, ref, note}` with `kind` one of `assertion` / `derivation` /
`independent-check` / `computation` / `paper` / `spec` / `human`.
**`assertion` is not a source** — an entry whose only evidence is an assertion
records what someone believed, not what is known. Write the `note` so a reader
can check it without you: quote the line, name the command.

**`derivation` is candidate provenance, not durable support.** It records the
original argument, assumptions, and versioned artifact so another checker can
inspect the exact thing that was proposed. Do not add a derivation-only candidate
to `knowledge.md`; keep it in the live plan and its versioned discovery artifact.
`add_entry` rejects derivation evidence unless the same entry includes an
`independent-check`.

**`independent-check` is the promotion gate for a new derivation.** Its `ref` and
`note` name the separate route — independent re-derivation, proof audit,
computation, or human review — and the exact candidate checked. The checker may
refute or confirm the candidate but must not silently repair or improve it.
Reading the author's conclusion back to them is not an independent route. Once a
check succeeds, retain both evidence items so the durable entry shows where the
result came from and how it was independently tested:

```python
add_entry(
    "Candidate C2 establishes ... under assumptions A1-A4.",
    kind="derived result",
    evidence=[
        {"kind": "derivation", "ref": "<versioned discovery artifact>#C2",
         "note": "Original argument and notation map."},
        {"kind": "independent-check", "ref": "<verifier report>",
         "note": "Fresh computation checked the stated consequence."},
    ],
)
```

Ordinary facts established directly by a paper, specification, computation, or
human decision retain their existing evidence rules. The second-route gate is
specifically for promoting new theoretical work.

**`looked_in` is a channel list, not a sentence.** "searched ePrint" and
"searched ePrint, NIST, breaks and the web" are different findings, and only the
second licenses a negative claim.

**Record negatives as readily as positives.** A gap that costs one call to write
saves the next session your entire search. If negatives are expensive to record
they do not get recorded, and the search repeats.

**`add_lesson` is for process, not cryptography.** A gotcha, a convention, a
correction — the things a future session would otherwise learn the hard way.
Findings about schemes go to `add_entry`.

---

## The one rule about writing

**Append. Never rewrite.** Use the helpers; they do a single `write()` in append
mode, which POSIX makes atomic against other appenders.

Do **not** read-modify-write, and do **not** use `edit_file` — its exact-match
replacement *is* read-modify-write. Measured here, 8 concurrent writers × 150
records each:

| | kept |
|---|---|
| `open(path, "a")` + one `write()` | **1200 / 1200** |
| read → append → write back | 7 / 1200 |

That is not a corner case. Delegated subagents inherit the same host grant and
write to the same files, so simultaneous writers are the normal condition.

Records are capped at 4 KB and the helper refuses larger ones. A record
approaching the cap is a record that should have been two.

Regression test:

```
python3 skills/workbench-knowledge/scripts/knowledge.py --selftest
```

---

## If the write fails, say so loudly

The helper raises `GrantMissing` rather than returning quietly. **Do not catch
it and carry on.** The read/write grant on the folder is *per project*: a
session in a different project holds none, and its first write fails.

An unrecorded lesson is lost, not deferred. Surface it to the human and ask for
the grant — that is a one-time click, and it is cheaper than the next session
repeating the work.

---

## What this deliberately does not do

- **No search index.** These files are small; read them. If they grow to where
  that hurts, that is the moment to reconsider — not before.
- **No status tracking.** Claims in flight belong in the plan
  (`generate_plan`, `update_step_status`) and, for discovery candidates, the
  versioned discovery artifact — not here. This is what *settled*.
- **No deletion.** Superseding an entry means appending the correction and
  saying what it replaces. The record of having believed something is itself
  worth keeping — this workbench's most expensive errors were confident recall,
  and they are only visible in hindsight if the earlier belief survives.
