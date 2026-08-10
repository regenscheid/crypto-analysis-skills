# crypto-analysis-skills

Skills for doing original cryptanalysis with Claude Science. **Skills only** — no
connectors, no corpora, no local servers. Everything they retrieve comes from one
remote MCP server.

This is a workbench, not a benchmark: it surfaces information to amplify a
cryptographer, rather than hiding it to score a model.

## What you need

**One MCP server**, added in Claude Science under *Settings → Connectors → Add
connector → remote / URL*:

```
https://research-mcp-api.npages.org/mcp
```

It bundles ePrint, the NIST CSRC publications, Firecrawl (web and paper search)
and a plain web fetcher. `skills/investigate/reference/tools.md` maps capability
to tool name — read that rather than guessing, and call `portal_list_servers`
when a name does not resolve, because the roster changes.

**Optional, per machine.** Two skills reach past the MCP server and degrade
honestly when the thing is absent:

| skill | wants | without it |
|---|---|---|
| `analyze-scheme` | Sage + `cryptographic_estimators` for `scripts/sweep.py` | name the cost model you could not run and put it in `NOT CHECKED` |
| `magma` | an SSH compute provider configured in Claude Science | skip; nothing else depends on it |

`workbench-knowledge` writes three markdown files to **`CRYPTO_FILES`**
(default `~/crypto-workbench-files`). Point it somewhere the session can write.

## The skills

**The loop.** Everything else is a tool it reaches for.

| | |
|---|---|
| **`investigate`** | question → what is known → claims → a plan → work it → an answer that cites its own evidence. Picks **VALIDATE** or **DISCOVER** mode up front, because the stopping rule differs. |

**Modes of work**, each with a boundary line naming its nearest neighbour:

| | |
|---|---|
| `analyze-scheme` | is a scheme secure — hard problem, known attacks, margin, where an attack would improve |
| `analyze-paper` | does the proof support the claim — notions, models, reduction loss |
| `discover-cryptanalysis` | search for new attack directions; produces falsifiable candidates, not verdicts |
| `validate-attack` | does a specific claimed attack hold up — by analysis or by implementation |
| `verify-claim` | settle one discrete claim |
| `derive-cost` | produce a cost where none was published |

**Supporting:**

| | |
|---|---|
| `crypto-review` | adversarial check on your own output — cost models, preconditions, notion misuse, invalid inferences |
| `workbench-knowledge` | what has been established, what was looked for and not found, lessons |
| `magma` | algebra a local kernel cannot do, on a remote compute host |

Several ship `reference/` material — security definitions as checkable
obligations, attack-family checklists, verified Sage idioms, a transfer routing
table, and the environment's measured constraints.

## Three rules that run through all of it

**Never say "verified".** Computation falsifies; it does not verify. The
vocabulary is "no counterexample at n ≤ N", with N stated.

**A negative is a claim about your search.** "Not found on ePrint" and "not found
on ePrint, the NIST round reports, and the web" are different findings, and only
the second licenses anything. A large share of competition cryptanalysis was
never a paper — it was a forum post — which is why the web channel matters.

**A cost figure without its model is not a result.** Name the model, give the
spread, record the versions.

## Provenance

Adapted from `claude-science-crypto`, which carried its own local connectors. The
skills are the same discipline; the retrieval layer moved to a hosted server. The
measured findings inside them — why a bound belongs in code rather than a
docstring, why a subagent must never wait on a human, why an artifact saved by
filename forks — are kept as measurements, with what was observed and when.
