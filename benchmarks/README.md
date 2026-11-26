# Open GEO & AEO Empirical Benchmarks (`benchmarks/`)

This directory contains machine-readable, public-domain (`CC0-1.0`) aggregate CSV datasets from empirical research conducted by **[Innflows Research](https://www.innflows.com/blog)**. Researchers, technical SEO engineers, and journalists may freely load, plot, and cite these tables.

---

## Included CSV Datasets

| File | Sample Scale | Summary | Full Methodology & Write-Up |
| :--- | :--- | :--- | :--- |
| [`fanout-query-mechanics-2026.csv`](./fanout-query-mechanics-2026.csv) | `36,000+` native web search queries across `~12,000` grounded responses | Head-to-head comparison of **ChatGPT** (`OpenAI Web Search`) vs. **Gemini** (`Google Search Grounding`) across query fan-out count, query length, `site:` operator usage (`44.5%` vs. `0.0%`), `best/top/vs` modifiers, year freshness stamps, and unbranded incumbent pre-selection (`~70%` vs. `~39%` median). | [36k Native Fan-Out Study](https://www.innflows.com/blog/seo/how-chatgpt-and-gemini-search-the-web-36k-query-study) |
| [`chatgpt-site-operator-targets-2026.csv`](./chatgpt-site-operator-targets-2026.csv) | `44.5%` `site:` subset of `22,000+` ChatGPT web searches | Distribution of domain classes targeted when ChatGPT emits `site:domain` queries (`62.8%` official brand websites, `25.9%` retail & price comparison, `6.3%` review media, `3.1%` government/standards, `2.0%` country-TLD scoping). | [36k Native Fan-Out Study](https://www.innflows.com/blog/seo/how-chatgpt-and-gemini-search-the-web-36k-query-study) |
| [`b2b-saas-ai-readiness-2026.csv`](./b2b-saas-ai-readiness-2026.csv) | `N = 100` public B2B SaaS root domains (`5` cohorts × `20` domains, Nov 2026) | Non-JS HTTP 200 reachability (`93%`), valid plaintext `/llms.txt` (`72%`, median `14,941` chars / `86` links), `/llms-full.txt` (`20%`), `Schema.org` JSON-LD coverage, and mean AI-readiness score (`87.7/100` overall; `93.4/100` among reachable domains). | [100 B2B SaaS Readiness Study](https://www.innflows.com/blog/seo/state-of-b2b-saas-ai-search-readiness-100-website-study) |
| [`b2b-saas-schema-coverage-2026.csv`](./b2b-saas-schema-coverage-2026.csv) | `n = 93` HTTP-200 reachable B2B SaaS homepages (`N = 100` total) | Adoption rates of specific `Schema.org` entity types on SaaS homepages (`Organization` `66.7%`, stable `@id` `53.8%`, `WebSite` `50.5%`, `WebPage` `24.7%`, `SoftwareApplication` `23.7%`, `FAQPage` `3.2%`). | [100 B2B SaaS Readiness Study](https://www.innflows.com/blog/seo/state-of-b2b-saas-ai-search-readiness-100-website-study) |

---

## Reproducing Website AI-Readiness Audits Locally

The technical HTTP, `robots.txt`, `/llms.txt` soft-404, SSR HTML extractability, and `Schema.org` JSON-LD checks used in Dataset B are available as an open-source zero-dependency CLI and MCP server ([`innflows/website-ai-readiness-audit`](https://github.com/innflows/website-ai-readiness-audit)):

```bash
# Audit any public domain in 5 seconds (Node.js 18+)
npx @innflows/ai-readiness-audit https://yourdomain.com

# Emit structured JSON for batch analysis or CI pipelines
npx @innflows/ai-readiness-audit https://yourdomain.com --json
```

---

## Citation (BibTeX)

```bibtex
@misc{innflows_awesome_geo_aeo_2026,
  author       = {{Innflows Research}},
  title        = {Awesome GEO \& AEO: Generative and Answer Engine Optimization Research, AI Crawler Specifications \& Open Benchmarks},
  year         = {2026},
  month        = nov,
  howpublished = {\url{https://github.com/innflows/awesome-geo-aeo}},
  note         = {Empirical datasets from https://www.innflows.com/blog}
}
```
