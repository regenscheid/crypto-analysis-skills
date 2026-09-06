---
name: structured-ring-and-ideal-lattice-analysis
description: "Analyzes algebraic structure in Ring/Module-LWE, NTRU, ideal- and module-lattice systems through subfield/subring attacks, automorphisms, ideal generators, norm/resultant relations, structured lattice reduction, and assumption transfer. It complements scheme-specific KEM and signature skills."
metadata:
  version: "0.1"
  display-name: "Structured Ring, Module, and Ideal-Lattice Analysis"
  tags: "ntru, ideal-lattice, module-lattice, subfield, short-generator"
  requires: "ring-definition, public-relation, key-distribution"
  produces: "ntru-structure-map, structured-attacks, transfer-analysis"
---

# Structured Ring, Module, and Ideal-Lattice Analysis

## Use this skill when

A target relies on cyclotomic or other quotient rings, ideals/modules, NTRU relations, short generators, automorphisms, subfields, subrings, or structured samples whose hardness may differ from unstructured lattices.

## Operating procedure

1. Write the exact ring/module, polynomial, modulus, quotient, involution, units, ideals/modules, dimensions, key distributions, invertibility conditions, and public relation. Distinguish the algebraic object from its coefficient embedding.
2. Construct the public key lattice(s) and identify what a sufficiently short vector reveals: secret pair, equivalent key, signing basis, principal generator, decryption capability, or only an unrelated short relation.
3. Evaluate direct lattice reduction and hybrid lattice/MITM attacks with correct embedding, scaling, norm geometry, secret sparsity, rotations/automorphisms, and verification.
4. Analyze subfield/subring and tower attacks: factor the defining polynomial over relevant fields, map norms/traces/projections, identify reduced-dimensional lattices, and verify whether recovered projected information lifts to a usable key.
5. Audit ideal versus module structure, principal-ideal status, unit ambiguity, short-generator recovery, class-group or cyclotomic-unit information, and whether literature assumptions match the target public object.
6. Analyze key equivalence and rotation classes, weak keys, noninvertible elements, resultants, gcd relations, and public-key canonicality.
7. For signatures, test historical transcript/basis leakage, Gaussian output dependence, cached tree/basis information, and the exact relationship between a short generator and the private signing trapdoor.
8. For encryption/KEM, integrate decryption failures, product-form/sparse secrets, ciphertext validity, transform behavior, and NTRU Prime-style changes intended to reduce structure.
9. Use small-ring Sage experiments to verify ideal/module maps and lift conditions; do not infer full-scale attacks from toy factorization without a scaling derivation.
10. Classify transfers carefully: an attack on an overstretched ideal-lattice assumption or historical NTRUSign does not automatically break modern NTRU KEMs or Falcon.

## Output contract

- An exact ring/ideal/module and public-lattice specification.
- Direct, hybrid, subfield, and short-generator attack records.
- Toy-instance algebraic validation and lift/verification tests.
- A transfer analysis for the exact NTRU-derived target.

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

- `NTRU98`
- `CS97-NTRU`
- `HG07-NTRUHYBRID`
- `ABD16-SUBFIELD`
- `GS02-IDEALGEN`
- `CDPR16-IDEAL`
- `NTRUPRIME17`
- `NTRUSIGN03`
- `NR06-HPP`
- `FALCON18`

Full records are bundled in `references/REFERENCES.md`.
