# Assess contribution without overstating novelty

Read this before describing a result as new, original, an improvement, a new
attack, or a research contribution. Correctness, originality, and significance
are separate judgments. A correct and important observation can be routine; an
original idea can be wrong or insignificant.

## Identify what changed relative to the closest known result

For a material result, give the closest known method or theorem, the present
target and scope, the changed parameter or assumption, and the additional
reasoning actually supplied. Cite the source at the strength inspected. Describe
the difference before assigning a contribution label.

| Relationship to prior work | Appropriate description |
|---|---|
| Same result independently derived or rerun | Reproduction or independent rediscovery |
| Existing result directly covers the case after substitution or checking its stated hypotheses | Routine application or parameter instantiation of the known result |
| New measurement or numerical evaluation using an unchanged method | New evaluation of a known method; identify the measurement or parameter coverage added |
| Known result used outside its established assumptions, with the missing justification still open | Proposed extension with an unresolved obligation |
| A change requires and receives a new substantive argument, construction, or justified bound | Substantive extension; name the additional contribution and qualify its novelty |
| A distinct mechanism, theorem, or proof technique is supplied | Potentially new method or result, subject to correctness and prior-art assessment |

These descriptions are not an automatic publication-worthiness score. A new
evaluation can be a valuable contribution, and a short proof can supply a deep
insight. Judge the actual difference, not its length or the amount of computation.

## Parameter changes are not themselves a new method

If a known attack on an algorithm applies to another parameter set by the same
argument, report an **application of the known attack to that parameter set**.
Credit the original method and state which hypotheses were checked. Do not call
it a novel attack or mechanism merely because the parameter combination was
absent from the paper, the catalog, or the current investigation.

Distinguish “not previously listed,” “not found in the sources searched,” and
“not previously known.” The first two do not establish the third. A result being
new to the agent or user is not evidence of scientific originality.

Conversely, do not assume every parameter change is routine. A changed parameter
can invalidate an assumption or require a new argument. Identify that obstacle
and the work that resolves it. Until then it is a proposed extension, not a proved
application or an established novel result.

An application may have important implications for a particular parameter set
or a previously stated claim. Describe that significance separately from the
originality of the underlying method. Do not suppress a useful finding because
it is not a new technique.

## Calibrate the originality statement

For an unchanged method, a precise source comparison can establish that the
work is an instantiation; no exhaustive priority search is needed to avoid a
novelty claim. Investigate publication history further when priority itself is
material to the user's question or to the contribution being claimed.

For a proposed contribution, identify exactly which part is believed to be new
and which ingredients are known. Report the scope and gaps of the relevant
prior-art search. Catalog absence, a failed search, or different notation does
not establish novelty. Use “potentially new; not found in the sources searched”
when that is the supported conclusion, not an unqualified priority claim.

Avoid attaching novelty to the whole result when only one component might be
original. Combining familiar steps is not automatically novel or automatically
routine: explain whether their combination resolves a previously open obstacle.

## Reporting examples

- “Using the method of [source], we evaluated parameter set P. The argument is
  unchanged. This parameter-specific evaluation was not found in the sources
  searched; we have not established that it was previously unknown.”
- “The published theorem requires assumption A. The proposed extension needs
  lemma L to remove A; L remains unproved, so this is an open extension.”
- “Lemma L supplies the additional argument beyond [source]. Its proof is
  [checked/unreviewed/conditional]; its originality remains [assessed within a
  stated search scope/unassessed].”

Apply the same classification in the headline, summary, detailed finding, and
conclusion. A caveat in an appendix cannot repair a headline claiming a “new
attack.” This is a reporting discipline, not a requirement for another catalog
schema, an automatic submission, or a project-knowledge store.
