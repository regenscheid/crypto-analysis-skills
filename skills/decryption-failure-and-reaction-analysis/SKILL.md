---
name: decryption-failure-and-reaction-analysis
description: "Models correctness failures in lattice, code, rank-metric, and other noisy PKE/KEMs; searches for failure-inducing inputs; and evaluates failure boosting, reaction attacks, and transform consequences."
metadata:
  version: "0.1"
  display-name: "Decryption-Failure and Reaction Analysis"
  tags: "decryption-failure, reaction-attack, dfr, correctness, rare-events"
  requires: "decrypt-decaps-algorithm, distributions, implementation"
  produces: "failure-predicate, dfr-estimates, reaction-attacks, failure-witnesses"
---

# Decryption-Failure and Reaction Analysis

## Use this skill when

A scheme can decrypt or decode incorrectly with nonzero probability, or security relies on a claimed decryption-failure rate.

## Operating procedure

1. Define failure exactly at every layer: core decryption/decoding error, message mismatch, re-encryption mismatch, fallback selection, shared-key mismatch, protocol failure, or externally observable reaction.
2. Derive the failure condition from the implemented arithmetic, rounding, compression, decoder, error distribution, key distribution, and boundary cases. Validate the derivation on toy and real instances.
3. Separate average random-ciphertext DFR, honest-encapsulation DFR, conditional per-key DFR, weak-key tails, and adversarially selected ciphertext failure probability.
4. Identify variables an adversary can bias or control and construct parameterized ciphertext/error families that move the system toward failure surfaces or informative decoder behavior.
5. Assess observability: direct error, key confirmation, retransmission, application behavior, chosen-ciphertext acceptance, side-channel-independent protocol effects, or statistical differences across repeated interactions.
6. Develop reaction and failure-boosting strategies. Quantify oracle noise, sample complexity, adaptivity, target information, false positives, and final secret/key verification.
7. Estimate rare events using exact convolution/dynamic programming, importance sampling, subset simulation, bounds, or validated analytic approximations. Do not extrapolate tiny DFRs from zero failures.
8. Analyze multi-target and many-ciphertext amplification, weak-key discovery, chosen public keys, and whether preprocessing can be shared.
9. Insert the resulting failure terms into KEM/PKE proofs and compare with the claimed security bound; distinguish correctness violation from CCA exploitation.
10. Package failure witnesses, key/ciphertext instances, statistical methodology, confidence intervals, and corrected/reference controls.

## Output contract

- A formal failure predicate and validated failure model.
- Average, conditional, weak-key, and adversarial DFR estimates with uncertainty.
- Failure-boosting/reaction attack records and oracle requirements.
- Concrete proof impact and reproducible failure witnesses.

## Non-negotiable guardrails

- Bind every conclusion to the exact artifact, version, parameter set, key format, and security game.
- Distinguish a faster algorithm for an underlying mathematical problem from a complete attack on the cryptosystem, and distinguish a proof gap from an exploit.
- Never present a weak-key, malformed-input, related-key, multi-target, decryption-oracle, leakage, fault, or quantum result as a standard-model full-scheme break without that qualification.
- Recompute data, oracle queries, arithmetic operations, bit complexity, memory, preprocessing, communication, verification, parallel depth, and success probability in explicit units.
- State the cost model, implementation assumptions, and estimator version; a single headline exponent is not a reproducible security estimate.
- Preserve failed attacks, rebuttals, corrections, withdrawn claims, and source-version chronology in the evidence ledger.
- Treat solver timeout, bounded search failure, and absence of a known attack as inconclusive—not as evidence of security.
- Mark every inference that is not established by a proof, derivation, experiment, validated implementation, or cited source.
- Absence of observed failures provides only a sample-size-dependent bound; it does not establish the advertised cryptographic DFR.

## Associated references

- `DANVERS19-FAIL`
- `DANVERS19-BOOTFAIL`
- `DANVERS21-MTFAIL`
- `GJS16-REACTION`
- `NIST-FIPS203`
- `HQC-SPEC`

Full records are bundled in `references/REFERENCES.md`.
