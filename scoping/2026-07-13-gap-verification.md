# Scoping study: is there a "processor vs. processee" gap in smart manufacturing research?

Date: 2026-07-13. Data source: OpenAlex (open scholarly database), exact-phrase searches unless noted.
Purpose: verify/crystallize the suspected research gap before committing to a full systematic literature review (SLR).

## Suspected gap (original formulation)

Modern manufacturing research (smart manufacturing / Industry 4.0) overemphasizes making the
manufacturing process and its resources smart (the **processor**) and underemphasizes the smart
product itself (the **processee**) — its connection to lifecycle, value, and user outcomes.

## Evidence collected

### 1. Volume asymmetry (works 2010–2026, exact phrase)

| Term | Works |
|---|---|
| "smart manufacturing" | 46,666 |
| "smart factory" | 30,495 |
| "smart product" | 10,970 |
| "intelligent product" | 5,051 |
| "smart connected product" | 3,044 |

Process-side : product-side ≈ 5:1 at the crudest keyword level (terms overlap; directional only).

### 2. Trends
- "smart product": steady growth 2008→2023 (42 → 1,650/yr), **plateau/decline 2024–2025** (~1,450/yr).
- "intelligent product": still growing (767 in 2023, ~750/yr 2024–25) — much of recent volume is
  consumer/AI-product usage, not manufacturing-context usage. Needs screening.
- "product-driven control" (McFarlane et al. stream — product as active agent steering its own
  production): **tiny and never scaled** — 84 works TOTAL since 2000, peak 10/yr (2009, 2023).
  The idea of the product-as-agent inside manufacturing existed but stayed marginal while
  process-side smart manufacturing exploded.

### 3. The product-side literature EXISTS — in separate communities
The naive claim "smart products are neglected" is refutable. Verified anchor works:
- Meyer, Främling & Holmström (2009) "Intelligent Products: A survey", Computers in Industry,
  508 citations. doi:10.1016/j.compind.2008.12.005 — operations/logistics community.
- Raff, Wentzel & Obwegeser (2020) "Smart Products: Conceptual Review, Synthesis, and Research
  Directions", Journal of Product Innovation Management, 185 citations. doi:10.1111/jpim.12544
  — innovation/marketing community. Notes the literature is "scattered, lacks uniform language".
- Active adjacent streams: digital servitization (business/marketing journals), smart
  product-service systems (design/engineering), closed-loop product lifecycle management (Kiritsis).

### 4. Partial precedent for the gap claim (novelty check)
- Pessôa & Jauregui Becker (2020) "Smart design engineering: a literature review of the impact of
  the 4th industrial revolution on product design and development", Research in Engineering Design,
  doi:10.1007/s00163-020-00330-z — explicitly notes industrial-revolution research is "mostly
  associated with manufacturing systems" while the impact spans the whole value chain incl. design.
- No paper found (so far) that states the processor/processee imbalance thesis explicitly for
  smart manufacturing. Deeper novelty check still needed in Scopus before committing.

## Verdict

The gap is real but must be reframed. Not "nobody studies smart products" (false) but:

**Framing A — disconnection**: smart-manufacturing research and smart-product research are
disciplinary silos; the interface (product as information carrier/active agent during production;
feedback loops from product use back into manufacturing decisions) is underdeveloped.
Verifiable via bibliometric coupling / co-citation analysis.

**Framing B — locus of intelligence** (recommended core): within smart-manufacturing literature,
intelligence is systematically located in the process/resources, rarely in the product being made.
Verifiable by coding a PRISMA-selected sample on "where the smart resides" (processor / processee /
both), plus which outcome is optimized (process productivity vs. product lifetime value/user outcome).

**Framing C — outcome orientation** (discussion layer): the field optimizes processor productivity
metrics rather than the outcomes the product delivers over its life (analogy: healthcare optimizing
clinician productivity vs. patient outcomes). Good for motivation/implications, hard to "prove" alone.

Recommended design: systematic mapping study = bibliometric mapping (A) + structured content
coding (B), with C as the interpretive lens. This is a recognized, publishable review genre.

## Next steps
1. Deeper novelty check in Scopus (search for prior "product-centric vs process-centric" review claims).
2. Define research questions + PRISMA protocol (databases: Scopus, Web of Science, IEEE Xplore;
   search strings; inclusion/exclusion; coding scheme). Consider registering protocol on OSF.
3. Venue shortlist (DOI-issuing): Procedia CIRP conferences / IFIP Advances in Production Management
   Systems (APMS) for conference route; Journal of Manufacturing Systems, Computers in Industry,
   International Journal of Production Research, Journal of Manufacturing Technology Management for
   journal route.
