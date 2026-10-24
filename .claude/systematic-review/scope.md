# Scope brief — confirmed by Teemu 2026-10-24

Source of truth: the registered protocol, OSF registration https://osf.io/w9vj4/
(DOI 10.17605/OSF.IO/W9VJ4, registered 2026-10-03) and `protocol/slr-protocol-v1.0.md`.
This brief copies it verbatim; any change from it is a registration deviation and must be
logged as a dated entry in the protocol amendment log.

1. **Focal construct / scope (medium breadth):** where smart-manufacturing research locates
   intelligence — in the manufacturing process and its resources (processor) vs the product
   being made (processee) or their interface — and which outcomes it optimizes. Medium =
   papers whose TITLE names smart/intelligent manufacturing, smart factory/production,
   manufacturing 4.0, or cyber-physical production systems.
2. **Unit of analysis:** the individual peer-reviewed journal paper (article or review).
   No geographic or sectoral restriction.
3. **Research questions:** RQ1 locus of intelligence; RQ2 outcomes optimized; RQ3 citation
   integration between the smart-manufacturing and smart-product literatures; RQ4 research
   agenda. Directional expectations H1–H3 as registered. Streams are coded via the frozen
   codebook (protocol §8), not a separate `research_stream` field.
4. **Time window:** 2012–2026 inclusive. 2012 = first year after the Industrie 4.0
   announcement (Hannover Messe 2011).
5. **Journal set:** none — no tier list, no ISSN filtering (title-level search defines scope).
6. **Databases:** Scopus + Web of Science Core Collection (Expanded API). Available but
   excluded: OpenAlex, Semantic Scholar — used for scoping/pilots only; no reported figure.
7. **Exclusion criteria:** E1 not a peer-reviewed journal article/review (conference papers →
   separate sensitivity set); E2 full text not English; E3 smart manufacturing only incidental;
   E4 unit of analysis not a manufacturing system/technology (macro economics/policy);
   E5 duplicate; E6 retracted.
8. **Search keyword blocks (title-level, verbatim from registration):**
   - Corpus A (audited, coded): `TITLE("smart manufacturing" OR "intelligent manufacturing" OR
     "smart factory" OR "smart production" OR "manufacturing 4.0" OR "cyber-physical production
     system*")` AND journal articles/reviews, English, journal source type.
   - Corpus B (RQ3 reference corpus, not coded): `TITLE("smart product*" OR "intelligent
     product*" OR "smart connected product*" OR "product-driven" OR "product avatar" OR
     "smart product-service")`, same filters.
   - Web of Science mirrors: same terms via `TI=`, 2012–2026, Article + Review, English.

Preregistration: done (OSF w9vj4, 2026-10-03). Screening has not begun.
