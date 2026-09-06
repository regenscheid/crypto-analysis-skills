---
name: ntru-and-falcon-analysis
description: "Analyzes NTRU encryption and NTRU-lattice signatures, especially Falcon/FN-DSA-style GPV sampling, using lattice reduction, hybrid and subfield attacks, short-generator questions, key-equivalent bases, FFT/LDL sampling, norm verification, and numerical correctness."
metadata:
  version: "0.1"
  display-name: "NTRU and Falcon Analysis"
  tags: "ntru, falcon, fn-dsa, gaussian-sampling, numerical-analysis, ideal-lattices"
  requires: "ntru-or-falcon-specification, implementation, parameters"
  produces: "ntru-estimates, sampler-audit, numerical-findings"
---

# NTRU and Falcon Analysis

## Use this skill when

The target uses an NTRU equation, NTRU lattice, compact NTRU KEM/PKE, Falcon/FN-DSA, or another NTRU-trapdoor signature.

## Operating procedure

1. Write the exact ring/module, modulus, polynomial degree, public relation, secret distribution, invertibility conditions, key-generation solver, basis representation, and signature/encryption equations.
2. Build the full and projected NTRU lattices. Estimate primal reduction, hybrid meet-in-the-middle, subfield/subring, overstretched-parameter, and special-form attacks with the actual secret distribution.
3. Search for key-equivalent secrets or bases: determine whether any short generator, rotated/conjugated pair, alternative basis, or approximate relation suffices for decryption, signing, or impersonation.
4. Analyze public ideal/module information precisely. Distinguish principal-ideal generator recovery, NTRU basis recovery, module structure, norm equations, and what is or is not publicly determined.
5. For encryption/KEM variants, audit message lifting, wraparound/decryption failure, chosen ciphertexts, FO transforms, and algebraic resultants or gcd relations.
6. For Falcon-like signatures, transcribe FFT/LDL tree construction, Gaussian sampling, recursive normalization, rejection/norm tests, encoding, and verification in both mathematical and finite-precision forms.
7. Audit numerical approximation: precision requirements, rounding mode, coherent key-derived cached values, approximation error dependence across signatures, underflow/overflow, exceptional inputs, and specification-permitted implementation variance.
8. Analyze transcript distributions for secret leakage, deviations from the target Gaussian, reuse/correlation, faulty sampling, skipped rejection, and malformed encodings.
9. Reproduce any proposed numerical or statistical attack against a high-precision reference and include false-positive controls, autocorrelation tests, and end-to-end forgery/key-recovery criteria.
10. Report separately on NTRU lattice hardness, principal-ideal questions, key-equivalent recovery, encryption correctness, signature distribution, and implementation numerical behavior.

## Output contract

- An NTRU ring/lattice and public-information map.
- Lattice, hybrid, subfield, and key-equivalent attack estimates.
- Falcon/FN-DSA sampler and numerical-conformance tests.
- Property-specific conclusions with exact implementation/version scope.

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

- `NTRU98`
- `CS97-NTRU`
- `HG07-NTRUHYBRID`
- `ABD16-SUBFIELD`
- `NTRUPRIME17`
- `GS02-IDEALGEN`
- `CDPR16-IDEAL`
- `GPV08`
- `FALCON18`
- `FALCON-SPEC`
- `PEIKERT10-GAUSS`
- `NR06-HPP`

Full records are bundled in `references/REFERENCES.md`.
