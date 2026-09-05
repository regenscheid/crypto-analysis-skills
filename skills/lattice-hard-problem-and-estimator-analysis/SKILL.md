---
name: lattice-hard-problem-and-estimator-analysis
description: "Builds reproducible classical and quantum security estimates for LWE, MLWE, RLWE, LWR, NTRU, SIS, MSIS, and related lattice instances, and audits reduction, estimator, and cost-model assumptions."
metadata:
  version: "0.1"
  display-name: "Lattice Hard-Problem and Estimator Analysis"
  tags: "lwe, mlwe, rlwe, lwr, sis, ntru, lattice-estimator"
  requires: "exact-lattice-instance, security-target, cost-model"
  produces: "versioned-estimates, sensitivity-analysis, reduction-audit"
---

# Lattice Hard-Problem and Estimator Analysis

## Use this skill when

A public-key scheme claims lattice security, cites an estimator, uses a nonstandard distribution or algebraic structure, or needs comparison across primal, dual, hybrid, BKW, combinatorial, and algebraic attacks.

## Operating procedure

1. Extract the exact instance from the scheme rather than from a parameter table: dimensions, module/ring degree, modulus, sample count, secret/error distributions, compression/rounding, public auxiliary samples, and success target.
2. Map scheme notation to standard LWE/MLWE/RLWE/LWR/NTRU/SIS/MSIS problem definitions. Record normal-form transformations, modulus switching, sample amplification, and any loss or distribution change.
3. Run primal uSVP/BDD and dual distinguishing estimates over plausible embeddings, sample counts, lattice dimensions, block sizes, success probabilities, and guessing choices.
4. Analyze hybrid attacks that guess secret/error coordinates or exploit sparsity, ternary/binomial distributions, product form, small support, or leaked coefficients. Include enumeration and verification costs.
5. Analyze BKW/coded-BKW, Arora–Ge/algebraic attacks, meet-in-the-middle, combinatorial attacks, and specialized NTRU or ideal/module attacks where their preconditions hold.
6. Version every estimator and reduction cost model. Record BKZ simulator, root-Hermite/block-size model, sieving/enumeration oracle, dimensions-for-free, memory, parallelism, and quantum speedup assumptions.
7. Test sensitivity to contested inputs: secret distribution, sample count, advantage target, reduction quality, finite-size corrections, ring/module structure, and cost per lattice operation.
8. Separate concrete cryptanalytic estimates from worst-case reductions. State reduction direction, approximation factors, quantum/classical status, and whether the actual parameters satisfy the theorem’s distributional hypotheses.
9. Cross-check headline estimates with at least one independent implementation or hand-derived calculation and preserve the full command/configuration.
10. Return ranges, not false precision, when estimator components are heuristic or extrapolated beyond benchmarks.

## Output contract

- A versioned normalized lattice-instance record.
- Primal, dual, hybrid, BKW, algebraic, and specialized attack estimates.
- Sensitivity tables and independent cross-checks.
- A reduction-versus-concrete-security conclusion with uncertainty bounds.

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

- `AJTAI96`
- `REGEV05-LWE`
- `LPR10-RLWE`
- `LS15-MLWE`
- `BPR12-LWR`
- `GN08-BKZ`
- `CN11-BKZ20`
- `MW16-REDUCTION`
- `BDGL16-SIEVE`
- `G6K18`
- `BKW93`
- `LP11-LWE`
- `APS15-LWE`
- `ARORA11-LWE`
- `WUNDERER19-HYBRID`
- `LATTICE-ESTIMATOR`
- `EST18-ALL`

Full records are bundled in `references/REFERENCES.md`.
