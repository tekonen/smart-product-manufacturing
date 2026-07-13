# Systematic mapping study protocol — v0.5 (2026-07-14)

> v0.5: IEEE Xplore dropped (journal-only criteria; IEEE journals covered via Scopus/WoS);
> Web of Science access confirmed; Quality and Synthesis chapters rewritten for clarity;
> RQ3 = Scopus reference exports (Option C).

> v0.2: all four open decisions resolved by Teemu (see end of file).
> v0.3: pilot-driven rubric fixes — new exclusion criterion (macro-econ/policy), D1 processor split
> (machine/human), abstracts sourced from Scopus with Semantic Scholar fallback. Product-intelligence
> grading (interface threshold) under discussion — see `intelligence-scale-options.md`.

## Working title

**"Where does the smart reside? A systematic mapping of the locus of intelligence in smart
manufacturing research"**

(Alternative: "Smart processes, dumb products? ..." — punchier, higher risk with conservative reviewers.)

## Background and rationale (one paragraph)

Smart manufacturing research has grown explosively since ~2012, but scoping evidence (OpenAlex,
2026-07-13, see `scoping/2026-07-13-gap-verification.md`) suggests the field locates intelligence
overwhelmingly in the manufacturing process and its resources — machines, scheduling, maintenance,
factories (the *processor*) — rather than in the product being made (the *processee*), its lifecycle,
and the outcomes it delivers to users. The product-as-agent idea (product-driven control, intelligent
products) predates Industry 4.0 but remained marginal (~84 works since 2000), while adjacent
product-side streams (smart product-service systems, digital servitization, smart products in
innovation research) evolved in separate communities with weak ties to manufacturing-systems research.
No prior review audits smart manufacturing literature on this dimension (novelty verified in Scopus
2026-07-13: no precedent for the claim; the term "locus of intelligence" is unclaimed in this domain).

## Research questions

- **RQ1 (locus):** In smart manufacturing research, where is the intelligence located — in the
  manufacturing process/resources (processor), in the product being manufactured (processee), or
  at their interface?
- **RQ2 (outcome):** Which outcomes does the research aim to improve — process-efficiency outcomes
  (productivity, cost, quality of conformance, uptime) or product-value outcomes (product capability,
  lifecycle value, user/customer outcomes)?
- **RQ3 (integration):** To what extent do the smart-manufacturing and smart-product literatures
  cite and build on each other (bibliometric coupling / co-citation)?
- **RQ4 (agenda):** What research opportunities follow, particularly for products that are smart
  *during* manufacturing and that connect production to lifecycle value (AI-enabled, user-adaptive
  products)?

## Design

Systematic mapping study (Petersen et al. 2015 guidelines for mapping studies in software
engineering, adapted) + bibliometric analysis, reported per **PRISMA 2020** (Preferred Reporting
Items for Systematic Reviews and Meta-Analyses) with the PRISMA flow diagram and checklist.
Protocol to be registered on OSF (Open Science Framework) before full screening begins.

## Search strategy

### Databases (revised v0.5, 2026-07-14)
1. **Scopus** (primary — record retrieval, abstracts, DOCTYPE filtering, and the RQ3 reference
   exports per Option C)
2. **Web of Science Core Collection** (second screening database — institutional access confirmed,
   works via university VPN)

**IEEE Xplore dropped (v0.5):** the inclusion criteria are journal-articles-only, and IEEE
journals are fully indexed in both Scopus and Web of Science — IEEE Xplore would add only
conference material that the criteria exclude anyway (pilot 2: 11/30 random records were
conference papers). Documented here so the PRISMA methods section can state the rationale.

**OpenAlex is not a review database in this study**: it was used for scoping and pilot sampling
only (documented in `scoping/` and `pilot/`), and contributes no reported figure in the paper
(per the RQ3 Option C decision).

### Draft search string (Scopus syntax, title-level to keep corpus tractable)

Corpus A — smart manufacturing (the audited corpus):

```
TITLE("smart manufacturing" OR "intelligent manufacturing" OR "smart factory"
  OR "smart production" OR "manufacturing 4.0" OR "cyber-physical production system*")
AND PUBYEAR > 2011 AND PUBYEAR < 2027
AND ( LIMIT-TO ( DOCTYPE , "ar" ) OR LIMIT-TO ( DOCTYPE , "re" ) )
AND ( LIMIT-TO ( LANGUAGE , "English" ) )
```

Corpus B — product-side reference corpus (for RQ3 bibliometrics, not coded):

```
TITLE("smart product*" OR "intelligent product*" OR "smart connected product*"
  OR "product-driven" OR "product avatar" OR "smart product-service")
AND PUBYEAR > 2011 AND PUBYEAR < 2027
```

Notes:
- Title-level search is a deliberate mapping-study choice (high precision, defensible scale);
  sensitivity check: run one TITLE-ABS-KEY variant on a sample year to estimate recall loss.
- "Industry 4.0" deliberately excluded from Corpus A core string (too broad — includes policy,
  education, etc.); include as sensitivity variant.
- 2012 start = post-Industrie 4.0 announcement (Hannover Messe 2011).

### Expected scale and sampling plan
Title-level Corpus A likely 3,000–6,000 records after dedup. Screening plan:
- If ≤ 2,000 after title/abstract screening: code all.
- If more: stratified random sample by year (target n≈800–1,200 coded), plus ALL papers with
  ≥100 citations (census of the influential core). Report both strata separately.

## Inclusion / exclusion criteria

**Include:** peer-reviewed journal articles and reviews (conference papers as sensitivity set);
English; primary focus on smart/intelligent manufacturing (technology, system, method, framework,
or management thereof); 2012–2026.

**Exclude:** editorials, book chapters, non-English; papers where "smart manufacturing" is only
incidental context (e.g., pure materials science, workforce policy); duplicates and retracted items;
**macro-level economics/policy studies whose unit of analysis is not a manufacturing
system/technology** (e.g., city/region/industry econometrics — pilot papers #27, #29; added v0.3).

## Screening procedure

1. Deduplicate (DOI + fuzzy title).
2. Title/abstract screening against criteria — **LLM-assisted with human validation**: Claude codes
   all records; Teemu manually screens a random 10% (target Cohen's kappa ≥ 0.8 vs. LLM; if below,
   revise rubric and re-run). Disclose fully in methods (this is current best practice, e.g.
   guidance emerging in Cochrane/Campbell on AI-assisted screening).
3. Full-text retrieval for coded set (Zotero library as store).
4. **Abstract source (v0.3):** abstracts taken from Scopus API records (complete for curated
   content); Semantic Scholar by DOI as fallback. OpenAlex abstracts NOT used for coding decisions
   (~40% missing for closed-access records, verified in pilot).

## Coding scheme (RQ1/RQ2 — the core contribution)

Each included paper coded on:

| Dimension | Categories |
|---|---|
| **D1. Locus of intelligence** | **processor-machine** (machine/cell/line/factory/supply system) / **processor-human** (worker-as-resource: human-centric, human-in-the-loop, operator support — v0.3 split to capture the Industry 5.0 wave) / processee (the product being made) / interface (product participates in its own production — threshold under discussion, see `intelligence-scale-options.md`) / both |
| **D2. Lifecycle phase addressed** | design / production / distribution / use / end-of-life / multiple |
| **D3. Outcome optimized** | process efficiency (cost, throughput, OEE) / conformance quality / flexibility & customization / product capability or user outcome / sustainability / other |
| **D4. Data-flow direction** | within-process / product→process (usage data feeds manufacturing/design) / process→product (production data enriches the delivered product) / bidirectional |
| **D5. Enabling technology** | free-coded then clustered (digital twin, IoT, ML, agents, ...) |
| **D6. Research type** | conceptual / model or method / case study / survey / review |

Pilot the rubric on 30 papers first; refine; then freeze and register.

**v0.4 amendments from pilot 2 (random sample, 2026-07-14, see `pilot/2026-07-13-pilot2-random-30.md`):**
- Product-intelligence scheme adopted: two-axis Meyer-based coding per Teemu's decision
  (capability C0–C3 × location L-obj/L-net/L-unstated), coded per lifecycle phase.
  **Location axis is conditional on capability ≥ C1** (undefined for C0 — ~95% of the random
  stratum needs one axis only).
- Retrieval and DOCTYPE filtering must come from Scopus (OpenAlex `type=article` includes
  conference papers, repository preprints, and non-indexed venues — 13/30 exclusions in pilot 2).
- Sampling for the real run: seeded random sample without replacement from the exported record set.

## RQ3 bibliometric plan — REVISED (2026-07-14): OpenAlex-bias options under decision

Concern: OpenAlex indexes preprints, repositories, theses and non-curated venues, inflating
citation counts and edge counts relative to Scopus/Web of Science. Options weighed:

- **(A) Hybrid node-validation** — node set = Scopus-screened records only; OpenAlex used solely
  for edges between those validated nodes; dedupe preprint/published pairs by DOI; validate a 5%
  random edge sample against Scopus. Metrics restricted to *structural/relative* measures
  (cross-corpus citation share, coupling clusters), never absolute counts. Effort: low.
  Residual risk: reviewer optics in manufacturing venues; some parsed-reference noise remains.
- **(B) Web of Science export + VOSviewer/bibliometrix** — "Full Record and Cited References"
  export (500–1,000 records/batch, ~10–14 batches for both corpora), standard bibliographic
  coupling + co-citation workflow. Reviewer-proof gold standard; now feasible (VPN access
  confirmed). Effort: moderate manual export work; WoS coverage narrower (document as limitation).
- **(C) Scopus CSV export with references** — same idea via Scopus web UI (2,000-record batches).
  Comparable to (B); keeps everything in one database family with the screening.
- **(D) Outscope the network entirely; replace with a reference-list audit** — for the coded
  random sample (~100+ papers), directly inspect reference lists and count citations landing in
  Corpus B (and vice versa for a Corpus B sample). No third-party citation index involved at all —
  immune to the bias by construction, simple to describe, and arguably more persuasive than a
  network figure at conference-paper scale.

**DECISION (Teemu, 2026-07-14): Option (C) for the conference paper** — Scopus CSV export with
cited references (web UI, 2,000-record batches, via university VPN), bibliographic coupling and
cross-corpus citation share computed from the exported reference lists (VOSviewer/bibliometrix).
Everything stays in the same database family as the screening; OpenAlex is not used for any
reported figure. Journal version: extend the same exports; option (A) may serve as a robustness
cross-check only.

- Hypothesis unchanged: cross-corpus citation share is low (<5%) and not increasing.

## Quality / risk-of-bias handling (clarified v0.5)

**Why there is no per-study quality appraisal.** In a medical systematic review, conclusions
depend on each study's *results*, so each study's internal quality (randomization, blinding, …)
must be graded. A mapping study is different: we do not use any paper's findings — we only
*classify* what each paper is about (locus, capability, outcome, phase). A methodologically weak
paper still counts as valid evidence of where the field directs its attention. Following the
standard guideline for mapping studies (Petersen, Vakkalanka & Kuzniarz 2015, Information and
Software Technology), individual-study appraisal is therefore omitted — reviewers of mapping
studies expect this and the guideline citation answers it.

**What we assess instead: threats to the validity of the MAP itself.** Four, each with a
concrete mitigation and a number that goes in the paper:

1. **Database coverage** — could Scopus + Web of Science miss relevant journals? Mitigation:
   two-database union; report the overlap percentage and the count contributed uniquely by each.
2. **Title-search recall** — searching titles only (for tractability) misses papers that mention
   smart manufacturing only in the abstract. Mitigation (sensitivity check): for one sample year,
   also run the TITLE-ABS-KEY variant, screen the extra records, and report (a) how many relevant
   papers the title search missed and (b) whether the missed papers differ systematically on D1 —
   if the missed papers are just as processor-centric, the recall loss cannot have created the
   finding.
3. **LLM-assisted coding** — Claude codes all records; is that coding trustworthy? Mitigation:
   Teemu independently codes a random 10% of records blind to the LLM's codes; agreement is
   reported as Cohen's kappa (weighted kappa for the ordinal capability axis, simple kappa for
   the categorical locus and location axes), with threshold ≥ 0.8. Below threshold → revise the
   codebook, re-run the full coding, re-validate. The kappa values, the codebook, and the decision
   tree are published with the paper so the coding is reproducible.
4. **Single primary coder** — even validated, one coder's systematic blind spots remain possible.
   Mitigation: the 10% dual-coding above, plus the published decision-tree codebook with worked
   boundary examples (C0: Zhong et al. 2015; C3: Wang et al. 2016), enabling independent
   replication. Acknowledged as a limitation.

## Synthesis and outputs (clarified v0.5)

The synthesis is descriptive: cross-tabulations of the coded dimensions, each answering one
specific question. Planned figures/tables:

1. **PRISMA 2020 flow diagram** — records identified → deduplicated → screened → coded, with
   exclusion counts per criterion. Mandatory for the reporting standard.
2. **Locus over time (D1 × publication year)** — stacked shares of processor-machine /
   processor-human / interface / processee per year. Question answered: *is the field drifting
   toward the product at all, or only toward the worker (Industry 5.0 wave)?* Pilot expectation:
   processor share stays ≈100%; the only visible shift is machine→human.
3. **Locus × outcome (D1 × D3) — the central evidence figure.** A heatmap: where the intelligence
   sits (rows) against what the research optimizes (columns). The thesis predicts mass
   concentrated in one corner: processor-locus × process-efficiency outcomes, with the
   product-value/user-outcome column nearly empty *regardless of locus*. This single figure
   carries the paper's claim — everything else is support.
4. **Capability profile (C0–C3 × lifecycle phase)** — histogram of product capability during
   manufacturing vs. during use. Question: *even when products get capabilities for the use phase,
   are they inert during their own production?* (Pilot 2: 18/18 C0 in manufacturing.)
   Location axis (L-obj/L-net) reported for the C1+ subset only.
5. **Locus × venue (D1 × journal)** — which journals host the rare interface/processee papers.
   Practical payoff: tells us (and readers) where the research agenda finds an audience.
6. **RQ3 figure: bibliographic coupling map + cross-corpus citation share** (from the Scopus
   reference exports, Option C) — visual evidence that the smart-manufacturing and smart-product
   literatures are distinct islands, plus the share of Corpus A references landing in Corpus B
   (hypothesis: <5%, flat over time).
7. **Narrative synthesis + research agenda (RQ4)** — structured by the empty cells of figures 3–4:
   each gap that the maps expose becomes an agenda item, including the AI-enabled, user-adaptive
   product angle (products that remain intelligent *during* manufacturing and connect production
   to lifecycle value).

## Publication plan

1. **Conference first (2027):** Procedia CIRP (CIRP Conference on Manufacturing Systems or CIRP
   Design) or IFIP Advances in Production Management Systems (APMS) — both DOI-issuing, indexed,
   realistic timelines, and standard PhD milestones. Condensed version: scoping + pilot coding.
2. **Journal (extended, 2027–28):** Journal of Manufacturing Systems, Computers in Industry, or
   International Journal of Production Research. Journal of Manufacturing Technology Management
   as a management-oriented fallback.

## Positioning against closest prior work (must-cite)

- Pessôa & Jauregui Becker 2020, Research in Engineering Design (partial precedent — design-process
  focus, not locus-of-intelligence audit). doi:10.1007/s00163-020-00330-z
- Zheng et al. 2019, Advanced Engineering Informatics (smart product-service systems survey).
  doi:10.1016/j.aei.2019.100973
- Raff, Wentzel & Obwegeser 2020, Journal of Product Innovation Management. doi:10.1111/jpim.12544
- Meyer, Främling & Holmström 2009, Computers in Industry. doi:10.1016/j.compind.2008.12.005
- Liu et al. 2026, Advanced Engineering Informatics (data-driven smart product/service design
  review — check scope overlap when published). doi:10.1016/j.aei.2026.104534

## Decisions (resolved 2026-07-13)

1. **Conference-first** — target Procedia CIRP (CIRP Conference on Manufacturing Systems or CIRP
   Design, 2027 cycle), extended journal version after.
2. **Web of Science**: institutional access confirmed (via university VPN) — use as second
   screening database alongside Scopus.
3. **OSF registration**: after pilot coding of 30 papers.
4. **"cyber-physical production system*" added** to the Corpus A title string (done above).
   Note: citation counts reported in the paper should come from Scopus, not OpenAlex — OpenAlex
   counts run higher than curated databases. OpenAlex is used for the RQ3 network analysis only.
