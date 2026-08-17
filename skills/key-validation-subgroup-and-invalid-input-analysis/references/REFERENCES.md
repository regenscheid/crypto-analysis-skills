# References for Key Validation, Subgroup, and Invalid-Input Analysis

These references are starting points, not substitutes for checking the exact target version, later corrections, implementation artifacts, and subsequent cryptanalysis.

When using a reference:

- cite the exact theorem, algorithm, table, parameter set, or source-code revision used;
- preserve the source adversary model and success definition;
- distinguish asymptotic analysis, concrete estimates, and implemented results;
- search for errata, follow-up attacks, rebuttals, and revised specifications;
- record any transfer from the cited object to the current target in a transfer matrix.

## Elliptic curves, generic groups, and pairings

- **`BMM00-INVALIDCURVE`** — Ingrid Biehl, Bernd Meyer, and Volker Müller, “Differential Fault Attacks on Elliptic Curve Cryptosystems,” CRYPTO 2000; includes invalid-curve techniques. https://doi.org/10.1007/3-540-44598-6_9
- **`ANTIPA03-VALIDATION`** — Adrian Antipa et al., “Validation of Elliptic Curve Public Keys,” PKC 2003. https://doi.org/10.1007/3-540-36288-6_15

## Finite-field discrete logarithms and Diffie–Hellman

- **`LIMLEE97-SUBGROUP`** — Chae Hoon Lim and Pil Joong Lee, “A Key Recovery Attack on Discrete Log-based Schemes Using a Prime Order Subgroup,” CRYPTO 1997. https://doi.org/10.1007/BFb0052259

## Isogenies, group actions, and quaternion methods

- **`GPST16-SIDH`** — Steven D. Galbraith, Christophe Petit, Barak Shani, and Yan Bo Ti, “On the Security of Supersingular Isogeny Cryptosystems,” ASIACRYPT 2016; IACR ePrint 2016/859. https://eprint.iacr.org/2016/859

## Security notions, transforms, protocols, standards, and current specifications

- **`RFC7748`** — Adam Langley, Mike Hamburg, and Sean Turner, Elliptic Curves for Security, RFC 7748, 2016. https://www.rfc-editor.org/rfc/rfc7748
- **`NIST-SP800-56A`** — NIST SP 800-56A Rev. 3, Recommendation for Pair-Wise Key-Establishment Schemes Using Discrete Logarithm Cryptography, 2018. https://csrc.nist.gov/pubs/sp/800/56/a/r3/final
