# Protocol v1.0 (FROZEN 2026-07-14) — Systematic mapping study

**Where does the smart reside? A systematic mapping of the locus of intelligence in smart
manufacturing research**

Consolidates protocol v0.1–v0.5 (decision history in `slr-protocol-v0.1.md`, kept as audit trail).
No open decisions. Changes after OSF registration require a dated amendment section, never edits
to this text.

---

## 1. Background and rationale

Smart manufacturing research has grown explosively since ~2012, but scoping evidence
(`scoping/2026-07-13-gap-verification.md`) indicates the field locates intelligence in the
manufacturing process and its resources — machines, scheduling, factories, and lately the worker
(the **processor**) — rather than in the product being made (the **processee**), its lifecycle,
and the outcomes it delivers to users. The product-as-agent idea (product-driven control,
intelligent products: McFarlane et al.; Meyer, Främling & Holmström 2009) predates Industry 4.0
but stayed marginal (~84 works since 2000), while product-side streams (smart products in
innovation research: Raff et al. 2020; smart product-service systems: Zheng et al. 2019; digital
servitization) evolved in separate communities. No prior review audits the smart-manufacturing
literature on this dimension (novelty verified in Scopus, 2026-07-13). Two pilots (n=46 coded)
support feasibility and the expected signal: 45 processor / 1 interface / 0 processee.

## 2. Research questions

- **RQ1 (locus):** Where does smart manufacturing research locate intelligence — in the process
  and its resources (machine or human), in the product being manufactured, or at their interface?
- **RQ2 (outcome):** Which outcomes does the research optimize — process outcomes (efficiency,
  conformance quality, flexibility) or product-value/user outcomes?
- **RQ3 (integration):** To what extent do the smart-manufacturing and smart-product literatures
  cite each other? Hypothesis: cross-corpus citation share <5%, flat over time.
- **RQ4 (agenda):** What research opportunities follow, in particular products that remain
  intelligent during their own manufacture and connect production to lifecycle value?

## 3. Design

Systematic mapping study (Petersen, Vakkalanka & Kuzniarz 2015) reported per PRISMA 2020
(Preferred Reporting Items for Systematic Reviews and Meta-Analyses: flow diagram + checklist).
Registered on OSF before full screening (draft: `osf-registration-draft.md`).

## 4. Data sources

1. **Scopus** — primary: record retrieval, abstracts, document-type filtering, and the RQ3
   cited-reference exports.
2. **Web of Science Core Collection** — second screening database (institutional access via
   university VPN, confirmed).

IEEE Xplore excluded: criteria are journal-articles-only and IEEE journals are indexed in both
databases; Xplore would contribute only excluded conference material. OpenAlex was used for
scoping and pilots only and contributes no reported figure.

## 5. Search strategy

**Corpus A — smart manufacturing (audited corpus), Scopus advanced query:**

```
TITLE("smart manufacturing" OR "intelligent manufacturing" OR "smart factory"
  OR "smart production" OR "manufacturing 4.0" OR "cyber-physical production system*")
AND PUBYEAR > 2011 AND PUBYEAR < 2027
AND (DOCTYPE(ar) OR DOCTYPE(re)) AND LANGUAGE(english) AND SRCTYPE(j)
```

**Corpus B — smart/intelligent products (RQ3 reference corpus, not coded):**

```
TITLE("smart product*" OR "intelligent product*" OR "smart connected product*"
  OR "product-driven" OR "product avatar" OR "smart product-service")
AND PUBYEAR > 2011 AND PUBYEAR < 2027
AND (DOCTYPE(ar) OR DOCTYPE(re)) AND LANGUAGE(english) AND SRCTYPE(j)
```

Web of Science mirror queries: same terms via `TI=`, timespan 2012–2026, document types
Article + Review, language English. Title-level search is a deliberate mapping-study choice;
recall loss quantified by sensitivity check (§9.2).

## 6. Eligibility criteria

**Include:** peer-reviewed journal articles and reviews; English; primary focus on
smart/intelligent manufacturing (technology, system, method, framework, or management thereof);
2012–2026.

**Exclude:** conference papers (retained separately as a sensitivity set), editorials, book
chapters; non-English full text; incidental-context papers (the search term is title decoration,
e.g., pilot-2 SD-card firmware case); **macro-level economics/policy studies whose unit of
analysis is not a manufacturing system/technology** (city/region/industry econometrics);
repository preprints; duplicates and retracted items.

## 7. Screening and sampling

1. Export both corpora from Scopus and Web of Science (CSV; see `data/EXPORT-INSTRUCTIONS.md`);
   merge and deduplicate by DOI + fuzzy title.
2. Screening and coding basis: Scopus abstracts (Semantic Scholar by DOI as fallback). OpenAlex
   abstracts are not used (≈40% missing for closed-access records).
3. LLM-assisted screening (Claude codes all sampled records) with human validation (§9.3).
4. **Sampling for coding:** census of all records with ≥100 Scopus citations (influential core)
   + seeded random sample without replacement from the remainder, stratified by year, target
   n≈800–1,200 coded in total. Both strata reported separately.

## 8. Coding scheme (frozen)

| Code | Values | Notes |
|---|---|---|
| **D1 locus of intelligence** | processor-machine / processor-human / processee / interface / both | interface requires capability **C3 in the manufacturing phase**; C1–C2 in manufacturing = subcode `product-as-data-carrier` |
| **D1b capability** (Meyer et al. 2009, amended) | C0 identified-only / C1 information handling / C2 problem notification / C3 decision making | coded **twice**: manufacturing phase and use phase; assign highest level supported by the text; when adjacent levels indistinguishable, code the lower and flag |
| **D1c location** (Meyer et al. 2009, amended) | L-obj (at the object) / L-net (through network/twin/cloud) / L-unstated | **conditional: coded only when capability ≥ C1** |
| **D2 lifecycle phase** | design / production / distribution / use / end-of-life / multiple | |
| **D3 outcome optimized** | process efficiency / conformance quality / flexibility & customization / product capability or user outcome / sustainability / other | |
| **D4 data-flow direction** | within-process / product→process / process→product / bidirectional | |
| **D5 enabling technology** | free-coded, clustered post hoc | |
| **D6 research type** | conceptual / model or method / case study / survey / review | |

Worked boundary examples in the codebook: Zhong et al. 2015 = C0 (RFID tracking is not product
intelligence); Wang et al. 2016 = C3 (products negotiate as agents). Rule: code what the paper
claims the system does, not what the technology could do.

## 9. Validity threats and mitigations (no per-study quality appraisal — mapping-study genre)

1. **Database coverage** — two-database union; report overlap % and unique contributions.
2. **Title-search recall** — sensitivity check: one sample year re-run as TITLE-ABS-KEY; screen
   the extra records; report the miss rate and whether missed papers differ on D1.
3. **LLM coding validity** — blind human dual-coding of a random 10%; weighted Cohen's kappa
   (capability axis), simple kappa (locus, location); threshold ≥0.8; below → revise codebook,
   recode all, re-validate. Kappas, codebook, and decision tree published.
4. **Single primary coder** — mitigated by (3) + published decision-tree codebook; acknowledged.

## 10. Synthesis and outputs

1. PRISMA 2020 flow diagram (exclusion counts per criterion).
2. Locus over time (D1 × year) — is the field drifting toward the product, or only machine→human?
3. **Locus × outcome (D1 × D3) heatmap — central evidence figure.**
4. Capability profile (C0–C3 × phase); location breakdown for the C1+ subset.
5. Locus × venue — where the rare interface/processee papers publish.
6. RQ3: bibliographic coupling map + cross-corpus citation share from Scopus cited-reference
   exports (VOSviewer or bibliometrix); OpenAlex in no reported figure.
7. Narrative synthesis + research agenda (RQ4) generated from the empty cells of outputs 3–4.

## 11. Publication plan

1. **Conference (2027):** Procedia CIRP (CIRP Conference on Manufacturing Systems or CIRP Design)
   — condensed scope: scoping evidence + pilot + cited-core census + reference-list-level RQ3.
2. **Journal (extended):** Journal of Manufacturing Systems / Computers in Industry /
   International Journal of Production Research — full random-stratum coding + full coupling map.

## 12. Positioning (must-cite prior work)

- Pessôa & Jauregui Becker 2020, Research in Engineering Design (closest precedent; design-process
  focus, not locus audit). doi:10.1007/s00163-020-00330-z
- Zheng et al. 2019, Advanced Engineering Informatics (smart product-service systems survey).
  doi:10.1016/j.aei.2019.100973
- Raff, Wentzel & Obwegeser 2020, Journal of Product Innovation Management. doi:10.1111/jpim.12544
- Meyer, Främling & Holmström 2009, Computers in Industry (capability/location scheme source).
  doi:10.1016/j.compind.2008.12.005
- Liu et al. 2026, Advanced Engineering Informatics (check scope overlap at publication).
  doi:10.1016/j.aei.2026.104534

## 13. Supporting documents

- Decision history: `slr-protocol-v0.1.md` (v0.1–v0.5 with rationale per change)
- Coding-scheme derivation: `intelligence-scale-options.md`
- Pilots: `../pilot/2026-07-13-pilot-coding-30.md`, `../pilot/2026-07-13-pilot2-random-30.md`
- Scoping: `../scoping/2026-07-13-gap-verification.md`
- Narrative material: `../notes/quotable-observations.md`
- OSF registration draft: `osf-registration-draft.md`
- Export procedure: `../data/EXPORT-INSTRUCTIONS.md`

---

## Amendment log (additions only; the frozen text above is never edited)

- **2026-07-14 — Registration infrastructure.** Public repository:
  https://github.com/tekonen/smart-product-manufacturing (tag `protocol-v1.0`, commit `3d0b7dd`).
  OSF project: https://osf.io/sz3d2/ (public; GitHub add-on connected). OSF *registration*
  pending submission — this entry will be amended with the registration URL and date once
  submitted. Screening has not begun.
