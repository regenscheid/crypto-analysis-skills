---
name: lattice-kem-and-pke-analysis
description: "Analyzes MLWE/MLWR and related lattice PKE/KEMs from base encryption through compression, decryption failure, CCA transforms, ciphertext validity, algebraic structure, and implementation-visible oracle behavior."
metadata:
  version: "0.1"
  display-name: "Lattice KEM and Public-Key Encryption Analysis"
  tags: "ml-kem, kyber, module-lwe, lattice-kem, decryption-failure, fo-transform"
  requires: "kem-pke-specification, implementation, parameter-set"
  produces: "lattice-kem-analysis, dfr-model, cca-transform-findings"
---

# Lattice KEM and Public-Key Encryption Analysis

## Use this skill when

The target resembles ML-KEM/Kyber, FrodoKEM, Saber, NewHope, or another LWE/MLWE/RLWE/LWR encryption or encapsulation scheme.

## Operating procedure

1. Transcribe key generation, encryption/encapsulation, decryption/decapsulation, compression/decompression, message encoding, hashes/KDFs, implicit rejection, and exact accepted encodings.
2. Derive the induced LWE/MLWE/LWR instances for public key, ciphertext components, and auxiliary values; include sample count, module rank, distributions, compression noise, and reused public parameters.
3. Run the lattice-estimator skill for primal, dual, hybrid, BKW, algebraic, and distribution-aware attacks; identify which component and sample set each estimate uses.
4. Derive correctness geometrically or probabilistically. Validate noise convolution, dependencies, wraparound, compression boundaries, message decoding, and claimed decryption-failure rate with exact arithmetic or high-precision simulation.
5. Audit the FO/CCA transform: reencryption equality, ciphertext hashing, secret-key/public-key binding, fallback-secret derivation, implicit rejection, malformed length handling, and chosen-ciphertext access.
6. Search for reaction oracles in timing, return codes, shared-secret use, protocol behavior, cache/page patterns, power/fault models only when in scope, and externally distinguishable downstream authentication failures.
7. Analyze ciphertext malleability, chosen coefficients, sparse/extreme ciphertexts, noncanonical encodings, NTT-domain assumptions, arithmetic overflow, and alternative representatives.
8. Test multi-target decryption-failure amplification, key reuse, chosen-public-key attacks, related ciphertexts, and whether one failure can bootstrap more information.
9. Compare reference, optimized, masked, hardware, and formally verified variants; implementation differences must be represented as different targets.
10. Map every finding separately to base-PKE one-wayness/IND-CPA, KEM IND-CCA, correctness/DFR, key recovery, shared-secret recovery, or implementation robustness.

## Output contract

- An exact PKE/KEM transcript and induced lattice-instance map.
- Lattice estimates and decryption-failure derivation.
- FO/implicit-rejection, malformed-ciphertext, and reaction-oracle tests.
- Claim-specific conclusions for base PKE, KEM CCA security, and correctness.

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

- `NIST-FIPS203`
- `NIST-SP800-227`
- `FO99`
- `HHK17-FO`
- `KYBER17`
- `FRODO16`
- `SABER18`
- `NEWHOPE16`
- `DANVERS19-FAIL`
- `DANVERS19-BOOTFAIL`
- `DANVERS21-MTFAIL`
- `LATTICE-ESTIMATOR`

Full records are bundled in `references/REFERENCES.md`.
