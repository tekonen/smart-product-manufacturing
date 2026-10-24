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
| A — smart manufacturing | Web of Science | 4,199 | 2,294 | +1,905 (web is 83% higher) | ⚠️ **OPEN — material discrepancy, under investigation** |
| B — smart products | Scopus | 524 | 524 | 0 | ✅ match |
| B — smart products | Web of Science | not yet run | 470 | — | ⏳ pending |

Result links supplied:

- Web of Science, Corpus A (4,199): https://www.webofscience.com/wos/woscc/summary/22404795-e039-417f-af30-8316b45d242a-01d008a126/relevance/1
- Scopus, Corpus A (2,742): https://www.scopus.com/pages/search/publications?searchId=eeab41d0-8dad-45db-bc53-41210f1c451b
- Scopus, Corpus B (524): https://www.scopus.com/pages/search/publications?searchId=5e77d3f1-868d-41a6-96b8-fa5c60fc4651

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

*(pending)*
