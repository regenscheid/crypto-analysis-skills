# Open-brief inventor frame

Use one or two inventor frames in a sustained DISCOVER pass when the current
open ideas share the same lens or leave a structural gap. The inventor searches
for an object, representation, relation, or invariant not yet tracked. It is
not assigned one existing attack technique or a request to rephrase the
current ideas.

## Input from the orchestrator

Give the frame the exact target and assumptions, confirmed lemmas with their
hypotheses, published SOTA rows, and critic-accepted closed lanes. Exclude the
closed-lane families as its primary lens; a closed lane is scoped to its
recorded assumptions, not a ban on all related mathematics. Give it the
absolute project directory and a session idea ID for its own notebook. First
append a full `idea` event for that inventor question, with a precise `title`
and `builds_on` IDs; the inventor's outcome then has a defined parent idea.
The inventor does not need every pending idea or the full board log.

## Work to do

Inspect objects native to the target before importing a familiar technique.
Examples include its distribution, representation, algebraic structure,
group action, automorphisms, normal forms, relation to public information,
and changes under key or parameter transformations. Ask what invariant or
information channel those objects expose. For each object attempted, record
the exact obstruction or missing premise before switching objects. A lack
of time, tools, context, or a useful idea is a soft dismissal.

Return a small set of distinct, mathematically formulated candidate ideas
with the confirmed lemma IDs they build on, their assumptions, and the
next inference that would test them. A candidate can be a definition,
lemma, conditional implication, or counterexample, not just a complete
attack. Use the standard structured outcome fields from the
[Claude Science adapter](claude-science.md#7-delegate-plan-tracks); include
`child_ideas` with a globally unique `idea_id`, proposed `title`, and
`builds_on` IDs when the open brief splits into focused ideas. Match those
IDs in `child_idea_ids` for a `split` outcome. The orchestrator appends the
raw return before triage. After the critic accepts a split, the orchestrator
appends full `idea` events for the accepted children before delegating them;
the split reducer's open placeholders alone contain no research question.

“Most-studied target” is not an obstruction. Keep the user's target fixed;
retargeting requires user approval.
