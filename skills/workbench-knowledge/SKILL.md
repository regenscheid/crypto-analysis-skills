---
name: workbench-knowledge
description: Read and extend the crypto workbench's durable knowledge — what has been established and how, what was looked for and not found, and lessons worth carrying between sessions. Use at the start of any substantive work to check what is already known, and whenever an investigation settles something, fails to find something, or teaches a gotcha worth not rediscovering.
license: Apache-2.0
---

# Workbench knowledge

Keep the durable research record in ordinary local files. `CRYPTO_FILES`
is the storage parent and defaults to `~/crypto-workbench-files`. Resolve a
stable, unique project ID, then use
`CRYPTO_FILES/projects/<project-id>/` as the project directory. Set
`CRYPTO_FILES` to an absolute writable path and grant it if the host
sandboxes writes. Never put two projects into the same project directory or
derive its path from a delegated agent's current working directory.

| Project file | Purpose |
|---|---|
| `knowledge.md` | what has been established, and **how** |
| `gaps.md` | what was looked for and **not** found |
| `lessons.md` | gotchas and conventions worth carrying forward |

The project also has an in-flight board: one append-only
`board/sessions/<session-id>.jsonl` ledger per session and generated
`board/notebooks/<session-id>/<idea-id>.md` notebooks. A project-wide
snapshot reduces all session ledgers. The three files above remain shared
across sessions; separate session ledgers let investigations take different
paths while retaining one project history. Read
[the research-board procedure](reference/research-board.md) before a sustained
DISCOVER investigation.

They used to be an MCP connector. They are files now because this is storage,
not search: 24 entries and 8 gaps do not need an index, and a connector needs an
app restart to pick up changes, hides its own failures from `tools/list`, and
cannot be opened by a person.

---

## Read it first

```python
import sys, os, glob
# CRYPTO_SKILLS may name the checkout, the installed skill, or its scripts
# folder. Claude Science can also install skills globally or per organization.
_candidates = [os.environ.get("CRYPTO_SKILLS", ""),
               "skills/workbench-knowledge/scripts",
               "../workbench-knowledge/scripts",
               os.path.expanduser("~/.cscience/skills/workbench-knowledge/scripts"),
               os.path.expanduser("~/crypto-analysis-skills/skills/workbench-knowledge/scripts")]
_candidates += glob.glob(os.path.expanduser(
    "~/.cscience/orgs/*/skills/workbench-knowledge/scripts"))
_script_dir = None
for _p in _candidates:
    if not _p:
        continue
    for _c in (_p, os.path.join(_p, "scripts"),
               os.path.join(_p, "skills/workbench-knowledge/scripts")):
        if all(os.path.isfile(os.path.join(_c, name))
               for name in ("knowledge.py", "board.py")):
            _script_dir = _c
            break
    if _script_dir:
        break
if _script_dir is None:
    raise FileNotFoundError("Set CRYPTO_SKILLS to the skills checkout or installed skill")
sys.path.insert(0, _script_dir)
from board import project_dir_for_id, board_snapshot
from knowledge import read_all, add_entry, add_entry_once, entry_id_for_claim, add_gap, add_lesson
project_dir = project_dir_for_id("<stable-project-id>")
print(read_all(project_dir=project_dir))
print(board_snapshot(project_dir))
```

Replace the placeholder with the host's stable project ID. If the host does
not expose one, obtain or create a stable ID and keep it in a project artifact
that later sessions can find; do not mint a new ID on every session. The root
agent resolves `project_dir` once and supplies its absolute path and session
ID to every delegate. The helpers do not infer either from the current working
directory. Existing top-level `knowledge.md`, `gaps.md`, and `lessons.md`
are legacy files; assign their relevant entries to a project deliberately
instead of silently mixing them with a new project.

Read all three project files and the project-wide board snapshot before
deriving anything.

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
          source="<investigation or session>", claim="C7",
          project_dir=project_dir)
add_gap(question, looked_in=["ePrint", "NIST", "firecrawl", "web"],
        finding="...", project_dir=project_dir)
add_lesson("Magma exits 0 on user errors; require a final done marker.",
           project_dir=project_dir)
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
add_entry_once(
    "Candidate C2 establishes ... under assumptions A1-A4.",
    kind="derived result",
    evidence=[
        {"kind": "derivation", "ref": "<versioned discovery artifact>#C2",
         "note": "Original argument and notation map."},
        {"kind": "independent-check", "ref": "<verifier report>",
         "note": "Fresh computation checked the stated consequence."},
    ],
    claim="<lemma-id>", project_dir=project_dir,
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

**Append. Never rewrite the authoritative record.** Use the helpers; each
knowledge entry and board event is one `write()` in append mode. Board
notebooks are derived views that can be rebuilt from the session ledger.

Do **not** read-modify-write, and do **not** use `edit_file` — its exact-match
replacement *is* read-modify-write. Measured here, 8 concurrent writers × 150
records each:

| | kept |
|---|---|
| `open(path, "a")` + one `write()` | **1200 / 1200** |
| read → append → write back | 7 / 1200 |

That is not a corner case. Delegated subagents inherit the same host grant and
write to the same files, so simultaneous writers are the normal condition.

Knowledge entries are capped at 4 KB; board events are capped at 1 MiB. A
knowledge entry approaching its cap should be split. Keep a board outcome
intact so the delegated return is recorded unchanged.

Regression test:

```
python3 skills/workbench-knowledge/scripts/knowledge.py --selftest
python3 skills/workbench-knowledge/scripts/board.py --selftest
```

---

## If the write fails, say so loudly

The knowledge helper raises `GrantMissing` rather than returning quietly. A
board ledger write raises `BoardWriteError`; inspect the ledger before retrying
because the attempted event may have been saved. If notebook materialization
raises `NotebookMaterializationError`, the event **was** saved: call
`rebuild_notebook(project_dir, session_id, idea_id)` after the filesystem issue
is resolved, without appending the outcome again. **Do not catch an error and
carry on as though the record is complete.** The read/write grant on the
folder is *per project*: a session in a different project holds none, and its
first write fails.

An unrecorded lesson is lost, not deferred. Surface it to the human and ask for
the grant — that is a one-time click, and it is cheaper than the next session
repeating the work.

---

## What this deliberately does not do

- **No search index.** These files are small; read them. If they grow to where
  that hurts, that is the moment to reconsider — not before.
- **No competing job or checkpoint system.** The host owns plans, progress,
  approvals, and artifact versions. The board records in-flight research ideas,
  outcomes, and evidence across sessions; only independently checked results
  enter `knowledge.md`.
- **No deletion.** Superseding an entry means appending the correction and
  saying what it replaces. The record of having believed something is itself
  worth keeping — this workbench's most expensive errors were confident recall,
  and they are only visible in hindsight if the earlier belief survives.
