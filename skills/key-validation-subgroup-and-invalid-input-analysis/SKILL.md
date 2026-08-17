---
name: key-validation-subgroup-and-invalid-input-analysis
description: "Analyzes public-key and peer-input validation, subgroup/cofactor confinement, invalid-curve/twist attacks, identity and low-order elements, malformed algebraic objects, and chosen-key attacks across DH, ECC, pairings, isogenies, codes, lattices, and proof systems."
metadata:
  version: "0.1"
  display-name: "Key Validation, Subgroup, and Invalid-Input Analysis"
  tags: "key-validation, subgroup, invalid-curve, malformed-input, rogue-key"
  requires: "input-formats, algebraic-domain, implementation"
  produces: "validation-matrix, invalid-input-corpus, validation-attacks"
---

# Key Validation, Subgroup, and Invalid-Input Analysis

## Use this skill when

An adversary can supply a public key, ephemeral share, ciphertext component, curve point, matrix, polynomial, code object, commitment, or other structured input.

## Operating procedure

1. Specify the mathematical validity language for each input: field/ring membership, curve equation, subgroup/order, cofactor, nonidentity, matrix rank, polynomial bounds, code dimensions, canonical encoding, and parameter provenance.
2. Compare full validation, partial validation, cofactor clearing, contributory checks, re-encryption checks, proof-of-possession, and no-validation paths in specification and code.
3. Enumerate adversarial inputs outside the intended domain: low-order and identity elements, twist/invalid curves, small subgroups, singular matrices, noninvertible ring elements, out-of-range coefficients, degenerate codes, malformed isogeny auxiliary points, and duplicate encodings.
4. Derive what secret-dependent computation occurs before rejection and what black-box output is observable: shared key, accept/reject, signature validity, protocol progress, or repeated session behavior.
5. For subgroup and invalid-curve attacks, compute subgroup orders, CRT reconstruction, query counts, oracle noise, and whether static secrets are reused. Include cofactors and scalar clamping exactly.
6. Test malicious public-key registration and key substitution, including rogue-key, chosen-key, and cross-parameter objects that make verification equations hold unexpectedly.
7. Audit batch/aggregate verification and fast paths that assume prior validation or fail to bind public keys and messages.
8. Design a generated corpus covering valid boundaries and invalid algebraic structures; independently verify each object’s intended classification.
9. Map exploits to the precise game and protocol interface. A rejected invalid point is not an attack; acceptance or informative secret-dependent behavior may be.
10. Specify minimal validation and transcript-binding requirements, including when standards permit alternate validation strategies.

## Output contract

- A validity-language and validation-path matrix.
- An adversarial structured-input corpus with independent classifiers.
- Subgroup/invalid-input attack derivations and complete query accounting.
- Claim mappings and minimal validation requirements.

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

- `LIMLEE97-SUBGROUP`
- `BMM00-INVALIDCURVE`
- `ANTIPA03-VALIDATION`
- `RFC7748`
- `NIST-SP800-56A`
- `GPST16-SIDH`

Full records are bundled in `references/REFERENCES.md`.
