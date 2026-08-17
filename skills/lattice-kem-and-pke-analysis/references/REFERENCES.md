# References for Lattice KEM and Public-Key Encryption Analysis

These references are starting points, not substitutes for checking the exact target version, later corrections, implementation artifacts, and subsequent cryptanalysis.

When using a reference:

- cite the exact theorem, algorithm, table, parameter set, or source-code revision used;
- preserve the source adversary model and success definition;
- distinguish asymptotic analysis, concrete estimates, and implemented results;
- search for errata, follow-up attacks, rebuttals, and revised specifications;
- record any transfer from the cited object to the current target in a transfer matrix.

## Lattice problems, estimators, encryption, and signatures

- **`KYBER17`** — Joppe Bos et al., “CRYSTALS—Kyber: A CCA-Secure Module-Lattice-Based KEM,” IEEE EuroS&P 2018; IACR ePrint 2017/634. https://eprint.iacr.org/2017/634
- **`FRODO16`** — Joppe Bos et al., “Frodo: Take Off the Ring! Practical, Quantum-Secure Key Exchange from LWE,” ACM CCS 2016; IACR ePrint 2016/659. https://eprint.iacr.org/2016/659
- **`SABER18`** — Jan-Pieter D’Anvers et al., “Saber: Module-LWR Based Key Exchange, CPA-Secure Encryption and CCA-Secure KEM,” AFRICACRYPT 2018; IACR ePrint 2018/230. https://eprint.iacr.org/2018/230
- **`NEWHOPE16`** — Erdem Alkim et al., “Post-Quantum Key Exchange—A New Hope,” USENIX Security 2016; IACR ePrint 2015/1092. https://eprint.iacr.org/2015/1092
- **`DANVERS19-FAIL`** — Jan-Pieter D’Anvers et al., “Decryption Failure Attacks on IND-CCA Secure Lattice-Based Schemes,” PKC 2019; IACR ePrint 2018/1089. https://eprint.iacr.org/2018/1089
- **`DANVERS19-BOOTFAIL`** — Jan-Pieter D’Anvers et al., “(One) Failure Is Not an Option: Bootstrapping the Search for Failures in Lattice-Based Encryption Schemes,” EUROCRYPT 2020; IACR ePrint 2019/1399. https://eprint.iacr.org/2019/1399
- **`DANVERS21-MTFAIL`** — Jan-Pieter D’Anvers et al., “Multitarget Decryption Failure Attacks and Their Application to Saber, Frodo and NTRU,” PKC 2022; IACR ePrint 2021/193. https://eprint.iacr.org/2021/193
- **`LATTICE-ESTIMATOR`** — Martin R. Albrecht et al., Lattice Estimator software and documentation. https://github.com/malb/lattice-estimator

## Security notions, transforms, protocols, standards, and current specifications

- **`NIST-FIPS203`** — NIST FIPS 203, Module-Lattice-Based Key-Encapsulation Mechanism Standard (ML-KEM), 2024. https://csrc.nist.gov/pubs/fips/203/final
- **`NIST-SP800-227`** — NIST SP 800-227, Recommendations for Key-Encapsulation Mechanisms, final, 2025. https://csrc.nist.gov/pubs/sp/800/227/final
- **`FO99`** — Eiichiro Fujisaki and Tatsuaki Okamoto, “Secure Integration of Asymmetric and Symmetric Encryption Schemes,” CRYPTO 1999. https://doi.org/10.1007/3-540-48405-1_34
- **`HHK17-FO`** — Dennis Hofheinz, Kathrin Hövelmanns, and Eike Kiltz, “A Modular Analysis of the Fujisaki–Okamoto Transformation,” TCC 2017; IACR ePrint 2017/604. https://eprint.iacr.org/2017/604
