---
name: code-based-structural-and-qc-analysis
description: "Analyzes hidden-code and structured-code systems for distinguishers, support recovery, filtration/conductor attacks, permutation/scrambler recovery, quasi-cyclic and quasi-dyadic algebra, automorphisms, low-rank representations, and key-equivalent secret codes."
metadata:
  version: "0.1"
  display-name: "Code-Based Structural and QC Analysis"
  tags: "code-structure, goppa, alternant, quasi-cyclic, mdpc, support-recovery"
  requires: "public-code, hidden-family, key-generation-distribution"
  produces: "structural-distinguishers, key-equivalent-recovery, qc-findings"
---

# Code-Based Structural and QC Analysis

## Use this skill when

The target publishes a disguised Goppa, alternant, Reed–Solomon, QC/MDPC, quasi-dyadic, rank-derived, or otherwise structured code.

## Operating procedure

1. Write the public code in every useful representation: generator/parity-check matrices, polynomial/module form, circulant blocks, support/multiplier description, automorphism group, dual, Schur powers, shortening/puncturing behavior, and key transformations.
2. State the hidden family and camouflage mechanism. Identify which statistics a random code would have and which invariants survive permutation, scaling, scrambling, shortening, dualization, or quasi-cyclic compression.
3. Run distinguishers based on square/Schur-product dimensions, hull, weight distribution, filtration, conductors, shortening chains, automorphisms, rank profiles, and algebraic relations.
4. Attempt support/multiplier or key-equivalent recovery using Sidelnikov–Shestakov, filtration/conductor methods, Gröbner systems, linearization, invariant subcodes, and fixed-point subcodes as applicable.
5. For QC/MDPC systems, exploit circulant polynomial algebra, folding/projection, rotations, sparse dual words, low-weight multiples, factorization of x^r−1, and ring zero divisors.
6. Quantify the fraction of weak keys or exceptional structures and test whether key generation filters them. Do not generalize an average or special-key result without the distribution.
7. Determine what recovered structure suffices: original secret key, an equivalent parity-check matrix, a decoder, a distinguisher, or only metadata.
8. Compare structural attack cost with generic ISD/key search and include public-key size/compression and multi-key precomputation.
9. Validate on exact or scaled key distributions with positive controls from known broken variants and negative controls from random codes.
10. Report structural distinguishing, key-equivalent recovery, decoding capability, and full-scheme consequence as separate result types.

## Output contract

- A code-structure and camouflage map.
- Distinguisher and support/key-equivalent recovery attack records.
- QC/automorphism/weak-key analyses.
- Comparison with generic decoding and exact scheme consequences.

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

- `MCELIECE78`
- `NIED86`
- `SIDEL92`
- `SENDRIER00-SSA`
- `FAUGERE10-GOPPA`
- `CLASSIC-MCELIECE-SPEC`
- `HQC-SPEC`
- `GJS16-REACTION`

Full records are bundled in `references/REFERENCES.md`.
