---
name: isogeny-hard-problem-and-group-action-analysis
description: "Analyzes the underlying isogeny, endomorphism-ring, quaternion-ideal, and commutative group-action problems using path finding, meet-in-the-middle, endomorphism recovery, vectorization/parallelization, hidden shift, and structural reductions."
metadata:
  version: "0.1"
  display-name: "Isogeny Hard-Problem and Group-Action Analysis"
  tags: "isogeny, group-action, sqisign, csidh, quaternion, endomorphism"
  requires: "isogeny-scheme, curve-action-parameters, protocol"
  produces: "isogeny-problem-map, path-estimates, protocol-findings"
---

# Isogeny Hard-Problem and Group-Action Analysis

## Use this skill when

A KEM, key agreement, signature, VDF, or proof system relies on supersingular/ordinary isogeny graphs, endomorphism rings, quaternion ideals, class-group actions, vectorization, or parallelization.

## Operating procedure

1. Specify the curve/isogeny setting: ordinary or supersingular, base field, curve model/invariants, endomorphism ring/order, isogeny degrees, torsion bases, orientation, group/action, public auxiliary information, and secret representation.
2. Define the exact hard problem: unstructured path finding, vectorization/parallelization, endomorphism-ring computation, group-action inversion, ideal equivalence, short/decomposed isogeny, or proof/witness recovery.
3. Compute generic graph/group-action baselines and the best classical meet-in-the-middle, random-walk, claw, Delfs–Galbraith, quaternion, and endomorphism-ring algorithms for the exact setting.
4. Analyze quantum hidden-shift, claw/path, and other algorithms with explicit oracle construction, coherent memory/qRAM, state preparation, and group-action evaluation cost.
5. Inventory auxiliary structure: torsion-point images, pairings, orientations, smooth-degree decompositions, endomorphisms, kernels, response isogenies, commitment curves, and validation behavior.
6. For SQIsign-like schemes, transcribe identification/signature transcripts and quaternion-ideal computations; audit witness distribution, commitment/challenge/response relations, norm bounds, compression, verification, and Fiat–Shamir/QROM proof.
7. For CSIDH/group-action schemes, analyze action evaluation, secret-exponent distribution, class-group relations, invalid curves, twist behavior, public-key validation, and active-oracle assumptions.
8. Search for endomorphism-ring leakage, orientation recovery, special curves, weak keys, repeated ideals/actions, equivalent secret representations, and protocol responses that reveal connecting paths.
9. Validate algorithms on small discriminants/graphs and verify recovered paths/ideals independently; document when toy attacks rely on smoothness or graph sizes absent at real parameters.
10. Keep SIDH-specific torsion-point attacks in the dedicated skill and require a transfer matrix before applying them to SQIsign, CSIDH, or generic isogeny systems.

## Output contract

- An exact isogeny/group-action problem and auxiliary-information map.
- Classical and quantum path/action/endomorphism estimates.
- Protocol/transcript, validation, and weak-key attack hypotheses.
- Small-instance verified paths/ideals and transfer classifications.

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

- `DELFS16-ISO`
- `CJS14-ISOGENYQ`
- `KUP05-HIDDENSHIFT`
- `CSIDH18`
- `SQISIGN20`
- `SQISIGN-SPEC`
- `JDF11-SIDH`

Full records are bundled in `references/REFERENCES.md`.
