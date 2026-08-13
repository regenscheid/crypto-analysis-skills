---
name: investigate
description: 'Run a cryptanalytic question end to end in the mode the request implies — validate an existing claim by retrieving and reproducing its evidence, or discover new attacks and analyses by treating prior art as a baseline and pursuing structural hypotheses. Use for any question that cannot be answered in a single lookup: checking a paper or attack, assessing a scheme, looking for new cryptanalysis or cross-field transfers, costing something no playbook covers, or resuming an investigation across sessions.'
license: Apache-2.0
---

# Investigate

This is the loop. Everything else in this workbench is a tool it reaches for.

> **question → what is already known → claims → a plan → work it → a written
> answer that cites its own evidence**

You drive it. The instructions below are the discipline and the sequence, not a
script — where your judgment is better than a rule, use it, and say why.

---

## Before step 0 — choose the research mode

Infer the mode from what the user is asking, then state it in one line before
working. The mode changes the stopping rule, not the evidence standard.

| request shape | mode |
|---|---|
| verify, reproduce, audit, check whether a stated result holds | **VALIDATE** |
| find new attacks, look for unexplored analysis, improve an attack, transfer a result from a related field | **DISCOVER** |

An explicit first line `MODE: VALIDATE` or `MODE: DISCOVER` overrides inference.
“Analyze this scheme” alone does not say whether the user wants a bounded
assessment of known results or a search for new ones. Ask once in that genuinely
ambiguous case; do not silently choose the more open-ended job.

When the request asks for both, make **DISCOVER** and **VALIDATE** separate phases.
The discovery phase produces candidates and primary evidence. The validation
phase independently checks the survivors; it does not improve them while checking
them.

Everything below applies to both modes unless a paragraph names one.

---

## 0. Establish the baseline

Cheapest move first.

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
from knowledge import read_all
print(read_all())            # knowledge.md + gaps.md + lessons.md — all small
```
```
e-print-mcp_search_eprint        the preprint literature
nist-mcp_search_csrc             the standards and the round-status reports
firecrawl-mcp_firecrawl_search   everything neither of those indexes
```

**`reference/tools.md` maps capability to tool name**, including the paper- and
web-search tools the local corpora do not have. Tool names drift; if one does not
resolve, call `portal_list_servers` rather than guessing a variant.

**Nothing prompts you to read the knowledge files.** They are files, not a tool
that appears in your context — so this step happens because you do it, or not at
all. See `workbench-knowledge`.

**A recorded gap is an answer.** It says a door is known to be closed and which
one. This project once ran a 603-second parameter sweep to settle a descent
question before noticing the estimator ships no descent model — the gap was
already recorded, and reading it would have cost one file read.

In **VALIDATE**, a baseline hit that settles the exact question may end the
investigation: say it, cite it, stop. In **DISCOVER**, the same hit settles that
subclaim and prevents duplicate work, but it does not end the investigation. It
becomes the known baseline or prunes one candidate; continue with
`discover-cryptanalysis`.

**And when the tooling fights you rather than the mathematics, read
`reference/environment.md`.** It carries what this environment permits, measured:
how to tell a proxy refusal from a host refusal, why nothing here can drive a
browser, the two kernels and which can read what, that `host.mcp()` discards
binary, and that a subagent has no route to a human. Most of it was established
only after a wrong assumption had already cost a day — which is the reason it
ships with the skill instead of living in one machine's knowledge file.

**For any named competition candidate, go to the NIST round-status reports
first** — IR 8240 / 8309 / 8413 / 8528 / 8610, one section per candidate saying
what happened to it and why:

```
nist-mcp_search_csrc("IR 8413 <scheme>")
nist-mcp_csrc_fulltext(ref, query="<scheme>")
```

**A large share of competition cryptanalysis was never a paper.** It was a
`pqc-forum` post or an official comment, so searching ePrint alone will miss it
and report a scheme as unbroken when it is not. Use
`firecrawl-mcp_firecrawl_search` for the forum, the announcement, the slide
deck. That channel is the point: memory is the only other route, and memory is
what this workbench exists to replace.

**A miss is not evidence of security.** Report what you searched and how
completely — see `crypto-review`'s `reference/invalid-inferences.md`, first row.

In **VALIDATE**, if you get a real answer: **say it, cite it, stop.** A question
answered in four calls is the best possible outcome, not a disappointing one.

---

## 1. Frame it

In **VALIDATE**, decompose into claims that can each be settled by **one** move:
a retrieval, a computation, or a bounded derivation. A claim needing all three
is three claims.

In **DISCOVER**, also allow candidate-producing steps: structural normalization,
analogy search, transfer mapping, candidate refinement and cheap falsification.
Each such step must produce a concrete update to the versioned candidate
register: a new candidate, a changed mapping, a falsification, a survivor, or a
named unresolved obligation. “Think about attacks” is not a step.

Order them so that what unblocks the most comes first, and say out loud what
depends on what — an unstated dependency shows up later as work nobody can do
and nobody can say why.

Say where each claim stands at birth: open, or already known to need a specific
computation. That framing becomes the plan in §1b, where the claims become
`steps` and independent lines become `delegations`.

---

## 1b. Plan it — `generate_plan`

A plan is a live artifact the human watches and approves, and it is strictly
better than narrating intentions in prose. Use it for real investigations.

**But every plan blocks on approval.** `generate_plan` saves the artifact and
*pauses*. There is no unattended mode. So planning a small question does not
make it more rigorous — it puts a click in front of an answer.

**Plan when** the work is genuinely multi-stage: several distinct analyses, a
pipeline worth sequencing, parallel directions, or real compute (Magma, a long
sweep, many full-text fetches).

**Skip it** for a lookup, a quick question, or a single computation — including
a four-claim investigation settled by four retrievals. When unsure, start
without one; you can plan later if the scope grows.

*(A session-level Plan mode toggle can make planning mandatory regardless. That
is the human's setting — you cannot read or change it, and nothing here
overrides it.)*

### Write it in the schema's own shape

```
phases[]          → delegations[]        ← each dispatched as its own subagent
                       → steps[]          { title, description }
desired_outputs[]
feasibility       { confidence, rationale }
```

Parallel directions are **delegations inside a phase**, not something you invent
structure for. Two fields carry most of the value and are the ones usually left
thin:

- **`desired_outputs`** — what will *exist* when this is done. A number, a
  table, a settled claim. Not "investigate X".
- **`feasibility.rationale`** — say honestly what could make this not work, and
  **what would make you abandon a track**. A plan with no stated failure
  condition runs to completion regardless of what it learns.

### Keep it current — this is a call, not an attitude

```
update_step_status(step="<exact title>", status=in_progress|completed|blocked|skipped, notes=…)
```

At the **start and end of every step you touch.** Progress is never inferred
from your activity. `step` must match the plan's title exactly — it is keyed on
the string. The session cannot be completed while any step lacks a terminal
status, so this is enforced, not merely encouraged.

In a multi-delegation phase, calling `update_step_status` on a track is what
**claims it for you** rather than delegating it. Do not claim tracks you intend
to hand off.

### Revising a plan you are part-way through

**Do not call `generate_plan` again** — that creates a new artifact and
supersedes the old one, discarding it. To amend, edit the plan JSON in place,
keeping its nested structure, and save a new version of the same artifact:

```
save_artifacts(files=[…], version_of={"<plan filename>": "<plan artifact_id>"})
```

This re-requests approval, which is correct — the human approved a different
plan. It also means **revision is not free**: amend when the plan is wrong, not
to tidy it.

**Keep step titles byte-identical** unless you mean to retire a step. Status is
keyed on the title string, so renaming a step during a revision is expected to
orphan its recorded progress. *That specific behaviour is unverified* — if you
must rename mid-flight, re-check the step's status afterwards rather than
assuming it carried.

Adapting is not disobedience: if a track's premise is refuted, or a cheap step
shows the expensive one is unnecessary, amend and say why. Following an approved
plan past the point where it stopped making sense is a failure to report.

### There is exactly one plan, and it is yours

**A delegated subagent cannot plan.** `generate_plan` is not in its toolset, and
no profile setting grants it — tested at maximum access (`unrestricted: true`,
zero exclusions) and it still is not there. `host.agents.*` configures skills and
connectors; it does not reach the platform's built-in tools. Planning and its
approval gate are wired to the root conversation.

So do not design around a subagent opening its own approval card. It cannot.

**This generalises, and it is the more useful form: a subagent has no channel to
a human.** Planning is one instance. Network access is another, and it failed
expensively before anyone wrote the rule down — see *Network access: only the
root asks, and nobody blocks* in §2b. Anything that ends in a person deciding —
an approval, a grant, a scope call, a permission — belongs to the root
conversation. A subagent that waits for one waits forever, and *silently*, which
is the part that costs hours rather than minutes.

**A subagent does have `update_step_status`.** It reports progress into *your*
plan rather than keeping one of its own — so a delegated track still shows
movement, and the plan stays the single place the human watches.

If a track needs its own human sign-off, the lever is **structure, not
delegation**: give it its own **phase** in your plan. Phases are the unit the
human approves. And when a track's real shape only becomes clear once work
starts, amend the plan then — `save_artifacts(version_of=…)` — rather than
guessing the detail up front to avoid a later approval.

---

## 2. Work the plan

Take the next step that is not blocked. Mark it `in_progress`, do it, mark it
`completed` — `update_step_status` at both ends, every time. Progress is never
inferred from your activity, and the session cannot be closed with a step left
in a non-terminal state.

Attempt each step by exactly one route:

**Retrieve.** Search the corpora, then read the **body** — `e-print-mcp_eprint_fulltext`,
`nist-mcp_csrc_fulltext`. An abstract identifies a reduction; it rarely
parameterises one. This project derived a cost model from an abstract, got the
reduction one equation wrong, and found out only when a human supplied the PDF.

*If an ePrint paper is not cached, `e-print-mcp_eprint_fulltext` queues it and
the server's own fetcher retrieves it.* You do not need to do anything, and
**you must not ask the human to run a command**: retrieval that needs a person
present is exactly what this loop is built to avoid.

**How long to expect — the tool tells you.** A queued call answers with an
estimate ("expect it in about 2 minute(s)"). **Use that number rather than a
rule of thumb**: it accounts for how many papers are ahead of yours and for the
server's rate limit, so when the hourly budget is nearly spent the honest answer
is an hour, not two minutes. Come back after the stated interval; do not
conclude it is broken because it is not there yet.

**Calling `e-print-mcp_eprint_fulltext` again IS the status check.** There is no
separate tool, and asking twice cannot queue the same paper twice.

Why it works that way, so you can reason when it does not: ePrint serves only
browsers (plain `curl` and `curl_cffi` impersonating four browser profiles all
return 403 with a challenge page), so a fetch means driving a real browser. That
happens in a separate container, one paper at a time, spaced out — the server is
one address to ePrint, and a shared address is easy to get blocked.

**Do not block, and do not poll.** Queue the paper, note that the step waits on
a fetch, work other steps, come back after the stated interval.

**A failed fetch retries on its own, and eventually stops.** Four attempts at 5
minutes, 30 minutes and 2 hours — about 2.6 hours in total — after which it is
marked `gave-up`. So:

- **missing after a few minutes** — normal, keep working.
- **`e-print-mcp_corpus_stats`** reports the queue (due, waiting on backoff,
  gave up) and the remaining fetch budget. Read it before assuming a fault.
- **`gave-up`** — the tool says so, and names what is still untried. Believe that
  wording and do not widen it: four refusals from ePrint is a fact about **one
  host**, not about the paper. This workbench has the counter-example on record —
  a body ePrint refused was read from the NIST-hosted copy. Try
  `nist-mcp_search_csrc`, a `firecrawl-mcp` fetch, or ask the human for the PDF
  before recording anything, and scope the gap to *body not retrieved from
  ePrint* with those listed as channels remaining.

**A throttle message is not a retrieval failure.** If a call says the fetch was
declined — interval, hourly cap, cooldown — nothing was asked of ePrint at all,
so it is not evidence about the paper and must not be recorded as one.

**Compute.** `sweep.py` — `lwe`, `uov`, `mq`, `minrank`, `subfield`, `sda`.
Always name the cost model; a bare exponent is not a result. If a figure looks
implausibly cheap, believe the guard and not the number.

**Before a long computation, time ONE unit of it.** Not an estimate — run the
smallest instance and look at the clock. If you cannot say what one iteration
costs, you are not ready to launch the sweep, and 94% of this workbench's runs
finish in under ten seconds, so the ones that do not are worth ten seconds of
thought first.

Two failures on 2026-08-06, both avoidable by that one step:

- A script whose own docstring said enumeration is *"infeasible past n~32"* ran a
  default grid up to **n=64** — SVP enumeration in dimension 128. It burned 20
  minutes and could never have finished. **A bound you know belongs in the code,
  not in the prose above it.**
- A `class_number()` call on a degree-128 field ran **27 hours**, orphaned to PID
  1 when its parent died, producing nothing after its first two rows.

So, in order:

1. **Would analysis or the literature settle it instead?** The cheapest
   computation is the one you do not run. A Gaussian-heuristic count often
   answers "is this vector unique" for *real* parameters, where enumeration
   answers it only for toy ones — a result at n=32 that cannot reach n=512 may
   not be worth having.
2. **Time one unit**, then multiply by the grid. Say the number out loud before
   starting.
3. **Bound the run** so it cannot outlive its usefulness — `timeout`, a solution
   cap, a smaller grid — and print progress per iteration with `flush=True`, or
   nobody can tell a slow run from a wedged one.
4. **Parallelise only once it is measured and worth it.** Independent trials over
   seeds pool trivially; a single Gröbner basis or one enumeration does not split
   at all, so four workers on four intractable instances is still intractable.
   If you do pool, each iteration must seed its own RNG from the loop index or
   the samples correlate silently, and set `OMP_NUM_THREADS=1` per worker so
   numpy's BLAS does not oversubscribe. **The crossover is about 20 ms of work
   per trial** — below it a pool is slower than the serial loop (measured:
   0.3x at 2 ms, 2.1x at 20 ms, 7.4x at 2.6 s). The runnable idiom, the
   mandatory `if __name__ == "__main__"` guard, and what does not
   parallelise at all are in `reference/sage-idioms.md` under Parallelism,
   shipped with `validate-attack`.

A computation that cannot terminate is not evidence. Neither is one still
running when the question has moved on.

**Derive.** `derive-cost`, one hop, verified at toy scale.

**Validate.** `validate-attack`, when the claim is that a specific attack works.
It decides for itself whether analysis or an implementation settles that —
reaching for code when a precondition already fails is the waste it exists to
prevent.

**Discover.** `discover-cryptanalysis`, only in **DISCOVER** mode. It separates
the prior-art, structure-first and adjacent-field tracks; records every concrete
candidate; cheaply falsifies the viable set; and hands at most the strongest two
to `derive-cost` or `validate-attack` under the standard budget.

Then record the outcome where it belongs:

- **`update_step_status(step, status, notes=…)`** — the step's fate, with the
  reason in `notes`. This is what the human watches.
- **`add_entry(...)`** (`workbench-knowledge`) — only once something is
  *settled*, with `evidence` whose `kind` is `assertion` / `computation` /
  `paper` / `spec` / `human` / `derivation` / `independent-check`.
  **`assertion` is not a source, and a derivation is not its own independent
  check.** Claim nothing stronger than the evidence supports; one run on one
  host is not `supported` until something independent agrees.
- **`add_gap(...)`** — what you looked for and did not find.

In **VALIDATE**, every step must either settle something or record a gap. In
**DISCOVER**, updating the candidate register with a mapping, falsification,
survivor or explicit unresolved obligation is also a valid outcome. A step that
does none of those needs restating, not more effort.

### When you are stuck

- **Everything blocked** — the blocking steps are the work. Look at what they
  wait on.
- **A claim you cannot source** — search first, then mark the step `blocked`
  with the reason, and `add_gap` with `looked_in` as a **channel list**:
  "searched ePrint" and "searched ePrint, NIST, breaks and the web" are
  different findings, and only the second licenses a negative.
- **A step that has stopped paying** — mark it `skipped` with a note saying
  why, and move on. Several attempts without movement is information about the
  step, not a reason to try harder.
- **A real choice for the human** — put it in the plan and amend if the answer
  changes the shape (`save_artifacts(version_of=…)`), stating each option's
  consequence. Never ask only in prose: a chat question is one scroll from gone.
- **A number you do not trust** — delegate to `CRYPTO_VERIFIER`. It has the
  python kernel and the connectors; REVIEWER has neither. Remember that a
  delegated agent returns its result to *you*, so publishing stays your step.

---

## 2b. Keep it moving — the default execution style

**Do not stop after one claim.** A single iteration per turn makes the human the
scheduler, and they have better things to do. Keep going.

### Keep working while there is work

Loop: next unblocked step → `in_progress` → attempt → record → `completed` →
again. The plan is current at every moment, so the human can watch without being
asked to.

**An open question does not stop the run.** Note it on the step and *carry on
with something else*. Blocking a whole investigation on one question is the
failure to avoid — work the rest of the plan while it waits.

### Stop when, and only when

- **Nothing is actionable.** Every remaining step is blocked or terminal.
- **The question is answered under the selected mode.** In VALIDATE, the exact
  claim is settled or unresolved with a named settling route. In DISCOVER, the
  baseline is established, every viable candidate has had its cheapest falsifier
  attempted, and the bounded survivor set has been pursued. Go to CONCLUDE.
- **Every remaining line waits on the same unanswered question.** Rare. Say so.
- **You have spent enough.** Judge it: a step that has consumed several attempts
  without moving is telling you something — mark it `skipped` and say why.

Note what is *not* on that list: an interesting finding, a surprising result, or
a claim you would like an opinion on. Record those and keep going. In DISCOVER,
finding an existing analysis is likewise not a stopping condition for the whole
run.

### Hand back with a state of play

When you stop, say — briefly — what moved, what is waiting, and what you would
do next. The human is resuming a live thing, not reading a report.

### Resuming, in a later session

**Read the plan and the knowledge files first — not your recollection**, which
is the failure mode this workbench was built against. The plan carries every
step with its status and the notes attached to it; `read_all()` carries what has
been settled and what is known to be missing.

The conversation is *not* gone, and that is worth knowing: past sessions persist,
are browsable in the UI, and are searchable with `archive_search`. If the plan
and the knowledge files leave you unsure why something was decided, search the
archive rather than guessing or re-deriving.

### Running unattended across time

The host has `routine_schedules` — a recurring tick bound to a conversation
(`every_minutes`, `on_tick`, `enabled`). **It has zero rows in this install, so
it is unexercised here and its API surface is unverified.** If you want an
investigation to advance on a schedule rather than when someone opens the
session, that is the mechanism to try, and finding out how it is invoked is the
first step. Do not assume it works because the table exists.

### What it must never do alone

Retrieving, computing, parking, reviving and raising decisions are all yours to
do unattended. Three things are not:

- **Concluding.** A finished plan is a state, not a result. The answer gets
  written and published for a person, always.
- **Deciding scope, or whether a cost is worth paying.** Raise it.
- **Promoting a claim to `supported` on your own say-so.** That needs something
  independent — a source, a computation, or `CRYPTO_VERIFIER`.

### Network access: only the root asks, and nobody blocks

Read `reference/environment.md` before a track needs direct network access. Three
failures look alike and only one needs a grant:

| symptom | meaning |
|---|---|
| `HTTP 000`, `Tunnel connection failed: 403` | the proxy refused CONNECT — never reached the host. **This one needs a grant.** |
| plain `HTTPError 403`/`404` | reached the host, which refused it. Fix the request, not permissions. |
| `Operation not permitted` | filesystem, not network |

Fetch through a connector where one exists; it already sets the right transport.
If you are a delegated subagent, **never call `request_network_access`**: there
is no human on that path. Record the exact domain and need, continue other work,
and return the request to the root. If you are the root, request all known
domains together, preferably before delegation.

There is no verified way to notify a running child that a grant arrived. Let it
retry later, or stop and re-delegate it. The invariant is simple: **a subagent
must never wait on something only a human can grant.**

---

## 3. Keep the work visible

**The plan is the live view, and `update_step_status` is what keeps it live.**
It is current by construction — there is nothing to publish and nothing to go
stale. This replaces a rule that used to live here: an earlier version of this
workbench kept its state in a connector and had to re-render and re-publish
after every write to stay visible. It was measured **20 hours behind** once. The
plan cannot drift that way, because the human is reading the same object you are
updating.

What still needs publishing with `save_artifacts` is **output**, not state:

- the **answer** (§4), as its own artifact
- tables, figures and CSVs a person would want to open — a sweep's numbers, a
  cost comparison, a plot

Re-saving the same filename adds a *version* rather than a second artifact, and
the interface presents versions as history — so revising a table in place is
free and keeps the trail.

Work the human cannot see has not been delivered. The difference now is that
keeping it visible costs a status call rather than a publish cycle.

---

## 4. Conclude

Stop when every step is terminal, or the question is answered. Running out of
steps is **not** the same as answering anything — so finish properly:

1. **Write the answer.** The original question, answered in prose, citing the
   evidence that supports it. Name what is still unverified; a conclusion with a
   stated soft spot is worth more than one that hides it.
   In DISCOVER, use the `discover-cryptanalysis` output sections and keep the
   known baseline, falsified candidates, survivors and scoped novelty search
   visibly separate.
2. **Graduate what settled.** `add_entry` for each settled result — including
   refutations, which are recorded as `NOT TRUE: …`. A refuted claim is a
   result, and the next session needs it as much as a positive one.
3. **Record the dead ends.** `add_gap` for what you looked for and did not find.
   A negative must be as cheap to record as a positive, or it does not get
   recorded and the next session repeats your search.
4. **Record any process lesson** with `add_lesson` — a gotcha or a correction
   that cost you time and would cost the next session the same.
5. **Publish the answer** as its own artifact. The plan shows how you got there;
   it is not the answer.

---

## 5. Audit before you believe yourself

Run `verify-claim` on your own output before presenting it. Every load-bearing
claim inventoried, classified
`[SOURCE]`/`[TOOL]`/`[KB]`/`[DERIVATION]`/`[RECALL]`, every number reproduced
from the command that supposedly produced it. A derivation is traceable primary
evidence, not its own independent check.

This is not ceremony. The session that built this workbench committed **all
eight** of that skill's failure modes in a day — including asserting a
"fresh" parameter set that was a published one, and reporting three conclusions
from a test that had silently failed. The most expensive errors here have not
been reasoning errors. They have been confident recall, and confident recall
feels exactly like knowing.

---

## What this deliberately does not do

- **It does not re-derive a known result merely to answer a validation
  question.** Retrieval is the designed path and a hit in `knowledge.md` is a
  success, not a shortcut. Discovery may use that result as a baseline while
  pursuing structurally different candidates.
- **It does not conclude without writing an answer.** A finished plan is a
  state, not a result.
- **It does not decide alone what a person should decide.** Scope, and whether a
  cost is worth paying, go in the plan for approval.
- **It does not keep private state.** Everything it learns is in the plan, the
  knowledge files, or a published artifact.
