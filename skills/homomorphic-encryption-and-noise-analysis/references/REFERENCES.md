# References for Homomorphic Encryption and Noise Analysis

These references are starting points, not substitutes for checking the exact target version, later corrections, implementation artifacts, and subsequent cryptanalysis.

When using a reference:

- cite the exact theorem, algorithm, table, parameter set, or source-code revision used;
- preserve the source adversary model and success definition;
- distinguish asymptotic analysis, concrete estimates, and implemented results;
- search for errata, follow-up attacks, rebuttals, and revised specifications;
- record any transfer from the cited object to the current target in a transfer matrix.

## Knapsack, homomorphic, hidden-order, and noncommutative families

- **`GENTRY09-FHE`** — Craig Gentry, “Fully Homomorphic Encryption Using Ideal Lattices,” STOC 2009. https://doi.org/10.1145/1536414.1536440
- **`BGV12-FHE`** — Zvika Brakerski, Craig Gentry, and Vinod Vaikuntanathan, “(Leveled) Fully Homomorphic Encryption without Bootstrapping,” ITCS 2012; IACR ePrint 2011/277. https://eprint.iacr.org/2011/277
- **`BFV12-FHE`** — Junfeng Fan and Frederik Vercauteren, “Somewhat Practical Fully Homomorphic Encryption,” IACR ePrint 2012/144. https://eprint.iacr.org/2012/144
- **`CKKS17`** — Jung Hee Cheon et al., “Homomorphic Encryption for Arithmetic of Approximate Numbers,” ASIACRYPT 2017; IACR ePrint 2016/421. https://eprint.iacr.org/2016/421

## Lattice problems, estimators, encryption, and signatures

- **`LPR10-RLWE`** — Vadim Lyubashevsky, Chris Peikert, and Oded Regev, “On Ideal Lattices and Learning with Errors over Rings,” EUROCRYPT 2010. https://doi.org/10.1007/978-3-642-13190-5_1
- **`ABD16-SUBFIELD`** — Martin R. Albrecht, Shi Bai, and Léo Ducas, “A Subfield Lattice Attack on Overstretched NTRU Assumptions,” CRYPTO 2016; IACR ePrint 2016/127. https://eprint.iacr.org/2016/127
- **`LATTICE-ESTIMATOR`** — Martin R. Albrecht et al., Lattice Estimator software and documentation. https://github.com/malb/lattice-estimator
