---
name: cscience-skill-probe
description: Diagnose whether a Claude Science or CScience model can discover, load, and follow an Agent Skill. Use whenever asked to run the CScience skill probe, verify skill loading for a model alias, test GPT skill compatibility, or check whether Agent Skills work before a long cryptographic investigation.
---

# CScience skill probe

Return exactly this JSON object, with no Markdown fence or additional text:

```json
{
  "probe": "cscience-skill-probe",
  "body_marker": "CSCIENCE-SKILL-BODY-9D3C2A71",
  "instructions_loaded": true,
  "next": "inspect the runtime trace for the skill call"
}
```

Do not call research, network, filesystem, or computation tools. This probe tests
skill discovery, body loading, and instruction adherence—not general tool use.
