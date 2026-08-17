# References for Integer Factorization and RSA Analysis

These references are starting points, not substitutes for checking the exact target version, later corrections, implementation artifacts, and subsequent cryptanalysis.

When using a reference:

- cite the exact theorem, algorithm, table, parameter set, or source-code revision used;
- preserve the source adversary model and success definition;
- distinguish asymptotic analysis, concrete estimates, and implemented results;
- search for errata, follow-up attacks, rebuttals, and revised specifications;
- record any transfer from the cited object to the current target in a transfer matrix.

## Integer factorization, RSA, and adaptive decryption attacks

- **`RSA78`** — Ronald L. Rivest, Adi Shamir, and Leonard Adleman, “A Method for Obtaining Digital Signatures and Public-Key Cryptosystems,” Communications of the ACM 21(2), 1978. https://doi.org/10.1145/359340.359342
- **`RABIN79`** — Michael O. Rabin, Digitalized Signatures and Public-Key Functions as Intractable as Factorization, MIT/LCS/TR-212, 1979. https://publications.csail.mit.edu/lcs/pubs/pdf/MIT-LCS-TR-212.pdf
- **`POLLARD74-P1`** — John M. Pollard, “Theorems on Factorization and Primality Testing,” Proceedings of the Cambridge Philosophical Society 76, 1974. https://doi.org/10.1017/S0305004100049252
- **`POLLARD75-RHOFACT`** — John M. Pollard, “A Monte Carlo Method for Factorization,” BIT 15, 1975. https://doi.org/10.1007/BF01933667
- **`LENSTRA87-ECM`** — Hendrik W. Lenstra Jr., “Factoring Integers with Elliptic Curves,” Annals of Mathematics 126(3), 1987. https://doi.org/10.2307/1971363
- **`POM84-QS`** — Carl Pomerance, “The Quadratic Sieve Factoring Algorithm,” EUROCRYPT 1984. https://doi.org/10.1007/3-540-39757-4_17
- **`LL93-NFS`** — Arjen K. Lenstra and Hendrik W. Lenstra Jr., eds., The Development of the Number Field Sieve, Lecture Notes in Mathematics 1554, 1993. https://doi.org/10.1007/BFb0091534
- **`COP96-SMALLROOTS`** — Don Coppersmith, “Finding a Small Root of a Bivariate Integer Equation; Factoring with High Bits Known,” EUROCRYPT 1996. https://doi.org/10.1007/3-540-68339-9_16
- **`WIENER90`** — Michael J. Wiener, “Cryptanalysis of Short RSA Secret Exponents,” IEEE Transactions on Information Theory 36(3), 1990. https://doi.org/10.1109/18.54902
- **`BD99`** — Dan Boneh and Glenn Durfee, “Cryptanalysis of RSA with Private Key d Less than N^0.292,” EUROCRYPT 1999. https://doi.org/10.1007/3-540-48910-X_1
- **`HASTAD88`** — Johan Håstad, “Solving Simultaneous Modular Equations of Low Degree,” SIAM Journal on Computing 17(2), 1988. https://doi.org/10.1137/0217013
- **`BLE98`** — Daniel Bleichenbacher, “Chosen Ciphertext Attacks Against Protocols Based on the RSA Encryption Standard PKCS #1,” CRYPTO 1998. https://doi.org/10.1007/BFb0055716
- **`MANGER01`** — James Manger, “A Chosen Ciphertext Attack on RSA Optimal Asymmetric Encryption Padding (OAEP),” CRYPTO 2001. https://doi.org/10.1007/3-540-44647-8_14

## Quantum algorithms and quantum resource analysis

- **`GE21-RSA`** — Craig Gidney and Martin Ekerå, “How to Factor 2048-bit RSA Integers in 8 Hours Using 20 Million Noisy Qubits,” Quantum 5, 2021. https://doi.org/10.22331/q-2021-04-15-433

## Security notions, transforms, protocols, standards, and current specifications

- **`RFC8017`** — Kathleen Moriarty et al., PKCS #1: RSA Cryptography Specifications Version 2.2, RFC 8017, 2016. https://www.rfc-editor.org/rfc/rfc8017
