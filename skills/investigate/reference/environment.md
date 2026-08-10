# What this environment does and does not permit

> Part of `investigate`. **These are properties of Claude Science, not of this
> workbench** — they stay true on someone else's machine, which is why they ship
> here rather than living in `knowledge.md`. Every one was measured, and several
> were measured only after a wrong assumption had already cost a day.

Read this when something fails in a way that looks like a bug in your code. Most
of the entries below were first diagnosed as the wrong problem entirely.

## Reading a failure correctly

The single highest-value table here. Three failures look alike in a traceback and
have nothing to do with each other.

| symptom | what it means | what fixes it |
|---|---|---|
| `HTTP 000`, or `Tunnel connection failed: 403` | the **proxy refused CONNECT** — the request never reached the host | a network-access grant, asked for by the **root** conversation |
| a plain `HTTPError 403` / `404` | the request **did reach the host**, which refused it | usually your request, not a grant — see the user-agent note below |
| `Operation not permitted` | **filesystem**, not network | a path grant, or the wrong kernel (below) |

`HTTP 000` is not an HTTP status. It is curl reporting that no request completed.
**Do not ask for a network grant before establishing which of these you have.** A
delegated track once burned 7.7 hours waiting on a grant that would have fixed
only half its problem, because both errors arrived together and were read as one.

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

## A subagent has no channel to a human

This is the one that costs hours rather than minutes, because it fails
**silently**.

`generate_plan` is not in a subagent's toolset at any access level. Neither is any
route to a person. `request_network_access` asks *your parent* — and a subagent's
parent is another agent, so nothing answers. Measured: a delegated track requested
a domain, blocked **7.7 hours**, produced zero artifacts, and was killed; the
request never received a verdict of any kind. The root conversation asking for a
different domain the same day was granted within one message.

**Anything ending in a person deciding — an approval, a grant, a scope call, a
permission — belongs to the root.** A subagent that needs one records it, keeps
working, and surfaces it where the parent will read it.

There is **no verified parent→child message channel.** `host.send_message` appears
in delegation briefs and has never once been invoked across thousands of host
calls — treat it as unproven. What is proven: `delegate`, `collect`, `stop_child`,
`list_running_children`, and `ask_user` (the root's route to a human). So get a
grant *before* delegating, let the child retry on a later pass, or `stop_child`
and re-delegate.

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

- A new conversation sees **all** the project's artifacts; `list_artifacts()`
  needs no scoping argument. Conversation-scoping is a default, not a wall.
- The ids it returns are **version ids**, not artifact ids. Saving by a version id
  resolves to the parent artifact and appends a new version — verified across
  conversations.
- Saving by **filename** is what forks silently: the same name can end up as two
  separate artifacts.
- `{{artifact:<version_id>}}` in a delegation brief expands to a filesystem path,
  and a subagent can read it with plain `open()`.
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
