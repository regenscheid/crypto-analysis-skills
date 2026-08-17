# What this environment does and does not permit

> Part of `investigate`. **These are properties of Claude Science, not of this
> workbench.** Runtime behavior can change between releases, so re-run the
> behavioral probes when the CScience pin changes. Several entries were measured
> only after a wrong assumption had already cost a day.

Read this when something fails in a way that looks like a bug in your code. Most
of the entries below were first diagnosed as the wrong problem entirely.

## Reading a failure correctly

The single highest-value table here. Three failures look alike in a traceback and
have nothing to do with each other.

| symptom | what it means | what fixes it |
|---|---|---|
| `HTTP 000`, or `Tunnel connection failed: 403` | the **proxy refused CONNECT** — the request never reached the host | a network-access grant requested by the active root or child that needs it |
| a plain `HTTPError 403` / `404` | the request **did reach the host**, which refused it | usually your request, not a grant — see the user-agent note below |
| `Operation not permitted` | **filesystem**, not network | a path grant, or the wrong kernel (below) |

`HTTP 000` is not an HTTP status. It is curl reporting that no request completed.
**Do not ask for a network grant before establishing which of these you have.**
An older deployment once left a delegated request parked for 7.7 hours, but
current 0.1.27 probes show working child cards. Treat that incident as a reason
to test each runtime pin, not as a current parent-only rule.

**A plain 403 is often the user-agent.** Measured against a NIST host: a default
`Python-urllib/3.x` user-agent gets 403, no user-agent at all gets 200, a
browser-like one gets 200. The connectors in this repo already set a proper
user-agent. Hand-rolled `urllib` in a kernel cell does not — which is why the
rule is **fetch through the connector**, and only reach for raw HTTP when nothing
else can.

## Network: no direct egress, and no listening sockets

A connector's sandbox has **no direct network** — only a proxy — and the proxy
refuses some hosts by allowlist and port 22 to every host. SSH from a connector
is not a configuration problem; it is not permitted.

**Nothing here may bind a local port**, in either kernel or a connector. That
single fact rules out browser automation in-process: Selenium and chromedriver
need a local listening service. Measured: a browser and a version-matched driver
drive fine *outside* the sandbox and fail on the port bind inside it, in both
kernels and in a connector — so the blocker is the bind, not the browser, the
driver version, or file permissions.

Consequence: **anything needing a real browser runs outside the sandbox** and
communicates through a shared directory. That is structural, not a workaround.

> Untested and worth testing: **binding is not connecting.** Nothing has
> established whether an *outbound* connection to a port something else already
> listens on is refused. If it is allowed, a browser started outside and driven
> over CDP would collapse a lot of this. Do not assume either way.

## Two kernels, different powers

| | `repl` | `python` |
|---|---|---|
| `host.*` control plane | **yes** | no |
| can read a granted repo path | **no** — `PermissionError` | **yes** |

Neither can publish a skill alone. The route that works is: read and stage in
`python`, then publish from `repl` reading the staged copy. Getting this wrong
destroyed all eight published skills once — the reads failed in `repl`, and the
empty results were published over the real ones.

Note also that the kernel's own grant table is **separate** from the sandbox
grants in `config.toml`, and is usually empty. Two different grant systems with
similar names is a reliable source of wrong conclusions.

## `host.mcp()` flattens results

It returns a **string**, and discards binary content. A spec-correct MCP
`EmbeddedResource` comes back as a description of itself — measured, a 906,304
base64-character PDF arrived as the 157-character string
`[Embedded resource (application/pdf): …]`. The bytes never reach the caller.

So **MCP resources are not a delivery route to a model in this app**, however
correct they are. What works:

- **local server** — return a file path, and hold a host grant for it
- **remote server** — an HTTPS URI served by the *server's own* host. Not the
  origin's: returning a publisher's URL is useless if the client cannot fetch it,
  which is the whole reason a fetcher exists.
- **either, expensively** — base64 in `TextContent`, which survives flattening at
  about 1.37 characters of context per byte

*Correction worth keeping:* an earlier version of this concluded "remote means
text only." That was too strong — byte delivery from a remote host is expensive,
not impossible. The measurement was right; the conclusion drawn from it was not.
The error was stopping at the first mechanism that failed instead of asking what
else could carry the same payload.

## Root and child control surfaces are deliberately different

`generate_plan` is root-only. A child linked by an exact delegation-name match
receives only that track's Plan Steps and updates those exact titles itself. An
unmatched child is ad hoc and receives no plan context. The root must not claim
or duplicate a linked child's status updates.

A delegated child is a leaf: `host.delegate` is refused, `host.collect` is not
in its SDK, and `host.children()` is empty. It can message its direct parent with
`host.send_message("parent", ...)`, but it cannot message or stop a sibling.
Project-wide frame reads are broader than mutation topology, so seeing a frame
does not imply permission to control it. A mutation API's “not found” can mean
topologically unreachable rather than globally absent.

`host.capabilities()` reports the `host.*` SDK, not top-level tools such as
`ask_user` or `update_step_status`. Attribute introspection is also unreliable
for policy-gated methods. A child's Current Context has also advertised the root
frame id in measured runs; use `"parent"` or returned delegation descriptors for
routing and use a bounded probe for capability checks.

## Child human gates work, and parked messages fail closed

In the tested 0.1.27 runtime, a child can call `ask_user`,
`request_network_access`, or `request_host_access` directly. Two children can
hold `ask_user` cards concurrently; answers remain associated with their own
frames, both children resume, and collection preserves the association.

All three human-gated parks enter `awaiting_user_response`. If the parent calls
`host.send_message` while the child is parked, the receipt has `status: "failed"`
and an error naming `(ask)`, `(network)`, or `(host)`. The call does not raise,
deliver or queue the message, inject an answer, deny the request, or dismiss the
card. The correct parent behavior is `wait_for_notification()` followed by
collection after the user acts. Always inspect the receipt: `status: "injected"`
means the child resumed before the send and the parked-state race was missed.

The user verdict returns only through the child's original gated call. A direct
tool verdict is authoritative and a later contradictory parent message cannot
manufacture a grant. Host-path validation can fail synchronously before any card
appears. An `<error>` transcript heading marks a failed tool result; it is not
part of the returned JSON payload. A child may instead ask the parent for
reasoning before it opens a card; that is ordinary direct-parent messaging, not
a way to answer an existing gate. Exact call patterns are in
`claude-science.md`.

## The research tools are a REMOTE server, and that is why they work

These skills call one remote MCP server over HTTPS. That is not incidental —
Claude Science **requires a public HTTPS URL** for a remote connector and rejects
`http://localhost` on the scheme alone, before anything connects. A container
bound to loopback therefore cannot serve tools to it, however correct the
container is; a properly hosted one can.

Two consequences worth holding:

- **A tool that vanishes is a server-side event, not your bug.** If a name stops
  resolving, call `portal_list_servers` and read the live list. The names in
  `tools.md` were current when written and are expected to drift.
- **Nothing here shares a filesystem with you.** A remote server cannot hand back
  a local path, so file-shaped results arrive as URLs or as text. `host.mcp()`
  flattens tool results to a string and drops binary content (above), so text and
  URLs are the only things that survive the trip regardless.

## Artifacts are the project-scoped store, and every version is immutable

Measured, and most of it is not what the naming suggests:

- A new conversation can discover project artifacts through `host.artifacts()`;
  use its project, frame, filename, or search filters when scope matters.
  Conversation-scoping is a default, not a wall.
- The ids it returns are **version ids**, not artifact ids. Saving by a version id
  resolves to the parent artifact and appends a new version — verified across
  conversations.
- Saving by **filename** is what forks silently: the same name can end up as two
  separate artifacts.
- For a computed id, `host.artifact_marker(version_id)` returns the marker to put
  in a delegation brief; it expands in the child's workspace, and the child can
  read it with plain `open()`. A literal marker authored inside a parent `repl`
  cell can pre-resolve before the task string exists and is not the safe pattern.
- Relative parent workspace paths fail in a child's separate workspace.
- `host.lineage[version_id]` and `host.lineage.graph(version_id)` are the source
  of truth for producing-frame and dependency provenance. An artifact listing
  can show `frame_id: None` even when lineage records the child producer.
- Every version is a **separate immutable file**, so there is **no append**. Each
  write is a whole new version, which means concurrent writers each write from
  their own snapshot and the later silently discards the earlier. **Single-writer
  merge is forced, not merely tidy.**
- A pinned version id keeps returning that version forever. Re-list before reading
  if you expect movement.

## Published skills are directories

`host.skills.edit(name, relpath, body)` writes a real file at that relative path,
and the skill reads it back the same way — which is how a skill ships its own
`scripts/` and `reference/`. Two levels of nesting is proven; three is not.

Published skills are **siblings in one flat directory**, with no per-skill
container. So whether one skill can read another's files is a question of read
access, not of architecture — and it is **untested**. Until it is settled, a
cross-skill reference should name the skill as well as the path, so it degrades
to a findable instruction rather than a dead link.

**Publishing is not a mirror.** Deleting a skill from the repo does not unpublish
it; the stale copy goes on loading and describing tools that may no longer exist.
A skill outliving its tools is worse than no skill, because it reads as
authoritative right up to the moment the call fails.
