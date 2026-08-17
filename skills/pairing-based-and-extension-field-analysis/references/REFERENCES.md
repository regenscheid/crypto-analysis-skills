# References for Pairing-Based and Extension-Field Analysis

These references are starting points, not substitutes for checking the exact target version, later corrections, implementation artifacts, and subsequent cryptanalysis.

When using a reference:

- cite the exact theorem, algorithm, table, parameter set, or source-code revision used;
- preserve the source adversary model and success definition;
- distinguish asymptotic analysis, concrete estimates, and implemented results;
- search for errata, follow-up attacks, rebuttals, and revised specifications;
- record any transfer from the cited object to the current target in a transfer matrix.

## Elliptic curves, generic groups, and pairings

- **`BF01-IBE`** — Dan Boneh and Matthew Franklin, “Identity-Based Encryption from the Weil Pairing,” CRYPTO 2001. https://doi.org/10.1007/3-540-44647-8_13
- **`BLS01`** — Dan Boneh, Ben Lynn, and Hovav Shacham, “Short Signatures from the Weil Pairing,” ASIACRYPT 2001. https://doi.org/10.1007/3-540-45682-1_30
- **`MOV93`** — Alfred Menezes, Tatsuaki Okamoto, and Scott Vanstone, “Reducing Elliptic Curve Logarithms to Logarithms in a Finite Field,” IEEE Transactions on Information Theory 39(5), 1993. https://doi.org/10.1109/18.259647
- **`FREYRUCK94`** — Gerhard Frey and Hans-Georg Rück, “A Remark Concerning m-divisibility and the Discrete Logarithm in the Divisor Class Group of Curves,” Mathematics of Computation 62, 1994. https://doi.org/10.1090/S0025-5718-1994-1218343-6
- **`KB16-EXTNFS`** — Taechan Kim and Razvan Barbulescu, “Extended Tower Number Field Sieve: A New Complexity for the Medium Prime Case,” CRYPTO 2016; IACR ePrint 2015/1027. https://eprint.iacr.org/2015/1027
- **`KIMBAR16-PAIRING`** — Taechan Kim and Razvan Barbulescu, “Extended Tower Number Field Sieve and Pairing-Friendly Curves,” CRYPTO 2016; parameter-impact analysis. https://eprint.iacr.org/2015/1027

## Finite-field discrete logarithms and Diffie–Hellman

- **`LIMLEE97-SUBGROUP`** — Chae Hoon Lim and Pil Joong Lee, “A Key Recovery Attack on Discrete Log-based Schemes Using a Prime Order Subgroup,” CRYPTO 1997. https://doi.org/10.1007/BFb0052259

## Quantum algorithms and quantum resource analysis

- **`SHOR94`** — Peter W. Shor, “Algorithms for Quantum Computation: Discrete Logarithms and Factoring,” FOCS 1994. https://doi.org/10.1109/SFCS.1994.365700
