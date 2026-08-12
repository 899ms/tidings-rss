<div align="center">
  <img src="https://tidings.info/apple-touch-icon.png" width="96" height="96" alt="Tidings app icon">
  <h1>Tidings RSS</h1>
  <p><strong>680 currently checked feeds, including 348 active Chinese independent blogs.</strong></p>
  <p><a href="README.zh-CN.md">简体中文</a> · <a href="#downloads">Downloads</a> · <a href="#complete-source-directory">Source directory</a> · <a href="CONTRIBUTING.md">Contribute</a> · <a href="https://tidings.info/">Get Tidings</a></p>
  <p>
    <a href="https://github.com/fuxiaoai/tidings-rss/actions/workflows/validate.yml"><img alt="Catalog validation" src="https://github.com/fuxiaoai/tidings-rss/actions/workflows/validate.yml/badge.svg"></a>
    <a href="https://github.com/fuxiaoai/tidings-rss/releases/latest"><img alt="Latest release" src="https://img.shields.io/github/v/release/fuxiaoai/tidings-rss?style=flat-square"></a>
    <a href="LICENSE"><img alt="CC0-1.0" src="https://img.shields.io/badge/license-CC0--1.0-blue?style=flat-square"></a>
  </p>
</div>

This catalog contains feeds worth keeping, not every URL that happened to respond once. Tidings' production parser checks each feed; duplicates, abandoned sites, and repeatedly failing endpoints are removed.

The 2026-08-12 review focused on Chinese independent blogs. We parsed all 1,331 RSS feeds listed by [chinese-independent-blogs](https://github.com/timqian/chinese-independent-blogs) twice, rechecked the strongest candidates, then ranked them using recent publishing activity, article-date distribution, feed text, and site type. The final 348 passed all three rounds and were not padded to the limit of 400.

## Downloads

Topic bundles intentionally overlap. Each normalized feed URL appears once in the complete collection.

| Collection | Feeds | Download | Contents |
| --- | ---: | --- | --- |
| Complete collection | `680` | [Download `tidings-all.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-all.opml) | Every retained source |
| Chinese independent blogs | `348` | [Download `tidings-blogs.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-blogs.opml) | Active Chinese personal blogs |
| Artificial intelligence | `95` | [Download `tidings-ai.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-ai.opml) | Models, research, tools, and writers |
| Fresh news | `39` | [Download `tidings-news.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-news.opml) | International, technology, security, and Chinese news |
| Research and science | `27` | [Download `tidings-research.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-research.opml) | Journals, preprints, labs, and science reporting |
| Engineering and technology | `380` | [Download `tidings-engineering.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-engineering.opml) | Engineering teams and technical writers |
| Video channels | `93` | [Download `tidings-videos.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-videos.opml) | AI, software, science, and business video |
| Podcasts | `73` | [Download `tidings-podcasts.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-podcasts.opml) | Technology, business, science, and Chinese shows |
| Chinese-language sources | `444` | [Download `tidings-chinese.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-chinese.opml) | Articles, communities, video, and audio |

[Browse OPML](opml/) · [SHA-256 checksums](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/SHA256SUMS.txt) · [Catalog summary](reports/catalog-summary.md) · [Machine-readable catalog](data/feeds.json)

## How the Chinese blogs were selected

The upstream list does not publish update dates, frequency, or uptime. We therefore used it only to discover candidates:

1. Parse all 1,331 feeds twice through Tidings and inspect up to 20 real article dates and feed-text lengths.
2. Require both rounds to pass, an update within 180 days, and at least two dated articles.
3. Rank activity in the last 30, 90, and 180 days, first-party hosting, and useful feed text.
4. Parse the leading candidates a third time, then remove failures, duplicate sites, SEO pages, promotional sites, and resource aggregators.
5. Recheck the existing catalog twice and remove repeatedly failing sources before merging.

The audit trail is in [`reports/chinese-blog-curation.json`](reports/chinese-blog-curation.json). It records parser rounds, recent activity, article counts, text length, score, and exclusion reason for every candidate.

## Importing and contributing

All downloads are OPML 2.0. They keep the catalog's primary categories and can be imported into compatible readers. This project distributes public endpoints and original catalog metadata, not article copies.

```bash
python scripts/catalog.py generate
python scripts/catalog.py check
python -m unittest discover -s tests -v
```

See [SOURCES.md](SOURCES.md), [NOTICE.md](NOTICE.md), and [CONTRIBUTING.md](CONTRIBUTING.md) for provenance, rights, and contribution rules.

## Reading the collection with Tidings

**Website: [tidings.info](https://tidings.info/)**

Any compatible reader can import these files. Tidings is the recommended option here because the catalog is checked with the same parser it uses in the app. It keeps OPML categories and handles RSS, Atom, and JSON Feed in one library.

The repository includes a dated v1.1.0 import test of the News and Research bundles: 44/44 News feeds and 28/28 Research feeds refreshed with no final failures. That record is historical evidence, not a claim about the 2026-08-12 snapshot.

[![A real Tidings import of the News and Research bundles](https://cdn.jsdelivr.net/gh/fuxiaoai/tidings-rss@v1.1.0/assets/tidings-import-news-research.png)](assets/tidings-import-news-research.png)

[Import record](reports/import-verification.json) · [Capture script](tools/capture_tidings_import.cjs)

Tidings also provides AI Radar, article Q&A, bilingual reading, video feeds, and structured community threads. Check the website for current feature and pricing details.

The full generated directory follows.

<!-- SOURCE_APPENDIX_START -->
## Complete source directory

All 680 feeds in the complete collection are listed below with their primary category and bundles. This appendix is generated from `data/feeds.json`.

<details>
<summary>Artificial Intelligence · 38</summary>

| Source | Description | Primary category | Feed | Bundles |
| --- | --- | --- | --- | --- |
| [AI](https://blog.google/innovation-and-ai/technology/ai/) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://blog.google/technology/ai/rss/) | ai, all, engineering |
| [AI Musings by Mu](https://kelvinmu.substack.com) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://kelvinmu.substack.com/feed) | ai, all, engineering |
| [AI 开发者日报](https://ainews.liduos.com) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://ainews.liduos.com/rss.xml) | ai, all, chinese, engineering |
| [Anthropic News](https://www.anthropic.com/news) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://rsshub.bestblogs.dev/anthropic/news) | ai, all, engineering |
| [Apple Machine Learning Research](https://machinelearning.apple.com) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://machinelearning.apple.com/rss.xml) | ai, all, engineering, research |
| [Artificial Intelligence](https://aws.amazon.com/blogs/machine-learning/) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://aws.amazon.com/blogs/amazon-ai/feed/) | ai, all, engineering |
| [cs.AI updates on arXiv.org](http://rss.arxiv.org/rss/cs.AI) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://rss.arxiv.org/rss/cs.AI) | ai, all, engineering, research |
| [cs.CL updates on arXiv.org](http://rss.arxiv.org/rss/cs.CL) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://export.arxiv.org/rss/cs.CL) | ai, all, engineering, research |
| [cs.CV updates on arXiv.org](http://rss.arxiv.org/rss/cs.CV) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://export.arxiv.org/rss/cs.CV) | ai, all, chinese, engineering, research |
| [cs.LG updates on arXiv.org](http://rss.arxiv.org/rss/cs.LG) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://export.arxiv.org/rss/cs.LG) | ai, all, chinese, engineering, research |
| [DeepSeek](https://wechat2rss.bestblogs.dev/feed/1709da4f538d4ce4fb6d7a8ba1a5a1c297919601.xml) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://wechat2rss.bestblogs.dev/feed/1709da4f538d4ce4fb6d7a8ba1a5a1c297919601.xml) | ai, all, engineering |
| [Google DeepMind News](https://deepmind.google/blog/) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://deepmind.com/blog/feed/basic/) | ai, all, engineering |
| [Hacker News - Newest: "AI"](https://news.ycombinator.com/newest) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://hnrss.org/newest?q=AI) | ai, all, engineering |
| [Hacker News - Newest: "LLM"](https://news.ycombinator.com/newest) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://hnrss.org/newest?q=LLM) | ai, all, engineering |
| [Hugging Face - Blog](https://huggingface.co/blog) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://huggingface.co/blog/feed.xml) | ai, all, engineering |
| [Last Week in AI](https://lastweekin.ai) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://lastweekin.ai/feed) | ai, all, engineering |
| [MIT News - Artificial intelligence](https://news.mit.edu/rss/topic/artificial-intelligence2) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://news.mit.edu/rss/topic/artificial-intelligence2) | ai, all, engineering, research |
| [OpenAI News](https://openai.com/news) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://openai.com/news/rss.xml) | ai, all, engineering |
| [Recent Commits to openclaw:main](https://github.com/openclaw/openclaw/commits/main) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://github.com/openclaw/openclaw/commits/main.atom) | ai, all, engineering |
| [Release notes from claude-code](https://github.com/anthropics/claude-code/releases) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://github.com/anthropics/claude-code/releases.atom) | ai, all, engineering |
| [Release notes from codex](https://github.com/openai/codex/releases) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://github.com/openai/codex/releases.atom) | ai, all, engineering |
| [Release notes from gemini-cli](https://github.com/google-gemini/gemini-cli/releases) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://github.com/google-gemini/gemini-cli/releases.atom) | ai, all, engineering |
| [Release notes from langchain](https://github.com/langchain-ai/langchain/releases) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://github.com/langchain-ai/langchain/releases.atom) | ai, all, engineering |
| [Release notes from modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol/releases) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://github.com/modelcontextprotocol/specification/releases.atom) | ai, all, engineering |
| [Release notes from openclaw](https://github.com/openclaw/openclaw/releases) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://github.com/openclaw/openclaw/releases.atom) | ai, all, engineering |
| [Release notes from servers](https://github.com/modelcontextprotocol/servers/releases) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://github.com/modelcontextprotocol/servers/releases.atom) | ai, all, engineering |
| [Simon Willison's Weblog](http://simonwillison.net/) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://simonwillison.net/atom/everything/) | ai, all, engineering |
| [The Batch \| DeepLearning.AI \| AI News & Insights](https://www.deeplearning.ai/the-batch/) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://rsshub.bestblogs.dev/deeplearning/the-batch) | ai, all, engineering |
| [The latest research from Google](https://research.google/blog/) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://research.google/blog/rss/) | ai, all, engineering, research |
| [大模型智能](https://wechat2rss.bestblogs.dev/feed/bfc6440c1a2443fab9a6bf607137d41db5cd5c93.xml) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://wechat2rss.bestblogs.dev/feed/bfc6440c1a2443fab9a6bf607137d41db5cd5c93.xml) | ai, all, chinese, engineering |
| [智谱](https://wechat2rss.bestblogs.dev/feed/433d2134dca54d80804daf32e8be546155be3300.xml) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://wechat2rss.bestblogs.dev/feed/433d2134dca54d80804daf32e8be546155be3300.xml) | ai, all, chinese, engineering |
| [月之暗面 Kimi](https://wechat2rss.bestblogs.dev/feed/c5c43d4bc17bae656763859ed0903bb6314ec6fe.xml) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://wechat2rss.bestblogs.dev/feed/c5c43d4bc17bae656763859ed0903bb6314ec6fe.xml) | ai, all, chinese, engineering |
| [机器之心](https://wechat2rss.bestblogs.dev/feed/8d97af31b0de9e48da74558af128a4673d78c9a3.xml) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://wechat2rss.bestblogs.dev/feed/8d97af31b0de9e48da74558af128a4673d78c9a3.xml) | ai, all, chinese, engineering |
| [机器之心SOTA模型](https://wechat2rss.bestblogs.dev/feed/2f520471856d56c7b3a95cd09eb777149b32828a.xml) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://wechat2rss.bestblogs.dev/feed/2f520471856d56c7b3a95cd09eb777149b32828a.xml) | ai, all, chinese, engineering |
| [腾讯混元](https://wechat2rss.bestblogs.dev/feed/306ce19a1ca590c9c2df781789e828d1acfa1356.xml) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://wechat2rss.bestblogs.dev/feed/306ce19a1ca590c9c2df781789e828d1acfa1356.xml) | ai, all, chinese, engineering |
| [通义实验室](https://wechat2rss.bestblogs.dev/feed/4ebee6222ae08705b8aabc9116f0defbcb6b17c6.xml) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://wechat2rss.bestblogs.dev/feed/4ebee6222ae08705b8aabc9116f0defbcb6b17c6.xml) | ai, all, chinese, engineering, research |
| [量子位](https://www.qbitai.com) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://www.qbitai.com/feed) | ai, all, chinese, engineering |
| [阶跃StepFun](https://wechat2rss.bestblogs.dev/feed/3e2714d06aa36142e8ed6b3f4e5cf9090a069dd2.xml) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://wechat2rss.bestblogs.dev/feed/3e2714d06aa36142e8ed6b3f4e5cf9090a069dd2.xml) | ai, all, chinese, engineering |

</details>

<details>
<summary>Engineering & Technology · 340</summary>

| Source | Description | Primary category | Feed | Bundles |
| --- | --- | --- | --- | --- |
| [1A23 Studio](https://1a23.com/) | 主要写编程、设计、音乐、开源。 | Engineering & Technology | [RSS](https://1a23.com/feed/) | all, blogs, chinese, engineering |
| [251 的魔法实验室](https://blog.251.sh/) | 主要写编程、生活、技术、教程。 | Engineering & Technology | [RSS](https://blog.251.sh/feed/) | all, blogs, chinese, engineering |
| [49th LunaSea](https://maki49.github.io/) | 主要写动漫游戏、生活随笔、科研、编程。 | Engineering & Technology | [RSS](https://maki49.github.io/feed.xml) | all, blogs, chinese, engineering |
| [51CTO技术栈](https://wechat2rss.bestblogs.dev/feed/d1fabe6c569ffc44979075dde2f57c65e07c3045.xml) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://wechat2rss.bestblogs.dev/feed/d1fabe6c569ffc44979075dde2f57c65e07c3045.xml) | all, chinese, engineering |
| [9to5Mac](https://9to5mac.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://9to5mac.com/feed) | all, engineering |
| [@Lenciel](https://lenciel.com/) | 主要写技术、管理、创业、吹水。 | Engineering & Technology | [RSS](https://lenciel.com/feed.xml) | all, blogs, chinese, engineering |
| [Abyss的小屋](https://www.rsnocsi.cn/) | 主要写AI、技术、生活、随笔。 | Engineering & Technology | [RSS](https://www.rsnocsi.cn/feed) | ai, all, blogs, chinese, engineering |
| [admin](https://blog.liua.us.ci/rss.xml) | 主要写编程、AI、生活。 | Engineering & Technology | [RSS](https://blog.liua.us.ci/rss.xml) | ai, all, blogs, chinese, engineering |
| [ALBERTAZ](https://albertaz.com) | 主要写前端、技术、绘画、笔记。 | Engineering & Technology | [RSS](https://www.albertaz.com/rss.xml) | all, blogs, chinese, engineering |
| [Alberto De Bortoli](https://albertodebortoli.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://albertodebortoli.com/rss/) | all, engineering |
| [Alliot's blog](https://blog.alliot.tech/) | 主要写编程、技术、运维、硬件。 | Engineering & Technology | [RSS](https://www.iots.vip/atom.xml) | all, blogs, chinese, engineering |
| [Amiya的书桌](https://blog.sayori.org/) | 主要写日记、资源、技术。 | Engineering & Technology | [RSS](https://blog.sayori.org/rss.xml) | all, blogs, chinese, engineering |
| [Android Performance](https://androidperformance.com/atom.xml) | 主要写编程、Android、分享。 | Engineering & Technology | [RSS](https://www.androidperformance.com/atom.xml) | all, blogs, chinese, engineering |
| [Apple Newsroom](https://www.apple.com/newsroom/rss-feed.rss) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.apple.com/newsroom/rss-feed.rss) | all, engineering |
| [AppleInsider News](https://appleinsider.com/rss/news) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://appleinsider.com/rss/news/) | all, engineering |
| [Archive: 2026 - GitHub Changelog](https://github.blog/changelog/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://github.blog/changelog/feed/) | all, engineering |
| [Ars Technica - All content](https://arstechnica.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://feeds.arstechnica.com/arstechnica/index) | all, engineering, news |
| [Arthur's Review](https://blog.leesaitool.com/) | 主要写AI、社会、哲学、随笔。 | Engineering & Technology | [RSS](https://blog.leesaitool.com/feed.xml) | ai, all, blogs, chinese, engineering |
| [Articles on Smashing Magazine — For Web Designers And Developers](https://www.smashingmagazine.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://rss1.smashingmagazine.com/feed/) | all, engineering |
| [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.awsarchitectureblog.com/atom.xml) | all, engineering |
| [AWS News Blog](https://aws.amazon.com/blogs/aws/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://aws.amazon.com/blogs/aws/feed/) | all, engineering |
| [Bboysoul's Blog](https://www.bboy.app/) | 主要写k8s 运维。 | Engineering & Technology | [RSS](https://www.bboy.app/atom.xml) | all, blogs, chinese, engineering |
| [Bensz](https://blognas.hwb0307.com/) | 主要写Docker、Linux、生物医学。 | Engineering & Technology | [RSS](https://blognas.hwb0307.com/feed/) | all, blogs, chinese, engineering |
| [Blog \| Phodal - A Growth Engineer](http://www.phodal.com/blog/) | 主要写编程。 | Engineering & Technology | [RSS](https://www.phodal.com/blog/feeds/rss/) | all, blogs, chinese, engineering |
| [Blog — Philo Li](https://philoli.com/) | 主要写编程、随笔。 | Engineering & Technology | [RSS](http://lulalap.com/atom.xml) | all, blogs, chinese, engineering |
| [Canva - Engineering Blog](https://www.canva.dev/blog/engineering/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.canva.dev/blog/engineering/feed.xml) | all, engineering |
| [CatCoding](http://catcoding.me/atom.xml) | 主要写编程、技术、写作、阅读。 | Engineering & Technology | [RSS](https://catcoding.me/atom.xml) | all, blogs, chinese, engineering |
| [CHEGVA](https://chegva.com) | 主要写编程、运维、随笔、国学。 | Engineering & Technology | [RSS](https://chegva.com/feed/) | all, blogs, chinese, engineering |
| [ChrAlpha's Blog](https://blog.ichr.me/) | 主要写笔记本、技术向、编程、思考。 | Engineering & Technology | [RSS](https://blog.ichr.me/atom.xml) | all, blogs, chinese, engineering |
| [Clark](https://www.dongyao.ren) | 主要写编程、学习、日常。 | Engineering & Technology | [RSS](https://www.dongyao.ren/feed/) | all, blogs, chinese, engineering |
| [Cloud Blog](https://cloud.google.com/blog/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://cloudblog.withgoogle.com/rss/) | all, engineering |
| [Company \| The JetBrains Blog](https://blog.jetbrains.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://blog.jetbrains.com/blog/feed) | all, engineering |
| [Cult of Mac](https://www.cultofmac.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.cultofmac.com/feed) | all, engineering |
| [Data4Fun](https://data4fun.cc/) | 主要写个人随笔、大数据、AI。 | Engineering & Technology | [RSS](https://data4fun.cc/index.xml) | ai, all, blogs, chinese, engineering |
| [Databricks](https://www.databricks.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.databricks.com/feed) | all, engineering |
| [Dax 的博客](https://daolanx.me/) | 主要写编程、全栈、生活。 | Engineering & Technology | [RSS](https://daolanx.me/zh/rss.xml) | all, blogs, chinese, engineering |
| [ddadaal.me](https://ddadaal.me) | 主要写编程、消费数码、随笔。 | Engineering & Technology | [RSS](https://ddadaal.me/rss.xml) | all, blogs, chinese, engineering |
| [Debug客栈](https://blog.debuginn.com/) | 主要写编程、科技、算法、读书。 | Engineering & Technology | [RSS](https://blog.debuginn.com/index.xml) | all, blogs, chinese, engineering |
| [Deepzz's Blog](https://deepzz.com) | 主要写编程、生活。 | Engineering & Technology | [RSS](https://deepzz.com/feed) | all, blogs, chinese, engineering |
| [Dennis](https://www.domon.cn/) | 主要写技术、生活、产品。 | Engineering & Technology | [RSS](https://www.domon.cn/rss/) | all, blogs, chinese, engineering |
| [DGideas' Blog](https://dgideas.net) | 主要写编程、技术、生活。 | Engineering & Technology | [RSS](https://dgideas.net/feed/) | all, blogs, chinese, engineering |
| [distjr_的博客](https://blog.distjr.top/atom.xml) | 主要写技术、随笔、音乐、二次元。 | Engineering & Technology | [RSS](https://blog.distjr.top/atom.xml) | all, blogs, chinese, engineering |
| [Dorck's Blog](https://dorck.cn/) | 主要写技术、开源、随笔、自由。 | Engineering & Technology | [RSS](https://dorck.cn/feed.xml) | all, blogs, chinese, engineering |
| [EdNovas的小站](https://ednovas.xyz/atom.xml) | 主要写编程、算法、Linux、科学上网。 | Engineering & Technology | [RSS](https://ednovas.xyz/atom.xml) | all, blogs, chinese, engineering |
| [Elastic Blog - Elasticsearch, Kibana, and ELK Stack](https://www.elastic.co) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.elastic.co/blog/feed) | all, engineering |
| [Engineering at Meta](https://engineering.fb.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://engineering.fb.com/feed/) | all, engineering |
| [Engineering at Slack](https://slack.engineering) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://slack.engineering/feed/) | all, engineering |
| [Environment + Energy – The Conversation](https://theconversation.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://theconversation.com/au/environment/articles.atom) | all, engineering |
| [Eric's Blog](https://wsdjeg.net/) | 主要写编程、生活、笔记。 | Engineering & Technology | [RSS](https://wsdjeg.net/feed.xml) | all, blogs, chinese, engineering |
| [Etsy Engineering \| Code as Craft](http://www.etsy.com/codeascraft/rss) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://codeascraft.com/feed/atom/) | all, engineering |
| [Feld Thoughts](https://feld.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://feld.com/feed) | all, engineering |
| [Fengc's Blog](https://fengcblog.880200.xyz) | 主要写摄影习作、摄影闲扯、相关测试、AI视频。 | Engineering & Technology | [RSS](https://rssweball.top/feed/afaf2a3c-e11a-4783-a358-9e2d20d76a69.xml) | ai, all, blogs, chinese, engineering |
| [for_the_zero的个人博客](https://ftz.is-a.dev) | 主要写编程、前端、软件开发、思考。 | Engineering & Technology | [RSS](https://ftz.is-a.dev/rss.xml) | ai, all, blogs, chinese, engineering |
| [forecho's Blog](https://blog.forecho.com/) | 主要写编程、美股投资、读书、随想。 | Engineering & Technology | [RSS](https://blog.forecho.com/atom.xml) | all, blogs, chinese, engineering |
| [freeCodeCamp Programming Tutorials: Python, JavaScript, Git & More](https://www.freecodecamp.org/news/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.freecodecamp.org/news/rss/) | all, engineering |
| [Frytea](https://frytea.com/) | 主要写编程、思考、高效。 | Engineering & Technology | [RSS](https://www.frytea.com/index.xml) | all, blogs, chinese, engineering |
| [GamerNoTitle](https://bili33.top) | 主要写编程、学习、技术、杂谈。 | Engineering & Technology | [RSS](https://bili33.top/atom.xml) | all, blogs, chinese, engineering |
| [GISerlab · 地理空间](https://blog.giserlab.cn) | 主要写GIS、技术、地信、地图。 | Engineering & Technology | [RSS](https://blog.giserlab.cn/feed.xml) | all, blogs, chinese, engineering |
| [Good Good Good](https://www.goodgoodgood.co) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.goodgoodgood.co/articles/rss.xml) | all, engineering |
| [Haku](https://re.karlbaey.top/) | 主要写技术、生活、编程、文学。 | Engineering & Technology | [RSS](https://re.karlbaey.top/rss.xml) | all, blogs, chinese, engineering |
| [HCLonely Blog](https://blog.hclonely.com/atom.xml) | 主要写前端、二次元、随笔。 | Engineering & Technology | [RSS](https://blog.hclonely.com/atom.xml) | all, blogs, chinese, engineering |
| [Henry Z's blog](https://changchen.me/) | 主要写技术、Python、SRE、生活。 | Engineering & Technology | [RSS](https://changchen.me/atom.xml) | all, blogs, chinese, engineering |
| [hsfzxjy 的博客](https://i.hsfzxjy.site/) | 主要写编程、开源、随想、生活。 | Engineering & Technology | [RSS](https://i.hsfzxjy.site/rss.xml) | all, blogs, chinese, engineering |
| [https://blog.fivest.one/feed](https://blog.fivest.one) | 主要写生活、吐槽、文艺、社会。 | Engineering & Technology | [RSS](http://blog.fivest.one/feed) | all, blogs, chinese, engineering |
| [I'm OWenT](https://owent.net/) | 主要写编程、后端、技术、思考。 | Engineering & Technology | [RSS](https://owent.net/index.xml) | all, blogs, chinese, engineering |
| [icodex \| 前端技术博客 \| 专注 React、TypeScript、AI 与性能优化 Blog](https://icodex.me/) | 主要写编程、前端、互联网、技术。 | Engineering & Technology | [RSS](https://icodex.me/atom.xml) | all, blogs, chinese, engineering |
| [idealclover](https://idealclover.top/) | 主要写编程、随笔、思考、生活。 | Engineering & Technology | [RSS](https://idealclover.top/feed) | all, blogs, chinese, engineering |
| [ImCBC](https://imcbc.cn/) | 主要写编程、随笔。 | Engineering & Technology | [RSS](https://www.bbing.com.cn/index.xml) | all, blogs, chinese, engineering |
| [inessential.com](https://inessential.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://inessential.com/xml/rss.xml) | all, engineering |
| [Innei](https://innei.in) | 主要写生活、随笔、前端、动漫。 | Engineering & Technology | [RSS](https://innei.ren/feed) | all, blogs, chinese, engineering |
| [IntelliJ IDEA : IntelliJ IDEA – the Leading IDE for Professional Development in Java and Kotlin \| The JetBrains Blog](https://blog.jetbrains.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://blogs.jetbrains.com/idea/feed/) | all, engineering |
| [ISLAND](https://youngxhui.top/) | 主要写编程、生活、随笔。 | Engineering & Technology | [RSS](https://youngxhui.top/index.xml) | all, blogs, chinese, engineering |
| [iTimothy](https://xiaozhou.net/atom.xml) | 主要写编程。 | Engineering & Technology | [RSS](https://xiaozhou.net/atom.xml) | all, blogs, chinese, engineering |
| [Jack Pu's Blog (蒲小花的博客－ポーのブログ)](https://www.jackpu.com/) | 主要写前端、生活。 | Engineering & Technology | [RSS](https://www.jackpu.com/rss/) | all, blogs, chinese, engineering |
| [Jacky Wong](https://jw1.ai/atom.xml) | 主要写前端、生活、技术、音乐。 | Engineering & Technology | [RSS](https://jw1.dev/atom.xml) | all, blogs, chinese, engineering |
| [jdjwzx233的博客](https://jdjwzx233.cn) | 主要写生活、编程、技术、日常。 | Engineering & Technology | [RSS](https://www.jdjwzx233.cn/atom.xml) | all, blogs, chinese, engineering |
| [Jimmy Song – Jimmy Song's Blog](https://jimmysong.io/) | 主要写编程。 | Engineering & Technology | [RSS](https://jimmysong.io/index.xml) | all, blogs, chinese, engineering |
| [Josherich’s Blog](https://josherich.me/) | 主要写编程、随笔。 | Engineering & Technology | [RSS](https://www.josherich.me/feed.xml) | all, blogs, chinese, engineering |
| [keggin's blog](https://keggin.tech) | 主要写编程、Linux、数模、逆向。 | Engineering & Technology | [RSS](https://keggin.tech/rss.xml) | all, blogs, chinese, engineering |
| [Kerry的学习笔记](https://kerrynotes.com) | 主要写软件、技术、分享。 | Engineering & Technology | [RSS](https://kerrynotes.com/feed/) | all, blogs, chinese, engineering |
| [kok的笔记本](https://wocai.de/) | 主要写编程、摄影。 | Engineering & Technology | [RSS](https://wocai.de/index.xml/) | all, blogs, chinese, engineering |
| [Kotlin : A concise multiplatform language developed by JetBrains \| The JetBrains Blog](https://blog.jetbrains.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://blog.jetbrains.com/kotlin/feed/) | all, engineering |
| [Krebs on Security](https://krebsonsecurity.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://krebsonsecurity.com/feed/) | all, engineering, news |
| [laike9m's blog](https://laike9m.com/blog/rss) | 主要写Python、生活、编程。 | Engineering & Technology | [RSS](https://laike9m.com/blog/rss/) | all, blogs, chinese, engineering |
| [Latest news](https://www.zdnet.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.zdnet.com/topic/security/rss.xml) | all, engineering |
| [LearnData 开源笔记](https://newzone.top/) | 主要写笔记、个人成长、编程。 | Engineering & Technology | [RSS](https://newzone.top/rss.xml) | all, blogs, chinese, engineering |
| [Lex Blog](https://dreams.plus/) | 主要写生活、随笔、编程、笔记。 | Engineering & Technology | [RSS](https://dreams.plus/rss.xml) | all, blogs, chinese, engineering |
| [LiaoKe的博客](https://blog.liao-ke.com/) | 主要写编程、开源、全栈、开发者。 | Engineering & Technology | [RSS](https://blog.liao-ke.com/rss.xml) | all, blogs, chinese, engineering |
| [LiesAuer's Blog](https://www.liesauer.net/blog/) | 主要写编程。 | Engineering & Technology | [RSS](https://www.liesauer.net/blog/feed/) | all, blogs, chinese, engineering |
| [Lifehacker](https://lifehacker.com/feed/rss) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://lifehacker.com/rss) | all, engineering |
| [LiuShen's Blog - 清羽飞扬](https://blog.liushen.fun/) | 主要写技术、生活、随笔、记录。 | Engineering & Technology | [RSS](https://blog.liushen.fun/atom.xml) | all, blogs, chinese, engineering |
| [Long Luo's Life Notes](https://www.longluo.me/atom.xml) | 主要写数学、物理、算法、编程。 | Engineering & Technology | [RSS](https://www.longluo.me/atom.xml) | all, blogs, chinese, engineering |
| [Longlong's Blog](https://blog.xlonglong.cn) | 主要写生活日常、随笔、学习笔记、炼丹。 | Engineering & Technology | [RSS](https://blog.xlonglong.cn/feed/) | all, blogs, chinese, engineering |
| [Louis C Deng's Blog](https://blog.aeilot.top/index.xml) | 主要写随笔、技术、艺术、生活。 | Engineering & Technology | [RSS](https://blog.aeilot.top/index.xml) | all, blogs, chinese, engineering |
| [lucifer的网络博客](https://lucifer.ren/blog) | 主要写编程、前端、算法。 | Engineering & Technology | [RSS](https://lucifer.ren/blog/atom.xml) | all, blogs, chinese, engineering |
| [luozhiyun`s Blog](https://www.luozhiyun.com) | 主要写编程、生活。 | Engineering & Technology | [RSS](https://www.luozhiyun.com/feed) | all, blogs, chinese, engineering |
| [LV88](https://lv88fg.com) | 主要写编程、学习、生活。 | Engineering & Technology | [RSS](https://scvoet.me/feed) | all, blogs, chinese, engineering |
| [MacTalk-池建强的 Blog](https://macshuo.com) | 主要写编程、iOS。 | Engineering & Technology | [RSS](http://macshuo.com/?feed=rss2) | all, blogs, chinese, engineering |
| [Martin Fowler](https://martinfowler.com/feed.atom) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://martinfowler.com/feed.atom) | all, engineering |
| [Mengke's blog - Mengke's coding journey](https://www.mengke.me/blog) | 主要写技术、生活、笔记。 | Engineering & Technology | [RSS](https://mengke.me/feed.xml) | all, blogs, chinese, engineering |
| [mephisto.cc](https://mephisto.cc/) | 主要写Linux、Python、Travel、Note。 | Engineering & Technology | [RSS](https://mephisto.cc/index.xml) | all, blogs, chinese, engineering |
| [Microsoft Azure Blog](https://azure.microsoft.com/en-us/blog/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://azure.microsoft.com/en-us/blog/feed/) | all, engineering |
| [Mobility](https://lichuanyang.top/) | 主要写编程、后端、java。 | Engineering & Technology | [RSS](http://lichuanyang.top/atom.xml) | all, blogs, chinese, engineering |
| [Mokeyjay's Blog - 超能小紫](https://mok.moe) | 主要写编程、开源、PHP、生活。 | Engineering & Technology | [RSS](https://www.mokeyjay.com/feed) | all, blogs, chinese, engineering |
| [Mosu](https://mosuzi.com/atom.xml) | 主要写随笔、生活、开发。 | Engineering & Technology | [RSS](https://www.mosuzi.com/atom.xml) | all, blogs, chinese, engineering |
| [Mox的笔记库](https://mocusez.site/zh-CN/) | 主要写编程、数据库、程序编译器、随笔。 | Engineering & Technology | [RSS](https://mocusez.site/zh-CN/atom.xml) | all, blogs, chinese, engineering |
| [Muyun99 的杂谈](https://muyun.work/) | 主要写科技、生活、算法、随笔。 | Engineering & Technology | [RSS](https://muyun.work/feed/) | all, blogs, chinese, engineering |
| [My](https://dayzmod.kdns.fr/) | 主要写编程、模组、游戏。 | Engineering & Technology | [RSS](https://dayzmod.kdns.fr/rss.xml) | all, blogs, chinese, engineering |
| [NBlog](https://blog.nocp.space) | 主要写编程、技术、随笔、音乐。 | Engineering & Technology | [RSS](https://nocp.space/rss/feed.json) | all, blogs, chinese, engineering |
| [Netflix TechBlog - Medium](https://netflixtechblog.com?source=rss----2615bd06b42e---4) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://netflixtechblog.com/feed) | all, engineering |
| [News – CNET](https://www.cnet.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.cnet.com/rss/news/) | all, engineering |
| [Nicksxs's Blog](https://nicksxs.me/atom.xml) | 主要写编程、后端、Java、PHP。 | Engineering & Technology | [RSS](https://nicksxs.me/atom.xml) | all, blogs, chinese, engineering |
| [Niracler 的博物志](https://niracler.com) | 主要写生活、编程、工具、随笔。 | Engineering & Technology | [RSS](https://niracler.com/rss.xml) | all, blogs, chinese, engineering |
| [Node.js Blog](https://nodejs.org/en) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://nodejs.org/en/feed/blog.xml) | all, engineering |
| [NPR Topics: Environment](https://www.npr.org/templates/story/story.php?storyId=1025) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://feeds.npr.org/1025/rss.xml) | all, engineering |
| [NYT > Climate and Environment](https://www.nytimes.com/section/climate) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://rss.nytimes.com/services/xml/rss/nyt/Climate.xml) | all, engineering |
| [obaby 𝐢‍𝐧⃝ void](https://zhongxiaojie.cn/) | 主要写生活、编程、硬件、人工智能。 | Engineering & Technology | [RSS](https://h4ck.org.cn/feed/) | ai, all, blogs, chinese, engineering |
| [oldj's blog](https://oldj.net) | 主要写编程、写作、以及涂鸦。 | Engineering & Technology | [RSS](https://oldj.net/feed) | all, blogs, chinese, engineering |
| [OneCoder](https://www.coderli.com/) | 主要写编程、教程、技术、随笔。 | Engineering & Technology | [RSS](https://www.coderli.com/feed.xml) | all, blogs, chinese, engineering |
| [OneV's Den](https://onevcat.com) | 主要写编程、iOS。 | Engineering & Technology | [RSS](https://onevcat.com/feed.xml) | all, blogs, chinese, engineering |
| [OnionTalk](https://hateonion.me/) | 主要写编程、前端、随笔。 | Engineering & Technology | [RSS](https://hateonion.me/index.xml) | all, blogs, chinese, engineering |
| [Oragekk&apos;s Blog](https://oragekk.me/) | 主要写编程、思考、学习笔记、生活杂想。 | Engineering & Technology | [RSS](https://oragekk.me/rss.xml) | all, blogs, chinese, engineering |
| [Origin](https://blog.singee.me/atom.xml) | 主要写编程、Python、随笔。 | Engineering & Technology | [RSS](https://blog.singee.me/atom.xml) | all, blogs, chinese, engineering |
| [Panda Home](https://old-panda.com/) | 主要写编程、生活。 | Engineering & Technology | [RSS](https://old-panda.com/feed/) | all, blogs, chinese, engineering |
| [Peng's Blog](https://pengs.top/atom.xml) | 主要写编程、技术、linux、生活。 | Engineering & Technology | [RSS](https://pengs.top/atom.xml) | all, blogs, chinese, engineering |
| [piglei](https://www.piglei.com/) | 主要写编程。 | Engineering & Technology | [RSS](https://www.piglei.com/feeds/latest/) | all, blogs, chinese, engineering |
| [Prakati India](https://prakati.in/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.prakati.in/feed/) | all, engineering |
| [ProAndroidDev - Medium](https://proandroiddev.com?source=rss----c72404660798---4) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://proandroiddev.com/feed) | all, engineering |
| [pseudoyu](https://www.pseudoyu.com/) | 主要写区块链、编程、工具、随笔。 | Engineering & Technology | [RSS](https://www.pseudoyu.com/zh/index.xml) | all, blogs, chinese, engineering |
| [Public Object](https://publicobject.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://publicobject.com/rss/) | all, engineering |
| [Python Insider](https://blog.python.org/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://blog.python.org/feeds/posts/default) | all, engineering |
| [Qaiu blog](https://blog.qaiu.top) | 主要写手机编程、技术、开发、教程。 | Engineering & Technology | [RSS](https://blog.qaiu.top/rss.xml) | all, blogs, chinese, engineering |
| [QingCCL](https://qingccl.com/) | 主要写文学、读书、随笔、技术。 | Engineering & Technology | [RSS](https://qingccl.github.io/rss.xml) | all, blogs, chinese, engineering |
| [QP's Blog](https://www.szqp.site) | 主要写生活、旅行、技术。 | Engineering & Technology | [RSS](https://www.szqp.site/feed) | all, blogs, chinese, engineering |
| [Qunar技术沙龙](https://wechat2rss.bestblogs.dev/feed/84c072f8d34d1690f2783d7dda6013cf6d892b7f.xml) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://wechat2rss.bestblogs.dev/feed/84c072f8d34d1690f2783d7dda6013cf6d892b7f.xml) | all, chinese, engineering |
| [Random Thoughts](https://blog.joway.io/) | 主要写编程、旅行、随笔。 | Engineering & Technology | [RSS](https://blog.joway.io/index.xml) | all, blogs, chinese, engineering |
| [Randy's Blog](https://lutaonan.com) | 主要写编程。 | Engineering & Technology | [RSS](https://lutaonan.com/rss.xml) | all, blogs, chinese, engineering |
| [Raz1ner](https://raz1ner.com) | 主要写Excel函数、Google脚本、技术、随笔。 | Engineering & Technology | [RSS](https://raz1ner.com/atom.xml) | all, blogs, chinese, engineering |
| [ReadWrite](https://readwrite.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://readwrite.com/feed/) | all, engineering |
| [Redis Blog](https://redis.io/en/blog) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://redis.io/feed/) | all, engineering |
| [Release notes from biome](https://github.com/biomejs/biome/releases) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://github.com/biomejs/biome/releases.atom) | all, engineering |
| [Release notes from bun](https://github.com/oven-sh/bun/releases) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://github.com/oven-sh/bun/releases.atom) | all, engineering |
| [Release notes from NetNewsWire](https://github.com/Ranchero-Software/NetNewsWire/releases) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://github.com/Ranchero-Software/NetNewsWire/releases.atom) | all, engineering |
| [Release notes from zed](https://github.com/zed-industries/zed/releases) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://github.com/zed-industries/zed/releases.atom) | all, engineering |
| [Replicate's blog](https://replicate.com/blog) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://replicate.com/blog/rss) | all, engineering |
| [Rokcso's Blog](https://rokcso.com/) | 主要写生活、技术、好奇心、产品管理。 | Engineering & Technology | [RSS](https://rokcso.com/index.xml) | ai, all, blogs, chinese, engineering |
| [ROYWANG](https://roy.wang/feed/index.xml) | 主要写技术、生活、日记。 | Engineering & Technology | [RSS](https://roy.wang/feed/) | all, blogs, chinese, engineering |
| [Roy的个人站](https://geofftools.cn/blog/) | 主要写编程、Swift、Python。 | Engineering & Technology | [RSS](https://geofftools.cn/blog/atom.xml) | all, blogs, chinese, engineering |
| [Rust Blog](https://blog.rust-lang.org/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://blog.rust-lang.org/feed.xml) | all, engineering |
| [rxliuli blog](https://blog.rxliuli.com/atom.xml) | 主要写前端、编程、随笔。 | Engineering & Technology | [RSS](https://blog.rxliuli.com/atom.xml) | all, blogs, chinese, engineering |
| [RYANUO](https://ryanuo.cc) | 主要写编程、嵌入式、前端、AI。 | Engineering & Technology | [RSS](https://ryanuo.cc/sitemap.xml) | ai, all, blogs, chinese, engineering |
| [Ryan‘s World](https://blog.12ms.xyz/) | 主要写编程、技术、运维、加密货币。 | Engineering & Technology | [RSS](https://blog.12ms.xyz/feed/) | all, blogs, chinese, engineering |
| [S T C H E N G](https://cheng.st/atom.xml) | 主要写随笔、旅行、摄影、运动。 | Engineering & Technology | [RSS](https://cheng.st/atom.xml) | all, blogs, chinese, engineering |
| [Schneier on Security](https://www.schneier.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.schneier.com/blog/index.rdf) | all, engineering, news |
| [Security Affairs](https://securityaffairs.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://securityaffairs.co/wordpress/feed) | all, engineering |
| [Sehnsucht](https://blog.sehnsucht.top/) | 主要写技术、生活、随笔、读书。 | Engineering & Technology | [RSS](https://blog.sehnsucht.top/rss.xml) | all, blogs, chinese, engineering |
| [Sekyoro的博客小屋](https://www.sekyoro.top/) | 主要写编程、学习笔记、机器学习、工具使用。 | Engineering & Technology | [RSS](https://www.sekyoro.top/atom.xml) | ai, all, blogs, chinese, engineering |
| [Seven's blog](https://blog.diqigan.cn/) | 主要写编程、随笔、Geek、Java。 | Engineering & Technology | [RSS](https://blog.diqigan.cn/atom.xml) | all, blogs, chinese, engineering |
| [Shanwer's Blog](https://blog.shanwer.top) | 主要写日常、生活、编程、随笔。 | Engineering & Technology | [RSS](https://blog.shanwer.top/feed/) | all, blogs, chinese, engineering |
| [sjdhome](https://sjdhome.com/) | 主要写编程、生活、学习。 | Engineering & Technology | [RSS](https://sjdhome.com/blog/atom.xml) | all, blogs, chinese, engineering |
| [Skywind Inside](https://skywind.me/blog) | 主要写编程。 | Engineering & Technology | [RSS](http://www.skywind.me/blog/feed) | all, blogs, chinese, engineering |
| [SkyWT](https://skywt.cn) | 主要写技术、开发、生活。 | Engineering & Technology | [RSS](https://blog.skywt.cn/feed/) | all, blogs, chinese, engineering |
| [Slashdot](https://slashdot.org/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://rss.slashdot.org/Slashdot/slashdotMain) | all, engineering |
| [smallyu的博客](https://smallyu.net/atom.xml) | 主要写技术、生活、区块链。 | Engineering & Technology | [RSS](https://smallyu.net/atom.xml) | all, blogs, chinese, engineering |
| [Spotify Engineering](https://engineering.atspotify.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://engineering.atspotify.com/feed/) | all, engineering |
| [Stack Overflow Blog](https://stackoverflow.blog/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://blog.stackoverflow.com/feed/) | all, engineering |
| [Steve Sun](https://sund.site/) | 主要写数字生活、文化、架构。 | Engineering & Technology | [RSS](https://www.sund.site/index.xml) | all, blogs, chinese, engineering |
| [Stratechery by Ben Thompson](https://stratechery.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://stratechery.com/feed/) | all, engineering |
| [Stray Episode](https://farer.org/) | 主要写编程、技术、游戏、思考。 | Engineering & Technology | [RSS](https://farer.org/rss/) | all, blogs, chinese, engineering |
| [Stripe Blog](https://stripe.com/blog) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://stripe.com/blog/feed.rss) | all, engineering |
| [StudyingLover's Blog](https://www.studyinglover.com/) | 主要写编程、机器学习、计算机视觉、元宇宙。 | Engineering & Technology | [RSS](https://studyinglover.com/atom.xml) | ai, all, blogs, chinese, engineering |
| [SUMSEC](https://sumsec.me) | 主要写技术、安全、生活、Java安全。 | Engineering & Technology | [RSS](https://sumsec.me/resources/atom.xml) | all, blogs, chinese, engineering |
| [Sunset 的重构博客](https://blog.sunmkt.uk/) | 主要写编程、开源、生活、随笔。 | Engineering & Technology | [RSS](https://blog.sunmkt.uk/feed.xml) | all, blogs, chinese, engineering |
| [Supabase Blog](https://supabase.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://supabase.com/rss.xml) | all, engineering |
| [Super Blog](https://superpung.com/atom.xml) | 主要写编程、生活、技术、观点。 | Engineering & Technology | [RSS](https://superpung.com/atom.xml) | all, blogs, chinese, engineering |
| [Surmon.me](https://surmon.me) | 主要写前端、编程、思考。 | Engineering & Technology | [RSS](https://surmon.me/rss.xml) | all, blogs, chinese, engineering |
| [Swift by Sundell](https://www.swiftbysundell.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.swiftbysundell.com/feed.rss) | all, engineering |
| [Swift.org](https://www.swift.org/atom.xml) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.swift.org/atom.xml) | all, engineering |
| [Taxodium](https://taxodium.ink/) | 主要写编程、随笔。 | Engineering & Technology | [RSS](https://taxodium.ink/rss.xml) | all, blogs, chinese, engineering |
| [Terrarum::异世界丨居正博客](https://blog.skyju.cc/) | 主要写编程、PHP、渗透、开源。 | Engineering & Technology | [RSS](https://blog.skyju.cc/index.xml) | all, blogs, chinese, engineering |
| [The Airbnb Tech Blog - Medium](https://medium.com/airbnb-engineering?source=rss----53c7c27702d5---4) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://medium.com/feed/airbnb-engineering) | all, engineering |
| [The ASF Blog](https://news.apache.org/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://news.apache.org/feed) | all, engineering |
| [The Cloudflare Blog](https://blog.cloudflare.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://blog.cloudflare.com/rss) | all, engineering |
| [The GitHub Blog](https://github.blog/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://github.blog/feed/) | all, engineering |
| [The Intercom Blog](https://www.intercom.com/blog/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.intercom.com/blog/feed) | all, engineering |
| [The JetBrains Blog](https://blog.jetbrains.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://blog.jetbrains.com/feed/) | all, engineering |
| [The Loop](https://www.loopinsight.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.loopinsight.com/feed) | all, engineering |
| [The New Stack](https://thenewstack.io/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://thenewstack.io/feed/) | all, engineering |
| [Tianhe Gao](https://tianheg.co/) | 主要写生活、技术。 | Engineering & Technology | [RSS](https://tianheg.co/index.xml) | all, blogs, chinese, engineering |
| [TrumanDu's Blog](http://blog.trumandu.top/atom.xml) | 主要写日记、随笔、学习、技术分享。 | Engineering & Technology | [RSS](http://blog.trumandu.top/atom.xml) | all, blogs, chinese, engineering |
| [Turing Post](https://www.turingpost.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://rss.beehiiv.com/feeds/UJIoBuf5BX.xml) | all, engineering |
| [Tw93 Blog](https://tw93.fun) | 主要写开源、前端、分享、MacOS。 | Engineering & Technology | [RSS](https://tw93.fun/feed.xml) | all, blogs, chinese, engineering |
| [Use Case: copilot - GitHub Changelog](https://github.blog/changelog/label/copilot/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://github.blog/changelog/label/copilot/feed/) | all, engineering |
| [Usubeni Fantasy](https://ssshooter.com/) | 主要写前端、随想、游戏、摄影。 | Engineering & Technology | [RSS](https://ssshooter.com/rss.xml) | all, blogs, chinese, engineering |
| [UWillno's Blog](https://uwillno.com) | 主要写Qt、WASM、技术、记录。 | Engineering & Technology | [RSS](https://uwillno.com/rss.xml) | all, blogs, chinese, engineering |
| [Vercel News](https://vercel.com/atom) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://vercel.com/atom) | all, engineering |
| [Visual Studio Blog](https://devblogs.microsoft.com/visualstudio/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://devblogs.microsoft.com/visualstudio/feed/) | all, engineering |
| [vivo互联网技术](https://wechat2rss.bestblogs.dev/feed/b3ceb5cb1e4602ca55704650a157ec9c5b2f0d31.xml) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://wechat2rss.bestblogs.dev/feed/b3ceb5cb1e4602ca55704650a157ec9c5b2f0d31.xml) | all, chinese, engineering |
| [Watermelonabc的Blog](https://watermelonabc.top/) | 主要写编程、技术、笔记、生活。 | Engineering & Technology | [RSS](https://watermelonabc.top/atom.xml) | all, blogs, chinese, engineering |
| [Weishu's Notes](https://weishu.me/) | 主要写编程。 | Engineering & Technology | [RSS](https://weishu.me/atom.xml) | all, blogs, chinese, engineering |
| [wmhwiki](https://wmhwiki.cn) | 主要写技术、生活。 | Engineering & Technology | [RSS](https://wmhwiki.cn/rss.xml) | all, blogs, chinese, engineering |
| [WuSiYu Blog](https://wusiyu.me/) | 主要写折腾、技术、DIY、Linux。 | Engineering & Technology | [RSS](https://wusiyu.me/feed/) | all, blogs, chinese, engineering |
| [x7aNote](https://xeonzilla.top/) | 主要写二次元、技术、随笔。 | Engineering & Technology | [RSS](https://xeonzilla.top/index.xml) | all, blogs, chinese, engineering |
| [XINDOO](https://zxs.io/) | 主要写算法、编程、人生。 | Engineering & Technology | [RSS](https://zxs.io/feed) | all, blogs, chinese, engineering |
| [YangXuan's Blog](https://yangxuan.ai) | 主要写AI、投资、量化。 | Engineering & Technology | [RSS](https://yangxuan.ai/feed/) | ai, all, blogs, chinese, engineering |
| [yCENzh's Blog](https://fuwari.oh1.top/) | 主要写技术、随笔、笔记、乱七八糟。 | Engineering & Technology | [RSS](https://fuwari.oh1.top/rss.xml) | all, blogs, chinese, engineering |
| [YeungYeah's Context](https://scottyeung.top/) | 主要写编程、算法、随笔、玄学。 | Engineering & Technology | [RSS](http://scottyeung.top/atom.xml) | all, blogs, chinese, engineering |
| [Yi's Blog](https://ycao.net/) | 主要写编程、学习、生活。 | Engineering & Technology | [RSS](https://ycao.top/feed.xml) | all, blogs, chinese, engineering |
| [Yiran's Blog](https://zdyxry.github.io/) | 主要写编程、Linux。 | Engineering & Technology | [RSS](https://zdyxry.github.io/atom.xml) | all, blogs, chinese, engineering |
| [YOLO Blog](https://www.yolo.blue/blog) | 主要写编程、随笔、游戏、生活。 | Engineering & Technology | [RSS](https://www.yolo.blue/blog/rss.xml) | all, blogs, chinese, engineering |
| [ypingcn](https://blog.ypingcn.com/) | 主要写技术、生活、分享、火狐。 | Engineering & Technology | [RSS](https://blog.ypingcn.com/feed.xml) | all, blogs, chinese, engineering |
| [zhecydn的博客站](https://blog.zhecydn.asia) | 主要写生活、随笔、技术、分享。 | Engineering & Technology | [RSS](https://blog.zhecydn.asia/feed/) | all, blogs, chinese, engineering |
| [一纸忘忧](https://www.ikxin.com/) | 主要写编程、PHP、开箱、Linux。 | Engineering & Technology | [RSS](https://www.ikxin.com/feed/) | all, blogs, chinese, engineering |
| [东东's Blog](https://blog.yasking.org/) | 主要写编程、技术、笔记。 | Engineering & Technology | [RSS](https://blog.yasking.org/atom.xml) | all, blogs, chinese, engineering |
| [东方星痕](https://ystyle.top) | 主要写编程、技术。 | Engineering & Technology | [RSS](https://ystyle.top/atom.xml) | all, blogs, chinese, engineering |
| [中文博客 on 范叶亮 \| Leo Van](https://leovan.me/cn/) | 主要写编程、算法、数据科学、思考。 | Engineering & Technology | [RSS](https://leovan.me/cn/index.xml) | all, blogs, chinese, engineering |
| [串串狗小刊 ⭐️](https://www.ccgxk.com/) | 主要写生活、编程、科技、记录。 | Engineering & Technology | [RSS](https://www.ccgxk.com/rss.php) | all, blogs, chinese, engineering |
| [九仞之行](https://styunlen.cn) | 主要写编程、技术、人文、音乐。 | Engineering & Technology | [RSS](https://styunlen.cn/feed) | all, blogs, chinese, engineering |
| [了迹奇有没](https://whrss.com/) | 主要写编程、思考、生活随笔。 | Engineering & Technology | [RSS](https://whrss.com/feed) | all, blogs, chinese, engineering |
| [二丫讲梵](https://wiki.eryajf.net) | 主要写运维、思索、编程。 | Engineering & Technology | [RSS](https://wiki.eryajf.net/rss.xml) | all, blogs, chinese, engineering |
| [仲平](https://blog.zopiya.com/) | 主要写生活、开发、旅行、摄影。 | Engineering & Technology | [RSS](https://blog.7wate.com/rss.xml) | all, blogs, chinese, engineering |
| [任霏的个人博客网站](https://blog.renfei.net) | 主要写编程、Java、经验。 | Engineering & Technology | [RSS](https://blog.renfei.net/rss.xml) | all, blogs, chinese, engineering |
| [伪斜杠青年](https://i.lckiss.com) | 主要写技术、折腾、随记。 | Engineering & Technology | [RSS](http://i.lckiss.com/?feed=rss2) | all, blogs, chinese, engineering |
| [依云's Blog](https://blog.lilydjwg.me/) | 主要写编程。 | Engineering & Technology | [RSS](https://blog.lilydjwg.me/posts.rss) | all, blogs, chinese, engineering |
| [侯锐的思考与分享](https://www.nosuchfield.com/) | 主要写编程。 | Engineering & Technology | [RSS](https://www.nosuchfield.com/atom.xml) | all, blogs, chinese, engineering |
| [保罗的小宇宙](https://paugram.com/) | 主要写生活、随笔、前端、动漫。 | Engineering & Technology | [RSS](https://paugram.com/feed) | all, blogs, chinese, engineering |
| [傥师妹TangShiMei的小空间](https://blog.224418.xyz/) | 主要写技术、生活、随笔、折腾。 | Engineering & Technology | [RSS](https://blog.224418.xyz/rss2.xml) | all, blogs, chinese, engineering |
| [傲雪の](https://www.oxue.de/) | 主要写技术、写作、生活、随笔。 | Engineering & Technology | [RSS](https://www.oxue.de/rss.xml) | all, blogs, chinese, engineering |
| [农码生涯，无酒无花 – The coding life, no wine, no shine.](https://nicrosoft.net/blog) | 主要写编程、生活。 | Engineering & Technology | [RSS](https://nicrosoft.net/blog/feed/) | all, blogs, chinese, engineering |
| [冰冻大西瓜](https://bddxg.top/) | 主要写前端、编程、生活、AI。 | Engineering & Technology | [RSS](https://bddxg.top/feed.rss) | ai, all, blogs, chinese, engineering |
| [刘郎阁](https://vjo.cc/) | 主要写编程、生活、记录、随笔。 | Engineering & Technology | [RSS](https://vjo.cc/feed/) | all, blogs, chinese, engineering |
| [创见思考——怎样度过这一生](https://www.fengcan.net) | 主要写AI、读书、医疗、人生决策。 | Engineering & Technology | [RSS](https://www.fengcan.net/feed/) | ai, all, blogs, chinese, engineering |
| [初然忆](https://www.imcry.vip/) | 主要写编程、生活、记录。 | Engineering & Technology | [RSS](https://www.imcry.vip/index.xml) | all, blogs, chinese, engineering |
| [北门清燕](https://bmqy.net/) | 主要写生活、随笔、前端。 | Engineering & Technology | [RSS](https://www.bmqy.net/feed.xml) | all, blogs, chinese, engineering |
| [千古八方的博客](https://rangotec.com/feed) | 主要写编程、Android、数据私有化。 | Engineering & Technology | [RSS](https://rangotec.com/feed) | all, blogs, chinese, engineering |
| [千里之豪的格物垛](https://blog.gadore.top) | 主要写技术、生活、图片。 | Engineering & Technology | [RSS](https://blog.gadore.top/feed.xml) | all, blogs, chinese, engineering |
| [半方池水半方田](https://blog.uuanqin.top/atom.xml) | 主要写编程、生活、分享。 | Engineering & Technology | [RSS](https://uuanqin.top/atom.xml) | all, blogs, chinese, engineering |
| [博客 on Neil的自留地](https://neilmin.com/zh/posts/) | 主要写编程、生活、笔记、随想。 | Engineering & Technology | [RSS](https://neilmin.com/zh/posts/index.xml) | all, blogs, chinese, engineering |
| [卡片创作实验室](https://cnfeat.com/) | 主要写编程。 | Engineering & Technology | [RSS](https://www.cnfeat.com/feed.xml) | all, blogs, chinese, engineering |
| [卡瓦邦噶！](https://www.kawabangga.com) | 主要写编程、随笔、技术。 | Engineering & Technology | [RSS](https://www.kawabangga.com/feed) | all, blogs, chinese, engineering |
| [又耳笔记](https://youerning.top/) | 主要写技术、编程、随笔。 | Engineering & Technology | [RSS](https://youerning.top/index.xml) | all, blogs, chinese, engineering |
| [后端技术杂谈](https://www.rowkey.cn/atom.xml) | 主要写编程。 | Engineering & Technology | [RSS](https://rowkey.cn/atom.xml) | all, blogs, chinese, engineering |
| [唐巧的博客](https://blog.devtang.com/atom.xml) | 主要写编程、创业、iOS。 | Engineering & Technology | [RSS](https://blog.devtang.com/atom.xml) | all, blogs, chinese, engineering |
| [喵二の小博客](https://www.miaoer.net) | 主要写技术、生活、学习。 | Engineering & Technology | [RSS](https://www.miaoer.net/feed) | all, blogs, chinese, engineering |
| [喵喵小站・博客志](https://www.mmbkz.cn/) | 主要写生活、日常、编程、笔记。 | Engineering & Technology | [RSS](https://www.mmbkz.cn/feed) | all, blogs, chinese, engineering |
| [土木坛子](https://tumutanzi.com) | 主要写科研学习、社会人文、信息技术、国外见闻。 | Engineering & Technology | [RSS](https://tumutanzi.com/feed) | all, blogs, chinese, engineering |
| [土法炼钢兴趣小组的算法知识备份](https://quant67.com/) | 主要写编程、技术、安全。 | Engineering & Technology | [RSS](https://quant67.com/rss.xml) | all, blogs, chinese, engineering |
| [土豆不好吃](https://dmesg.app) | 主要写编程。 | Engineering & Technology | [RSS](https://dmesg.app/feed) | all, blogs, chinese, engineering |
| [坠月川](https://www.hujingnb.com) | 主要写编程、技术。 | Engineering & Technology | [RSS](https://hujingnb.com/feed) | all, blogs, chinese, engineering |
| [夜法之书](https://blog.17lai.site) | 主要写技术、开源、hexo、成长。 | Engineering & Technology | [RSS](https://blog.17lai.site/atom.xml) | all, blogs, chinese, engineering |
| [失眠海峡](https://blog.imalan.cn/) | 主要写编程、日常、二次元、读书。 | Engineering & Technology | [RSS](https://blog.imalan.cn/feed.xml) | all, blogs, chinese, engineering |
| [如有乐享](https://51.ruyo.net) | 主要写技术、分享。 | Engineering & Technology | [RSS](https://51.ruyo.net/feed) | all, blogs, chinese, engineering |
| [姓王者的博客](https://xingwangzhe.fun/) | 主要写编程，随笔，大学，生活，开源。 | Engineering & Technology | [RSS](https://xingwangzhe.fun/rss.xml) | all, blogs, chinese, engineering |
| [寒夜雨](https://www.coderlock.site/) | 主要写编程、生活、AI、随想。 | Engineering & Technology | [RSS](https://www.coderlock.site/index.php/feed/) | ai, all, blogs, chinese, engineering |
| [崎径 其镜](http://www.z16388.top/atom.xml) | 主要写编程、游戏、音乐。 | Engineering & Technology | [RSS](http://www.z16388.top/atom.xml) | all, blogs, chinese, engineering |
| [嵌入式工程猫的博客](https://blog.vvzero.com) | 主要写软硬件全栈开发、生活。 | Engineering & Technology | [RSS](https://blog.vvzero.com/atom.xml) | all, blogs, chinese, engineering |
| [张戈博客](https://zhang.ge) | 主要写编程、运维。 | Engineering & Technology | [RSS](https://zhang.ge/feed) | all, blogs, chinese, engineering |
| [张洪Heo](https://blog.zhheo.com/) | 主要写设计、编程、生活、产品。 | Engineering & Technology | [RSS](https://blog.zhheo.com/rss.xml) | all, blogs, chinese, engineering |
| [张鑫旭-鑫空间-鑫生活](https://www.zhangxinxu.com/wordpress) | 主要写编程、前端。 | Engineering & Technology | [RSS](http://www.zhangxinxu.com/wordpress/?feed=rss2) | all, blogs, chinese, engineering |
| [愆伏](https://www.tortorse.com/atom.xml) | 主要写产品、前端、设计、杂谈。 | Engineering & Technology | [RSS](https://www.tortorse.com/atom.xml) | all, blogs, chinese, engineering |
| [我不是咕咕鸽](https://blog.laoda.de) | 主要写编程、技术分享、网络、容器。 | Engineering & Technology | [RSS](https://blog.laoda.de/rss.xml) | all, blogs, chinese, engineering |
| [所谓空想](https://www.alxh.page) | 主要写文学、音乐、技术。 | Engineering & Technology | [RSS](https://www.alxh.page/feed.rss) | all, blogs, chinese, engineering |
| [把酒诗代码](https://102no.com/) | 主要写编程、随笔。 | Engineering & Technology | [RSS](https://102no.com/atom.xml) | all, blogs, chinese, engineering |
| [披萨盒的赛博日志](https://blog.pushihao.com/atom.xml) | 主要写编程、AI、全栈、思考。 | Engineering & Technology | [RSS](https://blog.pushihao.com/atom.xml) | ai, all, blogs, chinese, engineering |
| [敖苛记](https://blog.kayro.cn/) | 主要写生活、技术、编程、开源。 | Engineering & Technology | [RSS](https://blog.kayro.cn/atom.xml) | all, blogs, chinese, engineering |
| [文武科技柜](https://www.wangdu.site) | 主要写编程、软件、随笔、生活。 | Engineering & Technology | [RSS](https://www.wangdu.site/feed) | all, blogs, chinese, engineering |
| [文艺数学君](https://mathpretty.com) | 主要写编程、生活、数学。 | Engineering & Technology | [RSS](https://mathpretty.com/feed/) | all, blogs, chinese, engineering |
| [方永、南天紫雲](https://www.vinoca.org) | 主要写编程、随笔。 | Engineering & Technology | [RSS](https://www.vinoca.org/atom.xml) | all, blogs, chinese, engineering |
| [明立非\|Mingnify的博客](https://mingnify.com/zh/blog/atom.xml) | 主要写Indie Maker、独立开发、AI、打造产品。 | Engineering & Technology | [RSS](https://mingnify.com/zh/blog/atom.xml) | ai, all, blogs, chinese, engineering |
| [星觅海的博客](https://www.xmhai.cn) | 主要写技术、生活、资源。 | Engineering & Technology | [RSS](https://www.xmhai.cn/rss.xml) | all, blogs, chinese, engineering |
| [映屿](https://blog.verdant.ee/) | 主要写技术、随笔、思考、阅读。 | Engineering & Technology | [RSS](https://www.glowisle.me/atom.xml) | all, blogs, chinese, engineering |
| [晓空blog](https://blog.moeworld.tech) | 主要写生活、开发，日常、二次元、游戏。 | Engineering & Technology | [RSS](https://blog.moeworld.tech/feed/) | all, blogs, chinese, engineering |
| [晴雀堂](https://blog.verynb.net/atom.xml) | 主要写技术、随笔、思考、成长。 | Engineering & Technology | [RSS](https://hehysh.github.io/atom.xml) | all, blogs, chinese, engineering |
| [朝舞网](https://ii74.com/) | 主要写编程、随笔。 | Engineering & Technology | [RSS](https://ii74.com/feed.php) | all, blogs, chinese, engineering |
| [杜老师说](https://dusays.com/) | 主要写运维，数码，资源。 | Engineering & Technology | [RSS](https://dusays.com/atom.xml) | all, blogs, chinese, engineering |
| [枫林灯语](https://blog.mfwt.top/) | 主要写编程、生活、技术、无线电。 | Engineering & Technology | [RSS](https://blog.mfwt.top/index.php/feed/) | all, blogs, chinese, engineering |
| [橙树志 ｜ citydatum](https://citydatum.cn) | 主要写城市、数据分析、技术、视觉。 | Engineering & Technology | [RSS](https://citydatum.cn/feed) | all, blogs, chinese, engineering |
| [欧雷流](https://ourai.ws/) | 主要写编程、前端、生活、思考。 | Engineering & Technology | [RSS](https://ourai.ws/atom.xml) | all, blogs, chinese, engineering |
| [歌词经理](https://blog.lyric.im/feed/atom) | 主要写产品、创业、编程。 | Engineering & Technology | [RSS](https://quaily.com/lyric/feed/atom) | all, blogs, chinese, engineering |
| [残页的小博客](https://blog.canyie.top/) | 主要写编程、Android、生活。 | Engineering & Technology | [RSS](https://blog.canyie.top/atom.xml) | all, blogs, chinese, engineering |
| [泠泫凝的异次元空间](https://lxnchan.cn/atom.xml) | 主要写运维、后端。 | Engineering & Technology | [RSS](https://lxnchan.cn/atom.xml) | all, blogs, chinese, engineering |
| [泫言](https://blog.cugxuan.cn/) | 主要写生活、编程、科技、记录。 | Engineering & Technology | [RSS](https://blog.cugxuan.cn/atom.xml) | all, blogs, chinese, engineering |
| [流动](https://liudon.com/) | 主要写技术、生活。 | Engineering & Technology | [RSS](https://liudon.com/index.xml) | all, blogs, chinese, engineering |
| [浅时光博客](https://www.dqzboy.com) | 主要写编程、技术分享、学习笔记。 | Engineering & Technology | [RSS](https://www.dqzboy.com/feed) | all, blogs, chinese, engineering |
| [涛叔](https://tao.zz.ac) | 主要写技术、学习、思考。 | Engineering & Technology | [RSS](https://taoshu.in/feed.xml) | all, blogs, chinese, engineering |
| [润土分享](https://runtushare.net) | 主要写编程。 | Engineering & Technology | [RSS](http://xiaix.me/rss/) | all, blogs, chinese, engineering |
| [清竹志-(原清竹茶馆)](https://blog.vadxq.com/atom.xml) | 主要写编程、前端、全栈、生活。 | Engineering & Technology | [RSS](https://blog.vadxq.com/atom.xml) | all, blogs, chinese, engineering |
| [游魂博客](https://www.iyouhun.com/) | 主要写编程、前端、技术、生活。 | Engineering & Technology | [RSS](https://www.iyouhun.com/rss.php) | all, blogs, chinese, engineering |
| [澄沨的漫游茶记](https://champhoon.xyz/) | 主要写ACG、日常、随笔、技术。 | Engineering & Technology | [RSS](https://champhoon.xyz/atom.xml) | all, blogs, chinese, engineering |
| [烧饼博客](https://u.sb/) | 主要写运维、域名。 | Engineering & Technology | [RSS](https://u.sb/rss.xml) | all, blogs, chinese, engineering |
| [猫涅的秘密结社](http://www.maonie.top/) | 主要写技术、信息安全、随笔、编程。 | Engineering & Technology | [RSS](https://www.maonie.top/atom.xml) | all, blogs, chinese, engineering |
| [猿客随笔](https://monkeyke.com/) | 主要写编程、生活、随笔。 | Engineering & Technology | [RSS](https://monkeyke.com/index.xml) | all, blogs, chinese, engineering |
| [王圆圆 - ICONPIK](https://www.iconpik.com/) | 主要写AI、编程、随笔。 | Engineering & Technology | [RSS](https://www.iconpik.com/rss/) | ai, all, blogs, chinese, engineering |
| [王欣说AI](https://wangxin.io/) | 主要写后端、开源、RPC、微服务。 | Engineering & Technology | [RSS](https://wangxin.io/atom.xml) | all, blogs, chinese, engineering |
| [王登科-DK博客](https://greatdk.com) | 主要写编程、创业。 | Engineering & Technology | [RSS](https://greatdk.com/feed) | all, blogs, chinese, engineering |
| [王福强的个人博客：一个架构士的思考与沉淀](http://afoo.me) | 主要写架构、创业、思考。 | Engineering & Technology | [RSS](https://afoo.me/feeds.xml) | all, blogs, chinese, engineering |
| [瓦解的生活记事](https://hin.cool/atom.xml) | 主要写分享、记录、技术、写作。 | Engineering & Technology | [RSS](https://hin.cool/atom.xml) | all, blogs, chinese, engineering |
| [白宦成](https://www.ixiqin.com) | 主要写编程、开源。 | Engineering & Technology | [RSS](https://www.ixiqin.com/feed/) | all, blogs, chinese, engineering |
| [白菜](https://blog.baicai.me/) | 主要写随笔、技术、经验、旅行。 | Engineering & Technology | [RSS](https://blog.baicai.me/index.xml) | all, blogs, chinese, engineering |
| [皓子的小站](https://howiehz.top) | 主要写技术、编程、开源、前端。 | Engineering & Technology | [RSS](https://howiehz.top/rss.xml) | all, blogs, chinese, engineering |
| [看川博客](https://kanchuan.com/blog) | 主要写iOS、开发、产品、生活。 | Engineering & Technology | [RSS](https://kanchuan.com/feed.xml) | all, blogs, chinese, engineering |
| [码农明明桑](https://isming.me/?utm_source=rss) | 主要写技术、生活、旅行、读书。 | Engineering & Technology | [RSS](https://isming.me/index.xml) | all, blogs, chinese, engineering |
| [码录集](https://www.coderlog.net) | 主要写编程、AI、C#、.NET。 | Engineering & Technology | [RSS](https://www.coderlog.net/rss.xml) | ai, all, blogs, chinese, engineering |
| [空屿](https://pinaland.cn/) | 主要写日常、二次元、动画、游戏。 | Engineering & Technology | [RSS](https://pinaland.cn/feed/) | all, blogs, chinese, engineering |
| [空鸣深语](https://blog.deepchirp.com/) | 主要写技术、生活、随笔。 | Engineering & Technology | [RSS](https://blog.deepchirp.com/atom.xml) | all, blogs, chinese, engineering |
| [竹林里有冰的博客](https://zhul.in) | 主要写技术、折腾、笔记、分享。 | Engineering & Technology | [RSS](https://zhul.in/rss.xml) | all, blogs, chinese, engineering |
| [粥里有勺糖](https://sugarat.top) | 主要写编程、大前端、开源、生活。 | Engineering & Technology | [RSS](https://sugarat.top/feed.rss) | all, blogs, chinese, engineering |
| [繁星点点](https://blog.52013120.xyz) | 主要写编程、技术、原创、网络。 | Engineering & Technology | [RSS](https://blog.52013120.xyz/rss.xml) | all, blogs, chinese, engineering |
| [维基萌](https://www.wikimoe.com) | 主要写动画、漫画、游戏、日常。 | Engineering & Technology | [RSS](https://www.wikimoe.com/rss.php) | all, blogs, chinese, engineering |
| [罗磊的独立博客](https://luolei.org) | 主要写编程、旅行。 | Engineering & Technology | [RSS](http://luolei.org/feed/) | all, blogs, chinese, engineering |
| [翔宇工作流](https://xiangyugongzuoliu.com/) | 主要写AI、编程、自动化、Claude Code。 | Engineering & Technology | [RSS](https://xiangyugongzuoliu.com/latest/rss/) | ai, all, blogs, chinese, engineering |
| [老范讲故事｜AI、大模型与商业世界的故事](https://lukefan.com) | 主要写编程。 | Engineering & Technology | [RSS](http://lukefan.com/?feed=rss2) | all, blogs, chinese, engineering |
| [肘子的 Swift 记事本 ｜ Fatbobman's Blog](https://fatbobman.com/) | 主要写编程、Swift、SwiftUI。 | Engineering & Technology | [RSS](https://fatbobman.com/zh/rss.xml) | all, blogs, chinese, engineering |
| [胡涂说](https://hutusi.com) | 主要写编程、随笔、生活。 | Engineering & Technology | [RSS](https://hutusi.com/feed.xml) | all, blogs, chinese, engineering |
| [草梅友仁的博客](https://blog.cmyr.ltd/atom.xml) | 主要写编程、技术、前端、日常。 | Engineering & Technology | [RSS](https://blog.cmyr.ltd/atom.xml) | all, blogs, chinese, engineering |
| [莫尔索随笔](https://liduos.com/atom.xml) | 主要写Python、SDN、读书笔记、LLM应用开发。 | Engineering & Technology | [RSS](https://liduos.com/atom.xml) | all, blogs, chinese, engineering |
| [蒙需](https://jiangcl.com) | 主要写法律、生活、编程、工程。 | Engineering & Technology | [RSS](https://jiangcl.com/feed) | all, blogs, chinese, engineering |
| [虹墨空间站](https://www.imaegoo.com/) | 主要写编程、前端、Serverless。 | Engineering & Technology | [RSS](https://www.imaegoo.com/atom.xml) | all, blogs, chinese, engineering |
| [蚊子的前端博客](https://www.xiabingbao.com) | 主要写编程、前端。 | Engineering & Technology | [RSS](https://www.xiabingbao.com/atom.xml) | all, blogs, chinese, engineering |
| [謝懿Shine](https://www.futseyi.com/) | 主要写技术开源、大模型、AI、生活。 | Engineering & Technology | [RSS](https://xieyi.org/rss.xml) | ai, all, blogs, chinese, engineering |
| [豌豆花下猫](https://pythoncat.top/) | 主要写编程、Python、翻译、随笔。 | Engineering & Technology | [RSS](https://pythoncat.top/rss.xml) | all, blogs, chinese, engineering |
| [轶哥博客](https://www.wyr.me) | 主要写编程、全栈、随笔。 | Engineering & Technology | [RSS](https://www.wyr.me/rss.xml) | all, blogs, chinese, engineering |
| [运维咖啡吧](https://blog.ops-coffee.com/atom.xml) | 主要写devops、运维、自动化开发、技术。 | Engineering & Technology | [RSS](https://blog.ops-coffee.cn/feed.xml) | all, blogs, chinese, engineering |
| [运维开发绿皮书](https://www.geekery.cn/) | 主要写技术、生活、开源。 | Engineering & Technology | [RSS](https://www.geekery.cn/rss.xml) | all, blogs, chinese, engineering |
| [远飞闲记](https://heyuanfei.com/) | 主要写阅读、思考、生活、技术。 | Engineering & Technology | [RSS](https://leonhe.cn/index.xml) | all, blogs, chinese, engineering |
| [迷途小书童的Note](https://xugaoxiang.com/) | 主要写工作、编程、技术。 | Engineering & Technology | [RSS](https://xugaoxiang.com/feed) | all, blogs, chinese, engineering |
| [逸思杂陈](https://blog.ponder.work/atom.xml) | 主要写编程、随笔。 | Engineering & Technology | [RSS](https://blog.ponder.work/atom.xml) | all, blogs, chinese, engineering |
| [酥米的小站](https://www.sumi233.top/) | 主要写生活，技术，网络，日常，随笔。 | Engineering & Technology | [RSS](https://www.sumi233.top/rss.xml) | all, blogs, chinese, engineering |
| [阁子](https://dfine.tech/atom.xml) | 主要写编程、算法、生活。 | Engineering & Technology | [RSS](https://dfine.tech/atom.xml) | all, blogs, chinese, engineering |
| [阿尔的代码屋 \| 全栈技术笔记](https://blog.algieba12.cn/) | 主要写随笔、AI、游戏开发、C++。 | Engineering & Technology | [RSS](https://blog.algieba12.cn/atom.xml) | ai, all, blogs, chinese, engineering |
| [阿掖山·博客](https://blog.mountaye.com) | 主要写物理、生物、编程、摄影。 | Engineering & Technology | [RSS](https://blog.mountaye.com/feed.xml) | all, blogs, chinese, engineering |
| [雪猫社](https://www.yukicat.net) | 主要写生活、随笔、运维、思考。 | Engineering & Technology | [RSS](https://www.yukicat.net/feed/) | all, blogs, chinese, engineering |
| [雪的数字花园 ❄️](https://blog.rnm.gv.uy/) | 主要写编程、开源、前端、折腾。 | Engineering & Technology | [RSS](https://blog.rnm.gv.uy/atom.xml) | all, blogs, chinese, engineering |
| [青石坞](https://www.qs5.org/) | 主要写技术、生活。 | Engineering & Technology | [RSS](https://www.qs5.org/feed/) | all, blogs, chinese, engineering |
| [非学·派'](https://fxpai.com) | 主要写摄影、技术、随笔。 | Engineering & Technology | [RSS](https://fxpai.com/feed) | all, blogs, chinese, engineering |
| [顶尖研发](https://bestcoder.cn/) | 主要写日常、随笔、技术。 | Engineering & Technology | [RSS](https://bestcoder.cn/feed) | all, blogs, chinese, engineering |
| [首页 on black8](https://0x8.net/) | 主要写编程、技术、linux、生活。 | Engineering & Technology | [RSS](https://unixetc.com/index.xml) | all, blogs, chinese, engineering |
| [鸟窝](https://colobu.com/) | 主要写编程。 | Engineering & Technology | [RSS](https://colobu.com/atom.xml) | all, blogs, chinese, engineering |
| [黑羽的个人博客](https://blog.thetbw.xyz) | 主要写编程、随笔、生活。 | Engineering & Technology | [RSS](https://blog.thetbw.xyz/atom.xml) | all, blogs, chinese, engineering |
| [𝟞𝟙𝟡'𝕤 𝔹𝕃𝕆𝔾](https://619.pp.ua) | 主要写学习、编程、随笔。 | Engineering & Technology | [RSS](https://66619.eu.org/feed/) | all, blogs, chinese, engineering |

</details>

<details>
<summary>Research & Science · 19</summary>

| Source | Description | Primary category | Feed | Bundles |
| --- | --- | --- | --- | --- |
| [AAAS: Science: Table of Contents](https://www.science.org/loi/science?af=R) | Research & Science 订阅源 | Research & Science | [RSS](https://www.science.org/action/showFeed?type=etoc&feed=rss&jc=science) | all, research |
| [All Top News -- ScienceDaily](https://www.sciencedaily.com/news/top/) | Research & Science 订阅源 | Research & Science | [RSS](https://www.sciencedaily.com/rss/top/science.xml) | all, research |
| [Amazon Science](https://www.amazon.science/) | Research & Science 订阅源 | Research & Science | [RSS](https://www.amazon.science/index.rss) | all, research |
| [BBC News — Science](https://www.bbc.co.uk/news/science_and_environment) | Research & Science 订阅源 | Research & Science | [RSS](https://feeds.bbci.co.uk/news/science_and_environment/rss.xml) | all, research |
| [eLife: latest articles](https://elifesciences.org) | Research & Science 订阅源 | Research & Science | [RSS](https://elifesciences.org/rss/recent.xml) | all, research |
| [FlowingData](https://flowingdata.com) | Research & Science 订阅源 | Research & Science | [RSS](https://flowingdata.com/feed) | all, research |
| [Latest Science News -- ScienceDaily](https://www.sciencedaily.com/news/) | Research & Science 订阅源 | Research & Science | [RSS](https://www.sciencedaily.com/rss/all.xml) | all, research |
| [NASA](https://www.nasa.gov) | Research & Science 订阅源 | Research & Science | [RSS](https://www.nasa.gov/news-release/feed/) | all, research |
| [Nature](http://feeds.nature.com/nature/rss/current) | Research & Science 订阅源 | Research & Science | [RSS](https://www.nature.com/nature.rss) | all, research |
| [NYT > Science](https://www.nytimes.com/section/science) | Research & Science 订阅源 | Research & Science | [RSS](https://rss.nytimes.com/services/xml/rss/nyt/Science.xml) | all, research |
| [Phys.org - latest science and technology news stories](https://phys.org/) | Research & Science 订阅源 | Research & Science | [RSS](https://phys.org/rss-feed/) | all, research |
| [PLOS One](https://journals.plos.org/plosone/) | Research & Science 订阅源 | Research & Science | [RSS](https://journals.plos.org/plosone/feed/atom) | all, research |
| [Quanta Magazine](https://www.quantamagazine.org) | Research & Science 订阅源 | Research & Science | [RSS](https://www.quantamagazine.org/feed/) | all, research |
| [Science Latest](https://www.wired.com) | Research & Science 订阅源 | Research & Science | [RSS](https://www.wired.com/feed/category/science/latest/rss) | all, research |
| [Scientific American Content: Global](https://www.scientificamerican.com) | Research & Science 订阅源 | Research & Science | [RSS](http://rss.sciam.com/ScientificAmerican-Global) | all, research |
| [Space \| The Guardian](https://www.theguardian.com/science/space) | Research & Science 订阅源 | Research & Science | [RSS](https://www.theguardian.com/science/space/rss) | all, research |
| [Space – latest in science and technology \| New Scientist](https://www.newscientist.com/subject/space/) | Research & Science 订阅源 | Research & Science | [RSS](https://www.newscientist.com/subject/space/feed/) | all, research |
| [腾讯研究院](https://wechat2rss.bestblogs.dev/feed/6152301e0978bffb0a8284cab339262b9764dcfb.xml) | Research & Science 订阅源 | Research & Science | [RSS](https://wechat2rss.bestblogs.dev/feed/6152301e0978bffb0a8284cab339262b9764dcfb.xml) | all, chinese, research |
| [阿里研究院](https://wechat2rss.bestblogs.dev/feed/e2f1190c120f7f3d74b630bfcfe9e58296bd535c.xml) | Research & Science 订阅源 | Research & Science | [RSS](https://wechat2rss.bestblogs.dev/feed/e2f1190c120f7f3d74b630bfcfe9e58296bd535c.xml) | all, chinese, research |

</details>

<details>
<summary>News · 34</summary>

| Source | Description | Primary category | Feed | Bundles |
| --- | --- | --- | --- | --- |
| [36氪](http://36kr.com) | News 订阅源 | News | [RSS](https://www.36kr.com/feed) | all, chinese, news |
| [AIGC Weekly](https://quaily.com/op7418/feed/atom) | News 订阅源 | News | [RSS](https://quaily.com/op7418/feed/atom) | all, news |
| [Al Jazeera – Breaking News, World News and Video from Al Jazeera](https://www.aljazeera.com) | News 订阅源 | News | [RSS](https://www.aljazeera.com/xml/rss/all.xml) | all, news |
| [BBC News — News](https://www.bbc.co.uk/news/world) | News 订阅源 | News | [RSS](https://feeds.bbci.co.uk/news/world/rss.xml) | all, news |
| [Cointelegraph.com News](https://cointelegraph.com) | News 订阅源 | News | [RSS](https://cointelegraph.com/rss/tag/blockchain) | all, news |
| [Engadget - Technology News & Expert Reviews](https://www.engadget.com/) | News 订阅源 | News | [RSS](https://www.engadget.com/rss.xml) | all, news |
| [Golang Weekly](https://golangweekly.com/) | News 订阅源 | News | [RSS](https://golangweekly.com/rss/) | all, news |
| [HackerNews每日摘要 on SuperTechFans](https://supertechfans.com/cn/) | News 订阅源 | News | [RSS](https://www.supertechfans.com/cn/index.xml) | all, chinese, news |
| [InfoQ — News](https://www.infoq.com) | News 订阅源 | News | [RSS](https://feed.infoq.com/) | all, news |
| [InfoQ 推荐](https://www.infoq.cn) | News 订阅源 | News | [RSS](https://plink.anyfeeder.com/infoq/recommend) | all, chinese, news |
| [IT之家](https://www.ithome.com/) | News 订阅源 | News | [RSS](https://www.ithome.com/rss/) | all, chinese, news |
| [MIT 科技评论 - 本周热榜](https://www.mittrchina.com/hot) | News 订阅源 | News | [RSS](https://rsshub.bestblogs.dev/mittrchina/hot) | all, chinese, news |
| [News from Google](https://blog.google/) | News 订阅源 | News | [RSS](https://blog.google/rss) | all, engineering, news |
| [NPR Topics: World](https://www.npr.org/templates/story/story.php?storyId=1004) | News 订阅源 | News | [RSS](https://feeds.npr.org/1004/rss.xml) | all, news |
| [NYT > Technology](https://www.nytimes.com/section/technology) | News 订阅源 | News | [RSS](https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml) | all, news |
| [NYT > World News](https://www.nytimes.com/section/world) | News 订阅源 | News | [RSS](https://rss.nytimes.com/services/xml/rss/nyt/World.xml) | all, news |
| [ProPublica](https://www.propublica.org/) | News 订阅源 | News | [RSS](https://www.propublica.org/feeds/propublica/main) | all, news |
| [TechCrunch](https://techcrunch.com/) | News 订阅源 | News | [RSS](https://techcrunch.com/feed/) | all, news |
| [The Verge — News](https://www.theverge.com) | News 订阅源 | News | [RSS](https://www.theverge.com/rss/index.xml) | all, news |
| [Top stories - Google News](https://news.google.com/?hl=en-US&gl=US&ceid=US:en) | News 订阅源 | News | [RSS](https://news.google.com/rss) | all, news |
| [WIRED](https://www.wired.com) | News 订阅源 | News | [RSS](https://www.wired.com/feed/rss) | all, news |
| [World](https://www.washingtonpost.com) | News 订阅源 | News | [RSS](https://feeds.washingtonpost.com/rss/world) | all, news |
| [World news \| The Guardian](https://www.theguardian.com/world) | News 订阅源 | News | [RSS](https://www.theguardian.com/world/rss) | all, news |
| [World News, Today World News, Latest International News, World Breaking News, Trending News of World - Times of India](https://timesofindia.indiatimes.com/world) | News 订阅源 | News | [RSS](https://timesofindia.indiatimes.com/rssfeeds/296589292.cms) | all, news |
| [大橘和朋友们的周刊](https://rrorangeandfriends.de) | News 订阅源 | News | [RSS](https://rrorangeandfriends.de/feed.xml) | all, chinese, news |
| [奇客Solidot–传递最新科技情报](https://www.solidot.org) | News 订阅源 | News | [RSS](https://www.solidot.org/index.rss) | all, chinese, news |
| [安全客-有思想的安全新媒体](https://www.anquanke.com) | News 订阅源 | News | [RSS](https://api.anquanke.com/data/v1/rss) | all, chinese, news |
| [少数派](https://sspai.com) | News 订阅源 | News | [RSS](https://sspai.com/feed) | all, chinese, news |
| [掘金本周最热](https://juejin.im/recommended?sort=weekly_hottest) | News 订阅源 | News | [RSS](https://rsshub.bestblogs.dev/juejin/trending/all/weekly) | all, chinese, news |
| [潮流周刊](https://weekly.tw93.fun/) | News 订阅源 | News | [RSS](https://weekly.tw93.fun/rss.xml) | all, chinese, news |
| [站长之家](http://www.chinaz.com) | News 订阅源 | News | [RSS](https://app.chinaz.com/?app=rss) | all, chinese, news |
| [蓝点网](https://www.landian.news) | News 订阅源 | News | [RSS](https://www.landiannews.com/feed) | all, chinese, news |
| [虎嗅](https://www.huxiu.com) | News 订阅源 | News | [RSS](https://rss.huxiu.com/) | all, chinese, news |
| [钛媒体：引领未来商业与生活新知](http://www.tmtpost.com) | News 订阅源 | News | [RSS](https://www.tmtpost.com/feed) | all, chinese, news |

</details>

<details>
<summary>Product & Design · 4</summary>

| Source | Description | Primary category | Feed | Bundles |
| --- | --- | --- | --- | --- |
| [61’s life](https://61.life/) | 主要写创业、管理、产品。 | Product & Design | [RSS](https://61.life/feed.xml) | all, blogs, chinese |
| [jax](https://cdjax.com) | 主要写产品、数码、随笔。 | Product & Design | [RSS](https://cdjax.com/?feed=rss2) | all, blogs, chinese |
| [Velas电波站](https://www.velasx.com/) | 主要写动画、游戏、小说、设计。 | Product & Design | [RSS](https://www.velasx.com/feed) | all, blogs, chinese |
| [拾月的博客](https://www.skyue.com/) | 主要写生活、股票投资、产品经理、软件数码。 | Product & Design | [RSS](https://www.skyue.com/feed/) | all, blogs, chinese |

</details>

<details>
<summary>Business & Startups · 5</summary>

| Source | Description | Primary category | Feed | Bundles |
| --- | --- | --- | --- | --- |
| [Macin](https://macin.org/atom.xml) | 主要写分享、投资、学习、Crypto。 | Business & Startups | [RSS](https://www.macin.org/atom.xml) | all, blogs, chinese |
| [扯氮集](http://weiwuhui.com) | 主要写创业、人生。 | Business & Startups | [RSS](http://weiwuhui.com/feed) | all, blogs, chinese |
| [知足常乐-水星投资理财的基本意念](http://mercurychong.blogspot.com/) | 主要写投资。 | Business & Startups | [RSS](http://mercurychong.blogspot.com/feeds/posts/default) | all, blogs, chinese |
| [虹线](https://1q43.blog) | 主要写商业、社科、科技、生活。 | Business & Startups | [RSS](https://1q43.blog/feed) | all, blogs, chinese |
| [雷蒙三十｜幫助忙碌現代人的聰明工作、好好生活的生產力指南](https://raymondhouch.com) | 主要写创业、数码、数字游民、生产力工具。 | Business & Startups | [RSS](https://raymondhouch.com/feed) | all, blogs, chinese |

</details>

<details>
<summary>Personal Blogs · 65</summary>

| Source | Description | Primary category | Feed | Bundles |
| --- | --- | --- | --- | --- |
| [ABB00717](https://blog.abb00717.com) | 主要写資訊安全、程式設計、技術、寫作。 | Personal Blogs | [RSS](https://blog.abb00717.com/index.xml) | all, blogs, chinese |
| [Another Dayu](https://anotherdayu.com/) | 主要写日常、流行病与卫生统计、科技、数码。 | Personal Blogs | [RSS](https://anotherdayu.com/feed/) | all, blogs, chinese |
| [Blog \| Lyunvy](https://blog.lyunvy.top/) | 主要写生活、学习。 | Personal Blogs | [RSS](https://blog.lyunvy.top/atom.xml) | all, blogs, chinese |
| [BMPI](https://www.bmpi.dev/) | 主要写Learn、Dev、Trade。 | Personal Blogs | [RSS](https://www.bmpi.dev/index.xml) | all, blogs, chinese |
| [by Upsangel](https://upsangel.com/) | 主要写网路硬件、NAS、单板电脑、记录。 | Personal Blogs | [RSS](https://upsangel.com/feed/) | all, blogs, chinese |
| [Conge](https://conge.livingwithfcs.org/) | 主要写生活、跑步、阅读。 | Personal Blogs | [RSS](https://conge.github.io/feed.xml) | all, blogs, chinese |
| [Cosmos的博客](https://cosmo-polite.com) | 主要写北美生活、思维碎片。 | Personal Blogs | [RSS](https://cosmo-polite.com/feed/) | all, blogs, chinese |
| [David Blog](https://blog.blahaj.uk/) | 主要写生活、随笔、影评、作品集。 | Personal Blogs | [RSS](https://blog.blahaj.uk/feed) | all, blogs, chinese |
| [Deep Router](https://deeprouter.org/) | 主要写路由器、家庭网络、工具、OpenWRT。 | Personal Blogs | [RSS](https://deeprouter.org/rss/feed.xml) | all, blogs, chinese |
| [Dejavu's Blog](https://blog.dejavu.moe/) | 主要写折腾、学习、生活、日志。 | Personal Blogs | [RSS](https://blog.dejavu.moe/index.xml) | all, blogs, chinese |
| [Dort 的博客](https://blog.dort.me/) | 主要写随笔、生活、记录。 | Personal Blogs | [RSS](https://blog.dort.me/rss.xml) | all, blogs, chinese |
| [Evan's Space](https://www.evan.xin) | 主要写生活。 | Personal Blogs | [RSS](https://evan.xin/feed) | all, blogs, chinese |
| [Fei's Tours & Tales](https://www.feifun.cn/feed.xml) | 主要写旅行、复古计算设备、随笔。 | Personal Blogs | [RSS](https://www.feifun.cn/feed.xml) | all, blogs, chinese |
| [Fernweh](https://blog.wohin.me/) | 主要写信息安全、诗歌、随笔。 | Personal Blogs | [RSS](https://blog.wohin.me/index.xml) | all, blogs, chinese |
| [GentleLucky](https://blog.gentlelucky.com/zh/) | 主要写随笔、思考、Java、知识管理。 | Personal Blogs | [RSS](https://blog.gentlelucky.com/zh/index.xml) | all, blogs, chinese |
| [happy xiao](https://happyxiao.com) | 主要写个人成长。 | Personal Blogs | [RSS](https://happyxiao.com/feed) | all, blogs, chinese |
| [ImPatrick](https://impatrick.blog) | 主要写繁中、攝影、生活、記錄。 | Personal Blogs | [RSS](https://impatrick.blog/feed/) | all, blogs, chinese |
| [Jake blog](https://jaketao.com) | 主要写硅谷科技、主机游戏、留学旅居、跨境电商。 | Personal Blogs | [RSS](https://jaketao.com/feed/) | all, blogs, chinese |
| [Jame](https://jame.work/) | 主要写随笔。 | Personal Blogs | [RSS](https://jame.work/feed.xml) | all, blogs, chinese |
| [JustZht's EchoChamber](https://www.justzht.com/) | 主要写随笔。 | Personal Blogs | [RSS](https://www.justzht.com/rss/) | all, blogs, chinese |
| [jz's ramblings](https://ramble.imzh.me/) | 主要写随笔。 | Personal Blogs | [RSS](https://ramble.imzh.me/index.xml) | all, blogs, chinese |
| [LCZBlog](https://blog.licaoz.com/) | 主要写生活、笔记。 | Personal Blogs | [RSS](https://blog.licaoz.com/feed/) | all, blogs, chinese |
| [LoRexxar's Blog \| 信息技术分享](https://lorexxar.cn/atom.xml) | 主要写安全。 | Personal Blogs | [RSS](https://lorexxar.cn/atom.xml) | all, blogs, chinese |
| [M-x Chris-An-Emacser](https://chriszheng.science/) | 主要写随笔、Emacs。 | Personal Blogs | [RSS](https://chriszheng.science/atom.xml) | all, blogs, chinese |
| [Markon Review](https://markonreview.com/) | 主要写游戏及产业评论。 | Personal Blogs | [RSS](https://markonreview.com/rss/) | all, blogs, chinese |
| [Redish101 Blog](https://blog.redish101.top/) | 主要写Python、Java、随笔。 | Personal Blogs | [RSS](https://blog.redish101.top/atom.xml) | all, blogs, chinese |
| [Save the Web Project](https://blog.save-web.org) | 主要写存档、备份、互联网、公益。 | Personal Blogs | [RSS](https://blog.save-web.org/feed/) | all, blogs, chinese |
| [SEISAMUSE](https://www.seis-jun.xyz/atom.xml) | 主要写科研、学习、生活。 | Personal Blogs | [RSS](https://www.seis-jun.xyz/atom.xml) | all, blogs, chinese |
| [Shuibaco • 水八口](http://shuiba.co/) | 主要写日常、旅途、思考。 | Personal Blogs | [RSS](https://shuiba.co/feed) | all, blogs, chinese |
| [Spring](https://spring.io) | Personal Blogs 订阅源 | Personal Blogs | [RSS](https://spring.io/blog.atom) | all, engineering |
| [SuperGrey 的筆記本](https://blog.supergrey.uk) | 主要写阅读随笔、动漫影评。 | Personal Blogs | [RSS](https://supergrey.bearblog.dev/rss/) | all, blogs, chinese |
| [tplate](https://trle5.xyz) | 主要写综合、杂谈、教程。 | Personal Blogs | [RSS](https://trle5.xyz/atom.xml) | all, blogs, chinese |
| [whyes 的博客](http://whyes.org/) | 主要写医学、科研、临床研究、硬件。 | Personal Blogs | [RSS](https://whyes.org/feed.xml) | all, blogs, chinese |
| [WSH](https://www.wsh233.cn) | 主要写生活、随笔、GISer、地信。 | Personal Blogs | [RSS](https://www.wsh233.cn/feed.xml) | all, blogs, chinese |
| [Wulu's Blog](https://wulu.zone/posts/) | 主要写笔记、经验分享、学习、教育。 | Personal Blogs | [RSS](https://wulu.zone/feed/post.xml) | all, blogs, chinese |
| [一派胡言 · Blog](https://yipai.me/blog) | 主要写胡一派、随笔、不折腾。 | Personal Blogs | [RSS](https://yipai.me/feed) | all, blogs, chinese |
| [不吐不快](https://mianao.info/atom.xml) | 主要写生活、硬件、教程、DIY。 | Personal Blogs | [RSS](https://mianao.info/atom.xml) | all, blogs, chinese |
| [专享生活](https://zhjwork.online) | 主要写专利、科技、随笔、法律。 | Personal Blogs | [RSS](https://zhjwork.online/feed) | all, blogs, chinese |
| [云心怀鹤](https://bluehe.cn/) | 主要写生活、生活方式、风光摄影、科技。 | Personal Blogs | [RSS](https://bluehe.cn/feed/) | all, blogs, chinese |
| [卢昌海个人主页](http://www.changhai.org) | 主要写物理、科普。 | Personal Blogs | [RSS](https://www.changhai.org/feed.xml) | all, blogs, chinese |
| [印记](https://yinji.org/) | 主要写生活、随笔。 | Personal Blogs | [RSS](https://yinji.org/feed) | all, blogs, chinese |
| [双绞麻痹](https://numb.tech/atom.xml) | 主要写随笔。 | Personal Blogs | [RSS](https://numb.tech/atom.xml) | all, blogs, chinese |
| [叶寻的博客](https://cyrusyip.org/zh-cn/) | 主要写生活、学习。 | Personal Blogs | [RSS](https://cyrusyip.org/zh-cn/index.xml) | all, blogs, chinese |
| [叶泯希](https://blog.418121.xyz/) | 主要写生活、摄影、教程。 | Personal Blogs | [RSS](https://blog.418121.xyz/rss2.xml) | all, blogs, chinese |
| [同和故事匯](https://hocassian.cn/) | 主要写編程、隨筆、Galgame、雜談。 | Personal Blogs | [RSS](https://hocassian.cn/feed/) | all, blogs, chinese |
| [四喜丸子](https://fourhappylions.com/) | 主要写养娃、家庭、海外生活。 | Personal Blogs | [RSS](https://fourhappylions.com/index.xml) | all, blogs, chinese |
| [如鱼饮水](https://wangjiezhe.com/atom.xml) | 主要写数学、随笔。 | Personal Blogs | [RSS](https://wangjiezhe.com/atom.xml) | all, blogs, chinese |
| [小陶持续精进](https://whyya.xyz/) | 主要写生活、生产力工具、效率、知识管理。 | Personal Blogs | [RSS](https://whyya.xyz/rss.xml) | all, blogs, chinese |
| [局域自由博客](https://localfreedom.pages.dev/) | 主要写软件、隐私、笔记、本地化。 | Personal Blogs | [RSS](https://localfreedom.pages.dev/index.xml) | all, blogs, chinese |
| [廊桥遗梦](https://blog.moran.im/) | 主要写随笔、生活、教程。 | Personal Blogs | [RSS](https://blog.moran.im/rss.xml) | all, blogs, chinese |
| [懋和道人](https://blog.dao.js.cn) | 主要写李至臣、李懋和、南通道士、风水。 | Personal Blogs | [RSS](https://blog.dao.js.cn/atom.xml) | all, blogs, chinese |
| [明天的乌云](https://blog.xlab.app/atom.xml) | 主要写安全、思考。 | Personal Blogs | [RSS](https://blog.xlab.app/atom.xml) | all, blogs, chinese |
| [木鸟杂记](https://www.qtmuniao.com) | 主要写分布式系统、存储、boltdb、源码阅读。 | Personal Blogs | [RSS](https://www.qtmuniao.com/atom.xml) | all, blogs, chinese |
| [林林杂语](https://www.xiaozonglin.cn/) | 主要写生活、随笔。 | Personal Blogs | [RSS](https://www.xiaozonglin.cn/feed/) | all, blogs, chinese |
| [柴郡猫](https://www.cheshirex.com) | 主要写生活、分享、记录。 | Personal Blogs | [RSS](https://www.cheshirex.com/feed) | all, blogs, chinese |
| [梅之夏](https://blog.mcenahle.page/) | 主要写随笔、记录、成长、学习。 | Personal Blogs | [RSS](https://blog.mcenahle.page/feed.xml) | all, blogs, chinese |
| [涵哲子居](https://iluc.cn/) | 主要写日常、随笔、乱七八糟。 | Personal Blogs | [RSS](https://iluc.cn/rss.xml) | all, blogs, chinese |
| [爱范儿](https://www.ifanr.com?utm_source=rss&utm_medium=rss&utm_campaign=) | Personal Blogs 订阅源 | Personal Blogs | [RSS](https://www.ifanr.com/feed) | all, chinese, news |
| [玉明-风起于青萍之末](https://xdym11235.com/) | 主要写信息安全。 | Personal Blogs | [RSS](https://xdym11235.com/feed) | all, blogs, chinese |
| [祝融说。](https://zhurongshuo.com/) | 主要写法不净空，觉无性也。。 | Personal Blogs | [RSS](https://zhurongshuo.com/index.xml) | all, blogs, chinese |
| [纸短情长](https://www.gtdstudy.com/) | 主要写阅读、思考。 | Personal Blogs | [RSS](http://yibie.github.io/index.xml) | all, blogs, chinese |
| [讀角獸](https://ducorn.com) | 主要写投資、健康、判斷。 | Personal Blogs | [RSS](https://ducorn.com/feed.xml) | all, blogs, chinese |
| [資工小廢物 - JN](https://blog.giveanornot.com/) | 主要写來自台灣、生活反思、社群媒體負面影響、開源軟體。 | Personal Blogs | [RSS](https://blog.giveanornot.com/index.xml) | all, blogs, chinese |
| [闲人LIFE](https://www.xianrenlife.com/) | 主要写随笔、小说、书评。 | Personal Blogs | [RSS](https://www.xianrenlife.com/feeds/posts/default) | all, blogs, chinese |
| [陈杨树下](https://demochen.com/) | 主要写阅读与思考、效率与工具、生活与成长。 | Personal Blogs | [RSS](https://www.demochen.com/atom.xml) | all, blogs, chinese |

</details>

<details>
<summary>Communities · 1</summary>

| Source | Description | Primary category | Feed | Bundles |
| --- | --- | --- | --- | --- |
| [V2EX](https://www.v2ex.com/) | Communities 订阅源 | Communities | [RSS](https://v2ex.com/index.xml) | all, chinese, news |

</details>

<details>
<summary>Culture & Ideas · 8</summary>

| Source | Description | Primary category | Feed | Bundles |
| --- | --- | --- | --- | --- |
| [KAIX.IN](https://kaix.in/) | 主要写读书、咖啡、随笔。 | Culture & Ideas | [RSS](https://kaix.in/feed/) | all, blogs, chinese |
| [Maohang Gao's Blog](http://kangaroogao.com/atom.xml) | 主要写游记、读书笔记、随笔。 | Culture & Ideas | [RSS](https://kangaroogao.com/atom.xml) | all, blogs, chinese |
| [ShineKid](https://shinekid.com) | 主要写生活、影视、文学。 | Culture & Ideas | [RSS](https://shinekid.com/feed/) | all, blogs, chinese |
| [Tripper Press - Take Photo, Think Seriously.](https://tripper.press) | 主要写摄影、文化产业、新媒体。 | Culture & Ideas | [RSS](https://tripper.press/atom.xml) | all, blogs, chinese |
| [东评西就](https://dongjunke.cn/) | 主要写社交媒体、科技互联网、思考、读书。 | Culture & Ideas | [RSS](https://dongjunke.cn/atom.xml) | all, blogs, chinese |
| [叉息的空中咖啡馆](https://www.xchere.xyz/atom.xml) | 主要写生活、随笔、记录、读书笔记。 | Culture & Ideas | [RSS](https://www.xchere.xyz/atom.xml) | all, blogs, chinese |
| [赫赫文王](https://kqh.me/) | 主要写历史、人文、艺术、日常。 | Culture & Ideas | [RSS](https://kqh.me/index.xml) | all, blogs, chinese |
| [静风说](https://www.jfsay.com) | 主要写生活、读书、电影、旅游。 | Culture & Ideas | [RSS](http://www.jfsay.com/feed) | all, blogs, chinese |

</details>

<details>
<summary>Videos · 93</summary>

| Source | Description | Primary category | Feed | Bundles |
| --- | --- | --- | --- | --- |
| [3Blue1Brown](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCYO_jab_esuFRV4b17AJtAw) | all, videos |
| [a16z](https://www.youtube.com/channel/UC9cn0TuPq4dnbTY-CBsm8XA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC9cn0TuPq4dnbTY-CBsm8XA) | all, videos |
| [Acquired](https://www.youtube.com/channel/UCyFqFYfTW2VoIQKylJ04Rtw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCyFqFYfTW2VoIQKylJ04Rtw) | all, videos |
| [AI Engineer](https://www.youtube.com/channel/UCLKPca3kwwd-B59HNr-_lvA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCLKPca3kwwd-B59HNr-_lvA) | ai, all, videos |
| [AI Explained](https://www.youtube.com/channel/UCNJ1Ymd5yFuUPtn21xtRbbw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCNJ1Ymd5yFuUPtn21xtRbbw) | ai, all, videos |
| [AI Master](https://www.youtube.com/channel/UC0yHbz4OxdQFwmVX2BBQqLg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC0yHbz4OxdQFwmVX2BBQqLg) | ai, all, videos |
| [AI Search](https://www.youtube.com/channel/UCIgnGlGkVRhd4qNFcEwLL4A) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCIgnGlGkVRhd4qNFcEwLL4A) | ai, all, videos |
| [AICodeKing](https://www.youtube.com/channel/UC0m81bQuthaQZmFbXEY9QSw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC0m81bQuthaQZmFbXEY9QSw) | ai, all, videos |
| [Alex Kantrowitz](https://www.youtube.com/channel/UCye1YedIypHffYb8k6Gp9wg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCye1YedIypHffYb8k6Gp9wg) | all, videos |
| [Ali Abdaal](https://www.youtube.com/channel/UCoOae5nYA7VqaXzerajD0lg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCoOae5nYA7VqaXzerajD0lg) | all, videos |
| [All-In Podcast](https://www.youtube.com/channel/UCESLZhusAkFfsNsApnjF_Cg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCESLZhusAkFfsNsApnjF_Cg) | all, videos |
| [Andrej Karpathy](https://www.youtube.com/channel/UCXUPKJO5MZQN11PqgIvyuvQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCXUPKJO5MZQN11PqgIvyuvQ) | ai, all, videos |
| [Andrew Huberman](https://www.youtube.com/channel/UC2D2CMWXMOVWx7giW1n3LIg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC2D2CMWXMOVWx7giW1n3LIg) | all, videos |
| [Android Developers](https://www.youtube.com/channel/UCVHFbqXqoYvEWM1Ddxl0QDg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?user=androiddevelopers) | all, videos |
| [AssemblyAI](https://www.youtube.com/channel/UCtatfZMf-8EkIwASXM4ts0A) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCtatfZMf-8EkIwASXM4ts0A) | ai, all, videos |
| [BBC Earth](https://www.youtube.com/channel/UCwmZiChSryoWQCZMIQezgTg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCwmZiChSryoWQCZMIQezgTg) | all, videos |
| [Beyond Coding](https://www.youtube.com/channel/UCdMz6KKEDW_1Qqas-ya7S6w) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCdMz6KKEDW_1Qqas-ya7S6w) | all, videos |
| [Bloomberg Originals](https://www.youtube.com/channel/UCUMZ7gohGI9HcU9VNsr2FJQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?user=Bloomberg) | all, videos |
| [Branch Education](https://www.youtube.com/channel/UCdp4_l1vPmpN-gDbUwhaRUQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCdp4_l1vPmpN-gDbUwhaRUQ) | all, videos |
| [Business Insider](https://www.youtube.com/channel/UCcyq283he07B7_KUX07mmtA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?user=businessinsider) | all, videos |
| [ByteByteGo](https://www.youtube.com/channel/UCZgt6AzoyjslHTC9dz0UoTw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCZgt6AzoyjslHTC9dz0UoTw) | all, videos |
| [CNET](https://www.youtube.com/channel/UCOmcA3f_RrH6b9NmcNa4tdg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?user=CNETTV) | all, videos |
| [Computerphile](https://www.youtube.com/channel/UC9-y-6csu5WGm29I7JiwpnA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC9-y-6csu5WGm29I7JiwpnA) | all, videos |
| [Curious Refuge](https://www.youtube.com/channel/UClnFtyUEaxQOCd1s5NKYGFA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UClnFtyUEaxQOCd1s5NKYGFA) | all, videos |
| [DeepLearningAI — Video](https://www.youtube.com/channel/UCcIXc5mJsHVYTZR1maL5l9w) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCcIXc5mJsHVYTZR1maL5l9w) | ai, all, videos |
| [Dwarkesh Patel](https://www.youtube.com/channel/UCXl4i9dYBrFOabk0xGmbkRA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCXl4i9dYBrFOabk0xGmbkRA) | all, videos |
| [Elizabeth Alli - DesignerUp](https://www.youtube.com/channel/UCw2R8kz3aotYtV9utqf0uaw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCw2R8kz3aotYtV9utqf0uaw) | all, videos |
| [EO](https://www.youtube.com/channel/UClWTCPVi-AU9TeCN6FkGARg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UClWTCPVi-AU9TeCN6FkGARg) | all, videos |
| [Fireship](https://www.youtube.com/channel/UCsBjURrPoezykLs9EqgamOA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCsBjURrPoezykLs9EqgamOA) | all, videos |
| [freeCodeCamp.org](https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC8butISFwT-Wl7EV0hUK0BQ) | all, videos |
| [Google](https://www.youtube.com/channel/UCK8sQmJBp8GCxrOtXWBpyEA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCK8sQmJBp8GCxrOtXWBpyEA) | all, videos |
| [Google DeepMind](https://www.youtube.com/channel/UCP7jMXSY2xbc3KCAE0MHQ-A) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCP7jMXSY2xbc3KCAE0MHQ-A) | ai, all, videos |
| [Greg Isenberg](https://www.youtube.com/channel/UCPjNBjflYl0-HQtUvOx0Ibw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCPjNBjflYl0-HQtUvOx0Ibw) | all, videos |
| [How I AI](https://www.youtube.com/channel/UCRYY7IEbkHLH_ScJCu9eWDQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCRYY7IEbkHLH_ScJCu9eWDQ) | ai, all, videos |
| [Hung-yi Lee](https://www.youtube.com/channel/UC2ggjtuuWvxrHHHiaDH1dlQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC2ggjtuuWvxrHHHiaDH1dlQ) | ai, all, videos |
| [Hussein Nasser](https://www.youtube.com/channel/UC_ML5xP23TOWKUcc-oAE_Eg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC_ML5xP23TOWKUcc-oAE_Eg) | all, videos |
| [Invest Like The Best](https://www.youtube.com/channel/UCpQBb0fToph3jrDulwz1iUQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCpQBb0fToph3jrDulwz1iUQ) | all, videos |
| [Justin Sung](https://www.youtube.com/channel/UC2Zs9v2hL2qZZ7vsAENsg4w) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC2Zs9v2hL2qZZ7vsAENsg4w) | all, videos |
| [Kurzgesagt – In a Nutshell](https://www.youtube.com/channel/UCsXVk37bltHxD1rDPwtNM8Q) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCsXVk37bltHxD1rDPwtNM8Q) | all, videos |
| [LangChain](https://www.youtube.com/channel/UCC-lyoTfSrcJzA1ab3APAgw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCC-lyoTfSrcJzA1ab3APAgw) | ai, all, videos |
| [Last Week in AI — Video](https://www.youtube.com/channel/UCKARTq-t5SPMzwtft8FWwnA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCKARTq-t5SPMzwtft8FWwnA) | ai, all, videos |
| [leerob](https://www.youtube.com/channel/UCZMli3czZnd1uoc1ShTouQw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCZMli3czZnd1uoc1ShTouQw) | ai, all, videos |
| [Lenny's Podcast](https://www.youtube.com/channel/UC6t1O76G0jYXOAoYCm153dA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC6t1O76G0jYXOAoYCm153dA) | all, videos |
| [Lex Fridman](https://www.youtube.com/channel/UCSHZKyawb77ixDdsGog4iWA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCSHZKyawb77ixDdsGog4iWA) | all, videos |
| [Liam Ottley](https://www.youtube.com/channel/UCui4jxDaMb53Gdh-AZUTPAg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCui4jxDaMb53Gdh-AZUTPAg) | ai, all, videos |
| [Linus Tech Tips](https://www.youtube.com/channel/UCXuqSBlHAE6Xw-yeJA0Tunw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?user=LinusTechTips) | all, videos |
| [Luma](https://www.youtube.com/channel/UC45T0I4p7A3dI0XvhivafZQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC45T0I4p7A3dI0XvhivafZQ) | all, videos |
| [Machine Learning Street Talk](https://www.youtube.com/channel/UCMLtBahI5DMrt0NPvDSoIRQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCMLtBahI5DMrt0NPvDSoIRQ) | ai, all, videos |
| [MacRumors](https://www.youtube.com/channel/UCaFGDBmGK_jw66u3av2Ysjw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?user=macrumors) | all, videos |
| [Marie Forleo](https://www.youtube.com/channel/UCuoxrRDDgk3UUnxR4tlkJYQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?user=marieforleo) | all, videos |
| [Matt Wolfe](https://www.youtube.com/channel/UChpleBmo18P08aKCIgti38g) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UChpleBmo18P08aKCIgti38g) | ai, all, videos |
| [Matthew Berman](https://www.youtube.com/channel/UCawZsQWqfGSbCI5yjkdVkTA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCawZsQWqfGSbCI5yjkdVkTA) | ai, all, videos |
| [MrBeast](https://www.youtube.com/channel/UCX6OQ3DkcsbYNE6H8uQQuVA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCX6OQ3DkcsbYNE6H8uQQuVA) | all, videos |
| [mrblock 區塊先生](https://www.youtube.com/channel/UCN2hSM8fBcvZBa8OOKc24eg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCN2hSM8fBcvZBa8OOKc24eg) | all, chinese, videos |
| [Nature on PBS](https://www.youtube.com/channel/UCcBp_9YPyma4c3HTadmRJ3Q) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCcBp_9YPyma4c3HTadmRJ3Q) | all, videos |
| [nature video](https://www.youtube.com/channel/UC7c8mE90qCtu11z47U0KErg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC7c8mE90qCtu11z47U0KErg) | all, videos |
| [Naval](https://www.youtube.com/channel/UCh_dVD10YuSghle8g6yjePg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCh_dVD10YuSghle8g6yjePg) | all, videos |
| [Nick Saraev](https://www.youtube.com/channel/UCbo-KbSjJDG6JWQ_MTZ_rNA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCbo-KbSjJDG6JWQ_MTZ_rNA) | ai, all, videos |
| [Nikhil Kamath](https://www.youtube.com/channel/UCnC8SAZzQiBGYVSKZ_S3y4Q) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCnC8SAZzQiBGYVSKZ_S3y4Q) | all, videos |
| [NNgroup](https://www.youtube.com/channel/UC2oCugzU6W8-h95W7eBTUEg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC2oCugzU6W8-h95W7eBTUEg) | all, videos |
| [No Priors: AI, Machine Learning, Tech, & Startups](https://www.youtube.com/channel/UCSI7h9hydQ40K5MJHnCrQvw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCSI7h9hydQ40K5MJHnCrQvw) | ai, all, videos |
| [OpenAI](https://www.youtube.com/channel/UCXZCJLdBC09xxGZ6gcdrc6A) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCXZCJLdBC09xxGZ6gcdrc6A) | ai, all, videos |
| [Patrick Boyle](https://www.youtube.com/channel/UCASM0cgfkJxQ1ICmRilfHLw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCASM0cgfkJxQ1ICmRilfHLw) | all, videos |
| [Pika Labs](https://www.youtube.com/channel/UC0SclYU4iiQRihtmDnak-gQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC0SclYU4iiQRihtmDnak-gQ) | ai, all, videos |
| [PowerfulJRE](https://www.youtube.com/channel/UCzQUP1qoWDoEbmsQxvdjxgQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCzQUP1qoWDoEbmsQxvdjxgQ) | all, videos |
| [Product School](https://www.youtube.com/channel/UC6hlQ0x6kPbAGjYkoz53cvA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC6hlQ0x6kPbAGjYkoz53cvA) | all, videos |
| [Real Engineering](https://www.youtube.com/channel/UCR1IuLEqb6UEA_zQ81kwXfg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCR1IuLEqb6UEA_zQ81kwXfg) | all, videos |
| [Riley Brown](https://www.youtube.com/channel/UCMcoud_ZW7cfxeIugBflSBw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCMcoud_ZW7cfxeIugBflSBw) | ai, all, videos |
| [Runway](https://www.youtube.com/channel/UCUBqu_z5uP0AZhYtuyFZB3g) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCUBqu_z5uP0AZhYtuyFZB3g) | ai, all, videos |
| [Ryan Peterman](https://www.youtube.com/channel/UCzB7YGrrxDC_POenf86H3_Q) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCzB7YGrrxDC_POenf86H3_Q) | all, videos |
| [Sabin Civil Engineering](https://www.youtube.com/channel/UCqZQJ4600a9wIfMPbYc60OQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCqZQJ4600a9wIfMPbYc60OQ) | all, videos |
| [Sequoia Capital](https://www.youtube.com/channel/UCWrF0oN6unbXrWsTN7RctTw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCWrF0oN6unbXrWsTN7RctTw) | all, videos |
| [Silicon Valley Girl](https://www.youtube.com/channel/UCiq1FIgtEK7LRAOB1JXTPig) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCiq1FIgtEK7LRAOB1JXTPig) | all, videos |
| [SpaceX](https://www.youtube.com/channel/UCtI0Hodo5o5dUb67FeUjDeA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?user=spacexchannel) | all, videos |
| [Spring I/O](https://www.youtube.com/channel/UCLMPXsvSrhNPN3i9h-u8PYg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCLMPXsvSrhNPN3i9h-u8PYg) | all, videos |
| [StatQuest with Josh Starmer](https://www.youtube.com/channel/UCtYLUTtgS3k1Fg4y5tAhLbw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCtYLUTtgS3k1Fg4y5tAhLbw) | all, videos |
| [Tao Prompts](https://www.youtube.com/channel/UCc1qMq2UBJD9cSKbeBwGoZQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCc1qMq2UBJD9cSKbeBwGoZQ) | ai, all, videos |
| [TED](https://www.youtube.com/channel/UCAuUUnT6oDeKwE6v1NGQxug) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCAuUUnT6oDeKwE6v1NGQxug) | all, videos |
| [The AI Advantage](https://www.youtube.com/channel/UCHhYXsLBEVVnbvsq57n1MTQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCHhYXsLBEVVnbvsq57n1MTQ) | ai, all, videos |
| [The Futur](https://www.youtube.com/channel/UC-b3c7kxa5vU-bnmaROgvog) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC-b3c7kxa5vU-bnmaROgvog) | all, videos |
| [The Knowledge Project Podcast](https://www.youtube.com/channel/UCLtTf_uKt0Itd0NG7txrwXA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCLtTf_uKt0Itd0NG7txrwXA) | all, videos |
| [The Pragmatic Engineer](https://www.youtube.com/channel/UCPbwhExawYrn9xxI21TFfyw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCPbwhExawYrn9xxI21TFfyw) | all, videos |
| [The Verge — Video](https://www.youtube.com/channel/UCddiUEpeqJcYeBxX1IVBKvQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?user=TheVerge) | all, videos |
| [Tina Huang](https://www.youtube.com/channel/UC2UXDak6o7rBm23k3Vv5dww) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC2UXDak6o7rBm23k3Vv5dww) | ai, all, videos |
| [Traversy Media](https://www.youtube.com/channel/UC29ju8bIPH5as8OGnQzwJyA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC29ju8bIPH5as8OGnQzwJyA) | all, videos |
| [Web Dev Simplified](https://www.youtube.com/channel/UCFbNIlppjAuEX4znoulh0Cw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCFbNIlppjAuEX4znoulh0Cw) | all, videos |
| [Wes Roth](https://www.youtube.com/channel/UCqcbQf6yw5KzRoDDcZ_wBSw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCqcbQf6yw5KzRoDDcZ_wBSw) | ai, all, videos |
| [Y Combinator](https://www.youtube.com/channel/UCcefcZRL2oaA_uBNeo5UOWg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCcefcZRL2oaA_uBNeo5UOWg) | all, videos |
| [Yannic Kilcher](https://www.youtube.com/channel/UCZHmQk67mSJgfCCTn7xBfew) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCZHmQk67mSJgfCCTn7xBfew) | ai, all, videos |
| [yobi321](https://www.youtube.com/channel/UCB_DbqNN9w30tnyWJSrIwyA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCB_DbqNN9w30tnyWJSrIwyA) | all, videos |
| [一席YiXi](https://www.youtube.com/channel/UCKFB_rVEFEF3l-onQGvGx1A) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCKFB_rVEFEF3l-onQGvGx1A) | all, chinese, videos |
| [一条Yit](https://www.youtube.com/channel/UCulFhrW_YCwkq_BP16C82mA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCulFhrW_YCwkq_BP16C82mA) | all, chinese, videos |
| [李永乐老师](https://www.youtube.com/channel/UCvNxfitQbWkmLuCd44UfrYQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCvNxfitQbWkmLuCd44UfrYQ) | all, chinese, videos |

</details>

<details>
<summary>Podcasts · 73</summary>

| Source | Description | Primary category | Feed | Bundles |
| --- | --- | --- | --- | --- |
| [30 for 30 Podcasts](http://espnradio.espn.com/espnradio/index) | 播客节目 | Podcasts | [RSS](https://feeds.megaphone.fm/ESP5765452710) | all, podcasts |
| [42章经 — Podcast](https://www.xiaoyuzhoufm.com/podcast/648b0b641c48983391a63f98) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/648b0b641c48983391a63f98) | all, chinese, podcasts |
| [AI炼金术 — Podcast](https://www.xiaoyuzhoufm.com/podcast/63e9ef4de99bdef7d39944c8) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/63e9ef4de99bdef7d39944c8) | ai, all, chinese, podcasts |
| [Darknet Diaries](https://darknetdiaries.com/) | 播客节目 | Podcasts | [RSS](https://feeds.megaphone.fm/darknetdiaries) | all, podcasts |
| [Discovery](http://www.bbc.co.uk/programmes/p002w557) | 播客节目 | Podcasts | [RSS](https://podcasts.files.bbci.co.uk/p002w557.rss) | all, podcasts |
| [Fragmented - AI Developer Podcast](https://fragmentedpodcast.com/) | 播客节目 | Podcasts | [RSS](https://feeds.simplecast.com/LpAGSLnY) | ai, all, podcasts |
| [Gastropod](https://gastropod.com/) | 播客节目 | Podcasts | [RSS](https://www.omnycontent.com/d/playlist/aaea4e69-af51-495e-afc9-a9760146922b/2a195077-f014-41d2-8313-ab190186b4c2/277bcd5c-0a05-4c14-8ba6-ab190186b4d5/podcast.rss) | all, podcasts |
| [Hacking Humans](https://thecyberwire.com/podcasts/hacking-humans) | 播客节目 | Podcasts | [RSS](https://feeds.megaphone.fm/hacking-humans) | all, podcasts |
| [Hanselminutes with Scott Hanselman](https://www.hanselminutes.com) | 播客节目 | Podcasts | [RSS](https://feeds.simplecast.com/gvtxUiIf) | all, podcasts |
| [Invest Like the Best with Patrick O'Shaughnessy](https://colossus.com/) | 播客节目 | Podcasts | [RSS](https://investlikethebest.libsyn.com/rss) | all, podcasts |
| [Invisibilia](https://www.npr.org/podcasts/510307/invisibilia) | 播客节目 | Podcasts | [RSS](https://feeds.npr.org/510307/podcast.xml) | all, podcasts |
| [Planet Money](https://www.npr.org/podcasts/510289/planet-money) | 播客节目 | Podcasts | [RSS](https://feeds.npr.org/510289/podcast.xml) | all, podcasts |
| [Reply All](http://gimletmedia.com/shows/reply-all) | 播客节目 | Podcasts | [RSS](https://feeds.megaphone.fm/replyall) | all, podcasts |
| [The Cynical Developer](https://cynical.dev/) | 播客节目 | Podcasts | [RSS](https://cynicaldeveloper.com/feed/podcast) | all, podcasts |
| [The Startup Junkies Podcast](https://www.startupjunkie.org/podcast) | 播客节目 | Podcasts | [RSS](https://startupjunkie.libsyn.com/rss) | all, podcasts |
| [The Vergecast](https://www.theverge.com/the-vergecast) | 播客节目 | Podcasts | [RSS](https://feeds.megaphone.fm/vergecast) | all, podcasts |
| [Throughline](https://www.npr.org/podcasts/510333/throughline) | 播客节目 | Podcasts | [RSS](https://feeds.npr.org/510333/podcast.xml) | all, podcasts |
| [TIANYU2FM — 对谈未知领域](https://www.xiaoyuzhoufm.com/podcast/5f22729f9504bbdb77253e46) | 播客节目 | Podcasts | [RSS](https://rsshub.xiaowuaiblog.com/xiaoyuzhou/podcast/5f22729f9504bbdb77253e46) | all, chinese, podcasts |
| [What's Next｜科技早知道](https://www.xiaoyuzhoufm.com/podcast/5e74b52c418a84a046ecaceb) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e74b52c418a84a046ecaceb) | all, chinese, podcasts |
| [一席](https://www.xiaoyuzhoufm.com/podcast/5e285326418a84a04627343f) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e285326418a84a04627343f) | all, chinese, podcasts |
| [三五环](https://www.xiaoyuzhoufm.com/podcast/5e280fab418a84a0461faa3c) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e280fab418a84a0461faa3c) | all, chinese, podcasts |
| [不合时宜](https://www.xiaoyuzhoufm.com/podcast/5e280fb8418a84a0461fd076) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e280fb8418a84a0461fd076) | all, chinese, podcasts |
| [东亚观察局](https://www.xiaoyuzhoufm.com/podcast/5e9a4e25418a84a046bc6156) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e9a4e25418a84a046bc6156) | all, chinese, podcasts |
| [东腔西调](https://www.xiaoyuzhoufm.com/podcast/5f72b66083c34e85dd14fde9) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5f72b66083c34e85dd14fde9) | all, chinese, podcasts |
| [乱翻书](https://www.xiaoyuzhoufm.com/podcast/61358d971c5d56efe5bcb5d2) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/61358d971c5d56efe5bcb5d2) | all, chinese, podcasts |
| [人民公园说AI](https://www.xiaoyuzhoufm.com/podcast/65257ff6e8ce9deaf70a65e9) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/65257ff6e8ce9deaf70a65e9) | ai, all, chinese, podcasts |
| [保持偏见](https://www.xiaoyuzhoufm.com/podcast/663e3c95af1e22bb157dcee3) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/663e3c95af1e22bb157dcee3) | all, chinese, podcasts |
| [信号与噪声](https://www.xiaoyuzhoufm.com/podcast/6819d5a7e37664602a344e0e) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/6819d5a7e37664602a344e0e) | ai, all, chinese, podcasts |
| [凹凸电波](https://www.xiaoyuzhoufm.com/podcast/5e2839ca418a84a0462431b7) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e2839ca418a84a0462431b7) | all, chinese, podcasts |
| [十字路口Crossing — Podcast](https://www.xiaoyuzhoufm.com/podcast/60502e253c92d4f62c2a9577) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/60502e253c92d4f62c2a9577) | ai, all, chinese, podcasts |
| [半拿铁 \| 商业沉浮录](https://www.xiaoyuzhoufm.com/podcast/62382c1103bea1ebfffa1c00) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/62382c1103bea1ebfffa1c00) | all, chinese, podcasts |
| [卫诗婕｜漫谈Light the Star](https://www.xiaoyuzhoufm.com/podcast/6627fda4b56459544087d86a) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/6627fda4b56459544087d86a) | all, chinese, podcasts |
| [商业就是这样](https://www.xiaoyuzhoufm.com/podcast/6022a180ef5fdaddc30bb101) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/6022a180ef5fdaddc30bb101) | all, chinese, podcasts |
| [声东击西](https://www.xiaoyuzhoufm.com/podcast/5e2831ed418a84a046231c00) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e2831ed418a84a046231c00) | all, chinese, podcasts |
| [声动早咖啡](https://www.xiaoyuzhoufm.com/podcast/60de7c003dd577b40d5a40f3) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/60de7c003dd577b40d5a40f3) | all, chinese, podcasts |
| [天真不天真](https://www.xiaoyuzhoufm.com/podcast/65cef9e3cace72dff8d98de3) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/65cef9e3cace72dff8d98de3) | all, chinese, podcasts |
| [屠龙之术](https://www.xiaoyuzhoufm.com/podcast/6507bc165c88d2412626b401) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/6507bc165c88d2412626b401) | all, chinese, podcasts |
| [岩中花述](https://www.xiaoyuzhoufm.com/podcast/625635587bfca4e73e990703) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/625635587bfca4e73e990703) | all, chinese, podcasts |
| [开始连接 LinkStart](https://www.xiaoyuzhoufm.com/podcast/63ff0da51b1faf8a0b70b337) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/63ff0da51b1faf8a0b70b337) | all, chinese, podcasts |
| [张小珺Jùn｜商业访谈录](https://www.xiaoyuzhoufm.com/podcast/626b46ea9cbbf0451cf5a962) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/626b46ea9cbbf0451cf5a962) | all, chinese, podcasts |
| [忽左忽右](https://www.xiaoyuzhoufm.com/podcast/5e4ee557418a84a0466737b7) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e4ee557418a84a0466737b7) | all, chinese, podcasts |
| [慢速生长](https://www.xiaoyuzhoufm.com/podcast/668d00c38fcadceb90158ac1) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/668d00c38fcadceb90158ac1) | all, chinese, podcasts |
| [捕蛇者说](https://www.xiaoyuzhoufm.com/podcast/5e2864f7418a84a04628f2da) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e2864f7418a84a04628f2da) | all, chinese, podcasts |
| [搞钱女孩](https://www.xiaoyuzhoufm.com/podcast/63d945ece725b5378a158d29) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/63d945ece725b5378a158d29) | all, chinese, podcasts |
| [文化有限](https://www.xiaoyuzhoufm.com/podcast/5e4515bd418a84a046e2b11a) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e4515bd418a84a046e2b11a) | all, chinese, podcasts |
| [晚点聊 LateTalk](https://www.xiaoyuzhoufm.com/podcast/61933ace1b4320461e91fd55) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/61933ace1b4320461e91fd55) | all, chinese, podcasts |
| [李诞](https://www.xiaoyuzhoufm.com/podcast/65bb55f6513a776b57dedb32) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/65bb55f6513a776b57dedb32) | all, chinese, podcasts |
| [枫言枫语 — Podcast](https://www.xiaoyuzhoufm.com/podcast/5e2864f5418a84a04628e249) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e2864f5418a84a04628e249) | all, chinese, podcasts |
| [此话当真](https://www.xiaoyuzhoufm.com/podcast/646f194853a5e5ea1408d97c) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/646f194853a5e5ea1408d97c) | all, chinese, podcasts |
| [游荡集](https://www.xiaoyuzhoufm.com/podcast/6163ca67c8c1d14e83366b31) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/6163ca67c8c1d14e83366b31) | all, chinese, podcasts |
| [牛油果烤面包](https://www.xiaoyuzhoufm.com/podcast/5e7c8b2b418a84a046e3ecbc) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e7c8b2b418a84a046e3ecbc) | all, chinese, podcasts |
| [独树不成林](https://www.xiaoyuzhoufm.com/podcast/64acd33c7a3d479103fbd32d) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/64acd33c7a3d479103fbd32d) | all, chinese, podcasts |
| [疯投圈](https://www.xiaoyuzhoufm.com/podcast/5e280faf418a84a0461fbd39) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e280faf418a84a0461fbd39) | all, chinese, podcasts |
| [皮蛋漫游记](https://www.xiaoyuzhoufm.com/podcast/6281264ad22bcf3950c80b56) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/6281264ad22bcf3950c80b56) | all, chinese, podcasts |
| [看理想圆桌](https://www.xiaoyuzhoufm.com/podcast/5e4ff4c7418a84a046977618) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e4ff4c7418a84a046977618) | all, chinese, podcasts |
| [知行小酒馆](https://www.xiaoyuzhoufm.com/podcast/6013f9f58e2f7ee375cf4216) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/6013f9f58e2f7ee375cf4216) | all, chinese, podcasts |
| [硅谷101 — Podcast](https://www.xiaoyuzhoufm.com/podcast/5e5c52c9418a84a04625e6cc) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e5c52c9418a84a04625e6cc) | all, chinese, podcasts |
| [硬地骇客](https://www.xiaoyuzhoufm.com/podcast/640ee2438be5d40013fe4a87) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/640ee2438be5d40013fe4a87) | all, chinese, podcasts |
| [科技乱炖](https://www.xiaoyuzhoufm.com/podcast/5e4243cd418a84a0469573fb) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e4243cd418a84a0469573fb) | all, chinese, podcasts |
| [第一财经](https://www.xiaoyuzhoufm.com/podcast/64c75555e8176c3ff81de98c) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/64c75555e8176c3ff81de98c) | all, chinese, podcasts |
| [纵横四海](https://www.xiaoyuzhoufm.com/podcast/62694abdb221dd5908417d1e) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/62694abdb221dd5908417d1e) | all, chinese, podcasts |
| [罗永浩的十字路口](https://www.xiaoyuzhoufm.com/podcast/68981df29e7bcd326eb91d88) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/68981df29e7bcd326eb91d88) | all, chinese, podcasts |
| [肥话连篇](https://www.xiaoyuzhoufm.com/podcast/61d50d72ee197a3aac3dac42) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/61d50d72ee197a3aac3dac42) | all, chinese, podcasts |
| [自习室 STUDY ROOM](https://www.xiaoyuzhoufm.com/podcast/65a5fb7540d4ef949c0140ac) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/65a5fb7540d4ef949c0140ac) | all, chinese, podcasts |
| [自我进化论](https://www.xiaoyuzhoufm.com/podcast/5e5de5cb418a84a0467beb90) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e5de5cb418a84a0467beb90) | all, chinese, podcasts |
| [蒋方舟·一寸](https://www.xiaoyuzhoufm.com/podcast/67c7eeb07ac3e30992e75a2f) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/67c7eeb07ac3e30992e75a2f) | all, chinese, podcasts |
| [诗梳风](https://www.xiaoyuzhoufm.com/podcast/696496f4db4738160d5fabde) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/696496f4db4738160d5fabde) | all, chinese, podcasts |
| [谭立人](https://www.xiaoyuzhoufm.com/podcast/65a2d0f07242f9fc1c1df60a) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/65a2d0f07242f9fc1c1df60a) | all, chinese, podcasts |
| [起朱楼宴宾客](https://www.xiaoyuzhoufm.com/podcast/61dd99a47b29652ff572257b) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/61dd99a47b29652ff572257b) | all, chinese, podcasts |
| [跨国串门儿计划](https://www.xiaoyuzhoufm.com/podcast/670f3da40d2f24f28978736f) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/670f3da40d2f24f28978736f) | ai, all, chinese, podcasts |
| [随机波动StochasticVolatility](https://www.xiaoyuzhoufm.com/podcast/5e7cc741418a84a046b0c2bd) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e7cc741418a84a046b0c2bd) | all, chinese, podcasts |
| [面基](https://www.xiaoyuzhoufm.com/podcast/6388760f22567e8ea6ad070f) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/6388760f22567e8ea6ad070f) | all, chinese, podcasts |
| [高能量](https://www.xiaoyuzhoufm.com/podcast/62c6ae08c4eaa82b112b9c84) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/62c6ae08c4eaa82b112b9c84) | all, chinese, podcasts |

</details>

<!-- SOURCE_APPENDIX_END -->
