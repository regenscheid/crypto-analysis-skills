# References for NTRU and Falcon Analysis

These references are starting points, not substitutes for checking the exact target version, later corrections, implementation artifacts, and subsequent cryptanalysis.

When using a reference:

- cite the exact theorem, algorithm, table, parameter set, or source-code revision used;
- preserve the source adversary model and success definition;
- distinguish asymptotic analysis, concrete estimates, and implemented results;
- search for errata, follow-up attacks, rebuttals, and revised specifications;
- record any transfer from the cited object to the current target in a transfer matrix.

## Lattice problems, estimators, encryption, and signatures

- **`NTRU98`** — Jeffrey Hoffstein, Jill Pipher, and Joseph H. Silverman, “NTRU: A Ring-Based Public Key Cryptosystem,” ANTS III, 1998. https://doi.org/10.1007/BFb0054868
- **`CS97-NTRU`** — Don Coppersmith and Adi Shamir, “Lattice Attacks on NTRU,” EUROCRYPT 1997. https://doi.org/10.1007/3-540-69053-0_5
- **`HG07-NTRUHYBRID`** — Nick Howgrave-Graham, “A Hybrid Lattice-Reduction and Meet-in-the-Middle Attack Against NTRU,” CRYPTO 2007. https://doi.org/10.1007/978-3-540-74143-5_9
- **`ABD16-SUBFIELD`** — Martin R. Albrecht, Shi Bai, and Léo Ducas, “A Subfield Lattice Attack on Overstretched NTRU Assumptions,” CRYPTO 2016; IACR ePrint 2016/127. https://eprint.iacr.org/2016/127
- **`NTRUPRIME17`** — Daniel J. Bernstein et al., “NTRU Prime: Reducing Attack Surface at Low Cost,” SAC 2017; IACR ePrint 2016/461. https://eprint.iacr.org/2016/461
- **`GS02-IDEALGEN`** — Craig Gentry and Michael Szydlo, “Cryptanalysis of the Revised NTRU Signature Scheme,” EUROCRYPT 2002. https://doi.org/10.1007/3-540-46035-7_21
- **`CDPR16-IDEAL`** — Ronald Cramer, Léo Ducas, Chris Peikert, and Oded Regev, “Recovering Short Generators of Principal Ideals in Cyclotomic Rings,” EUROCRYPT 2016; IACR ePrint 2015/313. https://eprint.iacr.org/2015/313
- **`GPV08`** — Craig Gentry, Chris Peikert, and Vinod Vaikuntanathan, “Trapdoors for Hard Lattices and New Cryptographic Constructions,” STOC 2008; IACR ePrint 2007/432. https://eprint.iacr.org/2007/432
- **`FALCON18`** — Pierre-Alain Fouque et al., “Falcon: Fast-Fourier Lattice-Based Compact Signatures over NTRU,” NIST PQC submission and IACR ePrint 2018/1234. https://eprint.iacr.org/2018/1234
- **`PEIKERT10-GAUSS`** — Chris Peikert, “An Efficient and Parallel Gaussian Sampler for Lattices,” CRYPTO 2010. https://doi.org/10.1007/978-3-642-14623-7_5
- **`NR06-HPP`** — Phong Q. Nguyen and Oded Regev, “Learning a Parallelepiped: Cryptanalysis of GGH and NTRU Signatures,” EUROCRYPT 2006. https://doi.org/10.1007/11761679_17

## Security notions, transforms, protocols, standards, and current specifications

- **`FALCON-SPEC`** — Falcon team, Falcon: Fast-Fourier Lattice-based Compact Signatures over NTRU, specification and supporting material. https://falcon-sign.info/
