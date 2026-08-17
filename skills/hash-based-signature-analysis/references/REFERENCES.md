# References for Hash-Based Signature Analysis

These references are starting points, not substitutes for checking the exact target version, later corrections, implementation artifacts, and subsequent cryptanalysis.

When using a reference:

- cite the exact theorem, algorithm, table, parameter set, or source-code revision used;
- preserve the source adversary model and success definition;
- distinguish asymptotic analysis, concrete estimates, and implemented results;
- search for errata, follow-up attacks, rebuttals, and revised specifications;
- record any transfer from the cited object to the current target in a transfer matrix.

## Hash-based signatures

- **`LAMPORT79`** — Leslie Lamport, Constructing Digital Signatures from a One-Way Function, SRI technical report, 1979. https://www.microsoft.com/en-us/research/publication/constructing-digital-signatures-one-way-function/
- **`MERKLE79`** — Ralph C. Merkle, “Secrecy, Authentication, and Public Key Systems,” Ph.D. dissertation, Stanford University, 1979. https://www.merkle.com/papers/Thesis1979.pdf
- **`WOTS89`** — Ralph C. Merkle, “A Certified Digital Signature,” CRYPTO 1989; describes the Winternitz one-time signature. https://doi.org/10.1007/0-387-34805-0_21
- **`HULSING13-WOTSPLUS`** — Andreas Hülsing, “W-OTS+—Shorter Signatures for Hash-Based Signature Schemes,” AFRICACRYPT 2013. https://doi.org/10.1007/978-3-642-38553-7_10
- **`RFC8391-XMSS`** — Andreas Hülsing et al., XMSS: eXtended Merkle Signature Scheme, RFC 8391, 2018. https://www.rfc-editor.org/rfc/rfc8391
- **`RFC8554-LMS`** — David McGrew et al., Leighton-Micali Hash-Based Signatures, RFC 8554, 2019. https://www.rfc-editor.org/rfc/rfc8554
- **`NIST-SP800-208`** — NIST SP 800-208, Recommendation for Stateful Hash-Based Signature Schemes, 2020. https://csrc.nist.gov/pubs/sp/800/208/final
- **`SPHINCS15`** — Daniel J. Bernstein et al., “SPHINCS: Practical Stateless Hash-Based Signatures,” EUROCRYPT 2015. https://doi.org/10.1007/978-3-662-46800-5_15
- **`SPHINCSPLUS19`** — Jean-Philippe Aumasson et al., “SPHINCS+: A Stateless Hash-Based Signature Framework,” ACM CCS 2019. https://sphincs.org/data/sphincs%2B-paper.pdf
- **`HULSING16-MULTITARGET`** — Andreas Hülsing, Joost Rijneveld, and Fang Song, “Mitigating Multi-Target Attacks in Hash-Based Signatures,” PKC 2016; IACR ePrint 2015/1256. https://eprint.iacr.org/2015/1256
- **`HULSING22-TIGHT`** — Andreas Hülsing et al., “Recovering the Tight Security Proof of SPHINCS+,” EUROCRYPT 2023; IACR ePrint 2022/346. https://eprint.iacr.org/2022/346
- **`PERLNER22-SPHINCS`** — Ray Perlner, “Breaking Category Five SPHINCS+ with SHA-256,” IACR ePrint 2022/1061. https://eprint.iacr.org/2022/1061

## Security notions, transforms, protocols, standards, and current specifications

- **`NIST-FIPS205`** — NIST FIPS 205, Stateless Hash-Based Digital Signature Standard (SLH-DSA), 2024. https://csrc.nist.gov/pubs/fips/205/final
