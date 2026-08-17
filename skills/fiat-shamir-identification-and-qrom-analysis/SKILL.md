---
name: fiat-shamir-identification-and-qrom-analysis
description: "Analyzes identification protocols and Fiat–Shamir signatures for completeness, commitment binding, special soundness, zero knowledge, challenge entropy, grinding, aborts, transcript compression, and classical/QROM extraction."
metadata:
  version: "0.1"
  display-name: "Fiat–Shamir, Identification, and QROM Analysis"
  tags: "fiat-shamir, identification, qrom, extraction, transcripts"
  requires: "identification-protocol, signature-transform, proof"
  produces: "transcript-model, extraction-audit, qrom-audit, attack-hypotheses"
---

# Fiat–Shamir, Identification, and QROM Analysis

## Use this skill when

A signature or proof is obtained by applying Fiat–Shamir to a Sigma protocol, MPC-in-the-head proof, VOLE proof, code-based identification scheme, lattice protocol, or multivariate proof.

## Operating procedure

1. Transcribe the interactive protocol: statement/witness relation, prover randomness, commitments, challenge space/distribution, responses, verifier predicate, repetitions, and abort/restart rules.
2. Verify completeness and identify malformed statements/commitments/responses that alter the relation or acceptance probability.
3. Audit soundness and extraction: special soundness threshold, number and structure of distinct challenges required, extractor runtime, witness uniqueness, and failure cases.
4. Audit honest-verifier zero knowledge and commitment hiding/binding. Check seed trees, compressed commitments, omitted views, recomputation, and simulation distance.
5. Transcribe Fiat–Shamir hashing with every domain separator, public key, message/context, salt, commitment root, repetition index, and parameter identifier. Test ambiguity and transcript-collision surfaces.
6. Analyze challenge entropy, grinding, rejection, precomputation, multi-target advantage, repeated commitments/nonces, and correlations across parallel repetitions.
7. Check the exact ROM proof and whether it uses forking, rewinding, oracle programming, or measure-and-reprogram. Recompute concrete loss and query factors.
8. For QROM claims, define superposition-query access and verify that the cited theorem covers the protocol’s aborts, multi-round structure, compressed commitments, and challenge encoding.
9. Search for transcript splicing, commitment reuse, selective-opening, challenge subset, response malleability, and verifier parsing attacks; then elevate any property to an actual forgery.
10. Produce small-parameter exhaustive checks of acceptance, transcript multiplicity, extraction, and challenge coverage, plus independent transcript verifiers.

## Output contract

- An identification-protocol and Fiat–Shamir transcript specification.
- Completeness, soundness/extraction, zero-knowledge, and challenge-entropy audits.
- A ROM/QROM concrete-bound audit.
- Transcript attack hypotheses, exhaustive tests, and forgery mappings.

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

- `FS86`
- `PS00-FORK`
- `UNRUH17-QROM`
- `KLS18-FSQROM`
- `IKOS07-MPCITH`
- `ZKBOO16`
- `VOLEITH23`

Full records are bundled in `references/REFERENCES.md`.
