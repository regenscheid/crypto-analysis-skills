# References for Decryption-Failure and Reaction Analysis

These references are starting points, not substitutes for checking the exact target version, later corrections, implementation artifacts, and subsequent cryptanalysis.

When using a reference:

- cite the exact theorem, algorithm, table, parameter set, or source-code revision used;
- preserve the source adversary model and success definition;
- distinguish asymptotic analysis, concrete estimates, and implemented results;
- search for errata, follow-up attacks, rebuttals, and revised specifications;
- record any transfer from the cited object to the current target in a transfer matrix.

## Hamming-metric code-based cryptography

- **`GJS16-REACTION`** — Qian Guo, Thomas Johansson, and Paul Stankovski, “A Key Recovery Attack on MDPC with CCA Security Using Decoding Errors,” ASIACRYPT 2016; IACR ePrint 2016/858. https://eprint.iacr.org/2016/858

## Lattice problems, estimators, encryption, and signatures

- **`DANVERS19-FAIL`** — Jan-Pieter D’Anvers et al., “Decryption Failure Attacks on IND-CCA Secure Lattice-Based Schemes,” PKC 2019; IACR ePrint 2018/1089. https://eprint.iacr.org/2018/1089
- **`DANVERS19-BOOTFAIL`** — Jan-Pieter D’Anvers et al., “(One) Failure Is Not an Option: Bootstrapping the Search for Failures in Lattice-Based Encryption Schemes,” EUROCRYPT 2020; IACR ePrint 2019/1399. https://eprint.iacr.org/2019/1399
- **`DANVERS21-MTFAIL`** — Jan-Pieter D’Anvers et al., “Multitarget Decryption Failure Attacks and Their Application to Saber, Frodo and NTRU,” PKC 2022; IACR ePrint 2021/193. https://eprint.iacr.org/2021/193

## Security notions, transforms, protocols, standards, and current specifications

- **`NIST-FIPS203`** — NIST FIPS 203, Module-Lattice-Based Key-Encapsulation Mechanism Standard (ML-KEM), 2024. https://csrc.nist.gov/pubs/fips/203/final
- **`HQC-SPEC`** — HQC team, Hamming Quasi-Cyclic (HQC) specification and supporting material. https://pqc-hqc.org/
