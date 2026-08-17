# References for MPC-in-the-Head Signature Analysis

These references are starting points, not substitutes for checking the exact target version, later corrections, implementation artifacts, and subsequent cryptanalysis.

When using a reference:

- cite the exact theorem, algorithm, table, parameter set, or source-code revision used;
- preserve the source adversary model and success definition;
- distinguish asymptotic analysis, concrete estimates, and implemented results;
- search for errata, follow-up attacks, rebuttals, and revised specifications;
- record any transfer from the cited object to the current target in a transfer matrix.

## Hamming-metric code-based cryptography

- **`SDITH-SPEC`** — SDitH team, Syndrome Decoding in the Head specification and supporting material. https://sdith.org/

## MPC-in-the-head, VOLE-in-the-head, and proof-derived signatures

- **`IKOS07-MPCITH`** — Yuval Ishai, Eyal Kushilevitz, Rafail Ostrovsky, and Amit Sahai, “Zero-Knowledge from Secure Multiparty Computation,” STOC 2007. https://doi.org/10.1145/1250790.1250834
- **`ZKBOO16`** — Irene Giacomelli, Jesper Madsen, and Claudio Orlandi, “ZKBoo: Faster Zero-Knowledge for Boolean Circuits,” USENIX Security 2016; IACR ePrint 2016/163. https://eprint.iacr.org/2016/163
- **`ZKBPP17`** — Melissa Chase et al., “Post-Quantum Zero-Knowledge and Signatures from Symmetric-Key Primitives,” ACM CCS 2017; IACR ePrint 2017/279. https://eprint.iacr.org/2017/279
- **`KKW18`** — Jonathan Katz, Vladimir Kolesnikov, and Xiao Wang, “Improved Non-Interactive Zero Knowledge with Applications to Post-Quantum Signatures,” ACM CCS 2018; IACR ePrint 2018/475. https://eprint.iacr.org/2018/475
- **`KALES20-PICNIC`** — Daniel Kales and Greg Zaverucha, “Improving the Performance of the Picnic Signature Scheme,” IACR ePrint 2020/427. https://eprint.iacr.org/2020/427
- **`BUI24-MPCITH`** — Dang Bui et al., “Faster Signatures from MPC-in-the-Head,” IACR ePrint 2024/252. https://eprint.iacr.org/2024/252

## Security notions, transforms, protocols, standards, and current specifications

- **`PICNIC-SPEC`** — Picnic team, Picnic specification and reference implementation. https://microsoft.github.io/Picnic/
- **`FS86`** — Amos Fiat and Adi Shamir, “How to Prove Yourself: Practical Solutions to Identification and Signature Problems,” CRYPTO 1986. https://doi.org/10.1007/3-540-47721-7_12
- **`KLS18-FSQROM`** — Eike Kiltz, Vadim Lyubashevsky, and Christian Schaffner, “A Concrete Treatment of Fiat–Shamir Signatures in the Quantum Random-Oracle Model,” EUROCRYPT 2018; IACR ePrint 2017/916. https://eprint.iacr.org/2017/916
