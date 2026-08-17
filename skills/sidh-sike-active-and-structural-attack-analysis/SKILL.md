---
name: sidh-sike-active-and-structural-attack-analysis
description: "Analyzes SIDH/SIKE-specific active and structural attacks, including torsion-point auxiliary information, GPST-style adaptive validation oracles, endomorphism-ring recovery, and the Castryck–Decru/Maino–Martindale/Robert breaks, with explicit limits on transfer to other isogeny families."
metadata:
  version: "0.1"
  display-name: "SIDH/SIKE Active and Structural Attack Analysis"
  tags: "sidh, sike, castryck-decru, gpst, torsion, active-attack"
  requires: "sidh-or-derived-scheme, parameters, implementation"
  produces: "sidh-attack-map, reproduced-breaks, transfer-analysis"
---

# SIDH/SIKE Active and Structural Attack Analysis

## Use this skill when

The target is SIDH, SIKE, a SIDH-derived protocol, or a new construction that exposes images of torsion bases or analogous auxiliary isogeny information.

## Operating procedure

1. Transcribe SIDH key generation and shared-secret computation, including secret isogeny degrees, torsion bases, images of the other party’s torsion basis, curve invariants, validation, and KEM transform.
2. Define the exact problem created by the public auxiliary points, not merely generic supersingular isogeny path finding. Map pairings, kernels, endomorphism action, and information preserved through isogenies.
3. Reconstruct GPST-style active attacks: malicious public keys, validation omissions, adaptive shared-secret/acceptance oracle, secret-bit extraction, query count, and countermeasures.
4. Reconstruct the structural key-recovery attacks of Castryck–Decru and subsequent formulations, identifying the role of auxiliary torsion images, endomorphisms, products/gluing, dimensions, and exceptional cases.
5. Verify attacks on official or archived parameter sets and implementations with exact source versions, independent key validation, recovered-isogeny checks, and runtime/memory logs.
6. Analyze the SIKE KEM transform only after core SIDH recovery: state whether key recovery, decapsulation, or chosen-ciphertext interaction is required and how correctness/implicit rejection behaves.
7. Test proposed variants/countermeasures by mapping which auxiliary information or algebraic relation is removed, altered, hidden, or still reconstructible.
8. Build a transfer matrix for any adjacent target. Explicitly test whether torsion-basis images, the same endomorphism relation, active oracle, and product-isogeny machinery are present.
9. Do not use the existence of the SIDH break as evidence against generic isogeny path finding, CSIDH, or SQIsign without a concrete reduction or attack.
10. Record historical chronology and corrections so obsolete SIKE security estimates are not reused.

## Output contract

- A SIDH auxiliary-information and attack-prerequisite map.
- Reproduced active and structural key-recovery records.
- Countermeasure/variant transfer matrices.
- A precise non-transfer statement for other isogeny families where requirements are absent.

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

- `JDF11-SIDH`
- `DFJP14-SIDH`
- `SIKE-SPEC`
- `GPST16-SIDH`
- `CD22-SIDH`
- `MM22-SIDH`
- `ROBERT22-SIDH`

Full records are bundled in `references/REFERENCES.md`.
