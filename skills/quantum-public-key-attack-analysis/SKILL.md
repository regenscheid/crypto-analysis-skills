---
name: quantum-public-key-attack-analysis
description: "Analyzes quantum attacks on public-key schemes with exact oracle models and resource accounting, including Shor, Grover/amplitude amplification, hidden shift, quantum walks, quantum ISD, and QROM effects."
metadata:
  version: "0.1"
  display-name: "Quantum Public-Key Attack Analysis"
  tags: "quantum, shor, grover, qrom, resource-estimation"
  requires: "mathematical-problem, construction-model, quantum-assumptions"
  produces: "quantum-model, quantum-attack-records, resource-ranges"
---

# Quantum Public-Key Attack Analysis

## Use this skill when

A scheme claims post-quantum security, a classical scheme is evaluated under quantum attack, or an attack invokes quantum subroutines or superposition oracles.

## Operating procedure

1. Define the quantum model: fault-tolerant or logical, Q1 versus Q2, available classical and quantum memory, qRAM, coherent access to public data/parameters, oracle construction, and allowed preprocessing.
2. Identify the attacked mathematical problem and whether a polynomial-time quantum algorithm applies: factoring, finite-field/ECC DLP, abelian hidden subgroup, hidden shift, period finding, or structured isogeny/group-action problem.
3. For search attacks, derive the classical predicate/oracle and cost of reversible evaluation, state preparation, uncomputation, amplitude amplification, success checking, and parallelization.
4. For lattice, code, MQ, isogeny, and subset-sum attacks, distinguish genuine quantum algorithmic improvements from merely applying Grover to a classical outer loop. Preserve memory and data assumptions.
5. Audit QROM interactions separately from mathematical attacks: superposition hash/signing access, measure-and-reprogram loss, rewinding limits, and whether a security proof covers the implementation’s transcript.
6. Estimate logical resources: T/Toffoli gates, Clifford gates where relevant, depth, logical qubits, measurements, qRAM/coherent storage, repetitions, and success probability.
7. If physical estimates are made, state code distance, physical error rates, factory assumptions, architecture, runtime, and uncertainty; do not mix them into an abstract query exponent.
8. Analyze multi-target and precomputation effects and whether standardized public parameters enable reusable quantum state preparation or arithmetic circuits.
9. Compare with classical attacks and the exact claim. A polynomial quantum attack to an underlying problem may still require protocol access or key extraction steps; include them.
10. Produce conservative and optimistic resource ranges and explicitly identify unimplemented or unvalidated algorithmic components.

## Output contract

- A precise quantum adversary/oracle model.
- Quantum attack records with query, logical, and physical resources separated.
- Classical-versus-quantum and Q1-versus-Q2 comparisons.
- A list of qRAM, state-preparation, arithmetic, and proof-model assumptions.

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

- `SHOR94`
- `GROVER96`
- `PROOS03-ECC`
- `GE21-RSA`
- `KUP05-HIDDENSHIFT`
- `CJS14-ISOGENYQ`
- `BERN10-QCODE`
- `UNRUH17-QROM`

Full records are bundled in `references/REFERENCES.md`.
