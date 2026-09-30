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

## Project/session research-board metrics

`python tools/trace_evidence.py --board-metrics normalized.json` reports one
Claude Science root session in one project. `board_metrics(path)` returns the
same JSON object for Python callers. This is an **offline normalized event
contract**, not a Claude Science API and not proof that the original capture is
authentic. Preserve the original trace, host-call tapes, and board ledgers.

The top-level `project_id` and `session_id` are the project's ID and the root
frame ID from `host.artifacts()["provenance"]`. `project_dir` is the absolute
`<CRYPTO_FILES>/projects/<project_id>` path. `capture_complete` has four
boolean channels: `board_reads`, `board_appends`, `delegations`, and
`delegation_returns`. Mark a channel `true` only after covering the entire
session. A missing or partial channel makes dependent metrics `null` and adds
their names to `unverified`; observed counts remain under `observed`. Do not
turn a failed search or inaccessible trace into a zero.

The following shortened example shows the event shapes. The root assigns a
unique `delegation_id` to **each child** before dispatch. A host `delegate`
call also has its own `host_call_id`; one batched host call can spawn several
children, each with a different `delegation_id` and `child_frame_id`. Events
are in observed execution order.

```json
{
  "schema_version": 1,
  "source_trace": "captured-run-with-host-call-tapes",
  "project_id": "proj_example",
  "session_id": "root-frame-id",
  "project_dir": "/absolute/crypto-workbench-files/projects/proj_example",
  "capture_complete": {
    "board_reads": true,
    "board_appends": true,
    "delegations": true,
    "delegation_returns": true
  },
  "events": [
    {
      "kind": "board_read",
      "call_id": "read-cell-1:0",
      "status": "succeeded",
      "project_dir": "/absolute/crypto-workbench-files/projects/proj_example",
      "scope": "project",
      "snapshot": {
        "open_idea_ids": ["idea-a"],
        "requeue_idea_ids": ["idea-a"],
        "soft_dismissals": [
          {"event_id": "prior-dismissal-id", "dismissal_index": 0, "idea_id": "idea-a", "reason_class": "lacked_tools"}
        ],
        "promoted_lemma_ids": ["lemma-prior"]
      }
    },
    {
      "kind": "delegation",
      "delegation_id": "assigned-child-1",
      "host_call_id": "host-call-7",
      "child_frame_id": "child-frame-id",
      "idea_id": "idea-a",
      "board_read_call_id": "read-cell-1:0",
      "expects_board_outcome": true,
      "context_summary": "Read /absolute/crypto-workbench-files/projects/proj_example/board."
    },
    {
      "kind": "delegation_return",
      "delegation_id": "assigned-child-1",
      "child_frame_id": "child-frame-id",
      "status": "completed",
      "structured_output": {
        "delegation_id": "assigned-child-1", "idea_id": "idea-a", "state": "open", "findings": [],
        "dismissals": [], "lemma_proposals": [], "notebook_append": ""
      }
    },
    {
      "kind": "board_append",
      "call_id": "append-cell-9:0",
      "event_id": "board-event-id",
      "session_id": "root-frame-id",
      "ledger_path": "/absolute/crypto-workbench-files/projects/proj_example/board/sessions/root-frame-id.jsonl",
      "event_type": "outcome",
      "payload": {
        "delegation_id": "assigned-child-1", "idea_id": "idea-a", "state": "open", "findings": [],
        "dismissals": [], "lemma_proposals": [], "notebook_append": ""
      },
      "capture_source": "delegation_return",
      "delegation_id": "assigned-child-1",
      "child_frame_id": "child-frame-id"
    }
  ]
}
```

Normalize a `board_read` only from an observed completed `board_snapshot`
call and its returned snapshot. Record the absolute `project_dir` argument and
`scope: "project"` when `session_id=None` was passed; a session-filtered read
uses `scope: "session"` and cannot prove project-wide carry or re-derivation.
A failed read has `status: "failed"` and no snapshot. Copy the snapshot's
`open_ideas[*].idea_id`, `requeue_idea_ids`,
`soft_dismissals[*].event_id`, `soft_dismissals[*].idea_id`,
`soft_dismissals[*].dismissal.reason_class`, and `lemmas[*].lemma.lemma_id` into
the normalized fields shown above. Add `dismissal_index` as the zero-based
position in the source outcome's `dismissals` array; use `0` for a standalone
`dismissal` event. Resolve each snapshot `event_id` against the project
ledgers to recover this index. The `(event_id, dismissal_index)` pair is
unique even when one outcome produced several soft dismissals. A name in a
prompt or report is not a read.

Normalize `board_append` from an actual line in
`<project_dir>/board/sessions/<session_id>.jsonl`: `event_id`, `session_id`,
`type` as `event_type`, and the verbatim `payload`. Add the absolute
`ledger_path` and a trace `call_id` for the successful append call (use a cell
ID plus ordinal when one cell appends more than once). The helper can store
`provenance` **outside** the verbatim payload for outcomes. When the ledger
contains its `delegation_id` and `child_frame_id`, copy those to the normalized
event and set `capture_source: "delegation_return"`. If provenance cannot be
established, set `capture_source: "unknown"`; use `"manual"` only when the
trace explicitly shows a manual outcome. An unknown outcome origin makes the
negative return-to-append metric unverified.

For CScience captures, `host_call_log` in `~/.cscience/operon-cli.db` records
`method`, `args_json`, `data_inline`, and `data_ref`, linked to an
`execution_log` cell by `execution_log_id`. Large responses live in the
project's `host_call_tapes` under its artifact store. Normalize each spawned
child from a `delegate` call's arguments and returned `frame_id`. Set
`expects_board_outcome` from the actual `output_schema` in the delegation
request; it is `true` only for the standard board fragment (`delegation_id`,
`idea_id`, `state`, `findings`, `dismissals`, `lemma_proposals`,
`notebook_append`, and `child_idea_ids` when `state="split"`). Use the root
assigned, per-child `delegation_id` from the request and returned structured
output. Preserve `host_call_log.id` separately as `host_call_id` when useful;
it can be shared by several children in one batched call. A normalized
`delegation_id` must equal `structured_output.delegation_id` and the persisted
outcome payload and provenance IDs. The persisted `child_frame_id` must equal
the returned child frame ID. The root's delegated `idea_id` must agree with the
returned and persisted outcome's `idea_id` when the trace binds a child to an
idea. Valid outcomes require all board fields; a dismissal requires nonempty
`attempted` text, and a split outcome requires distinct `child_idea_ids`.
Normalize a **terminal** `delegation_return` from a blocking `delegate` result
or later `collect` result. `delegate(wait=False)` running descriptors are not
terminal returns. `collect` results have the same `frame_id` and may include
`structured_output`, `deviations`, and artifact IDs. Carry the actual
`context_summary` field, including `null` when omitted. Set `idea_id` and
`board_read_call_id` on a delegation only when the trace explicitly binds that
child to the idea and preceding read; otherwise the idea classification is
unverified. Do not extract either from free-form praise or a final report.

The report counts idea dispatches by distinct `(board_read_call_id, idea_id)`
pairs. Snapshot `requeue_idea_ids` takes precedence over ordinary carried open
ideas; a new idea requires a persisted `idea` event between the read and
delegation. `soft_dismissals_requeued` counts distinct
`(event_id, dismissal_index)` pairs
for ideas actually requeued. `rederivations_of_existing_lemmas` counts derived
lemma proposals whose `restates` IDs match promoted lemma IDs in the preceding
snapshot. This is a trace-observable restatement, not an independent judgment
of mathematical equivalence. A delegation satisfies the board-path check only
when `context_summary` contains the absolute `<project_dir>/board` path or a
descendant path. A return is counted as appended only when the persisted
`outcome` has the same delegation ID, child frame ID, and **exact structured
output payload**, and its append follows the terminal return in trace order.
A modified payload appears among unappended returns and in
`modified_return_child_frame_ids`. A completed child expected to return the
board fragment but missing those structured fields also counts as unappended;
`unsatisfied_board_return_child_frame_ids` identifies it separately.

Useful manual evaluation questions for ordinary mathematical work:

- Did the response produce a definition, inference, lemma, counterexample, or
  useful partial result beyond the supplied material?
- Are open premises visible in every dependent conclusion?
- Did a repeated known-result check address a concrete uncertainty?
- Does the evidence distinguish a finite fact from an empirical observation?
- Can the reviewer identify the remaining mathematical obligation from the output?

Use supplied context for continuation evaluations. These trace metrics measure
record handling, not whether the research claims are correct or novel.

## HAWK board validation protocol

For the proposed HAWK τ-cocycle rediscovery trial, freeze and hash a corpus
containing only pre-July-2026 versions of the HAWK specification, GP25, Duc23,
BN24, and NIST IR 8610, plus the exact reference implementation used to
generate a fresh HAWK-256 challenge. Keep the challenge's secret material and
all later attack disclosures outside both agent sessions. Disable live web and
literature retrieval for the trial; verify the available corpus and skill list
inside each fresh session before work starts. A frozen corpus alone cannot rule
out knowledge already present in the selected model, so record its identity and
training cutoff where available.

Run matched, isolated CScience sessions with the same model, prompt, frozen
inputs, compute profile, network access, and operational resource cap. The
skills arm uses the revised crypto skills; the comparison arm has an explicit
empty skill list while retaining the same host adapter and compute access.
Do not remove skills from a live shared installation to create the comparison.
Keep any new HAWK attack-catalog record out of both arms. Verify required
Sage/lattice dependencies and hidden-challenge generation before either arm;
do not infer readiness from a provider manifest alone.

The research board's scientific stopping rule remains idea state: continue
until no open ideas remain or the user stops. An external wall-clock/model-call
cap may end an experimental run for operational reasons; report that as a
censored run with its remaining open ideas, not as a solved or obstructed
campaign. Save source hashes, model and tool settings, original host traces,
board ledgers, normalized events, and the metrics above. Verify any returned
equivalent signing key against the hidden challenge outside the agent. Compare
the actual mathematics as well as the trace metrics. Consider a maintainer
authored fork hook only for a specific drift seen in these traces. This
protocol is not itself a completed validation run.

## Mathematical development and contribution cases

`mathematical-research-cases.json` contains fourteen manual evaluation cases with
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

The elementary-corollary case checks whether a newly named rank inequality is
recognized as a direct consequence of supplied standard facts. The expected
assessment concerns the displayed reasoning, not another literature survey.

Use `reconstructed-ranked-research-prompt.json` for the middle condition. Its
wording is a reconstructed representative prompt authorized by the user, not an
exact historical prompt. The original-skills baseline is commit `098013c`, the
parent of this PR's first commit. Record the full resolved commit IDs and skill
body hashes for every executed condition; do not use an evolving branch name as
the only version identifier.

Use fresh, isolated conversations with identical supplied context, tool access,
model versions, effort, and resource limits. Keep review criteria and prior
condition outputs out of generation context. Verify which skill bodies actually
loaded; merely attaching revised files does not establish that the host used
them. Counterbalance condition order and run at least two repetitions per case
and condition before describing a repeated pattern. Report run-level outcomes,
disagreements, and execution failures; two repetitions alone do not establish
statistical significance or general improvement.

`delegated-cryptanalysis-cases.json` adds three supplemental handoffs covering
an important routine finding undervalued by its author, an unnoticed connection
between accurately reviewed reports, and premature closure after a correct but
narrow examination. A dedicated correctness reviewer has already checked the
supplied findings. Assess what research judgment the orchestrator adds: omitted
implications, meaningful connections, and justified treatment of open questions.
Repeating the supplied correctness checks does not satisfy this objective.
These bounded fixtures do not measure open-ended cryptanalytic creativity.

`delegated-mathematics-cases.json` supplies three further cases with fixed
synthetic subagent handoffs. Review whether the main agent catches a false proof,
continues past an unjustified dismissal, and corrects inflated novelty. These
and the broader cryptanalysis cases isolate the main agent's response to supplied
work; they do not measure real delegation or differences between model
capabilities. A live delegation trial
must also record the primary and child model/effort settings actually used,
subtask prompts, returned artifacts, and what the primary agent checked or added.
Do not infer those settings from UI labels or role names.
