---
name: derive-cost
description: Produce a concrete cost for a target nothing has costed yet — search what is already known, find and read a reduction to a problem that IS costed, instantiate it with real parameters, verify at toy scale, and write the result back as an entry or a gap. Use when an attack's structure is understood but its cost cannot be obtained.
license: Apache-2.0
---

# Derive a cost where none was published

This is the workbench's miss handler: what happens when it does not already
know something. One hop, bounded by construction —

> target nothing has costed → candidate reduction → **instantiate at toy
> scale** → verify or refute → write back

When `discover-cryptanalysis` hands this skill a candidate, take the mapping as
the object to cost. Do not expand the candidate portfolio or search for a
different technique here; return the cost, refutation, or unresolved obligation
to the discovery register.

**The deliverable is a number, and the reduction is how you get there.** That
matters because "reduction" ordinarily names a *security* reduction — the proof
that breaking a scheme breaks an assumption — and auditing one of those as an
argument is `analyze-paper`'s job, not this. Here a reduction is a route: it
carries you from a target you cannot price to a problem an estimator can, and it
is worth exactly as much as the cost that comes out the far end.

It exists because of a specific observed failure. In a blind test on Rainbow,
the analysis derived the MinRank structure **correctly** and still could not
produce a cost, because nothing turned that derivation into
`MRProblem(q, m, n, k, r)`. The reasoning was right and the answer was missing.
The gap was not knowledge; it was the step between a derivation and a
parameterised call.

## Plan first, if this is multi-stage

A full reduction hunt is a pipeline, and that is exactly the shape `generate_plan` is for:
parallel directions become `delegations` in a phase, and the human approves the
approach once instead of discovering it at the end.

Skip planning for a single lookup or bounded estimator call. Follow
`investigate`'s **Plan without stalling** rule and its platform adapter rather
than duplicating host-specific plan mechanics.

## 1. Search what is already known — including the dead ends

```
nist-mcp_search_csrc             already broken? the round-status reports say
firecrawl-mcp_firecrawl_search   pqc-forum posts and official comments
e-print-mcp_search_eprint        the preprint literature
```
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
print(read_all())     # knowledge, gaps and lessons — all of it, it is small
```

**Do this first, every time.** A returned gap is as valuable as an entry: it
tells you a door is already known to be closed and which one. This project ran a
603-second parameter sweep to settle a descent question before noticing the
estimator ships no descent model — a gap record would have cost one call and
saved the run.

**Ask whether it is already broken before costing it.** The cheapest possible
outcome is discovering the target is broken and the attack is already written
down. A large share of competition cryptanalysis was never a paper — it was a
`pqc-forum` post or an official comment — so `e-print-mcp_search_eprint` alone
will miss it. Check the NIST round-status reports (IR 8240/8309/8413/8528/8610)
and search the web. **A miss is not evidence of security**; it is a claim about
your search, and it must name its channels.

If the KB answers your question, you are done. Say so and stop.

## 2. Find the reduction, and read it — do not recall it

Search the corpora for how the target reduces to something standard:

```
e-print-mcp_search_eprint("<scheme> key recovery reduces to")
e-print-mcp_search_eprint("<scheme> MinRank attack")
```

Read what you find — and there is now a mechanism behind that word:

```
e-print-mcp_eprint_fulltext(paper_id, query)    the paper's BODY, from a local cache
```

A reduction remembered rather than read is the failure this whole workbench is
built against, and abstracts are enough to *identify* a reduction but rarely
enough to *parameterise* it. This project spent a session deriving a cost model
from an abstract, getting a reduction one equation wrong, and only finding out
when a human handed over the PDF. The body had the theorem in it the whole time.

First read of a paper takes **up to about two minutes** — the watcher polls the
queue every 60 seconds and the browser fetch itself is 20-40 seconds (measured).
Every read after that is instant. Come back on a later pass rather than
concluding it is broken because it is not there yet. If the body is genuinely
unreachable, say the parameterisation is unverified and mark it so downstream —
but check the cache before claiming that.

## 3. Instantiate — this is the step that was missing

A derivation is not a cost. Turn it into an actual call with actual numbers.

The costed problems available, with their real signatures:

```python
from cryptographic_estimators.MREstimator import MREstimator
MREstimator(q, m, n, k, r)        # q field order, m x n matrices,
                                  # k solution-vector length, r target rank
from cryptographic_estimators.UOVEstimator import UOVEstimator
UOVEstimator(n, m, q)             # n variables, m equations
from cryptographic_estimators.MQEstimator import MQEstimator
MQEstimator(n, m, q)
```

Write the mapping down explicitly, symbol by symbol, before running anything:

> Rainbow's public key gives `m` quadratic forms in `n` variables over `F_q`;
> the MinRank instance is `k = m` matrices of size `n × n`, target rank
> `r = <the oil-space dimension the reduction identifies>`.

**State every symbol's origin.** A mapping with one unexplained index is where
a wrong cost comes from, and the number it produces will look entirely
plausible.

A worked instance, so the shape is concrete:

```
MREstimator(q=16, m=15, n=15, k=78, r=6)
  BruteForce      2^143.8      SupportMinors   2^144.0
  Minors          2^144.7      KernelSearch    2^147.7
  BigK            2^154.7
```

A newly computed parameter cost is an evaluation of the method used, not by
itself a new algorithm or attack. For contribution language, use
[contribution assessment](../investigate/reference/contribution-assessment.md).

## 4. Verify at toy scale before trusting the real one

Run the mapping on parameters small enough to check another way — a scheme
whose cost is already published, or an instance you can brute-force. If the
toy instance does not reproduce a known answer, the comparison is unresolved.
Check inputs, units, implementation, reference assumptions, and mathematical
mapping before assigning the cause. Do not use the full-size estimate until the
discrepancy is explained.

This is the whole reason the hop is bounded: one reduction, instantiated,
checked against something independent. Not a search for the best attack.

## 5. Sanity-check the result before writing it back

From `crypto-review`, the checks that matter most here:

- Does the cheapest family actually **apply**, or is the estimator pricing an
  attack whose preconditions the scheme does not meet?
- Is a sub-2^64 figure on a standardised parameter set a break, or a misapplied
  model? Assume the latter until shown otherwise.
- Which **cost model** is this, and does it match what the comparison target
  used? A figure without its model is not a result.

## 6. Write back — both outcomes

**It worked** — the reduction holds and the instance prices:

```python
add_entry("<scheme> key recovery reduces to MinRank with "
          "q=…, m=…, n=…, k=…, r=…; cheapest family <X> at 2^<c>",
          kind="reduction",
          evidence=[{"kind": "paper", "ref": "…", "note": "source of the reduction"},
                    {"kind": "computation", "ref": "…", "note": "toy-scale verification"}])
```

**It did not** — say so with the same effort:

```python
add_gap(question="…", looked_in=["ePrint", "NIST", "firecrawl", "web"], finding="…")
```

A negative finding must be as cheap to record as a positive one. If it is not,
it does not get recorded, and the next session repeats your search.

Then close the loop on the plan — `update_step_status` with the outcome in
`notes`. A cost derived but not independently checked is a result awaiting
verification, not an established one; say which it is.

## What this deliberately does not do

- **It does not search for the best attack.** One hop, one reduction. Breadth
  is a different job and an unbounded one.
- **It does not trust an estimator to know whether its attack applies.** An
  estimator prices what you ask it to price.
- **It does not treat an abstract as a parameterisation.** Identifying a
  reduction and instantiating it are different steps with different evidence
  requirements.

## Publish as you go

You are the one doing the research, so you are the one who surfaces it. The
connectors keep state current on disk; they cannot call `save_artifacts` and it
would be wrong if they could. **Publishing is part of the work, not bookkeeping
after it.**

Follow the current host artifact interface and
`investigate/reference/claude-science.md` for version identity. Do not infer
versioning from a repeated filename or impose a publish-after-every-write rule
on the host. Workspace knowledge and persistence are managed by the harness.

Publish when it changes, not once:

- **the plan** — it is live and needs no publishing; keep it current with
  `update_step_status` at the start and end of every step. That replaces what
  used to be a publish cycle here, and cannot drift the way a rendered file did.
- **anything you generate that a person would want to look at** — a cost table
  across parameter sets, a figure, a scheme's extracted structure, the mapping
  from a paper's symbols onto estimator arguments.

Measured on 2026-08-02: the ledger's state file ran **20 hours ahead** of its
rendered view, because publishing was left to memory. A day of real work — a
claim parked, revived, and given new paper evidence — existed only in a file
nobody looks at. Work the human cannot see has not been delivered.

**A tool-carrying specialist publishes its own work; you publish the synthesis.**
Measured, after the question was left open once and then answered:
`CRYPTO_VERIFIER` wrote four artifacts from three frames of its own — figures and
CSVs from its verification runs. So do not re-publish what it already published.

`REVIEWER` is the opposite case and it is what misled an earlier version of this
note: it has produced zero artifacts, because it has no execution at all. Absence
of artifacts from an agent with no tools says nothing about agents with tools.

What stays yours: the synthesis. A specialist publishes its evidence; the answer
that cites it, and the ledger state that records it, are the delegator's.
