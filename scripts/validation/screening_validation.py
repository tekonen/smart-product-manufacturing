#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyzotero>=1.6", "httpx>=0.25", "tenacity>=8.0", "pandas>=2", "xlrd>=2", "openpyxl>=3"]
# ///
"""Registered screening-validation steps the academic-research plugin does not ship.

Three subcommands, run in this order (registered in OSF w9vj4 and protocol §7 / §9.3):

  prescreen  Remove records BEFORE screening (PRISMA "records removed before screening"):
             E1 = Web of Science records whose publication type is book / book series
                  (S/B — "Article; Book Chapter"), which the Zotero import stores as journal
                  articles; matched by DOI, else normalized title, to the WoS web export.
             E6 = retracted items, as placed by Teemu in the Zotero collection "E6 retracted".
             Tags each item `prescreen:E1|E6` + `abstract:exclude` (+ `retracted:flag` for E6),
             so the plugin's abstract_screen.py skips them. Dry run unless --apply.
  sample     Draw the blind human-validation sample: seeded random 10% (rounded up) of the
             screening pool (Corpus A minus prescreen exclusions). Refuses to run if any pool
             item already carries a model decision tag (blinding guard). Writes a blinded sheet
             (title, abstract, year, venue only) to screening/ (gitignored: abstracts are
             licensed) and a key-only manifest with the seed to analysis/validation/ (committed
             BEFORE the human pass, so the sample cannot be redrawn after the fact).
  kappa      After the model has screened: Cohen's kappa between Teemu's sheet and the model's
             last decision per item (screening/abstract_screening.csv). Primary, registered
             statistic: binary exclude vs proceed (include + borderline), threshold >= 0.80.
             Also reports the 3-class kappa. Writes counts-only report to analysis/validation/.

Zotero access goes through the plugin's own zotero_io module (never direct HTTP).

Usage (from the project root; VPN not needed):
  uv run scripts/validation/screening_validation.py prescreen [--apply]
  uv run scripts/validation/screening_validation.py sample [--seed YYYYMMDD]
  uv run scripts/validation/screening_validation.py kappa --sheet <path.csv|.xlsx>
"""
from __future__ import annotations

import argparse
import datetime as dt
import glob
import json
import math
import os
import random
import re
import sys
from collections import Counter
from pathlib import Path

GROUP = "6732772"          # Zotero "Smart Products" — canonical record in CLAUDE.md
CORPUS_A = "5KWXUAKK"      # Corpus A collection key
E6_COLLECTION_NAME = "E6 retracted"
WOS_EXPORTS = "data/raw/wos_corpusA*.xls"
LOG = Path("screening/abstract_screening.csv")
SHEET = Path("screening/human_validation_sample.csv")
OUT = Path("analysis/validation")
THRESHOLD = 0.80
VALID = ("include", "borderline", "exclude")


def _plugin_pipelines() -> Path:
    env = os.environ.get("ACADEMIC_RESEARCH_PIPELINES")
    if env:
        return Path(env)
    base = Path.home() / ".claude/plugins/cache/mronkko/academic-research"
    versions = sorted(base.glob("*/scripts/pipelines"),
                      key=lambda p: [int(x) if x.isdigit() else x
                                     for x in re.split(r"[.]", p.parts[-3])])
    if not versions:
        sys.exit("academic-research plugin not found; set ACADEMIC_RESEARCH_PIPELINES")
    return versions[-1]


_PIPE = _plugin_pipelines()
sys.path[:0] = [str(_PIPE), str(_PIPE.parent)]  # pipelines/ and scripts/ (core.*)
import zotero_io  # noqa: E402


def client() -> "zotero_io.ZoteroClient":
    return zotero_io.ZoteroClient.from_config(GROUP, prefer_local=False)


def norm_doi(x) -> str:
    s = str(x or "").strip().lower()
    s = re.sub(r"^https?://(dx\.)?doi\.org/", "", s)
    return s if s.startswith("10.") else ""


def norm_title(x) -> str:
    return re.sub(r"[^a-z0-9]", "", str(x or "").lower())


def tags_of(item: dict) -> set[str]:
    return {t.get("tag", "") for t in item.get("data", {}).get("tags", [])}


def corpus_items(z) -> list[dict]:
    return z.collection_items(CORPUS_A)


# ---------------------------------------------------------------- prescreen
def cmd_prescreen(args) -> None:
    import pandas as pd

    z = client()
    items = corpus_items(z)
    by_doi = {norm_doi(i["data"].get("DOI")): i["key"] for i in items if norm_doi(i["data"].get("DOI"))}
    by_title = {norm_title(i["data"].get("title")): i["key"] for i in items}
    print(f"Corpus A items: {len(items)}")

    # E1 — WoS book / book-series records within the registered WoS filters.
    files = sorted(glob.glob(WOS_EXPORTS))
    web = pd.concat([pd.read_excel(f, engine="xlrd") for f in files], ignore_index=True)
    py = pd.to_numeric(web["Publication Year"], errors="coerce")
    dtyp = web["Document Type"].fillna("").str.lower()
    reg = (py.between(2012, 2027)  # 2027 = online-2026 issues retained by the API search
           & dtyp.str.contains(r"\barticle\b|\breview\b", regex=True)
           & web["Language"].fillna("").str.strip().str.lower().eq("english"))
    nonj = web[reg & web["Publication Type"].fillna("").str.strip().str.upper().isin(["S", "B"])]
    nonj = nonj.drop_duplicates("UT (Unique WOS ID)")
    e1, e1_unmatched = {}, []
    for _, r in nonj.iterrows():
        k = by_doi.get(norm_doi(r.get("DOI"))) or by_title.get(norm_title(r.get("Article Title")))
        (e1.__setitem__(k, r.get("Article Title")) if k else e1_unmatched.append(r.get("Article Title")))
    print(f"E1 book/book-series records in WoS export: {len(nonj)}; matched in Zotero: {len(e1)}; "
          f"unmatched: {len(e1_unmatched)}")

    # E6 — retracted items, from Teemu's Zotero collection.
    colls = {c["data"]["name"]: c["key"] for c in z.cloud.everything(z.cloud.collections())}
    if E6_COLLECTION_NAME not in colls:
        sys.exit(f'Collection "{E6_COLLECTION_NAME}" not found in group {GROUP} — create it first.')
    e6_items = z.collection_items(colls[E6_COLLECTION_NAME])
    corpus_keys = {i["key"] for i in items}
    e6 = {i["key"]: i["data"].get("title") for i in e6_items if i["key"] in corpus_keys}
    print(f'E6 retracted (collection "{E6_COLLECTION_NAME}"): {len(e6_items)}; in Corpus A: {len(e6)}')

    overlap = set(e1) & set(e6)
    if overlap:
        print(f"  {len(overlap)} item(s) are both E1 and E6 — counted once, under E6.")
        for k in overlap:
            e1.pop(k)

    manifest = {
        "generated": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "corpus_a_items": len(items),
        "E1_non_journal": sorted(e1), "E1_unmatched_titles": e1_unmatched,
        "E6_retracted": sorted(e6),
        "screening_pool": len(items) - len(e1) - len(e6),
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "prescreen_exclusions.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Screening pool after prescreen: {manifest['screening_pool']}")
    print(f"Manifest: {OUT / 'prescreen_exclusions.json'}")

    if not args.apply:
        print("\n[DRY RUN] no Zotero tags written. Re-run with --apply.")
        return
    updates = [(k, {"add": ["prescreen:E1", "abstract:exclude"]}) for k in e1]
    updates += [(k, {"add": ["prescreen:E6", "retracted:flag", "abstract:exclude"]}) for k in e6]
    stats = z.batch_update_tags(updates)
    print(f"Tags applied: {stats}")


# ------------------------------------------------------------------- sample
def cmd_sample(args) -> None:
    z = client()
    items = corpus_items(z)
    pool, model_tagged = [], []
    for i in items:
        t = tags_of(i)
        if any(x.startswith("prescreen:") for x in t):
            continue
        if any(x.startswith("abstract:") for x in t):
            model_tagged.append(i["key"])
        pool.append(i)
    if model_tagged:
        sys.exit(f"BLINDING GUARD: {len(model_tagged)} pool items already carry model abstract:* "
                 f"tags. The human sample must be drawn before model screening.")
    seed = args.seed or int(dt.date.today().strftime("%Y%m%d"))
    keys = sorted(i["key"] for i in pool)
    n = math.ceil(0.10 * len(keys))
    chosen = sorted(random.Random(seed).sample(keys, n))
    by_key = {i["key"]: i["data"] for i in pool}

    import csv
    SHEET.parent.mkdir(parents=True, exist_ok=True)
    with SHEET.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["item_key", "title", "abstract", "year", "venue",
                    "human_decision", "human_code", "human_notes"])
        for k in chosen:
            d = by_key[k]
            w.writerow([k, d.get("title", ""), d.get("abstractNote", ""),
                        str(d.get("date", ""))[:4], d.get("publicationTitle", ""), "", "", ""])
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = {"drawn": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                "seed": seed, "method": "random.Random(seed).sample(sorted(pool_keys), ceil(0.10*N))",
                "pool_size": len(keys), "sample_size": n, "sample_keys": chosen}
    (OUT / "human_sample_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Pool {len(keys)} → sample {n} (seed {seed}).")
    print(f"Blinded sheet: {SHEET}  (fill human_decision = include|borderline|exclude,")
    print(f"               human_code = I1-I3/E1-E4 as in protocol/screening-prompt.md)")
    print(f"Manifest (commit BEFORE screening): {OUT / 'human_sample_manifest.json'}")


# -------------------------------------------------------------------- kappa
def kappa(a: list[str], b: list[str]) -> float:
    n = len(a)
    labels = sorted(set(a) | set(b))
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = Counter(a), Counter(b)
    pe = sum(ca[l] * cb[l] for l in labels) / (n * n)
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


def cmd_kappa(args) -> None:
    import csv
    import pandas as pd

    manifest = json.loads((OUT / "human_sample_manifest.json").read_text())
    sheet = (pd.read_excel(args.sheet) if str(args.sheet).endswith((".xlsx", ".xls"))
             else pd.read_csv(args.sheet, dtype=str))
    human = {r.item_key: str(r.human_decision).strip().lower() for r in sheet.itertuples()}
    model = {}
    with LOG.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("decision") in VALID:
                model[row["item_key"]] = row["decision"]
    keys = manifest["sample_keys"]
    bad = [k for k in keys if human.get(k) not in VALID]
    missing = [k for k in keys if k not in model]
    if bad or missing:
        sys.exit(f"Incomplete: {len(bad)} sample rows without a valid human decision, "
                 f"{len(missing)} without a model decision.")
    h = [human[k] for k in keys]
    m = [model[k] for k in keys]
    bin_ = lambda v: "exclude" if v == "exclude" else "proceed"  # noqa: E731
    k_bin = kappa([bin_(x) for x in h], [bin_(x) for x in m])
    k3 = kappa(h, m)
    confusion = Counter(zip(h, m))
    report = {"computed": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
              "n": len(keys), "seed": manifest["seed"],
              "kappa_binary_exclude_vs_proceed": round(k_bin, 4),
              "kappa_3class": round(k3, 4), "threshold": THRESHOLD,
              "passes_registered_threshold": k_bin >= THRESHOLD,
              "confusion_human_by_model": {f"{a}|{b}": c for (a, b), c in sorted(confusion.items())}}
    (OUT / "kappa_report.json").write_text(json.dumps(report, indent=2) + "\n")
    with Path("screening/kappa_disagreements.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["item_key", "human", "model"])
        for k, a, b in zip(keys, h, m):
            if a != b:
                w.writerow([k, a, b])
    print(json.dumps(report, indent=2))
    print("PASS" if k_bin >= THRESHOLD else "FAIL — revise prompt, re-screen all, re-validate on a fresh 10%")


def main() -> None:
    os.chdir(Path(__file__).resolve().parents[2])
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("prescreen"); a.add_argument("--apply", action="store_true")
    b = sub.add_parser("sample"); b.add_argument("--seed", type=int)
    c = sub.add_parser("kappa"); c.add_argument("--sheet", default=str(SHEET))
    args = p.parse_args()
    {"prescreen": cmd_prescreen, "sample": cmd_sample, "kappa": cmd_kappa}[args.cmd](args)


if __name__ == "__main__":
    main()
