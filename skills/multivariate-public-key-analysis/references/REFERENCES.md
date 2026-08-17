# References for Multivariate Public-Key Analysis

These references are starting points, not substitutes for checking the exact target version, later corrections, implementation artifacts, and subsequent cryptanalysis.

When using a reference:

- cite the exact theorem, algorithm, table, parameter set, or source-code revision used;
- preserve the source adversary model and success definition;
- distinguish asymptotic analysis, concrete estimates, and implemented results;
- search for errata, follow-up attacks, rebuttals, and revised specifications;
- record any transfer from the cited object to the current target in a transfer matrix.

## Multivariate and Oil-and-Vinegar cryptography

- **`MI88`** — Tsutomu Matsumoto and Hideki Imai, “Public Quadratic Polynomial-Tuples for Efficient Signature-Verification and Message-Encryption,” EUROCRYPT 1988. https://doi.org/10.1007/3-540-45961-8_13
- **`PATARIN96-HFE`** — Jacques Patarin, “Hidden Fields Equations (HFE) and Isomorphisms of Polynomials,” EUROCRYPT 1996. https://doi.org/10.1007/3-540-68339-9_4
- **`F4-99`** — Jean-Charles Faugère, “A New Efficient Algorithm for Computing Gröbner Bases (F4),” Journal of Pure and Applied Algebra 139, 1999. https://doi.org/10.1016/S0022-4049(99)00005-5
- **`F5-02`** — Jean-Charles Faugère, “A New Efficient Algorithm for Computing Gröbner Bases Without Reduction to Zero (F5),” ISSAC 2002. https://doi.org/10.1145/780506.780516
- **`XL00`** — Nicolas Courtois et al., “Efficient Algorithms for Solving Overdefined Systems of Multivariate Polynomial Equations,” EUROCRYPT 2000. https://doi.org/10.1007/3-540-45539-6_27
- **`FGS05-DIFFMQ`** — Pierre-Alain Fouque, Louis Granboulan, and Jacques Stern, “Differential Cryptanalysis for Multivariate Schemes,” EUROCRYPT 2005. https://doi.org/10.1007/11426639_20
- **`RAINBOW05`** — Jintai Ding and Dieter Schmidt, “Rainbow, a New Multivariable Polynomial Signature Scheme,” ACNS 2005. https://doi.org/10.1007/11496137_12
- **`BEULLENS22-RAINBOW`** — Ward Beullens, “Breaking Rainbow Takes a Weekend on a Laptop,” IACR ePrint 2022/214. https://eprint.iacr.org/2022/214
- **`MAYO21`** — Ward Beullens, “MAYO: Practical Post-Quantum Signatures from Oil-and-Vinegar Maps,” SAC 2021; IACR ePrint 2021/1144. https://eprint.iacr.org/2021/1144

## Rank-metric cryptography

- **`KS99-MINRANK`** — Aviad Kipnis and Adi Shamir, “Cryptanalysis of the HFE Public Key Cryptosystem by Relinearization,” CRYPTO 1999; foundational MinRank attack. https://doi.org/10.1007/3-540-48405-1_2

## Security notions, transforms, protocols, standards, and current specifications

- **`MAYO-SPEC`** — MAYO team, MAYO specification and supporting material. https://pqmayo.org/
- **`NIST-IR8610`** — NIST IR 8610, Status Report on the Second Round of the Additional Digital Signature Schemes for the NIST Post-Quantum Cryptography Standardization Process, 2026. https://csrc.nist.gov/pubs/ir/8610/final
