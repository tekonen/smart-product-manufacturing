# Product-intelligence grading: three candidate schemes (brainstorm, 2026-07-13)

Problem (pilot finding #4): a binary "interface" code is not reproducible at the boundary.
Zhong et al. 2015 (RFID work-in-progress tracking) and Wang et al. 2016 (products as negotiating
agents) both involve "products with technology on them," yet are clearly different phenomena.
We need a graded scale where two independent coders reach the same level from the same abstract.

Design constraints: (a) anchored in established taxonomies so reviewers accept it without a fight;
(b) each level has a binary, answerable-from-text test question; (c) fast enough to apply to
~1,000 abstracts.

Anchor literature (all verified earlier in this project or canonical):
- McFarlane et al. 2003: Level 1 information-oriented vs Level 2 decision-oriented intelligent product.
- Meyer, Främling & Holmström 2009 (Computers in Industry): 3 dimensions — level of intelligence
  (information handling → problem notification → decision making), LOCATION of intelligence
  (in the object vs through the network), aggregation (item vs container).
- Porter & Heppelmann 2014 (Harvard Business Review): monitoring → control → optimization → autonomy.
- Raff, Wentzel & Obwegeser 2020 (Journal of Product Innovation Management): four archetypes —
  digital, connected, responsive, intelligent.

---

## Option 1 — Five-level ordinal scale P0–P4 (Porter & Heppelmann × Meyer hybrid) — RECOMMENDED

Assign the HIGHEST level for which the test question is answered "yes" from title+abstract
(full text on escalation). One code per paper per lifecycle phase (see "phase-split" below).

| Level | Name | Definition | Reproducible test question | Pilot example |
|---|---|---|---|---|
| **P0** | Identified | Product carries identity only; all knowledge about it lives in external systems | "Does the product contribute anything beyond an ID/location lookup key?" → **No** | Zhong et al. 2015 (RFID shop-floor tracking) |
| **P1** | Data-carrying / sensing | Product stores or measures data about itself beyond identity (history, condition, parameters) | "Does the paper describe product-borne data or product-attached sensing about the product's own state?" → Yes | product with embedded process-history memory |
| **P2** | Self-monitoring / notifying | Product (or its dedicated digital counterpart) evaluates its own state against expectations and raises events | "Does the product itself initiate a notification/alert about its own condition?" → Yes | Meyer et al.'s "problem notification" |
| **P3** | Decision-influencing | Product-borne data/logic triggers or alters decisions about the product's OWN processing or use (routing, parameters, scheduling, maintenance) | "Does a decision in the described system change as a function of product-specific state, with the product/its agent framed as the source?" → Yes | product-driven control (McFarlane) |
| **P4** | Autonomous / negotiating | Product acts as an agent with its own objective function — negotiates, self-optimizes, adapts behavior | "Does the product participate in negotiation/optimization as an actor?" → Yes | Wang et al. 2016 (products as negotiating agents) |

**Locus mapping:** D1 = interface requires **P3 or higher during the production phase**.
P1–P2 papers get a new subcode `product-as-data-carrier` (visible in results, doesn't inflate INT).
This resolves the Zhong-vs-Wang boundary cleanly: Zhong = P0, Wang = P4.

**Phase-split (recommended addition):** code the P-level twice — once for the manufacturing phase,
once for the use phase. Expected money finding: papers with high use-phase intelligence still score
P0–P1 during manufacturing, and vice versa; almost no paper is ≥P3 in both.

Pros: ordinal (supports "the field's median product is P0" statements), anchored in the two most
cited taxonomies, one code per phase, boundary cases have worked examples.
Cons: P2/P3 boundary needs care when the "product" evaluating state is actually its cloud twin
(see Option 2's location axis — partially absorbed via the flag below).

## Option 2 — Two-axis coding (Meyer et al. faithful)

Axis 1 — capability: information handling / problem notification / decision making (3 levels).
Axis 2 — location: intelligence **at the object** (embedded) vs **through the network** (twin,
cloud, platform).

Pros: manufacturing-native, directly citable to Meyer et al. 2009; the location axis captures a
real phenomenon of the digital-twin era — the product is "smart" only by proxy, its intelligence
lives in someone else's cloud, which has ownership/lock-in implications your discussion can exploit.
Cons: two codes per paper per phase (~4 codes total) — slower; 3 capability levels lose the
P0 "identified only" floor that the RFID boundary needs; coders must resolve "where does the twin
run?" which abstracts often don't say → reproducibility risk on Axis 2.

## Option 3 — Minimal three-level (passive / informational / decisional)

P0+P1 collapsed to "passive/informational-carrier", P2 folded into informational, P3+P4 = decisional.

Pros: highest inter-coder reliability, fastest at 1,000-abstract scale.
Cons: loses the monitoring→deciding transition (which is where Porter & Heppelmann's framework puts
the industry's actual frontier), and loses the P4 agent tier that makes the Wang 2016 exception
legible. Weakens the paper's conceptual contribution.

---

## DECISION (Teemu, 2026-07-13): Option 2 adopted, with two amendments

Adopted scheme — two-axis coding per lifecycle phase (manufacturing / use):

**Axis 1 — capability** (Meyer et al. 2009, amended with an explicit floor):
- **C0 none/identified-only** (amendment: preserves the RFID boundary from Option 1's P0 —
  product contributes nothing beyond an ID/location lookup key)
- **C1 information handling** (product-borne data or product-attached sensing of own state)
- **C2 problem notification** (product-initiated alerts about own condition)
- **C3 decision making** (product state/logic alters or makes decisions about its own
  processing or use)

**Axis 2 — location** (Meyer et al. 2009, amended with an honest-uncertainty category):
- **L-obj** intelligence at the object (embedded)
- **L-net** intelligence through the network (twin/cloud/platform)
- **L-unstated** (amendment: abstract does not say — code without guessing; full-text check
  only for papers that are C2+ where location matters most)

**Locus mapping:** D1 = interface requires **C3 in the manufacturing phase** (either location).
C1–C2 in manufacturing = `product-as-data-carrier` subcode.

Conservative rule retained: when two adjacent capability levels are indistinguishable from the
abstract, code the lower and flag. Weighted kappa on the capability axis; simple kappa on location.

## Recommendation (superseded by decision above; kept for audit trail)

**Option 1 (P0–P4), coded per lifecycle phase, PLUS a single binary flag borrowed from Option 2:**
`intelligence location: on-product / off-product (twin/cloud/platform) / unstated`.

That yields per paper: P-level(manufacturing), P-level(use), location flag — three quick codes that
together support the strongest findings: (a) locus histogram, (b) phase asymmetry, (c) the
"smart-by-proxy" pattern where product intelligence exists only as an off-product twin.

Reproducibility apparatus regardless of option chosen:
1. Decision tree printed in the appendix (the five test questions in order, top-down).
2. Worked boundary examples from the pilot (Zhong P0; Wang P4; a P2/P3 boundary case to be found
   during rubric freeze).
3. Rule: code what the PAPER claims the system does, not what the technology could do.
4. Rule: when the abstract is insufficient to distinguish two adjacent levels, code the LOWER level
   and flag for full-text check (conservative bias, reported).
5. 10% dual-coded sample; report Cohen's kappa (target ≥0.8) — weighted kappa for ordinal scale.
