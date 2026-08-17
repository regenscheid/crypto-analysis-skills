---
name: key-agreement-and-ake-protocol-analysis
description: "Analyzes unauthenticated and authenticated key agreement for session matching, forward secrecy, KCI, unknown-key share, reflection, replay, identity/transcript binding, key confirmation, and hybrid composition."
metadata:
  version: "0.1"
  display-name: "Key Agreement and AKE Protocol Analysis"
  tags: "key-agreement, ake, forward-secrecy, kci, uks, transcript-binding"
  requires: "protocol-specification, session-model, key-establishment-primitive"
  produces: "ake-session-model, attack-traces, property-matrix"
---

# Key Agreement and AKE Protocol Analysis

## Use this skill when

The target derives a shared secret through DH/ECDH, RSA transport, KEMs, isogenies, or hybrids inside a protocol or standalone key-establishment scheme.

## Operating procedure

1. Define protocol roles, long-term and ephemeral keys, sessions, peer identities, matching conversations, state, transcript, negotiated algorithms, and the exact session-key derivation.
2. Choose and instantiate the security model: BR, CK, eCK, HMQV-style, contributory key agreement, or the protocol’s stated model. Record reveal, corruption, ephemeral-secret, and session-state queries plus freshness.
3. Trace authentication and key confirmation. Identify which transcript elements, identities, certificates, roles, public keys, nonces, groups, and algorithms are signed/MACed/KDF-bound.
4. Test replay, reflection, interleaving, unknown-key share, identity misbinding, role confusion, key-compromise impersonation, static/ephemeral key substitution, and state reuse.
5. Audit validation of peer public values: identity, subgroup/cofactor, curve/twist, all-zero/shared-secret checks, invalid encodings, and malicious parameter choices.
6. Analyze forward secrecy and post-compromise security under each corruption timing. Distinguish passive compromise from active attacks and erased versus retained state.
7. Check contributory behavior and key control: can one party force a known, low-entropy, repeated, or component-selected secret? Analyze failure and all-zero handling.
8. For hybrids, invoke the combiner skill and test downgrade, split views, asymmetric component failure, and transcript misbinding.
9. Model concurrency, retransmission, resumption, prekeys, group reuse, and multi-user/multi-session amplification in the deployed interface.
10. Produce complete attack traces with session labels and reveal chronology; map them to the exact AKE property rather than saying only “MITM.”

## Output contract

- A populated oracle/session model and transcript-binding map.
- Attack traces for KCI, UKS, reflection, replay, validation, and key-control hypotheses.
- A property matrix for secrecy, authentication, forward secrecy, and key confirmation.
- Protocol-level tests and mitigation requirements.

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

- `BR93-AKE`
- `CK01-AKE`
- `ECK07`
- `HMQV05`
- `NIST-SP800-56A`
- `NIST-SP800-56B`
- `RFC8446`
- `RFC9954`

Full records are bundled in `references/REFERENCES.md`.
