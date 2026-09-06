---
name: composite-residuosity-and-homomorphic-pke-analysis
description: "Analyzes Paillier, Damgård–Jurik, and related composite-residuosity encryption, as well as homomorphic constructions whose security or correctness depends on hidden-order arithmetic, noise management, or malleable ciphertext algebra."
metadata:
  version: "0.1"
  display-name: "Composite Residuosity and Homomorphic PKE Analysis"
  tags: "paillier, composite-residuosity, homomorphic-encryption, fhe, malleability"
  requires: "scheme-specification, parameters, ciphertext-interface"
  produces: "homomorphic-assumption-map, correctness-analysis, attack-records"
---

# Composite Residuosity and Homomorphic PKE Analysis

## Use this skill when

The target uses Paillier-style additive homomorphism, composite residuosity, an RSA/unknown-order group, or a homomorphic encryption layer whose accepted ciphertext algebra affects confidentiality or integrity.

## Operating procedure

1. Record modulus generation, prime structure, subgroup/order assumptions, generator selection, message space, randomness distribution, ciphertext representation, decryption equation, and validation rules.
2. Map the advertised claim to decisional composite residuosity, higher residuosity classes, factoring, strong RSA, LWE/RLWE, circular security, or another exact assumption. Keep semantic security, circuit privacy, and robustness separate.
3. Test elementary failures: shared factors, weak or reused randomness, noninvertible randomness, malformed generators, small subgroups, noncanonical representatives, and ciphertexts outside the intended language.
4. Exploit homomorphism symbolically. Determine which linear, multiplicative, equality, range, or relation information is revealed by public operations, re-randomization, decryption responses, or downstream protocol checks.
5. For Paillier/Damgård–Jurik, analyze residuosity-class tests, chosen-ciphertext malleability, plaintext-domain wraparound, signed/packed encodings, threshold-share verification, and proofs of plaintext knowledge/range.
6. For lattice FHE, identify the exact RLWE/RGSW assumptions, secret and error distributions, modulus chain, gadget decomposition, key switching/relinearization keys, bootstrapping keys, and public encryptions of secret-dependent values.
7. Audit correctness as an attack surface: noise growth, scale/rounding, approximation error, overflow, modulus switching, decryption failure, and adversarial circuits or ciphertexts that amplify failure or leakage.
8. Analyze protocol composition. Homomorphic malleability is intentional, so integrity must come from proofs, authentication, or an outer protocol; test whether omitted binding permits substitution or selective-failure attacks.
9. Recompute concrete costs for factoring/lattice attacks and include public auxiliary material, multi-key settings, packed slots, and reusable evaluation keys in the instance.
10. Report separate conclusions for IND-CPA/CCA confidentiality, function/circuit privacy, correctness, robustness, verifiability, and threshold security.

## Output contract

- A composite-residuosity or FHE assumption and parameter map.
- Ciphertext-language, malleability, encoding, and correctness attack records.
- Concrete factoring/lattice estimates including auxiliary public material.
- Property-specific conclusions for confidentiality, privacy, correctness, and robustness.

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

- `PAI99`
- `DJ01`
- `GENTRY09-FHE`
- `BGV12-FHE`
- `BFV12-FHE`
- `CKKS17`
- `BP97-STRONGRSA`
- `LATTICE-ESTIMATOR`

Full records are bundled in `references/REFERENCES.md`.
