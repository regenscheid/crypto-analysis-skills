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
