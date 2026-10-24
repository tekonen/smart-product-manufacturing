# Search-scope validation — human web-interface searches vs scripted API searches

Registered check (protocol amendment log 2026-09-13; OSF registration https://osf.io/w9vj4/, field
"Data validation"): the record volume returned by the AI/API-supported search workflow is
cross-checked against the count a human obtains by entering the same query directly in each
service's native web interface. Any material discrepancy is investigated and resolved before
screening.

## Attestation

I, Teemu Karppinen, confirm that on 2026-10-24 I ran the registered search queries myself, directly
in the native web interfaces of Web of Science Core Collection (webofscience.com) and Scopus
(scopus.com), over the Aalto University network, and obtained the counts below.

*(Recorded by Claude at Teemu's request, from the counts and result links he supplied on
2026-10-24. The links are session-bound search pages tied to his institutional login and may not
open for other readers; the counts are the attested record.)*

## Results

| Corpus | Database | Human web count | API count (2026-10-24) | Difference | Status |
|---|---|---:|---:|---:|---|
| A — smart manufacturing | Scopus | 2,742 | 2,742 | 0 | ✅ match |
| A — smart manufacturing | Web of Science | 2,289 *(Teemu's wider web export, 4,199 rows, filtered to the registered criteria)* | 2,294 | −5, all explained | ✅ **match — every web record is in the API set** |
| B — smart products | Scopus | 524 | 524 | 0 | ✅ match |
| B — smart products | Web of Science | 526 *(2026-10-24, year filter applied)* | 470 | +56 (web is 12% higher) | ⚠️ **OPEN — residual gap, under investigation** |

Result links supplied:

- Web of Science, Corpus A (4,199): https://www.webofscience.com/wos/woscc/summary/22404795-e039-417f-af30-8316b45d242a-01d008a126/relevance/1
- Scopus, Corpus A (2,742): https://www.scopus.com/pages/search/publications?searchId=eeab41d0-8dad-45db-bc53-41210f1c451b
- Scopus, Corpus B (524): https://www.scopus.com/pages/search/publications?searchId=5e77d3f1-868d-41a6-96b8-fa5c60fc4651
- Web of Science, Corpus B (526): https://www.webofscience.com/wos/woscc/summary/af1d6c88-6d4f-4d1f-b518-fa82063b0d87-01d00934bd/relevance/1

API figures: `analysis/corpusA/search_metadata.json`, `analysis/corpusB/search_metadata.json`.

## Web of Science Corpus A discrepancy — screening is blocked until this is resolved

Not yet diagnosed. Candidate explanations to check, in order:

1. **Filters not identical.** The registered Web of Science query includes
   `DT=(Article OR Review) AND LA=(English)` and the 2012–2026 window. If the web search omitted
   any of these (e.g. proceedings papers, early access, other languages, years outside the
   window), the web count rises.
2. **Different Core Collection editions.** The web interface searches every edition Aalto
   subscribes to; the API key may be entitled to fewer (for example without the Emerging Sources
   Citation Index).
3. **Search field.** The registered query is title-only (`TI=`); a Topic search (`TS=`, which also
   covers abstract and keywords) would return many more.
4. **Phrase handling.** The web interface applies lemmatization (matching plural forms); if the
   API does not, "smart factory" would miss "smart factories" there.

Resolution and its effect on the corpus will be recorded below and in the protocol amendment log.

## Resolution

**2026-10-24 — partial.** Teemu identified that the first Web of Science Corpus A web search had no
publication-year filter (2012–2026), so its 4,199 is not comparable to the API count and is set
aside; Corpus A must be re-run in the web interface with the year filter. Candidate 1 (filters not
identical) is thereby confirmed as at least part of the cause.

The Corpus B web search, run with the year filter, returned 526 against the API's 470. A residual
gap of 56 records (12%) remains open; remaining candidates are 2 (editions / API entitlement) and
4 (phrase lemmatization), plus any filter still differing (document type, language).

**2026-10-24 — Corpus A, Web of Science: RESOLVED, PASS.** Instead of re-running the web search,
Teemu exported his wider web query (no year filter; 4,199 rows in 5 batches, 4,113 unique Web of
Science accession numbers — the batches overlapped) to `data/raw/wos_corpusA_*.xls`. The
registered filters were applied to that export by `scripts/validation/wos_export_vs_api.py` and
the result compared with the API search record by record (accession number):

| Step on the web export | Records |
|---|---:|
| all unique records | 4,113 |
| + publication year 2012–2026 | 3,942 |
| + document type Article/Review + language English (= registered query) | **2,289** |
| API search (registered query) | **2,294** |

- Records in both: 2,289. **Web-only: 0** — the API search missed nothing the web search found.
- **API-only: 5** — all journal articles/reviews whose final publication year in the export is
  **2027** (published online in 2026, assigned to 2027 issues). The API's year filter evidently
  matches the online date; the export shows the issue year. They belong in the window by online
  date and stay in the corpus.
- The original 4,199 is fully explained by the missing year filter (171 records outside
  2012–2026) plus the missing document-type and language filters.

**Note for screening (criterion E1).** The registered Web of Science query filters on document type
but not on source type, so 26 records in the API set are *not* journal publications: book chapters
in book series or books (publication type S/B, document type "Article; Book Chapter"), and 2
proceedings papers in a book series. The Scopus query excludes such records by source type. These
26 fail E1 (not a peer-reviewed journal article/review) and are excluded at screening, reported
under E1 in the flow diagram.

**Corpus B, Web of Science (526 web vs 470 API): still open.** Most likely the same cause: the web
count lacked the document-type and language filters. To confirm with the same record-level check,
a Corpus B web export is needed.
