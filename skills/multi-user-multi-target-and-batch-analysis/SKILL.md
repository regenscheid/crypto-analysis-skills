---
name: multi-user-multi-target-and-batch-analysis
description: "Analyzes how many users, keys, ciphertexts, signatures, targets, sessions, or batched equations change attack cost and security bounds, including shared preprocessing and one-out-of-many effects."
metadata:
  version: "0.1"
  display-name: "Multi-User, Multi-Target, and Batch Analysis"
  tags: "multi-user, multi-target, batch, aggregate, precomputation"
  requires: "single-user-claim, deployment-scale, attack-record"
  produces: "multi-target-model, amortized-costs, batch-findings, scaled-bounds"
---

# Multi-User, Multi-Target, and Batch Analysis

## Use this skill when

A deployment or attack involves many public keys, signatures, ciphertexts, protocol sessions, or batch/aggregate verification rather than a single isolated target.

## Operating procedure

1. Define the population and success event: any target, a chosen target, one forgery among many users, one weak key, one failure, or simultaneous compromise. Record key/data independence assumptions.
2. Translate the single-user game and bound into the actual multi-user/multi-target experiment, preserving adaptive registration, chosen messages, shared parameters, and per-user oracle budgets.
3. Identify reusable work: global tables, factor-base/NFS precomputation, lattice/code preprocessing, hash tables, transcript grinding, solver setup, common matrices, or standardized group parameters.
4. Derive target amplification and weak-key discovery probabilities from the true per-target distribution, including heavy tails and conditional key classes rather than applying a blind linear factor.
5. Analyze one-out-of-many and DOOM-style decoding/forgery problems, multi-target decryption failures, batch hidden-number attacks, and shared public-parameter attacks.
6. Audit batch and aggregate verification for rogue keys, duplicate messages, cancellation, randomized coefficients, subgroup validation, error localization, and fallback to individual verification.
7. Account for memory/bandwidth bottlenecks, parallel depth, communication, target enumeration, candidate ownership, and final per-key verification.
8. Recompute proof losses and claimed security levels for realistic deployment sizes and lifetimes; distinguish theorem union bounds from constructive attacks that exploit many targets.
9. Run sensitivity analysis over number of users, data per user, key rotation, and shared-precomputation lifetime.
10. State whether a result changes practical risk, only a conservative bound, or the standardized per-key security claim.

## Output contract

- A multi-user/multi-target experiment and population model.
- Shared-preprocessing and target-amplification cost analysis.
- Batch/aggregate verification attack tests.
- Security estimates across deployment sizes and lifetimes.

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

- `BBM00-MULTIUSER`
- `HULSING16-MULTITARGET`
- `DOOM11`
- `DANVERS21-MTFAIL`
- `VOW99-PARALLEL`
- `BN06-FORK`

Full records are bundled in `references/REFERENCES.md`.
