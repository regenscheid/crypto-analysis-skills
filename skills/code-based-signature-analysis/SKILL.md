---
name: code-based-signature-analysis
description: "Analyzes hash-and-sign, syndrome-decoding, identification-derived, and structured code-based signatures through decodable-syndrome density, complete-decoding cost, rejection distributions, public-code structure, Fiat–Shamir soundness, and forgery/key-recovery attacks."
metadata:
  version: "0.1"
  display-name: "Code-Based Signature Analysis"
  tags: "code-signatures, cfs, wave, cross, sdith, hash-and-sign"
  requires: "signature-specification, public-code, proof"
  produces: "code-signature-attacks, transcript-audit, forgery-estimates"
---

# Code-Based Signature Analysis

## Use this skill when

The target resembles CFS, Wave, CROSS, SDitH-derived signatures, code-based identification, or any scheme signing by decoding a syndrome or proving knowledge of a low-weight word.

## Operating procedure

1. Classify the construction: trapdoor hash-and-sign, identification/Fiat–Shamir, proof-derived signature, or algebraic code signature. Transcribe key generation, signing retries, challenge generation, response, and verification.
2. For hash-and-sign, derive the density of decodable syndromes, complete-decoding work, signer rejection distribution, salt/counter handling, and whether signatures leak the hidden decoder or code structure.
3. For identification-derived schemes, enumerate challenge space, rounds/repetitions, commitment binding, response openings, special soundness, extraction, zero knowledge, and Fiat–Shamir/QROM transformation.
4. Normalize every forgery route to decoding, low-weight codeword, DOOM, code equivalence, structural key recovery, collision/preimage, or proof-system soundness.
5. Analyze public-key structure using Schur powers, hull/dual, automorphisms, puncturing/shortening, weight distribution, and equivalent-decoder recovery.
6. Test malleability and parsing: response permutations, reordered commitments, alternate salts, noncanonical vectors, weight-bound equalities, duplicate representations, and malformed public keys.
7. Analyze signing randomness, rejection/counter reuse, repeated commitments, biased low-weight sampling, faulted responses, and multi-signature statistical leakage.
8. Compute generic forgery via ISD/DOOM for the actual number of signatures/users and compare with structural and proof-level attacks.
9. Validate toy instances with an honest signer and independently generated forgeries; preserve exact hash domains and transcript encoding.
10. Conclude separately on EUF-CMA/SUF-CMA, key recovery/equivalent decoding, signer distribution/privacy, correctness, and implementation acceptance language.

## Output contract

- A construction/transcript and hard-problem map.
- Complete-decoding, ISD/DOOM, proof, and structural forgery estimates.
- Signing-distribution and malformed-signature tests.
- Claim-specific forgery and key-recovery conclusions.

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

- `CFS01`
- `STERN93-ID`
- `WAVE19`
- `CROSS-SPEC`
- `SDITH-SPEC`
- `DOOM11`
- `FS86`
- `UNRUH17-QROM`
- `NIST-IR8610`
- `NIST-R3SIG-2026`

Full records are bundled in `references/REFERENCES.md`.
