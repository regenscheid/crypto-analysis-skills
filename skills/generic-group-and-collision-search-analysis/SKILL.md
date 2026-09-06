---
name: generic-group-and-collision-search-analysis
description: "Applies and audits generic-group lower bounds, Pollard rho/kangaroo, baby-step/giant-step, parallel collision search, distinguished points, automorphism speedups, and multi-target relation search."
metadata:
  version: "0.1"
  display-name: "Generic-Group and Collision-Search Analysis"
  tags: "generic-group, pollard-rho, kangaroo, collision-search, lower-bounds"
  requires: "group-or-action-instance, target-relation"
  produces: "generic-group-baselines, parallel-search-model, applicability-audit"
---

# Generic-Group and Collision-Search Analysis

## Use this skill when

A public-key claim relies on a cyclic/group-action search problem and specialized algebraic attacks are absent or need a correct generic baseline.

## Operating procedure

1. Define the black-box group or action interface, order information, available encodings/equality, inversion, sampling, auxiliary oracles, target relation, and whether the action is free/transitive.
2. Check whether the scheme actually fits the generic model. Record pairings, endomorphisms, coordinates, auxiliary torsion, representations, or leakage that expose non-generic structure.
3. Derive baby-step/giant-step and Pollard rho/kangaroo costs for the exact order, interval, target count, success probability, and memory budget.
4. Design the iteration function, partition, distinguished-point rule, collision detection, automorphism quotient, and verification; include fruitless cycles and nonuniform walks.
5. Analyze parallelization using distinguished points: expected work, wall time, communication, central storage, duplicate walks, checkpointing, and processor efficiency.
6. Analyze multi-target/multi-key speedups and reusable tables without confusing a union-bound advantage with shared algorithmic work.
7. Use generic-group lower bounds to delimit black-box attacks, but state explicitly why they do not rule out representation-specific or algebraic attacks.
8. For quantum models, compare Grover/amplitude amplification, Shor where applicable, and hidden-shift algorithms; state oracle/state-preparation assumptions.
9. Validate constants on small groups and independently verify recovered relations.
10. Export a baseline record reusable by finite-field, ECC, isogeny/group-action, hidden-order, and pairing modules.

## Output contract

- A generic-model applicability audit.
- BSGS/rho/kangaroo/parallel/multi-target baseline records.
- A walk implementation and small-instance validation where needed.
- A list of target-specific non-generic structures requiring specialist analysis.

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

- `SHANKS71-BSGS`
- `POLLARD78-DLOG`
- `SHOUP97-GGM`
- `NECHAEV94-GGM`
- `VOW99-PARALLEL`
- `TESKE01-RHO`
- `GROVER96`

Full records are bundled in `references/REFERENCES.md`.
