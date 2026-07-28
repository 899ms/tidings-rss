<div align="center">
  <img src="https://tidings.info/apple-touch-icon.png" width="96" height="96" alt="Tidings app icon">
  <h1>Tidings RSS</h1>
  <p><strong>627 hand-picked feeds for people who still love the open web.</strong></p>
  <p>AI · News · Research · Blogs · Engineering · Video · Podcasts · Chinese</p>
  <p>
    <a href="README.zh-CN.md">简体中文</a> ·
    <a href="#download-the-collections">Download</a> ·
    <a href="#what-is-inside">Explore</a> ·
    <a href="CONTRIBUTING.md">Contribute</a> ·
    <a href="https://tidings.info/">Get Tidings</a>
  </p>
  <p>
    <a href="https://github.com/fuxiaoai/tidings-rss/actions/workflows/validate.yml"><img alt="Catalog validation" src="https://github.com/fuxiaoai/tidings-rss/actions/workflows/validate.yml/badge.svg"></a>
    <a href="https://github.com/fuxiaoai/tidings-rss/releases/latest"><img alt="Latest release" src="https://img.shields.io/github/v/release/fuxiaoai/tidings-rss?style=flat-square"></a>
    <a href="LICENSE"><img alt="CC0-1.0" src="https://img.shields.io/badge/license-CC0--1.0-blue?style=flat-square"></a>
  </p>
</div>

This is not a bulk export of feed URLs. I built and openly shared this catalog to make it easy to start with a genuinely useful RSS library—not spend a weekend discovering that half of an old OPML file is dead.

The candidates came from public feed directories, publisher-owned endpoints, community recommendations, and my long-running AI Radar collection. I then opened the live feeds, removed duplicates and stale endpoints, rebuilt the categories from current publisher metadata, and rejected anything that Tidings could not actually parse. The result is a deliberately selected mix of official sources, respected publications, independent writers, researchers, engineering teams, educators, and creators.

Every download is standard OPML, so it works with Tidings, NetNewsWire, Reeder, Feedly, Inoreader, FreshRSS, Miniflux, and other compatible readers. **For the best experience with these collections, I recommend [Tidings](https://tidings.info/): the catalog was validated through its production parser, its importer preserves the included categories, and its AI-native reading workflow was built for exactly this kind of mixed source library.**

## Download the collections

Choose one focused collection or take the complete catalog. Topic collections intentionally overlap; `tidings-all.opml` keeps each normalized feed only once.

| Collection | Feeds | Download | Best for |
| --- | ---: | --- | --- |
| Complete collection | `627` | [Download `tidings-all.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-all.opml) | A broad, ready-made RSS library |
| Artificial intelligence | `74` | [Download `tidings-ai.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-ai.opml) | Labs, researchers, releases, analysis, and AI video |
| Fresh news | `44` | [Download `tidings-news.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-news.opml) | Current world, technology, security, and Chinese news |
| Research & science | `28` | [Download `tidings-research.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-research.opml) | Journals, preprints, labs, space, and science reporting |
| Blogs & essays | `374` | [Download `tidings-blogs.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-blogs.opml) | Independent thinking and long-form writing |
| Engineering & technology | `186` | [Download `tidings-engineering.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-engineering.opml) | Company engineering, languages, architecture, and releases |
| Video channels | `93` | [Download `tidings-videos.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-videos.opml) | AI, programming, science, design, and business video |
| Podcasts | `86` | [Download `tidings-podcasts.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-podcasts.opml) | Technology, business, science, culture, and Chinese shows |
| Chinese sources | `239` | [Download `tidings-chinese.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-chinese.opml) | Chinese-language articles, communities, video, and audio |

[Browse every OPML file](opml/) · [Download SHA-256 checksums](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/SHA256SUMS.txt) · [Catalog summary](reports/catalog-summary.md) · [Machine-readable catalog](data/feeds.json)

## What is inside

The names below are examples, not decorative endorsements: every one is present in the linked OPML and passed the same live-feed acceptance process. Famous names were not automatically accepted, and lesser-known independent sources were not automatically excluded.

### Complete collection · 627 feeds

The complete collection combines all of the focused packs: AI labs, major newsrooms, journals, independent blogs, company engineering teams, videos, podcasts, Chinese sources, communities, product writing, and culture. Representative entries include [OpenAI News](https://openai.com/news/), [The GitHub Blog](https://github.blog/), [MIT Technology Review](https://www.technologyreview.com/), [Nature](https://www.nature.com/nature/), [Daring Fireball](https://daringfireball.net/), [Product Hunt](https://www.producthunt.com/), [Hacker News](https://news.ycombinator.com/), [3Blue1Brown](https://www.youtube.com/@3blue1brown), [Planet Money](https://www.npr.org/podcasts/510289/planet-money), [少数派](https://sspai.com/), and [36氪](https://36kr.com/).

### Artificial intelligence · 74 feeds

This collection follows model builders, research labs, open-source ecosystems, release streams, trusted analysts, and Chinese AI coverage.

- **Labs and platforms:** [OpenAI News](https://openai.com/news/), [Anthropic News](https://www.anthropic.com/news), [Google DeepMind](https://deepmind.google/blog/), [Hugging Face](https://huggingface.co/blog), [Apple Machine Learning Research](https://machinelearning.apple.com/), [Google Research](https://research.google/blog/), and [AWS Machine Learning](https://aws.amazon.com/blogs/machine-learning/).
- **Research and releases:** arXiv `cs.AI`, `cs.CL`, `cs.CV`, and `cs.LG`, MIT AI, plus release feeds for Codex, Claude Code, Gemini CLI, LangChain, Model Context Protocol, and OpenClaw.
- **People and analysis:** [Simon Willison](https://simonwillison.net/), [The Batch](https://www.deeplearning.ai/the-batch/), Last Week in AI, 机器之心, 量子位, DeepSeek, 智谱, 通义实验室, and 月之暗面 Kimi.
- **Video and audio:** [Andrej Karpathy](https://www.youtube.com/@AndrejKarpathy), [AI Explained](https://www.youtube.com/@aiexplained-official), [Google DeepMind](https://www.youtube.com/@googledeepmind), DeepLearning.AI, Machine Learning Street Talk, Yannic Kilcher, AI 炼金术, and 人民公园说 AI.

### Fresh news · 44 feeds

The news pack is deliberately compact and applies an additional freshness rule. It balances global desks, investigative reporting, technology, security, and high-signal Chinese publications.

- **World and public-interest news:** [BBC News](https://www.bbc.com/news), [The New York Times World](https://www.nytimes.com/section/world), [The Guardian World](https://www.theguardian.com/world), [Al Jazeera](https://www.aljazeera.com/), [NPR World](https://www.npr.org/sections/world/), [ProPublica](https://www.propublica.org/), and The Washington Post World.
- **Technology and security:** [MIT Technology Review](https://www.technologyreview.com/), [WIRED](https://www.wired.com/), [The Verge](https://www.theverge.com/), [TechCrunch](https://techcrunch.com/), [Ars Technica](https://arstechnica.com/), [Krebs on Security](https://krebsonsecurity.com/), and [Schneier on Security](https://www.schneier.com/).
- **Chinese coverage:** [36氪](https://36kr.com/), [少数派](https://sspai.com/), [虎嗅](https://www.huxiu.com/), [IT之家](https://www.ithome.com/), [Solidot](https://www.solidot.org/), InfoQ 推荐, 爱范儿, and 钛媒体.

### Research & science · 28 feeds

This is a practical research-reading pack rather than an indiscriminate journal dump. It combines primary publication streams, preprints, university and industry labs, space, and accessible science reporting.

- **Journals and preprints:** [Nature](https://www.nature.com/nature/), [Science](https://www.science.org/journal/science), [PLOS ONE](https://journals.plos.org/plosone/), [eLife](https://elifesciences.org/), and arXiv `cs.AI`, `cs.CL`, `cs.CV`, and `cs.LG`.
- **Labs and institutions:** [NASA](https://www.nasa.gov/), [Amazon Science](https://www.amazon.science/), [Apple Machine Learning Research](https://machinelearning.apple.com/), [Google Research](https://research.google/blog/), [MIT AI News](https://news.mit.edu/topic/artificial-intelligence2), and 通义实验室.
- **Science reporting and explanation:** [Quanta Magazine](https://www.quantamagazine.org/), [Scientific American](https://www.scientificamerican.com/), [ScienceDaily](https://www.sciencedaily.com/), [Phys.org](https://phys.org/), BBC Science, New Scientist Space, and Guardian Space.

### Blogs & essays · 374 feeds

The largest focused collection is for writing with a recognizable point of view: experienced engineers, founders, researchers, designers, product thinkers, and independent authors.

- **Software and the web:** [Simon Willison](https://simonwillison.net/), [Martin Fowler](https://martinfowler.com/), [Coding Horror](https://blog.codinghorror.com/), [Brendan Gregg](https://www.brendangregg.com/blog/), [Scott Hanselman](https://www.hanselman.com/blog/), [Dan Abramov](https://overreacted.io/), 张鑫旭, and 谢益辉.
- **Products, companies, and strategy:** [Paul Graham's Essays](http://www.paulgraham.com/articles.html), [Stratechery](https://stratechery.com/), [Benedict Evans](https://www.ben-evans.com/), [Daring Fireball](https://daringfireball.net/), [Tim Ferriss](https://tim.blog/), A List Apart, CSS-Tricks, and UX Collective.
- **Chinese independent voices:** 刘润, 云风, 小众软件, 张鑫旭, 谢益辉, 硅谷 101, 极客公园, and 晚点 LatePost.

### Engineering & technology · 186 feeds

This pack follows the people who build and operate real systems: company engineering teams, language communities, architecture practitioners, security experts, and developer-tool releases.

- **Engineering organizations:** [The GitHub Blog](https://github.blog/), [Engineering at Meta](https://engineering.fb.com/), [Cloudflare](https://blog.cloudflare.com/), [Google Developers](https://developers.googleblog.com/), [Netflix TechBlog](https://netflixtechblog.com/), [Spotify Engineering](https://engineering.atspotify.com/), [Airbnb Engineering](https://medium.com/airbnb-engineering), [Slack Engineering](https://slack.engineering/), and [AWS Architecture](https://aws.amazon.com/blogs/architecture/).
- **Languages and frameworks:** [The Go Blog](https://go.dev/blog/), [Rust Blog](https://blog.rust-lang.org/), [React Blog](https://react.dev/blog), Mozilla Hacks, Kotlin, IntelliJ IDEA, Stack Overflow Blog, and Martin Fowler.
- **Chinese engineering teams:** [美团技术团队](https://tech.meituan.com/), 腾讯技术工程, 阿里技术, 字节跳动技术团队, 小众软件, 机器之心, and 量子位.

### Video channels · 93 feeds

YouTube channels are represented as standard Atom feeds, so new videos arrive alongside articles instead of requiring another algorithmic timeline.

- **AI and engineering:** [OpenAI](https://www.youtube.com/@OpenAI), [Google DeepMind](https://www.youtube.com/@googledeepmind), [Andrej Karpathy](https://www.youtube.com/@AndrejKarpathy), [Computerphile](https://www.youtube.com/@Computerphile), [freeCodeCamp.org](https://www.youtube.com/@freecodecamp), [Fireship](https://www.youtube.com/@Fireship), [ByteByteGo](https://www.youtube.com/@ByteByteGo), and StatQuest.
- **Science and ideas:** [3Blue1Brown](https://www.youtube.com/@3blue1brown), [Kurzgesagt](https://www.youtube.com/@kurzgesagt), [TED](https://www.youtube.com/@TED), BBC Earth, Nature Video, Real Engineering, and SpaceX.
- **Products, business, and Chinese creators:** Y Combinator, a16z, Acquired, Lenny's Podcast, The Pragmatic Engineer, 李永乐老师, 一席 YiXi, and mrblock 區塊先生.

### Podcasts · 86 feeds

The podcast pack mixes durable English-language shows with a substantial Chinese selection instead of treating podcasts as an afterthought.

- **Technology and security:** [Darknet Diaries](https://darknetdiaries.com/), [The Vergecast](https://www.theverge.com/the-vergecast), [Accidental Tech Podcast](https://atp.fm/), [Hanselminutes](https://www.hanselminutes.com/), Hacking Humans, Malicious Life, and Fragmented.
- **Business, science, and ideas:** [Planet Money](https://www.npr.org/podcasts/510289/planet-money), [Hidden Brain](https://hiddenbrain.org/), [BBC Discovery](https://www.bbc.co.uk/programmes/p002w557), [EconTalk](https://www.econtalk.org/), Invest Like the Best, Throughline, and 60-Second Science.
- **Chinese shows:** 硅谷 101, 声东击西, 忽左忽右, 罗永浩的十字路口, 半拿铁, 晚点聊 LateTalk, 知行小酒馆, 捕蛇者说, 乱翻书, and 人民公园说 AI.

### Chinese sources · 239 feeds

This is a cross-format Chinese-language library, not merely a translation of the English packs. It includes articles, WeChat publishing, communities, podcasts, and video.

- **AI and engineering:** 机器之心, [量子位](https://www.qbitai.com/), 智谱, 通义实验室, 腾讯混元, 字节跳动技术团队, [美团技术团队](https://tech.meituan.com/), 腾讯技术工程, and 阿里技术.
- **News and independent writing:** [36氪](https://36kr.com/), [少数派](https://sspai.com/), [虎嗅](https://www.huxiu.com/), [阮一峰的网络日志](https://www.ruanyifeng.com/blog/), [V2EX](https://www.v2ex.com/), IT之家, Solidot, 爱范儿, 小众软件, and 晚点 LatePost.
- **Audio and video:** 硅谷 101, 声东击西, 忽左忽右, 半拿铁, 一席, 李永乐老师, 罗永浩的十字路口, and 人民公园说 AI.

## How the catalog is curated

The current catalog was produced from 884 normalized candidates and checked on **2026-07-28**.

1. Gather discovery candidates from public directories, official publisher pages, community lists, and the local AI Radar collection.
2. Normalize URLs and remove exact and canonical duplicates.
3. Fetch every endpoint through the same production parser used by Tidings.
4. Accept RSS, Atom, or JSON Feed only when parsing succeeds and at least one item is returned.
5. Remove dated sources that have been inactive for more than two years.
6. Apply an additional 21-day freshness threshold to the News collection.
7. Rebuild names, websites, categories, language, and collection membership from live feed metadata.
8. Import the News and Research OPML files into a clean Tidings profile and remove persistent failures from every collection.

This is a dated quality check, not a promise that every publisher or bridge will remain online forever. The evidence is public: [validation summary](reports/validation-summary.json), [source and license boundaries](SOURCES.md), [import verification](reports/import-verification.json), and the weekly live-check workflow.

## Use it in any RSS reader

These files contain standard OPML outlines and public RSS, Atom, or JSON Feed endpoints. Import the downloaded file using your reader's OPML import command; the included topic hierarchy is preserved by readers that support nested categories. This repository catalogs endpoints and original metadata—it does not republish article bodies.

## Keep the list alive

Good directories fail when they only accept additions and never revisit old entries. Contributions are intentionally small and reviewable:

- suggest a public RSS, Atom, or JSON Feed;
- explain why it is worth following;
- choose the closest category and collection;
- verify that it currently returns at least one parseable item;
- regenerate the OPML files and run the dependency-free checks.

Start with [CONTRIBUTING.md](CONTRIBUTING.md) or the **Feed suggestion** issue template. Original catalog metadata is dedicated to the public domain under CC0-1.0; publishers retain all rights to their names and feed content.

```bash
python scripts/catalog.py generate
python scripts/catalog.py check
python -m unittest discover -s tests -v
```

[CC0-1.0 license](LICENSE) · [Notices](NOTICE.md) · [Changelog](CHANGELOG.md)

## Recommended reader: Tidings

**Official website: [https://tidings.info](https://tidings.info/)**

All of the OPML files above work in standards-compatible readers. Tidings is the recommended companion because these collections were verified against its real fetching and parsing path—not against a simplified URL checker. It imports the supplied hierarchy directly, handles RSS, Atom, and JSON Feed in one library, and has been deeply adapted for the mixture of articles, images, videos, communities, and long-running archives found here.

### A real import, not a mockup

The screenshot below comes from a clean local Tidings profile after importing the published News and Research files. The application completed **44/44 News** refreshes and **28/28 Research** refreshes with no remaining failed feed. It then opened a live MIT Technology Review story, fetched all **32 content blocks** and the lead image, and rendered **24 substantial paragraphs**. The capture is rejected automatically if a loading message, full-text error, failed article image, or navigation boilerplate remains visible.

[![A real Tidings window showing a fully fetched, image-rich article after importing the News and Research OPML collections](https://cdn.jsdelivr.net/gh/fuxiaoai/tidings-rss@v1.1.0/assets/tidings-import-news-research.png)](assets/tidings-import-news-research.png)

[Open the original screenshot](assets/tidings-import-news-research.png) · [Read the machine-verifiable import record](reports/import-verification.json) · [See the capture script](tools/capture_tidings_import.cjs)

### Why Tidings fits this catalog

- **Core reading stays free:** subscribe to RSS, Atom, and JSON Feed, read and organize articles, search locally, import or export OPML, manage local settings, and export articles to PDF without paying.
- **AI Radar for the whole reading queue:** analyze unread stories in batches, connect related developments, surface themes, and keep links back to the source articles.
- **AI inside the article:** generate summaries, ask questions about the current article, and read the original together with a bilingual translation.
- **Purpose-built source views:** dedicated image and video feeds, YouTube and Bilibili support, and enhanced reply threads for V2EX and Linux.do when the source permits it.
- **Designed for large, mixed libraries:** indexed local storage, bounded concurrent refresh, per-host request limits, and batched persistence keep fetching and navigation responsive.
- **Graceful source handling:** site-specific enhancements can fall back to the standard title, summary, and original link when an upstream page or bridge is unavailable.

| AI Radar | AI summary |
| :---: | :---: |
| [![Tidings AI Radar](https://tidings.info/assets/screenshots/ai-radar-en.webp)](https://tidings.info/assets/screenshots/ai-radar-en.webp) | [![Tidings AI article summary](https://tidings.info/assets/screenshots/ai-summary-en.webp)](https://tidings.info/assets/screenshots/ai-summary-en.webp) |
| Connect developments while preserving source references. | Generate a structured summary without leaving the article. |
| **Ask the article** | **Bilingual reading** |
| [![Ask questions about an article in Tidings](https://tidings.info/assets/screenshots/ask-article-en.webp)](https://tidings.info/assets/screenshots/ask-article-en.webp) | [![Tidings bilingual reading](https://tidings.info/assets/screenshots/bilingual-en.webp)](https://tidings.info/assets/screenshots/bilingual-en.webp) |
| Ask questions grounded in the article you are reading. | Keep the original and translation together. |
| **Video feeds** | **Community discussions** |
| [![Tidings video feeds](https://tidings.info/assets/screenshots/videos-feed-en.webp)](https://tidings.info/assets/screenshots/videos-feed-en.webp) | [![Tidings forum reply view](https://tidings.info/assets/screenshots/forum-en.webp)](https://tidings.info/assets/screenshots/forum-en.webp) |
| Browse video subscriptions in a dedicated visual feed. | Read supported community discussions as structured threads. |

<div align="center">
  <p><strong>Bring the open web back into one calm, searchable, AI-enhanced reading space.</strong></p>
  <p><a href="https://tidings.info/"><strong>Visit tidings.info →</strong></a></p>
</div>

---

If this catalog saves you time, star the repository, share a focused OPML with someone who still loves RSS, and contribute the one feed you would hate to lose.
