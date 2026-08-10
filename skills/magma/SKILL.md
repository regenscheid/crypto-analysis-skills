---
name: magma
description: Run Magma computations on the remote SSH compute host — Gröbner bases and MQ systems, finite fields and polynomial rings, elliptic curves and isogenies, linear algebra over small fields. Use when a cryptanalytic claim needs an actual computation rather than an estimate, when a cost model needs checking at toy scale before being trusted at real scale, or when the algebra is beyond what the local Sage kernel can do.
license: Apache-2.0
---

# Magma

Magma runs on a **compute host**, not through a connector. There is no
`magma_run` tool and no `cas` connector — an earlier version of this skill said
there was, and calling it fails with `host_call 'mcp' failed`.

Why it works this way, so you can reason when something breaks: a connector's
sandbox gets no direct network, only a proxy, and that proxy **refuses port 22
to every host** (measured). SSH from a connector is not a misconfiguration, it
is not permitted. Claude Science reaches the host itself, outside the sandbox,
using the user's own ssh and `~/.ssh/config`.

---

## 0. The rule that matters most: the exit code lies

**Magma exits 0 when your script fails.** Measured on the host for every error
class: exit code **0**, stderr **empty**, diagnostic on **stdout**.

`SetQuitOnError(true)` promotes most classes to exit 1 — syntax errors, bad
argument types, failed asserts, `error "..."`, illegal zero denominator — but
**not undeclared identifiers**, which still exit 0 while halting the script.

This is dangerous here specifically because `compute_result` hands you an
`exit_code`, and it will say `0`:

> A script that prints a good number and *then* hits a typo produces that
> number, stops, and reports success. Partial output is indistinguishable from
> complete output unless you look.

**So: never accept a result on `exit_code` alone.** Scan stdout for a line
beginning `User error:` or `Runtime error:`. Anything printed above such a line
is real but **incomplete**.

Cheapest total defence — make the script assert its own completion:

```magma
SetQuitOnError(true);
// ... work ...
printf "done\n";
```

If `done` is absent from stdout, the run failed no matter what the exit code
says. Do this in every script.

---

## 1. Running something

Submit a job to your SSH compute provider. `ssh:<host>` below is whatever you
named it in Settings > Compute; `list_compute` reports the configured providers.

```
compute_submit(
  provider = "ssh:<host>",
  command  = "magma -b job.m < /dev/null",
  intent   = "why this run exists, in one line",
  inputs   = [{"src": "job.m"}],
  outputs  = [{"glob": "out/*.txt", "visibility": "featured"}],
  timeout_seconds = 600,
)
```

then `compute_result(provider=…, job_id=…)`, and `compute_close` when done.
`compute_cancel` stops a runaway job.

Two flags in that command are not optional:

- **`-b`** suppresses Magma's banner, which is otherwise indistinguishable from
  your output.
- **`< /dev/null`** matters more than it looks: on an error Magma falls back to
  reading stdin and will silently consume whatever is feeding the process.
  Observed eating the rest of a driving shell script mid-run.

### Make it killable — `compute_cancel` alone does NOT stop Magma

**Use this form, not a bare `magma` command:**

```
exec timeout -k 10 3600 magma -b job.m < /dev/null
```

Both words earn their place, and this exact combination is verified on the host:

- **`exec`** replaces the wrapper shell with the process being run. Without it,
  cancelling kills the *shell* and Magma is **reparented to PID 1 and keeps
  running** — measured, and observed in the wild: a cancelled job carried on
  burning four threads while the platform reported `status: cancelled`.
- **`timeout -k`** is the backstop for everything the signal path misses. It
  exits 124 and leaves nothing behind. Set it to something you would actually
  accept, not the maximum.

Magma itself is well behaved — it dies on `SIGTERM`. The orphan is created by
the wrapper, not by Magma ignoring signals, which is why `exec` fixes it.

**A cancelled job is not a stopped job until you have checked.** After
`compute_cancel`, confirm nothing survived:

```
ps -eo pid,ppid,etime,pcpu,args | grep [m]agma
```

A `PPID` of `1` is the signature: that process was orphaned and nothing will
reap it but its own `timeout`. Kill it by PID.

**The same trap catches interactive ssh.** A local `ssh host 'magma …'` that
hits *your* client-side timeout leaves the remote Magma running — the local
process died, the remote one never heard about it. Wrap remote commands in
`timeout` too.

Write the script to a file and pass it as an `input` rather than inlining a
heredoc — the file is then the reproducible artefact, which is what
`verify-claim` will ask for.

### Long jobs: make progress pollable

**The SSH provider has no live log** — the panel says so, and output only appears
when the job completes. For a run that may take hours that is not good enough:
you cannot tell "still working" from "wedged", and neither can the human.

Magma flushes to a log file **as it runs** (verified: content readable 2 s in,
growing at 5 s). So give every long job a log:

```magma
SetLogFile("/tmp/<jobname>.log" : Overwrite := true);
SetVerbose("Groebner", 1);        // step degrees as F4 reaches them
```

Then read it whenever asked, with a **second, trivial** compute job that returns
in seconds:

```
compute_submit(provider="ssh:<host>",
               command="tail -40 /tmp/<jobname>.log",
               intent="progress check", timeout_seconds=30)
```

For Gröbner work this is the difference between waiting blind and knowing: the
verbose trace shows the **step degree** as it climbs, and the degree is what
predicts whether the run will finish at all. A job sitting at degree 7 with the
memory still flat is progressing; one that jumped a degree may not land.

**If a job is already running without a log**, you cannot retrofit one. The
fallback is coarse but real — `ps -eo pid,etime,pcpu,rss,args | grep [m]agma`
gives elapsed time, CPU and resident memory, which distinguishes "working hard"
from "stuck" even without knowing how far along it is.

### The host — read its own notes, do not rely on this file

**The host carries its own description**, in the compute provider's notes
(`memory_md`, shown when you use it). That is the authority on what is installed
and how to run there, and it reaches agents that never loaded this skill.
Keep a note of your own host's quirks — Magma version, thread defaults, scratch
space — in the provider's `memory_md`, which the agent reads before running.
Spelled with the `<repo>/` prefix because a bare `reference/` now means *this
skill's own* reference directory.

The shape of it, so you can plan before submitting: Ubuntu, **40 cores, 503 GB**,
no scheduler, Magma 2.28-23, **and since 2026-08-06 Sage 10.9 as well** (just
run `sage`; it is reachable from dispatched jobs, not only interactive logins).
Plenty of `/tmp`. Concurrency is fine —
the licence is machine-level, not a per-session slot. **`GetNthreads()` is 1 by
default**, so a job takes one of forty cores unless it asks.

**Deliberate duplication, and only here:** §0's exit-code trap appears in both
this skill and the host notes. Everything else is stated once. That one is
repeated because it is the only failure that yields a *plausible wrong number*
rather than an error, and it must survive either document going unread.

If the two disagree, the host notes win on host facts — they sit next to the
machine. Fix this file rather than working around it.

---

## 2. How to use it well

**Toy scale first, always.** Run where you know the answer, confirm it
reproduces, then scale. This is the only way to tell "the algebra is wrong" from
"the parameters are big". A Gröbner basis returning `[1]` means the system is
inconsistent, which usually indicts your *encoding*, not the cryptography.

**Plant the answer.** To test a solver, build a system with a known solution:

```magma
sol := [Random(K) : i in [1..n]];
eqs := [f - Evaluate(f, sol) : f in randoms];   // vanish at sol by construction
```

Verified: recovers the planted solution for 10 variables, 12 quadratics over
GF(2) in 0.03s. A random system without this step is usually inconsistent and
teaches you nothing.

**Know the cost curve before committing.** Measured, random dense quadratics
over GF(2) with `m = n` plus field equations, 8 threads:

| n | CPU seconds |
|---|---|
| 20 | 2.1 |
| 24 | 57 |
| 28 | 723 |

Roughly 12× per +4 variables. Single trials — the variance is unmeasured, so
treat these as sizing guidance, not a scaling law.

**Name the cost model.** A timing from this host is a measurement on *this
host*. It supports "this took 57s at n=24"; it does not by itself support a
security level. Extrapolating needs a stated model — that is what `sweep.py` is
for.

**Print machine-readable output.** `%o` is Magma's directive (not `%s`, not
`%d`):

```magma
printf "gb_size=%o max_deg=%o secs=%o\n", #G, Max([TotalDegree(g) : g in G]), secs;
```

---

## 3. Idioms verified to run on this host

**Finite fields and polynomial rings**
```magma
P<x> := PolynomialRing(GF(2));
print IsIrreducible(x^8 + x^4 + x^3 + x + 1);      // true
```
Build the ring over the field you actually mean. The Rijndael polynomial is
irreducible over `GF(2)` and *reducible* over `GF(2^8)` — asking the second
question and reading it as the first is easy and silent.

**MQ / Gröbner**
```magma
SetNthreads(8);
P := PolynomialRing(GF(2), n, "grevlex");       // grevlex, or you pay for nothing
t := Cputime(); G := GroebnerBasis(eqs); secs := Cputime(t);
V := Variety(ideal<P | eqs>);
```

**Linear algebra over small fields**
```magma
M := KMatrixSpace(GF(2), 4, 6) ! [Random(GF(2)) : i in [1..24]];
print Rank(M); print Dimension(Kernel(M));
```

**Elliptic curves**
```magma
E := EllipticCurve([GF(2^127 - 1) | 0, 7]);
print #E; print Factorisation(#E);
```

**Supersingularity / isogeny setting**
```magma
p := 431; F<i> := GF(p^2);
E := EllipticCurve([F | 1, 0]);
print IsSupersingular(E);        // true
print #E eq (p + 1)^2;           // true
```

---

## 4. Gotchas, all measured here

- **Heterogeneous tuples coerce silently.** `[<"n", 256>, <"cost", 1.5>]` turns
  `256` into `256.000000000000000000000000000`. Keep types uniform, or print
  values separately.
- **`Variety` returns tuples; your solution is probably a sequence.** `sol in V`
  fails with *"No valid universe containing all elements"*. Compare elementwise:
  `exists{v : v in V | [v[i] : i in [1..n]] eq sol}`.
- **`print a, b;` is not two values.** `print "dim:", Dimension(I)` printed
  `dim: 1 [ 3 ]` — `Dimension` returned a dimension *and* an independent set.
  Use one `printf` with explicit directives when you intend to parse it.

---

## 5. Recording what you get

A Magma run is evidence of kind `computation`:

```python
update_step_status(step="<exact plan step title>", status="completed",
                   notes="GB terminated at degree 4, 57s CPU at n=24, planted solution recovered")

# and, once it is settled rather than merely observed:
add_entry("Random dense m=n MQ over GF(2) solves at n=24 in ~57s CPU (8 threads).",
          kind="measurement",
          evidence=[{"kind": "computation", "note": "<the script and its output>"}])
```

**Keep the script with the number.** A timing without the code that produced it
cannot be reproduced and `verify-claim` will flag it, correctly. One run on one
host is a data point, never established fact — that needs something
independent.

---

## What this must not do

- **Do not report a number without confirming the run completed.** `exit_code`
  0 is not success here; check for `done` and for error markers. This is the
  failure this skill exists to prevent.
- **Do not extrapolate a toy timing to a security level** without a named cost
  model.
- **Do not assume the host is unreachable because one call failed.** If ssh
  fails, the cause is almost always in `~/.ssh/config` and the human can check
  it with a one-line `ssh <host> true`. Say so, and carry on
  with claims that do not need Magma.
- **Do not report a job as stopped because `compute_cancel` returned.** It
  reports that the platform stopped *tracking* the job. Check for a surviving
  process before saying it is over — and if you launched without `exec`, expect
  one.
- **Do not leave a long run unbounded.** Every submission carries a `timeout`,
  because the failure mode is not a lost result — it is a computation nobody is
  watching, on a machine someone else is using.
