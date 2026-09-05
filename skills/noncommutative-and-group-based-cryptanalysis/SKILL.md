---
name: noncommutative-and-group-based-cryptanalysis
description: "Analyzes braid-group, conjugacy, decomposition, semidirect-product, matrix-group, and other noncommutative public-key proposals through faithful representations, linearization, centralizers, length-based heuristics, subgroup structure, normal forms, quotient attacks, and protocol equations."
metadata:
  version: "0.1"
  display-name: "Noncommutative and Group-Based Cryptanalysis"
  tags: "noncommutative, braid-groups, conjugacy, linearization, group-based-crypto"
  requires: "group-platform, parameter-generation, protocol"
  produces: "group-assumption-map, representation-attacks, protocol-findings"
---

# Noncommutative and Group-Based Cryptanalysis

## Use this skill when

The target relies on conjugacy search, simultaneous conjugacy, decomposition, factorization, semidirect products, group actions, matrix groups, braids, or another nonstandard noncommutative hard problem.

## Operating procedure

1. Specify the platform group/semigroup, representation and normal form, parameter distribution, public subgroups, secret-word distribution, protocol equations, and exact search/decision assumption.
2. Check well-posedness and generic hardness: uniqueness/equivalence of secrets, centralizers, centers, commuting subgroups, quotient maps, abelianization, finite images, and whether the public problem is easier than the named abstract problem.
3. Search for faithful or useful linear representations, matrix conjugacy, invariant subspaces, eigenvalue/Jordan information, module structure, and polynomial-time reductions to linear algebra.
4. Analyze normal-form and length leakage, summit/ultra-summit sets, peeling, memory-based length attacks, subgroup distance, and distributional biases; calibrate heuristic success on the exact key distribution.
5. Exploit simultaneous instances, shared conjugators, commuting factors, centralizer intersections, multiple transcripts, chosen public elements, and equivalent secrets.
6. Study quotient and homomorphic-image attacks first: solve in successively richer quotients/images and lift/filter candidates in the original group.
7. Model meet-in-the-middle, generic collision search, subgroup enumeration, rewriting, Gröbner/SAT encodings, and lattice methods if exponents or matrix entries yield additive relations.
8. Audit encodings and equality: nonunique words, canonicalization bugs, invalid elements, subgroup membership, identity/central elements, and protocol acceptance of equivalent representatives.
9. Compare the proposal against known cryptanalysis of its exact platform and parameter generation; “noncommutative” alone is not a security argument.
10. Validate by recovering an equivalent secret or completing impersonation/decryption, and separate heuristic evidence from proven polynomial-time reductions.

## Output contract

- A platform-group, representation, and assumption map.
- Linearization, quotient, centralizer, and length-based attack records.
- Distribution and encoding/membership tests.
- A calibrated conclusion on the exact proposal, not the abstract group problem.

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

- `AAG99`
- `KOLEE00`
- `HT02-LENGTH`
- `CJ03-BRAID`
- `SHOUP97-GGM`
- `VOW99-PARALLEL`

Full records are bundled in `references/REFERENCES.md`.
