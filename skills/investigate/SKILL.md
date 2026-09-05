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
or scoped partial results. A standalone mathematical question does not require
a cryptographic family audit. Read
[the evidence distinctions](reference/evidence-interpretation.md) when choosing
what a result can support. Formal proof assistants remain optional.

Known inputs do not need to be reproduced on every continuation. Recheck when
their assumptions, version, or reliability affect the current inference. A
partial derivation with explicit open premises is a result worth reporting.

For mathematical cryptanalysis and research proposals, read
[the research workflow](reference/mathematical-research-workflow.md). Its product
boundaries govern the scope of the routing, execution, and completion lists below.
Use a full family assessment for an assessment assignment; a stated mathematical
question needs the relevant definitions and assumptions, not an unrelated audit.
Read [paper use and verification](reference/paper-use-and-verification.md) when
using literature. Invoke `verify-claim` for a correctness check of an assigned
claim, not merely because a published result is an ingredient.

For empirical observations and uncertainty, use
`empirical-statistical-and-heuristic-claim-separation` directly; it does not
require entering FORMALIZE mode.

When synthesizing delegated mathematics, apply
[orchestrator review](reference/delegated-mathematics-review.md) to correctness,
depth, and contribution labels. The main agent owns the final judgment even
when specialist work is complete.

## Declare the mode

State one mode before substantive work. Infer it from the request; do not ask
when the language already decides it.

| Mode | Use when | Stopping rule |
|---|---|---|
| **ASSESS** | Map a scheme, paper, proof, or parameter set against known results | Cover the applicable known families and qualify every conclusion |
| **DISCOVER** | Develop mathematical cryptanalysis, research questions, or proposals | Deliver the requested proposal or substantive mathematical progress with open obligations; do not claim more than the evidence supports |
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
attack development. When source normalization is part of the assignment, load the domain literature
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

For a full scheme assessment, cover every applicable family. For a proposal,
selected mathematical question, or paper verification, choose the capabilities
needed for that assignment. Load a technique skill before relying on its procedure
and explain why it was used. A question outside current scope is unexamined, not
mathematically inapplicable.

## Execute the investigation

For mathematical research, follow `discover-cryptanalysis` and develop the
selected question with `mathematical-research-development`. Retain open premises
and meaningful intermediate results; apply the completion rule for the requested
proposal or development task.

For a full scheme assessment, work through the relevant scope:

1. Establish source grounding and normalize the target's definitions and claims.
2. Identify applicable known families and their model assumptions.
3. Source or compute relevant generic and published comparisons in named models.
4. Map the coverage required for the assessment, including unexamined areas.
5. Support new quantitative conclusions with the relevant resource and success
   accounting; distinguish attributed results from independently checked values.
6. Report claim-level conclusions with their evidence and limitations.

For paper verification, give `verify-claim` the assigned statement and scope;
use `analyze-paper` when reviewing the whole document. A new session, citation,
or catalog subject link does not require repeating compatible prior checks.
A failed search or solver timeout supports a scoped statement about the attempt.

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
[`reference/completion-contract.md`](reference/completion-contract.md). Include the elements
needed to assess the requested product:

- the mode and frozen target;
- the source-grounding record, including searched channels, opened sources, and
  retrieval gaps;
- a skill trace naming the skills actually loaded and used;
- assessment coverage where assigned, distinguishing unexamined from inapplicable;
- evidence and scope for every material finding;
- the research proposal or mathematics produced in DISCOVER mode, with unresolved premises;
- unresolved obligations, blocked work, and the next meaningful mathematical step or test.

In DISCOVER mode, a requested research proposal can be complete with unresolved
questions. If mathematical development was requested, a survey or another list
is insufficient: return the derivation, partial result, or precise obstruction.
Do not conclude FORMALIZE mode from source text
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

## Assess contribution before reporting novelty

Read [contribution assessment](reference/contribution-assessment.md) before
describing any result as new or original. Separate the known method, the present
application, the additional reasoning, and the significance. A straightforward
application to another parameter set is not a new attack mechanism. Keep that
distinction consistent in the headline and the detailed finding.

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
