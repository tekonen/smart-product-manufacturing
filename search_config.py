"""Search configuration — CORPUS A (smart manufacturing; the audited, screened and coded corpus).

Verbatim from the registered protocol: OSF registration https://osf.io/w9vj4/
(DOI 10.17605/OSF.IO/W9VJ4) and protocol/slr-protocol-v1.0.md §5. Any change here is a
registration deviation and must be logged in the protocol amendment log first.

Corpus B (RQ3 reference corpus, not screened) lives in search_config_corpusB.py and is run
separately so the two corpora are never merged.

Usage (requires the plugin patch in scripts/plugin-patches/ — no journal filter):
    uv run <plugin>/scripts/pipelines/search.py --config ./search_config.py \
        --databases scopus,wos --output-dir analysis/raw/corpusA --metadata-dir analysis/corpusA
"""

# 1. Time window (inclusive). The searchers add PUBYEAR > 2011 AND PUBYEAR < 2027 (Scopus)
#    and PY=2012-2026 (Web of Science), matching the registered window.
FROM_YEAR = 2012
TO_YEAR = 2026

# 2. Journal scope — deliberately EMPTY: the registered design is title-scoped with no journal
#    list or tier filter.
JOURNALS = {}

# 3. Queries — (label, scopus_query, wos_query). Year filter is added by the searchers.
QUERY_DEFS = [
    (
        "corpusA_smart_manufacturing",
        'TITLE("smart manufacturing" OR "intelligent manufacturing" OR "smart factory" '
        'OR "smart production" OR "manufacturing 4.0" OR "cyber-physical production system*") '
        'AND (DOCTYPE(ar) OR DOCTYPE(re)) AND LANGUAGE(english) AND SRCTYPE(j)',
        'TI=("smart manufacturing" OR "intelligent manufacturing" OR "smart factory" '
        'OR "smart production" OR "manufacturing 4.0" OR "cyber-physical production system*") '
        'AND DT=(Article OR Review) AND LA=(English)',
    ),
]

# 4. OpenAlex / Semantic Scholar block terms — not used (registered databases are Scopus + WoS).
BLOCK_A_TERMS = []
BLOCK_B_TERMS = []
