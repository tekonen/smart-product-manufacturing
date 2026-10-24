"""Search configuration — CORPUS B (smart/intelligent products; RQ3 reference corpus, NOT screened).

Verbatim from the registered protocol (OSF https://osf.io/w9vj4/, protocol §5). Run separately
from Corpus A so the corpora are never merged.

Usage:
    uv run <plugin>/scripts/pipelines/search.py --config ./search_config_corpusB.py \
        --databases scopus,wos --output-dir analysis/raw/corpusB --metadata-dir analysis/corpusB
"""

FROM_YEAR = 2012
TO_YEAR = 2026

JOURNALS = {}  # no journal filter (title-scoped design)

QUERY_DEFS = [
    (
        "corpusB_smart_products",
        'TITLE("smart product*" OR "intelligent product*" OR "smart connected product*" '
        'OR "product-driven" OR "product avatar" OR "smart product-service") '
        'AND (DOCTYPE(ar) OR DOCTYPE(re)) AND LANGUAGE(english) AND SRCTYPE(j)',
        'TI=("smart product*" OR "intelligent product*" OR "smart connected product*" '
        'OR "product-driven" OR "product avatar" OR "smart product-service") '
        'AND DT=(Article OR Review) AND LA=(English)',
    ),
]

BLOCK_A_TERMS = []
BLOCK_B_TERMS = []
