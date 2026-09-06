---
name: pairing-based-and-extension-field-analysis
description: "Analyzes pairing-based signatures, encryption, identity-based systems, and protocols through subgroup validation, embedding degree, extension-field discrete logs, TNFS/NFS variants, pairing equations, and aggregate/batch verification."
metadata:
  version: "0.1"
  display-name: "Pairing-Based and Extension-Field Analysis"
  tags: "pairings, bls, ibe, extension-field, tnfs, aggregate-signatures"
  requires: "pairing-parameters, construction, verification-equations"
  produces: "pairing-parameter-audit, dlp-estimates, pairing-protocol-tests"
---

# Pairing-Based and Extension-Field Analysis

## Use this skill when

The target uses bilinear or multilinear-looking maps, BLS signatures, pairing-based IBE, SNARK verification components, or pairing-friendly curves.

## Operating procedure

1. Record source and target groups, field characteristic/degree, curve family, subgroup orders/cofactors, embedding degree, twists, pairing type, Miller loop/final exponentiation, and encodings.
2. Map each security claim to the correct assumption: DLP in G1/G2/GT, CDH/co-CDH, XDH/SXDH, q-type assumptions, or knowledge assumptions. Do not substitute them silently.
3. Estimate generic attacks in source groups and finite-field DLP attacks in the target group using the appropriate NFS/TNFS/exTNFS or special-form model.
4. Audit curve-generation and extension-field parameters for special polynomial structure, small subgroups, weak twists, insufficient embedding degree, and outdated finite-field security estimates.
5. Analyze subgroup and invalid-point attacks, cofactor clearing, identity handling, subgroup checks, and cross-group encoding confusion.
6. For BLS/aggregate signatures, test rogue-key attacks, proof of possession, duplicate messages, message augmentation, key/message binding, batch randomization, and signature/public-key infinity cases.
7. For IBE/encryption/AKE, inspect identity hashing, domain separation, key extraction assumptions, key privacy, chosen-ciphertext transforms, and transcript binding.
8. Audit pairing-product equations for cancellation, omitted terms, alternative encodings, malformed proofs, and unsafe batch verification.
9. Include Shor estimates for classical deployments and separate source-group versus target-field bottlenecks.
10. Produce parameter-specific estimates and protocol tests rather than generic “pairing security” statements.

## Output contract

- A pairing/group/field parameter and assumption map.
- Source-group and target-field attack estimates.
- Subgroup, rogue-key, aggregate/batch, and encoding tests.
- Claim-specific findings for signatures, IBE/PKE, and protocols.

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
- `BLS01`
- `MOV93`
- `FREYRUCK94`
- `KB16-EXTNFS`
- `KIMBAR16-PAIRING`
- `LIMLEE97-SUBGROUP`
- `SHOR94`

Full records are bundled in `references/REFERENCES.md`.
