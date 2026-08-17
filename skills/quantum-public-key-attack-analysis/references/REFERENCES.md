# References for Quantum Public-Key Attack Analysis

These references are starting points, not substitutes for checking the exact target version, later corrections, implementation artifacts, and subsequent cryptanalysis.

When using a reference:

- cite the exact theorem, algorithm, table, parameter set, or source-code revision used;
- preserve the source adversary model and success definition;
- distinguish asymptotic analysis, concrete estimates, and implemented results;
- search for errata, follow-up attacks, rebuttals, and revised specifications;
- record any transfer from the cited object to the current target in a transfer matrix.

## Quantum algorithms and quantum resource analysis

- **`SHOR94`** — Peter W. Shor, “Algorithms for Quantum Computation: Discrete Logarithms and Factoring,” FOCS 1994. https://doi.org/10.1109/SFCS.1994.365700
- **`GROVER96`** — Lov K. Grover, “A Fast Quantum Mechanical Algorithm for Database Search,” STOC 1996; arXiv quant-ph/9605043. https://arxiv.org/abs/quant-ph/9605043
- **`PROOS03-ECC`** — John Proos and Christof Zalka, “Shor’s Discrete Logarithm Quantum Algorithm for Elliptic Curves,” Quantum Information & Computation 3(4), 2003. https://arxiv.org/abs/quant-ph/0301141
- **`GE21-RSA`** — Craig Gidney and Martin Ekerå, “How to Factor 2048-bit RSA Integers in 8 Hours Using 20 Million Noisy Qubits,” Quantum 5, 2021. https://doi.org/10.22331/q-2021-04-15-433
- **`KUP05-HIDDENSHIFT`** — Greg Kuperberg, “A Subexponential-Time Quantum Algorithm for the Dihedral Hidden Subgroup Problem,” SIAM Journal on Computing 35(1), 2005. https://doi.org/10.1137/S0097539703436345
- **`CJS14-ISOGENYQ`** — Andrew M. Childs, David Jao, and Vladimir Soukharev, “Constructing Elliptic Curve Isogenies in Quantum Subexponential Time,” Journal of Mathematical Cryptology 8(1), 2014. https://doi.org/10.1515/jmc-2012-0016
- **`BERN10-QCODE`** — Daniel J. Bernstein, “Grover vs. McEliece,” PQCrypto 2010. https://cr.yp.to/codes/grovercode-20100303.pdf

## Security notions, transforms, protocols, standards, and current specifications

- **`UNRUH17-QROM`** — Dominique Unruh, “Post-Quantum Security of Fiat–Shamir,” ASIACRYPT 2017; IACR ePrint 2017/398. https://eprint.iacr.org/2017/398
