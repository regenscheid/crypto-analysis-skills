# References for PKE Security and Adaptive-Oracle Analysis

These references are starting points, not substitutes for checking the exact target version, later corrections, implementation artifacts, and subsequent cryptanalysis.

When using a reference:

- cite the exact theorem, algorithm, table, parameter set, or source-code revision used;
- preserve the source adversary model and success definition;
- distinguish asymptotic analysis, concrete estimates, and implemented results;
- search for errata, follow-up attacks, rebuttals, and revised specifications;
- record any transfer from the cited object to the current target in a transfer matrix.

## Integer factorization, RSA, and adaptive decryption attacks

- **`HASTAD88`** — Johan Håstad, “Solving Simultaneous Modular Equations of Low Degree,” SIAM Journal on Computing 17(2), 1988. https://doi.org/10.1137/0217013
- **`COP96-SMALLROOTS`** — Don Coppersmith, “Finding a Small Root of a Bivariate Integer Equation; Factoring with High Bits Known,” EUROCRYPT 1996. https://doi.org/10.1007/3-540-68339-9_16
- **`BLE98`** — Daniel Bleichenbacher, “Chosen Ciphertext Attacks Against Protocols Based on the RSA Encryption Standard PKCS #1,” CRYPTO 1998. https://doi.org/10.1007/BFb0055716
- **`MANGER01`** — James Manger, “A Chosen Ciphertext Attack on RSA Optimal Asymmetric Encryption Padding (OAEP),” CRYPTO 2001. https://doi.org/10.1007/3-540-44647-8_14

## Security notions, transforms, protocols, standards, and current specifications

- **`GM84-PKE`** — Shafi Goldwasser and Silvio Micali, “Probabilistic Encryption,” Journal of Computer and System Sciences 28(2), 1984. https://doi.org/10.1016/0022-0000(84)90070-9
- **`BDPR98-PKE`** — Mihir Bellare, Anand Desai, David Pointcheval, and Phillip Rogaway, “Relations Among Notions of Security for Public-Key Encryption Schemes,” CRYPTO 1998. https://doi.org/10.1007/BFb0055718
- **`CS98-CCA`** — Ronald Cramer and Victor Shoup, “A Practical Public Key Cryptosystem Provably Secure Against Adaptive Chosen Ciphertext Attack,” CRYPTO 1998. https://doi.org/10.1007/BFb0055717
- **`RFC8017`** — Kathleen Moriarty et al., PKCS #1: RSA Cryptography Specifications Version 2.2, RFC 8017, 2016. https://www.rfc-editor.org/rfc/rfc8017
