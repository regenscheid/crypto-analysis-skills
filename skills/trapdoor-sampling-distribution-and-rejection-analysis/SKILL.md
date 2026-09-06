---
name: trapdoor-sampling-distribution-and-rejection-analysis
description: "Audits secret-dependent sampling, trapdoor preimage sampling, discrete Gaussians, bounded/rejection sampling, aborts, output distributions, precision, and statistical-distance claims in signatures and encryption."
metadata:
  version: "0.1"
  display-name: "Trapdoor Sampling, Distribution, and Rejection Analysis"
  tags: "sampling, gaussian, rejection, distribution, precision"
  requires: "sampling-algorithm, proof, implementation"
  produces: "sampler-model, distribution-audit, precision-tests, sampling-attacks"
---

# Trapdoor Sampling, Distribution, and Rejection Analysis

## Use this skill when

Security or key hiding depends on sampled outputs being close to a target distribution independent of the secret/trapdoor.

## Operating procedure

1. Write the ideal target distribution and the implemented sampling algorithm, including centers, widths, bounds, precision, tables, recursions, caches, random bits, rejection thresholds, and abort conditions.
2. Identify every secret-, key-, message-, or state-dependent parameter and derive how it can influence acceptance probability or output distribution.
3. Reconstruct the proof of distributional closeness: smoothing/GPV conditions, rejection-sampling ratio, Rényi/statistical divergence, truncation, finite precision, and accumulated multi-signature distance.
4. Audit arithmetic semantics: rounding mode, floating/fixed-point precision, transcendental approximations, integer overflow, branch-independent but value-dependent truncation, and specification latitude.
5. Test conditional and joint distributions, not only marginals: coefficients, norms, signs, retries, tree leaves, cached values, cross-signature autocorrelation, and dependence on keys/messages.
6. Estimate distinguishability and key-recovery relevance under many signatures and multi-user targets. Convert per-sample divergence into the appropriate transcript-level bound.
7. Search for rejection/abort or malformed-input oracles that expose acceptance counts, retries, output absence, or protocol-level differences without relying on physical timing.
8. Use high-precision reference implementations and exact/small-instance samplers as controls; preserve seeds and intermediate values for differential testing.
9. If a distributional deviation is found, derive whether it enables distinguishing, secret estimation, forgery, or only proof-bound degradation, with complete sample complexity.
10. Report implementation leakage channels separately from purely output-distribution attacks.

## Output contract

- An ideal-versus-implemented sampler specification.
- A distribution-distance proof audit and multi-sample bound.
- High-precision differential tests and joint-distribution measurements.
- Attack records or proof-impact findings with sample complexity.

## Non-negotiable guardrails

- Bind every conclusion to the exact artifact, version, parameter set, key format, and security game.
- Distinguish a faster algorithm for an underlying mathematical problem from a complete attack on the cryptosystem, and distinguish a proof gap from an exploit.
- Never present a weak-key, malformed-input, related-key, multi-target, decryption-oracle, leakage, fault, or quantum result as a standard-model full-scheme break without that qualification.
- For a new or independently verified quantitative conclusion, account for the relevant data, oracle queries, arithmetic/bit operations, memory, preprocessing, communication, verification, parallel depth, and success probability in explicit units. Preserve attributed published quantities as source claims; reuse unchanged checked inputs and recompute affected dependencies.
- State the cost model, implementation assumptions, and estimator version; a single headline exponent is not a reproducible security estimate.
- Preserve failed attacks, rebuttals, corrections, withdrawn claims, and source-version chronology in the evidence ledger.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not established by a proof, derivation, experiment, validated implementation, or cited source.

## Associated references

- `GPV08`
- `LYU09-FSABORT`
- `PEIKERT10-GAUSS`
- `MP12-TRAPDOOR`
- `PREST17-RENYI`
- `FALCON18`
- `DILITHIUM18`

Full records are bundled in `references/REFERENCES.md`.
