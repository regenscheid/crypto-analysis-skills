---
name: module-lattice-signature-analysis
description: "Analyzes Fiat–Shamir-with-aborts, trapdoor-sampling, and module-lattice signatures through MSIS/MLWE assumptions, rejection sampling, norm bounds, transcript distributions, nonce/randomness, algebraic attacks, and ROM/QROM proofs."
metadata:
  version: "0.1"
  display-name: "Module-Lattice Signature Analysis"
  tags: "lattice-signatures, ml-dsa, dilithium, fiat-shamir-with-aborts, rejection-sampling"
  requires: "signature-specification, proof, implementation"
  produces: "lattice-signature-attacks, distribution-audit, proof-findings"
---

# Module-Lattice Signature Analysis

## Use this skill when

The target resembles ML-DSA/Dilithium, BLISS, Lyubashevsky-style signatures, HAWK-like lattice signatures, or another lattice identification/signature construction.

## Operating procedure

1. Transcribe key generation, signing loops, commitment, challenge space, response equations, hint/compression logic, rejection conditions, verification norms, and serialization.
2. Map forgery to the exact SIS/MSIS/LWE/MLWE or NTRU-style problems and list all proof events: challenge collisions, abort distributions, programmed-oracle points, extraction conditions, and public-key well-formedness.
3. Normalize the concrete lattice instances for key recovery and forgery. Include public samples, secret distribution, challenge weight, response bounds, hint leakage, signature count, and any reused preprocessing.
4. Analyze rejection sampling mathematically and empirically: output distribution, acceptance rate, dependence on secret/key, bounded arithmetic, floating-point or table approximation, and effects of deterministic signing.
5. Search for nonce/randomness reuse, partial randomness, biased sampling, faulted challenges/responses, skipped rejection, duplicate commitments, and cross-implementation transcript correlations.
6. Analyze verification boundary cases: norm equalities, decompositions, high/low bits, hint reconstruction, challenge recomputation, noncanonical encodings, duplicate representations, and malformed public keys.
7. Investigate algebraic/multi-signature attacks using many transcripts, linear relations, hidden-number-like leakage, submodule structure, small challenges, and meet-in-the-middle or Gröbner/SAT formulations where justified.
8. Audit ROM/QROM and Fiat–Shamir reasoning with exact hash domains and transcript binding; quantify forking/measure-and-reprogram losses and multi-user effects.
9. Compare key-recovery and forgery estimates with generic lattice baselines and include verification cost and success probability.
10. Conclude separately on key recovery, EUF-CMA/SUF-CMA forgery, signature distribution/privacy, correctness, malleability, and implementation-specific failures.

## Output contract

- A signing/verification state machine and proof-obligation map.
- Normalized MSIS/MLWE/SIS attack instances and estimates.
- Rejection, randomness, boundary, and malformed-input tests.
- Separate forgery, key-recovery, distribution, and correctness conclusions.

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

- `NIST-FIPS204`
- `DILITHIUM18`
- `LYU09-FSABORT`
- `LYU12-LATSIG`
- `BLISS13`
- `GPV08`
- `MP12-TRAPDOOR`
- `PREST17-RENYI`
- `KLS18-FSQROM`
- `LATTICE-ESTIMATOR`
- `NIST-IR8610`
- `NIST-R3SIG-2026`

Full records are bundled in `references/REFERENCES.md`.
