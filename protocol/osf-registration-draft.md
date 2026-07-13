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
