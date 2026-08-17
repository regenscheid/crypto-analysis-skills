# References for Lattice Hard-Problem and Estimator Analysis

These references are starting points, not substitutes for checking the exact target version, later corrections, implementation artifacts, and subsequent cryptanalysis.

When using a reference:

- cite the exact theorem, algorithm, table, parameter set, or source-code revision used;
- preserve the source adversary model and success definition;
- distinguish asymptotic analysis, concrete estimates, and implemented results;
- search for errata, follow-up attacks, rebuttals, and revised specifications;
- record any transfer from the cited object to the current target in a transfer matrix.

## Lattice problems, estimators, encryption, and signatures

- **`AJTAI96`** — Miklós Ajtai, “Generating Hard Instances of Lattice Problems,” STOC 1996. https://doi.org/10.1145/237814.237838
- **`REGEV05-LWE`** — Oded Regev, “On Lattices, Learning with Errors, Random Linear Codes, and Cryptography,” STOC 2005 / Journal of the ACM 56(6), 2009. https://doi.org/10.1145/1568318.1568324
- **`LPR10-RLWE`** — Vadim Lyubashevsky, Chris Peikert, and Oded Regev, “On Ideal Lattices and Learning with Errors over Rings,” EUROCRYPT 2010. https://doi.org/10.1007/978-3-642-13190-5_1
- **`LS15-MLWE`** — Adeline Langlois and Damien Stehlé, “Worst-Case to Average-Case Reductions for Module Lattices,” Designs, Codes and Cryptography 75, 2015. https://doi.org/10.1007/s10623-014-9938-4
- **`BPR12-LWR`** — Abhishek Banerjee, Chris Peikert, and Alon Rosen, “Pseudorandom Functions and Lattices,” EUROCRYPT 2012; introduces Learning With Rounding. https://doi.org/10.1007/978-3-642-29011-4_40
- **`GN08-BKZ`** — Nicolas Gama and Phong Q. Nguyen, “Predicting Lattice Reduction,” EUROCRYPT 2008. https://doi.org/10.1007/978-3-540-78967-3_3
- **`CN11-BKZ20`** — Yuanmi Chen and Phong Q. Nguyen, “BKZ 2.0: Better Lattice Security Estimates,” ASIACRYPT 2011. https://doi.org/10.1007/978-3-642-25385-0_1
- **`MW16-REDUCTION`** — Daniele Micciancio and Michael Walter, “Practical, Predictable Lattice Basis Reduction,” EUROCRYPT 2016; IACR ePrint 2015/1123. https://eprint.iacr.org/2015/1123
- **`BDGL16-SIEVE`** — Anja Becker, Léo Ducas, Nicolas Gama, and Thijs Laarhoven, “New Directions in Nearest Neighbor Searching with Applications to Lattice Sieving,” SODA 2016; IACR ePrint 2015/1128. https://eprint.iacr.org/2015/1128
- **`G6K18`** — Martin R. Albrecht et al., “The General Sieve Kernel and New Records in Lattice Reduction,” EUROCRYPT 2019; IACR ePrint 2017/721. https://eprint.iacr.org/2017/721
- **`BKW93`** — Avrim Blum, Adam Kalai, and Hal Wasserman, “Noise-Tolerant Learning, the Parity Problem, and the Statistical Query Model,” STOC 2000; BKW algorithm. https://doi.org/10.1145/335305.335336
- **`LP11-LWE`** — Richard Lindner and Chris Peikert, “Better Key Sizes (and Attacks) for LWE-Based Encryption,” CT-RSA 2011. https://doi.org/10.1007/978-3-642-19074-2_21
- **`APS15-LWE`** — Martin R. Albrecht, Rachel Player, and Sam Scott, “On the Concrete Hardness of Learning with Errors,” Journal of Mathematical Cryptology 9(3), 2015; IACR ePrint 2015/046. https://eprint.iacr.org/2015/046
- **`ARORA11-LWE`** — Sanjeev Arora and Rong Ge, “New Algorithms for Learning in Presence of Errors,” ICALP 2011. https://doi.org/10.1007/978-3-642-22012-8_31
- **`WUNDERER19-HYBRID`** — Thomas Wunderer, “A Detailed Analysis of the Hybrid Lattice-Reduction and Meet-in-the-Middle Attack,” Journal of Mathematical Cryptology 13(1), 2019. https://doi.org/10.1515/jmc-2016-0044
- **`LATTICE-ESTIMATOR`** — Martin R. Albrecht et al., Lattice Estimator software and documentation. https://github.com/malb/lattice-estimator
- **`EST18-ALL`** — Martin R. Albrecht et al., “Estimate All the {LWE, NTRU} Schemes!,” SCN 2018; IACR ePrint 2018/331. https://eprint.iacr.org/2018/331
