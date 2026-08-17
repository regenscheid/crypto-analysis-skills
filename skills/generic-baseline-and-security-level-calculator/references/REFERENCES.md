# References for Generic Baseline and Security-Level Calculator

These references are starting points, not substitutes for checking the exact target version, later corrections, implementation artifacts, and subsequent cryptanalysis.

When using a reference:

- cite the exact theorem, algorithm, table, parameter set, or source-code revision used;
- preserve the source adversary model and success definition;
- distinguish asymptotic analysis, concrete estimates, and implemented results;
- search for errata, follow-up attacks, rebuttals, and revised specifications;
- record any transfer from the cited object to the current target in a transfer matrix.

## Elliptic curves, generic groups, and pairings

- **`SHOUP97-GGM`** — Victor Shoup, “Lower Bounds for Discrete Logarithms and Related Problems,” EUROCRYPT 1997. https://doi.org/10.1007/3-540-69053-0_26
- **`VOW99-PARALLEL`** — Paul C. van Oorschot and Michael J. Wiener, “Parallel Collision Search with Cryptanalytic Applications,” Journal of Cryptology 12, 1999. https://doi.org/10.1007/PL00003816

## Finite-field discrete logarithms and Diffie–Hellman

- **`SHANKS71-BSGS`** — Daniel Shanks, “Class Number, a Theory of Factorization, and Genera,” 1971; source of baby-step giant-step. https://www.ams.org/books/pspum/020/
- **`POLLARD78-DLOG`** — John M. Pollard, “Monte Carlo Methods for Index Computation (mod p),” Mathematics of Computation 32(143), 1978. https://doi.org/10.2307/2006496

## Hamming-metric code-based cryptography

- **`ESSER22-ISD`** — André Esser, “Revisiting Nearest-Neighbor-Based Information Set Decoding,” IACR ePrint 2022/1328. https://eprint.iacr.org/2022/1328

## Integer factorization, RSA, and adaptive decryption attacks

- **`LL93-NFS`** — Arjen K. Lenstra and Hendrik W. Lenstra Jr., eds., The Development of the Number Field Sieve, Lecture Notes in Mathematics 1554, 1993. https://doi.org/10.1007/BFb0091534

## Lattice problems, estimators, encryption, and signatures

- **`LATTICE-ESTIMATOR`** — Martin R. Albrecht et al., Lattice Estimator software and documentation. https://github.com/malb/lattice-estimator

## Multivariate and Oil-and-Vinegar cryptography

- **`F4-99`** — Jean-Charles Faugère, “A New Efficient Algorithm for Computing Gröbner Bases (F4),” Journal of Pure and Applied Algebra 139, 1999. https://doi.org/10.1016/S0022-4049(99)00005-5

## Quantum algorithms and quantum resource analysis

- **`SHOR94`** — Peter W. Shor, “Algorithms for Quantum Computation: Discrete Logarithms and Factoring,” FOCS 1994. https://doi.org/10.1109/SFCS.1994.365700
- **`GROVER96`** — Lov K. Grover, “A Fast Quantum Mechanical Algorithm for Database Search,” STOC 1996; arXiv quant-ph/9605043. https://arxiv.org/abs/quant-ph/9605043
