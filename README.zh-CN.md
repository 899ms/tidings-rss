<div align="center">
  <img src="https://tidings.info/apple-touch-icon.png" width="96" height="96" alt="Tidings 应用图标">
  <h1>Tidings RSS</h1>
  <p><strong>为仍然热爱开放互联网的人，精选 627 个真正值得订阅的 RSS 源。</strong></p>
  <p>AI · 新闻 · 科研 · 博客 · 工程技术 · 视频 · 播客 · 中文内容</p>
  <p>
    <a href="README.md">English</a> ·
    <a href="#直接下载">直接下载</a> ·
    <a href="#每个合集里有什么">浏览内容</a> ·
    <a href="CONTRIBUTING.zh-CN.md">参与贡献</a> ·
    <a href="https://tidings.info/">获取 Tidings</a>
  </p>
  <p>
    <a href="https://github.com/fuxiaoai/tidings-rss/actions/workflows/validate.yml"><img alt="目录校验" src="https://github.com/fuxiaoai/tidings-rss/actions/workflows/validate.yml/badge.svg"></a>
    <a href="https://github.com/fuxiaoai/tidings-rss/releases/latest"><img alt="最新版本" src="https://img.shields.io/github/v/release/fuxiaoai/tidings-rss?style=flat-square"></a>
    <a href="LICENSE"><img alt="CC0-1.0" src="https://img.shields.io/badge/license-CC0--1.0-blue?style=flat-square"></a>
  </p>
</div>

这不是把一堆 Feed 地址直接导出后就结束的项目。我把这个目录开源出来，是希望大家可以直接得到一套真正有阅读价值的 RSS 资料库，而不是花一整个周末导入旧 OPML，最后才发现其中一半早已失效。

候选源来自公开目录、发布者提供的订阅地址、社区推荐，以及我长期维护的 AI Radar 列表。之后我重新访问在线 Feed，删除重复、过期和无法解析的地址，使用发布者当前的标题与站点信息重新分类，并把无法通过 Tidings 真实解析链路的源全部剔除。最终保留下来的，是一组经过主动筛选的官网动态、知名媒体、独立作者、研究机构、工程团队、教育者、视频创作者和播客节目。

所有下载文件都是标准 OPML，可以导入 Tidings、NetNewsWire、Reeder、Feedly、Inoreader、FreshRSS、Miniflux 等兼容软件。**如果希望获得与这些合集最匹配的体验，我首选推荐 [Tidings](https://tidings.info/)：整个目录使用它的正式解析器完成验证，导入时会保留现有分类，并且它围绕这种多来源阅读方式，对 AI、视频、社区和大型订阅库做了深度增强。**

## 直接下载

可以只选择自己关心的主题，也可以下载完整目录。各主题包之间会有意重叠；`tidings-all.opml` 中每个规范化订阅地址只保留一次。

| 合集 | 数量 | 下载 | 适合人群 |
| --- | ---: | --- | --- |
| 综合全集 | `627` | [下载 `tidings-all.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-all.opml) | 希望一次建立完整 RSS 资料库 |
| AI / 人工智能 | `74` | [下载 `tidings-ai.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-ai.opml) | 模型公司、研究、版本动态、观点和 AI 视频 |
| 最新新闻 | `44` | [下载 `tidings-news.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-news.opml) | 国际、科技、安全和中文新闻 |
| 科研与科学 | `28` | [下载 `tidings-research.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-research.opml) | 期刊、论文预印本、实验室、航天和科学报道 |
| 博客与深度文章 | `374` | [下载 `tidings-blogs.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-blogs.opml) | 独立观点、技术实践和长篇写作 |
| 工程与技术 | `186` | [下载 `tidings-engineering.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-engineering.opml) | 大厂工程、编程语言、架构和项目版本动态 |
| 视频频道 | `93` | [下载 `tidings-videos.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-videos.opml) | AI、编程、科学、设计和商业视频 |
| 播客 | `86` | [下载 `tidings-podcasts.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-podcasts.opml) | 科技、商业、科学、文化和中文播客 |
| 中文订阅源 | `239` | [下载 `tidings-chinese.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-chinese.opml) | 中文文章、社区、视频和音频内容 |

[浏览全部 OPML](opml/) · [下载 SHA-256 校验文件](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/SHA256SUMS.txt) · [目录统计](reports/catalog-summary.md) · [机器可读目录](data/feeds.json)

## 每个合集里有什么

下面列出的名字不是为了装饰 README：每一个都真实存在于对应 OPML，并且通过了相同的在线 Feed 验收。知名度不会让一个失效源自动入选，小众也不会让一个长期输出优质内容的作者被自动淘汰。

### 综合全集 · 627 个源

综合版包含所有主题包：AI 实验室、主流新闻、科研期刊、独立博客、大厂工程团队、视频、播客、中文内容、社区、产品与文化。代表源包括 [OpenAI News](https://openai.com/news/)、[The GitHub Blog](https://github.blog/)、[MIT Technology Review](https://www.technologyreview.com/)、[Nature](https://www.nature.com/nature/)、[Daring Fireball](https://daringfireball.net/)、[Product Hunt](https://www.producthunt.com/)、[Hacker News](https://news.ycombinator.com/)、[3Blue1Brown](https://www.youtube.com/@3blue1brown)、[Planet Money](https://www.npr.org/podcasts/510289/planet-money)、[少数派](https://sspai.com/)和[36氪](https://36kr.com/)。

### AI / 人工智能 · 74 个源

这个合集同时关注模型开发者、研究机构、开源生态、项目版本、可信分析者和中文 AI 资讯，不会只收集发布会新闻。

- **模型公司与平台：** [OpenAI News](https://openai.com/news/)、[Anthropic News](https://www.anthropic.com/news)、[Google DeepMind](https://deepmind.google/blog/)、[Hugging Face](https://huggingface.co/blog)、[Apple Machine Learning Research](https://machinelearning.apple.com/)、[Google Research](https://research.google/blog/)和 [AWS Machine Learning](https://aws.amazon.com/blogs/machine-learning/)。
- **论文与项目版本：** arXiv `cs.AI`、`cs.CL`、`cs.CV`、`cs.LG`，MIT AI，以及 Codex、Claude Code、Gemini CLI、LangChain、Model Context Protocol、OpenClaw 的 Release Feed。
- **作者与行业分析：** [Simon Willison](https://simonwillison.net/)、[The Batch](https://www.deeplearning.ai/the-batch/)、Last Week in AI、机器之心、量子位、DeepSeek、智谱、通义实验室、月之暗面 Kimi。
- **视频与播客：** [Andrej Karpathy](https://www.youtube.com/@AndrejKarpathy)、[AI Explained](https://www.youtube.com/@aiexplained-official)、[Google DeepMind](https://www.youtube.com/@googledeepmind)、DeepLearning.AI、Machine Learning Street Talk、Yannic Kilcher、AI 炼金术、人民公园说 AI。

### 最新新闻 · 44 个源

新闻包刻意保持精简，并额外应用最新内容时效规则。它同时覆盖国际新闻、调查报道、科技、安全和高质量中文媒体。

- **国际与公共议题：** [BBC News](https://www.bbc.com/news)、[纽约时报国际版](https://www.nytimes.com/section/world)、[The Guardian World](https://www.theguardian.com/world)、[Al Jazeera](https://www.aljazeera.com/)、[NPR World](https://www.npr.org/sections/world/)、[ProPublica](https://www.propublica.org/)和 The Washington Post World。
- **科技与安全：** [MIT Technology Review](https://www.technologyreview.com/)、[WIRED](https://www.wired.com/)、[The Verge](https://www.theverge.com/)、[TechCrunch](https://techcrunch.com/)、[Ars Technica](https://arstechnica.com/)、[Krebs on Security](https://krebsonsecurity.com/)和 [Schneier on Security](https://www.schneier.com/)。
- **中文资讯：** [36氪](https://36kr.com/)、[少数派](https://sspai.com/)、[虎嗅](https://www.huxiu.com/)、[IT之家](https://www.ithome.com/)、[Solidot](https://www.solidot.org/)、InfoQ 推荐、爱范儿、钛媒体。

### 科研与科学 · 28 个源

这是一套适合日常阅读的科研包，而不是把所有期刊机械堆在一起。它组合了论文与期刊更新、大学和企业实验室、航天动态，以及能把复杂问题讲清楚的科学媒体。

- **期刊与论文预印本：** [Nature](https://www.nature.com/nature/)、[Science](https://www.science.org/journal/science)、[PLOS ONE](https://journals.plos.org/plosone/)、[eLife](https://elifesciences.org/)，以及 arXiv `cs.AI`、`cs.CL`、`cs.CV`、`cs.LG`。
- **实验室与研究机构：** [NASA](https://www.nasa.gov/)、[Amazon Science](https://www.amazon.science/)、[Apple Machine Learning Research](https://machinelearning.apple.com/)、[Google Research](https://research.google/blog/)、[MIT AI News](https://news.mit.edu/topic/artificial-intelligence2)和通义实验室。
- **科学报道与解释：** [Quanta Magazine](https://www.quantamagazine.org/)、[Scientific American](https://www.scientificamerican.com/)、[ScienceDaily](https://www.sciencedaily.com/)、[Phys.org](https://phys.org/)、BBC Science、New Scientist Space、Guardian Space。

### 博客与深度文章 · 374 个源

这是最大的主题包，重点不是“流量”，而是作者是否拥有清晰、持续、值得长期关注的观点。内容来自资深工程师、创业者、研究者、设计师、产品作者和独立写作者。

- **软件与开放网络：** [Simon Willison](https://simonwillison.net/)、[Martin Fowler](https://martinfowler.com/)、[Coding Horror](https://blog.codinghorror.com/)、[Brendan Gregg](https://www.brendangregg.com/blog/)、[Scott Hanselman](https://www.hanselman.com/blog/)、[Dan Abramov](https://overreacted.io/)、张鑫旭、谢益辉。
- **产品、公司与策略：** [Paul Graham Essays](http://www.paulgraham.com/articles.html)、[Stratechery](https://stratechery.com/)、[Benedict Evans](https://www.ben-evans.com/)、[Daring Fireball](https://daringfireball.net/)、[Tim Ferriss](https://tim.blog/)、A List Apart、CSS-Tricks、UX Collective。
- **中文独立作者：** 刘润、云风、小众软件、张鑫旭、谢益辉、硅谷 101、极客公园、晚点 LatePost。

### 工程与技术 · 186 个源

工程包关注真正构建和维护系统的人：大厂工程团队、编程语言社区、架构实践者、安全专家和开发工具版本动态。

- **公司工程团队：** [The GitHub Blog](https://github.blog/)、[Engineering at Meta](https://engineering.fb.com/)、[Cloudflare](https://blog.cloudflare.com/)、[Google Developers](https://developers.googleblog.com/)、[Netflix TechBlog](https://netflixtechblog.com/)、[Spotify Engineering](https://engineering.atspotify.com/)、[Airbnb Engineering](https://medium.com/airbnb-engineering)、[Slack Engineering](https://slack.engineering/)和 [AWS Architecture](https://aws.amazon.com/blogs/architecture/)。
- **语言与框架：** [The Go Blog](https://go.dev/blog/)、[Rust Blog](https://blog.rust-lang.org/)、[React Blog](https://react.dev/blog)、Mozilla Hacks、Kotlin、IntelliJ IDEA、Stack Overflow Blog、Martin Fowler。
- **中文工程团队：** [美团技术团队](https://tech.meituan.com/)、腾讯技术工程、阿里技术、字节跳动技术团队、小众软件、机器之心、量子位。

### 视频频道 · 93 个源

YouTube 频道会以标准 Atom Feed 的方式进入阅读器。新视频和文章出现在同一套订阅系统里，不需要再依赖另一个推荐算法时间线。

- **AI 与工程：** [OpenAI](https://www.youtube.com/@OpenAI)、[Google DeepMind](https://www.youtube.com/@googledeepmind)、[Andrej Karpathy](https://www.youtube.com/@AndrejKarpathy)、[Computerphile](https://www.youtube.com/@Computerphile)、[freeCodeCamp.org](https://www.youtube.com/@freecodecamp)、[Fireship](https://www.youtube.com/@Fireship)、[ByteByteGo](https://www.youtube.com/@ByteByteGo)、StatQuest。
- **科学与知识：** [3Blue1Brown](https://www.youtube.com/@3blue1brown)、[Kurzgesagt](https://www.youtube.com/@kurzgesagt)、[TED](https://www.youtube.com/@TED)、BBC Earth、Nature Video、Real Engineering、SpaceX。
- **产品、商业和中文创作者：** Y Combinator、a16z、Acquired、Lenny's Podcast、The Pragmatic Engineer、李永乐老师、一席 YiXi、mrblock 區塊先生。

### 播客 · 86 个源

播客不是这个目录的附属品。这个合集把经得住长期订阅的英文节目与数量可观的中文节目放在一起。

- **科技与安全：** [Darknet Diaries](https://darknetdiaries.com/)、[The Vergecast](https://www.theverge.com/the-vergecast)、[Accidental Tech Podcast](https://atp.fm/)、[Hanselminutes](https://www.hanselminutes.com/)、Hacking Humans、Malicious Life、Fragmented。
- **商业、科学与人文：** [Planet Money](https://www.npr.org/podcasts/510289/planet-money)、[Hidden Brain](https://hiddenbrain.org/)、[BBC Discovery](https://www.bbc.co.uk/programmes/p002w557)、[EconTalk](https://www.econtalk.org/)、Invest Like the Best、Throughline、60-Second Science。
- **中文节目：** 硅谷 101、声东击西、忽左忽右、罗永浩的十字路口、半拿铁、晚点聊 LateTalk、知行小酒馆、捕蛇者说、乱翻书、人民公园说 AI。

### 中文订阅源 · 239 个源

这不是英文合集的中文翻译版，而是一套跨格式的中文内容库，包含文章、公众号、社区、播客和视频。

- **AI 与工程：** 机器之心、[量子位](https://www.qbitai.com/)、智谱、通义实验室、腾讯混元、字节跳动技术团队、[美团技术团队](https://tech.meituan.com/)、腾讯技术工程、阿里技术。
- **资讯与独立写作：** [36氪](https://36kr.com/)、[少数派](https://sspai.com/)、[虎嗅](https://www.huxiu.com/)、[阮一峰的网络日志](https://www.ruanyifeng.com/blog/)、[V2EX](https://www.v2ex.com/)、IT之家、Solidot、爱范儿、小众软件、晚点 LatePost。
- **音频与视频：** 硅谷 101、声东击西、忽左忽右、半拿铁、一席、李永乐老师、罗永浩的十字路口、人民公园说 AI。

## 这些源是怎样筛出来的

当前目录从 884 个规范化候选源开始，并于 **2026-07-28** 完成复核。

1. 从公开目录、发布者官网、社区清单和本地 AI Radar 收集候选源；
2. 规范化 URL，删除精确重复和指向同一内容的规范化重复；
3. 使用 Tidings 正式版本的同一套解析链路抓取每一个地址；
4. 只有 RSS、Atom 或 JSON Feed 解析成功且至少返回一篇内容时才会入选；
5. 删除有明确日期且超过两年没有更新的源；
6. 最新新闻包额外要求最近内容不早于 21 天；
7. 使用在线 Feed 的当前标题、站点、语言和内容重新组织分类；
8. 在干净的 Tidings 用户目录中真实导入新闻和科研包，把持续失败的源从所有合集剔除。

这是带日期的质量检查，不是对发布者或第三方桥接服务永久在线的承诺。完整证据均已公开：[验证摘要](reports/validation-summary.json)、[来源与许可边界](SOURCES.md)、[导入验证记录](reports/import-verification.json)以及每周自动执行的在线检查。

## 适配各类 RSS 阅读器

所有文件都使用标准 OPML 结构，内部只包含公开的 RSS、Atom 或 JSON Feed 地址。下载后使用阅读器的“导入 OPML”功能即可；支持嵌套分类的软件会继续保留文件中的主题层级。项目只整理公开端点和原创目录元数据，不转载文章正文。

## 欢迎一起维护

优秀目录往往不是因为找不到好内容而失效，而是因为只进不出、没有人持续复核。本项目鼓励范围清晰、容易审查的小型 Pull Request：

- 推荐公开的 RSS、Atom 或 JSON Feed；
- 说明它为什么值得长期订阅；
- 选择最接近的分类和主题包；
- 确认当前至少返回一篇可解析内容；
- 重新生成 OPML 并执行零依赖检查。

请先阅读[中文贡献指南](CONTRIBUTING.zh-CN.md)，也可以直接使用 **Feed suggestion** Issue 模板。项目原创目录元数据以 CC0-1.0 放弃权利；发布者名称和 Feed 内容的权利仍归各自所有者。

```bash
python scripts/catalog.py generate
python scripts/catalog.py check
python -m unittest discover -s tests -v
```

[CC0-1.0 许可](LICENSE) · [权利声明](NOTICE.md) · [更新记录](CHANGELOG.md)

## 首选阅读器：Tidings

**官方网站：[https://tidings.info](https://tidings.info/)**

上面的 OPML 可以导入任何兼容标准的阅读器，但我首选推荐 Tidings。原因不是它与这个项目同名，而是这些合集确实使用了 Tidings 的正式抓取和解析链路完成验证，而不是只做了一次 URL 存活检查。它会直接导入现有分类，在同一个资料库里处理 RSS、Atom 和 JSON Feed，并且针对这里常见的文章、图片、视频、社区和长期内容归档做了深度适配。

### 真实导入，不是效果图

下面的界面来自一个全新的本地 Tidings 用户目录。应用导入本项目发布的新闻和科研 OPML 后，完成了 **44/44 个新闻源**和 **28/28 个科研源**的刷新，没有剩余失败源。随后它打开一篇实时获取的 MIT Technology Review 文章，完成 **32 个正文块**、头图和 **24 个有效长段落**的全文抓取。只要界面仍有加载提示、全文错误、失败图片或误抓的导航文案，截图脚本就会拒绝出图。

[![Tidings 真实导入新闻与科研 OPML 后展示完整图文正文](https://cdn.jsdelivr.net/gh/fuxiaoai/tidings-rss@v1.1.0/assets/tidings-import-news-research.png)](assets/tidings-import-news-research.png)

[打开仓库中的原始截图](assets/tidings-import-news-research.png) · [查看机器可验证的导入记录](reports/import-verification.json) · [查看截图脚本](tools/capture_tidings_import.cjs)

### 为什么更推荐 Tidings

- **基础阅读完全免费：** RSS、Atom、JSON Feed 订阅、文章阅读与分类、本地搜索、OPML 导入导出、本地设置和 PDF 导出都可以免费使用。
- **面向整个未读队列的 AI Radar：** 批量分析未读文章，把相关进展连接起来，提炼主题，同时保留返回每篇原文的引用。
- **直接进入文章的 AI 能力：** 生成文章摘要、围绕当前文章提问，并把原文和双语翻译放在同一阅读上下文中。
- **针对不同来源的专属视图：** 图片流、视频流、YouTube、Bilibili，以及在来源允许时展示 V2EX、Linux.do 的结构化回帖。
- **为大型混合订阅库优化：** 使用带索引的本地存储、受控并行刷新、同域名并发限制和批量持久化，让抓取与浏览保持响应。
- **安全降级而不是整篇消失：** 当上游页面或桥接服务暂时不可用时，站点增强能力可以回退到标准标题、摘要和原文链接。

| AI Radar | AI 摘要 |
| :---: | :---: |
| [![Tidings AI Radar](https://tidings.info/assets/screenshots/ai-radar-zh.webp)](https://tidings.info/assets/screenshots/ai-radar-zh.webp) | [![Tidings 文章 AI 摘要](https://tidings.info/assets/screenshots/ai-summary-zh.webp)](https://tidings.info/assets/screenshots/ai-summary-zh.webp) |
| 连接相关进展，同时保留返回原文的引用。 | 不离开文章即可生成结构化摘要。 |
| **围绕文章提问** | **双语阅读** |
| [![在 Tidings 中围绕文章提问](https://tidings.info/assets/screenshots/ask-article-zh.webp)](https://tidings.info/assets/screenshots/ask-article-zh.webp) | [![Tidings 双语阅读](https://tidings.info/assets/screenshots/bilingual-zh.webp)](https://tidings.info/assets/screenshots/bilingual-zh.webp) |
| 围绕正在阅读的文章进行有上下文的问答。 | 原文与译文放在一起，不切断阅读上下文。 |
| **视频订阅** | **社区回帖** |
| [![Tidings 视频订阅](https://tidings.info/assets/screenshots/videos-feed-zh.webp)](https://tidings.info/assets/screenshots/videos-feed-zh.webp) | [![Tidings 论坛回帖视图](https://tidings.info/assets/screenshots/forum-zh.webp)](https://tidings.info/assets/screenshots/forum-zh.webp) |
| 用独立的视觉化信息流浏览视频订阅。 | 把支持的社区讨论展示为结构化回帖。 |

<div align="center">
  <p><strong>把开放互联网重新收进一个安静、可搜索、由 AI 增强的阅读空间。</strong></p>
  <p><a href="https://tidings.info/"><strong>访问 tidings.info →</strong></a></p>
</div>

---

如果这个目录帮你节省了时间，欢迎 Star、把合适的主题 OPML 分享给仍然喜欢 RSS 的朋友，并提交那个你最不希望消失的优质订阅源。
