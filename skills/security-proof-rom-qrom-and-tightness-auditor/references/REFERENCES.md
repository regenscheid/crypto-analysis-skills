# References for Security Proof, ROM/QROM, and Tightness Auditor

These references are starting points, not substitutes for checking the exact target version, later corrections, implementation artifacts, and subsequent cryptanalysis.

When using a reference:

- cite the exact theorem, algorithm, table, parameter set, or source-code revision used;
- preserve the source adversary model and success definition;
- distinguish asymptotic analysis, concrete estimates, and implemented results;
- search for errata, follow-up attacks, rebuttals, and revised specifications;
- record any transfer from the cited object to the current target in a transfer matrix.

## Hash-based signatures

- **`HULSING22-TIGHT`** — Andreas Hülsing et al., “Recovering the Tight Security Proof of SPHINCS+,” EUROCRYPT 2023; IACR ePrint 2022/346. https://eprint.iacr.org/2022/346

## Security notions, transforms, protocols, standards, and current specifications

- **`BR93-ROM`** — Mihir Bellare and Phillip Rogaway, “Random Oracles are Practical: A Paradigm for Designing Efficient Protocols,” ACM CCS 1993. https://doi.org/10.1145/168588.168596
- **`PS00-FORK`** — David Pointcheval and Jacques Stern, “Security Arguments for Digital Signatures and Blind Signatures,” Journal of Cryptology 13, 2000. https://doi.org/10.1007/s001450010003
- **`BN06-FORK`** — Mihir Bellare and Gregory Neven, “Multi-signatures in the Plain Public-Key Model and a General Forking Lemma,” ACM CCS 2006. https://doi.org/10.1145/1180405.1180453
- **`UNRUH17-QROM`** — Dominique Unruh, “Post-Quantum Security of Fiat–Shamir,” ASIACRYPT 2017; IACR ePrint 2017/398. https://eprint.iacr.org/2017/398
- **`KLS18-FSQROM`** — Eike Kiltz, Vadim Lyubashevsky, and Christian Schaffner, “A Concrete Treatment of Fiat–Shamir Signatures in the Quantum Random-Oracle Model,” EUROCRYPT 2018; IACR ePrint 2017/916. https://eprint.iacr.org/2017/916
- **`FO99`** — Eiichiro Fujisaki and Tatsuaki Okamoto, “Secure Integration of Asymmetric and Symmetric Encryption Schemes,” CRYPTO 1999. https://doi.org/10.1007/3-540-48405-1_34
- **`HHK17-FO`** — Dennis Hofheinz, Kathrin Hövelmanns, and Eike Kiltz, “A Modular Analysis of the Fujisaki–Okamoto Transformation,” TCC 2017; IACR ePrint 2017/604. https://eprint.iacr.org/2017/604
