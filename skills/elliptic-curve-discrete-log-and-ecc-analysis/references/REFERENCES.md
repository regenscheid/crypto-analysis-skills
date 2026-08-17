# References for Elliptic-Curve Discrete-Log and ECC Analysis

These references are starting points, not substitutes for checking the exact target version, later corrections, implementation artifacts, and subsequent cryptanalysis.

When using a reference:

- cite the exact theorem, algorithm, table, parameter set, or source-code revision used;
- preserve the source adversary model and success definition;
- distinguish asymptotic analysis, concrete estimates, and implemented results;
- search for errata, follow-up attacks, rebuttals, and revised specifications;
- record any transfer from the cited object to the current target in a transfer matrix.

## Elliptic curves, generic groups, and pairings

- **`MILLER85-ECC`** — Victor S. Miller, “Use of Elliptic Curves in Cryptography,” CRYPTO 1985. https://doi.org/10.1007/3-540-39799-X_31
- **`KOBLITZ87-ECC`** — Neal Koblitz, “Elliptic Curve Cryptosystems,” Mathematics of Computation 48(177), 1987. https://doi.org/10.2307/2007884
- **`MOV93`** — Alfred Menezes, Tatsuaki Okamoto, and Scott Vanstone, “Reducing Elliptic Curve Logarithms to Logarithms in a Finite Field,” IEEE Transactions on Information Theory 39(5), 1993. https://doi.org/10.1109/18.259647
- **`FREYRUCK94`** — Gerhard Frey and Hans-Georg Rück, “A Remark Concerning m-divisibility and the Discrete Logarithm in the Divisor Class Group of Curves,” Mathematics of Computation 62, 1994. https://doi.org/10.1090/S0025-5718-1994-1218343-6
- **`SMART99-ANOMALOUS`** — Nigel P. Smart, “The Discrete Logarithm Problem on Elliptic Curves of Trace One,” Journal of Cryptology 12, 1999. https://doi.org/10.1007/s001459900052
- **`SEMA97-ANOMALOUS`** — Igor Semaev, “Evaluation of Discrete Logarithms in a Group of p-torsion Points of an Elliptic Curve in Characteristic p,” Mathematics of Computation 67, 1998. https://doi.org/10.1090/S0025-5718-98-00987-2
- **`BMM00-INVALIDCURVE`** — Ingrid Biehl, Bernd Meyer, and Volker Müller, “Differential Fault Attacks on Elliptic Curve Cryptosystems,” CRYPTO 2000; includes invalid-curve techniques. https://doi.org/10.1007/3-540-44598-6_9
- **`ANTIPA03-VALIDATION`** — Adrian Antipa et al., “Validation of Elliptic Curve Public Keys,” PKC 2003. https://doi.org/10.1007/3-540-36288-6_15
- **`GLV01`** — Robert Gallant, Robert Lambert, and Scott Vanstone, “Faster Point Multiplication on Elliptic Curves with Efficient Endomorphisms,” CRYPTO 2001. https://doi.org/10.1007/3-540-44647-8_11
- **`CURVE25519`** — Daniel J. Bernstein, “Curve25519: New Diffie–Hellman Speed Records,” PKC 2006. https://cr.yp.to/ecdh/curve25519-20060209.pdf
- **`VOW99-PARALLEL`** — Paul C. van Oorschot and Michael J. Wiener, “Parallel Collision Search with Cryptanalytic Applications,” Journal of Cryptology 12, 1999. https://doi.org/10.1007/PL00003816
- **`TESKE01-RHO`** — Edlyn Teske, “On Random Walks for Pollard’s Rho Method,” Mathematics of Computation 70, 2001. https://doi.org/10.1090/S0025-5718-00-01213-8

## Quantum algorithms and quantum resource analysis

- **`PROOS03-ECC`** — John Proos and Christof Zalka, “Shor’s Discrete Logarithm Quantum Algorithm for Elliptic Curves,” Quantum Information & Computation 3(4), 2003. https://arxiv.org/abs/quant-ph/0301141

## Security notions, transforms, protocols, standards, and current specifications

- **`RFC7748`** — Adam Langley, Mike Hamburg, and Sean Turner, Elliptic Curves for Security, RFC 7748, 2016. https://www.rfc-editor.org/rfc/rfc7748
- **`RFC8032`** — Simon Josefsson and Ilari Liusvaara, Edwards-Curve Digital Signature Algorithm (EdDSA), RFC 8032, 2017. https://www.rfc-editor.org/rfc/rfc8032
