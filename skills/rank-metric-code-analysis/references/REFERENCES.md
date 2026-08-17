# References for Rank-Metric Code Analysis

These references are starting points, not substitutes for checking the exact target version, later corrections, implementation artifacts, and subsequent cryptanalysis.

When using a reference:

- cite the exact theorem, algorithm, table, parameter set, or source-code revision used;
- preserve the source adversary model and success definition;
- distinguish asymptotic analysis, concrete estimates, and implemented results;
- search for errata, follow-up attacks, rebuttals, and revised specifications;
- record any transfer from the cited object to the current target in a transfer matrix.

## Rank-metric cryptography

- **`GABID85`** — Ernst Gabidulin, “Theory of Codes with Maximum Rank Distance,” Problems of Information Transmission 21(1), 1985.
- **`GPT91`** — Ernst Gabidulin, Alexei Paramonov, and Olga Tretjakov, “Ideals over a Non-Commutative Ring and Their Application in Cryptology,” EUROCRYPT 1991. https://doi.org/10.1007/3-540-46416-6_23
- **`OVERBECK08`** — Raphael Overbeck, “Structural Attacks for Public Key Cryptosystems Based on Gabidulin Codes,” Journal of Cryptology 21, 2008. https://doi.org/10.1007/s00145-007-9003-9
- **`LRPC13`** — Philippe Gaborit, Gaétan Murat, Olivier Ruatta, and Gilles Zémor, “Low Rank Parity Check Codes and Their Application to Cryptography,” WCC 2013. https://www.unilim.fr/pages_perso/olivier.ruatta/wccRank_sub.pdf
- **`GRS13-RSD`** — Philippe Gaborit, Olivier Ruatta, and Julien Schrek, “On the Complexity of the Rank Syndrome Decoding Problem,” IEEE Transactions on Information Theory 62(2), 2016; IACR ePrint 2013/686. https://eprint.iacr.org/2013/686
- **`BARDET19-RANKALG`** — Magali Bardet et al., “An Algebraic Attack on Rank Metric Code-Based Cryptosystems,” EUROCRYPT 2020; arXiv 1910.00810. https://arxiv.org/abs/1910.00810
- **`RANKSIGN18-BREAK`** — Thomas Debris-Alazard and Jean-Pierre Tillich, “Two Attacks on Rank Metric Code-Based Schemes: RankSign and an IBE Scheme,” ASIACRYPT 2018; IACR ePrint 2018/823. https://eprint.iacr.org/2018/823
- **`KS99-MINRANK`** — Aviad Kipnis and Adi Shamir, “Cryptanalysis of the HFE Public Key Cryptosystem by Relinearization,” CRYPTO 1999; foundational MinRank attack. https://doi.org/10.1007/3-540-48405-1_2
