---
name: hidden-order-class-group-and-vdf-analysis
description: "Analyzes class-group and RSA hidden-order constructions, strong-RSA assumptions, unknown-order groups, accumulators, time-lock/VDF protocols, discriminant generation, relation finding, proof soundness, and quantum hidden-shift/factoring threats."
metadata:
  version: "0.1"
  display-name: "Hidden-Order, Class-Group, and VDF Analysis"
  tags: "hidden-order, class-groups, vdf, strong-rsa, accumulators"
  requires: "group-setup, construction, parameters"
  produces: "hidden-order-audit, relation-estimates, vdf-proof-findings"
---

# Hidden-Order, Class-Group, and VDF Analysis

## Use this skill when

The target uses a class group, RSA group of unknown order, strong-RSA assumption, accumulator, verifiable delay function, or hidden-order action.

## Operating procedure

1. Specify the group representation, unknown-order generation, discriminant or RSA modulus generation, element sampling, normalization/canonicalization, and trusted-setup assumptions.
2. Map claims to factoring, strong RSA, adaptive root, class-group DLP, principal-ideal/relation problems, sequentiality, or proof-of-exponentiation assumptions.
3. Estimate classical group operations and the best class-group relation/DLP algorithms for the exact discriminant size and structure; state memory and precomputation.
4. Audit parameter generation for hidden trapdoors, smooth orders, nonfundamental or special discriminants, reused moduli, shared factors, and adversarially selected group elements.
5. Test membership, canonicality, identity, torsion, ambiguous forms, malformed proofs, and whether invalid elements escape the intended group or reduce order.
6. For VDFs, separate evaluation sequentiality, verification soundness, uniqueness, challenge derivation, batching/aggregation, and proof system assumptions. Analyze parallelism and preprocessing precisely.
7. Analyze proof-of-exponentiation and accumulator equations for adaptive roots, omitted binding, replay, nonmembership/membership confusion, and batch cancellation.
8. For quantum analysis, distinguish factoring/Shor threats in RSA groups from hidden-shift or class-group action algorithms and state oracle/qRAM assumptions.
9. Audit implementation arithmetic and normalization only insofar as it changes the black-box accepted language or mathematical result; route physical leakage separately.
10. Map findings to group-order secrecy, relation finding, proof soundness, sequentiality, or protocol composition.

## Output contract

- A hidden-order group and setup-assumption audit.
- Classical and quantum relation/DLP/factoring estimates.
- Element/proof validation and VDF soundness tests.
- Property-specific findings for accumulators, VDFs, and protocols.

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

- `BW88-CLASSGROUP`
- `HAFNER89-CLASSGROUP`
- `BP97-STRONGRSA`
- `WESO19-VDF`
- `PIET19-VDF`
- `SHOR94`
- `KUP05-HIDDENSHIFT`

Full records are bundled in `references/REFERENCES.md`.
