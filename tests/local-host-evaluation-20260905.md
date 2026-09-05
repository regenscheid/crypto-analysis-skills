# Local host evaluation status — 2026-09-05

No behavioral comparison was executed in this local follow-up. The fourteen
original cases remain unevaluated through Claude Science in this task, as do the
three supplemental delegated-mathematics cases. No improvement in correctness,
depth, continuation, checking effort, or contribution labeling is claimed.

The local `cscience --help` invocation exited with a module-not-found error for
its installed `runtime/claude-science.js`. The `claude-science --help` command
succeeded and exposes a browser-host interface, with no documented batch prompt
command. `claude-science status` reported a running release host at version
0.1.43 on port 8765, with an active conversation.

Opening that local host through the available browser tool was denied because
the admin-enforced browser policy could not be verified. The tool explicitly
prohibited bypassing the control or using an indirect workaround. No model
generation was submitted. The existing daemon, harness, installed skills,
settings, and active conversation were left unchanged.

The user authorized a representative reconstructed ranked-research prompt, now
recorded in `reconstructed-ranked-research-prompt.json`; historical prompt
recovery is not a blocker. The matched protocol is in `evaluation-contract.md`.
Its conditions still require accessible host execution, verified skill loading,
matched resources, and repeated runs before behavioral findings can be reported.

Local structural audits and evaluator unit regressions validate repository
consistency and trace handling only. They do not substitute for this comparison.
Canonical bibliography generation and a full passage-support audit remain
unfinished. This follow-up corrected reference interpretation and review scope;
it did not independently verify every bibliographic record or source passage.
