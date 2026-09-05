# Orchestrator review of delegated mathematics

The main agent remains responsible for the mathematical conclusions it adopts
and for whether the requested work was developed far enough. A subagent's fluent
summary, confidence, or completion status does not establish either. This matters
especially when the host gives the orchestrator a more capable model or more
context; do not assume model settings or capabilities from the agent's role.

## Review correctness before adopting a conclusion

Inspect the actual statement and argument, relevant computations, assumptions,
and unresolved obligations, not just the subagent's summary. Check the new,
load-bearing inferences and how they compose with the rest of the work. Confirm
that quantifiers, domains, conditional premises, and evidence scope survive
synthesis. A missing artifact leaves the corresponding review incomplete.

Reuse compatible checked ingredients under [paper use](paper-use-and-verification.md).
Reviewing a new deduction does not require re-proving every theorem it uses.
Focus fresh checking on the inference, changed dependency, or concrete suspected
error. Preserve explicit assignments to verify a paper or reproduce a result.

Judge the submitted argument before repairing it. Record a gap in that version;
if development continues, distinguish the revised argument and check its changed
steps. A main-agent review is not automatically an independent verification:
name the actual checking route and its scope under
[evidence interpretation](evidence-interpretation.md).

## Review depth separately from correctness

A correct response may still stop at an outline or settle only an easy special
case. Compare the mathematical product with the user's requested question and
the supplied partial work. Identify the precise obligation still missing.

Before adopting a consequential dismissal, examine its reason. Failure of one
argument, limited subagent effort, an unknown premise, or an unavailable tool
does not prove that the question has no useful continuation. For the selected
mathematical question, consider whether a different representation, intermediate
lemma, or conditional formulation changes the unresolved inference. Develop a
justified next step when the assignment and resources call for it; do not merely
ask for a longer list or a more confident restatement.

This is a proportionate review at synthesis or a meaningful mathematical
boundary, not a duplicate investigation after every subtask. Direct attention
to consequential conclusions, unexplained exclusions, and incomplete reasoning.
Do not claim exhaustive coverage of possible ideas or guaranteed originality.

## Own the final contribution assessment

Apply [contribution assessment](contribution-assessment.md) to the actual
deduction even when the subagent labels it a new theorem. Identify known
ingredients, their deduction, and any substantive additional step. If there is
none, label it a routine derivation or elementary corollary without requiring an
exhaustive literature survey. Preserve its practical significance separately.

Report what the orchestrator checked, what mathematics it added or corrected,
and what remains unreviewed or unresolved. Use existing host artifacts and
resource controls; this guidance creates no new review service or storage system.
