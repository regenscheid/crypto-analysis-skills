# References for Module-Lattice Signature Analysis

These references are starting points, not substitutes for checking the exact target version, later corrections, implementation artifacts, and subsequent cryptanalysis.

When using a reference:

- cite the exact theorem, algorithm, table, parameter set, or source-code revision used;
- preserve the source adversary model and success definition;
- distinguish asymptotic analysis, concrete estimates, and implemented results;
- search for errata, follow-up attacks, rebuttals, and revised specifications;
- record any transfer from the cited object to the current target in a transfer matrix.

## Lattice problems, estimators, encryption, and signatures

- **`DILITHIUM18`** — Léo Ducas et al., “CRYSTALS-Dilithium: A Lattice-Based Digital Signature Scheme,” TCHES 2018. https://doi.org/10.13154/tches.v2018.i1.238-268
- **`LYU09-FSABORT`** — Vadim Lyubashevsky, “Fiat–Shamir with Aborts: Applications to Lattice and Factoring-Based Signatures,” ASIACRYPT 2009. https://doi.org/10.1007/978-3-642-10366-7_35
- **`LYU12-LATSIG`** — Vadim Lyubashevsky, “Lattice Signatures without Trapdoors,” EUROCRYPT 2012; IACR ePrint 2011/537. https://eprint.iacr.org/2011/537
- **`BLISS13`** — Léo Ducas et al., “Lattice Signatures and Bimodal Gaussians,” CRYPTO 2013; IACR ePrint 2013/383. https://eprint.iacr.org/2013/383
- **`GPV08`** — Craig Gentry, Chris Peikert, and Vinod Vaikuntanathan, “Trapdoors for Hard Lattices and New Cryptographic Constructions,” STOC 2008; IACR ePrint 2007/432. https://eprint.iacr.org/2007/432
- **`MP12-TRAPDOOR`** — Daniele Micciancio and Chris Peikert, “Trapdoors for Lattices: Simpler, Tighter, Faster, Smaller,” EUROCRYPT 2012; IACR ePrint 2011/501. https://eprint.iacr.org/2011/501
- **`PREST17-RENYI`** — Thomas Prest, “Sharper Bounds in Lattice-Based Cryptography Using the Rényi Divergence,” ASIACRYPT 2017; IACR ePrint 2017/101. https://eprint.iacr.org/2017/101
- **`LATTICE-ESTIMATOR`** — Martin R. Albrecht et al., Lattice Estimator software and documentation. https://github.com/malb/lattice-estimator

## Security notions, transforms, protocols, standards, and current specifications

- **`NIST-FIPS204`** — NIST FIPS 204, Module-Lattice-Based Digital Signature Standard (ML-DSA), 2024. https://csrc.nist.gov/pubs/fips/204/final
- **`KLS18-FSQROM`** — Eike Kiltz, Vadim Lyubashevsky, and Christian Schaffner, “A Concrete Treatment of Fiat–Shamir Signatures in the Quantum Random-Oracle Model,” EUROCRYPT 2018; IACR ePrint 2017/916. https://eprint.iacr.org/2017/916
- **`NIST-IR8610`** — NIST IR 8610, Status Report on the Second Round of the Additional Digital Signature Schemes for the NIST Post-Quantum Cryptography Standardization Process, 2026. https://csrc.nist.gov/pubs/ir/8610/final
- **`NIST-R3SIG-2026`** — NIST, “Round 3 Additional Signatures,” Post-Quantum Cryptography project page, updated July 29, 2026. https://csrc.nist.gov/projects/pqc-dig-sig/round-3-additional-signatures
