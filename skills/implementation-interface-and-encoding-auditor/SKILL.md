---
name: implementation-interface-and-encoding-auditor
description: "Audits public-key key, ciphertext, signature, point, polynomial, codeword, and transcript encodings plus parsing, canonicality, validation, error handling, and domain separation. Use to find mathematical-interface flaws without conflating them with physical side channels."
metadata:
  version: "0.1"
  display-name: "Implementation Interface and Encoding Auditor"
  tags: "encoding, parsing, validation, canonicality, domain-separation"
  requires: "specification, implementations, wire-formats"
  produces: "encoding-matrix, malformed-test-vectors, interface-findings"
---

# Implementation Interface and Encoding Auditor

## Use this skill when

A scheme crosses a serialization, API, validation, or transform boundary, especially when proofs assume unique parsing or valid group/code/lattice elements.

## Operating procedure

1. Inventory every external and internal representation: private/public keys, ciphertexts, shared secrets, signatures, points, field elements, polynomials, matrices, seeds, commitments, proofs, and protocol frames.
2. Specify accepted byte languages exactly: lengths, endianness, padding, unused bits, coefficient ranges, compressed forms, point signs, infinity/identity, subgroup/cofactor rules, and duplicate encodings.
3. Trace parsing order and failure behavior, including truncation, trailing data, integer overflow, negative/large coefficients, invalid points, malformed matrices, and noncanonical but equivalent objects.
4. Check whether serialize/parse and encode/decode are inverse and injective over the proof domain. Exhaustively test small encodings and fuzz boundary cases.
5. Map validation to cryptographic operations: public-key validation, ciphertext re-encryption, subgroup checks, signature equation inputs, transcript hashes, KDF contexts, and implicit rejection.
6. Audit domain separation and context binding across algorithms, parameter sets, modes, hash/XOF calls, commitments, challenge generation, KDFs, and hybrid components.
7. Test whether malformed or alternative encodings alter acceptance, rejection, derived keys, challenge hashes, caching, equality tests, or session binding.
8. Compare specification, reference code, optimized code, protocol profile, and proof assumptions. Record permissible implementation latitude that changes security behavior.
9. Classify findings as interoperability defect, canonicalization gap, validation oracle, malleability, key substitution, cross-protocol confusion, or proof/implementation mismatch.
10. Create minimized test vectors and map any exploit to the exact security game and oracle availability.

## Output contract

- A complete encoding/validation matrix.
- Canonicality and round-trip test vectors, including malformed cases.
- A domain-separation and context-binding audit.
- Classified findings with minimized reproductions and claim mappings.

## Non-negotiable guardrails

- Bind every conclusion to the exact artifact, version, parameter set, key format, and security game.
- Distinguish a faster algorithm for an underlying mathematical problem from a complete attack on the cryptosystem, and distinguish a proof gap from an exploit.
- Never present a weak-key, malformed-input, related-key, multi-target, decryption-oracle, leakage, fault, or quantum result as a standard-model full-scheme break without that qualification.
- Recompute data, oracle queries, arithmetic operations, bit complexity, memory, preprocessing, communication, verification, parallel depth, and success probability in explicit units.
- State the cost model, implementation assumptions, and estimator version; a single headline exponent is not a reproducible security estimate.
- Preserve failed attacks, rebuttals, corrections, withdrawn claims, and source-version chronology in the evidence ledger.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not established by a proof, derivation, experiment, validated implementation, or cited source.
- Timing, power, electromagnetic, cache, and fault leakage require a separate implementation-attack model; this skill covers black-box-visible interface behavior and mathematical validity.

## Associated references

- `RFC8017`
- `RFC7748`
- `RFC8032`
- `RFC9180`
- `NIST-FIPS203`
- `NIST-FIPS204`
- `NIST-FIPS205`

Full records are bundled in `references/REFERENCES.md`.
