# References for Generic-Group and Collision-Search Analysis

These references are starting points, not substitutes for checking the exact target version, later corrections, implementation artifacts, and subsequent cryptanalysis.

When using a reference:

- cite the exact theorem, algorithm, table, parameter set, or source-code revision used;
- preserve the source adversary model and success definition;
- distinguish asymptotic analysis, concrete estimates, and implemented results;
- search for errata, follow-up attacks, rebuttals, and revised specifications;
- record any transfer from the cited object to the current target in a transfer matrix.

## Elliptic curves, generic groups, and pairings

- **`SHOUP97-GGM`** — Victor Shoup, “Lower Bounds for Discrete Logarithms and Related Problems,” EUROCRYPT 1997. https://doi.org/10.1007/3-540-69053-0_26
- **`NECHAEV94-GGM`** — V. I. Nechaev, “Complexity of a Determinate Algorithm for the Discrete Logarithm,” Mathematical Notes 55, 1994. https://doi.org/10.1007/BF02113297
- **`VOW99-PARALLEL`** — Paul C. van Oorschot and Michael J. Wiener, “Parallel Collision Search with Cryptanalytic Applications,” Journal of Cryptology 12, 1999. https://doi.org/10.1007/PL00003816
- **`TESKE01-RHO`** — Edlyn Teske, “On Random Walks for Pollard’s Rho Method,” Mathematics of Computation 70, 2001. https://doi.org/10.1090/S0025-5718-00-01213-8

## Finite-field discrete logarithms and Diffie–Hellman

- **`SHANKS71-BSGS`** — Daniel Shanks, “Class Number, a Theory of Factorization, and Genera,” 1971; source of baby-step giant-step. https://www.ams.org/books/pspum/020/
- **`POLLARD78-DLOG`** — John M. Pollard, “Monte Carlo Methods for Index Computation (mod p),” Mathematics of Computation 32(143), 1978. https://doi.org/10.2307/2006496

## Quantum algorithms and quantum resource analysis

- **`GROVER96`** — Lov K. Grover, “A Fast Quantum Mechanical Algorithm for Database Search,” STOC 1996; arXiv quant-ph/9605043. https://arxiv.org/abs/quant-ph/9605043
