# Contributing to Awesome GEO & AEO

Thank you for helping keep **Awesome GEO & AEO** accurate, empirical, and vendor-neutral!

## What Belongs Here

1. **Peer-Reviewed Papers & Preprints**: Academic work on Generative Engine Optimization (GEO), Answer Engine Optimization (AEO), search-grounded RAG query planning, citation attribution, or knowledge conflict resolution. Include venue/year, authors, canonical arXiv/OpenReview/ACL/ACM URL, and a concise 1–2 sentence technical summary.
2. **Official Crawler & Protocol Updates**: Verifiable changes to `User-Agent` tokens, IP CIDR feeds, `robots.txt` policies, `llms.txt` conventions, or `Schema.org` guidance from AI search operators—always accompanied by an official primary documentation link.
3. **Reproducible Empirical Benchmarks**: Studies with transparent sample sizes (`N`), methodology notes, and publicly inspectable metrics.
4. **Tools & Platforms**: Open-source CLIs, evaluation harnesses, MCP servers, or established commercial GEO/AEO platforms. Keep descriptions factual (surfaces tracked, core capabilities, and publicly verifiable pricing models)—no superlative marketing claims (`"world's #1"`, `"guaranteed #1 ranking"`).
5. **White-Hat Engineering Only**: We do **not** accept prompt-injection payloads, hidden-text cloaking tricks, fake review scripts, or adversarial spam techniques.

## Pull Request Checklist

- [ ] Verify all external URLs return `HTTP 200` and point to canonical sources (no affiliate or UTM tracking parameters).
- [ ] Update [`README_CN.md`](./README_CN.md) alongside [`README.md`](./README.md) if you are adding a major paper, crawler specification, or tool entry (or note in your PR if you would like maintainer help translating).
- [ ] Run the local validation suite before submitting:
  ```bash
  python3 scripts/validate_repo.py
  ```
- [ ] Review our [Code of Conduct](./CODE_OF_CONDUCT.md).
