# What the offline checks establish

`score_routing_response.py` checks report format and expected names. Its legacy
`passed` field means only that those smoke checks (and supplied trace checks)
passed. It does not measure mathematical progress, correctness, novelty, coverage,
or whether cited evidence supports a conclusion. `research_progress` is always
`not_assessed`; compare actual mathematical outputs in a separate review.

`check_cscience_probe.py` checks exact body-content adherence. A correct marker
does not by itself prove that a host invoked a skill.

Both tools accept `--trace` as the following **offline normalized JSON**, prepared
from the existing harness trace. No harness instrumentation or API change is
required. Preserve the original trace and map only observed successful skill-body
loads. The normalization must never infer a load from a response, a skill name in
a prompt, an available tool definition, or a failed call.

```json
{
  "schema_version": 1,
  "source_trace": "captured-run.jsonl",
  "events": [
    {
      "kind": "skill_load",
      "skill_id": "cscience-skill-probe",
      "status": "succeeded",
      "call_id": "original-call-id",
      "body_sha256": "REPLACE_WITH_64_LOWERCASE_HEX_DIGITS_FROM_THE_RETURNED_BODY"
    }
  ]
}
```

Hash the UTF-8 body actually returned, not the description or a local file that
was never loaded. This document records trace evidence; the checker does not
authenticate the original trace or prove that the loaded guidance was followed.
Missing trace evidence stays unassessed. Malformed or name-only traces fail when
supplied; failed calls cannot count as successful loads.

Useful manual evaluation questions for ordinary mathematical work:

- Did the response produce a definition, inference, lemma, counterexample, or
  useful partial result beyond the supplied material?
- Are open premises visible in every dependent conclusion?
- Did a repeated known-result check address a concrete uncertainty?
- Does the evidence distinguish a finite fact from an empirical observation?
- Can the reviewer identify the remaining mathematical obligation from the output?

Use supplied context for continuation evaluations; project-memory mechanisms and
long-running job management belong to the harness, outside these tests.

## Mathematical development and contribution cases

`mathematical-research-cases.json` contains thirteen manual evaluation cases with
supplied premises and review criteria. They cover routine parameter substitution,
important applications of known methods, invalidated hypotheses, reuse of
established mathematics, sustained block-matrix derivation, and conditional work.
They do not execute cryptanalytic attacks or change the harness.

For a behavioral trial, give the model the prompt and relevant skills, keeping
the review criteria separate until assessment. Inspect the actual reasoning,
source use, and output. Compare the same prompt and supplied context before and
after the skill change; record the model configuration and available resources.
Do not count a case as passed because expected words appeared. These cases have
not been run through Claude Science merely by being checked into the repository.


## Comparison protocol

Compare the original skills, the original skills plus the user's ranked-question
prompt, and the revised skills on the same supplied mathematical questions. Keep
model version, sampling settings, available tools, input context, and resource
limits matched. Use more than one run before attributing a difference to wording.
These are evaluations of the existing host, not changes to its execution API.

Review the actual products and, where available, traces. Distinguish source
interpretation from paper verification, and count repeated checking as justified
only when it addresses a changed dependency or the assigned verification task.
Assess mathematical progress by the inference produced, its correctness and
scope, and the unresolved obligations it exposes. Report time or resource use
by activity only when the trace supports that measurement. Do not optimize for
claimed novelty, number of proposed questions, or the absence of negative results.

The added cases cover a false paper claim, use of an established theorem,
post-selection inference, a zero-event confidence limit, a nine-question proposal,
continuation from a partial derivation, and scoped negative results. Their
presence and reference answers do not constitute a live model evaluation.
