---
name: mathematical-research-development
description: Develop an explicitly stated mathematical question into definitions, lemmas, derivations, counterexamples, or scoped partial results. Use when the requested work is ordinary mathematical reasoning, a proof gap, or a conditional argument that cannot be settled by retrieving a known answer. Formal proof assistants are optional.
---

# Develop a mathematical argument

Take one stated mathematical question. Work on its unresolved reasoning and
return the mathematics produced, including useful partial results.

## Make the question precise

State the objects, domains, quantifiers, assumptions, desired conclusion, and
what would constitute a counterexample. Distinguish a theorem sought from a
numerical observation or an interpretation of an existing source.

Use supplied context and cite known ingredients. Recheck an established fact
when its statement, assumptions, version, or reliability matters to the current
inference. Do not restart a broad literature survey merely because work resumes.
Read a load-bearing source before treating its exact statement as established.

## Develop the unresolved part

Separate a difficult assertion into explicit mathematical obligations. For each
step, write the inference and the assumptions it consumes. A conditional lemma
can be useful while one premise remains open; carry that premise into every
dependent conclusion.

Choose a representation that makes the argument inspectable: definitions and
equations, a dependency diagram, a finite example, or a proof with named lemmas.
If a calculation is needed, state which mathematical uncertainty it addresses.
Do not treat more citations, a longer plan, or repeated arithmetic as a substitute
for the missing inference.

Distinguish these outcomes:

- **Established step:** the stated argument or exact check supports its scope.
- **Conditional step:** the implication is justified, but a premise remains open.
- **Conjecture:** a proposed statement whose proof is incomplete.
- **Refuted statement:** a valid counterexample or contradiction defeats it.
- **Unresolved question:** available work has not decided it.

Failure to prove a statement does not refute it. Failure of one proof strategy
does not refute the statement either. Explain what each failed argument actually
rules out.

## Check the claim at the right strength

Read [evidence interpretation](../investigate/reference/evidence-interpretation.md)
when deciding what a derivation or computation establishes. Review quantifiers,
boundary cases, hidden assumptions, and dependence between lemmas. Separate
development from independent checking when the conclusion warrants it. A formal
proof assistant is one assurance option, not a requirement for doing mathematics.

## Return useful partial work

Give the current statement, derivation or counterexample, scope, remaining
obligation, and why that obligation matters. If time ends, return the mathematical
progress already made; do not relabel an unfinished proof as a failed conjecture.

The host supplies investigation context and project knowledge. This skill does
not define storage, checkpoints, background execution, or a new persistence
format. It does not select targets or execute exploitation workflows. Physical
security is outside this skill's scope.
