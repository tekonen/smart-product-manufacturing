# Database export instructions (run over university VPN, 2026-07-14)

Deposit all files in `data/raw/` with the exact names below. After they exist, Claude runs
merge + deduplication + the seeded random sample and reports the PRISMA identification numbers.

## 1. Scopus — Corpus A records

1. scopus.com → Advanced document search → paste:
   ```
   TITLE("smart manufacturing" OR "intelligent manufacturing" OR "smart factory" OR "smart production" OR "manufacturing 4.0" OR "cyber-physical production system*") AND PUBYEAR > 2011 AND PUBYEAR < 2027 AND (DOCTYPE(ar) OR DOCTYPE(re)) AND LANGUAGE(english) AND SRCTYPE(j)
   ```
2. Record the total count and the search date (goes into the PRISMA diagram).
3. Select all → Export → **CSV** → field set: Citation information + Abstract & keywords +
   **Include references** (needed for RQ3, Option C). Scopus caps CSV-with-references exports at
   ~2,000 records/batch → split by year ranges (e.g., 2012–2018 / 2019–2021 / 2022–2024 /
   2025–2026) so each batch stays under the cap.
4. Filenames: `scopus_corpusA_<years>.csv` (e.g., `scopus_corpusA_2012-2018.csv`).

## 2. Scopus — Corpus B records (RQ3 reference corpus)

Same procedure with:
```
TITLE("smart product*" OR "intelligent product*" OR "smart connected product*" OR "product-driven" OR "product avatar" OR "smart product-service") AND PUBYEAR > 2011 AND PUBYEAR < 2027 AND (DOCTYPE(ar) OR DOCTYPE(re)) AND LANGUAGE(english) AND SRCTYPE(j)
```
References included here too (needed for the reverse citation-share direction).
Filenames: `scopus_corpusB_<years>.csv`.

## 3. Web of Science — both corpora (screening cross-check, no references needed)

1. webofscience.com → Core Collection → Advanced search:
   ```
   TI=("smart manufacturing" OR "intelligent manufacturing" OR "smart factory" OR "smart production" OR "manufacturing 4.0" OR "cyber-physical production system*")
   ```
   Refine: Publication years 2012–2026; Document types Article, Review; Language English.
2. Export → **Excel or Tab-delimited** → "Full Record" (cited references NOT needed from WoS —
   RQ3 uses Scopus references only). Batch limit 1,000 records → export in chunks
   `wos_corpusA_<n>.xls`.
3. Repeat with `TI=("smart product*" OR "intelligent product*" OR "smart connected product*" OR "product-driven" OR "product avatar" OR "smart product-service")` → `wos_corpusB_<n>.xls`.
4. Record totals + search date.

## 4. Sensitivity-check export (small, do last)

Scopus, one sample year (2019), TITLE-ABS-KEY variant of the Corpus A query, CSV without
references → `scopus_corpusA_sensitivity_2019_titleabskey.csv`. Used to quantify title-search
recall loss (protocol §9.2).

## What Claude runs at merge time (registered commitments)

1. **Known-item validation (blocking):** confirm the merged Corpus A contains all five canonical
   papers listed in the protocol v1.0 amendment log (Kang 2016, Kusiak 2017, Tao 2018,
   Monostori 2014, Wang 2016 — by DOI). Any miss blocks screening: revise string, re-export,
   log the revision.
2. Batch-truncation reconciliation (per-year counts vs. export files).
3. Deduplication (DOI + fuzzy title) across Scopus and Web of Science; report overlap % and
   unique contributions per database.
4. Seeded random sample (seed = ISO date of merge run, archived in the amendment log) +
   ≥100-citation census stratum.
5. PRISMA identification numbers reported back.

## Notes

- Keep the Scopus result page's exact total per query — the PRISMA "records identified" numbers
  must match the export files.
- If a batch export silently truncates (Scopus does this occasionally), the per-year counts
  won't reconcile — Claude checks this automatically at merge time.
- Random-sample seed will be fixed as the ISO date of the merge run and archived in the protocol
  amendment log before sampling.
