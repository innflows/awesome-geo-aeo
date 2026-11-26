# Production GEO & AEO Templates (`templates/`)

Copy-paste, standards-compliant reference configurations for engineering and technical SEO teams:

| File | Standard | Purpose |
| :--- | :--- | :--- |
| [`robots.txt`](./robots.txt) | IETF RFC 9309 | Splits live AI search/citation crawlers (`OAI-SearchBot`, `ChatGPT-User`, `Claude-SearchBot`, `PerplexityBot`, `Googlebot`, `Bingbot`) from foundation-model pre-training crawlers (`GPTBot`, `ClaudeBot`, `Google-Extended`, `CCBot`). |
| [`llms.txt`](./llms.txt) | `llmstxt.org` | Clean `text/markdown` root summary exposing product positioning, transparent pricing tiers, core docs URLs, and canonical social/directory profiles without SPA HTML noise. |
| [`saas-jsonld-graph.json`](./saas-jsonld-graph.json) | `Schema.org` JSON-LD | Connected `@graph` linking `Organization`, `WebSite`, `SoftwareApplication` (with `Offer` pricing), and `FAQPage` via stable `#organization` / `#software` `@id` URIs and `sameAs` links. |

Validate your live deployment after publishing:

```bash
npx @innflows/ai-readiness-audit https://yourdomain.com
```
