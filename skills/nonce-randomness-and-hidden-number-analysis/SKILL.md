---
name: nonce-randomness-and-hidden-number-analysis
description: "Analyzes secret-dependent nonces, ephemeral scalars, salts, errors, masks, and randomness for reuse, bias, partial exposure, correlations, state rollback, and hidden-number/lattice attacks."
metadata:
  version: "0.1"
  display-name: "Nonce, Randomness, and Hidden-Number Analysis"
  tags: "nonce, randomness, hidden-number, bias, reuse"
  requires: "randomness-generation, public-equations, implementation"
  produces: "randomness-map, hnp-models, sample-complexity, misuse-tests"
---

# Nonce, Randomness, and Hidden-Number Analysis

## Use this skill when

A signature, encryption, proof, or key-agreement scheme uses fresh secret randomness whose reuse or bias can reveal a long-term key or witness.

## Operating procedure

1. Inventory every random value, its generation algorithm, entropy source, deterministic derivation, personalization/context inputs, state, rejection/conditioning, caching, and lifetime.
2. Write the exact public equation linking each random value and secret to observable outputs. Normalize modular sign and range conventions before deriving attacks.
3. Test exact reuse, partial reuse, affine relations, shared prefixes/suffixes, cross-key/cross-protocol reuse, state rollback, fork/VM cloning, counter reset, and deterministic-nonce context omission.
4. Model bias and leakage as intervals, known bits, noisy approximations, modular inequalities, or distributions. Estimate min-entropy and correlation rather than assuming uniformity.
5. Construct hidden-number/lattice embeddings or algebraic systems appropriate to the observation model. Account for scaling, wraparound, sign ambiguity, outliers, and verification.
6. Analyze how many samples are needed as a function of leakage precision, bias, lattice dimension, solver quality, target count, and success probability.
7. Test rejection sampling and retries for conditional bias or externally visible information, even when raw random generation is uniform.
8. Check deterministic standards such as RFC 6979 and scheme-specific derivations for correct inclusion of key, message/prehash, context, parameter set, and optional randomness.
9. Validate attacks on synthetic data with controlled leakage before interpreting real traces or outputs. Use an independent key verifier.
10. Classify the result as mathematical randomness failure, API misuse, state-management defect, or physical leakage; keep the latter outside a black-box conclusion unless explicitly modeled.

## Output contract

- A randomness lifecycle and dependency map.
- A catalog of reuse, bias, correlation, rollback, and context-omission hypotheses.
- Hidden-number/lattice attack models with sample/success estimates.
- Synthetic validation and minimized misuse tests.

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

- `BV96-HNP`
- `HGS01-NONCE`
- `NS02-NONCE`
- `RFC6979`
- `DILITHIUM18`
- `FALCON18`

Full records are bundled in `references/REFERENCES.md`.
