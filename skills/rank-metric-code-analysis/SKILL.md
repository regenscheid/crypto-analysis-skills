---
name: rank-metric-code-analysis
description: "Analyzes rank-metric encryption, KEMs, signatures, and identification systems through rank syndrome decoding, MinRank, support trapping, algebraic solving, Frobenius/module structure, Gabidulin distinguishers, and structural key recovery."
metadata:
  version: "0.1"
  display-name: "Rank-Metric Code Analysis"
  tags: "rank-metric, gabidulin, lrpc, minrank, rank-syndrome-decoding"
  requires: "rank-instance, field-representation, construction"
  produces: "rank-attack-estimates, structural-findings, weak-key-analysis"
---

# Rank-Metric Code Analysis

## Use this skill when

The target uses Gabidulin/LRPC or other rank-metric codes, rank syndrome decoding, MinRank, matrix-code equivalence, or low-rank matrices over extension fields.

## Operating procedure

1. Normalize field extensions, base-field matrix representation, code length/dimension, rank weight, syndrome equations, support dimension, public matrices, and secret/error distributions.
2. Separate rank syndrome decoding, MinRank, low-rank codeword, code equivalence, support recovery, and structural distinguishing; identify which exact problem each proof and attack addresses.
3. Estimate combinatorial support-trapping and rank-decoding algorithms with finite parameters, Gaussian-binomial counts, memory, multi-syndrome targets, and verification.
4. Build algebraic systems from minors, bilinear equations, Kipnis–Shamir-style formulations, support variables, and field equations. Use Gröbner/XL/linearization only with explicit degree and monomial accounting.
5. Analyze Frobenius closures, q-sums/q-products, dual/intersection dimensions, Overbeck-style distinguishers, and structural recovery for Gabidulin-derived public codes.
6. For LRPC and related decoders, study support expansion, product spaces, weak keys, decoding failure, rank erasures, and whether failures reveal secret support.
7. Audit extension-field representations, basis choices, subfield subcodes, automorphisms, circulant/module compression, and equivalent keys/decoders.
8. Compare algebraic, combinatorial, structural, and generic matrix-enumeration costs under the same units and success target.
9. Validate equations and rank conventions on exhaustive small instances; many published/modeling errors arise from transposes, base-field expansion, or incorrect rank constraints.
10. Map results separately to distinguishing, RSD/MinRank solving, equivalent-key recovery, decryption/signing capability, and full construction security.

## Output contract

- A normalized rank-metric/MinRank instance.
- Combinatorial, algebraic, and structural attack estimates.
- Weak-key/failure and extension-field representation tests.
- Exact consequences for KEM/PKE/signature claims.

## Non-negotiable guardrails

- Bind every conclusion to the exact artifact, version, parameter set, key format, and security game.
- Distinguish a faster algorithm for an underlying mathematical problem from a complete attack on the cryptosystem, and distinguish a proof gap from an exploit.
- Never present a weak-key, malformed-input, related-key, multi-target, decryption-oracle, leakage, fault, or quantum result as a standard-model full-scheme break without that qualification.
- Recompute data, oracle queries, arithmetic operations, bit complexity, memory, preprocessing, communication, verification, parallel depth, and success probability in explicit units.
- State the cost model, implementation assumptions, and estimator version; a single headline exponent is not a reproducible security estimate.
- Preserve failed attacks, rebuttals, corrections, withdrawn claims, and source-version chronology in the evidence ledger.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not established by a proof, derivation, experiment, validated implementation, or cited source.

## Associated references

- `GABID85`
- `GPT91`
- `OVERBECK08`
- `LRPC13`
- `GRS13-RSD`
- `BARDET19-RANKALG`
- `RANKSIGN18-BREAK`
- `KS99-MINRANK`

Full records are bundled in `references/REFERENCES.md`.
