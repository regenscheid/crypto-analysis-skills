# Research retrieval by capability

> Part of `investigate`. Work from the capability needed, not a provider or tool
> name. Literal tool names elsewhere in this catalog are examples from the
> reference **crypto-research-mcp** deployment; translate them to equivalent
> connected MCP, native, or approved local tools when necessary.

## Discover the available route

Before the first retrieval phase:

1. Inspect the tools and MCP connectors available in the current host.
2. Prefer a specialized literature, standards, citation, or repository tool
   when it provides provenance and structured results.
3. Otherwise use a general web-search tool, then a web-fetch tool or an
   available local client for the exact source.
4. If no route supplies the required capability, record it as `BLOCKED` in the
   source-grounding record and tell the user which evidence remains unavailable.

If the reference deployment's `portal_list_servers` exists, use it to refresh
the live connector inventory when a tool name stops resolving. On other hosts,
use their connector or tool-discovery surface. Do not guess renamed tools.

## Reference capability map

| Capability | Reference deployment | Acceptable equivalent |
|---|---|---|
| search cryptographic preprints | `e-print-mcp_search_eprint` | literature-search MCP or domain-constrained web search |
| read preprint metadata | `e-print-mcp_get_eprint` | bibliographic or DOI/ePrint metadata tool |
| read a paper body | `e-print-mcp_eprint_fulltext` | paper-reader MCP, HTML full text, or fetched PDF extraction |
| obtain a paper PDF | `e-print-mcp_eprint_file` | source PDF URL plus a host PDF reader or local PDF tools |
| inspect recent preprints | `e-print-mcp_recent_eprint` | date-filtered literature search |
| search standards and round reports | `nist-mcp_search_csrc` | official-site search or standards MCP |
| read normative text | `nist-mcp_csrc_fulltext` | official HTML/PDF plus document reader |
| check a standard's currency | `nist-mcp_csrc_currency` | official revision/status page |
| search broader scholarly literature | `firecrawl-mcp_firecrawl_research_search_papers` | scholarly-search MCP or web search |
| find citing or related papers | `firecrawl-mcp_firecrawl_research_related_papers` | citation-graph or related-work tool |
| read a paper outside the corpus | `firecrawl-mcp_firecrawl_research_read_paper` | fetched HTML/PDF plus document reader |
| search non-paper sources | `firecrawl-mcp_firecrawl_search` | general web search |
| fetch a specific page | `web-fetch-mcp_web_fetch`, `firecrawl-mcp_firecrawl_scrape` | native/MCP web fetch or approved local HTTP client |
| find implementations and PoCs | `firecrawl-mcp_firecrawl_research_search_github` | repository search or general web search |

**An abstract is not a paper.** Search results identify candidates; they rarely
establish exact preconditions, models, constants, or scope. Open the body and
record a theorem, algorithm, table, page, section, code revision, or normative
locator before using a source as load-bearing evidence.

## Recover from connector failure without looping

- **Tool name not found:** refresh the live tool inventory once and select the
  equivalent capability.
- **Repeated transport, authorization, or server failure:** stop that route
  after the repeated identical failure, preserve the diagnostic, and try one
  materially distinct connector or fetch route.
- **All routes fail:** mark the source class and affected claims `BLOCKED`, flag
  them to the user, and continue only with work independent of that evidence.

Do not turn a transient failure into a permanent global ignore rule. Keep it as
a retriable, dated entry in the investigation record. Do not issue a large batch
of calls after the same failure has already established that the route is down.

## Read PDFs as documents, not just text

Prefer trustworthy HTML or connector-provided full text when available. If the
source is PDF-only, use the host's PDF reader or available local PDF library or
CLI. Preserve page numbers and extraction provenance.

Text extraction is not authoritative for equations, tables, diagrams, or
pseudocode. Render the relevant pages and inspect the page images with an
available vision-capable model or document tool, then cross-check them against
the extracted text. If neither reliable extraction nor page inspection is
available, mark those portions `BLOCKED` rather than reconstructing them from
memory.

## Fetch responsibly

Prefer a connected fetch tool because it can apply its own network policy,
redirect handling, caching, and request headers. When using a direct HTTP client,
send a descriptive non-empty `User-Agent`, follow redirects deliberately, and
retain the final URL and response status. A publisher-specific rejection is a
reason to try an official mirror or another available route, not evidence that
the document does not exist.

## Cover the open-web gap

Much competition cryptanalysis appears only in forum posts, official comments,
workshop slides, issue trackers, or submission pages. A preprint-corpus miss is
therefore not a prior-art result. For a named competition candidate, cover:

1. official standards or round-status records;
2. forum, comment, announcement, and implementation channels;
3. the scholarly and preprint literature.

A negative is a claim about the search and must name its queries, aliases,
channels, dates, exclusions, and blocked routes.

## Keep compute and retrieval separate

Literature connectors need not provide estimators or compute hosts.

- For costing, use `analyze-scheme`'s `scripts/sweep.py` only when SageMath and
  `cryptographic_estimators` are available. Otherwise mark the row `NOT CHECKED`
  and name the missing model.
- For large algebra, use the host's configured compute provider when available;
  otherwise preserve the computation as blocked work.

Prefer the narrowest tool that answers the question. Broad crawlers, monitoring
jobs, and autonomous web agents are not ordinary first-line retrieval tools.
