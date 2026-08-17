---
name: subset-sum-and-knapsack-analysis
description: "Analyzes knapsack/subset-sum public-key constructions and embedded subset-sum subproblems through density, lattice embeddings, modular relations, representation techniques, meet-in-the-middle/dissection, and trapdoor-disguise recovery."
metadata:
  version: "0.1"
  display-name: "Subset-Sum and Knapsack Analysis"
  tags: "knapsack, subset-sum, lattice-embedding, representation, dissection"
  requires: "subset-sum-instance, key-generation, cost-model"
  produces: "subset-sum-estimates, trapdoor-attacks, validation-results"
---

# Subset-Sum and Knapsack Analysis

## Use this skill when

The target is a knapsack cryptosystem or exposes a bounded/sparse integer relation, subset sum, modular subset sum, or hidden superincreasing sequence.

## Operating procedure

1. Specify the exact instance: number and bit size of weights, modulus, density, target distribution, coefficient alphabet, modular versus integer equation, number of solutions, public disguise, and trapdoor relation.
2. Audit key generation for superincreasing or low-density remnants, multiplier/modulus weaknesses, gcd relations, approximate ratios, correlated weights, insufficient permutation/masking, and weak instances.
3. Construct lattice embeddings with explicit scaling, determinant, expected target norm, competing short vectors, sign/offset conventions, and recovery verification. Test multiple embeddings rather than citing density alone.
4. Evaluate meet-in-the-middle, Schroeppel–Shamir-style memory tradeoffs, representation algorithms, dissection, modular filtering, and multi-target/precomputation variants under explicit memory constraints.
5. Analyze low- and high-density regimes separately, including heuristic phase transitions, solution multiplicity, random-instance assumptions, and when a public-key distribution is distinguishable from random subset sum.
6. Search for trapdoor-disguise recovery using modular approximations, simultaneous Diophantine relations, lattice basis structure, and public/private weight correlations.
7. If subset sum is a subroutine inside another family, map how a recovered subset/relation becomes a key, forgery, decoded error, or only an internal witness.
8. For quantum variants, identify the exact search/list subroutine improved and account for memory/qRAM and reversible list processing.
9. Validate scaled instances with exhaustive solution counts and independently verify every recovered subset/trapdoor.
10. Report instance-specific costs and success probabilities; do not classify security solely by the density heuristic.

## Output contract

- A subset-sum/knapsack instance and key-generation audit.
- Lattice, MITM, representation, dissection, and quantum estimates.
- Scaled-instance validation and verified recovered relations.
- A construction-level transfer analysis for embedded subset-sum problems.

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

- `MH78-KNAPSACK`
- `SHAMIR82-KNAPSACK`
- `LO85-SUBSETSUM`
- `COS92-SUBSETSUM`
- `HGJ10-SUBSETSUM`
- `BCJ11-SUBSETSUM`
- `DDKS12-DISSECTION`
- `LLL82`
- `GROVER96`

Full records are bundled in `references/REFERENCES.md`.
