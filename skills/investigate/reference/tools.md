# The research tools, by what you want rather than what they are called

> Part of `investigate`. Every skill here assumes one remote MCP server —
> **crypto-research-mcp** — and calls its tools by name. The names below were
> current when this was written and **will drift**. If one does not resolve, call
> `portal_list_servers` and read the live list rather than guessing a variant.

## Retrieval, in the order that costs least

| you want | call |
|---|---|
| preprints by topic | `e-print-mcp_search_eprint` |
| one preprint's metadata | `e-print-mcp_get_eprint` |
| **a paper's body** | `e-print-mcp_eprint_fulltext` |
| the PDF itself | `e-print-mcp_eprint_file` |
| what appeared recently | `e-print-mcp_recent_eprint` |
| a standard or round report | `nist-mcp_search_csrc` |
| **a standard's normative text** | `nist-mcp_csrc_fulltext` |
| is this standard current? | `nist-mcp_csrc_currency` |
| published literature beyond ePrint | `firecrawl-mcp_firecrawl_research_search_papers` |
| what cites or resembles a paper | `firecrawl-mcp_firecrawl_research_related_papers` |
| read a paper the corpora lack | `firecrawl-mcp_firecrawl_research_read_paper` |
| **anything that was never a paper** | `firecrawl-mcp_firecrawl_search` |
| a specific page | `web-fetch-mcp_web_fetch`, `firecrawl-mcp_firecrawl_scrape` |
| implementations, PoC code | `firecrawl-mcp_firecrawl_research_search_github` |

**An abstract is not a paper.** `search_*` returns titles and abstracts; an
abstract identifies a result and rarely states the preconditions, the model, or
the constants. Reaching a conclusion from search output alone is the commonest
avoidable error here — open the body.

## The gap that the open web fills

**A large share of competition cryptanalysis was never published as a paper.** It
was a `pqc-forum` post, an official comment, a slide from a workshop, or a note
on a submission page. `e-print-mcp_search_eprint` cannot see any of it.

So "no attack found on ePrint" is not "no attack found". For any named
competition candidate the sequence is:

1. `nist-mcp_search_csrc` — the round-status reports (IR 8240, 8309, 8413, 8528,
   8610) carry one section per candidate saying what happened and why
2. `firecrawl-mcp_firecrawl_search` — the forum thread, the comment, the
   announcement
3. `e-print-mcp_search_eprint` — the paper, if one was ever written

**A negative is a claim about your search, and it must name its channels.** See
`crypto-review`'s `reference/invalid-inferences.md`, first row.

## What this server does not have

No local "was it broken" corpus, no local estimator, no compute host. Those are
separate concerns:

- **costing** — `analyze-scheme` ships `scripts/sweep.py`, which needs Sage and
  `cryptographic_estimators` **on the machine running the skill**. Absent those,
  the skill still applies: name the model, state what you could not compute, and
  put it in `NOT CHECKED`.
- **algebra at scale** — `magma` uses Claude Science's own SSH compute provider,
  which is configured per-user and is not part of this MCP server.

## Tools that are not research tools

`portal_*` manage which sub-servers are enabled; `firecrawl_monitor_*` schedule
recurring crawls; `firecrawl_crawl` and `firecrawl_agent` are broad, slow and
expensive. None belongs in an ordinary investigation. **Prefer the narrowest tool
that answers the question** — a crawl where a search would do is the same
category of error as a computation nobody sized.
