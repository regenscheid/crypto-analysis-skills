# References for `sat-lrat-certification`

Reviewed through 2026-08-16.

- **LRAT17** — [LRAT: Efficiently Verifying Clausal Proofs](https://arxiv.org/abs/1612.02353) (2017) — Nathan Wetzler et al.. `research-paper`. Certificate format and checking methodology for SAT refutations.
- **FRAT22** — [FRAT: A Flexible Proof Format for SAT Solver Elaboration](https://arxiv.org/abs/2109.09665) (2022) — Marijn Heule et al.. `research-paper`. Solver-oriented proof logging and elaboration into checkable formats.
- **LRAT-CATCHER26** — [LRAT-Catcher: Importing SAT Refutations into Lean](https://arxiv.org/abs/2607.00815) (2026) — LRAT-Catcher authors. `research-paper`. Imports LRAT certificates and connects verified encodings to Lean theorems.
- **CADICAL-REPO** — [CaDiCaL SAT solver](https://github.com/arminbiere/cadical) (2026) — Armin Biere et al.. `official-repository`. Modern SAT solver with proof logging support; treat solver as untrusted when certificates are checked.
- **LEAN-BVDECIDE** — [Lean tactic reference: bv_decide and decision procedures](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/) (2026) — Lean project. `official-manual`. Documents proof-producing or kernel-checked tactics including bit-vector decision procedures.
