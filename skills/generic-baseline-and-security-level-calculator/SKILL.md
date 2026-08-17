---
name: generic-baseline-and-security-level-calculator
description: "Computes reproducible generic, exhaustive, multi-target, and quantum baselines for public-key schemes and their underlying problems. Use before claiming that a specialized attack is meaningful or assigning a bit-security number."
metadata:
  version: "0.1"
  display-name: "Generic Baseline and Security-Level Calculator"
  tags: "baselines, bit-security, complexity, multi-target, quantum"
  requires: "claim-row, parameter-set, cost-model"
  produces: "generic-baselines, parameter-estimate-records, sensitivity-analysis"
---

# Generic Baseline and Security-Level Calculator

## Use this skill when

A claimed attack complexity or parameter security level needs a correct comparison point under a stated classical or quantum cost model.

## Operating procedure

1. Select the exact claim row and success target. Distinguish key recovery, message recovery, forgery, distinguishing, collision, decoding, relation finding, and protocol impersonation.
2. Compute exhaustive-search and guessing baselines from the actual secret distribution and min-entropy, not merely nominal key length.
3. For generic groups, calculate baby-step/giant-step, Pollard rho/kangaroo, parallel collision search, subgroup decomposition, and multi-target variants with explicit group-operation and memory counts.
4. For factoring and finite-field DLP, record current algorithm family, asymptotic expression, finite-size calibration source, precomputation reuse, and special-form effects.
5. For lattices, codes, multivariate systems, subset sum, and isogenies, call the relevant family estimator or attack skill and import a versioned baseline record rather than inventing an exponent.
6. Compute birthday, collision, preimage, and multi-target baselines for hash-based components and proof transcripts.
7. Apply multi-user, multi-key, many-ciphertext, many-signature, or batch-verification scaling only where the game and attack actually permit sharing or target amplification.
8. For quantum estimates, separate query complexity from logical gates, depth, qubits, memory/qRAM, state preparation, error correction, and physical resources. Distinguish Shor-type polynomial attacks from Grover/amplitude-amplified search.
9. Normalize all estimates to a comparison table while preserving native units; state success probability and repetitions rather than reporting only log2 work.
10. Run sensitivity analysis over disputed constants, memory limits, parallelism, and cost conventions, and mark extrapolations beyond validated estimator ranges.

## Output contract

- A generic-baseline table keyed by claim, model, parameter set, and success probability.
- Versioned parameter-estimate records with native and normalized units.
- Classical, Q1, and Q2 comparisons where applicable.
- Sensitivity ranges and a list of assumptions that dominate each estimate.

## Non-negotiable guardrails

- Bind every conclusion to the exact artifact, version, parameter set, key format, and security game.
- Distinguish a faster algorithm for an underlying mathematical problem from a complete attack on the cryptosystem, and distinguish a proof gap from an exploit.
- Never present a weak-key, malformed-input, related-key, multi-target, decryption-oracle, leakage, fault, or quantum result as a standard-model full-scheme break without that qualification.
- Recompute data, oracle queries, arithmetic operations, bit complexity, memory, preprocessing, communication, verification, parallel depth, and success probability in explicit units.
- State the cost model, implementation assumptions, and estimator version; a single headline exponent is not a reproducible security estimate.
- Preserve failed attacks, rebuttals, corrections, withdrawn claims, and source-version chronology in the evidence ledger.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not established by a proof, derivation, experiment, validated implementation, or cited source.
- Do not compare unlike units—such as bit operations, field multiplications, AES calls, lattice nodes, quantum queries, and physical gates—without an explicit conversion model.

## Associated references

- `SHOR94`
- `GROVER96`
- `SHANKS71-BSGS`
- `POLLARD78-DLOG`
- `SHOUP97-GGM`
- `VOW99-PARALLEL`
- `LL93-NFS`
- `LATTICE-ESTIMATOR`
- `ESSER22-ISD`
- `F4-99`

Full records are bundled in `references/REFERENCES.md`.
