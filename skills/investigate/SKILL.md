---
name: investigate
description: Conduct rigorous end-to-end cryptographic security investigations and visibly route them through the relevant cryptanalysis or formal-method skills. Use whenever asked to analyze a scheme or paper, find issues or weaknesses, search for attacks, reproduce or validate a result, audit a security claim or proof, compare parameters, or resume cryptographic research. Infer the requested task from its intent; individual words such as “new” do not by themselves select a mode.
---

# Investigate cryptographic security

Act as the control plane. Select and load the relevant specialist skills, keep a
coverage record, execute the work, and show which skills actually contributed.
Do not merely recommend skills or stop after writing a plan.

## Scope and mathematical work

The host owns project knowledge, persistence, and resumption. Use supplied
context; do not create another knowledge or checkpoint system. Physical-security
investigations are outside this effort's scope.

For an explicitly stated mathematical question, use
`mathematical-research-development` to produce definitions, lemmas, derivations,
or scoped partial results. Read
[the evidence distinctions](reference/evidence-interpretation.md) when choosing
what a result can support. Formal proof assistants remain optional.

Known inputs do not need to be reproduced on every continuation. Recheck when
their assumptions, version, or reliability affect the current inference. A
partial derivation with explicit open premises is a result worth reporting.

## Declare the mode

State one mode before substantive work. Infer it from the request; do not ask
when the language already decides it.

| Mode | Use when | Stopping rule |
|---|---|---|
| **ASSESS** | Map a scheme, paper, proof, or parameter set against known results | Cover the applicable known families and qualify every conclusion |
| **DISCOVER** | Find issues, weaknesses, attacks, improvements, transfers, or unexplored directions | Generate and cheaply falsify structurally distinct candidates; literature review alone is not completion |
| **VALIDATE** | Check or reproduce a specific attack, claim, computation, or citation | Settle the claim or identify the exact unresolved obligation |
| **FORMALIZE** | Produce machine-checked proof, certified computation, or implementation refinement | Replay the artifact and state its model and trusted computing base |

Use separate phases when the request combines discovery and independent
validation. Do not let the validating phase improve the candidate it is meant
to check.

## Freeze the target

Record before analysis:

- exact primitive, construction, implementation, or document;
- version, revision, parameter set, rounds, and artifact identifiers;
- claimed property and security notion;
- attacker powers, oracle access, quantum model, and exclusions;
- available evidence, implementations, tools, and compute limits.

If an essential item is missing, continue on the parts it does not block and
mark every conditional conclusion. Never silently substitute a nearby version.

## Catalog references

Read [catalog use](reference/catalog-use.md) when consulting the
configured catalog MCP server. It supplies changing examples and citations;
linked skills are relevant reading, not mandatory invocations.

## Establish source grounding

Begin a source and prior-art track before expensive computation or original
attack development. In `ASSESS` and `DISCOVER`, load the domain literature
extractor (`symmetric-literature-attack-extractor` or
`public-key-literature-attack-extractor`). The structure-first track may run in
parallel so it remains intellectually independent; it does not replace source
grounding.

Search the exact target and aliases, components and assumptions, normative
specifications, known attacks and failed approaches, errata and follow-ups,
implementations and issue discussions, and relevant non-paper sources. Open the
body or exact artifact for every load-bearing result; titles, snippets, and
abstracts are discovery evidence only.

Maintain the source-grounding record in
[`reference/completion-contract.md`](reference/completion-contract.md). If a
retrieval capability is absent or repeatedly fails, try a distinct available
route, record the failure, and flag the blocked coverage to the user. Continue
only with work that does not depend on the missing source, labeled as such.

## Route explicitly

Load the matching domain orchestrator before technique work:

- symmetric primitive, hash, stream cipher, mode, MAC, or AEAD:
  `symmetric-cryptanalysis-orchestrator`;
- public-key encryption, KEM, signature, key agreement, or mathematical
  assumption: `public-key-cryptanalysis-orchestrator`;
- machine-checked evidence: `formal-methods-router`, only when requested or when
  its expected assurance justifies its modeling cost;
- mixed construction: load every applicable orchestrator and keep their claims
  separate.

Also load the object-level workflow when relevant: `analyze-scheme`,
`analyze-paper`, `validate-attack`, `verify-claim`, `derive-cost`, or
`discover-cryptanalysis`.

From each orchestrator, select every applicable technique family—not merely the
most familiar one. Load a technique skill before relying on its procedure. Add
each selected skill to the skill trace with a one-line reason. Add excluded
families to the coverage ledger with a concrete non-applicability reason.

## Execute the investigation

Work in dependency order and update the evidence state after each material
result:

1. Establish the source-grounding record from project knowledge and
   authoritative primary sources.
2. Formalize the claim and normalize the target structure.
3. Establish generic attacks, security baselines, and claimed margins.
4. Normalize relevant prior attacks with exact preconditions and costs.
5. Map the full applicable attack surface.
6. In DISCOVER mode, generate hypotheses from structure, proof seams,
   distributions, interfaces, and transfer—not from analogy alone.
7. Apply the cheapest decisive falsifier to each viable hypothesis before
   developing it further.
8. Recompute end-to-end complexity, success probability, memory, data, oracle
   access, preprocessing, verification, and amortization in named models.
9. Independently review every load-bearing claim before presenting it.

Use more than one structurally independent hypothesis source in DISCOVER mode
unless the target rules the others out. A failed search or solver timeout updates
the ledger; it never becomes evidence of security.

## Select computational tools by capability

Before a computation can become load-bearing, read
[`reference/computation.md`](reference/computation.md). Identify the capability
the method requires, inspect the execution routes actually available on the
current platform, and choose the best suitable implementation. Do not assume
Python, SageMath, R, Magma, or any other named program is always present or
always preferred.

Prefer a suitable executable already visible inside the analysis environment,
then an existing managed environment, then an isolated environment provisioned
through the platform, and finally an approved configured remote resource.
Preserve the host's sandbox, permissions, credential handling, environment
management, and execution manifests.

## Enforce completion

Maintain the ledger and status vocabulary in
[`reference/completion-contract.md`](reference/completion-contract.md). A final
answer is incomplete unless it contains:

- the mode and frozen target;
- the source-grounding record, including searched channels, opened sources, and
  retrieval gaps;
- a skill trace naming the skills actually loaded and used;
- a coverage row for every applicable or considered family;
- evidence and scope for every material finding;
- candidate outcomes and falsification status in DISCOVER mode;
- unresolved obligations, blocked work, and the next decisive test.

Do not conclude DISCOVER mode after finding prior work, generating vague ideas,
or testing one favorite family. Do not conclude FORMALIZE mode from source text
that was not replayed. Do not call a scheme secure or an analysis verified;
state the bounded evidence and what was not checked.

## Plan without stalling

Use a plan for genuinely multi-stage work, parallel tracks, or expensive
compute. Keep it short enough to begin execution immediately after any required
approval. Skip formal planning for a single lookup or bounded computation.

When a plan changes, preserve completed evidence and explain the changed
premise. Mark blocked and abandoned tracks explicitly. Never treat plan creation
as the requested research result.

## Use the current platform correctly

Keep the investigation procedure platform-neutral. When running in Claude
Science, read:

- [`reference/claude-science.md`](reference/claude-science.md) before the first
  call to `ask_user`, `generate_plan`, `update_step_status`, `host.delegate`,
  `request_network_access`, or `save_artifacts`; its exact call patterns and
  verified elicitation and approval rules are required, not optional background;
- [`reference/tools.md`](reference/tools.md) before any literature, web, or
  document retrieval; translate capability needs to the tools actually present;
- [`reference/computation.md`](reference/computation.md) before selecting,
  installing, provisioning, or remotely invoking computational software;
- [`reference/environment.md`](reference/environment.md) when sandbox, network,
  kernel, connector, or artifact behavior affects the work.

If a named tool is unavailable, discover the current equivalent. After a
repeated identical failure, stop retrying that route, record the retriable
failure, try a distinct route, and tell the user if the capability remains
blocked. Do not fabricate a successful call or silently downgrade the grounding
requirement.

## Report from evidence

Use this compact order:

1. **Mode and target**
2. **Skill trace**
3. **Source and prior-art grounding**
4. **Claim and attack-surface map**
5. **Coverage ledger**
6. **Findings and surviving candidates**
7. **Validation, costs, and confidence**
8. **Limits and next decisive work**

Answer the user’s original question directly. Artifacts and plans support the
answer; they are not substitutes for it.
