---
name: scheme-structure-and-assumption-mapper
description: "Builds a machine-usable map of a public-key scheme’s algorithms, algebraic objects, distributions, encodings, boundaries, transforms, validation rules, and assumption chain. Use before generating or transferring attacks."
metadata:
  version: "0.1"
  display-name: "Scheme Structure and Assumption Mapper"
  tags: "structure, assumptions, algorithms, encodings, distributions"
  requires: "specification, implementation, parameter-sets"
  produces: "design-assumption-graph, parameter-table, attack-surface-map"
---

# Scheme Structure and Assumption Mapper

## Use this skill when

The target must be decomposed beyond its family name so attack prerequisites can be mapped to exact operations and interfaces.

## Operating procedure

1. Transcribe KeyGen, Encaps/Decaps or Encrypt/Decrypt, Sign/Verify, and session-key derivation into side-effect-explicit pseudocode, including all aborts and implicit rejection branches.
2. Record algebraic domains: groups, rings, fields, modules, lattices, codes, varieties, isogeny graphs, polynomial systems, hash trees, or proof systems; include dimensions, moduli, orders, and representations.
3. Map every random variable and distribution: seeds, secrets, errors, nonces, salts, challenges, masks, Gaussian or bounded samples, code errors, and rejection-conditioned outputs.
4. Draw data dependencies from secret material to public keys, ciphertexts, signatures, transcripts, validation decisions, and derived keys. Mark repeated, cached, or cross-session values.
5. Identify construction boundaries: KEM transform, PKE core, DEM, Fiat–Shamir layer, commitment layer, Merkle authentication, combiner, KDF, transcript hash, and protocol framing.
6. Inventory encodings and parsing rules, including canonicality, lengths, compression, sign conventions, point/subgroup representation, public-key checks, and malformed-input behavior.
7. Record stated assumptions and the exact reduction chain, including decisional/search variants, structured versus unstructured problems, average/worst case, random-oracle use, and correctness hypotheses.
8. Identify symmetries, automorphisms, subfields, subgroups, low-rank structure, quasi-cyclic structure, sparsity, repeated matrices, shared parameters, and any public auxiliary information.
9. Mark implementation choices permitted by the specification but not fixed by the mathematical description, especially sampling precision, constant-time requirements, validation, and error handling.
10. Emit explicit attack surfaces and route each to construction and family skills.

## Output contract

- A design/assumption graph with algorithms, domains, distributions, boundaries, and dependency edges.
- A versioned parameter and encoding table.
- A reduction/assumption map and attack-surface inventory.
- A routing list for the applicable construction and family skills.

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

- `NIST-SP800-227`
- `NIST-FIPS186-5`
- `NIST-SP800-56A`
- `NIST-SP800-56B`
- `NIST-FIPS203`
- `NIST-FIPS204`
- `NIST-FIPS205`

Full records are bundled in `references/REFERENCES.md`.
