# crypto-analysis-skills

Composable Agent Skills for rigorous cryptanalysis and cryptographic formal
methods. The repository is designed for Claude Science first and keeps the
portable `SKILL.md` core suitable for other Agent Skills hosts.

The complete catalog is meant to be installed. Skill names and descriptions
participate in routing; full skill bodies and bundled references load on demand.
Use a dedicated cryptography profile or organization so unrelated science tasks
do not have to route across this catalog.

## What is included

The current installation contains 161 skills:

- 10 original workbench skills for investigation, scheme and paper analysis,
  attack validation, costing, review, durable knowledge, and Magma;
- 29 symmetric-cryptanalysis skills;
- 59 public-key cryptanalysis skills;
- 63 formal-method and theorem-prover skills.

Six workflow names appeared in both cryptanalysis packs. They remain separate
and are installed with `symmetric-` or `public-key-` prefixes so every skill has
a globally unique callable name.

The formal-method pack is installed with the rest of the catalog but is routed
through `formal-methods-router`. Ordinary cryptanalysis does not have to invoke
a prover merely because the skills are available.

## Control plane

`investigate` is the default entry skill for substantive cryptographic work. It:

1. selects `ASSESS`, `DISCOVER`, `VALIDATE`, or `FORMALIZE` mode;
2. loads the symmetric, public-key, or formal-method orchestrator;
3. selects applicable technique skills explicitly;
4. records a skill trace and complete attack-family coverage ledger;
5. executes the investigation rather than stopping after planning or literature
   review;
6. applies mode-specific completion gates before concluding.

Requests containing “find issues,” “look hard,” “weakness,” “new attack,” or
similar language route to `DISCOVER`. That mode requires structurally distinct
candidates, cheap falsification, explicit unchecked areas, and bounded handoff
of survivors for costing or independent validation.

The main control skills are intentionally short. Detailed domain checklists,
platform behavior, schemas, and references remain on demand.

## Repository layout

Only `skills/` is an Agent Skills runtime surface. Claude Science does not read
the repository's configuration, reports, tests, or maintenance tools when it
selects a skill.

| Path | Role | Install into Claude Science? | Editing policy |
|---|---|---:|---|
| `skills/` | The 161 runtime Agent Skills and their bundled resources | Yes | Edit core skills deliberately; refresh imported skills from their source packs |
| `config/` | Committed machine-readable manifests and cross-repository contracts | No | Generate with repository tools; do not hand-edit |
| `reports/` | Committed, regenerated inspection output | No | Generate with `audit_skills.py`; do not treat as authoritative source |
| `tests/` | Runtime probes and routing acceptance cases | Only install the probe temporarily when testing | Edit when adding a failure case or changing an output contract |
| `tools/` | Developer utilities for import, validation, and response scoring | No | Maintain as ordinary repository code |
| `.agents/` | Ignored local staging for source packs and catalog references | No | Replace locally when new source material arrives |

The flat `skills/` layout is the compatibility boundary. Logical grouping lives
in the domain orchestrators and `config/skill-registry.json`, while the runtime
continues to see ordinary sibling skill directories.

## Claude Science and CScience

Install every directory under `skills/` into the skill location used by the
intended Claude Science organization or cryptography profile. A global personal
installation commonly uses `~/.cscience/skills/`; organization-scoped installs
may live under that organization's `~/.cscience/orgs/.../skills/` directory.

Do not install `.agents/`. It is a local, ignored staging area for source packs,
not part of the runtime distribution.

The original workbench expects one remote research MCP connector:

```text
https://research-mcp-api.npages.org/mcp
```

`skills/investigate/reference/tools.md` maps research capabilities to the
connector's current tool names. Skills degrade by recording a missing capability
when a connector or local backend is unavailable.

### Verify GPT skill loading

CScience routes non-Anthropic models through a compatibility layer, so ordinary
tool-call success does not establish that Agent Skills work. Before a long run:

1. temporarily install `tests/cscience-skill-probe/` as a skill;
2. run both prompts in `tests/cscience-skill-probe-cases.json` with the exact
   model alias and effort setting intended for the investigation;
3. save the raw response and, when possible, the runtime skill-call trace;
4. check the response with:

```bash
python3 tools/check_cscience_probe.py response.json --trace trace.txt
```

This distinguishes discovery failure, body-loading failure, and instruction
adherence failure. Separately confirm that CScience's effort-model and
background-model mappings include the selected GPT aliases.

After the probe passes, run a case from `tests/routing-cases.json` and score the
captured investigation response:

```bash
python3 tools/score_routing_response.py find-fn-dsa-issues response.md --trace trace.txt
```

The trace option is important: a polished report that merely mentions a skill
does not prove the runtime loaded it.

## Optional local backends

| Skill | Optional backend | Without it |
|---|---|---|
| `analyze-scheme` | SageMath and `cryptographic_estimators` | Mark the relevant cost row `NOT CHECKED` and identify the missing model |
| `magma` | A Claude Science SSH compute provider | Skip Magma-specific computation; other skills remain available |
| theorem-prover skills | The named prover and pinned dependencies | Produce a formalization plan or blocked obligation, never a claimed proof |

`workbench-knowledge` writes to `CRYPTO_FILES`, defaulting to
`~/crypto-workbench-files`.

## Maintainer manifests, reports, and tools

These files support reproducible maintenance and attack-catalog consistency.
They are not prompts, and their contents do not consume model context.

### `config/imported-skills.json`

This is the provenance and integrity manifest for the 151 skills imported from
the symmetric, public-key, and formal-method packs. Each record contains:

- source domain and original name;
- installed canonical name;
- source tree hash;
- installed tree hash after collision renaming and cross-reference rewriting.

`tools/import_skill_packs.py --check` reads this manifest and hashes the current
installed trees. A mismatch means an imported skill changed after the recorded
import. That may be an accidental edit or an intentional refactor requiring an
explicitly reviewed manifest update.

This manifest is internal to this repository. The attack catalog should not use
it: source filenames and import hashes are packaging details, not public skill
identifiers.

Do not hand-edit it. Regenerate it while importing a new pack version, or record
reviewed local changes explicitly with:

```bash
python3 tools/import_skill_packs.py --accept-installed-changes
```

Review the skill diff before running that command. It preserves the original
source hash and changes only the installed hash, making the local divergence
visible without pretending it came from the staged pack.

### `config/skill-registry.json`

This is the public identity contract for all installed skills, including the ten
core skills. It is generated directly from the installed `SKILL.md` files and
contains only:

- the canonical `skill_id`, exactly equal to the frontmatter `name`;
- the broad domain: `core`, `symmetric`, `public-key`, or `formal`.

The registry is the file that external consumers should use. In particular, the
attack catalog should validate every attack's `skill_ids` against a pinned copy
of this registry.

Regenerate it with `tools/audit_skills.py` whenever a skill is added, removed, or
renamed. A body or reference edit that leaves the skill name unchanged does not
alter the catalog contract, although running the audit remains appropriate.

Do not add aliases or catalog attack records to this file. Skill IDs are intended
to be stable; a rename is a coordinated migration across both repositories.

### `reports/skill-inventory.json`

This is a deterministic review artifact generated from the current `skills/`
tree. It records:

- skill count and counts by domain;
- every name and description;
- description word counts and body line counts;
- missing relative links;
- structural warnings and errors.

Use its version-control diff to notice unexpected description changes, prompt
growth, missing resources, or domain movement. It is useful for maintainers and
reviewers but is not authoritative: `SKILL.md` remains the source of truth and
`config/skill-registry.json` remains the external identifier contract.

Do not hand-edit this report. Regenerate it before reviewing or committing skill
changes. If the project later chooses not to commit generated reports, the same
tool can produce it as disposable build output without changing runtime behavior.

### `tools/`

| Tool | Reads | Writes or checks | Use it when |
|---|---|---|---|
| `import_skill_packs.py` | Extracted packs under `.agents/`, or installed skills when checking | Copies self-contained skills into `skills/`; writes, verifies, or explicitly refreshes installed hashes in `config/imported-skills.json` | Performing a fresh import, verifying imported trees, or recording a reviewed local divergence |
| `audit_skills.py` | `skills/`, routing cases, the Claude Science adapter contract, and the import manifest | Writes `config/skill-registry.json` and `reports/skill-inventory.json`; checks names, descriptions, links, collisions, routing identifiers, and required adapter API/behavior text | After any skill change and before committing |
| `check_cscience_probe.py` | A captured CScience response and optional runtime trace | Pass/fail result for discovery, body loading, and exact adherence | Testing a particular model alias and effort configuration |
| `score_routing_response.py` | A routing case, captured investigation response, and optional trace | Pass/fail result for mode, actual skill trace, coverage, and completion behavior | Comparing Claude/GPT behavior or reproducing a routing regression |

Python `__pycache__/` directories are disposable interpreter caches and are
ignored by version control.

### `tests/`

`tests/cscience-skill-probe/` is a deliberately tiny diagnostic Agent Skill. Its
body contains a marker not present in its description. A correct response shows
that the model loaded the body; a runtime trace additionally shows that the host
actually invoked the skill.

`tests/cscience-skill-probe-cases.json` contains the implicit and explicit probe
prompts. `tests/routing-cases.json` contains representative cryptanalysis prompts
and their expected modes and skill traces. Add a case whenever a real failure is
found so future refactors have an evidence-based regression target.

`tests/claude-science-adapter-contract.json` protects the exact Claude Science
API calls and measured runtime rules documented by `investigate`. The audit fails
if a future shortening removes required plan, child-gate, delegation, artifact,
or lineage instructions, or restores a disproven parent-only rule. Update this
contract only when a rerun against a named runtime version changes the evidence.

## Standard validation

Run the deterministic checks from the repository root:

```bash
python3 tools/import_skill_packs.py --check
python3 tools/audit_skills.py
```

The first command verifies that the imported trees still match their recorded
hashes. The second validates all installed skills and regenerates the registry
and inventory. Both should succeed with zero errors before a release.

To reproduce an import from a fresh local `.agents` staging area, run
`python3 tools/import_skill_packs.py`. The importer refuses to overwrite an
existing skill so a source-pack refresh cannot silently destroy local changes.
Perform refreshes in an empty temporary destination or dedicated branch, inspect
the diff, and then accept the intended changes into `skills/` and the manifest.

## Common maintenance workflows

| Change | Required action | Attack-catalog action |
|---|---|---|
| Edit a core skill body or reference | Run `audit_skills.py`; review the inventory diff | None if `name` is unchanged |
| Deliberately edit an imported skill | Review why it diverges; run `import_skill_packs.py --accept-installed-changes`; run both validators; review the manifest diff | None if `name` is unchanged |
| Refresh an imported pack | Stage under `.agents/`; import into an empty destination; review collisions and content diffs; update installed trees and manifest; run both validators | Sync the registry only if canonical names changed |
| Add a skill | Add its directory and valid `SKILL.md`; run `audit_skills.py` | Sync the registry before referencing the new ID |
| Rename or remove a skill | Update folder, frontmatter, internal references, routing cases, and registry | Migrate every affected `skill_ids` entry in the same coordinated change |
| Add or edit an attack | No skill-repository change | Validate its `skill_ids` against the pinned registry |
| Diagnose GPT/CScience behavior | Run the probe, then a routing case; retain raw response and trace | None |

## Attack catalog boundary

The cryptographic attack catalog is not installed as Agent Skills and is not
copied into this repository. It is reference input for identifier and coverage
checks and is intended to become an MCP server.

Both systems use one canonical identifier: the exact `name` in a skill's
`SKILL.md` frontmatter. Attack records should store those values directly in a
`skill_ids` array. The catalog derives its reverse skill-to-attack index from the
records instead of maintaining a second hand-written crosswalk.

`config/skill-registry.json` is the validation boundary. Adding or changing an
attack does not change the registry. Adding or renaming a skill regenerates the
registry, after which catalog validation can reject unknown identifiers. There
is no runtime alias layer.

### Catalog-side use

Store direct canonical IDs on each attack record:

```json
{
  "attack_id": "ATT-PQC-...",
  "skill_ids": [
    "ntru-and-falcon-analysis",
    "public-key-attack-complexity-and-success-auditor"
  ]
}
```

Derive the reverse `skill_id → attacks` index from those records. Do not maintain
a separate hand-written crosswalk, because it can disagree with the records.

Because the skills and attack catalog live in separate repositories, the catalog
should vendor or otherwise pin a released `skill-registry.json` together with
the source repository commit or tag. Catalog validation should fail for unknown,
duplicate, or legacy namespaced IDs. It may report—but should not necessarily
fail on—skills with no attacks and attacks with no mapped skill.

The catalog can grow continuously against the same pinned registry. A registry
sync is required only when the set of canonical skill IDs changes. The MCP should
report the registry revision against which its catalog was validated so clients
can diagnose drift.

## Portability

Cryptanalytic procedure stays in portable `SKILL.md` files. Claude
Science-specific planning, delegation, connector, artifact, and compatibility
behavior lives in `skills/investigate/reference/claude-science.md` and related
references.

Open Science Desktop integration is a future adapter layer. It should reuse the
portable skills and supply host-specific discovery, traces, tools, and artifact
handling without forking the cryptanalytic method. This integration does not
modify the Open Science repository.

## Evidence rules

- Never infer security from a search miss, timeout, or bounded experiment.
- Never report a cost without its model, units, assumptions, and success rate.
- Keep primitive, construction, parameter, implementation, and deployment
  findings separate.
- Preserve negative and conflicting evidence.
- Call a result a break only when its actual model, scope, preconditions, costs,
  and independent check support that word.
