---
name: information-set-decoding-and-generic-decoding-analysis
description: "Builds reproducible information-set decoding and generic decoding estimates for Hamming-metric code-based encryption, KEMs, signatures, and identification systems, including finite-size optimization, memory, parallelism, multi-target, and quantum variants."
metadata:
  version: "0.1"
  display-name: "Information-Set Decoding and Generic Decoding Analysis"
  tags: "code-based, isd, syndrome-decoding, low-weight-codeword, quantum-isd"
  requires: "decoding-instance, target-success, cost-model"
  produces: "isd-estimates, finite-parameter-optimization, generic-code-baseline"
---

# Information-Set Decoding and Generic Decoding Analysis

## Use this skill when

A scheme relies on syndrome decoding, low-weight codewords, Goppa/QC/MDPC decoding, or a Hamming-metric decoding problem and needs a correct generic attack baseline.

## Operating procedure

1. Normalize the decoding instance: field, code length/dimension/redundancy, target weight, code distribution, syndrome count, number of solutions, key/ciphertext structure, and desired success probability.
2. Implement or evaluate Prange, Lee–Brickell, Stern, Dumer, MMT, BJMM, May–Ozerov, and current optimized variants as applicable; do not select an algorithm from asymptotics alone.
3. Optimize integer parameters for the exact finite instance. Record list sizes, representation multiplicities, filtering probabilities, nearest-neighbor subroutines, and verification.
4. Separate operation counts from bit complexity and wall-time models. Include memory, bandwidth, sorting/hashing, communication, preprocessing, and parallel efficiency.
5. Analyze DOOM/multi-syndrome and multi-user targets, amortized precomputation, many ciphertexts/signatures, and key-reuse effects.
6. For structured public codes, calculate the generic ISD instance but hand structural assumptions to the structural code skill; never claim generic-code security from ISD alone.
7. For quantum analysis, state whether the estimate uses Groverized outer search, quantum walks, coherent lists/qRAM, or a concrete circuit; report queries, gates, depth, and qubits separately.
8. Validate against published records or an independent estimator and preserve code version, optimization choices, and random seeds.
9. Analyze decoding versus distinguishing and key recovery separately; a ciphertext decoder may not recover the private code, while a structural distinguisher may not decode.
10. Export a reusable generic-decoding baseline for Classic McEliece, HQC, BIKE-like designs, code signatures, rank variants only after metric conversion is justified, and MPCitH statements.

## Output contract

- A normalized finite decoding instance.
- Optimized classical, multi-target, and quantum ISD estimates.
- Versioned parameter records and validation checks.
- A clear split between generic decoding, distinguishing, and key recovery.

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

- `MCELIECE78`
- `PRANGE62`
- `LEEBRICKELL88`
- `STERN89-ISD`
- `DUMER91-ISD`
- `MMT11-ISD`
- `BJMM12-ISD`
- `MAYOZEROV15-ISD`
- `BOTHMAY17-ISD`
- `ESSER22-ISD`
- `DOOM11`
- `BERN10-QCODE`

Full records are bundled in `references/REFERENCES.md`.
