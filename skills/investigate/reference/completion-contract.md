# Investigation completion contract

Use this contract to prevent premature or invisible completion.

## Skill trace

Record only skills whose bodies were loaded and whose procedures materially
affected the work.

| Order | Skill | Why selected | Product or decision |
|---:|---|---|---|
| 1 | `investigate` | End-to-end cryptographic investigation | Mode and routing |

Do not list a skill merely because it was installed or mentioned by another
skill. If the runtime exposes skill-call identifiers or transcripts, retain them
with the research artifact.

## Coverage ledger

Create one row for every technique family selected or considered by the domain
orchestrator.

| Family or surface | Skill | Applicability reason | Status | Evidence | Next decisive action |
|---|---|---|---|---|---|

Use only these statuses:

- `EXAMINED` — the stated evidence supports the scoped result;
- `CANDIDATE` — a falsifiable attack hypothesis survives initial triage;
- `FALSIFIED` — a named proof, counterexample, or controlled experiment defeats
  this exact candidate;
- `NOT_APPLICABLE` — a concrete structural or model precondition fails;
- `BLOCKED` — missing artifact, capability, access, or prerequisite;
- `DEFERRED` — worthwhile but outside the declared budget, with a proposed test;
- `INCONCLUSIVE` — attempted evidence does not decide the question.

Never use `NO_ATTACK` or `SECURE` as a status.

## Candidate record

For every DISCOVER candidate, record:

1. exact target and mechanism;
2. structural reason it might work;
3. required attacker model and preconditions;
4. expected impact if true;
5. cheapest decisive falsifier;
6. test result or unresolved obligation;
7. preliminary time, data, memory, and success accounting;
8. evidence provenance and confidence.

An analogy, related paper, or unexplained statistical anomaly is an input to a
candidate—not a candidate result.

## Completion gates

### ASSESS

- Freeze target, claims, and models.
- Cover every applicable known family from the selected orchestrator.
- Compare costs to named generic and claimed baselines.
- State search channels and exclusions behind every negative result.

### DISCOVER

- Satisfy ASSESS gates needed for a reliable baseline.
- Generate candidates from every plausible structural source.
- Attempt the cheapest falsifier for each viable candidate.
- Hand surviving high-value candidates to costing or validation.
- Preserve falsified, blocked, and deferred branches in the ledger.

### VALIDATE

- State the claim so one result can decide it.
- Check preconditions before implementation.
- Reproduce all load-bearing numbers with actual tools.
- Seek an independent source, derivation, implementation, or checker.

### FORMALIZE

- State the exact theorem and correspondence boundary.
- Pin the toolchain and declare axioms or assumptions.
- Replay from a clean state.
- Report the trusted computing base and unformalized gaps.

If a gate cannot be satisfied, return a scoped partial result with the blocking
condition. Do not silently lower the gate.
