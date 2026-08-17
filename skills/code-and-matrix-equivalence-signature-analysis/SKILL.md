---
name: code-and-matrix-equivalence-signature-analysis
description: "Analyzes signatures and identification schemes based on linear/code equivalence, matrix-code equivalence, and related isomorphism/group-action problems, including LESS- and MEDS-like designs, canonical forms, stabilizers, structural invariants, and Fiat–Shamir soundness."
metadata:
  version: "0.1"
  display-name: "Code- and Matrix-Equivalence Signature Analysis"
  tags: "code-equivalence, matrix-equivalence, less, meds, group-actions, signatures"
  requires: "scheme-specification, public-objects, group-action, parameter-set"
  produces: "equivalence-map, structural-attacks, transcript-audit, forgery-findings"
---

# Code- and Matrix-Equivalence Signature Analysis

## Use this skill when

The target hides a monomial, permutation, linear, left/right matrix, or other isometry between public codes or tensor/matrix spaces and proves knowledge of that equivalence.

## Operating procedure

1. Specify the public objects, field, dimensions, metric, acting group, left/right/monomial/permutation action, secret distribution, orbit, stabilizer, canonicalization, and exact search/decision equivalence problem.
2. Separate recovery of the original secret, any equivalent isometry, a canonical representative, a distinguisher, orbit membership, and direct signature forgery. Determine which output actually enables impersonation or signing.
3. Analyze orbit sizes, automorphism/stabilizer groups, weak objects with large stabilizers, key collisions, equivalent secrets, and whether public-key generation samples uniformly from the claimed hard distribution.
4. For linear-code equivalence, apply support splitting, hull and Schur-product invariants, puncturing/shortening, weight enumerators, graph reductions, canonical labeling, low-weight structures, and automorphism recovery.
5. For matrix-code equivalence, analyze left/right matrix actions, tensor flattenings, rank distributions, bilinear systems, MinRank reductions, module decomposition, invariant subspaces, and simultaneous-equivalence instances.
6. Estimate generic group-action collision, meet-in-the-middle, claw, parallel collision, and many-key attacks with exact orbit/stabilizer corrections, memory, preprocessing, and verification cost.
7. Transcribe the identification protocol and Fiat–Shamir transform: commitment distribution, challenge set, openings, special soundness, extraction, zero knowledge, repetitions, seed trees, transcript compression, and QROM loss.
8. Test canonical and noncanonical encodings, row-reduced forms, equivalent generators, response composition order, duplicate representatives, malformed public objects, and signer/verifier disagreement.
9. Transfer attacks among LESS, MEDS, and related variants only through an explicit requirement matrix covering the action, object distribution, canonical form, challenge structure, and parameter regime.
10. Validate on independently generated instances by recovering an equivalent action or producing an accepted forgery; report structural, generic-action, proof-system, and implementation findings separately.

## Output contract

- An object, action, orbit, stabilizer, and equivalence-problem map.
- Structural-invariant, canonical-form, generic-action, and algebraic attack records.
- A Fiat–Shamir/transcript and encoding audit.
- Scheme-specific conclusions for key recovery, equivalent signing, and forgery.

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

- `LESS-SPEC`
- `LESS20`
- `LESSFM21`
- `MEDS22`
- `MEDS-SPEC`
- `SENDRIER00-SSA`
- `KS99-MINRANK`
- `FS86`
- `KLS18-FSQROM`

Full records are bundled in `references/REFERENCES.md`.
