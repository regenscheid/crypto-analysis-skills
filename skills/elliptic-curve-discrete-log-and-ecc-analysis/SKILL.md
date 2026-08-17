---
name: elliptic-curve-discrete-log-and-ecc-analysis
description: "Analyzes ECC and ECDLP systems through curve/group validation, generic rho/kangaroo attacks, endomorphisms, pairing/anomalous reductions, invalid-curve/twist attacks, scalar distributions, and construction-level ECDSA/EdDSA/ECDH behavior."
metadata:
  version: "0.1"
  display-name: "Elliptic-Curve Discrete-Log and ECC Analysis"
  tags: "ecc, ecdlp, invalid-curve, twist, ecdsa, eddsa, ecdh"
  requires: "curve-parameters, encodings, construction"
  produces: "curve-audit, ecdlp-estimates, ecc-attack-records"
---

# Elliptic-Curve Discrete-Log and ECC Analysis

## Use this skill when

The target uses elliptic-curve signatures, key agreement, encryption, VRFs, pairings, or an elliptic-curve group action.

## Operating procedure

1. Record curve model, field, coefficients, group and twist orders, cofactors, base point, encoding, scalar clamping/reduction, endomorphisms, parameter-generation provenance, and validation rules.
2. Compute generic ECDLP baselines with Pollard rho/kangaroo, parallel distinguished points, automorphism/negation speedups, multi-target effects, and realistic memory/communication.
3. Check special reductions and exceptional classes: MOV/Frey–Rück embedding, anomalous curves, supersingular/low-embedding-degree curves, weak twists, and special endomorphisms.
4. Analyze invalid-curve, twist, low-order, identity, and subgroup attacks using exact scalar processing, cofactor handling, all-zero checks, and protocol feedback.
5. Audit point encodings and decompression: canonical field elements, sign bits, infinity, exceptional coordinates, non-curve points, and agreement between parser and arithmetic.
6. For ECDSA/DSA-like signatures, invoke nonce/HNP analysis and inspect signature malleability, key substitution, hash truncation, and public-key recovery semantics.
7. For EdDSA/Schnorr-like signatures, inspect deterministic nonce/context binding, cofactor equations, batch verification, small-order points, and duplicate/equivalent encodings.
8. For ECDH/X25519-style agreement, inspect clamping, noncontributory/all-zero outputs, static key reuse, public-key validation strategy, transcript binding, KCI, and forward secrecy.
9. Estimate Shor resources for the exact curve and arithmetic model; report logical versus physical assumptions.
10. Separate ECDLP hardness, group-selection defects, input-validation attacks, nonce failures, and protocol failures in conclusions.

## Output contract

- A curve/twist/group and encoding audit.
- Generic ECDLP and special-reduction estimates.
- Invalid-input, nonce, signature, and key-agreement attack records.
- Classical/quantum claim-specific conclusions.

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

- `MILLER85-ECC`
- `KOBLITZ87-ECC`
- `MOV93`
- `FREYRUCK94`
- `SMART99-ANOMALOUS`
- `SEMA97-ANOMALOUS`
- `BMM00-INVALIDCURVE`
- `ANTIPA03-VALIDATION`
- `GLV01`
- `CURVE25519`
- `VOW99-PARALLEL`
- `TESKE01-RHO`
- `RFC7748`
- `RFC8032`
- `PROOS03-ECC`

Full records are bundled in `references/REFERENCES.md`.
