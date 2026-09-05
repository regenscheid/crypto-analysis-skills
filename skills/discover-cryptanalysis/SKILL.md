---
name: discover-cryptanalysis
description: Actively search for new or previously missed cryptanalytic weaknesses by combining a complete attack-surface map, independent structure-first reasoning, prior-art extraction, cross-field transfer, proof and interface seams, falsifiable candidate generation, cheap disproof, costing, and independent validation. Use whenever asked to find issues, look hard for weaknesses, search for new attacks, improve known attacks, investigate unexplored directions, or transfer techniques to a cryptographic target. Do not stop at literature review or vague ideas.
---

# Discover cryptanalysis

Start with `MODE: DISCOVER`. Produce falsifiable attack candidates and scoped
negative results—not novelty, break, or security verdicts.

Use `investigate` as the control plane and `analyze-scheme` when the target lacks
a frozen claim set, structure map, generic baselines, and attack-family coverage
ledger.

## Fix the objective

Record:

- exact target layer, version, parameters, distributions, and round scope;
- security notion, attacker powers, oracle model, and quantum model;
- desired consequence: recovery, forgery, distinguishing, collision, inversion,
  failure exploitation, proof separation, or concrete cost reduction;
- best generic and known baselines under named models;
- excluded implementation or deployment surfaces.

Do not silently turn a primitive property, reduced-round result, weak-key case,
or model-specific distinguisher into a full-construction break.

## Route before ideating

Load the appropriate domain orchestrator and its structure mapper, claim
formalizer, hypothesis generator, transfer skill, cost auditor, and reproduction
planner. Use the domain-qualified workflow names for shared capabilities:

- symmetric workflows begin with `symmetric-`;
- public-key workflows begin with `public-key-`.

Then load every applicable technique skill identified by the orchestrator. Keep
excluded techniques in the coverage ledger with the failing precondition.

## Run independent search tracks

Keep these tracks independent until each produces evidence or candidates:

1. **Prior art** — start immediately and load the domain literature extractor;
   cover the exact scheme, former names, components, assumptions, failed
   approaches, corrections, code, standards records, and non-paper sources.
2. **Structure first** — objects, maps, ranks, distributions, invariants,
   symmetries, sparsity, locality, repetition, failure events, and departures
   from canonical constructions without starting from attack names.
3. **Transfer** — mechanisms from adjacent mathematical, optimization,
   coding-theory, solver, program-analysis, and protocol literature. Read
   [`reference/transfer.md`](reference/transfer.md) before this track.
4. **Proof and interface seams** — reduction losses, model gaps, encodings,
   validation, rejection behavior, malleability, multi-user effects, and
   composition boundaries.

Search misses must name channels, queries, aliases, dates, and unavailable
sources. They never license “novel,” “unbroken,” or “no prior work.”
The structure-first track may proceed in parallel to avoid anchoring, but it
cannot substitute for the prior-art track or close its completion gate.

## Maintain candidates

Use no more than five mechanism-distinct viable candidates in a standard run
and pursue at most the strongest two. Keep fewer when fewer survive; never add
filler or count parameter variants as different mechanisms.

For each candidate, record:

1. stable ID, target, and mechanism;
2. structural handle and source result, if any;
3. complete notation or object mapping;
4. required preconditions, each satisfied, failed, or unchecked;
5. predicted consequence and exact scope;
6. cheapest decisive falsifier and its result;
7. preliminary time, data, memory, success, and verification costs;
8. provenance, confidence, next action, and unblock condition.

Use the statuses in `investigate/reference/completion-contract.md`. A candidate
cannot survive while a critical precondition is unchecked or while its cheapest
falsifier exists only as a plan. Park it honestly when budget or access prevents
the test.

## Falsify before developing

Try, in order:

1. type, dimension, direction-of-reduction, security-model, or scope checks;
2. source preconditions instantiated at the real parameters;
3. tiny positive cases and negative controls;
4. bounded estimator, algebra, SAT/SMT, MILP, exhaustive, or simulation tests;
5. deeper derivation, implementation, or formal proof only for survivors.

Reject transfers that preserve vocabulary but not the operation used by the
source result. Preserve clean falsifications: the obstruction is reusable
cryptanalytic knowledge.

## Hand off survivors

- Use `derive-cost` when the mechanism is concrete but unpriced.
- Use `validate-attack` when applicability or execution is the disputed claim.
- Use `analyze-paper` when the transferred source may prove less than attributed.
- Use `formal-methods-router` when a narrow universal, equivalence, finite-search,
  implementation, probability, or reduction obligation justifies it.
- Use `verify-claim` or an independent implementation to challenge every
  load-bearing survivor without repairing it during review.

Freeze the candidate before independent checking. A checker that paraphrases or
improves the original derivation is not independent evidence.

## Completion gates

Do not stop because the known literature was recovered, one promising direction
was found, or one favorite technique failed. Complete the applicable family
ledger and source-grounding record, attempt the cheapest falsifier for every
viable candidate, and hand off the strongest survivors for bounded costing or
validation.

Stop with a scoped partial result when remaining work is blocked or deliberately
outside budget. State the exact unblock condition and next decisive experiment.

## Contribution labels

Before reporting a candidate as new, read
[contribution assessment](../investigate/reference/contribution-assessment.md).
Identify the closest known result and the additional reasoning. Applying an
unchanged known argument to a different parameter set is a routine application,
even if that case was absent from the sources searched. Report its significance
without claiming a new mechanism. An extension outside the source's assumptions
remains unresolved until the additional obligation is met.

## Output contract

Return:

1. target, objective, models, and baselines;
2. skill trace and complete coverage ledger;
3. independent search-track results;
4. structural handles;
5. full candidate records, including falsified and parked candidates;
6. surviving candidates and independent-check status;
7. relationship to prior work, additional contribution, and novelty-search limits;
8. unchecked areas and prioritized next work.

Do not force a positive result. A rigorous map of attractive directions and the
specific reasons they fail is successful discovery work.
