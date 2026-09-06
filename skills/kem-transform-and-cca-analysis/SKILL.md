---
name: kem-transform-and-cca-analysis
description: "Analyzes KEM security, Fujisaki–Okamoto-style transforms, implicit rejection, re-encryption checks, KEM/DEM composition, and decapsulation interfaces for classical and post-quantum KEMs."
metadata:
  version: "0.1"
  display-name: "KEM Transform and CCA Analysis"
  tags: "kem, fujisaki-okamoto, cca, implicit-rejection, decapsulation"
  requires: "kem-specification, pke-core, proof, implementation"
  produces: "kem-transform-map, rejection-model, cca-audit, ciphertext-tests"
---

# KEM Transform and CCA Analysis

## Use this skill when

The target is a KEM or derives a KEM from a CPA-secure PKE/core primitive, especially with deterministic re-encryption or implicit rejection.

## Operating procedure

1. Formalize the KEM game: key generation, encapsulation, decapsulation, challenge, excluded ciphertext, decapsulation oracle, correctness/failure probability, multi-user setting, and malicious-public-key scope.
2. Transcribe the complete transform including message/coin derivation, hashing/domain separation, ciphertext recomputation, equality testing, fallback-secret generation, KDF input, and returned key.
3. Identify the exact transform theorem and prerequisites: PKE correctness, one-wayness/IND-CPA, disjoint simulations, plaintext checking, randomness recoverability, spreadness, random-oracle access, and failure assumptions.
4. Audit all rejection modes. Determine whether invalid, malformed, noncanonical, or failure-causing ciphertexts produce distinguishable outputs through errors, timing-independent protocol behavior, key confirmation, or repeated sessions.
5. Check ciphertext and public-key binding in the KDF and fallback path; test chosen-key, key-substitution, ciphertext malleability, component omission, and cross-parameter/cross-protocol confusion.
6. Analyze decryption failures separately, then reinsert their probability and adversarial amplifiability into the transform proof and concrete bound.
7. Test decapsulation consistency under alternative encodings, duplicate ciphertext representations, parsing differences, and deterministic re-encryption mismatches.
8. Analyze KEM/DEM or HPKE composition: authenticated versus base modes, context binding, sender authentication, export secrets, and how KEM failures propagate to the protocol.
9. Recompute proof loss, query factors, multi-user scaling, failure terms, and success probability under the implementation’s exact behavior.
10. Create adversarial ciphertext suites and state whether findings violate correctness, robustness, IND-CCA, contributory behavior, or only interoperability.

## Output contract

- A transform diagram and theorem-prerequisite checklist.
- A decapsulation/rejection oracle model.
- A concrete CCA bound including correctness/failure and multi-user terms.
- Adversarial ciphertext tests and classified KEM findings.

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

- `FO99`
- `HHK17-FO`
- `NIST-SP800-227`
- `RFC9180`
- `NIST-FIPS203`
- `KYBER17`
- `CLASSIC-MCELIECE-SPEC`
- `HQC-SPEC`

Full records are bundled in `references/REFERENCES.md`.
