# Patch: academic-research plugin 0.5.12 — allow searches without a journal filter

Applied 2026-10-24. The plugin cache is overwritten on plugin updates; re-apply after any update
(check the version folder under `~/.claude/plugins/cache/mronkko/academic-research/`).

**Why:** the shipped Scopus and Web of Science searchers always append a journal ISSN filter
(`ISSN(...)` / `IS=(...)`). This review's registered design (OSF w9vj4) is title-scoped with no
journal list, so an empty `JOURNALS = {}` produced a malformed query. The patch skips the journal
clause only when the list is empty; behaviour is unchanged for journal-filtered reviews.
Candidate for upstreaming to the plugin author.

## scripts/pipelines/searchers/scopus.py — `_full_query`

```python
    def _full_query(self, core: str, ctx: SearchContext) -> str:
        years = f"PUBYEAR > {ctx.from_year - 1} AND PUBYEAR < {ctx.to_year + 1}"
        if not ctx.issns:  # no journal list -> no journal filter (title-scoped designs)
            return f"{core} AND {years}"
        issn_part = " OR ".join(ctx.issns)
        return f"{core} AND ISSN({issn_part}) AND {years}"
```

## scripts/pipelines/searchers/wos.py — `_full_query`

```python
    def _full_query(self, core: str, ctx: SearchContext) -> str:
        if not ctx.issns:  # no journal list -> no journal filter (title-scoped designs)
            return f"{core} AND PY={ctx.from_year}-{ctx.to_year}"
        issn_part = " OR ".join(ctx.issns)
        return f"{core} AND IS=({issn_part}) AND PY={ctx.from_year}-{ctx.to_year}"
```
