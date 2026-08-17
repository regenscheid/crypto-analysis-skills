---
name: code-based-failure-and-reaction-analysis
description: "Analyzes decoding failures, decoder iteration behavior, rejection sampling, error generation, and externally visible reaction oracles in code-based KEM/PKE systems, with emphasis on sparse/QC/MDPC decoders and implicit-rejection transforms."
metadata:
  version: "0.1"
  display-name: "Code-Based Failure and Reaction Analysis"
  tags: "reaction-attacks, decoding-failure, mdpc, hqc, implicit-rejection"
  requires: "decoder-implementation, key-error-distributions, oracle-interface"
  produces: "dfr-estimate, reaction-model, adaptive-attack-records"
---

# Code-Based Failure and Reaction Analysis

## Use this skill when

A code-based scheme has nonzero decoding failure, an iterative or probabilistic decoder, secret-dependent error behavior, rejection in key or error generation, or any observable decapsulation outcome.

## Operating procedure

1. Transcribe the exact decoder, stopping rules, thresholds, iteration schedule, syndrome updates, failure flags, fallback-key logic, and all externally visible behavior after decapsulation.
2. Derive the claimed decoding-failure rate under the actual key and error distributions. Preserve dependencies from quasi-cyclic rotations, fixed-weight sampling, sparse keys, and decoder state.
3. Instrument intermediate syndromes, counters, flips, iterations, and rejection events in a research build while preserving an uninstrumented control implementation.
4. Construct chosen-error/ciphertext families that vary distance, overlap, rotations, trapping sets, or parity-check correlations one controlled feature at a time.
5. Search for black-box reaction signals in explicit failure, distinct returned keys, downstream key-confirmation behavior, protocol retries, retransmissions, and externally visible acceptance. Record timing, cache, power, electromagnetic, and fault channels only as out-of-scope handoffs to a separate implementation-attack model.
6. Develop statistical key-recovery hypotheses: estimate how each observation updates beliefs about secret support, cyclic differences, parity-check overlaps, or decoder thresholds; account for adaptive query selection and multiple testing.
7. Audit CCA transforms and implicit rejection. Determine whether fallback derivation, ciphertext re-encryption, secret-key encoding, or protocol use truly makes all invalid ciphertexts observationally equivalent.
8. Analyze multi-target and bootstrapping effects: one rare failure may identify a weak key, train a classifier, create stronger probes, or amortize across rotations/users.
9. Recompute complete query, computation, storage, false-positive, and verification costs and compare with generic ISD/key recovery.
10. Validate against fresh keys and held-out ciphertexts. Require end-to-end secret recovery, decoder reconstruction, or a precisely scoped distinguisher before claiming a break.

## Output contract

- A decoder/correctness model and validated DFR estimate.
- A reaction-oracle observability matrix.
- Statistical/adaptive key-recovery attack records with controls.
- A CCA/implicit-rejection and full-scheme consequence assessment.

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

- `GJS16-REACTION`
- `FABSIC17-REACTION`
- `FABSIC18-LEDA`
- `GUO20-HQCFAIL`
- `FO99`
- `HHK17-FO`
- `HQC-SPEC`
- `NIST-IR8545`

Full records are bundled in `references/REFERENCES.md`.
