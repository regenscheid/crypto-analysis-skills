---
name: identity-and-attribute-based-encryption-analysis
description: "Analyzes IBE, HIBE, KP-ABE, CP-ABE, and related fine-grained encryption for selective/adaptive security, authority and key-generation trust, collusion resistance, policy/identity encoding, delegation, revocation, and CCA composition."
metadata:
  version: "0.1"
  display-name: "Identity- and Attribute-Based Encryption Analysis"
  tags: "ibe, hibe, abe, kp-abe, cp-abe, collusion, pairings, lattices"
  requires: "scheme-specification, authority-model, policy-language, parameter-set"
  produces: "ibe-abe-security-model, policy-map, collusion-tests, reduction-findings"
---

# Identity- and Attribute-Based Encryption Analysis

## Use this skill when

The target derives decryption capability from an identity, hierarchy, attribute set, access policy, or authority-issued secret key, using pairings, lattices, or another public-key family.

## Operating procedure

1. Classify the construction and claim: IBE/HIBE, key-policy ABE, ciphertext-policy ABE, predicate/functional variant, outsourced decryption, multi-authority system, anonymous/key-private variant, or revocable/time-bound system.
2. Formalize setup authorities, master-secret exposure, identity/attribute registration, key extraction queries, delegation, corruption, collusion sets, challenge restrictions, selective versus adaptive choice, chosen-ciphertext access, and the exact success event.
3. Transcribe identity, policy, attribute, time, and context encodings; hash-to-group or lattice gadget mappings; canonical forms; wildcards; duplicate attributes; ordering; negation; and domain separation across key and ciphertext components.
4. Map every ciphertext and key component to the access structure or predicate. Verify correctness at threshold boundaries, repeated attributes, unsatisfied policies, malformed shares, delegated keys, and mixed-authority inputs.
5. Analyze collusion resistance by combining keys from different users, identities, attributes, epochs, or authorities. Search for linear dependencies, shared randomness, reusable blinding factors, subgroup components, and equivalent policies.
6. For pairing systems, audit subgroup membership, composite/prime-order conversions, dual-system assumptions, parameter generation, pairing-friendly curve security, and whether nominal source-group hardness survives embedding and extension-field attacks.
7. For lattice systems, instantiate exact LWE/SIS dimensions, trapdoors, gadget matrices, delegation noise growth, public auxiliary samples, policy depth, correctness margins, and estimator settings.
8. Audit security reductions for selective-to-adaptive loss, artificial aborts, complexity leveraging, dual-system hybrids, random-oracle programming, q-type/nonstandard assumptions, and multi-user/multi-authority degradation.
9. Analyze revocation, update keys, outsourced/delegated decryption, transformation keys, verification of partial decryptions, CCA transforms, and protocol reactions that reveal policy satisfaction or decryption validity.
10. Validate candidate attacks with generated users/policies and independently checked decryptions; distinguish master-key recovery, user-key recovery, collusion, policy bypass, anonymity loss, and proof-only findings.

## Output contract

- An authority, identity/policy, query, and corruption security model.
- A component-to-policy and assumption/reduction map.
- Collusion, encoding, subgroup/lattice, delegation, revocation, and CCA attack records.
- Separate conclusions for confidentiality, anonymity, collusion resistance, and authority trust.

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

- `BF01-IBE`
- `WATERS05-IBE`
- `SW05-FUZZYIBE`
- `GPSW06-ABE`
- `BSW07-CPABE`
- `LW10-DUALSYSTEM`
- `GVW13-LATTICEABE`
- `BDPR98-PKE`
- `CS98-CCA`

Full records are bundled in `references/REFERENCES.md`.
