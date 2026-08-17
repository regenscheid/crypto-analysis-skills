---
name: threshold-multisignature-and-aggregate-analysis
description: "Analyzes threshold signatures, Schnorr/RSA/ECDSA multisignatures, BLS aggregation, distributed key generation, and related protocols for rogue keys, nonce attacks, adaptive corruption, aborts, transcript confusion, and proof-model gaps."
metadata:
  version: "0.1"
  display-name: "Threshold, Multisignature, and Aggregate-Signature Analysis"
  tags: "threshold-signatures, multisignatures, aggregate-signatures, frost, musig, bls, dkg"
  requires: "protocol-specification, registration-model, corruption-model, implementation"
  produces: "session-model, rogue-key-tests, nonce-audit, forgery-and-robustness-findings"
---

# Threshold, Multisignature, and Aggregate-Signature Analysis

## Use this skill when

The target lets multiple parties jointly produce, aggregate, or batch-verify signatures, including FROST, MuSig/MuSig2, threshold RSA/ECDSA, BLS aggregate signatures, or a post-quantum threshold adaptation.

## Operating procedure

1. Classify the primitive precisely: threshold signature under one public key, multisignature under an aggregate key, aggregate signature on one or many messages, batch verification, distributed key generation, proactive refresh, or adaptor signature. State whether the final signature is ordinary or protocol-specific.
2. Formalize participants, threshold, corruption model, registration model, trusted setup, DKG/VSS assumptions, static versus adaptive corruption, rushing, concurrency, abort powers, and whether the adversary controls the coordinator or aggregator.
3. Audit key setup and aggregation for rogue-key and key-substitution attacks, proof-of-possession or knowledge requirements, duplicate keys, identity binding, weighting coefficients, subgroup validation, and inconsistent participant views.
4. Audit nonce generation and preprocessing: single-use guarantees, commitments, binding factors, pairwise/session identifiers, deterministic derivation, reserve pools, crash rollback, nonce-share exposure, and cross-session/cross-protocol reuse.
5. Derive each partial-signature equation and the final verification equation. Test whether malformed shares, missing signers, participant reordering, duplicate identities, aggregate-key changes, or message-list ambiguity can preserve acceptance.
6. Analyze concurrent and two-round attacks, including Wagner/generalized-birthday combination, Drijvers-style attacks, coordinator equivocation, challenge manipulation, and whether preprocessing or many sessions amortize the attack.
7. For threshold protocols, test share robustness, identifiable abort, complaint/blame procedures, malicious DKG, share refresh, repair, key resharing, and whether a failed session leaks information about shares or nonces.
8. For BLS and pairing-based aggregation, test rogue keys, same-message versus distinct-message modes, proof of possession, duplicate messages, infinity/identity elements, subgroup checks, batch randomization, and pairing-product edge cases.
9. Audit reductions and security definitions for plain versus registered-key models, algebraic/group models, ROM/QROM, one-more assumptions, adaptive corruptions, and tightness across users and sessions.
10. Validate any attack by producing a forgery, extracting a share/secret, causing verifier disagreement, or violating the exact robustness/availability claim; preserve protocol traces and independently verify the final signature.

## Output contract

- A participant, corruption, setup, and session model.
- A key-aggregation, nonce, transcript, and verification-equation audit.
- Attack records for rogue-key, concurrency, nonce, abort, share, aggregation, and batch-verification paths.
- A claim-level conclusion for unforgeability, robustness, accountability, and privacy.

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

- `BN06-FORK`
- `MUSIG18`
- `MUSIG2-21`
- `DRIJVERS19-MULTISIG`
- `RFC9591-FROST`
- `SHOUP00-THRSA`
- `LINDELL17-2ECDSA`
- `BLS01`
- `RFC6979`

Full records are bundled in `references/REFERENCES.md`.
