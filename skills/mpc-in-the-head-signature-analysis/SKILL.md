---
name: mpc-in-the-head-signature-analysis
description: "Analyzes MPC-in-the-head and related proof-derived signatures—including Picnic, ZKBoo/ZKB++, MQOM, and SDitH-style systems—through simulated views, commitments, challenge combinatorics, seed trees/PPRFs, transcript compression, soundness, and Fiat–Shamir/QROM security."
metadata:
  version: "0.1"
  display-name: "MPC-in-the-Head Signature Analysis"
  tags: "mpc-in-the-head, picnic, mqom, sdith, proof-derived-signatures"
  requires: "mpcith-signature, relation, implementation, proof"
  produces: "mpcith-transcript-map, soundness-audit, forgery-estimates"
---

# MPC-in-the-Head Signature Analysis

## Use this skill when

The target proves knowledge of a witness by simulating an MPC execution in the signer’s head and opening selected views or parties.

## Operating procedure

1. Specify the proved relation/circuit, secret sharing, number of parties, MPC protocol, views, tapes/seeds, commitments, output checks, challenge space, opened/hidden subsets, repetitions, and signature compression.
2. Verify completeness and reconstruct the verifier’s exact view regeneration, commitment recomputation, transcript hashing, and consistency checks for every challenge type.
3. Derive soundness per repetition and globally from the actual challenge combinatorics, admissible cheating strategies, special soundness/extraction threshold, and correlated/parallel repetitions.
4. Audit commitments and seed expansion: binding/hiding assumptions, salt/address/domain separation, seed-tree or PPRF reconstruction, unopened leaves, duplicate nodes, and cross-repetition reuse.
5. Analyze transcript compression and omitted commitments/views for ambiguity, collision, selective-opening, splicing, and inconsistent recomputation across implementations.
6. Search for repeated randomness, state rollback, commitment reuse, challenge grinding, biased challenges, malformed public keys/statements, response malleability, and low-cost partial simulations.
7. For Fiat–Shamir, audit message/public-key binding, challenge derivation, salts, ROM/QROM proof, forking/measure-and-reprogram loss, multi-user/multi-target effects, and abort/retry behavior.
8. Analyze the underlying relation separately: LowMC/key recovery for Picnic, MQ inversion for MQOM, syndrome decoding for SDitH, and whether a faster relation solver yields a full forgery.
9. Exhaustively enumerate small transcripts/challenges and build an independent verifier/extractor to validate soundness and parsing.
10. Recompute concrete forgery cost from relation attacks, transcript cheating, hash collisions, and proof losses; report the minimum complete path.

## Output contract

- An MPC/view/challenge and commitment map.
- Concrete soundness/extraction and ROM/QROM audits.
- Seed-tree, transcript, reuse, grinding, and malformed-input tests.
- Complete forgery estimates for the target MPC-in-the-head signature.

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

- `IKOS07-MPCITH`
- `ZKBOO16`
- `ZKBPP17`
- `KKW18`
- `KALES20-PICNIC`
- `BUI24-MPCITH`
- `PICNIC-SPEC`
- `SDITH-SPEC`
- `FS86`
- `KLS18-FSQROM`

Full records are bundled in `references/REFERENCES.md`.
