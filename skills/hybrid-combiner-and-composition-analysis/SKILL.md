---
name: hybrid-combiner-and-composition-analysis
description: "Analyzes classical–post-quantum and same-family KEM, key-exchange, encryption, and signature combiners; covers transcript binding, downgrade resistance, component robustness, non-separability, and guarantees when one component fails."
metadata:
  version: "0.1"
  display-name: "Hybrid Combiner and Composition Analysis"
  tags: "hybrid, combiner, pqc-migration, composition, downgrade"
  requires: "component-specifications, protocol-profile, security-goal"
  produces: "combiner-security-matrix, downgrade-tests, composition-findings"
---

# Hybrid Combiner and Composition Analysis

## Use this skill when

A protocol combines two or more KEMs, key exchanges, public-key encryptions, or signatures, especially during post-quantum migration or when one component may be malicious, weak, malformed, or later compromised.

## Operating procedure

1. Identify the composition goal: confidentiality or unforgeability if any component holds, security only if all hold, authentication, contributory behavior, non-separability, downgrade resistance, backward compatibility, or graceful migration. Formalize the corresponding game.
2. Map every component’s exact game, key ownership, validation rules, failure behavior, public inputs, secret outputs, and adversary model. Do not combine incompatible guarantees by name alone.
3. Transcribe the combiner: concatenation/extraction or signature tuple, KDF/hash, domain separation, labels, component ordering, algorithm identifiers, transcript/identity/message binding, framing, verification policy, and error handling.
4. Test robustness to one malicious or broken component: chosen shared secret, all-zero output, invalid key, adaptive failure, key control, related ciphertext/signature, stripping, substitution, replay, and verifier disagreement.
5. Audit downgrade and misbinding paths in negotiation, certificates, algorithm identifiers, transcripts, resumption, and fallback. Verify that the derived key commits to the complete algorithm suite and peer identities.
6. Analyze correlated randomness, shared seeds, reused static keys, component interactions, and whether one component leaks or constrains the other.
7. Check the proof theorem’s assumptions, tightness, random-oracle/KDF model, and treatment of malformed inputs. Map protocol behavior to the theorem exactly.
8. Recompute multi-user and multi-session bounds and account for component correctness/failure probabilities and asymmetric rejection behavior.
9. Design component-substitution, split-view, downgrade, invalid-input, and one-component-compromise tests with explicit expected outcomes.
10. State the strongest property actually obtained when zero, one, or multiple components remain secure.

## Output contract

- A component and combiner security matrix.
- A transcript/KDF/domain-separation map.
- One-component-compromise, downgrade, and misbinding test cases.
- A claim-level conclusion for each compromise pattern.

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

- `BINDEL18-HYBRID`
- `GIACON18-COMBINERS`
- `RFC9180`
- `RFC9794`
- `RFC9954`
- `RFC8446`
- `RFC9955`
- `RFC10024`

Full records are bundled in `references/REFERENCES.md`.
