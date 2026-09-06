---
name: automated-algebra-and-search-model-builder
description: "Builds and validates SageMath, Gröbner-basis, SAT/SMT, CP-SAT, MILP, lattice, decoding, MinRank, or graph-search models for public-key cryptanalysis, with semantic cross-checks and certificates."
metadata:
  version: "0.1"
  display-name: "Automated Algebra and Search Model Builder"
  tags: "automation, algebra, sat, smt, groebner, lattice, isd"
  requires: "formal-hypothesis, target-algorithms"
  produces: "validated-search-model, witness-checker, solver-artifacts"
---

# Automated Algebra and Search Model Builder

## Use this skill when

A cryptanalytic hypothesis requires automated equation solving, combinatorial search, parameter exploration, exact arithmetic, or optimized path/decoding/lattice computation.

## Operating procedure

1. Define the mathematical variables, domains, equations/constraints, objective, symmetries, and success witness independently of any solver syntax.
2. Choose the method from structure: Gröbner/F4/F5 or XL for polynomial systems, SAT/SMT/CP for bit/arithmetic constraints, lattice reduction for approximate integer relations, ISD for low-weight solutions, graph/path search for isogenies, or exhaustive dynamic programming for small instances.
3. Construct a tiny hand-checkable instance and verify every equation, indexing convention, field/modulus operation, encoding, and boundary condition against the specification.
4. Add semantic invariants and round-trip tests. Generate witnesses from the real algorithm and ensure the model accepts them; perturb witnesses and ensure rejection.
5. Break symmetries only with proven-safe constraints and record how solution counts change. Do not silently impose genericity, nonzero, full-rank, or canonical assumptions.
6. Separate existence, optimization, counting, and average-case questions. A single found witness does not estimate prevalence, and failure to find one does not prove absence.
7. Request independently checkable witnesses, Gröbner bases, rank certificates, lattice vectors, paths, or UNSAT certificates where available.
8. Benchmark scaling across controlled instance families; record memory, branching, degree growth, solver randomness, and timeout/censoring.
9. Cross-check at least a subset with an independent implementation or algebra system and compare exact intermediate values.
10. Export the model, generator, checker, instances, and logs as reproduction artifacts; state the proven scope of every negative result.

## Output contract

- A documented mathematical model and machine-readable instance generator.
- Witness/solution checker and tiny-instance validation suite.
- Solver configurations, certificates or witnesses, scaling data, and logs.
- A scope statement distinguishing proof, bounded search, and heuristic evidence.

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

- `LLL82`
- `F4-99`
- `F5-02`
- `XL00`
- `KS99-MINRANK`
- `BARDET19-RANKALG`
- `LATTICE-ESTIMATOR`

Full records are bundled in `references/REFERENCES.md`.
