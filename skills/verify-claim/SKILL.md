---
name: verify-claim
description: Settle one security claim — restate it precisely enough to be checkable, establish how it was obtained, pick the route that actually settles it (open the source, reproduce the computation, run it at toy scale, or discharge the notion's obligations), and report it supported, refuted or unresolved. Use when a claim is load-bearing and a decision depends on whether it holds.
license: Apache-2.0
---

# Settle one claim

When invoked directly by “verify,” “reproduce,” “audit,” “check whether,” or
equivalent language, start the answer with `MODE: VALIDATE`. When a DISCOVER
investigation hands over a frozen survivor, preserve `MODE: DISCOVER` and label
this work as its independent-validation phase. In either case, do not expand
from the supplied claim into a search for neighboring attacks.

You are handed a claim and asked whether it holds. **One claim, deliberately** —
working out *which* claims in a body of work are load-bearing is `analyze-paper`'s
job, and merging the two turns a bounded check into an unbounded one.

Two questions, in that order:

> **Where did this come from, and can I get it again?**
> **What would settle it, and is that cheaper than assuming?**

A claim traced to a paper that was opened, a command that was run, or a knowledge
base entry that was retrieved is **supported**. A claim that arrived because the
analyst knew it is **unsupported**, however true it happens to be. A claim that
arrived through a new derivation is a **candidate**: writing down the reasoning
gives it provenance, but does not independently check it. That distinction does
most of the work here: an unsupported claim that is right this time is
indistinguishable, from the inside, from one that is wrong, and a derivation
reviewed only by its author still has the author's blind spots.

**Retrieval is a pass, not a shortcut.** If `knowledge.md` already answers it, that
is the workbench working — the four tiers exist so that settled things are looked
up rather than re-derived. Nothing here penalises using them. What it penalises
is asserting without them.

## Which skill this is

- **`verify-claim`** — one claim, settled. Any kind: a cost, a notion, an
  attribution, a negative.
- **`analyze-paper`** — a whole document, and which of its claims are worth
  settling. It hands work to this skill.
- **`validate-attack`** — the claim is specifically that an attack works.
- **`derive-cost`** — nothing has costed the target and a number is needed.
- **`crypto-review`** — whether the *reasoning* is sound, not whether the claim is.

## Why this replaces the blind test

An earlier design (E4) hid an answer key and scored whether the analyst *derived*
rather than *recalled*. Two things killed it. The knowledge base had by then
accumulated the answer verbatim, so retrieving it — the correct behaviour — was
scored as cheating. And per `docs/ROADMAP.md` §1, a thing that hides information
to score an agent is a benchmark; this project is a workbench, which surfaces
information to amplify a person. Hiding nothing measures more, burns no targets,
and can run on real work rather than a staged artifact.

## Plan first, if this is multi-stage

Settling one claim usually is not, and **most of the time no plan is needed here**
— that is the point of the skill being bounded to one. Reach for `generate_plan`
only when a batch arrives from `analyze-paper` and the claims can be settled in
parallel: they become `delegations` in a phase, and the human approves the
approach once instead of discovering it at the end.

**Every plan blocks on approval**, so a single number reproduced from one command
should never get one. The threshold, the schema, `update_step_status`, and how to
amend a plan without discarding it are all in `investigate` §1b — follow that
rather than a second copy of the rule here.

## Step 1 — Restate the claim precisely enough to be settled

A claim as received is usually not checkable. "ML-KEM-512 is category 1" has no
truth value until you say under which metric, against which peg, and at which
revision of the peg. **Restating is not a formality — it is where most claims
turn out to be two claims, or none.**

First, is it load-bearing? A claim is, if a decision changes when it is false. In
this domain that is reliably:

- **numbers** — attack costs, security levels, memory, probabilities, degrees
- **parameter sets** — any `(n, m, q, r)` tuple, any named parameter set
- **attributions** — "X broke Y", "paper Z shows", "the standard says"
- **applicability** — "this attack applies", "the precondition is met"
- **negatives** — "no such paper exists", "the estimator has no model for this",
  "this is not in the corpus"

Negatives are the most frequently wrong of these. See failure mode 5.

Then pin down what would make it true or false:

- **the notion and the model**, if it is a security claim — "IND-CCA2" alone is
  incomplete, and ROM and standard-model versions are different claims. The
  `analyze-paper` skill's `reference/` set states each notion as obligations to
  discharge rather than prose to cite.
- **the cost model and unit**, if it is a cost. A bare exponent is not a claim.
- **the exact parameters** it is asserted about, not the ones nearby.
- **what was searched, and how completely**, if it is a negative.

If the restatement cannot be written, stop and say so. An unstatable claim is a
finding, and it is the cheapest one available.

## Step 2 — Establish how it was obtained

| tag | meaning |
|---|---|
| `[SOURCE]` | a document was opened **this session** — cite file and page, or the retrieval call |
| `[TOOL]` | a command was run this session — cite the exact invocation |
| `[KB]` | retrieved from the knowledge base or ledger — cite the entry id |
| `[DERIVATION]` | a new argument was worked this session — cite the candidate artifact and state its assumptions; this is candidate provenance, not independent support |
| `[RECALL]` | asserted from knowledge, with no retrieval and no computation |

`[RECALL]` is not forbidden. It is *flagged*, and for a load-bearing claim it must
be converted to `[SOURCE]` or `[TOOL]` before the work is acted on.

`[DERIVATION]` is not `[RECALL]`: it exposes a checkable chain of reasoning. But
it is not `[TOOL]` merely because some algebra was typed into a notebook. A tool
run supports exactly the finite computation it performed; it does not
independently establish the general argument that selected or interpreted that
computation.

The classification comes from the **transcript**, not from the prose. A sentence
that reads like a citation is not a citation; look for the tool call.

## Step 3 — Pick the route that actually settles it

Reproducing a number is one route, not the definition of the work. Match the
route to what the claim rests on:

| the claim rests on | settle it by |
|---|---|
| a computation someone ran | **reproduce it** — run the command the document says produces it |
| what a document says | **open the document** — `e-print-mcp_eprint_fulltext`, `nist-mcp_csrc_fulltext`, the body not the abstract |
| a definition being met | **discharge the obligations** — the `analyze-paper` skill's `reference/` set lists them per notion |
| an attack working | **hand it to `validate-attack`** — which decides whether analysis or code settles it |
| a cost nobody has computed | **hand it to `derive-cost`** |
| a new theoretical derivation | **check it by an independent route** — independent re-derivation, proof audit, computation, or human review |
| something not existing | **name the channels searched** — a negative is a claim about the search |

When the route *is* reproduction, two checks catch most of what goes wrong:

- **Does any command produce this number at all?** A figure with no generating
  command is unsupported no matter how plausible.
- **Do the inputs match the claim's inputs?** A number computed for one parameter
  set and reported for another is the single most common real defect here.

Pick the cheapest route that would actually change your mind. A route that cannot
refute the claim is not settling it, it is confirming it.

For a new derivation, make independence concrete. Give the checker the exact
claim, target definitions, assumptions, and candidate artifact, then ask it to
find the shortest refutation or check the argument through a separate route.
`CRYPTO_VERIFIER` may do this in a fresh delegation. It must not repair a missing
step, strengthen a weak lemma, or optimise the proposed attack: a gap is a failed
check, not an invitation to co-author a better candidate.

Record the original reasoning as `derivation` evidence and the separate result
as `independent-check` evidence. The latter names which route was used and what
was actually checked. Reading the same conclusion twice, or having the author
rephrase it, is not independent. Prior art can support ingredients, but it does
not check a new inference unless it establishes that exact inference under the
same assumptions.

## Step 4 — Work the failure taxonomy

These are not hypotheticals. Every one is drawn from work in this repository, and
each cost real time or shipped a wrong answer.

**1. Uncited recall of reference data.** Parameter tables, published costs, which
scheme a name refers to. *Observed:* a probe's "fresh" parameters were a
published LUOV set, asserted from memory and never checked; the same class of
error recurred a second time on the same file. **Check:** every parameter tuple
and published figure carries `[SOURCE]`.

**2. Over-correction from a partial source.** Treating one document as exhaustive
and overturning a true statement with it. *Observed:* a correct claim that LUOV
round 2 used prime `r` was "corrected" to composite on the strength of a version
of the paper that omits the table showing both — arriving with more confidence
than the original error. **Check:** before overturning a prior claim, establish
that the new source is *complete* for that question. Prefer the archival version
over a conference version; they differ.

**3. Stale derived numbers after an input change.** *Observed:* changing a
parameter set and recomputing some outputs but not others left a key-recovery
figure 10.2 bits wrong, inside a rubric with a ±0.5 tolerance. **Check:** when an
input changes, re-run *everything* downstream, not the numbers you remember
depending on it.

**4. Unit or model mismatch in a comparison.** *Observed:* "the structure costs
60 bits" subtracted a field-multiplication count over `F_8` from a bit-operation
count over `F_4096`. **Check:** every difference of two costs states the unit and
the cost model of both. A bare exponent is not a result.

**5. A negative concluded from an incomplete look.** *Observed three times in one
session:* "the repo has no attack references" from a sparse checkout that never
pulled `solution/`; "the paper body is unreachable" from one host's `robots.txt`
when another host served it; "the corpus does not cover this" when the full-text
cache held 9 of 924 documents. **Check:** a negative must name what was searched
and how completely. "Not found in X" is a claim about X.

**6. Discarding the diagnostic you already had.** *Observed:* a fetch returned
HTTP 403 and the script kept the status code and threw away the response body.
The body was the Cloudflare interstitial, which would have said the challenge was
never solved. Instead "403" was reported as a bare fact and written up as a
property of the *publisher* — when it was a property of the script's control
flow. Three further "403" rows in the same table inherited the error.

**Check:** when something fails, keep what it said. A status code without its
body, an exception without its message, a non-zero exit without stderr — each is
a diagnosis discarded at the moment it was free. This is worse than failure mode
5: there the evidence was never gathered; here it was in hand and destroyed.

**7. Verification that shares the asserter's sources.** *Observed:* an
adversarial review refuted 19 findings of 19; two were correct, one fatally. The
refuter had no channel the author lacked. **Check:** a verifier must open a
source the author did not. A second opinion from the same library is not
verification.

**8. Silent aggregate failure.** *Observed twice:* one estimator family raising
discarded eight valid results, and the failure formatted as a tuple rather than
an error. **Check:** any "cheapest of N" states what was skipped. A minimum over
a silently reduced set is a lower bound wearing an answer's clothes.

## Step 5 — Report

One of three verdicts, and the third is a real answer:

- **supported** — with the route that settled it and the evidence it produced
- **refuted** — with the same
- **unresolved** — with **what would settle it and why that was not done**

Do not round `unresolved` to true or false. Forcing uncertainty into a verdict is
how the 19-of-19 refutation happened, and an unresolved claim with a named next
step is more useful than a confident wrong one.

A new theoretical claim carrying only `[DERIVATION]` is `unresolved` as a claim
and remains a candidate in the discovery artifact. It can become `supported`
only after an independent re-derivation, proof audit, computation, or human
review checks the same claim. A failed cheap falsifier may refute it immediately;
independence is a gate for promotion, not a reason to preserve a dead candidate.

Report the restatement alongside the verdict. A claim settled in a form nobody
else would recognise has not been settled for them — and if the restatement
turned one claim into two, say so and give a verdict for each.

When several claims came from one `analyze-paper` pass, a summary line helps:

```
claims settled       n of N
  supported / refuted / unresolved   n / n / n
  [RECALL] converted to [SOURCE]|[TOOL]   n
```

**The list is the deliverable**, not the rate — a single unsupported parameter set
matters more than a high percentage.

## Step 6 — Write back

Facts that had to be retrieved once should not be retrieved again from scratch:

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
from knowledge import add_entry, add_gap
add_entry(statement=…, kind="…",
          evidence=[
              {"kind": "derivation", "ref": "<discovery artifact>#C2",
               "note": "Original argument, assumptions, and notation map."},
              {"kind": "independent-check", "ref": "<verifier report>",
               "note": "Fresh proof audit checked C2 without repairing it."},
          ])
add_gap(question=…, looked_in=[…], finding=…)
```

See `workbench-knowledge`. These **append** — never rewrite those files, and
never reach for `edit_file` to add a record: concurrent writers lose entries
that way (measured, 1193 of 1200).

`looked_in` is a list of **channels**, not a mood. "Searched ePrint" and "searched
ePrint, the NIST corpus, and the web" are different findings,
and the second is the one that licenses a negative.

Do not write a derivation-only candidate to durable knowledge. Keep it in the
live plan and the versioned discovery artifact until the `independent-check`
record exists. Ordinary sourced facts retain their existing evidence rules; this
extra gate applies when the claimed result is newly derived.

## What this deliberately does not do

- **It does not decide which claims matter.** It takes one. Working out what a
  document's load-bearing claims are is `analyze-paper`, and keeping them apart is
  what keeps this bounded.
- **It does not judge whether the analysis is good.** A well-sourced wrong
  conclusion still fails review; that is `crypto-review`'s job.
- **It does not promote a derivation by repeating it.** New theoretical work
  needs a genuinely separate checking route before it becomes durable knowledge.
- **It does not require deriving what can be looked up.** Retrieval is the
  designed path.
- **It does not report "verified".** Computation falsifies; it does not verify.
  For a claim settled by running something, the vocabulary is "no counterexample
  at n ≤ N", with N stated.
- **It does not hide anything.** There is no answer key, nothing is scored
  against a secret, and the same work can be audited repeatedly without being
  spent.
