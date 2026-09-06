---
name: isogeny-and-quaternion-signature-analysis
description: "Analyzes SQIsign-like and other isogeny/quaternion signatures through quaternion-ideal and endomorphism-ring representations, KLPT-style algorithms, commitment/challenge/response paths, norm equations, special soundness, response compression, key validation, and quantum hidden-shift/path attacks."
metadata:
  version: "0.1"
  display-name: "Isogeny and Quaternion Signature Analysis"
  tags: "sqisign, isogeny-signatures, quaternion-ideals, endomorphism-rings, klpt"
  requires: "signature-specification, quaternion-data, proof"
  produces: "quaternion-map, signature-attacks, encoding-findings"
---

# Isogeny and Quaternion Signature Analysis

## Use this skill when

The target signs using supersingular isogenies, quaternion ideals, endomorphism rings, orientations, SQIsign-like identification, or related group-action proofs.

## Operating procedure

1. Transcribe key generation and the identification/signature protocol in both curve/isogeny and quaternion-ideal language. Record maximal orders, ideals, norms, orientations, auxiliary structures, and all conversions.
2. Map assumptions and algorithms: endomorphism-ring computation, isogeny path, ideal equivalence, strong approximation/KLPT, norm equations, Deuring correspondence, hidden shift, and proof-of-knowledge properties.
3. Verify commitment, challenge, and response equations; identify what two or more accepting transcripts extract and whether exceptional challenges, nonunique paths, or equivalent ideals defeat extraction.
4. Analyze signer algorithms and distributions: random ideal/path sampling, norm selection, smoothness searches, rejection, compression, canonicalization, and whether output distributions depend on the secret order/ideal.
5. Search for transcript relations across many signatures, repeated commitments/randomness, biased challenges, equivalent responses, low-norm combinations, and lattice/algebraic recovery of secret ideal/order information.
6. Audit response compression/decompression, curve and isogeny encoding, orientation/sign bits, canonical j-invariants, exceptional curves, torsion bases, subgroup membership, and malformed public keys/signatures.
7. Analyze Fiat–Shamir and QROM proof losses, transcript/domain binding, deterministic signing, multi-user/multi-target settings, and grinding.
8. Estimate classical and quantum endomorphism/path/hidden-shift attacks for exact parameters and distinguish attacks on key generation, identification soundness, and signature forgery.
9. Validate mathematical conversions and verifier equations on small examples and independent implementations; require explicit accepted forgeries or recovered equivalent secrets for strong claims.
10. Track current candidate versions and withdrawals/changes separately; do not transfer a result across parameter/specification revisions without a requirement matrix.

## Output contract

- A curve–quaternion–ideal representation map.
- Identification/extraction and signer-distribution analyses.
- Encoding, malformed-input, and transcript-relation tests.
- Classical/quantum forgery and key-recovery estimates.

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

- `SQISIGN20`
- `SQISIGN-SPEC`
- `CSIDH18`
- `DELFS16-ISO`
- `CJS14-ISOGENYQ`
- `KUP05-HIDDENSHIFT`
- `FS86`
- `UNRUH17-QROM`
- `NIST-IR8610`
- `NIST-R3SIG-2026`

Full records are bundled in `references/REFERENCES.md`.
