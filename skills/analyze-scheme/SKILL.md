---
name: analyze-scheme
description: Produce an attack-surface map for a cryptographic scheme — name the hard problem it rests on, extract exact parameters, gather what is already known against that problem, inventory the structure its trapdoor adds, cost every applicable attack family against a named model, compare to the claimed level, rank the ways it deviates from the canonical construction, and say where an attack would improve. Use when assessing a new or modified scheme, checking whether a parameter set meets its claimed NIST category, reviewing a submission that proposes a construction, deciding where cryptanalytic effort is best spent, or supplying the structural baseline for an explicit discovery investigation. Covers lattice (LWE/NTRU/SIS), multivariate (UOV/MQ/MinRank), and symmetric/hash targets.
---

# Analyzing a scheme

Produces an **attack-surface map**, not a verdict. The output is something a
cryptographer steers. In an ordinary assessment, the one judgement it never
makes on its own is step 7. An explicit **DISCOVER** request authorises the
bounded selection rule in `discover-cryptanalysis`; it does not authorise
unbounded pursuit or expensive compute.

Three questions organise it, and they are asked in this order because each
constrains the next:

> **What hard problem does this rest on?** (§1–2)
> **What is already known against that problem?** (§3–5)
> **Where is the margin thin, and what would an attack exploit?** (§6–8)

If the user says only “analyze this scheme,” ask once whether they want this
bounded attack-surface assessment or a DISCOVER run that continues into new
candidate generation. Do not infer the more open-ended stopping rule from that
phrase alone. An explicit mode or clear “verify/check” versus “find new/transfer”
language settles the choice.

## Which object are you evaluating?

A scheme is several objects and a finding about one is not a finding about
another. Name which layer you are on before answering anything:

| layer | the question |
|---|---|
| **primitive** | is the hard problem, permutation, or curve sufficiently understood? |
| **construction** | does the composition satisfy the intended notion? |
| **parameter set** | do these parameters withstand the best known attacks at the claimed level? |

Keeping them apart prevents three category errors that recur in this domain:

- **A distinguisher against an underlying permutation is not a break of the
  construction.** Say what property was violated and what follows for the whole.
- **An attack on reduced rounds is evidence about margin**, not an attack on the
  full algorithm.
- **A proof about the construction does not prove the primitive secure**, and the
  reverse.

Two further layers — **implementation** (constant-time behaviour, faults,
leakage) and **deployment** (nonce handling, key lifecycle, multi-user, protocol
composition) — are real and **out of scope here**. This workbench does not touch
them. If a question turns on one, say so rather than answering it from the map.

## The three rules

**1. Never compute anything yourself.** Every number comes from an estimator or
from Sage. Models get `44² mod 187` wrong; this is measured, not hypothetical
(`docs/ROADMAP.md` §3, class 1). If you find yourself doing arithmetic, stop and
run it.

**2. Check a family's preconditions before running it, and report the ones that
fail.** The characteristic failure in this domain is applying a known attack
without verifying its hypotheses hold (§3, class 3). `scripts/sweep.py` treats
an exception as a *result* — "MITM needs 728 samples, has 512" is a finding
worth reporting, not an error to swallow.

**3. Never say "secure", "verified", or a bare λ.** Say which family is
cheapest, under which cost model, and what was not checked. The failure mode a
human-steered tool amplifies is fluent prose over unverified reasoning (§3,
class 5) — and the paper that measured it found those flaws are *hard for human
experts to catch*, so the reader is the weak link, not the backstop.

---

## Plan first, if this is multi-stage

A full attack-surface map is a pipeline, and that is exactly the shape `generate_plan` is for:
parallel directions become `delegations` in a phase, and the human approves the
approach once instead of discovering it at the end.

**But every plan blocks on approval**, so skip it for a single family check or one estimator run.
The threshold, the schema, `update_step_status`, and how to amend a plan without
discarding it are all in `investigate` §1b — follow that rather than a second
copy of the rule here.

## Step 1 — Name the hard problem

Before any parameter, say what breaking this scheme is supposed to require.
Getting this wrong invalidates every number downstream, and it is a different
failure from a mistyped parameter: a wrong problem produces a *coherent* analysis
of the wrong thing.

- Which standard problem, and is the reduction to it **tight, loose, or folklore**?
- Is the scheme's problem the textbook one, or a **variant**? Module-LWE is not
  LWE; UOV with subfield coefficients is not UOV. The variant is usually where
  the attack surface is.
- If the reduction is to a problem nobody costs, that is `derive-cost`.
- If the reduction is claimed by a paper and you are auditing that claim, that is
  `analyze-paper`.

**Obligation:** state the problem, the variant, and how you know — a normative
document, a paper you opened, or a recorded knowledge entry.

## Step 2 — Extract exact parameters

Do not infer a parameter from a related one; a transcription error here
invalidates everything downstream.

| Problem | Parameters needed |
|---|---|
| LWE / Module-LWE | n, q, m, secret and error distributions (and η if binomial) |
| NTRU | n, q, and the secret distribution — plus whether q is *overstretched* |
| SIS | n, q, m, **norm bound β and which norm** (ℓ₂ vs ℓ∞ — the estimator defaults to ℓ₂ and ML-DSA states ℓ∞) |
| UOV-like | n (variables), m (equations), q |
| MQ | n, m, q, and whether the system is square or underdetermined |
| Block cipher / permutation | block size, S-box, linear layer, rounds, key schedule |

For a standardised scheme, take parameters from the **normative text**, not from
memory or a summary — `nist-mcp_csrc_fulltext("FIPS 203", "parameter sets")`.

**Obligation:** state where each parameter came from.

## Step 3 — What is already known against it

Ask this **before** costing anything. The cheapest possible outcome is that the
attack already exists and is on disk, and costing a family from scratch when a
published result covers it is the most common waste in this loop.

```
nist-mcp_search_csrc("<scheme>")        the round-status reports, one section each
nist-mcp_csrc_fulltext(ref, query)      read what NIST said and why
firecrawl-mcp_firecrawl_search          pqc-forum, comments, announcements
e-print-mcp_search_eprint("<scheme> attack")
```

**A miss means "no source carried here", never "unbroken".** The corpus covers
schemes an upstream benchmark marks solved — mostly first-round SHA-3, CAESAR,
LWC and PQC submissions. LUOV is absent from it and was broken. On a miss, ask
the `nist` connector: IR 8240 / 8309 / 8413 / 8528 / 8610 carry one section per
candidate saying what happened to it and why.

That pairing exists because the corpora have complementary blind spots. `eprint`
holds papers; a large fraction of competition cryptanalysis was never a paper.
The status reports hold the narrative; none of it appears in any title or
abstract, so it is invisible unless the full text is cached.

Then the literature, on the **problem** as well as the scheme:

```
e-print-mcp_search_eprint("<scheme name>")            the synonym table handles renames —
e-print-mcp_search_eprint("<hard problem> attack")    searching Kyber finds ML-KEM
e-print-mcp_eprint_fulltext(paper_id, query)          the body; an abstract is not a result
```

Check `nist-mcp_csrc_currency` if a NIST document is involved; a superseded standard is a
different claim.

**Obligation:** state what was searched and how completely. A negative here is a
claim about the search, not about the world.

## Step 4 — Inventory the structure

> **Structure is attack surface.** Every trapdoor is something the designer
> *added* so the key holder can invert. Every addition is a handle.

List what was added and why:

- the trapdoor itself (oil subspace, short basis, NTT-friendly ring, …)
- distribution choices made for performance — sparse secrets, small or bounded
  error, low-entropy noise
- ring and modulus structure — does `x^n + 1` split fully mod q? Check it, do not
  assume (`reference/sage-idioms.md` in the `validate-attack` skill; for ML-KEM it
  splits into **128 degree-2 factors, not 256 linear ones**, which is why its NTT
  is incomplete)
- any parameter pushed to an extreme for performance — especially a **large q**

This step feeds steps 7 and 8. Write it down even when nothing looks exploitable.

## Step 5 — Cost the applicable families

One step, three obligations, in order. The gate comes first because skipping it
is how the most dangerous number in this repo's history got produced.

### 5a. Admissibility — can the estimator express your target?

> **An estimator that accepts your parameters has not thereby agreed to model
> your scheme.**

Write down the object the estimator *actually modelled* and diff it against what
you inventoried in step 4. Every constructor encodes assumptions its argument
list cannot express, and it will not tell you when they are violated — it returns
a confident, internally consistent number for a different scheme.

| Estimator | Silently assumes | Violated by |
|---|---|---|
| `UOVEstimator(n,m,q)` | oil dimension = m; a **single layer**; public map uniform over F_q | **Rainbow** (oil dim = o₂ < m), **LUOV / QR-UOV** (coefficients in a proper subfield), MAYO, SNOVA |
| `MQEstimator(n,m,q)` | a generic system; semi-regularity for degree-of-regularity | any structured or lifted central map |
| `LWE.Parameters(...)` | the distributions you passed, and **m samples you declared** | schemes with ciphertext compression, asymmetric Xs/Xe, or reused keys |

This gate is why the blind regression's most dangerous number appeared: at
Rainbow-I's shape `UOVEstimator` reports `IntersectionAttack at 2^22.1` — four
million operations — with no complaint, because it silently modelled a
single-layer scheme. `sweep.py` now warns on both counts, but **the warning is
not a substitute for doing this step.**

Two rules that follow:

- **A sub-2^64 result on anything claiming a NIST category is a modelling error
  until proven otherwise.** Do not report it as a break.
- **A family that rewrote your instance did not cost your instance.** `coded_bkw`
  will happily consume 2^166 samples against the 512 you declared and return a
  number for that other problem.

### 5b. Walk every family, preconditions first

Consult the checklist for the problem class:

- `reference/lattice.md`
- `reference/multivariate.md`
- `reference/symmetric.md`

Then run the sweep. **`DOT_SAGE` is not optional here** — see below:

```bash
# Sage and cryptographic_estimators must be on the machine running this skill;
# they are not part of the research MCP server. Adjust both paths to your setup.
export DOT_SAGE=${DOT_SAGE:-~/.sage_home}      # a WRITABLE Sage home -- see below
SAGE=${SAGE:-$(command -v sage)}
$SAGE --python scripts/sweep.py lwe ML-KEM-512
$SAGE --python scripts/sweep.py lwe n=512 q=3329 eta=3 m=512
$SAGE --python scripts/sweep.py uov ov-Ip
$SAGE --python scripts/sweep.py mq n=112 m=44 q=256
```

**Without `DOT_SAGE`, `import estimator` fails before it computes anything**, with
a traceback that looks like a broken Sage install rather than an environment
problem:

```
File ".../sage/misc/misc.py", line 71, in <module>
  os.makedirs(DOT_SAGE, mode=0o700, exist_ok=True)
FileExistsError: [Errno 17] File exists: '/Users/<you>/.sage/'
```

`exist_ok=True` raises only when the path exists and is not a directory. From a
terminal `~/.sage` is an ordinary directory and this never happens; inside the
app's bash it does. Same family as a PDF-extraction helper hard-coding absolute
`POPPLER_PATHS` — **the app's execution environment is not your terminal's**, and
a thing that works in one can fail in the other. The workbench keeps a writable
Sage home under the granted path for exactly this. Measured 2026-08-04 in the
FN-DSA run, which lost two calls to it.

It sorts applicable families by cost, reports every precondition failure with
its actual message, and fires two warnings automatically — when a dual attack is
cheapest, and when F5 is far above the cheapest MQ family.

**Symmetric has no estimator.** You build a MILP or SAT model and solve it. Use
`scripts/present_milp.py` from the `validate-attack` skill as the template, and
**reproduce a published bound before trusting your model** — a model missing its
propagation constraint returns a clean, confident, entirely wrong answer.

**Obligation:** report the families that did *not* apply, and why. That list is
evidence the sweep was complete.

### 5c. Report with a named model, and memory

Never a bare λ. For lattice, report the cost-model spread — ADPS16, MATZOV,
BDGL16 differ by 25+ bits on the same instance, and CheNgu12 prices a different
algorithm family entirely. Quote **ADPS16** when comparing against a NIST
submission's own claim, since core-SVP is the convention those use.

**Report memory alongside time.** UOV's CollisionAttack wins ov-Is on time at
2^141.0 while needing 2^131.7 memory.

**Obligation:** model named, spread given, estimator commit and Sage version
recorded — the sweep prints provenance for this reason.

## Step 6 — Margin against the claim

Compare the cheapest applicable attack to the claimed level.

For a NIST category claim, consult the `analyze-paper` skill's
`reference/nist-categories.md` before doing anything else. Four traps live there:
the pegs are computational-resource comparisons under **all** metrics NIST deems
relevant, not bit counts; those pegs are estimates that have been revised;
category claims **have been withdrawn in practice** (IR 8413 records category-5
claims called into question during round 3); and "security category" is
overloaded — FIPS 199 uses it for information-system impact levels.

**MAXDEPTH:** every CFP quantum threshold is depth-divided. A quantum cost
without a MAXDEPTH assumption is not comparable to the threshold.

## Step 7 — Rank the deviations *(this is the collaborative step)*

Where the research is. The selected investigation mode determines what follows.

Compare against the canonical construction and rank each deviation by how much
structure it adds. For each, ask **what does this buy an attacker** — and check
whether it triggers a family that is dormant for the canonical scheme:

| Deviation | Family it wakes |
|---|---|
| sparse or small-support secret | `primal_hybrid`, `dual_hybrid` |
| bounded / low-entropy error | `arora_gb` |
| large q relative to n (NTRU) | `primal_dsd` — overstretched regime |
| unlimited samples (key reuse) | `coded_bkw`, `mitm` |
| underdetermined MQ system | `Hashimoto` |
| small field | `CollisionAttack`; the Boolean-only MQ families |
| low-rank structure in the public map | MinRank |

In **VALIDATE** or an ordinary assessment, present these ranked, with reasoning,
and **stop**. The human decides which are worth pursuing. Do not assert that a
deviation is harmless.

In **DISCOVER**, record the complete ranked list in the candidate artifact and
continue through `discover-cryptanalysis`. That skill may cheaply falsify every
viable candidate and pursue at most the strongest two under the standard budget.
It must preserve the unselected candidates rather than silently dropping them.

## Step 8 — Where would an attack improve?

The map says what the best *known* attack costs. This step asks what a better one
would need — and it is the reason to do the analysis rather than read a summary.

Three prompts, each answerable from what steps 4–7 produced:

- **Can a deviation specialise a generic family?** Step 7 says which family a
  deviation wakes. The next question is whether that family, *specialised to this
  structure*, beats the generic cost. That is where new cryptanalysis usually
  comes from.
- **Where is the largest gap between the generic and structured attack?** A big
  gap means the structure is either carrying a lot of security or hiding a lot of
  attack surface, and nobody knows which without looking.
- **What is assumed rather than computed?** A semi-regularity assumption, a
  heuristic success probability, an unevaluated constant. Each is a place the
  real cost may differ from the estimated one in either direction.

**Mark everything here as conjecture, explicitly.** This step produces hypotheses,
not results, and the distance between them is the whole point of the workbench.
A hypothesis worth pursuing goes to `discover-cryptanalysis`, which makes the
transfer and falsification obligations explicit before handing a concrete attack
to `validate-attack` or an uncosted reduction to `derive-cost`.

---

## Output format

```
SCHEME      <name>, <parameter set>
PROBLEM     <hard problem>, which variant, and how you know
PARAMETERS  every value, and where each came from

KNOWN       prior breaks, status-report findings, literature
            what was searched, and how completely

STRUCTURE   what the trapdoor adds

FAMILIES    cheapest first, with cost model named
            families that did not apply, and why

MARGIN      cheapest attack vs claimed level; category caveats if relevant

DEVIATIONS  ranked, with the family each wakes        <- for the human
IMPROVEMENT where an attack would get better          <- conjecture, labelled

NOT CHECKED  <- mandatory, never empty
PROVENANCE   Sage version, estimator commits
```

**`NOT CHECKED` is mandatory.** Every analysis has gaps — a family whose
preconditions could not be evaluated, a Gröbner claim needing Magma, an
implementation not run. An empty `NOT CHECKED` means the analysis was not
examined, not that it was complete.

**But `NOT CHECKED` is not a `add_gap`.** It records this run's budget and
tooling, not something about the scheme: someone with a Magma licence and more
hours has a different list, so it is false on their machine. It belongs in the
answer and in the plan.

A family you **did** evaluate and ruled out is the opposite, and it is worth a
gap — say which precondition failed and at what parameters, because that is what
saves the next session the same check:

```python
add_gap(question="Does <family> apply to <scheme> at <params>?",
        looked_in=["estimator", "ePrint", "NIST"],
        finding="Ruled out: <precondition> fails — <the number that settles it>.")
```

The rule behind the split: **a gap records what was learned by looking. If
nothing was learned, it is a to-do.** The distinction is load-bearing because the
next session reads a gap as *this door was checked and is shut*; filing an
unexamined family as a gap would stop someone looking at a family nobody has
examined. See `discover-cryptanalysis` for the same rule across its eight
headings.


---

## What this skill does not do

- **Decide whether a scheme is secure.** It maps attack surface.
- **Audit a proof.** That is `analyze-paper`, and it is mostly not computational.
- **Run an attack.** That is `validate-attack`. Estimation is not demonstration,
  and a cost estimate is not a break.
- **Evaluate an implementation or a deployment.** Out of scope — see the layer
  table at the top.
- **Compute a degree of regularity.** The semi-regular figure is an *estimate*
  and `MQEstimator` assumes it. Confirming a real system is semi-regular needs an
  actual Gröbner run — see the Magma note in `reference/multivariate.md` and
  `TODO.md`.

## Publish as you go

You are the one doing the research, so you are the one who surfaces it. The
connectors keep state current on disk; they cannot call `save_artifacts` and it
would be wrong if they could. **Publishing is part of the work, not bookkeeping
after it.**

Re-saving the same filename does **not** create a second artifact — it adds a
*version*, and the interface presents those as history. Every publish is a frame
in the investigation's timeline, so **publish after every write**: forty-eight
versions across a run is the good outcome, not churn, because it lets a reader
scrub back to what the state looked like before a claim moved. Publishing
sparingly throws that away.

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
