# References for Finite-Field Discrete-Log and DH Analysis

These references are starting points, not substitutes for checking the exact target version, later corrections, implementation artifacts, and subsequent cryptanalysis.

When using a reference:

- cite the exact theorem, algorithm, table, parameter set, or source-code revision used;
- preserve the source adversary model and success definition;
- distinguish asymptotic analysis, concrete estimates, and implemented results;
- search for errata, follow-up attacks, rebuttals, and revised specifications;
- record any transfer from the cited object to the current target in a transfer matrix.

## Finite-field discrete logarithms and Diffie–Hellman

- **`DH76`** — Whitfield Diffie and Martin E. Hellman, “New Directions in Cryptography,” IEEE Transactions on Information Theory 22(6), 1976. https://doi.org/10.1109/TIT.1976.1055638
- **`ELG85`** — Taher ElGamal, “A Public Key Cryptosystem and a Signature Scheme Based on Discrete Logarithms,” IEEE Transactions on Information Theory 31(4), 1985. https://doi.org/10.1109/TIT.1985.1057074
- **`SHANKS71-BSGS`** — Daniel Shanks, “Class Number, a Theory of Factorization, and Genera,” 1971; source of baby-step giant-step. https://www.ams.org/books/pspum/020/
- **`PH78`** — Stephen Pohlig and Martin Hellman, “An Improved Algorithm for Computing Logarithms over GF(p) and Its Cryptographic Significance,” IEEE Transactions on Information Theory 24(1), 1978. https://doi.org/10.1109/TIT.1978.1055817
- **`POLLARD78-DLOG`** — John M. Pollard, “Monte Carlo Methods for Index Computation (mod p),” Mathematics of Computation 32(143), 1978. https://doi.org/10.2307/2006496
- **`ADL79-INDEX`** — Leonard M. Adleman, “A Subexponential Algorithm for the Discrete Logarithm Problem with Applications to Cryptography,” FOCS 1979. https://doi.org/10.1109/SFCS.1979.2
- **`GORDON93-NFSDL`** — Daniel M. Gordon, “Discrete Logarithms in GF(p) Using the Number Field Sieve,” SIAM Journal on Discrete Mathematics 6(1), 1993. https://doi.org/10.1137/0406007
- **`BGJT14-SMALLCHAR`** — Razvan Barbulescu, Pierrick Gaudry, Antoine Joux, and Emmanuel Thomé, “A Heuristic Quasi-Polynomial Algorithm for Discrete Logarithm in Finite Fields of Small Characteristic,” EUROCRYPT 2014; IACR ePrint 2013/400. https://eprint.iacr.org/2013/400
- **`ADRIAN15-LOGJAM`** — David Adrian et al., “Imperfect Forward Secrecy: How Diffie–Hellman Fails in Practice,” ACM CCS 2015. https://weakdh.org/imperfect-forward-secrecy-ccs15.pdf
- **`LIMLEE97-SUBGROUP`** — Chae Hoon Lim and Pil Joong Lee, “A Key Recovery Attack on Discrete Log-based Schemes Using a Prime Order Subgroup,” CRYPTO 1997. https://doi.org/10.1007/BFb0052259

## Quantum algorithms and quantum resource analysis

- **`SHOR94`** — Peter W. Shor, “Algorithms for Quantum Computation: Discrete Logarithms and Factoring,” FOCS 1994. https://doi.org/10.1109/SFCS.1994.365700

## Security notions, transforms, protocols, standards, and current specifications

- **`NIST-SP800-56A`** — NIST SP 800-56A Rev. 3, Recommendation for Pair-Wise Key-Establishment Schemes Using Discrete Logarithm Cryptography, 2018. https://csrc.nist.gov/pubs/sp/800/56/a/r3/final
