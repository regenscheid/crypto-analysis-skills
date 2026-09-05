---
name: discover-cryptanalysis
description: Develop mathematical cryptanalysis questions, research proposals, and scoped results about specified cryptographic constructions, assumptions, or parameters. Use for human-directed standards research, unexplored mathematical questions, proposed extensions of known results, or continued development of a selected question. Distinguish a requested proposal from a request to carry out the mathematical work.
---

# Develop mathematical cryptanalysis

Start with `MODE: DISCOVER` and identify the requested product: a research
proposal, development of a selected mathematical question, or a scoped assessment
supported by that mathematics. Read
[the research workflow](../investigate/reference/mathematical-research-workflow.md).
It governs agenda breadth, research maturity, checking effort, and completion.

## Fix the mathematical question and scope

State the construction or mathematical object, version, parameters, distributions,
security definition, and assumptions relevant to the question. Identify the
conclusion sought and the contribution it would make to understanding the proposed
standard. Preserve distinctions among an underlying problem, a component result,
a construction-level claim, and a parameter evaluation.

Use the relevant domain orchestrator for definitions and references. A proposal
or supporting lemma does not require a completed full-family assessment. If the
assignment includes such an assessment, state and satisfy that separate scope.
Use the user's specified objects and existing host context.

## Relate the question to known mathematics

Identify the closest known ingredients and the unresolved inference. Use the
catalog and primary literature for examples, definitions, and the limits of prior
results. Follow [catalog use](../investigate/reference/catalog-use.md) and
[paper use and verification](../investigate/reference/paper-use-and-verification.md).
An adequately sourced result can be used without independently auditing its paper.
Check its hypotheses here and keep any uncertainty in dependent conclusions.

Do not let familiar technique names determine the only questions considered.
For a stated mathematical object, useful alternatives may concern its definition,
representation, distribution, invariants, supporting lemmas, or the scope of an
implication. An analogy motivates a question; an explicit mathematical argument
is needed for a result. Formal proof assistants remain an optional route.

## Build the requested research proposal

When a proposal is requested, retain the distinct questions warranted by the
scope. There is no fixed cap of five viable questions or two pursued questions.
Deduplicate equivalent formulations and routine parameter variants; do not pad
the agenda. Separate the broader agenda from work currently allocated to a
user-selected question.

For each question, give its mathematical formulation, significance, known
ingredients, unresolved assumptions, meaningful intermediate milestone, and
reasoned priority. Distinguish significance from readiness and research horizon
from modeled adversary cost. A long-horizon question need not have an immediate
cheap experiment to be worth proposing. Do not invent numerical probabilities of
novelty or success.

A proposal is complete when the requested questions and their rationale are
reviewable. It need not present an unproved idea as a viable attack or pretend
that all prerequisites are already established.

## Develop the selected question

When mathematical work is requested, use `mathematical-research-development` and
perform the inference beyond the outline. Develop a definition, lemma, derivation,
conditional implication, or counterexample that advances the selected question.
A new shortlist is not a substitute for that work.

An unknown prerequisite can itself be the question. Preserve it as unknown and
carry it through conditional results. Use a direct check when it resolves a
specific uncertainty; do not require a cheap falsifier before any deeper reasoning
can begin. Sometimes the useful next product is the formulation that makes a
later test meaningful.

When an approach stalls, identify the exact obstruction before changing the
representation or intermediate claim. Failure of that approach does not refute
the question. Continue from supplied partial mathematics without repeating the
original survey unless assumptions, evidence, or scope changed.

## Check the conclusion that is actually claimed

Use [evidence interpretation](../investigate/reference/evidence-interpretation.md).
State whether a conclusion is conditional, empirical, exactly checked, or proved.
A quantitative cost claim needs its appropriate model, units, success event, and
relevant resource accounting; an unpriced mathematical lemma can remain useful.

Use `verify-claim` when the correctness of a specified paper claim is the assigned
question. Independently check a new mathematical argument when presenting it as
an established result; review the fixed argument and report a gap without silently
repairing it. Reproduction is appropriate for an empirical claim that depends on
it, not a universal prerequisite to research proposals or theoretical results.

## Report progress and contribution

For delegated cryptanalytic work, including research proposals and scoped
assessments, apply
[orchestrator review](../investigate/reference/delegated-cryptanalysis-review.md)
to omissions, premature stopping, connections, and overlooked significance.
A correctness review alone does not establish the depth of the research.

Return the formulation, known ingredients reused, mathematics produced, scope,
remaining obligations, and why the next inference matters. Distinguish the end
of this work episode from resolution of the overall research question. Use the
host's existing context and artifact facilities; this skill defines no project
knowledge store or job manager.

Before originality language, read
[contribution assessment](../investigate/reference/contribution-assessment.md).
Identify the additional reasoning beyond the closest known result. A routine
application at another parameter set can matter to standards evaluation without
being a new method. Catalog absence, independent rediscovery, or changed notation
does not establish novelty.

Do not force a positive result. A justified obstruction, corrected assumption,
conditional characterization, or more precise research question can be substantive
progress. State the original question and what this episode actually resolved.
