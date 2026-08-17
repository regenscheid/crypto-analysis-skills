# References for Threshold, Multisignature, and Aggregate-Signature Analysis

These references are starting points, not substitutes for checking the exact target version, later corrections, implementation artifacts, and subsequent cryptanalysis.

When using a reference:

- cite the exact theorem, algorithm, table, parameter set, or source-code revision used;
- preserve the source adversary model and success definition;
- distinguish asymptotic analysis, concrete estimates, and implemented results;
- search for errata, follow-up attacks, rebuttals, and revised specifications;
- record any transfer from the cited object to the current target in a transfer matrix.

## Elliptic curves, generic groups, and pairings

- **`BLS01`** — Dan Boneh, Ben Lynn, and Hovav Shacham, “Short Signatures from the Weil Pairing,” ASIACRYPT 2001. https://doi.org/10.1007/3-540-45682-1_30

## Security notions, transforms, protocols, standards, and current specifications

- **`BN06-FORK`** — Mihir Bellare and Gregory Neven, “Multi-signatures in the Plain Public-Key Model and a General Forking Lemma,” ACM CCS 2006. https://doi.org/10.1145/1180405.1180453
- **`MUSIG18`** — Gregory Maxwell et al., “Simple Schnorr Multi-Signatures with Applications to Bitcoin,” IACR ePrint 2018/068. https://eprint.iacr.org/2018/068
- **`MUSIG2-21`** — Jonas Nick, Tim Ruffing, and Yannick Seurin, “MuSig2: Simple Two-Round Schnorr Multi-Signatures,” CRYPTO 2021; IACR ePrint 2020/1261. https://eprint.iacr.org/2020/1261
- **`DRIJVERS19-MULTISIG`** — Manu Drijvers et al., “On the Security of Two-Round Multi-Signatures,” IEEE Symposium on Security and Privacy 2019; IACR ePrint 2018/417. https://eprint.iacr.org/2018/417
- **`RFC9591-FROST`** — Deirdre Connolly et al., The Flexible Round-Optimized Schnorr Threshold (FROST) Protocol for Two-Round Schnorr Signatures, RFC 9591, 2024. https://www.rfc-editor.org/rfc/rfc9591
- **`SHOUP00-THRSA`** — Victor Shoup, “Practical Threshold Signatures,” EUROCRYPT 2000. https://doi.org/10.1007/3-540-45539-6_10
- **`LINDELL17-2ECDSA`** — Yehuda Lindell, “Fast Secure Two-Party ECDSA Signing,” CRYPTO 2017; IACR ePrint 2017/552. https://eprint.iacr.org/2017/552
- **`RFC6979`** — Thomas Pornin, Deterministic Usage of DSA and ECDSA, RFC 6979, 2013. https://www.rfc-editor.org/rfc/rfc6979
