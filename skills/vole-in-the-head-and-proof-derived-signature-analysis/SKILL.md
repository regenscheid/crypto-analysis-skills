---
name: vole-in-the-head-and-proof-derived-signature-analysis
description: "Analyzes VOLE-in-the-head, QuickSilver-style consistency checks, FAEST-like signatures, and related proof-derived signatures through VOLE correlations, commitments, field checks, challenge structure, transcript compression, and QROM security."
metadata:
  version: "0.1"
  display-name: "VOLE-in-the-Head and Proof-Derived Signature Analysis"
  tags: "vole-in-the-head, faest, quicksilver, proof-derived-signatures, qrom"
  requires: "voleith-signature, relation, implementation, proof"
  produces: "vole-transcript-map, soundness-audit, forgery-estimates"
---

# VOLE-in-the-Head and Proof-Derived Signature Analysis

## Use this skill when

The target derives a signature from VOLE correlations, vector commitments, QuickSilver-like proofs, or a proof of knowledge of a symmetric-key witness such as an AES key.

## Operating procedure

1. Specify the witness relation/circuit, field, VOLE correlations, sender/receiver values, commitments, vector commitments or hashes, consistency checks, challenges, repetitions, and compressed transcript.
2. Transcribe generation and verification of every correlation and check. Identify which values are committed before challenges and which are reconstructed from seeds.
3. Derive soundness from the exact algebraic check polynomial, field size, challenge distribution, number of checks, and any batching. Include correlations between checks and repetitions.
4. Audit VOLE generation and seed expansion for reuse, related correlations, all-zero/degenerate challenges, linear dependencies, selective opening, and malformed values outside the intended field/range.
5. Analyze QuickSilver or analogous proof compilation: multiplication checks, degree, batching coefficients, statement/witness binding, and whether omitted circuit constraints create accepting false statements.
6. Audit commitment/hash domains, salts, public key/message/context, parameter identifiers, transcript framing, and collision or ambiguous-parsing possibilities.
7. Analyze Fiat–Shamir/QROM security, challenge grinding, multi-user/multi-target loss, and the exact applicability of VOLE-in-the-head QROM results to the implemented compression and abort behavior.
8. Analyze the underlying witness relation separately (for example AES key recovery) and determine whether relation cryptanalysis or weak keys actually yields a signature forgery within the game.
9. Build an independent small-instance verifier/extractor and exhaustively test false statements, malformed correlations, transcript splicing, and challenge edge cases.
10. Recompute the minimum complete forgery cost across algebraic cheating, relation recovery, commitment collision, and proof-reduction loss.

## Output contract

- A VOLE/correlation/check and transcript map.
- Concrete soundness, batching, and QROM audits.
- Correlation-reuse, malformed-input, and transcript tests.
- Complete forgery estimates and independent verifier artifacts.

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

- `VOLEITH23`
- `QUICKSILVER21`
- `FAEST-SPEC`
- `VOLEQROM26`
- `FS86`
- `KLS18-FSQROM`

Full records are bundled in `references/REFERENCES.md`.
