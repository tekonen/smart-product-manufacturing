# OSF registration draft (paste-ready, 2026-07-14)

Target: OSF Registries → "Open-Ended Registration" or "Generalized Systematic Review Registration"
template (either works for mapping studies; the generalized SR template is the better fit).
Field names below follow the generalized template; trim to fit character limits where needed.

---

**Title:** Where does the smart reside? A systematic mapping of the locus of intelligence in
smart manufacturing research

**Description / Background:**
Smart manufacturing research has grown rapidly since 2012, yet scoping evidence suggests the
field systematically locates intelligence in the manufacturing process and its resources —
machines, scheduling systems, factories, and more recently the human worker — rather than in the
product being manufactured, its lifecycle, or the outcomes it delivers to users. Product-oriented
research streams (intelligent products, smart product-service systems, digital servitization)
exist but evolved in separate communities. No prior review has audited the smart-manufacturing
literature for where intelligence resides and which outcomes it serves. This systematic mapping
study quantifies that asymmetry and derives a research agenda.

**Research questions:**
RQ1: Where does smart manufacturing research locate intelligence — in the process/resources
(machine or human), in the product being manufactured, or at their interface?
RQ2: Which outcomes does the research optimize — process outcomes or product-value/user outcomes?
RQ3: To what extent do the smart-manufacturing and smart-product literatures cite each other?
RQ4: What research opportunities follow for products that remain intelligent during their own
manufacture and connect production to lifecycle value?

**Hypotheses (directional expectations from two pilots, n=46, conducted before registration and
disclosed as such):**
H1: >90% of coded papers locate intelligence in the processor (machine or human); <5% in the
product or at the product-process interface.
H2: Product capability during the manufacturing phase is C0 (identified-only) for the large
majority of papers, including papers whose products have use-phase capabilities.
H3: The cross-corpus citation share between the smart-manufacturing corpus and the smart-product
corpus is below 5% of references and not increasing over time.

**Study design:** Systematic mapping study per Petersen, Vakkalanka & Kuzniarz (2015); reporting
per PRISMA 2020. No per-study quality appraisal (classification study; individual study results
are not used).

**Data sources:** Scopus (primary; records, abstracts, cited-reference exports) and Web of Science
Core Collection. Search: title-level, 2012–2026, journal articles and reviews, English.
Corpus A (audited): TITLE("smart manufacturing" OR "intelligent manufacturing" OR "smart factory"
OR "smart production" OR "manufacturing 4.0" OR "cyber-physical production system*").
Corpus B (RQ3 reference corpus): TITLE("smart product*" OR "intelligent product*" OR "smart
connected product*" OR "product-driven" OR "product avatar" OR "smart product-service").

**Eligibility criteria:** Include peer-reviewed journal articles/reviews in English with primary
focus on smart manufacturing. Exclude conference papers (kept as sensitivity set), editorials,
book chapters, non-English full text, incidental-context papers, macro-level economics/policy
studies whose unit of analysis is not a manufacturing system/technology, preprints, duplicates,
retracted items.

**Sampling plan:** Census of records with ≥100 Scopus citations plus a seeded random sample
(without replacement, stratified by publication year) from the remainder; target 800–1,200 coded
records; strata reported separately. Random seed fixed and archived before sampling.

**Variables (coding scheme, frozen before registration):**
D1 locus of intelligence: processor-machine / processor-human / processee / interface / both.
D1b product capability (Meyer, Främling & Holmström 2009, amended): C0 identified-only /
C1 information handling / C2 problem notification / C3 decision making — coded separately for
the manufacturing phase and the use phase. Interface locus requires C3 in manufacturing.
D1c intelligence location (conditional on capability ≥C1): at-object / through-network / unstated.
D2 lifecycle phase; D3 outcome optimized; D4 data-flow direction; D5 enabling technology
(free-coded); D6 research type. Codebook with decision tree and worked boundary examples is
archived with this registration.

**Analysis plan:** Descriptive cross-tabulations (locus × year; locus × outcome; capability ×
phase; locus × venue); PRISMA flow diagram; RQ3 via bibliographic coupling and cross-corpus
citation share computed from Scopus cited-reference exports (VOSviewer/bibliometrix). No
inferential statistics beyond inter-rater agreement.

**Coding procedure and validation:** Primary coding by a large language model (Claude, Anthropic)
applied to titles+abstracts, escalating to full text per codebook rules; a blind random 10% of
records independently coded by the human author. Agreement thresholds: weighted Cohen's kappa
≥0.80 on the ordinal capability axis, simple kappa ≥0.80 on locus and location. Below threshold:
codebook revised, full corpus recoded, validation repeated. All kappas reported.

**Known biases / prior work disclosure:** Two pilots (cited-core n=28, random n=18) were coded
before registration and shaped the codebook; their results (45 processor / 1 interface /
0 processee) are disclosed above as directional expectations and will be reported as pilot work,
separate from the registered coding run.

**Timeline:** Screening and coding 2026 H2; conference submission (Procedia CIRP) 2027 cycle;
extended journal version thereafter.

---

## Additional form fields (texts as submitted 2026-07-14; mirrored in protocol v1.0 amendment log)

**Dependent/outcome/main variables:** the coded dimensions D1–D6 as defined in protocol §8
(locus of intelligence; product capability C0–C3 per phase; intelligence location; lifecycle
phase; outcome optimized; data-flow direction; enabling technology; research type), plus the
RQ3 cross-corpus citation share.

**Independent variables:** Not applicable — descriptive mapping review; no associations, effects,
interventions, or treatments examined.

**Additional variables/covariates:** None. Bibliographic metadata (publication year, venue) used
descriptively; sampling stratum (≥100-citation census vs. seeded random sample) and database
source reported as stratifiers. No covariates, moderators, or mediators modeled. Full detail in
the archived protocol v1.0.

**Databases:** Scopus; Web of Science Core Collection.

**Interfaces:** Scopus via Elsevier's native web interface (scopus.com, Advanced document
search); Web of Science via Clarivate's native web interface (Advanced search).

**Grey literature:** none searched — eligibility restricted to peer-reviewed journal articles and
reviews by design; conference papers captured only as a separate sensitivity set; preprints,
theses, and reports excluded.

**Search validation procedure:** (1) known-item validation — the final Corpus A export must
contain Kang et al. 2016, Kusiak 2017, Tao et al. 2018, Monostori 2014, and Wang et al. 2016
(DOIs in protocol amendment log); any miss triggers string revision + re-export, documented in
the amendment log before screening. (2) Recall sensitivity check — title-only vs. TITLE-ABS-KEY
for sample year 2019; miss rate and D1 profile of missed papers reported.

**Other search strategies:** none for corpus construction — no ascendancy/descendancy
(snowballing), because the corpus boundary must be reproducible and RQ3 measures citation flows,
which citation-based corpus building would contaminate. Citation data used analytically only.

**Author contact:** none; all data from published records. Results of contacting authors: N/A.

**Software:** Scopus + Web of Science (native web interfaces) for retrieval; Claude (Anthropic
LLM via Claude Code, model version recorded in the repository at coding time) for screening/coding
with independent human validation; Python (pandas) scripts (archived in the repository) for
merge/dedup/sampling; Zotero for full texts; VOSviewer and/or bibliometrix for RQ3; Git/GitHub
for versioning. Versions recorded in the repository as used.

**Funding:** [Teemu fills the true variant — unfunded, or funder named, with "funder has no role"
clause.]

**Conflicts of interest:** none declared; no party with an interest in the outcome is involved.
Author has no affiliation with Anthropic, whose language model is used as a coding instrument.

**Screening stages:** Stage 0 dedup (scripted, DOI + fuzzy title, overlap reported) → Stage 1
title/abstract screening (LLM applying exclusion criteria E1–E6 with per-criterion decisions;
blind human 10% validation, κ ≥ 0.80, below → revise + full re-screen) → Stage 2 coding of the
sampled set (title/abstract, escalate to full text on adjacent-level ambiguity; conservative
lower-code rule; borderline cases resolved by the human author).

**Screened fields / blinding:** no blinding — title, abstract, year, venue, document type
visible (year and venue are themselves coded variables; document-type and incidental-context
criteria depend on them). Author names play no role in any rule. Mitigation = blind 10%
dual-screening with pre-registered threshold.

**Exclusion criteria (applied in order; first met = recorded reason):** E1 not a peer-reviewed
journal article/review (conference papers → separate sensitivity set; editorials, chapters,
preprints excluded); E2 full text not English; E3 smart manufacturing incidental to the paper's
subject; E4 unit of analysis not a manufacturing system/technology (macro econ/policy);
E5 duplicate; E6 retracted. Window/language additionally enforced by the search string.

**Screener instructions:** in the registration-linked repository — protocol v1.0 §§6–8 +
intelligence-scale-options.md (per-level test questions, worked examples: Zhong 2015 = C0,
Wang 2016 = C3). The verbatim LLM screening prompt is archived in the repository as
`protocol/screening-prompt.md` BEFORE screening begins.

**Screening reliability:** two screeners, asymmetric roles — LLM screens all; human author
independently screens a blind random 10% (validation sample drawn and human pass completed
before viewing model decisions). Simple kappa for include/exclude + categorical codes, weighted
kappa for the ordinal capability scale; κ ≥ 0.80 pre-registered; failure → revise instruments,
re-screen all, re-validate on a fresh 10%. All kappas reported.

**Reconciliation:** disagreements in the overlap sample reconciled only AFTER kappa computation;
human decision final, reasons recorded; systematic ambiguities amend the codebook via the
amendment log even when κ passes. Outside the overlap sample, model decisions are corrected only
by full re-runs under a revised codebook — no ad-hoc single-record edits.

**Sampling and sample size:** census of eligible records with ≥100 Scopus citations + seeded
year-stratified random sample of the remainder; target 800–1,200 coded. Fallback: eligible
corpus ≤2,000 → code all. Descriptive analysis, no power analysis; n≈1,000 gives ≤ ±3 pp
(95% CI, worst case) for proportions. Seed archived in the amendment log before sampling;
10% validation subsample (~80–120) adequate for kappa estimation.

**Screening procedure justification:** LLM + blind human validation instead of dual-human
screening (corpus scale vs. single-author feasibility; low-inference decisions; rigor via
pre-registered instruments — archived prompt, κ threshold, re-run-not-spot-fix rule). No
blinding (venue/year are study variables). Title-only search = precision at tractable scale,
recall loss quantified by registered sensitivity check. Criteria piloted on 60 records.
