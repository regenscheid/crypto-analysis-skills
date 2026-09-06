# Exploratory and confirmatory evidence

Use the statistical work required by the claim. An exploratory observation can
be useful before it supports an inference about a population. Formal verification
is optional and does not replace a suitable sampling model.

## Define the population and observation

State the unit sampled, its distribution, the statistic, exclusions, and the
conclusion sought. Multiple measurements of one object need not be independent
samples of the population of objects. Shared randomness, conditioning, filtering,
and censoring can change the relevant distribution and effective information.

Preserve the actual observation before interpreting it. “Zero events in these
trials,” “no solution returned before timeout,” and “a universal obstruction was
proved” are different results. A low-powered comparison may be inconclusive even
when the underlying effect is important.

## Exploration is allowed to change the question

During a pilot, inspect patterns, diagnose an implementation, and refine the
statistic or formulation. Record selections that affect interpretation: which
outcomes, parameter values, subgroups, or transformations were examined and why
the reported observation was selected. Do not present that choice as fixed in
advance or interpret the selected p-value as if no selection occurred.

A surprising observation can motivate a mathematical question without immediate
confirmation. Report it as exploratory and explain what it suggests and what
it does not establish. Absence of confirmation does not erase the observation.

## Confirmation answers a fixed question

Before collecting confirmatory evidence, state the target effect or estimand,
sampling process, comparison, uncertainty method, and stopping rule. Use fresh
data that did not drive selection when feasible. If data are reused, account for
selection with a justified method or retain an exploratory conclusion. Repeated
looks and optional stopping require a compatible sequential method; ordinary
fixed-sample inference does not become sequentially valid by reporting the final
sample size. Reusing a seed is not independent replication.

Report effect size and uncertainty, including null results and exclusions.
Statistical significance does not measure effect size, importance, or the
probability that a hypothesis is true. See the ASA's
[six principles](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf), p. 2.

## Zero-event example and its exact limits

For a fixed sample of n independent Bernoulli trials with common event probability
p, zero observed events has probability (1-p)^n. Inverting that probability gives
the one-sided exact upper confidence limit p_U = 1 - alpha^(1/n), at confidence
level 1-alpha. It is an upper limit, not a measured event rate or a posterior
probability for p. This short derivation is the source of the formula here.

At n=100 and alpha=0.05, p_U is about 0.02951. Zero observations do not establish
p=0 or exclude a probability of one in a thousand. Dependence, selection, changing
p, or optional stopping can invalidate this calculation's assumptions. Distinguish
one-sided from two-sided intervals; the latter divide the error budget between
tails. NIST's [binomial confidence-interval discussion](https://itl.nist.gov/div898/handbook/prc/section2/prc241.htm)
provides the corresponding finite-binomial inversion and small-count cautions.

## Correspondence and negative conclusions

A toy model establishes facts about that model. State the map to the intended
setting and which assumptions, distributions, or dependencies it preserves.
Empirical scaling alone is not proof of an asymptotic law. Use existing modeling
references when that correspondence is the disputed step.

Scope a negative result to the attempt and its assumptions. A repaired tool,
changed model, stronger method, or new source may justify reconsideration; a
new session alone does not. Use the host's existing context for these facts.
The output should expose uncertainty, not create another project record system.
