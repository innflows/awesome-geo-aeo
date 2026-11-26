# 2026 AI Search Crawlers & Model Training Bots Reference

Modern AI vendors operate **separate user agents** for (1) **real-time search indexing & live user-triggered citations** versus (2) **foundation-model pre-training**. Blanket-blocking all AI user agents in `robots.txt` removes your domain from search-grounded citations in ChatGPT, Claude, and Perplexity—even if your only goal was opting out of model training.

---

## 1. Search / Retrieval Bots vs. Model Training Bots

### A. AI Search Indexing & Live Grounding Bots (Keep `Allow` for Citations)

| `User-Agent` Token | Operator | Primary Function | Official Verification / IP Ranges |
| :--- | :--- | :--- | :--- |
| `OAI-SearchBot` | OpenAI | Indexes web pages for **ChatGPT Search** citations and summaries (not used for foundation model training) | `https://openai.com/searchbot.json` |
| `ChatGPT-User` | OpenAI | Fetches live web pages on behalf of a user prompt or Custom GPT action | `https://openai.com/chatgpt-user.json` |
| `Claude-SearchBot` | Anthropic | Indexes web content for **Claude Web Search** citations | [Anthropic Crawler Docs](https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) |
| `Claude-User` | Anthropic | Live page fetches triggered directly by a Claude user | [Anthropic Crawler Docs](https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) |
| `PerplexityBot` | Perplexity | Indexes pages for **Perplexity** answer citations (not used for foundation model training) | `https://www.perplexity.ai/perplexitybot.json` |
| `Perplexity-User` | Perplexity | User-initiated live page retrieval inside Perplexity | `https://www.perplexity.ai/perplexity-user.json` |
| `Googlebot` | Google | Powers Google Search, **Google AI Overviews**, **Google AI Mode**, and **Gemini** Google Search grounding | `https://developers.google.com/search/apis/ipranges/googlebot.json` |
| `Bingbot` | Microsoft | Powers Bing Search, **Microsoft Copilot**, and downstream Bing-grounded search APIs | `https://www.bing.com/toolbox/bingbot.json` |
| `Applebot` | Apple | Powers Siri, Spotlight, and Safari search suggestions | `https://search.developer.apple.com/applebot.json` |
| `DuckAssistBot` | DuckDuckGo | Fetches sources for Duck.ai / DuckAssist instant answers | [DuckAssistBot Docs](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot/) |

### B. Foundation Model Training & Corpus Crawlers (Optional Opt-Out)

| `User-Agent` Token | Operator | Effect of `Disallow: /` | Official Documentation |
| :--- | :--- | :--- | :--- |
| `GPTBot` | OpenAI | Opts content out of OpenAI generative AI foundation model training while leaving `OAI-SearchBot` unaffected | `https://openai.com/gptbot.json` |
| `ClaudeBot` | Anthropic | Opts content out of Anthropic model training corpus collection | [Anthropic Crawler Docs](https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) |
| `Google-Extended` | Google | Opts content out of Gemini foundation model training and Vertex AI grounding without affecting Google Search or AI Overviews | [Google Crawlers Overview](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers) |
| `Applebot-Extended` | Apple | Opts content out of Apple Intelligence generative model training while keeping `Applebot` search active | [About Applebot](https://support.apple.com/en-us/119829) |
| `Meta-ExternalAgent` | Meta | Crawls public web pages for Meta AI training and indexing | [Meta Web Crawlers](https://developers.facebook.com/docs/sharing/webmasters/web-crawlers/) |
| `Bytespider` | ByteDance | Web corpus crawler for ByteDance LLM training | Standard `robots.txt` token |
| `CCBot` | Common Crawl | Open web archive widely used in open-weights pre-training datasets | `https://commoncrawl.org/ccbot` |
| `Amazonbot` | Amazon | Crawls web pages for Alexa answers and Amazon AI service improvements | `https://developer.amazon.com/support/amazonbot` |

---

## 2. Production Pitfall: Policy-vs-Edge Contradictions (CDN / WAF `403` & `429`)

In our [November 2026 audit of 100 public B2B SaaS websites](../benchmarks/b2b-saas-ai-readiness-2026.csv):

- **`0.0%` (`0 / 95`)** blocked `OAI-SearchBot`, `ChatGPT-User`, or `PerplexityBot` in `/robots.txt`.
- **`7.0%` (`7 / 100`)** inadvertently blocked non-JavaScript HTTP retrieval agents at the CDN/WAF edge (`Cloudflare HTTP 403` Bot Fight Mode or `Vercel Firewall HTTP 429` JS checkpoints)—including sites whose `/robots.txt` explicitly welcomed AI search bots.

### How to Verify Your Edge Layer Without Guessing

1. **Test from a plain non-JS HTTP client (not a logged-in desktop browser)**:
   ```bash
   curl -sIL -A "Mozilla/5.0 (compatible; OAI-SearchBot/1.0; +https://openai.com/searchbot)" https://yourdomain.com/
   ```
2. **Run a full 18-check readiness audit via `npx`**:
   ```bash
   npx @innflows/ai-readiness-audit https://yourdomain.com
   ```
3. **Allowlist verified bot IP CIDR blocks in Cloudflare / Vercel / AWS WAF**:
   - Prefer **verified bot category rules** or official CIDR JSON feeds (`openai.com/searchbot.json`, `perplexitybot.json`, `googlebot.json`, `bingbot.json`) over spoofing-prone `User-Agent` substring bypasses.
