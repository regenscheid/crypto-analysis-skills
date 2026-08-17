---
name: pke-security-and-adaptive-oracle-analysis
description: "Analyzes public-key encryption against one-way, IND-CPA, IND-CCA, non-malleability, plaintext-validity, padding-oracle, rerandomization, and adaptive-decryption attacks across classical and post-quantum schemes."
metadata:
  version: "0.1"
  display-name: "PKE Security and Adaptive-Oracle Analysis"
  tags: "pke, ind-cpa, ind-cca, padding-oracle, malleability"
  requires: "pke-specification, implementation, claim-row"
  produces: "pke-oracle-model, pke-attack-records, oracle-tests"
---

# PKE Security and Adaptive-Oracle Analysis

## Use this skill when

The target exposes Encrypt/Decrypt or a PKE core inside a KEM, hybrid encryption, envelope format, or protocol.

## Operating procedure

1. Formalize the exact PKE game, message space/distribution, challenge restriction, decryption-oracle behavior, public-key validity assumptions, and multi-user setting.
2. Decompose encryption into trapdoor/core operation, randomness generation, encoding/padding, redundancy/checking, symmetric wrapping, and serialization. Map which values are public, secret, recomputed, or validated.
3. Test algebraic malleability, homomorphism, rerandomization, ciphertext scaling/translation, component substitution, and relations that preserve or predict plaintext validity.
4. Enumerate adaptive feedback channels: explicit errors, validity bits, length or format distinctions, protocol alerts, key-confirmation behavior, retransmission, and externally visible state changes. Model noisy or rate-limited oracles explicitly.
5. Analyze message entropy and structure. Apply small-root, broadcast, common-modulus, related-message, partial-information, and hidden-number techniques only when their prerequisites are present.
6. Check public-key registration and malformed-key attacks, including key substitution, invalid group elements, noncanonical keys, and adversarially generated parameters.
7. Audit padding/encoding proofs and implementation behavior. Verify that ciphertext parsing, randomness recovery, plaintext checking, and error unification match the theorem.
8. Attempt to elevate any plaintext predicate or validity distinguisher to adaptive message/key recovery; count queries, oracle noise, candidate intervals/lists, and verification.
9. Compare the complete attack with one-way/IND-CPA/IND-CCA baselines at equal success probability and state whether the attack reaches the advertised interface.
10. Produce minimized oracle tests and mitigations that preserve the intended game rather than merely hiding one error string.

## Output contract

- A PKE game/oracle model and construction decomposition.
- A catalog of algebraic, padding, validity, malformed-key, and adaptive-oracle hypotheses.
- Complete attack records for any exploitable predicates or recovery procedures.
- Minimized tests and claim-preserving mitigation requirements.

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

- `GM84-PKE`
- `BDPR98-PKE`
- `CS98-CCA`
- `RFC8017`
- `HASTAD88`
- `COP96-SMALLROOTS`
- `BLE98`
- `MANGER01`

Full records are bundled in `references/REFERENCES.md`.
