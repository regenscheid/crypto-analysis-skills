---
name: homomorphic-encryption-and-noise-analysis
description: "Analyzes lattice-based homomorphic encryption for RLWE assumptions, noise growth and decryption failure, modulus/key switching, relinearization, bootstrapping, evaluation-key exposure, circular/KDM assumptions, approximate arithmetic, and chosen-ciphertext boundaries."
metadata:
  version: "0.1"
  display-name: "Homomorphic Encryption and Noise Analysis"
  tags: "homomorphic-encryption, fhe, rlwe, noise, ckks, bfv, bgv"
  requires: "he-scheme, parameters, evaluation-profile, implementation"
  produces: "he-noise-model, evaluation-key-audit, attack-estimates"
---

# Homomorphic Encryption and Noise Analysis

## Use this skill when

The target is BFV/BGV/CKKS-like FHE, leveled HE, threshold HE, or another scheme with public evaluation material and noise-managed ciphertexts.

## Operating procedure

1. Transcribe key generation, encryption/decryption, addition/multiplication, relinearization, rotation, modulus switching/rescaling, bootstrapping, key switching, threshold operations, and all public evaluation keys.
2. Instantiate the exact Ring/Module-LWE or NTRU assumptions for secret/public/evaluation-key distributions, rings, moduli, dimensions, samples, and gadget decompositions; invoke lattice estimator analysis.
3. Derive deterministic and probabilistic noise/error propagation for each operation, including rounding, scaling, rescaling, approximation, key switching, and bootstrapping. Validate against exact/reference arithmetic.
4. Define correctness for exact versus approximate schemes and model adversarially selected circuits/ciphertexts, parameter overflow, wraparound, scale mismatch, and decoding thresholds.
5. Analyze decryption failure, failure amplification, malformed ciphertexts, and whether applications expose decryption/validity/re-encryption reactions despite schemes often not claiming CCA security.
6. Audit evaluation-key assumptions: encryptions of secret-dependent values, circular/KDM security, key-switch chains, rotation/Galois keys, shared randomness, and cross-key/multi-key relations.
7. Search for algebraic, subfield/subring, sparse-secret, hybrid lattice, and many-sample attacks strengthened by evaluation keys or special ring/modulus choices.
8. For CKKS-like approximation, separate numerical error/precision loss from cryptographic noise and analyze whether application-level comparison/rounding creates an oracle or semantic failure.
9. Analyze threshold/multi-key protocols for malicious shares, key validation, transcript binding, noise flooding, robustness, and leakage-free assumptions at the black-box protocol level.
10. Report security, correctness, privacy, and application-semantic findings separately; “somewhat homomorphic but not CCA secure” is not itself a defect unless the claimed interface requires CCA.

## Output contract

- An HE algorithm/evaluation-key and assumption map.
- A validated noise/precision and correctness model.
- Lattice, subfield, evaluation-key, malformed-ciphertext, and protocol attack records.
- Property-specific findings for confidentiality, correctness, and application semantics.

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

- `GENTRY09-FHE`
- `BGV12-FHE`
- `BFV12-FHE`
- `CKKS17`
- `LPR10-RLWE`
- `ABD16-SUBFIELD`
- `LATTICE-ESTIMATOR`

Full records are bundled in `references/REFERENCES.md`.
