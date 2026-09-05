---
name: security-proof-rom-qrom-and-tightness-auditor
description: "Audits public-key security proofs, game hops, reductions, random-oracle programming, Fiat–Shamir extraction, correctness events, multi-user losses, and concrete tightness in classical and quantum random-oracle models."
metadata:
  version: "0.1"
  display-name: "Security Proof, ROM/QROM, and Tightness Auditor"
  tags: "proof-audit, rom, qrom, fiat-shamir, tightness"
  requires: "security-proof, implementation, claim-matrix"
  produces: "proof-audit, recomputed-bounds, rom-qrom-findings"
---

# Security Proof, ROM/QROM, and Tightness Auditor

## Use this skill when

A scheme’s security rests on a reduction, random oracle, forking lemma, measure-and-reprogram argument, or concrete bound that must be checked against the implementation and claimed parameters.

## Operating procedure

1. Copy the theorem, definitions, parameters, oracle model, and exact advantage bound. Record the proof and specification versions separately.
2. Reconstruct the sequence of games and the simulator/reduction interfaces. For each hop state whether it is exact, computational, statistical, or conditioned on a bad event.
3. Check random-oracle programming: domains, prefixes, collision handling, adaptive queries, challenge timing, reprogrammed points, and whether the implementation performs the same domain separation.
4. For Fiat–Shamir, audit special soundness, honest-verifier zero knowledge, commitment binding, challenge entropy, aborts/restarts, extraction, forking or measure-and-reprogram loss, and multi-round compression.
5. For KEM/PKE transforms, audit re-encryption checks, implicit rejection, plaintext checking, randomness recovery, decryption failures, and the precise assumptions needed by the transform theorem.
6. Recompute all concrete losses: query powers, guessing factors, multi-user terms, statistical distances, correctness/failure probability, reduction runtime, and success amplification.
7. Check QROM claims independently. A classical ROM proof, classical rewinding, or classical oracle-programming step does not automatically survive superposition queries.
8. Verify that public-key, ciphertext, signature, and transcript encodings used in the implementation preserve uniqueness and the proof’s parsing assumptions.
9. Classify issues as exposition gaps, repairable proof defects, theorem/implementation mismatch, loose but valid bound, unsupported QROM claim, or attack-enabling flaw.
10. Create attack hypotheses only when the failed proof step exposes a concrete adversarial strategy; otherwise report a proof finding, not a break.

## Output contract

- A game-hop and reduction audit with source locators.
- A recomputed concrete bound for each parameter set.
- A ROM/QROM programming and Fiat–Shamir checklist.
- A classified list of proof defects, instantiation mismatches, and attack hypotheses.

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

- `BR93-ROM`
- `PS00-FORK`
- `BN06-FORK`
- `UNRUH17-QROM`
- `KLS18-FSQROM`
- `FO99`
- `HHK17-FO`
- `HULSING22-TIGHT`

Full records are bundled in `references/REFERENCES.md`.
