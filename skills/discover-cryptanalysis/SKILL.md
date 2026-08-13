---
name: discover-cryptanalysis
description: Search for new cryptanalytic directions against a primitive, construction, or parameter set by separating prior-art, structure-first, and adjacent-field tracks; mapping external results onto the target; cheaply falsifying candidates; and independently checking the strongest survivors. Use when asked to find new attacks, unexplored analyses, structural weaknesses, or results from related fields that may apply to a cryptographic algorithm. Do not use for reproducing or checking an existing claim; use investigate in validation mode or validate-attack instead.
license: Apache-2.0
---

# Discover cryptanalysis

Start the answer with `MODE: DISCOVER`. In a mixed request, label this the
discovery phase and keep the later independent-validation phase separate.

**This skill runs in the root conversation.** It creates delegations and it asks
the user before widening scope — and a delegated subagent can do neither:
`generate_plan` is not in its toolset at any access level, and it has no route to
a human at all. A subagent handed this skill will block on an approval nobody can
answer. Measured: one did, for 7.7 hours, producing nothing. Delegate the bounded
skills (`validate-attack`, `derive-cost`, `CRYPTO_VERIFIER`) *from* here; do not
delegate this.

Produce **testable attack candidates**, not novelty or security verdicts.

> known baseline → structural handles → independent transfer search → candidate
> register → cheap falsification → bounded pursuit → independent check

Treat prior art as the starting line. Never stop merely because the known
analysis has been recovered, and never infer novelty from a search miss.

## Fix the target and objective

Name the layer before generating ideas:

| Layer | Target |
|---|---|
| primitive | hard problem, permutation, curve, or algebraic object |
| construction | composition and claimed security notion |
| parameter set | concrete instance and claimed work factor |

State one attack objective precisely enough to falsify:

- security notion and adversary/oracle model
- full or reduced target
- exact parameters and distributions
- desired consequence: key recovery, forgery, distinguishing, collision,
  inversion, or a concrete cost reduction
- baseline cost and named cost model, when one exists

Keep implementation and deployment attacks out of scope unless the user asks
for them explicitly. Do not silently turn a primitive distinguisher into a
construction break.

Use `analyze-scheme` first when the target lacks an attack-surface map. In
discovery mode, continue from its ranked structural deviations; do not stop at
its normal human steering point.

## Plan the discovery run

Use the live investigation plan because discovery is inherently multi-track.
Create separate delegations for:

1. **Prior art** — establish what is already known about the scheme, problem,
   variants, and failed approaches.
2. **Structure first** — normalize the target into mathematical objects and
   identify handles without searching for an attack name.
3. **Adjacent fields** — search for mechanisms attached to those objects
   outside the scheme's usual cryptanalytic vocabulary.
   `firecrawl-mcp_firecrawl_research_search_papers` reaches literature ePrint
   does not index, `..._related_papers` walks outward from a known result, and
   `..._search_github` finds implementations. This track is the reason the
   remote research server is worth having: the local corpora are cryptography
   only, and a transfer by definition comes from somewhere else.

Keep the tracks independent until their outputs exist. Searching adjacent
fields only after reading the known attacks anchors the search on existing
terminology and reproduces the baseline.

**You are the only writer of the discovery artifact.** The tracks report through
`update_step_status` and return their candidate rows to you; you merge them and
save. Never let two tracks save `discovery-<target>.md`.

This is not tidiness. Every artifact version is a separate immutable file, so
there is no append and no merge: two savers each write from their own snapshot
and **the later one silently discards the earlier** — no conflict, no error,
nothing in the log. Three parallel tracks writing one register is the shape that
loses two thirds of a discovery run and looks like it worked.

Mark every plan step at start and finish as required by `investigate`. Record
unfinished candidates in the plan notes; they reach the artifact when you merge.

**The tracks are subagents, so brief them accordingly.** They cannot plan, cannot
ask the user, and must never call `request_network_access` — there is no human on
the other end of a subagent's request, and one that waits for approval waits
forever and silently. A track that needs something only you can grant records it
and keeps working. See `investigate` §2b.

## Establish the known baseline

Read the workbench knowledge, including gaps and lessons. Search the NIST
status reports for competition candidates (`nist-mcp_search_csrc`), ePrint
(`e-print-mcp_search_eprint`), the wider literature
(`firecrawl-mcp_firecrawl_research_search_papers`) and the open web
(`firecrawl-mcp_firecrawl_search`) — the last matters because competition
cryptanalysis is often a forum post rather than a paper. Search the primitive and hard problem as well as the
scheme and its former names.

Separate:

- published attacks and their exact scope
- known non-applications and failed approaches
- best known costs under named models
- unexplored structure or unchecked assumptions
- channels, queries, date, and coverage limitations

Report a miss only as:

> No prior application found in these channels and queries: …

Never shorten that to “novel,” “new,” “unbroken,” or “no prior work.”

## Normalize structure before proposing attacks

Write the target as objects and maps rather than scheme vocabulary:

- fields, rings, modules, vector spaces, varieties, codes, lattices, graphs,
  tensors, Boolean functions, or probability distributions
- public and secret maps, kernels, images, ranks, ideals, group actions, and
  decompositions
- invariants, symmetries, sparsity, low rank, bias, locality, repeated
  structure, and atypical parameter regimes
- randomness assumptions and the way the real distribution departs from them

Diff the target against its canonical construction and rank the added
structure. Every proposed transfer must name which handle it consumes.

Read [reference/transfer.md](reference/transfer.md) before running the
adjacent-field track. Use its routing table, mapping obligations, mismatch
guards, and cheap falsifiers; load it only for discovery work that reaches this
stage.

## Build the candidate register

Maintain no more than **five viable, mechanism-distinct candidates**. Keep fewer
when fewer survive mapping; never invent filler or count parameter variants as
different mechanisms.

Give every candidate a stable ID and record:

| Field | Required content |
|---|---|
| mechanism | the proposed attack route and the structural handle it uses |
| source result | theorem, algorithm, empirical result, target fact, or technique being extended |
| notation mapping | source objects and symbols mapped to target objects and parameters |
| assumptions | each source precondition marked satisfied, failed, or unchecked |
| consequence | the predicted effect on the stated attack objective and scope |
| prior-application search | channels, exact queries, date, and result |
| cheapest falsifier | the smallest analysis or computation that should kill it |
| provenance | sources, computations, and every original step marked `[DERIVATION]` |
| next action | falsifier, `derive-cost`, `validate-attack`, independent check, or reason to park |

Use this literal field order for each candidate, including falsified candidates:

```markdown
### Cn — short mechanism name
- **Status:**
- **Mechanism and structural handle:**
- **Source result:** (or “structure-first composition”)
- **Notation mapping:**
- **Assumptions:** satisfied / failed / unchecked, one by one
- **Predicted consequence and scope:**
- **Prior-application search:** channels, exact queries, date, result
- **Cheapest falsifier and result:**
- **Provenance:** `[SOURCE]`, `[TOOL]`, `[DERIVATION]`, as applicable
- **Next action or unblock condition:**
```

Do not promote a candidate beyond `screening` while any field is absent. An
honest “unchecked because …” is a field value; silently omitting the field is
not. Copy the full record into the falsified or survivor section rather than
reducing it to a one-line label.

**But a complete record is not an evidenced one, and the gate to `survivor` is
evidence.** Ten filled fields reading `unchecked` satisfy the rule above while
establishing nothing — that is the way this register decays, and it decays
invisibly because it still looks rigorous. So, additionally:

- **No candidate becomes `survivor` while an assumption its mechanism *depends
  on* is `unchecked`.** Unchecked assumptions off the critical path are fine and
  should stay visible; an unchecked one the route needs is the whole question.
- **`Cheapest falsifier` must carry a *result*, not a plan.** "Would run X" is
  still `screening`. A survivor is a candidate whose falsifier ran and failed to
  kill it.
- If neither is achievable within budget, the status is `parked` with the
  unblock condition — not `survivor`. **Parked is an honest outcome; a hollow
  survivor is not.**

Use this status lifecycle:

```
screening → falsified | survivor | parked
survivor → pursuing | parked
pursuing → falsified | awaiting-independent-check | parked
awaiting-independent-check → independently-supported
                           → independently-refuted
```

- Use `screening` only while the mapping and cheapest falsifier are explicit.
- Use `falsified` when a precondition, control, or computation kills the route;
  record the exact failure.
- Use `survivor` only after the cheapest falsifier failed to refute it.
- Use `pursuing` for at most two selected survivors.
- Use `parked` for a viable candidate blocked by budget, access, or missing
  theory; record the unblock condition.
- Use `independently-supported` only after a check that did not reuse the
  derivation as its proof.

Treat status as evidence state, not confidence or importance.

For a structure-first candidate with no external source result, cite the target
facts it composes and mark the proposed composition `[DERIVATION]`. Do not
manufacture a neighboring-field citation merely to fill the field.

## Falsify before developing

Run the cheapest falsifier for **every** viable candidate. Prefer, in order:

1. type, dimension, direction-of-reduction, or model checks
2. source-theorem preconditions instantiated with the target's real parameters
3. a tiny positive case and a negative control
4. a short Sage, Magma, estimator, SAT, or MILP computation
5. only then, a deeper derivation or experiment

Reject a transfer when it preserves only vocabulary or vector-space dimension
but not the operation used by the source result. Record clean falsifications as
results; a discovery run with no survivor is successful when it closes
plausible directions rigorously.

## Enforce the standard budget

Under the standard run:

- carry at most five mechanism-distinct candidates
- run a cheap falsifier against every viable candidate
- pursue at most the strongest two survivors
- keep toy computations short and checkable
- stop before expensive compute, real-scale implementation, a broader security
  objective, or a second-hop transfer

Rank survivors lexicographically by applicable preconditions, consequence for
the stated objective, falsifiability, concrete feasibility, and mechanism
diversity. Do not hide a failed precondition inside a numerical score.

Ask the user before exceeding two pursued candidates, widening scope, or
starting expensive compute. Park the remaining candidates with an explicit
unblock condition rather than discarding them.

## Hand off bounded claims

Keep discovery responsible for breadth and mapping. Once a candidate is
concrete:

- hand it to `derive-cost` when the mechanism is understood but no concrete
  cost exists
- hand it to `validate-attack` when the claim is that the mapped attack applies
  or runs
- use `analyze-paper` when a transferred theorem or reduction may not prove the
  informal claim attributed to it

Give the receiving skill one frozen candidate, its notation mapping, real
parameters, assumptions, and target objective. Do not ask those bounded skills
to continue generating attacks.

## Require an independent check

Mark original mathematical work as `[DERIVATION]` in prose and as evidence kind
`derivation`. A derivation alone remains a candidate.

Freeze a surviving candidate before delegation. Ask `CRYPTO_VERIFIER` to
**refute or independently check** the stated candidate by re-derivation, proof
audit, computation, or source verification. Explicitly forbid it from improving
the route, repairing failed assumptions, or proposing a neighboring attack.

Record the returned evidence as `independent-check`. A matching conclusion
counts only when the checker used an independent route; paraphrasing the
candidate does not.

Promote a finding to durable workbench knowledge only after an independent
check or human review supports it. Keep unchecked derivations in the live plan
and discovery artifact, never in durable knowledge as settled fact.

## Maintain the discovery artifact

Create one Markdown artifact named `discovery-<target>.md`, then **save every
later version by id, never by name**:

```python
first = save_artifacts(files=["discovery-<target>.md"])     # keep what this returns
save_artifacts(files=["discovery-<target>.md"],
               version_of={"discovery-<target>.md": "<id from the previous save>"})
```

**Saving by filename alone forks the artifact silently** — measured, and
`OPEN_PROBLEM.md` already exists twice in this project for exactly this reason.
Note also that the ids `list_artifacts()` hands back are **version** ids, not
artifact ids; passing the most recent one resolves to its parent and appends.
Re-list before reading if you expect movement, because a pinned version id keeps
returning that same version forever.

This matters more here than in most skills because the register is saved after
**every** candidate status or evidence change — so a fork does not lose one
write, it splits the whole run in two. See `investigate`'s
`reference/environment.md` for the full artifact mechanics.

Keep these sections distinct:

1. **Known baseline**
2. **Structural handles**
3. **Candidate register**
4. **Falsified candidates**
5. **Survivors**
6. **Novelty-search scope**
7. **Unchecked areas**
8. **Provenance**

Use those exact eight headings in both the artifact and the final answer, even
when a section says “none.” Under **Novelty-search scope**, include a three-row
track table for **prior art**, **structure first**, and **adjacent fields** with
their channels or methods, queries or normalization inputs, outputs, date, and
coverage limits. This makes the independence of the three tracks auditable.

**`Unchecked areas` is the one heading that must never be empty**, and it is
`analyze-scheme`'s rule about `NOT CHECKED` applying here for the same reason:
every discovery run has them — a structural handle nobody had time to normalize,
a source paper behind a paywall, an assumption that would need Magma. **An empty
`Unchecked areas` means the run was not examined, not that it was exhaustive.**
The other seven may honestly read "none"; write *why* when they do, because
"Falsified candidates: none" after five candidates says something quite different
from the same words after one.

Keep falsified and parked candidates visible in later versions. Publish
specialist evidence from the specialist and publish the synthesis here; do not
duplicate artifacts already produced by `CRYPTO_VERIFIER`.

## Which of these headings is durable

The artifact is scoped to this conversation. **Some of what it holds is a
finding that outlives the run, and some is this run's own bookkeeping**, and the
skill has never said which is which — so in practice none of it has been
recorded. One HQC run graded 26 adjacent-field leads CLOSED, each with its
obstruction and a measurement, and `knowledge.md`, `gaps.md` and `lessons.md`
mention HQC zero times.

| heading | where it goes |
|---|---|
| **Falsified candidates** | **one `add_gap` each** — the obstruction is the finding |
| **Novelty-search scope** | the `looked_in` channel list on those gaps, coverage limits included |
| Survivors | the artifact, until an `independent-check` exists |
| **Unchecked areas** | **the plan. Never a gap.** |
| Known baseline, Structural handles, Provenance | the artifact |

A falsified candidate is the highest-return record this skill produces:
something was looked for, and what closed it is known. Write the obstruction,
not the outcome — *"small-doubling theory has nothing to act on: the supports
realise 93-94% of maximal doubling"* is reusable, *"no attack found"* is not.

Recording them is one cell, not one call per row:

```python
for c in falsified:
    add_gap(question=c["candidate"],
            looked_in=["ePrint", "NIST", "firecrawl", "web"],   # actual channels
            finding=c["obstruction"], tags=c["field"])
```

**`Unchecked areas` must not become gaps, and this matters more than it looks.**
A gap is read by the next session as *this door was checked and is shut*. An
unchecked area is a door nobody opened — filing it as a gap tells a future agent
something was searched when it was not, which can stop them looking. That turns
the most valuable record type into a harmful one. Those belong in the plan,
where they are this run's remaining work and nobody else's conclusion.

The test, if a case is unclear: **a gap records what was learned by looking. If
nothing was learned, it is a to-do.** "Behind a paywall, and the NIST-hosted copy
also lacked it" was learned. "Nobody had time to normalize it" was not.


## Guard the words “novel” and “break”

Do not claim novelty from absence. State the bounded search result, its date,
channels, queries, aliases, and unavailable sources.

Do not call a result a break until all of these exist:

- a defined security objective and adversary model
- verified preconditions on the actual target
- concrete time, memory, data, and success probability
- an explicit full-versus-reduced scope
- comparison with the claimed threshold under a named model
- an independent check

Until then use “candidate,” “structural observation,” “reduced-instance
result,” or the exact weaker consequence established.

## Conclude

Report the known baseline, the structural handles, every candidate and
falsification, the pursued survivors, the bounded novelty search, unchecked
areas, and provenance using the exact eight artifact headings above. Before
finishing, audit that every candidate has all ten required fields, every viable
candidate has a falsifier result, the three search tracks are separately
reported, and every survivor's independent-check state is explicit. Say what
each survivor could imply and what has not been shown.

Do not force a positive result. A precise map of attractive transfers that fail
their assumptions is reusable cryptanalytic progress.
