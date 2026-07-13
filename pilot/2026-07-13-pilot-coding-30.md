# Pilot coding — 30 papers (2026-07-13)

Sample: top-10 most-cited journal articles per period (2012–16, 2017–21, 2022–26) from the
Corpus A title search (OpenAlex mirror of the Scopus string). This is the **cited-core census
stratum**, not the random stratum — findings indicate what the field's most influential work does.

Coding basis: title + abstract (OpenAlex). ~40% of records lack abstracts in OpenAlex
(closed-access); those marked confidence M were coded from title + prior knowledge of these
canonical papers and MUST be re-verified against Scopus abstracts/full text before the real run.

Codes: D1 locus (PROC=processor, PRODee=processee, INT=interface, BOTH), D2 lifecycle phase,
D3 outcome, D6 type. (D4 data-flow and D5 technology noted where meaningful.) Conf = H/M/L.

## Stratum 2012–2016

| # | Paper (year, venue) | D1 | D2 | D3 | D6 | Conf |
|---|---|---|---|---|---|---|
| 1 | Wang et al. 2016, Implementing Smart Factory of Industrie 4.0 (Int. J. Distributed Sensor Networks) | PROC (note: framework includes product-carried RFID → possible INT aspects, check full text) | production | flexibility | conceptual | H |
| 2 | Wang et al. 2016, Self-organized multi-agent smart factory (Computer Networks) | **INT** — abstract confirms "smart shop-floor objects such as machines, conveyers, and products" classified as agent types with "autonomous decision and distributed cooperation"; NOTE: product agency serves factory flexibility/efficiency, not product value | production | flexibility | model | H |
| 3 | Kang et al. 2016, Smart manufacturing: past/present/future (IJPEM-GT) | PROC | production | efficiency | review | M |
| 4 | Monostori 2014, Cyber-physical Production Systems (Procedia CIRP) | PROC | production | efficiency+flexibility | conceptual | H |
| 5 | Davis et al. 2012, Smart manufacturing, manufacturing intelligence (Computers & Chemical Engineering) | PROC | production | efficiency (demand-dynamic) | conceptual | M |
| 6 | Ivanov et al. 2015, Short-term supply chain scheduling (IJPR) | PROC | production+distribution | efficiency | model | H |
| 7 | Radziwon et al. 2014, The Smart Factory (Procedia Engineering) | PROC | production | flexibility | review | H |
| 8 | Zhong et al. 2015, Big data analytics, RFID shop floor (IJPR) | PROC (logistics resources as "smart manufacturing objects"; WIP items borderline INT) | production | efficiency | method+case | H |
| 9 | O'Donovan et al. 2015, Industrial big data pipeline for maintenance (J. of Big Data) | PROC | production | efficiency (maintenance) | method | H |
| 10 | Paelke 2014, AR supporting workers (ETFA/IEEE) | PROC (human worker as resource) | production | efficiency | prototype | H |

## Stratum 2017–2021

| # | Paper | D1 | D2 | D3 | D6 | Conf |
|---|---|---|---|---|---|---|
| 11 | Tao et al. 2018, Data-driven smart manufacturing (J. Manufacturing Systems) | PROC | production | efficiency | conceptual | M |
| 12 | Wang et al. 2018, Deep learning for smart manufacturing (J. Manufacturing Systems) | PROC | production | efficiency+quality | review | M |
| 13 | Qi & Tao 2018, Digital twin and big data 360° (IEEE Access) | PROC | production | efficiency | review | H |
| 14 | Lu et al. 2019, Digital-twin-driven smart manufacturing (Robotics & CIM) | PROC | production | efficiency | review | M |
| 15 | Tao et al. 2019, Digital twins and CPS: correlation/comparison (Engineering) | PROC | production | efficiency | conceptual | M |
| 16 | Tao & Zhang 2017, Digital Twin Shop-Floor (IEEE Access) | PROC | production | efficiency | conceptual | H |
| 17 | Kusiak 2017, Smart manufacturing (IJPR) | PROC | production | efficiency | conceptual | H |
| 18 | Chen et al. 2017, Smart Factory of Industry 4.0 (IEEE Access) | PROC | production | efficiency+flexibility | conceptual+case | H |
| 19 | Zheng P. et al. 2018, Smart manufacturing systems framework (Frontiers of Mech. Eng.) | PROC (scenarios: smart design/machining/control/monitoring/scheduling — "smart design" = design *process* made smart, not product intelligence) | design+production | efficiency | conceptual | H |
| 20 | Uhlemann et al. 2017, Digital twin: realizing CPPS (Procedia CIRP) | PROC | production | efficiency (planning) | method | H |

## Stratum 2022–2026

| # | Paper | D1 | D2 | D3 | D6 | Conf |
|---|---|---|---|---|---|---|
| 21 | Li et al. 2022, Digital twin in smart manufacturing (J. Industrial Information Integration) | PROC (DT-driven green performance evaluation of manufacturing projects) | production | sustainability | framework+case | H |
| 22 | Wang B. et al. 2022, Human-centric smart manufacturing, HCPS (J. Manufacturing Systems) | PROC — **"human-centric" = worker-as-resource, not product/user** | production | efficiency+wellbeing | conceptual | M |
| 23 | Wu et al. 2022, Network slicing for IIoT (IEEE Comm. Surveys) | PROC (network infrastructure) | production | efficiency | survey | H |
| 24 | Wang J. et al. 2022, Hybrid physics/data models (J. Manufacturing Systems) | PROC (application areas incl. product design = design process) | design+production | efficiency | review | H |
| 25 | Nain et al. 2022, Edge computing in intelligent manufacturing (J. Manufacturing Systems) | PROC | production | efficiency | review | M |
| 26 | Ma et al. 2022, DT + big data sustainable smart manufacturing (Applied Energy) | PROC (mentions product lifecycle in passing) | production | sustainability | framework | H |
| 27 | Yin et al. 2022, Digital green innovation PSR framework (Systems) | — **borderline EXCLUDE**: macro/industry-level policy evaluation, not manufacturing tech | — | sustainability | model | H |
| 28 | Ryalat et al. 2023, Smart factory design, CPS+IoT (Applied Sciences) | PROC | production | flexibility | prototype | H |
| 29 | Shen & Zhang 2023, Intelligent manufacturing & pollution (J. Innovation & Knowledge) | — **borderline EXCLUDE**: city-level econometrics | — | sustainability | empirical-macro | H |
| 30 | Ahmad & Rahimi 2022, DL object detection survey (J. Manufacturing Systems) | PROC | production | quality | survey | H |

## Preliminary result (cited core, n=28 after 2 borderline exclusions)

- **D1 locus: 27/28 processor, 1/28 interface, 0/28 processee.**
- D2: 28/28 production phase only — no paper connects to use phase or end-of-life.
- D3: efficiency/flexibility/quality dominate; zero papers optimize product capability or user outcome.
- Even the "human-centric" (Industry 5.0-adjacent) turn relocates attention to the **worker as a
  production resource** — not to the product or its user. Directly parallels the healthcare analogy
  (clinician productivity vs. patient outcome): the locus never leaves the process.

This is exactly the thesis, now with a first quantified signal from the field's most-cited work.

## Rubric learnings (to fold into protocol v0.3)

1. **New exclusion criterion needed**: macro-level economics/policy studies (city/industry
   econometrics) pass the title screen — add explicit exclusion "unit of analysis is not a
   manufacturing system/technology" (papers #27, #29).
2. **Split D1 processor** into `processor-machine` and `processor-human` — captures the
   human-centric/Industry 5.0 wave separately; strengthens the argument (the field's corrective
   move went to the worker, still not the product).
3. **Abstract source**: OpenAlex lacks abstracts for ~40% of closed-access records — pull abstracts
   from Scopus records for the real screening run (they are included in Scopus API responses).
4. Borderline rule needed for RFID/work-in-progress-tracking papers (#8): tracking a product's
   location ≠ product intelligence; propose "INT requires the product to carry data or make/trigger
   decisions that alter its own processing."
5. Papers coded at confidence M (title + canonical knowledge, missing abstract) must be re-verified
   against full text before publication-grade claims — flagged in tables above.

## Re-verification of M-confidence codings (2026-07-13, same day)

All 12 missing abstracts were retrieved (Semantic Scholar by DOI: Tao 2018, Wang 2018, Lu 2019,
Tao 2019; Scopus `get_abstract_details`: Wang 2016 CN, Kang 2016, Davis 2012, Zheng 2018, Li 2022,
Wang B. 2022, Wang J. 2022, Nain 2022). Outcome:

- **All 12 D1 locus codings CONFIRMED** — every M row upgraded to H.
- Three refinements, none affecting the headline: #19 and #24 D2 → design+production ("smart
  design" in both = the design *process* made smart, not product intelligence — itself a telling
  pattern); #21 D3 → sustainability (green performance evaluation).
- #2 (the single INT paper) confirmed verbatim: products are one agent type among "machines,
  conveyers, and products". Important nuance: even here, product agency is instrumentalized for
  **factory flexibility and efficiency** — the product negotiates to optimize the process, not to
  enhance its own value or user outcome. The one exception proves the rule.
- Headline unchanged: **27/28 processor, 1/28 interface (process-serving), 0/28 processee.**

Confidence-M flag in the tables above is now obsolete; all rows H. Kept for audit trail.

## Threats to validity of this pilot
- Cited-core stratum only; the random stratum may differ (though likely MORE processor-heavy, since
  the cited core includes agenda-setting reviews that at least mention products).
- Single coder (Claude), abstracts only, 12/30 without abstract at coding time.
- OpenAlex mirror of the Scopus string; counts differ from Scopus (OpenAlex ~7,315 articles
  2012–26; Scopus expected lower).
