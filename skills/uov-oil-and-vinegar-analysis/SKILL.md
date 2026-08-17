---
name: uov-oil-and-vinegar-analysis
description: "Performs specialized analysis of UOV, QR-UOV, MAYO-like and other Oil-and-Vinegar signatures, focusing on hidden oil subspaces, Kipnis–Shamir/MinRank systems, reconciliation and intersection attacks, equivalent keys, direct forgery, and parameterized hybrid algebraic attacks."
metadata:
  version: "0.1"
  display-name: "UOV and Oil-and-Vinegar Analysis"
  tags: "uov, oil-and-vinegar, qr-uov, mayo, snova, minrank"
  requires: "uov-family-specification, public-quadratic-forms, parameters"
  produces: "oil-subspace-model, uov-attacks, equivalent-key-findings"
---

# UOV and Oil-and-Vinegar Analysis

## Use this skill when

The target is UOV, Rainbow-derived, QR-UOV, MAYO, SNOVA, or any multivariate signature whose trapdoor is an oil/vinegar or hidden-subspace decomposition.

## Operating procedure

1. Extract oil/vinegar dimensions, number of equations, field, affine transformations, central-map coefficients, public-key compression, signing algorithm, vinegar sampling, and failure/retry behavior.
2. Represent quadratic forms as matrices/bilinear polar forms and identify the hidden oil subspace property. State conventions for characteristic two and diagonal terms explicitly.
3. Construct Kipnis–Shamir/MinRank and invariant-subspace systems; estimate ranks, kernel intersections, number of solutions, degree of regularity, and equivalent oil spaces.
4. Apply reconciliation, intersection, projection, subspace, differential, and rectangular/minus-variant attacks appropriate to the parameter regime.
5. Analyze direct forgery by fixing vinegar variables, exploiting underdetermined systems, guessing oil variables, finding low-rank combinations, or using Gröbner/XL hybrids. Include signature verification and false solutions.
6. Search for equivalent signing keys rather than only the original affine masks; determine whether a recovered oil subspace or alternative central map is enough.
7. Account for many public quadratic forms, multiple messages/signatures, salt and vinegar distributions, compressed-key structure, cyclic/QR structure, and multi-target users.
8. Audit signing failures and rejection: weak vinegar choices, rank-deficient linear systems, timing/iteration leakage when in scope, deterministic generation, and faulty signatures.
9. Validate algebraic models on exact small parameters and on full parameter subsets; cross-check public equations independently from the attack code.
10. Compare with generic MQ/direct-forgery baselines and report whether the attack is structural, generic, weak-key, or parameter-specific.

## Output contract

- An oil-subspace and quadratic-form model.
- Kipnis–Shamir/MinRank, reconciliation, intersection, and direct-forgery estimates.
- Equivalent-key and signing-failure tests.
- Scheme-specific conclusions for UOV-family candidates.

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

- `UOV99`
- `KS98-OV`
- `KS99-MINRANK`
- `BEULLENS20-UOV`
- `BEULLENS22-RAINBOW`
- `MAYO21`
- `UOV23`
- `UOV-SPEC`
- `MAYO-SPEC`
- `NIST-IR8610`
- `NIST-R3SIG-2026`

Full records are bundled in `references/REFERENCES.md`.
