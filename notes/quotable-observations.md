# Quotable observations from the pilots (collected 2026-07-14)

Material for the paper's narrative — each observation illustrates the locus-of-intelligence thesis
with a concrete, citable case. Quotes are verbatim from the retrieved abstracts (Scopus/Semantic
Scholar/OpenAlex records); paraphrases are marked. Pilot row references point to
`pilot/2026-07-13-pilot-coding-30.md` (P1) and `pilot/2026-07-13-pilot2-random-30.md` (P2).

---

## 1. The exception that proves the rule: product agency, but in service of the factory

Wang, S., Wan, J., Zhang, D., Li, D., & Zhang, C. (2016). Towards smart factory for industry 4.0:
A self-organized multi-agent system with big data based feedback and coordination.
*Computer Networks*, 101, 158–168. https://doi.org/10.1016/j.comnet.2015.12.017 — P1 #2.

The ONLY interface-locus paper in 46 coded (both pilots). Products are agents:
> "…a smart factory framework that incorporates industrial network, cloud, and supervisory control
> terminals with smart shop-floor objects such as machines, conveyers, and products."
> "The autonomous decision and distributed cooperation between agents lead to high flexibility."

But the objective function is the factory's: "high flexibility… high efficiency." The product
negotiates to optimize the process — its own lifetime value and user never appear.

## 2. The worker gets a negotiating digital twin; the product never does

Graessler, I., & Poehler, A. (2017). Integration of a digital twin as human representation in a
scheduling procedure of a cyber-physical production system. *2017 IEEE International Conference on
Industrial Engineering and Engineering Management (IEEM)*.
https://doi.org/10.1109/IEEM.2017.8289898 — P2 conference sensitivity set.

> "The interconnection and negotiation among the devices open up possibilities for a new kind of
> integration of human employees…"

Agency is progressively extended from machines to humans — the processee is skipped. Strong paired
with observation 1: the field grants negotiating power to every actor in the factory except the
thing being made.

## 3. "Human-centric" relocates attention to the worker-as-resource, not to the product or its user

Wang, B., Zheng, P., Yin, Y., Shih, A., & Wang, L. (2022). Toward human-centric smart
manufacturing: A human-cyber-physical systems (HCPS) perspective. *Journal of Manufacturing
Systems*, 63, 471–490. https://doi.org/10.1016/j.jmsy.2022.05.005 — P1 #22.

> "Advances in human-centric smart manufacturing (HSM) reflect a trend towards the integration of
> human-in-the-loop with technologies, to address challenges of human-machine relationships."

The field's own corrective turn (Industry 5.0 wave) moves the locus from machine to worker —
still a production resource. Directly parallel to the healthcare framing: optimizing clinician
productivity is not the same as optimizing patient outcomes. Earliest random-sample instance of
the same pattern: Zamfirescu, C.-B., Pârvu, B.-C., Schlick, J., & Zühlke, D. (2013). Preliminary
insides [sic] for an anthropocentric cyber-physical reference architecture of the smart factory.
*Studies in Informatics and Control*, 22(3). https://doi.org/10.24846/v22i3y201303 — P2.

## 4. "Smart design" means the design PROCESS made smart — not an intelligent product

Zheng, P., Wang, H., Sang, Z., Zhong, R. Y., Liu, Y., Liu, C., Mubarok, K., Yu, S., & Xu, X.
(2018). Smart manufacturing systems for Industry 4.0: Conceptual framework, scenarios, and future
perspectives. *Frontiers of Mechanical Engineering*, 13(2), 137–150.
https://doi.org/10.1007/s11465-018-0499-5 — P1 #19.

> "…demonstrative scenarios that pertain to smart design, smart machining, smart control, smart
> monitoring, and smart scheduling…"

Every "smart X" in the canonical scenario list is a process activity. Useful against the objection
"but the field does cover design": it covers *designing*, not the designed artifact's intelligence.

## 5. Even end-of-life products are passive material flowing through a smart process

Jun, C., Lee, J. Y., Kim, B. H., & Noh, S. D. (2017). Application of core technologies for smart
manufacturing: A case study of cost benefit analysis based on modeling and simulation for
sustainability. *2017 Winter Simulation Conference (WSC)*.
https://doi.org/10.1109/WSC.2017.8248161 — P2 conference sensitivity set.

Material Flow Cost Accounting simulation of vehicle-recycling factories (paraphrase): the
circular-economy setting par excellence, yet the end-of-life vehicle appears only as material to
be processed — no product-borne history, no product data informing its own disassembly. If smart
products carried their lifecycle data, exactly this application would be transformed.

## 6. Tracking is not intelligence: the C0 boundary case

Zhong, R. Y., Xu, C., Chen, C., & Huang, G. Q. (2015). Big Data Analytics for Physical
Internet-based intelligent manufacturing shop floors. *International Journal of Production
Research*, 53(2). https://doi.org/10.1080/00207543.2015.1086037 — P1 #8.

> "…typical logistics resources are converted into smart manufacturing objects (SMOs) using
> Internet of Things (IoT) and wireless technologies…"

"Smart objects" here = RFID-tagged, externally tracked. All analytics happen in the shop-floor
system; the object contributes an ID. Canonical worked example for capability level C0 in the
codebook (contrast with observation 1 = C3).

## 7. Product data flows into process models — the product itself stays inert

Wuest, T. (2024). Hybrid analytics in smart manufacturing systems — addressing the manufacturing
data challenge. *Smart and Sustainable Manufacturing Systems*, 8(1).
https://doi.org/10.1520/ssms20230015 — P2.

> "Smart manufacturing has opened tremendous opportunities to access, collect, and analyze a
> plethora of process and product data."

Product data is raised, then consumed entirely by process-side models. Illustrates the D4
data-flow code (product→process) coexisting with capability C0: the product is a data *subject*,
never a data *carrier* or decision participant.

## 8. Production-phase tunnel vision even when "product lifecycle" is invoked

Ma, S., Ding, W., Liu, Y., Ren, S., & Yang, H. (2022). Digital twin and big data-driven
sustainable smart manufacturing based on information management systems for energy-intensive
industries. *Applied Energy*, 326, 119986. https://doi.org/10.1016/j.apenergy.2022.119986 — P1 #26.

> "…sustainable smart manufacturing enables lower cost, higher productivity and flexibility,
> better quality and sustainability during the product lifecycle management."

"Product lifecycle" appears in the abstract; the system described optimizes energy in production.
Example of lifecycle vocabulary without lifecycle scope — supports the D2 finding (28/28 cited-core
papers stop at the production phase).

## 9. Aggregate statistics (for the results narrative)

- Combined pilots, n=46 coded: **45 processor / 1 interface / 0 processee**; cited core additionally
  28/28 production-phase-only; random stratum 18/18 capability C0.
- "Product-driven control" stream (McFarlane et al. lineage): 84 works total since 2000 (OpenAlex,
  exact phrase, 2026-07-13) — the product-as-agent idea predates Industry 4.0 and never scaled.
- Crude corpus asymmetry 2010–2026: "smart manufacturing"+"smart factory" ≈ 77k works vs.
  "smart product"+"intelligent product"+"smart connected product" ≈ 19k (OpenAlex exact phrase;
  use Scopus figures in the paper).

## Verification status

Quotes in §1–§8 are from retrieved abstracts, verbatim except where marked paraphrase. Before
manuscript submission: re-check each quote against the publisher full text (abstracts occasionally
differ between indexes), and replace OpenAlex-derived counts in §9 with Scopus equivalents.
