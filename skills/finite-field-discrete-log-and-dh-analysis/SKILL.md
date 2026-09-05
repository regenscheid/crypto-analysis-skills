---
name: finite-field-discrete-log-and-dh-analysis
description: "Analyzes finite-field discrete-logarithm and Diffie–Hellman systems using generic algorithms, subgroup decomposition, index calculus/NFS, parameter precomputation, small-subgroup attacks, and protocol validation."
metadata:
  version: "0.1"
  display-name: "Finite-Field Discrete-Log and DH Analysis"
  tags: "finite-field, discrete-log, diffie-hellman, subgroup, nfs-dl"
  requires: "field-group-parameters, construction, protocol-interface"
  produces: "dlog-estimates, subgroup-attacks, parameter-audit"
---

# Finite-Field Discrete-Log and DH Analysis

## Use this skill when

The target uses DSA, ElGamal, finite-field DH/MQV, Schnorr-type signatures over finite fields, or a finite-field pairing subgroup.

## Operating procedure

1. Record field size and representation, subgroup order/factorization, generator provenance, cofactor, public parameters, exponent distribution, static/ephemeral reuse, validation, and standardized group sharing.
2. Compute generic DLP baselines using baby-step/giant-step, Pollard rho/kangaroo, parallel collision search, Pohlig–Hellman decomposition, and multi-target effects.
3. Select the appropriate index-calculus family for the field: prime-field NFS-DL, special-NFS variants, extension/small-characteristic algorithms, and descent. Record precomputation versus individual-log costs.
4. Audit parameter generation for trapdoored or special-form primes, smooth subgroup factors, weak generators, insufficient subgroup size, and reusable precomputation across deployments.
5. Analyze small-subgroup and subgroup-confinement attacks with actual peer validation, exponent reuse, oracle behavior, CRT reconstruction, and session protocol.
6. Analyze ElGamal/DSA/Schnorr construction-specific issues: nonce relations, malleability, plaintext structure, re-randomization, proof of possession, and challenge/hash binding.
7. For authenticated key agreement, test UKS, KCI, reflection, identity/transcript binding, key confirmation, all-one/identity values, and static/ephemeral compromise.
8. Estimate Logjam-style common-parameter risk and distinguish one-time field precomputation from per-key individual logarithms.
9. Include Shor-resource estimates for classical deployments and explicitly separate them from any PQC claim.
10. Map results to DLP, CDH/DDH, signature forgery, message recovery, or AKE properties; these assumptions are not interchangeable.

## Output contract

- A finite-field/group parameter and validation audit.
- Generic and index-calculus DLP estimates with precomputation split.
- Subgroup-confinement and protocol attack records.
- Assumption-specific conclusions for DLP/CDH/DDH and constructions.

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

- `DH76`
- `ELG85`
- `SHANKS71-BSGS`
- `PH78`
- `POLLARD78-DLOG`
- `ADL79-INDEX`
- `GORDON93-NFSDL`
- `BGJT14-SMALLCHAR`
- `ADRIAN15-LOGJAM`
- `LIMLEE97-SUBGROUP`
- `NIST-SP800-56A`
- `SHOR94`

Full records are bundled in `references/REFERENCES.md`.
