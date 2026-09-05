# Develop the mathematics without restarting the background work

Use this guidance for a stated mathematical question. The task may concern a
known theorem, an unfinished proof, or a conjecture. It is not an attack-selection
or execution procedure.

## Separate the question from its background

Identify what the supplied material already establishes and the inference still
missing. Use the host-provided context and exact source statements. If their
provenance or scope is inadequate, qualify the dependency or inspect the relevant
source; do not silently promote recall into an established premise.

The purpose of an initial check is to make the current mathematical question
well-defined. It is not to exhaust every neighboring topic. A standalone lemma
does not require a survey of an entire cryptographic family.

For an established ingredient, distinguish **using the theorem**, **checking that
its hypotheses hold here**, and **independently re-proving the theorem**. Using it
usually requires the second, not the third. A supplied proof or inspected exact
statement can remain an ingredient across subsequent derivation steps.

Repeat a check when there is a specific reason: changed assumptions or inputs,
a different source revision, conflicting evidence, a suspected error, or an
explicit reproduction/validation objective. State which uncertainty the repeated
work will resolve. “I should be more rigorous” alone does not identify one.

## Generate alternatives that change the reasoning

When one approach stalls, reconsider the representation or intermediate claim.
Useful mathematical moves include:

- Express the same object intrinsically and in coordinates; identify which
  assumptions each representation makes visible or hides.
- Compare constructive existence, a necessary-condition argument, and a
  contradiction proof. These answer different intermediate questions.
- Separate an exact identity from an inequality, or a universal statement from
  a statement under an additional assumption. Do not blur the resulting scopes.
- Study a limiting or degenerate case to expose a missing hypothesis, then ask
  whether its lesson has a general derivation. Examples alone do not generalize.
- Relate two formulations through an explicit map. An analogy is useful only
  when the objects, operations, and required properties can be compared.

Use moves that fit the question; do not mechanically enumerate this list. When
asked to rank approaches, explain the unresolved obligation each addresses,
its dependencies, and what mathematical progress would distinguish it from the
others. Do not invent numerical success probabilities or a fixed number of paths.

## Carry an argument past the sketch

After selecting an approach, perform the next substantive inference. Introduce
the notation, derive the identity, prove the lemma, construct the object, or
identify exactly why the proposed step fails. A plausible outline is not the
requested mathematical development.

For a difficult argument, work toward an intermediate result that can stand on
its own: a conditional implication, a reduction to a precise lemma, a bound with
its assumptions, or a counterexample to an auxiliary statement. Derive its scope
explicitly. Do not abandon useful mathematics merely because the overall theorem
will take longer than the remaining turn.

Longer work is justified by progress in the reasoning: fewer unresolved
obligations, a stronger justified intermediate result, a more informative
representation, or a precise obstruction. Rephrasing the same sketch, regenerating
the same list, and repeatedly checking an unchanged known ingredient are not
progress. When reasoning stalls, change the approach or report the obstruction;
do not disguise the stall as another literature survey.

Do not confuse the absence of an immediate counterexample with proof, or the
absence of an immediate proof with refutation. Keep conditional arguments useful
by tracking their premises in the explanation, using the host's existing context.

## Spend checking effort where it changes the conclusion

During development, check types, quantifiers, assumptions, and algebra at the
steps where they matter. A separate independent review belongs to a clearly
stated result or load-bearing inference. It need not interrupt every tentative
line of working mathematics. Keep tentative material labeled until checked.

If a tool call is needed, name the uncertainty it addresses and what its output
can establish. Prefer a direct derivation when it settles the claim. Prefer a
calculation when the premise is empirical or exact finite checking is the useful
route. Do not require both routes automatically.

At handoff, explain what mathematics was added, which known ingredients were
reused, and which new obligations were checked or remain open. No new workspace
record format, checkpoint service, or resource scheduler is needed.
