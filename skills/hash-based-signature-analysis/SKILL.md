---
name: hash-based-signature-analysis
description: "Analyzes stateful and stateless hash-based signatures—Lamport/WOTS+, Merkle trees, LMS/HSS, XMSS/XMSSMT, SPHINCS+/SLH-DSA—through exact hash assumptions, state management, hypertree/FORS structure, multi-target effects, domain separation, and verification parsing."
metadata:
  version: "0.1"
  display-name: "Hash-Based Signature Analysis"
  tags: "hash-based-signatures, slh-dsa, sphincs, xmss, lms, wots"
  requires: "signature-specification, hash-instantiations, operational-model"
  produces: "hash-assumption-map, state-audit, forgery-estimates"
---

# Hash-Based Signature Analysis

## Use this skill when

The target is a one-time, few-time, Merkle-tree, hypertree, LMS/XMSS, SPHINCS+/SLH-DSA, or other hash-based signature scheme.

## Operating procedure

1. Transcribe the hierarchy: OTS or few-time component, chains, authentication tree/hypertree, FORS or equivalent, address format, masks/tweaks, randomized hashing, message digest split, and signature encoding.
2. Map each claim to one-wayness, second-preimage, collision, multi-function/multi-target, pseudorandom-function, or tweakable-hash properties. Do not replace all of them with “hash strength.”
3. For stateful schemes, audit index allocation, durable state, rollback, cloning, backup/restore, concurrency, crash consistency, exhaustion, and multi-device coordination. Demonstrate the consequence of repeated OTS keys.
4. For stateless schemes, derive the exact number of reachable targets across WOTS/FORS/tree nodes, users, signatures, and layers; apply the scheme’s security proof and current multi-target bounds rather than a naïve digest-size rule.
5. Analyze chain structure, checksum, base-w encoding, message-digit distributions, forgery direction, partial chain exposure, and repeated/related signatures.
6. Audit address/domain separation and robust/simple variants: every hash invocation must bind function type, layer, tree, leaf, chain, step, and key context as specified.
7. Test noncanonical signatures, alternate encodings, out-of-range indices, tree-address truncation, malformed authentication paths, integer overflow, and verifier acceptance differences.
8. Analyze randomness/optrand handling, deterministic modes, faulted or repeated randomness, secret-seed derivation, and whether message hashing exposes chosen-target advantages.
9. Recompute classical and quantum preimage/collision/multi-target estimates with exact query model and include signature-volume limits.
10. Conclude separately on state safety, one-time/few-time security, tree authentication, overall EUF-CMA bounds, implementation parsing, and parameter category.

## Output contract

- A component/hash-assumption and address-domain map.
- State-management or stateless multi-target analysis.
- OTS/chain/tree and malformed-signature attack tests.
- Classical/quantum security estimates for the exact signature volume.

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

- `LAMPORT79`
- `MERKLE79`
- `WOTS89`
- `HULSING13-WOTSPLUS`
- `RFC8391-XMSS`
- `RFC8554-LMS`
- `NIST-SP800-208`
- `SPHINCS15`
- `SPHINCSPLUS19`
- `HULSING16-MULTITARGET`
- `HULSING22-TIGHT`
- `PERLNER22-SPHINCS`
- `NIST-FIPS205`

Full records are bundled in `references/REFERENCES.md`.
