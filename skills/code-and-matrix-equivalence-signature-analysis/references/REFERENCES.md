# References for Code- and Matrix-Equivalence Signature Analysis

These references are starting points, not substitutes for checking the exact target version, later corrections, implementation artifacts, and subsequent cryptanalysis.

When using a reference:

- cite the exact theorem, algorithm, table, parameter set, or source-code revision used;
- preserve the source adversary model and success definition;
- distinguish asymptotic analysis, concrete estimates, and implemented results;
- search for errata, follow-up attacks, rebuttals, and revised specifications;
- record any transfer from the cited object to the current target in a transfer matrix.

## Hamming-metric code-based cryptography

- **`LESS-SPEC`** — LESS team, “LESS: Linear Equivalence Signature Scheme,” NIST additional-signatures Round 1 specification. https://csrc.nist.gov/csrc/media/Projects/pqc-dig-sig/documents/round-1/spec-files/less-spec-web.pdf
- **`LESS20`** — Jean-François Biasse et al., “LESS is More: Code-Based Signatures Without Syndromes,” AFRICACRYPT 2020. https://doi.org/10.1007/978-3-030-51938-4_3
- **`LESSFM21`** — Alessandro Barenghi et al., “LESS-FM: Fine-Tuning Signatures from the Code Equivalence Problem,” PQCrypto 2021; IACR ePrint 2021/396. https://eprint.iacr.org/2021/396
- **`MEDS22`** — Tung Chou et al., “Take Your MEDS: Digital Signatures from Matrix Code Equivalence,” EUROCRYPT 2023; IACR ePrint 2022/1559. https://eprint.iacr.org/2022/1559
- **`MEDS-SPEC`** — MEDS team, “MEDS Specification Document,” NIST additional-signatures Round 1 specification. https://csrc.nist.gov/csrc/media/Projects/pqc-dig-sig/documents/round-1/spec-files/MEDS-spec-web.pdf
- **`SENDRIER00-SSA`** — Nicolas Sendrier, “Finding the Permutation Between Equivalent Linear Codes: The Support Splitting Algorithm,” IEEE Transactions on Information Theory 46(4), 2000. https://doi.org/10.1109/18.850662

## Rank-metric cryptography

- **`KS99-MINRANK`** — Aviad Kipnis and Adi Shamir, “Cryptanalysis of the HFE Public Key Cryptosystem by Relinearization,” CRYPTO 1999; foundational MinRank attack. https://doi.org/10.1007/3-540-48405-1_2

## Security notions, transforms, protocols, standards, and current specifications

- **`FS86`** — Amos Fiat and Adi Shamir, “How to Prove Yourself: Practical Solutions to Identification and Signature Problems,” CRYPTO 1986. https://doi.org/10.1007/3-540-47721-7_12
- **`KLS18-FSQROM`** — Eike Kiltz, Vadim Lyubashevsky, and Christian Schaffner, “A Concrete Treatment of Fiat–Shamir Signatures in the Quantum Random-Oracle Model,” EUROCRYPT 2018; IACR ePrint 2017/916. https://eprint.iacr.org/2017/916
