---
name: empirical-statistical-and-heuristic-claim-separation
description: "Prevents experiments, statistical inference, asymptotic models, estimator output, and heuristic assumptions from being mislabeled as formal proof while showing when they can support or motivate a formal subproblem."
metadata:
  version: "0.1.0"
  display-name: "Empirical, Statistical, and Heuristic Claim Separation"
  category: "certified-computation"
  tags: "evidence, statistics, heuristic, experiment, claim-discipline"
  requires: "experimental or estimator result, target claim, sampling/model assumptions"
  produces: "evidence classification, confidence/uncertainty report, formalizable subclaims, appropriate conclusion language"
  optional: "true"
  namespace: "formal"
---

# Empirical, Statistical, and Heuristic Claim Separation

## Purpose

Prevents experiments, statistical inference, asymptotic models, estimator output, and heuristic assumptions from being mislabeled as formal proof while showing when they can support or motivate a formal subproblem.

## Use this skill when

Use this skill when a cryptanalysis project mixes simulations, Monte Carlo counts, performance measurements, lattice estimators, random-permutation heuristics, numerical correlations, and formal or exact claims.

## Do not invoke automatically

Do not use it to obstruct ordinary experimental cryptanalysis. Its purpose is to label evidence accurately and identify small high-value proof obligations, not to demand that every measurement become a theorem.

## Optional entry contract

**Inputs**
- experimental or estimator result
- target claim
- sampling/model assumptions

**Expected products**
- evidence classification
- confidence/uncertainty report
- formalizable subclaims
- appropriate conclusion language

This skill is an optional specialist route. Completion of an ordinary cryptanalysis task does not require invoking it unless the claim or evidence goal warrants formal methods.

## Operating procedure

1. Write the strongest desired conclusion and list each supporting item as derivation, checked witness, exhaustive computation, certified computation, formal theorem, statistical estimate, benchmark, heuristic model, or expert judgment.
2. For experiments, record population, sampling design, keys/instances, seeds, exclusions, censoring/timeouts, stopping rules, multiple testing, and the exact observed statistic.
3. Compute suitable confidence intervals or posterior/likelihood summaries and report zero-event upper bounds correctly; do not equate no observed failures with probability zero.
4. For performance and attack estimates, separate algorithmic operation counts, implementation measurements, hardware/model assumptions, extrapolation, and asymptotic terms.
5. For lattice, random-permutation, Markov, independence, or Gaussian heuristics, state where each assumption enters and test sensitivity to plausible alternatives.
6. Identify formalizable kernels—such as a combinatorial identity, exact witness checker, finite bound, or rounding lemma—without claiming the remaining empirical conclusion becomes formal automatically.
7. Use replication, holdout instances, independent implementations, and adversarial controls to reduce ordinary scientific error.
8. Choose calibrated conclusion language and evidence status. Preserve contradictions and negative results rather than averaging them away.
9. Publish raw/aggregated data provenance, analysis code, uncertainty, assumptions, and optional formal follow-up tasks.

## Output contract

- A claim-to-evidence table with explicit evidence classes.
- Statistical uncertainty and estimator-assumption report.
- Reproducible experiment/benchmark manifest.
- A prioritized list of optional formal subclaims and what they would add.

## Non-negotiable guardrails

- No observed event is not impossibility.
- An estimator is not a certified lower bound unless its model and computation are proved.
- Benchmarks are platform- and implementation-specific.
- Do not downplay valuable empirical evidence merely because it is not formal.

## Related formal skills

- `formalization-value-and-scope-triage`
- `exact-probability-counting-and-tail-bound-certification`

## Optional CryptoSkills cross-references

- `public-key-evidence-synthesis-and-research-backlog`
- `symmetric-evidence-synthesis-and-research-backlog`

## Associated primary references

- **ARB** — [Arb: Arbitrary-Precision Ball Arithmetic](https://arblib.org/) (2026) — Arb project. `official-project`.
- **MPFR** — [GNU MPFR](https://www.mpfr.org/) (2026) — GNU MPFR project. `official-project`.
- **FPLLL-REPO** — [fplll](https://github.com/fplll/fplll) (2026) — fplll project. `official-repository`.
- **SHANNON26** — [ShannonProver: Towards Automating Formal Cryptographic Proofs](https://arxiv.org/abs/2607.02847) (2026) — Yiping Ma et al.. `research-paper`.

Bundled source metadata is in `references/REFERENCES.md`.
