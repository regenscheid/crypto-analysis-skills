---
name: hard-problem-reduction-and-assumption-auditor
description: "Audits the chain from a public-key scheme’s advertised security to its underlying mathematical assumptions, including reduction direction, variants, structure, tightness, correctness conditions, and idealized models."
metadata:
  version: "0.1"
  display-name: "Hard-Problem Reduction and Assumption Auditor"
  tags: "reductions, assumptions, proof-audit, tightness, instantiation"
  requires: "security-proof, scheme-parameters, claim-matrix"
  produces: "assumption-reduction-map, proof-findings, concrete-loss-analysis"
---

# Hard-Problem Reduction and Assumption Auditor

## Use this skill when

A scheme cites LWE, SIS, factoring, CDH, decoding, MinRank, isogeny path finding, one-way functions, or another assumption and the exact implication must be checked.

## Operating procedure

1. List each security theorem and copy its exact statement, parameter mapping, oracle model, correctness premise, and excluded events.
2. Draw the reduction chain from the scheme game to intermediate primitives and finally to named hard problems. Keep proof reductions separate from heuristic cryptanalysis estimates.
3. For every edge, record direction and type: black-box/non-black-box, classical/quantum, tight/non-tight, uniform/non-uniform, average/worst case, search/decision, exact/approximate, and structured/unstructured.
4. Check that the instantiated distribution matches the theorem: modulus, dimension, rank, noise law, secret law, code ensemble, curve/group distribution, hash domain, salt/challenge size, and key-generation conditioning.
5. Identify correctness, decryption-failure, rejection-sampling, simulation, rewinding, oracle-programming, or extraction events that contribute additive advantage or loss.
6. Recompute concrete loss terms, including query factors, multi-user factors, abort probabilities, guessing steps, hybrids, and statistical-distance terms.
7. Test assumption substitutability. Do not replace decisional Module-LWE with generic SVP, code indistinguishability with decoding, or SIDH path finding with a generic isogeny problem without documenting the missing implication.
8. Compare each assumption against the best known specialized attacks and structural distinguishers for the exact parameter regime.
9. Classify findings as proof defect, instantiation mismatch, loose bound, unsupported assumption leap, or actual cryptanalytic consequence. State what further construction is needed to turn a proof issue into an attack.
10. Update the claim matrix and assumption map without weakening the original theorem statement by paraphrase.

## Output contract

- A completed assumption/reduction map.
- A theorem-by-theorem proof audit with recomputed concrete loss.
- A list of instantiation mismatches and unsupported implication steps.
- A mapping from each proof finding to affected claim rows and attack hypotheses.

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

- `GM84-PKE`
- `BR93-ROM`
- `FO99`
- `HHK17-FO`
- `REGEV05-LWE`
- `LPR10-RLWE`
- `MCELIECE78`
- `JDF11-SIDH`
- `IKOS07-MPCITH`

Full records are bundled in `references/REFERENCES.md`.
