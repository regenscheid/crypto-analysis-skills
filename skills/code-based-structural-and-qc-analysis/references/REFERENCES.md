# References for Code-Based Structural and QC Analysis

These references are starting points, not substitutes for checking the exact target version, later corrections, implementation artifacts, and subsequent cryptanalysis.

When using a reference:

- cite the exact theorem, algorithm, table, parameter set, or source-code revision used;
- preserve the source adversary model and success definition;
- distinguish asymptotic analysis, concrete estimates, and implemented results;
- search for errata, follow-up attacks, rebuttals, and revised specifications;
- record any transfer from the cited object to the current target in a transfer matrix.

## Hamming-metric code-based cryptography

- **`MCELIECE78`** — Robert J. McEliece, “A Public-Key Cryptosystem Based on Algebraic Coding Theory,” DSN Progress Report 42-44, 1978. https://ipnpr.jpl.nasa.gov/progress_report2/42-44/44N.PDF
- **`NIED86`** — Harald Niederreiter, “Knapsack-Type Cryptosystems and Algebraic Coding Theory,” Problems of Control and Information Theory 15, 1986.
- **`SIDEL92`** — Vladimir Sidelnikov and Sergei Shestakov, “On Insecurity of Cryptosystems Based on Generalized Reed–Solomon Codes,” Discrete Mathematics and Applications 2(4), 1992. https://doi.org/10.1515/dma.1992.2.4.439
- **`SENDRIER00-SSA`** — Nicolas Sendrier, “Finding the Permutation Between Equivalent Linear Codes: The Support Splitting Algorithm,” IEEE Transactions on Information Theory 46(4), 2000. https://doi.org/10.1109/18.850662
- **`FAUGERE10-GOPPA`** — Jean-Charles Faugère et al., “Algebraic Cryptanalysis of McEliece Variants with Compact Keys,” EUROCRYPT 2010; IACR ePrint 2009/477. https://eprint.iacr.org/2009/477
- **`GJS16-REACTION`** — Qian Guo, Thomas Johansson, and Paul Stankovski, “A Key Recovery Attack on MDPC with CCA Security Using Decoding Errors,” ASIACRYPT 2016; IACR ePrint 2016/858. https://eprint.iacr.org/2016/858

## Security notions, transforms, protocols, standards, and current specifications

- **`CLASSIC-MCELIECE-SPEC`** — Classic McEliece team, Classic McEliece specification, papers, and software. https://classic.mceliece.org/
- **`HQC-SPEC`** — HQC team, Hamming Quasi-Cyclic (HQC) specification and supporting material. https://pqc-hqc.org/
