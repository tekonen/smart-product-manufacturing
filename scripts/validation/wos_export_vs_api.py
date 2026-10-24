"""Search-scope validation: Web of Science web-interface export vs scripted API search.

Reads Teemu's Web of Science web exports (data/raw/wos_corpusA_*.xls — a WIDER query run without
the year filter), applies the registered filters step by step, and compares the surviving records
with the API search (analysis/raw/corpusA/search_results_raw.csv, rows with db == "wos") by the
unique Web of Science accession number (UT).

Registered Web of Science query: TI=(...) AND DT=(Article OR Review) AND LA=(English), PY=2012-2026.
Prints counts only (no record content), so the output is safe to paste into the validation record.

Usage:
    uv run --with pandas --with xlrd python scripts/validation/wos_export_vs_api.py [A|B]
"""
import glob
import sys
import re

import pandas as pd

CORPUS = sys.argv[1] if len(sys.argv) > 1 else "A"  # "A" or "B"
EXPORTS = sorted(glob.glob(f"data/raw/wos_corpus{CORPUS}*.xls"))
API_CSV = f"analysis/raw/corpus{CORPUS}/search_results_raw.csv"


def norm_ut(x) -> str:
    s = str(x or "").strip().upper()
    m = re.search(r"(\d{15})", s)  # WoS UT is WOS:<15 digits>
    return m.group(1) if m else ""


web = pd.concat([pd.read_excel(f, engine="xlrd") for f in EXPORTS], ignore_index=True)
web["ut"] = web["UT (Unique WOS ID)"].map(norm_ut)
print(f"Export files: {len(EXPORTS)}  rows: {len(web)}  unique UT: {web['ut'].nunique()}")
web = web.drop_duplicates("ut")

py = pd.to_numeric(web["Publication Year"], errors="coerce")
dt = web["Document Type"].fillna("").str.lower()
pt = web["Publication Type"].fillna("").str.strip().str.upper()
la = web["Language"].fillna("").str.strip().str.lower()

f_year = py.between(2012, 2026)
f_dt = dt.str.contains(r"\barticle\b|\breview\b", regex=True)
f_la = la.eq("english")
f_pt = pt.eq("J")

print("\nCumulative filters on the web export:")
print(f"  all records                                  {len(web):6d}")
print(f"  + PY 2012-2026                               {int(f_year.sum()):6d}"
      f"   (missing year: {int(py.isna().sum())})")
print(f"  + PT = J (journal)                           {int((f_year & f_pt).sum()):6d}")
reg = f_year & f_dt & f_la
print(f"  registered: PY + DT Article/Review + LA Eng  {int(reg.sum()):6d}")
print(f"  registered + PT = J                          {int((reg & f_pt).sum()):6d}")

api = pd.read_csv(API_CSV, dtype=str)
api = api[api["db"].str.lower().eq("wos")].copy()
api["ut"] = api["wos_id"].map(norm_ut)
api_ut = set(api["ut"]) - {""}
print(f"\nAPI Web of Science rows: {len(api)}  unique UT: {len(api_ut)}")

for label, mask in [("registered", reg), ("registered + PT=J", reg & f_pt)]:
    web_ut = set(web.loc[mask, "ut"]) - {""}
    only_web = web_ut - api_ut
    only_api = api_ut - web_ut
    print(f"\n[{label}] web {len(web_ut)} vs API {len(api_ut)}: "
          f"both {len(web_ut & api_ut)}, web-only {len(only_web)}, API-only {len(only_api)}")
    if only_api:
        in_export = only_api & set(web["ut"])
        print(f"  API-only: {len(in_export)} present in export but filtered out, "
              f"{len(only_api - in_export)} absent from export entirely")
        sub = web[web["ut"].isin(in_export)]
        if len(sub):
            print("    filtered-out by PT/DT/LA/PY:",
                  sub[["Publication Type", "Document Type", "Language", "Publication Year"]]
                  .astype(str).agg(" | ".join, axis=1).value_counts().to_dict())
    if only_web:
        sub = web[web["ut"].isin(only_web)]
        print("  web-only by Publication Type:", sub["Publication Type"].value_counts().to_dict())
        print("  web-only by Document Type:   ",
              sub["Document Type"].value_counts().head(6).to_dict())
        print("  web-only by year:            ",
              pd.to_numeric(sub["Publication Year"], errors="coerce")
              .value_counts().sort_index().to_dict())

# Records outside the registered window explain the original 4,199 web figure.
print("\nWeb records outside 2012-2026 or with missing year:", int((~f_year).sum()))
