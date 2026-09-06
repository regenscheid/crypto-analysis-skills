---
name: integer-factorization-and-rsa-analysis
description: "Analyzes RSA and other integer-factorization cryptography from prime generation through factoring, small-secret and small-root attacks, algebraic relations, padding/encoding, decryption oracles, and quantum resources."
metadata:
  version: "0.1"
  display-name: "Integer Factorization and RSA Analysis"
  tags: "rsa, factorization, small-roots, padding-oracle, coppersmith"
  requires: "rsa-or-factorization-scheme, parameters, encodings"
  produces: "factorization-estimates, rsa-attack-records, key-generation-audit"
---

# Integer Factorization and RSA Analysis

## Use this skill when

The target uses RSA, Rabin, hidden factorization, strong-RSA-type assumptions, or an integer-modulus trapdoor.

## Operating procedure

1. Record modulus generation, prime count and sizes, balance, primality conditions, strong/safe-prime constraints, shared or deterministic generation, public exponent, private exponent/CRT values, and key validation.
2. Screen for elementary failures: repeated/shared primes, close primes, small factors, biased generation, non-coprime exponents, common modulus, reused CRT components, and malformed keys.
3. Estimate factorization with trial division/Pollard methods, ECM, quadratic sieve, GNFS or SNFS as appropriate. State special-form effects, finite-size calibration, memory, parallelism, and precomputation.
4. Analyze small-private-exponent and partial-key exposure using continued fractions, lattice/small-root methods, approximate common divisors, known bits, and CRT relations. Verify theorem bounds for the exact key distribution.
5. Analyze low-exponent, broadcast, related-message, partial-plaintext, stereotyped-message, and Coppersmith-style attacks with the actual padding/encoding polynomial and message entropy.
6. Audit RSA-PSS, PKCS #1 v1.5, OAEP, KEM, and key-transport encodings for transform assumptions, noncanonical parsing, validity oracles, and adaptive interval attacks.
7. Model signature-specific algebra: textbook multiplicativity, blinding, fault-independent malformed signatures, verification exponents, and key-substitution or cross-protocol use.
8. Include multi-key batch GCD, shared precomputation, and large-population weak-key discovery when the deployment scale warrants it.
9. For quantum analysis, estimate Shor arithmetic for the exact modulus size and report logical/physical resources separately from polynomial asymptotics.
10. Map each result to factoring hardness, one-way RSA, RSA inversion, signature forgery, PKE/KEM CCA, or protocol authentication rather than treating all as “breaking RSA.”

## Output contract

- An RSA/factorization parameter and key-generation audit.
- Versioned estimates for factoring and relevant algebraic attacks.
- Padding/oracle, small-root, and partial-key attack records.
- Claim-specific classical and quantum conclusions.

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

- `RSA78`
- `RABIN79`
- `POLLARD74-P1`
- `POLLARD75-RHOFACT`
- `LENSTRA87-ECM`
- `POM84-QS`
- `LL93-NFS`
- `COP96-SMALLROOTS`
- `WIENER90`
- `BD99`
- `HASTAD88`
- `BLE98`
- `MANGER01`
- `RFC8017`
- `GE21-RSA`

Full records are bundled in `references/REFERENCES.md`.
