---
name: multivariate-public-key-analysis
description: "Analyzes multivariate quadratic public-key systems using direct and hybrid Gröbner-basis methods, XL/linearization, MinRank, differential and invariant-subspace structure, equivalent keys, field equations, and implementation-specific equation reductions."
metadata:
  version: "0.1"
  display-name: "Multivariate Public-Key Analysis"
  tags: "multivariate, mq, groebner, minrank, hfe, rainbow, mayo"
  requires: "public-polynomial-system, key-generation, parameter-set"
  produces: "mq-model, algebraic-attacks, structural-findings"
---

# Multivariate Public-Key Analysis

## Use this skill when

The target publishes a system of multivariate polynomials for signatures, PKE, identification, or a proof system, including HFE-, Rainbow-, UOV-, MAYO-, or MQ-derived designs.

## Operating procedure

1. Write the public and central maps over the exact base/extension field, number of variables/equations, degree, affine masks, layer structure, oil/vinegar partitions, hidden subspaces, and key-generation distribution.
2. Distinguish inversion of a random MQ instance, MinRank, recovery of affine transformations/central map, equivalent-key recovery, and direct forgery. Record which is sufficient for the scheme.
3. Build direct polynomial systems for key recovery and forgery including field equations, message/hash constraints, salt variables, rank conditions, and any public linear relations.
4. Run F4/F5/XL/Boolean or hybrid solving models with explicit monomial orders, degree of regularity, matrix dimensions, sparsity, linear algebra exponent, memory, and success probability.
5. Analyze hybrid attacks that guess variables/subspaces/layers, reduce fields, exploit underdetermined systems, or combine MinRank with Gröbner solving. Optimize finite parameters rather than quoting asymptotic exponents.
6. Search for structural invariants: differential bilinear forms, common kernels, polar maps, invariant/oil subspaces, rank distributions, Kipnis–Shamir systems, and equivalent transformations.
7. Analyze minus/plus modifiers, projections, vinegar selection, repeated signing samples, compressed public keys, cyclic/quasi-cyclic structure, and small-field peculiarities.
8. Test public-key and signature encodings, rank/weight bounds, malformed inputs, deterministic vinegar/randomness, rejection behavior, and algebraic edge cases.
9. Validate solver models by generating small keys with known trapdoors, recovering a key or forgery, and checking all public equations independently.
10. Conclude separately on generic MQ hardness, structural key recovery, equivalent signing keys, direct forgery, proof assumptions, and parameter security.

## Output contract

- A normalized MQ/central-map and hidden-structure model.
- Direct, hybrid, MinRank, and structural attack records.
- Versioned Gröbner/linearization models and validation artifacts.
- Separate key-recovery, equivalent-key, and direct-forgery conclusions.

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

- `MI88`
- `PATARIN96-HFE`
- `KS99-MINRANK`
- `F4-99`
- `F5-02`
- `XL00`
- `FGS05-DIFFMQ`
- `RAINBOW05`
- `BEULLENS22-RAINBOW`
- `MAYO21`
- `MAYO-SPEC`
- `NIST-IR8610`

Full records are bundled in `references/REFERENCES.md`.
