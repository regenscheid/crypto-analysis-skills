---
name: digital-signature-forgery-and-malleability-analysis
description: "Analyzes classical and post-quantum signatures for EUF/SUF forgery, signature and public-key malleability, key substitution, message/context confusion, batch/aggregate verification issues, and signing-oracle exploitation."
metadata:
  version: "0.1"
  display-name: "Digital-Signature Forgery and Malleability Analysis"
  tags: "signatures, forgery, malleability, key-substitution, euf-cma, suf-cma"
  requires: "signature-specification, implementation, security-claim"
  produces: "signature-game-map, forgery-hypotheses, malleability-tests"
---

# Digital-Signature Forgery and Malleability Analysis

## Use this skill when

The target provides Sign/Verify or derives signatures from identification, trapdoor sampling, hashes, codes, lattices, multivariate maps, isogenies, or proof systems.

## Operating procedure

1. Formalize the signature game: EUF-CMA or SUF-CMA, stateful/randomized/deterministic signing, signing and hash oracles, public-key registration, multi-user setting, quantum access, and message/context domain.
2. Transcribe key generation, signing, verification, retries/aborts, randomness/nonce generation, hashing, challenge derivation, and serialization. Identify all equations a valid signature satisfies.
3. Search for algebraic and representational malleability: sign changes, equivalent points/polynomials/vectors, noncanonical encodings, challenge collisions, linear combinations, rerandomization, and alternative transcripts for the same message.
4. Analyze message and context binding: prehash variants, domain separation, parameter identifiers, application contexts, public-key commitment, and cross-protocol or cross-algorithm reuse.
5. Test signing-oracle leverage: nonce reuse/bias, correlated masks, rejection information, chosen-message structure, related keys, state rollback, one-time-key reuse, and repeated commitments.
6. For identification/Fiat–Shamir signatures, invoke the dedicated FS/QROM skill; for sampling signatures, invoke the sampling skill; for family-specific equations, invoke the relevant mathematical module.
7. Audit verification edge cases, public-key validation, batch/aggregate equations, rogue-key defenses, duplicate messages/keys, and partial verification shortcuts.
8. Elevate any structural relation to a forgery by proving freshness, acceptance, and oracle compliance; count queries, candidates, false positives, and verification.
9. Distinguish key recovery, existential forgery, strong forgery, key substitution, denial of service, and non-repudiation concerns. Map each to the exact claim.
10. Produce minimized forgery/malleability tests and recompute concrete security in single- and multi-user settings.

## Output contract

- A signature game and verification-equation map.
- A malleability, key-substitution, and context-binding test suite.
- Complete forgery or key-recovery records where applicable.
- Claim-level classification under EUF/SUF and multi-user/QROM models.

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

- `GMR88-SIG`
- `BR96-PSS`
- `FS86`
- `PS00-FORK`
- `NIST-FIPS186-5`
- `RFC6979`
- `RFC8032`
- `NIST-FIPS204`
- `NIST-FIPS205`

Full records are bundled in `references/REFERENCES.md`.
