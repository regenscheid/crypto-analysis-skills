---
name: code-based-kem-and-pke-analysis
description: "Analyzes Hamming-metric code-based PKE/KEMs—including McEliece/Niederreiter, Classic McEliece, QC-MDPC/BIKE-like systems, and HQC—through decoding, hidden-code structure, key indistinguishability, quasi-cyclic algebra, decryption failures, reaction attacks, and CCA transforms."
metadata:
  version: "0.1"
  display-name: "Code-Based KEM and PKE Analysis"
  tags: "code-based, kem, pke, mceliece, hqc, bike, reaction"
  requires: "code-based-scheme, decoder, implementation, parameters"
  produces: "code-scheme-audit, isd-estimates, structural-attacks, reaction-tests"
---

# Code-Based KEM and PKE Analysis

## Use this skill when

The target encrypts or encapsulates by adding a low-weight error or solving a syndrome-decoding problem over a hidden or structured code.

## Operating procedure

1. Record the public and secret code ensembles, field, length/dimension/redundancy, error weight/distribution, generator/parity-check representation, scramblers/permutations, quasi-cyclic blocks, decoding algorithm, and key/ciphertext encodings.
2. Map the security claim to generic syndrome decoding, codeword finding, code indistinguishability, structural key recovery, quasi-cyclic variants, and the construction’s KEM/PKE transform.
3. Run the ISD skill for exact finite-length decoding estimates, including multiple syndromes/targets, memory, nearest-neighbor subroutines, and quantum variants.
4. Analyze structural distinguishers and key recovery: support splitting, hull/Schur-product or algebraic invariants, alternant/Goppa structure, sparse parity checks, cyclic automorphisms, folded/projection attacks, and code equivalence.
5. For QC-MDPC/HQC-like schemes, derive decoder and reconciliation failure conditions, weak-key tails, chosen-ciphertext failure amplification, and black-box reaction observability.
6. Audit ciphertext validity, weight/range checks, syndrome parsing, decoding success criteria, message encoding, re-encryption, implicit rejection, and noncanonical representations.
7. Analyze public-key size reduction and quasi-cyclic structure for subcode, dual-code, low-weight parity-check, folding, and multi-instance attacks; verify whether structure survives randomization.
8. Recompute concrete security including decoding, structural attacks, transform loss, decryption failures, multi-user/multi-target factors, and public-key validation.
9. Test reference and optimized decoders on controlled error patterns, exhaustive small codes, adversarial ciphertexts, and independent corrected/reference implementations.
10. Separate generic decoding, structural key recovery, reaction attacks, correctness defects, and implementation parsing findings in the conclusion.

## Output contract

- A code/decoder/transform and assumption map.
- Finite-length ISD and structural-attack estimates.
- A decryption-failure/reaction model with adversarial ciphertext tests.
- Concrete claim-level findings for the exact code-based target.

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

- `MCELIECE78`
- `NIED86`
- `CLASSIC-MCELIECE-SPEC`
- `HQC-SPEC`
- `PRANGE62`
- `BJMM12-ISD`
- `MAYOZEROV15-ISD`
- `SENDRIER00-SSA`
- `FAUGERE10-GOPPA`
- `GJS16-REACTION`
- `NIST-IR8545`
- `HHK17-FO`

Full records are bundled in `references/REFERENCES.md`.
