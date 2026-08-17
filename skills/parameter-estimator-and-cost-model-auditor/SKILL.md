---
name: parameter-estimator-and-cost-model-auditor
description: "Runs or audits public-key security estimators and cost models for lattices, codes, discrete logs, factorization, multivariate systems, isogenies, and quantum attacks with version pinning, sensitivity analysis, and cross-checks."
metadata:
  version: "0.1"
  display-name: "Parameter Estimator and Cost-Model Auditor"
  tags: "estimator, parameters, cost-model, reproducibility"
  requires: "parameter-instance, estimator-or-cost-model"
  produces: "parameter-estimate-records, sensitivity-ranges, cross-checks"
---

# Parameter Estimator and Cost-Model Auditor

## Use this skill when

A security level depends on software, tables, asymptotic formulas, or heuristic cost models rather than a direct implemented attack.

## Operating procedure

1. Define the mathematical instance from the specification, not from an estimator preset: dimensions, moduli, distributions, ranks, weights, field sizes, group orders, structure, and target success probability.
2. Pin estimator name, repository, commit, dependency versions, command, configuration, hardware assumptions, and output units. Save machine-readable input and output.
3. Enumerate every attack family the estimator supports and every relevant family it omits. Do not report only the minimum returned by a default command.
4. Audit cost-model choices: classical/quantum, enumeration/sieving, RAM/gates/bit operations, nearest-neighbor model, polynomial-system solver model, ISD memory model, precomputation, and parallelism.
5. Check parameter conversions and secret/error distributions, including rounding, sparse secrets, module/ring reductions, quasi-cyclic structure, extension fields, and multi-target settings.
6. Vary disputed parameters and model constants to produce sensitivity curves or ranges. Identify phase transitions where a different attack becomes dominant.
7. Cross-check with at least one independent implementation, analytic derivation, published table, or small-instance experiment when feasible.
8. Separate asymptotic interpolation from calibrated finite-size data and mark extrapolation beyond demonstrated instances.
9. Compare estimator output with the exact claim and include correctness/failure terms and construction losses where relevant.
10. Store a parameter-estimate record that can be rerun and diffed when software or assumptions change.

## Output contract

- A versioned parameter-estimate record for each attack/model/parameter set.
- A sensitivity and dominant-attack analysis.
- A list of estimator omissions, unsupported extrapolations, and conversion risks.
- Cross-check results and rerunnable commands.

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

- `LATTICE-ESTIMATOR`
- `EST18-ALL`
- `ESSER22-ISD`
- `BARDET19-RANKALG`
- `F4-99`
- `DELFS16-ISO`
- `GE21-RSA`

Full records are bundled in `references/REFERENCES.md`.
