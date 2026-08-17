# References for Information-Set Decoding and Generic Decoding Analysis

These references are starting points, not substitutes for checking the exact target version, later corrections, implementation artifacts, and subsequent cryptanalysis.

When using a reference:

- cite the exact theorem, algorithm, table, parameter set, or source-code revision used;
- preserve the source adversary model and success definition;
- distinguish asymptotic analysis, concrete estimates, and implemented results;
- search for errata, follow-up attacks, rebuttals, and revised specifications;
- record any transfer from the cited object to the current target in a transfer matrix.

## Hamming-metric code-based cryptography

- **`MCELIECE78`** — Robert J. McEliece, “A Public-Key Cryptosystem Based on Algebraic Coding Theory,” DSN Progress Report 42-44, 1978. https://ipnpr.jpl.nasa.gov/progress_report2/42-44/44N.PDF
- **`PRANGE62`** — Eugene Prange, “The Use of Information Sets in Decoding Cyclic Codes,” IRE Transactions on Information Theory 8(5), 1962. https://doi.org/10.1109/TIT.1962.1057777
- **`LEEBRICKELL88`** — Pil Joong Lee and Ernest Brickell, “An Observation on the Security of McEliece’s Public-Key Cryptosystem,” EUROCRYPT 1988. https://doi.org/10.1007/3-540-45961-8_25
- **`STERN89-ISD`** — Jacques Stern, “A Method for Finding Codewords of Small Weight,” Coding Theory and Applications, 1989. https://doi.org/10.1007/BFb0019850
- **`DUMER91-ISD`** — Ilya Dumer, “On Minimum Distance Decoding of Linear Codes,” Fifth Joint Soviet-Swedish International Workshop on Information Theory, 1991.
- **`MMT11-ISD`** — Alexander May, Alexander Meurer, and Enrico Thomae, “Decoding Random Linear Codes in O(2^0.054n),” ASIACRYPT 2011; IACR ePrint 2011/473. https://eprint.iacr.org/2011/473
- **`BJMM12-ISD`** — Anja Becker, Antoine Joux, Alexander May, and Alexander Meurer, “Decoding Random Binary Linear Codes in 2^(n/20),” EUROCRYPT 2012; IACR ePrint 2012/026. https://eprint.iacr.org/2012/026
- **`MAYOZEROV15-ISD`** — Alexander May and Ilya Ozerov, “On Computing Nearest Neighbors with Applications to Decoding of Binary Linear Codes,” EUROCRYPT 2015. https://doi.org/10.1007/978-3-662-46800-5_8
- **`BOTHMAY17-ISD`** — Leonard Both and Alexander May, “Decoding Linear Codes with High Error Rate and Its Impact for LPN Security,” PQCrypto 2017. https://doi.org/10.1007/978-3-319-59879-6_2
- **`ESSER22-ISD`** — André Esser, “Revisiting Nearest-Neighbor-Based Information Set Decoding,” IACR ePrint 2022/1328. https://eprint.iacr.org/2022/1328
- **`DOOM11`** — Nicolas Sendrier, “Decoding One Out of Many,” PQCrypto 2011. https://doi.org/10.1007/978-3-642-25405-5_5

## Quantum algorithms and quantum resource analysis

- **`BERN10-QCODE`** — Daniel J. Bernstein, “Grover vs. McEliece,” PQCrypto 2010. https://cr.yp.to/codes/grovercode-20100303.pdf
