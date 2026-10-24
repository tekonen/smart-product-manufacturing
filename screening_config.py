"""Per-project screening configuration for a systematic review.

Copy this file to the root of your SLR project and edit the two
prompts (abstract screening + full-text coding) for your specific
review. `abstract_screen.py` and `fulltext_code.py` read this module
by path (via `--config`).

The prompts ARE the scope of your screening — reviewers will read
them to judge whether your decisions can be reproduced. Keep this
file in git; version the prompts via `*_PROMPT_VERSION` strings so
log rows record which version rendered each decision.

Usage:
    uv run ${CLAUDE_PLUGIN_ROOT}/scripts/pipelines/abstract_screen.py \\
        --config ./screening_config.py --group <id> --collection <key>
"""

# =============================================================================
# Abstract screening (stage 1) — Claude Haiku on title + abstract
# =============================================================================

ABSTRACT_SCREENING_MODEL = "claude-haiku-4-5-20251001"
ABSTRACT_SCREENING_PROMPT_VERSION = "v1-2026-10-24"

# Approved by Teemu 2026-10-24 (criterion by criterion). Mirrors the registered criteria
# (OSF w9vj4): inclusion I1-I3, exclusion E1-E4; E5/E6 handled by pipeline. Verbatim copy
# archived in protocol/screening-prompt.md BEFORE screening (registered commitment).
ABSTRACT_SCREENING_SYSTEM_PROMPT = """\
You are a systematic review screener for a systematic MAPPING study. Your task is to decide
whether a paper is ELIGIBLE for the corpus. You are NOT judging whether it supports any
hypothesis.

Review question (context only): Where does smart manufacturing research locate intelligence —
in the manufacturing process and its resources (machines, systems, workers), in the product
being manufactured, or at their interface — and which outcomes does it optimize?

IMPORTANT: Do NOT judge where a paper locates intelligence. Papers about smart machines,
factories, scheduling, workers, products, or anything else are ALL eligible if the criteria
below are met. Classification happens later; screening decides eligibility only.

=== INCLUSION CRITERIA — ALL must hold ===
I1. Primary focus: the paper's main subject is smart / intelligent manufacturing — a
    manufacturing technology, system, method, framework, or the management of these.
    Examples: smart factories; cyber-physical production systems; digital twins of production;
    AI, machine learning, IoT or data analytics applied to manufacturing; Industry 4.0
    manufacturing operations; human-centric or Industry 5.0 manufacturing; smart or
    intelligent products in a manufacturing context; adoption of smart manufacturing by firms.
I2. Unit of analysis: a manufacturing system, technology, firm-level practice, or product.
I3. Document type: a peer-reviewed journal article or review.

=== EXCLUSION CRITERIA — ANY one excludes (registered codes) ===
E1. Not a peer-reviewed journal article or review — e.g. editorial, guest editorial,
    book chapter, conference paper, erratum, news item, trade-magazine piece, short note.
E2. Full text not in English. (Normally not decidable here — use only if evident.)
E3. Smart manufacturing is only incidental — the actual subject lies outside manufacturing;
    the term appears as title decoration or motivation only. Example: a chip, material, or
    software study that mentions smart manufacturing only as a possible application.
E4. Unit of analysis is not a manufacturing system or technology — macro-level economics or
    policy studies of a city, region, country, or industry. Example: econometric study of the
    effect of "intelligent manufacturing" on regional pollution, employment, or GDP.
(E5 duplicate and E6 retracted are handled outside this prompt, by the deduplication pipeline
and the retraction check.)

=== DECISION RULES ===
- INCLUDE: the title/abstract shows I1, I2 and I3 all hold and no exclusion applies.
- EXCLUDE: the title/abstract clearly shows an exclusion criterion applies. Cite its code.
- BORDERLINE: uncertain — no abstract, ambiguous focus, mixed unit of analysis, or document
  type unclear. Borderline papers are decided at the full-text stage.

BIAS: Be liberal. When uncertain between include and borderline, choose include. When uncertain
between borderline and exclude, choose borderline. Missing an eligible paper is more costly than
reading one extra full text.

Respond with EXACTLY two lines:
DECISION: include|borderline|exclude
REASON: <one sentence citing the criterion code (I1–I3 or E1–E4) that triggered the decision>
"""


# =============================================================================
# Full-text coding (stage 2) — Claude Sonnet on full PDF text
# =============================================================================

FULLTEXT_CODING_MODEL = "claude-sonnet-4-6"
FULLTEXT_CODING_PROMPT_VERSION = "v1-2026-04-21"

# Define every coding field the script should extract. Each entry:
#   name         — snake_case column name (goes into CSV + manuscript)
#   description  — free-text guidance given to the LLM
#   example      — optional one-sentence example of what a good value looks like
#
# The script serialises these into the JSON schema section of the prompt.
# Add, remove, or reorder fields freely — the CSV schema follows this list.
FULLTEXT_CODING_FIELDS = [
    {
        "name": "key_findings",
        "description": "Short summary of what the paper concludes about the "
                       "relationship under study. Two to four sentences. "
                       "Paraphrase; do not copy the abstract verbatim.",
    },
    {
        "name": "sample",
        "description": "One sentence describing the sample: country, size, "
                       "population, sampling frame. Example: 'Survey of 1,243 "
                       "Finnish nascent entrepreneurs drawn from GEM 2014.'",
    },
    {
        "name": "method",
        "description": "The empirical method(s) used. Include research design "
                       "(cross-sectional / longitudinal / experiment / "
                       "qualitative / case / meta-analysis), estimation "
                       "technique, and any causal-identification strategy.",
    },
    # Add as many fields as your coding schema demands. 5–15 is typical.
    # Suggested additions for entrepreneurship SLRs:
    #   theories_and_references  — theoretical lenses used
    #   direction_of_relationship — sign of the main effect
    #   moderators_boundary_conditions — specified boundary conditions
    #   causal_inference_strength — RCT / quasi-experiment / observational
    #   future_research          — explicit gaps the authors call out
]

FULLTEXT_CODING_SYSTEM_PROMPT = """\
You are a systematic-review coder. You read the full text of a paper and \
extract a structured record for downstream analysis.

RESEARCH QUESTION:
<INSERT YOUR RESEARCH QUESTION — same as abstract screening>

INCLUSION CRITERIA (the paper reached this stage because the abstract \
passed — your job now is to decide whether the full text confirms \
inclusion, and if so, to extract the coding fields):

<INSERT YOUR STAGE-2 CRITERIA HERE. Typically: re-verify all stage-1 \
criteria against the full text; check for population/construct/outcome \
assumptions that the abstract didn't clarify>

EXCLUSION CODES (for the full-text stage):
  FE1-<full-text exclusion reason>
  FE2-<...>
  FE3-<...>
  FE4-<...>
  FE5-<catch-all>

OUTPUT FORMAT — strict JSON, one object. Fields:

{{
  "decision": "include" | "exclude",
  "exclusion_code": "<code or empty if include>",
  "reason": "<one to three sentences justifying the decision>",
  {coding_fields_json_placeholder}
}}

Additional rules:
- For every coding field above, provide SUBSTANTIVE content if include, or \
an empty string if exclude.
- Do not paraphrase the abstract. Extract from body, methods, results, \
and discussion.
- If a citation is claimed ("prior work by Smith 2019"), include a short \
reference in the relevant field so the evidence is traceable.
- Return ONLY the JSON object — no prose before or after.
"""
