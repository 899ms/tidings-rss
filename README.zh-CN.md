<div align="center">
  <img src="https://tidings.info/apple-touch-icon.png" width="96" height="96" alt="Tidings 应用图标">
  <h1>Tidings RSS</h1>
  <p><strong>680 个经过在线复核的 RSS 源，其中有 348 个持续更新的中文独立博客。</strong></p>
  <p>
    <a href="README.md">English</a> ·
    <a href="#直接下载">下载 OPML</a> ·
    <a href="#全量源清单">查看完整清单</a> ·
    <a href="CONTRIBUTING.zh-CN.md">参与维护</a> ·
    <a href="https://tidings.info/">获取 Tidings</a>
  </p>
  <p>
    <a href="https://github.com/fuxiaoai/tidings-rss/actions/workflows/validate.yml"><img alt="目录校验" src="https://github.com/fuxiaoai/tidings-rss/actions/workflows/validate.yml/badge.svg"></a>
    <a href="https://github.com/fuxiaoai/tidings-rss/releases/latest"><img alt="最新版本" src="https://img.shields.io/github/v/release/fuxiaoai/tidings-rss?style=flat-square"></a>
    <a href="LICENSE"><img alt="CC0-1.0" src="https://img.shields.io/badge/license-CC0--1.0-blue?style=flat-square"></a>
  </p>
</div>

这里放的是我愿意长期订阅的源，不是抓到多少算多少。每个 Feed 都要经过 Tidings 实际使用的解析器；重复、停更和连续访问失败的地址会被删掉。目录有检查日期，也会继续变化。

这次重点整理了中文独立博客。候选来自 [中文独立博客列表](https://github.com/timqian/chinese-independent-blogs)：先对 1,331 个带 RSS 的博客做两轮解析，再复查高分候选，并按最近更新时间、近几个月的发文分布、Feed 正文信息量和站点类型排序。最近 90 天仍在写的作者优先；超过 180 天没有文章、日期无法确认、三轮中有一次失败、SEO 或推广倾向明显的站点没有收录。最后留下 348 个，没有为了凑到 400 回填弱源。

## 直接下载

主题包会有重叠，综合全集里的 Feed 地址只出现一次。

| 合集 | 数量 | 下载 | 内容 |
| --- | ---: | --- | --- |
| 综合全集 | `680` | [下载 `tidings-all.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-all.opml) | 目录中的全部优质源 |
| 中文独立博客 | `348` | [下载 `tidings-blogs.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-blogs.opml) | 持续更新的中文个人博客 |
| AI / 人工智能 | `95` | [下载 `tidings-ai.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-ai.opml) | 模型、研究、工具和作者 |
| 最新新闻 | `39` | [下载 `tidings-news.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-news.opml) | 国际、科技、安全和中文新闻 |
| 科研与科学 | `27` | [下载 `tidings-research.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-research.opml) | 期刊、预印本、实验室和科学报道 |
| 工程与技术 | `380` | [下载 `tidings-engineering.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-engineering.opml) | 工程团队、编程与技术作者 |
| 视频频道 | `93` | [下载 `tidings-videos.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-videos.opml) | AI、编程、科学和商业视频 |
| 播客 | `73` | [下载 `tidings-podcasts.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-podcasts.opml) | 科技、商业、科学与中文节目 |
| 中文订阅源 | `444` | [下载 `tidings-chinese.opml`](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/tidings-chinese.opml) | 中文文章、社区、视频和音频 |

[浏览 OPML](opml/) · [SHA-256 校验文件](https://github.com/fuxiaoai/tidings-rss/releases/latest/download/SHA256SUMS.txt) · [目录统计](reports/catalog-summary.md) · [机器可读目录](data/feeds.json)

## 中文独立博客怎么选

上游清单适合发现作者，但不提供文章日期、更新频率或在线成功率，所以这里没有照搬它的排序。2026-08-12 的筛选过程是：

1. 对 1,331 个 Feed 分别运行两轮 Tidings 解析，读取最近 20 篇文章的真实日期和正文长度；
2. 只让两轮成功、最近 180 天内有更新、并且至少有两篇可确认日期文章的博客进入候选榜；
3. 结合最近 30、90、180 天的发文情况、第一方 Feed、正文信息量和上游参考顺序评分；
4. 对高分候选运行第三轮解析，删除本轮失败、同站点重复、SEO、推广和资源聚合型站点；
5. 旧目录也重新检查两轮，连续异常的源不再进入全集。

完整筛选记录在 [`reports/chinese-blog-curation.json`](reports/chinese-blog-curation.json)。它记录每个候选通过了几轮、最近更新时间、近期文章数量、正文长度和淘汰原因。你可以直接查某个博客为什么留下，或者为什么被删。

RSS 没有永久在线的保证。一次超时也不足以判死刑，所以这里用多轮结果，计划任务则每周重新检查整个目录。发布者改地址或停止维护后，下一次整理仍可能删除它。

## 导入与维护

文件按 OPML 2.0 生成，保留主分类，可以导入支持 OPML 的阅读器。项目只整理公开 Feed 地址和目录元数据，不转载文章正文。

推荐新源时，请给出发布者网站、Feed 地址和具体推荐理由。中文独立博客还要能证明最近仍在更新。生成与检查命令如下：

```bash
python scripts/catalog.py generate
python scripts/catalog.py check
python -m unittest discover -s tests -v
```

来源、许可和内容权利边界见 [SOURCES.md](SOURCES.md) 与 [NOTICE.md](NOTICE.md)。

## 用 Tidings 阅读这些合集

**官网：[tidings.info](https://tidings.info/)**

这些 OPML 可以交给任何兼容阅读器。我更推荐 Tidings，因为本目录的每个 Feed 都用它实际采用的解析链路检查过；导入后原有分类会保留，RSS、Atom 和 JSON Feed 也能放在同一个资料库中管理。

此前的真实导入测试使用了新闻与科研包：44/44 个新闻源、28/28 个科研源完成刷新，最终失败数为 0；样本文章的正文和图片也完成了抓取。这是 v1.1.0 的测试记录，不冒充本次 2026-08-12 的目录快照。

[![Tidings 导入新闻与科研 OPML 后的真实界面](https://cdn.jsdelivr.net/gh/fuxiaoai/tidings-rss@v1.1.0/assets/tidings-import-news-research.png)](assets/tidings-import-news-research.png)

[查看导入记录](reports/import-verification.json) · [查看截图脚本](tools/capture_tidings_import.cjs)

Tidings 提供分类、搜索和 OPML 导入导出，也能把 AI Radar、文章问答、双语阅读、视频订阅和社区回帖放进同一套阅读流程。功能和价格以官网当前说明为准。

| AI Radar | 双语阅读 |
| :---: | :---: |
| [![Tidings AI Radar](https://tidings.info/assets/screenshots/ai-radar-zh.webp)](https://tidings.info/assets/screenshots/ai-radar-zh.webp) | [![Tidings 双语阅读](https://tidings.info/assets/screenshots/bilingual-zh.webp)](https://tidings.info/assets/screenshots/bilingual-zh.webp) |
| 从未读文章中找出相关进展，并保留原文入口。 | 原文和译文放在同一篇文章里。 |
| **视频订阅** | **社区回帖** |
| [![Tidings 视频订阅](https://tidings.info/assets/screenshots/videos-feed-zh.webp)](https://tidings.info/assets/screenshots/videos-feed-zh.webp) | [![Tidings 社区回帖](https://tidings.info/assets/screenshots/forum-zh.webp)](https://tidings.info/assets/screenshots/forum-zh.webp) |
| 单独浏览视频订阅。 | 阅读支持站点的结构化讨论。 |

下面是本次全集的完整清单。它由 `data/feeds.json` 生成，不靠手工同步。

<!-- SOURCE_APPENDIX_START -->
## 全量源清单

下面列出全集中的 680 个订阅源。每项都标明主分类与所属合集；内容由 `data/feeds.json` 生成。

<details>
<summary>Artificial Intelligence · 38</summary>

| 名称 | 介绍 | 主分类 | Feed | 所属合集 |
| --- | --- | --- | --- | --- |
| [AI](https://blog.google/innovation-and-ai/technology/ai/) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://blog.google/technology/ai/rss/) | AI、全集、工程 |
| [AI Musings by Mu](https://kelvinmu.substack.com) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://kelvinmu.substack.com/feed) | AI、全集、工程 |
| [AI 开发者日报](https://ainews.liduos.com) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://ainews.liduos.com/rss.xml) | AI、全集、中文、工程 |
| [Anthropic News](https://www.anthropic.com/news) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://rsshub.bestblogs.dev/anthropic/news) | AI、全集、工程 |
| [Apple Machine Learning Research](https://machinelearning.apple.com) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://machinelearning.apple.com/rss.xml) | AI、全集、工程、科研 |
| [Artificial Intelligence](https://aws.amazon.com/blogs/machine-learning/) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://aws.amazon.com/blogs/amazon-ai/feed/) | AI、全集、工程 |
| [cs.AI updates on arXiv.org](http://rss.arxiv.org/rss/cs.AI) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://rss.arxiv.org/rss/cs.AI) | AI、全集、工程、科研 |
| [cs.CL updates on arXiv.org](http://rss.arxiv.org/rss/cs.CL) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://export.arxiv.org/rss/cs.CL) | AI、全集、工程、科研 |
| [cs.CV updates on arXiv.org](http://rss.arxiv.org/rss/cs.CV) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://export.arxiv.org/rss/cs.CV) | AI、全集、中文、工程、科研 |
| [cs.LG updates on arXiv.org](http://rss.arxiv.org/rss/cs.LG) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://export.arxiv.org/rss/cs.LG) | AI、全集、中文、工程、科研 |
| [DeepSeek](https://wechat2rss.bestblogs.dev/feed/1709da4f538d4ce4fb6d7a8ba1a5a1c297919601.xml) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://wechat2rss.bestblogs.dev/feed/1709da4f538d4ce4fb6d7a8ba1a5a1c297919601.xml) | AI、全集、工程 |
| [Google DeepMind News](https://deepmind.google/blog/) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://deepmind.com/blog/feed/basic/) | AI、全集、工程 |
| [Hacker News - Newest: "AI"](https://news.ycombinator.com/newest) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://hnrss.org/newest?q=AI) | AI、全集、工程 |
| [Hacker News - Newest: "LLM"](https://news.ycombinator.com/newest) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://hnrss.org/newest?q=LLM) | AI、全集、工程 |
| [Hugging Face - Blog](https://huggingface.co/blog) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://huggingface.co/blog/feed.xml) | AI、全集、工程 |
| [Last Week in AI](https://lastweekin.ai) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://lastweekin.ai/feed) | AI、全集、工程 |
| [MIT News - Artificial intelligence](https://news.mit.edu/rss/topic/artificial-intelligence2) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://news.mit.edu/rss/topic/artificial-intelligence2) | AI、全集、工程、科研 |
| [OpenAI News](https://openai.com/news) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://openai.com/news/rss.xml) | AI、全集、工程 |
| [Recent Commits to openclaw:main](https://github.com/openclaw/openclaw/commits/main) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://github.com/openclaw/openclaw/commits/main.atom) | AI、全集、工程 |
| [Release notes from claude-code](https://github.com/anthropics/claude-code/releases) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://github.com/anthropics/claude-code/releases.atom) | AI、全集、工程 |
| [Release notes from codex](https://github.com/openai/codex/releases) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://github.com/openai/codex/releases.atom) | AI、全集、工程 |
| [Release notes from gemini-cli](https://github.com/google-gemini/gemini-cli/releases) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://github.com/google-gemini/gemini-cli/releases.atom) | AI、全集、工程 |
| [Release notes from langchain](https://github.com/langchain-ai/langchain/releases) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://github.com/langchain-ai/langchain/releases.atom) | AI、全集、工程 |
| [Release notes from modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol/releases) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://github.com/modelcontextprotocol/specification/releases.atom) | AI、全集、工程 |
| [Release notes from openclaw](https://github.com/openclaw/openclaw/releases) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://github.com/openclaw/openclaw/releases.atom) | AI、全集、工程 |
| [Release notes from servers](https://github.com/modelcontextprotocol/servers/releases) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://github.com/modelcontextprotocol/servers/releases.atom) | AI、全集、工程 |
| [Simon Willison's Weblog](http://simonwillison.net/) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://simonwillison.net/atom/everything/) | AI、全集、工程 |
| [The Batch \| DeepLearning.AI \| AI News & Insights](https://www.deeplearning.ai/the-batch/) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://rsshub.bestblogs.dev/deeplearning/the-batch) | AI、全集、工程 |
| [The latest research from Google](https://research.google/blog/) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://research.google/blog/rss/) | AI、全集、工程、科研 |
| [大模型智能](https://wechat2rss.bestblogs.dev/feed/bfc6440c1a2443fab9a6bf607137d41db5cd5c93.xml) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://wechat2rss.bestblogs.dev/feed/bfc6440c1a2443fab9a6bf607137d41db5cd5c93.xml) | AI、全集、中文、工程 |
| [智谱](https://wechat2rss.bestblogs.dev/feed/433d2134dca54d80804daf32e8be546155be3300.xml) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://wechat2rss.bestblogs.dev/feed/433d2134dca54d80804daf32e8be546155be3300.xml) | AI、全集、中文、工程 |
| [月之暗面 Kimi](https://wechat2rss.bestblogs.dev/feed/c5c43d4bc17bae656763859ed0903bb6314ec6fe.xml) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://wechat2rss.bestblogs.dev/feed/c5c43d4bc17bae656763859ed0903bb6314ec6fe.xml) | AI、全集、中文、工程 |
| [机器之心](https://wechat2rss.bestblogs.dev/feed/8d97af31b0de9e48da74558af128a4673d78c9a3.xml) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://wechat2rss.bestblogs.dev/feed/8d97af31b0de9e48da74558af128a4673d78c9a3.xml) | AI、全集、中文、工程 |
| [机器之心SOTA模型](https://wechat2rss.bestblogs.dev/feed/2f520471856d56c7b3a95cd09eb777149b32828a.xml) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://wechat2rss.bestblogs.dev/feed/2f520471856d56c7b3a95cd09eb777149b32828a.xml) | AI、全集、中文、工程 |
| [腾讯混元](https://wechat2rss.bestblogs.dev/feed/306ce19a1ca590c9c2df781789e828d1acfa1356.xml) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://wechat2rss.bestblogs.dev/feed/306ce19a1ca590c9c2df781789e828d1acfa1356.xml) | AI、全集、中文、工程 |
| [通义实验室](https://wechat2rss.bestblogs.dev/feed/4ebee6222ae08705b8aabc9116f0defbcb6b17c6.xml) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://wechat2rss.bestblogs.dev/feed/4ebee6222ae08705b8aabc9116f0defbcb6b17c6.xml) | AI、全集、中文、工程、科研 |
| [量子位](https://www.qbitai.com) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://www.qbitai.com/feed) | AI、全集、中文、工程 |
| [阶跃StepFun](https://wechat2rss.bestblogs.dev/feed/3e2714d06aa36142e8ed6b3f4e5cf9090a069dd2.xml) | Artificial Intelligence 订阅源 | Artificial Intelligence | [RSS](https://wechat2rss.bestblogs.dev/feed/3e2714d06aa36142e8ed6b3f4e5cf9090a069dd2.xml) | AI、全集、中文、工程 |

</details>

<details>
<summary>Engineering & Technology · 340</summary>

| 名称 | 介绍 | 主分类 | Feed | 所属合集 |
| --- | --- | --- | --- | --- |
| [1A23 Studio](https://1a23.com/) | 主要写编程、设计、音乐、开源。 | Engineering & Technology | [RSS](https://1a23.com/feed/) | 全集、中文独立博客、中文、工程 |
| [251 的魔法实验室](https://blog.251.sh/) | 主要写编程、生活、技术、教程。 | Engineering & Technology | [RSS](https://blog.251.sh/feed/) | 全集、中文独立博客、中文、工程 |
| [49th LunaSea](https://maki49.github.io/) | 主要写动漫游戏、生活随笔、科研、编程。 | Engineering & Technology | [RSS](https://maki49.github.io/feed.xml) | 全集、中文独立博客、中文、工程 |
| [51CTO技术栈](https://wechat2rss.bestblogs.dev/feed/d1fabe6c569ffc44979075dde2f57c65e07c3045.xml) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://wechat2rss.bestblogs.dev/feed/d1fabe6c569ffc44979075dde2f57c65e07c3045.xml) | 全集、中文、工程 |
| [9to5Mac](https://9to5mac.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://9to5mac.com/feed) | 全集、工程 |
| [@Lenciel](https://lenciel.com/) | 主要写技术、管理、创业、吹水。 | Engineering & Technology | [RSS](https://lenciel.com/feed.xml) | 全集、中文独立博客、中文、工程 |
| [Abyss的小屋](https://www.rsnocsi.cn/) | 主要写AI、技术、生活、随笔。 | Engineering & Technology | [RSS](https://www.rsnocsi.cn/feed) | AI、全集、中文独立博客、中文、工程 |
| [admin](https://blog.liua.us.ci/rss.xml) | 主要写编程、AI、生活。 | Engineering & Technology | [RSS](https://blog.liua.us.ci/rss.xml) | AI、全集、中文独立博客、中文、工程 |
| [ALBERTAZ](https://albertaz.com) | 主要写前端、技术、绘画、笔记。 | Engineering & Technology | [RSS](https://www.albertaz.com/rss.xml) | 全集、中文独立博客、中文、工程 |
| [Alberto De Bortoli](https://albertodebortoli.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://albertodebortoli.com/rss/) | 全集、工程 |
| [Alliot's blog](https://blog.alliot.tech/) | 主要写编程、技术、运维、硬件。 | Engineering & Technology | [RSS](https://www.iots.vip/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Amiya的书桌](https://blog.sayori.org/) | 主要写日记、资源、技术。 | Engineering & Technology | [RSS](https://blog.sayori.org/rss.xml) | 全集、中文独立博客、中文、工程 |
| [Android Performance](https://androidperformance.com/atom.xml) | 主要写编程、Android、分享。 | Engineering & Technology | [RSS](https://www.androidperformance.com/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Apple Newsroom](https://www.apple.com/newsroom/rss-feed.rss) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.apple.com/newsroom/rss-feed.rss) | 全集、工程 |
| [AppleInsider News](https://appleinsider.com/rss/news) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://appleinsider.com/rss/news/) | 全集、工程 |
| [Archive: 2026 - GitHub Changelog](https://github.blog/changelog/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://github.blog/changelog/feed/) | 全集、工程 |
| [Ars Technica - All content](https://arstechnica.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://feeds.arstechnica.com/arstechnica/index) | 全集、工程、新闻 |
| [Arthur's Review](https://blog.leesaitool.com/) | 主要写AI、社会、哲学、随笔。 | Engineering & Technology | [RSS](https://blog.leesaitool.com/feed.xml) | AI、全集、中文独立博客、中文、工程 |
| [Articles on Smashing Magazine — For Web Designers And Developers](https://www.smashingmagazine.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://rss1.smashingmagazine.com/feed/) | 全集、工程 |
| [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.awsarchitectureblog.com/atom.xml) | 全集、工程 |
| [AWS News Blog](https://aws.amazon.com/blogs/aws/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://aws.amazon.com/blogs/aws/feed/) | 全集、工程 |
| [Bboysoul's Blog](https://www.bboy.app/) | 主要写k8s 运维。 | Engineering & Technology | [RSS](https://www.bboy.app/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Bensz](https://blognas.hwb0307.com/) | 主要写Docker、Linux、生物医学。 | Engineering & Technology | [RSS](https://blognas.hwb0307.com/feed/) | 全集、中文独立博客、中文、工程 |
| [Blog \| Phodal - A Growth Engineer](http://www.phodal.com/blog/) | 主要写编程。 | Engineering & Technology | [RSS](https://www.phodal.com/blog/feeds/rss/) | 全集、中文独立博客、中文、工程 |
| [Blog — Philo Li](https://philoli.com/) | 主要写编程、随笔。 | Engineering & Technology | [RSS](http://lulalap.com/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Canva - Engineering Blog](https://www.canva.dev/blog/engineering/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.canva.dev/blog/engineering/feed.xml) | 全集、工程 |
| [CatCoding](http://catcoding.me/atom.xml) | 主要写编程、技术、写作、阅读。 | Engineering & Technology | [RSS](https://catcoding.me/atom.xml) | 全集、中文独立博客、中文、工程 |
| [CHEGVA](https://chegva.com) | 主要写编程、运维、随笔、国学。 | Engineering & Technology | [RSS](https://chegva.com/feed/) | 全集、中文独立博客、中文、工程 |
| [ChrAlpha's Blog](https://blog.ichr.me/) | 主要写笔记本、技术向、编程、思考。 | Engineering & Technology | [RSS](https://blog.ichr.me/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Clark](https://www.dongyao.ren) | 主要写编程、学习、日常。 | Engineering & Technology | [RSS](https://www.dongyao.ren/feed/) | 全集、中文独立博客、中文、工程 |
| [Cloud Blog](https://cloud.google.com/blog/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://cloudblog.withgoogle.com/rss/) | 全集、工程 |
| [Company \| The JetBrains Blog](https://blog.jetbrains.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://blog.jetbrains.com/blog/feed) | 全集、工程 |
| [Cult of Mac](https://www.cultofmac.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.cultofmac.com/feed) | 全集、工程 |
| [Data4Fun](https://data4fun.cc/) | 主要写个人随笔、大数据、AI。 | Engineering & Technology | [RSS](https://data4fun.cc/index.xml) | AI、全集、中文独立博客、中文、工程 |
| [Databricks](https://www.databricks.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.databricks.com/feed) | 全集、工程 |
| [Dax 的博客](https://daolanx.me/) | 主要写编程、全栈、生活。 | Engineering & Technology | [RSS](https://daolanx.me/zh/rss.xml) | 全集、中文独立博客、中文、工程 |
| [ddadaal.me](https://ddadaal.me) | 主要写编程、消费数码、随笔。 | Engineering & Technology | [RSS](https://ddadaal.me/rss.xml) | 全集、中文独立博客、中文、工程 |
| [Debug客栈](https://blog.debuginn.com/) | 主要写编程、科技、算法、读书。 | Engineering & Technology | [RSS](https://blog.debuginn.com/index.xml) | 全集、中文独立博客、中文、工程 |
| [Deepzz's Blog](https://deepzz.com) | 主要写编程、生活。 | Engineering & Technology | [RSS](https://deepzz.com/feed) | 全集、中文独立博客、中文、工程 |
| [Dennis](https://www.domon.cn/) | 主要写技术、生活、产品。 | Engineering & Technology | [RSS](https://www.domon.cn/rss/) | 全集、中文独立博客、中文、工程 |
| [DGideas' Blog](https://dgideas.net) | 主要写编程、技术、生活。 | Engineering & Technology | [RSS](https://dgideas.net/feed/) | 全集、中文独立博客、中文、工程 |
| [distjr_的博客](https://blog.distjr.top/atom.xml) | 主要写技术、随笔、音乐、二次元。 | Engineering & Technology | [RSS](https://blog.distjr.top/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Dorck's Blog](https://dorck.cn/) | 主要写技术、开源、随笔、自由。 | Engineering & Technology | [RSS](https://dorck.cn/feed.xml) | 全集、中文独立博客、中文、工程 |
| [EdNovas的小站](https://ednovas.xyz/atom.xml) | 主要写编程、算法、Linux、科学上网。 | Engineering & Technology | [RSS](https://ednovas.xyz/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Elastic Blog - Elasticsearch, Kibana, and ELK Stack](https://www.elastic.co) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.elastic.co/blog/feed) | 全集、工程 |
| [Engineering at Meta](https://engineering.fb.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://engineering.fb.com/feed/) | 全集、工程 |
| [Engineering at Slack](https://slack.engineering) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://slack.engineering/feed/) | 全集、工程 |
| [Environment + Energy – The Conversation](https://theconversation.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://theconversation.com/au/environment/articles.atom) | 全集、工程 |
| [Eric's Blog](https://wsdjeg.net/) | 主要写编程、生活、笔记。 | Engineering & Technology | [RSS](https://wsdjeg.net/feed.xml) | 全集、中文独立博客、中文、工程 |
| [Etsy Engineering \| Code as Craft](http://www.etsy.com/codeascraft/rss) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://codeascraft.com/feed/atom/) | 全集、工程 |
| [Feld Thoughts](https://feld.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://feld.com/feed) | 全集、工程 |
| [Fengc's Blog](https://fengcblog.880200.xyz) | 主要写摄影习作、摄影闲扯、相关测试、AI视频。 | Engineering & Technology | [RSS](https://rssweball.top/feed/afaf2a3c-e11a-4783-a358-9e2d20d76a69.xml) | AI、全集、中文独立博客、中文、工程 |
| [for_the_zero的个人博客](https://ftz.is-a.dev) | 主要写编程、前端、软件开发、思考。 | Engineering & Technology | [RSS](https://ftz.is-a.dev/rss.xml) | AI、全集、中文独立博客、中文、工程 |
| [forecho's Blog](https://blog.forecho.com/) | 主要写编程、美股投资、读书、随想。 | Engineering & Technology | [RSS](https://blog.forecho.com/atom.xml) | 全集、中文独立博客、中文、工程 |
| [freeCodeCamp Programming Tutorials: Python, JavaScript, Git & More](https://www.freecodecamp.org/news/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.freecodecamp.org/news/rss/) | 全集、工程 |
| [Frytea](https://frytea.com/) | 主要写编程、思考、高效。 | Engineering & Technology | [RSS](https://www.frytea.com/index.xml) | 全集、中文独立博客、中文、工程 |
| [GamerNoTitle](https://bili33.top) | 主要写编程、学习、技术、杂谈。 | Engineering & Technology | [RSS](https://bili33.top/atom.xml) | 全集、中文独立博客、中文、工程 |
| [GISerlab · 地理空间](https://blog.giserlab.cn) | 主要写GIS、技术、地信、地图。 | Engineering & Technology | [RSS](https://blog.giserlab.cn/feed.xml) | 全集、中文独立博客、中文、工程 |
| [Good Good Good](https://www.goodgoodgood.co) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.goodgoodgood.co/articles/rss.xml) | 全集、工程 |
| [Haku](https://re.karlbaey.top/) | 主要写技术、生活、编程、文学。 | Engineering & Technology | [RSS](https://re.karlbaey.top/rss.xml) | 全集、中文独立博客、中文、工程 |
| [HCLonely Blog](https://blog.hclonely.com/atom.xml) | 主要写前端、二次元、随笔。 | Engineering & Technology | [RSS](https://blog.hclonely.com/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Henry Z's blog](https://changchen.me/) | 主要写技术、Python、SRE、生活。 | Engineering & Technology | [RSS](https://changchen.me/atom.xml) | 全集、中文独立博客、中文、工程 |
| [hsfzxjy 的博客](https://i.hsfzxjy.site/) | 主要写编程、开源、随想、生活。 | Engineering & Technology | [RSS](https://i.hsfzxjy.site/rss.xml) | 全集、中文独立博客、中文、工程 |
| [https://blog.fivest.one/feed](https://blog.fivest.one) | 主要写生活、吐槽、文艺、社会。 | Engineering & Technology | [RSS](http://blog.fivest.one/feed) | 全集、中文独立博客、中文、工程 |
| [I'm OWenT](https://owent.net/) | 主要写编程、后端、技术、思考。 | Engineering & Technology | [RSS](https://owent.net/index.xml) | 全集、中文独立博客、中文、工程 |
| [icodex \| 前端技术博客 \| 专注 React、TypeScript、AI 与性能优化 Blog](https://icodex.me/) | 主要写编程、前端、互联网、技术。 | Engineering & Technology | [RSS](https://icodex.me/atom.xml) | 全集、中文独立博客、中文、工程 |
| [idealclover](https://idealclover.top/) | 主要写编程、随笔、思考、生活。 | Engineering & Technology | [RSS](https://idealclover.top/feed) | 全集、中文独立博客、中文、工程 |
| [ImCBC](https://imcbc.cn/) | 主要写编程、随笔。 | Engineering & Technology | [RSS](https://www.bbing.com.cn/index.xml) | 全集、中文独立博客、中文、工程 |
| [inessential.com](https://inessential.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://inessential.com/xml/rss.xml) | 全集、工程 |
| [Innei](https://innei.in) | 主要写生活、随笔、前端、动漫。 | Engineering & Technology | [RSS](https://innei.ren/feed) | 全集、中文独立博客、中文、工程 |
| [IntelliJ IDEA : IntelliJ IDEA – the Leading IDE for Professional Development in Java and Kotlin \| The JetBrains Blog](https://blog.jetbrains.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://blogs.jetbrains.com/idea/feed/) | 全集、工程 |
| [ISLAND](https://youngxhui.top/) | 主要写编程、生活、随笔。 | Engineering & Technology | [RSS](https://youngxhui.top/index.xml) | 全集、中文独立博客、中文、工程 |
| [iTimothy](https://xiaozhou.net/atom.xml) | 主要写编程。 | Engineering & Technology | [RSS](https://xiaozhou.net/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Jack Pu's Blog (蒲小花的博客－ポーのブログ)](https://www.jackpu.com/) | 主要写前端、生活。 | Engineering & Technology | [RSS](https://www.jackpu.com/rss/) | 全集、中文独立博客、中文、工程 |
| [Jacky Wong](https://jw1.ai/atom.xml) | 主要写前端、生活、技术、音乐。 | Engineering & Technology | [RSS](https://jw1.dev/atom.xml) | 全集、中文独立博客、中文、工程 |
| [jdjwzx233的博客](https://jdjwzx233.cn) | 主要写生活、编程、技术、日常。 | Engineering & Technology | [RSS](https://www.jdjwzx233.cn/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Jimmy Song – Jimmy Song's Blog](https://jimmysong.io/) | 主要写编程。 | Engineering & Technology | [RSS](https://jimmysong.io/index.xml) | 全集、中文独立博客、中文、工程 |
| [Josherich’s Blog](https://josherich.me/) | 主要写编程、随笔。 | Engineering & Technology | [RSS](https://www.josherich.me/feed.xml) | 全集、中文独立博客、中文、工程 |
| [keggin's blog](https://keggin.tech) | 主要写编程、Linux、数模、逆向。 | Engineering & Technology | [RSS](https://keggin.tech/rss.xml) | 全集、中文独立博客、中文、工程 |
| [Kerry的学习笔记](https://kerrynotes.com) | 主要写软件、技术、分享。 | Engineering & Technology | [RSS](https://kerrynotes.com/feed/) | 全集、中文独立博客、中文、工程 |
| [kok的笔记本](https://wocai.de/) | 主要写编程、摄影。 | Engineering & Technology | [RSS](https://wocai.de/index.xml/) | 全集、中文独立博客、中文、工程 |
| [Kotlin : A concise multiplatform language developed by JetBrains \| The JetBrains Blog](https://blog.jetbrains.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://blog.jetbrains.com/kotlin/feed/) | 全集、工程 |
| [Krebs on Security](https://krebsonsecurity.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://krebsonsecurity.com/feed/) | 全集、工程、新闻 |
| [laike9m's blog](https://laike9m.com/blog/rss) | 主要写Python、生活、编程。 | Engineering & Technology | [RSS](https://laike9m.com/blog/rss/) | 全集、中文独立博客、中文、工程 |
| [Latest news](https://www.zdnet.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.zdnet.com/topic/security/rss.xml) | 全集、工程 |
| [LearnData 开源笔记](https://newzone.top/) | 主要写笔记、个人成长、编程。 | Engineering & Technology | [RSS](https://newzone.top/rss.xml) | 全集、中文独立博客、中文、工程 |
| [Lex Blog](https://dreams.plus/) | 主要写生活、随笔、编程、笔记。 | Engineering & Technology | [RSS](https://dreams.plus/rss.xml) | 全集、中文独立博客、中文、工程 |
| [LiaoKe的博客](https://blog.liao-ke.com/) | 主要写编程、开源、全栈、开发者。 | Engineering & Technology | [RSS](https://blog.liao-ke.com/rss.xml) | 全集、中文独立博客、中文、工程 |
| [LiesAuer's Blog](https://www.liesauer.net/blog/) | 主要写编程。 | Engineering & Technology | [RSS](https://www.liesauer.net/blog/feed/) | 全集、中文独立博客、中文、工程 |
| [Lifehacker](https://lifehacker.com/feed/rss) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://lifehacker.com/rss) | 全集、工程 |
| [LiuShen's Blog - 清羽飞扬](https://blog.liushen.fun/) | 主要写技术、生活、随笔、记录。 | Engineering & Technology | [RSS](https://blog.liushen.fun/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Long Luo's Life Notes](https://www.longluo.me/atom.xml) | 主要写数学、物理、算法、编程。 | Engineering & Technology | [RSS](https://www.longluo.me/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Longlong's Blog](https://blog.xlonglong.cn) | 主要写生活日常、随笔、学习笔记、炼丹。 | Engineering & Technology | [RSS](https://blog.xlonglong.cn/feed/) | 全集、中文独立博客、中文、工程 |
| [Louis C Deng's Blog](https://blog.aeilot.top/index.xml) | 主要写随笔、技术、艺术、生活。 | Engineering & Technology | [RSS](https://blog.aeilot.top/index.xml) | 全集、中文独立博客、中文、工程 |
| [lucifer的网络博客](https://lucifer.ren/blog) | 主要写编程、前端、算法。 | Engineering & Technology | [RSS](https://lucifer.ren/blog/atom.xml) | 全集、中文独立博客、中文、工程 |
| [luozhiyun`s Blog](https://www.luozhiyun.com) | 主要写编程、生活。 | Engineering & Technology | [RSS](https://www.luozhiyun.com/feed) | 全集、中文独立博客、中文、工程 |
| [LV88](https://lv88fg.com) | 主要写编程、学习、生活。 | Engineering & Technology | [RSS](https://scvoet.me/feed) | 全集、中文独立博客、中文、工程 |
| [MacTalk-池建强的 Blog](https://macshuo.com) | 主要写编程、iOS。 | Engineering & Technology | [RSS](http://macshuo.com/?feed=rss2) | 全集、中文独立博客、中文、工程 |
| [Martin Fowler](https://martinfowler.com/feed.atom) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://martinfowler.com/feed.atom) | 全集、工程 |
| [Mengke's blog - Mengke's coding journey](https://www.mengke.me/blog) | 主要写技术、生活、笔记。 | Engineering & Technology | [RSS](https://mengke.me/feed.xml) | 全集、中文独立博客、中文、工程 |
| [mephisto.cc](https://mephisto.cc/) | 主要写Linux、Python、Travel、Note。 | Engineering & Technology | [RSS](https://mephisto.cc/index.xml) | 全集、中文独立博客、中文、工程 |
| [Microsoft Azure Blog](https://azure.microsoft.com/en-us/blog/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://azure.microsoft.com/en-us/blog/feed/) | 全集、工程 |
| [Mobility](https://lichuanyang.top/) | 主要写编程、后端、java。 | Engineering & Technology | [RSS](http://lichuanyang.top/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Mokeyjay's Blog - 超能小紫](https://mok.moe) | 主要写编程、开源、PHP、生活。 | Engineering & Technology | [RSS](https://www.mokeyjay.com/feed) | 全集、中文独立博客、中文、工程 |
| [Mosu](https://mosuzi.com/atom.xml) | 主要写随笔、生活、开发。 | Engineering & Technology | [RSS](https://www.mosuzi.com/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Mox的笔记库](https://mocusez.site/zh-CN/) | 主要写编程、数据库、程序编译器、随笔。 | Engineering & Technology | [RSS](https://mocusez.site/zh-CN/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Muyun99 的杂谈](https://muyun.work/) | 主要写科技、生活、算法、随笔。 | Engineering & Technology | [RSS](https://muyun.work/feed/) | 全集、中文独立博客、中文、工程 |
| [My](https://dayzmod.kdns.fr/) | 主要写编程、模组、游戏。 | Engineering & Technology | [RSS](https://dayzmod.kdns.fr/rss.xml) | 全集、中文独立博客、中文、工程 |
| [NBlog](https://blog.nocp.space) | 主要写编程、技术、随笔、音乐。 | Engineering & Technology | [RSS](https://nocp.space/rss/feed.json) | 全集、中文独立博客、中文、工程 |
| [Netflix TechBlog - Medium](https://netflixtechblog.com?source=rss----2615bd06b42e---4) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://netflixtechblog.com/feed) | 全集、工程 |
| [News – CNET](https://www.cnet.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.cnet.com/rss/news/) | 全集、工程 |
| [Nicksxs's Blog](https://nicksxs.me/atom.xml) | 主要写编程、后端、Java、PHP。 | Engineering & Technology | [RSS](https://nicksxs.me/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Niracler 的博物志](https://niracler.com) | 主要写生活、编程、工具、随笔。 | Engineering & Technology | [RSS](https://niracler.com/rss.xml) | 全集、中文独立博客、中文、工程 |
| [Node.js Blog](https://nodejs.org/en) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://nodejs.org/en/feed/blog.xml) | 全集、工程 |
| [NPR Topics: Environment](https://www.npr.org/templates/story/story.php?storyId=1025) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://feeds.npr.org/1025/rss.xml) | 全集、工程 |
| [NYT > Climate and Environment](https://www.nytimes.com/section/climate) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://rss.nytimes.com/services/xml/rss/nyt/Climate.xml) | 全集、工程 |
| [obaby 𝐢‍𝐧⃝ void](https://zhongxiaojie.cn/) | 主要写生活、编程、硬件、人工智能。 | Engineering & Technology | [RSS](https://h4ck.org.cn/feed/) | AI、全集、中文独立博客、中文、工程 |
| [oldj's blog](https://oldj.net) | 主要写编程、写作、以及涂鸦。 | Engineering & Technology | [RSS](https://oldj.net/feed) | 全集、中文独立博客、中文、工程 |
| [OneCoder](https://www.coderli.com/) | 主要写编程、教程、技术、随笔。 | Engineering & Technology | [RSS](https://www.coderli.com/feed.xml) | 全集、中文独立博客、中文、工程 |
| [OneV's Den](https://onevcat.com) | 主要写编程、iOS。 | Engineering & Technology | [RSS](https://onevcat.com/feed.xml) | 全集、中文独立博客、中文、工程 |
| [OnionTalk](https://hateonion.me/) | 主要写编程、前端、随笔。 | Engineering & Technology | [RSS](https://hateonion.me/index.xml) | 全集、中文独立博客、中文、工程 |
| [Oragekk&apos;s Blog](https://oragekk.me/) | 主要写编程、思考、学习笔记、生活杂想。 | Engineering & Technology | [RSS](https://oragekk.me/rss.xml) | 全集、中文独立博客、中文、工程 |
| [Origin](https://blog.singee.me/atom.xml) | 主要写编程、Python、随笔。 | Engineering & Technology | [RSS](https://blog.singee.me/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Panda Home](https://old-panda.com/) | 主要写编程、生活。 | Engineering & Technology | [RSS](https://old-panda.com/feed/) | 全集、中文独立博客、中文、工程 |
| [Peng's Blog](https://pengs.top/atom.xml) | 主要写编程、技术、linux、生活。 | Engineering & Technology | [RSS](https://pengs.top/atom.xml) | 全集、中文独立博客、中文、工程 |
| [piglei](https://www.piglei.com/) | 主要写编程。 | Engineering & Technology | [RSS](https://www.piglei.com/feeds/latest/) | 全集、中文独立博客、中文、工程 |
| [Prakati India](https://prakati.in/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.prakati.in/feed/) | 全集、工程 |
| [ProAndroidDev - Medium](https://proandroiddev.com?source=rss----c72404660798---4) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://proandroiddev.com/feed) | 全集、工程 |
| [pseudoyu](https://www.pseudoyu.com/) | 主要写区块链、编程、工具、随笔。 | Engineering & Technology | [RSS](https://www.pseudoyu.com/zh/index.xml) | 全集、中文独立博客、中文、工程 |
| [Public Object](https://publicobject.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://publicobject.com/rss/) | 全集、工程 |
| [Python Insider](https://blog.python.org/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://blog.python.org/feeds/posts/default) | 全集、工程 |
| [Qaiu blog](https://blog.qaiu.top) | 主要写手机编程、技术、开发、教程。 | Engineering & Technology | [RSS](https://blog.qaiu.top/rss.xml) | 全集、中文独立博客、中文、工程 |
| [QingCCL](https://qingccl.com/) | 主要写文学、读书、随笔、技术。 | Engineering & Technology | [RSS](https://qingccl.github.io/rss.xml) | 全集、中文独立博客、中文、工程 |
| [QP's Blog](https://www.szqp.site) | 主要写生活、旅行、技术。 | Engineering & Technology | [RSS](https://www.szqp.site/feed) | 全集、中文独立博客、中文、工程 |
| [Qunar技术沙龙](https://wechat2rss.bestblogs.dev/feed/84c072f8d34d1690f2783d7dda6013cf6d892b7f.xml) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://wechat2rss.bestblogs.dev/feed/84c072f8d34d1690f2783d7dda6013cf6d892b7f.xml) | 全集、中文、工程 |
| [Random Thoughts](https://blog.joway.io/) | 主要写编程、旅行、随笔。 | Engineering & Technology | [RSS](https://blog.joway.io/index.xml) | 全集、中文独立博客、中文、工程 |
| [Randy's Blog](https://lutaonan.com) | 主要写编程。 | Engineering & Technology | [RSS](https://lutaonan.com/rss.xml) | 全集、中文独立博客、中文、工程 |
| [Raz1ner](https://raz1ner.com) | 主要写Excel函数、Google脚本、技术、随笔。 | Engineering & Technology | [RSS](https://raz1ner.com/atom.xml) | 全集、中文独立博客、中文、工程 |
| [ReadWrite](https://readwrite.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://readwrite.com/feed/) | 全集、工程 |
| [Redis Blog](https://redis.io/en/blog) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://redis.io/feed/) | 全集、工程 |
| [Release notes from biome](https://github.com/biomejs/biome/releases) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://github.com/biomejs/biome/releases.atom) | 全集、工程 |
| [Release notes from bun](https://github.com/oven-sh/bun/releases) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://github.com/oven-sh/bun/releases.atom) | 全集、工程 |
| [Release notes from NetNewsWire](https://github.com/Ranchero-Software/NetNewsWire/releases) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://github.com/Ranchero-Software/NetNewsWire/releases.atom) | 全集、工程 |
| [Release notes from zed](https://github.com/zed-industries/zed/releases) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://github.com/zed-industries/zed/releases.atom) | 全集、工程 |
| [Replicate's blog](https://replicate.com/blog) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://replicate.com/blog/rss) | 全集、工程 |
| [Rokcso's Blog](https://rokcso.com/) | 主要写生活、技术、好奇心、产品管理。 | Engineering & Technology | [RSS](https://rokcso.com/index.xml) | AI、全集、中文独立博客、中文、工程 |
| [ROYWANG](https://roy.wang/feed/index.xml) | 主要写技术、生活、日记。 | Engineering & Technology | [RSS](https://roy.wang/feed/) | 全集、中文独立博客、中文、工程 |
| [Roy的个人站](https://geofftools.cn/blog/) | 主要写编程、Swift、Python。 | Engineering & Technology | [RSS](https://geofftools.cn/blog/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Rust Blog](https://blog.rust-lang.org/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://blog.rust-lang.org/feed.xml) | 全集、工程 |
| [rxliuli blog](https://blog.rxliuli.com/atom.xml) | 主要写前端、编程、随笔。 | Engineering & Technology | [RSS](https://blog.rxliuli.com/atom.xml) | 全集、中文独立博客、中文、工程 |
| [RYANUO](https://ryanuo.cc) | 主要写编程、嵌入式、前端、AI。 | Engineering & Technology | [RSS](https://ryanuo.cc/sitemap.xml) | AI、全集、中文独立博客、中文、工程 |
| [Ryan‘s World](https://blog.12ms.xyz/) | 主要写编程、技术、运维、加密货币。 | Engineering & Technology | [RSS](https://blog.12ms.xyz/feed/) | 全集、中文独立博客、中文、工程 |
| [S T C H E N G](https://cheng.st/atom.xml) | 主要写随笔、旅行、摄影、运动。 | Engineering & Technology | [RSS](https://cheng.st/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Schneier on Security](https://www.schneier.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.schneier.com/blog/index.rdf) | 全集、工程、新闻 |
| [Security Affairs](https://securityaffairs.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://securityaffairs.co/wordpress/feed) | 全集、工程 |
| [Sehnsucht](https://blog.sehnsucht.top/) | 主要写技术、生活、随笔、读书。 | Engineering & Technology | [RSS](https://blog.sehnsucht.top/rss.xml) | 全集、中文独立博客、中文、工程 |
| [Sekyoro的博客小屋](https://www.sekyoro.top/) | 主要写编程、学习笔记、机器学习、工具使用。 | Engineering & Technology | [RSS](https://www.sekyoro.top/atom.xml) | AI、全集、中文独立博客、中文、工程 |
| [Seven's blog](https://blog.diqigan.cn/) | 主要写编程、随笔、Geek、Java。 | Engineering & Technology | [RSS](https://blog.diqigan.cn/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Shanwer's Blog](https://blog.shanwer.top) | 主要写日常、生活、编程、随笔。 | Engineering & Technology | [RSS](https://blog.shanwer.top/feed/) | 全集、中文独立博客、中文、工程 |
| [sjdhome](https://sjdhome.com/) | 主要写编程、生活、学习。 | Engineering & Technology | [RSS](https://sjdhome.com/blog/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Skywind Inside](https://skywind.me/blog) | 主要写编程。 | Engineering & Technology | [RSS](http://www.skywind.me/blog/feed) | 全集、中文独立博客、中文、工程 |
| [SkyWT](https://skywt.cn) | 主要写技术、开发、生活。 | Engineering & Technology | [RSS](https://blog.skywt.cn/feed/) | 全集、中文独立博客、中文、工程 |
| [Slashdot](https://slashdot.org/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://rss.slashdot.org/Slashdot/slashdotMain) | 全集、工程 |
| [smallyu的博客](https://smallyu.net/atom.xml) | 主要写技术、生活、区块链。 | Engineering & Technology | [RSS](https://smallyu.net/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Spotify Engineering](https://engineering.atspotify.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://engineering.atspotify.com/feed/) | 全集、工程 |
| [Stack Overflow Blog](https://stackoverflow.blog/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://blog.stackoverflow.com/feed/) | 全集、工程 |
| [Steve Sun](https://sund.site/) | 主要写数字生活、文化、架构。 | Engineering & Technology | [RSS](https://www.sund.site/index.xml) | 全集、中文独立博客、中文、工程 |
| [Stratechery by Ben Thompson](https://stratechery.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://stratechery.com/feed/) | 全集、工程 |
| [Stray Episode](https://farer.org/) | 主要写编程、技术、游戏、思考。 | Engineering & Technology | [RSS](https://farer.org/rss/) | 全集、中文独立博客、中文、工程 |
| [Stripe Blog](https://stripe.com/blog) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://stripe.com/blog/feed.rss) | 全集、工程 |
| [StudyingLover's Blog](https://www.studyinglover.com/) | 主要写编程、机器学习、计算机视觉、元宇宙。 | Engineering & Technology | [RSS](https://studyinglover.com/atom.xml) | AI、全集、中文独立博客、中文、工程 |
| [SUMSEC](https://sumsec.me) | 主要写技术、安全、生活、Java安全。 | Engineering & Technology | [RSS](https://sumsec.me/resources/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Sunset 的重构博客](https://blog.sunmkt.uk/) | 主要写编程、开源、生活、随笔。 | Engineering & Technology | [RSS](https://blog.sunmkt.uk/feed.xml) | 全集、中文独立博客、中文、工程 |
| [Supabase Blog](https://supabase.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://supabase.com/rss.xml) | 全集、工程 |
| [Super Blog](https://superpung.com/atom.xml) | 主要写编程、生活、技术、观点。 | Engineering & Technology | [RSS](https://superpung.com/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Surmon.me](https://surmon.me) | 主要写前端、编程、思考。 | Engineering & Technology | [RSS](https://surmon.me/rss.xml) | 全集、中文独立博客、中文、工程 |
| [Swift by Sundell](https://www.swiftbysundell.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.swiftbysundell.com/feed.rss) | 全集、工程 |
| [Swift.org](https://www.swift.org/atom.xml) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.swift.org/atom.xml) | 全集、工程 |
| [Taxodium](https://taxodium.ink/) | 主要写编程、随笔。 | Engineering & Technology | [RSS](https://taxodium.ink/rss.xml) | 全集、中文独立博客、中文、工程 |
| [Terrarum::异世界丨居正博客](https://blog.skyju.cc/) | 主要写编程、PHP、渗透、开源。 | Engineering & Technology | [RSS](https://blog.skyju.cc/index.xml) | 全集、中文独立博客、中文、工程 |
| [The Airbnb Tech Blog - Medium](https://medium.com/airbnb-engineering?source=rss----53c7c27702d5---4) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://medium.com/feed/airbnb-engineering) | 全集、工程 |
| [The ASF Blog](https://news.apache.org/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://news.apache.org/feed) | 全集、工程 |
| [The Cloudflare Blog](https://blog.cloudflare.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://blog.cloudflare.com/rss) | 全集、工程 |
| [The GitHub Blog](https://github.blog/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://github.blog/feed/) | 全集、工程 |
| [The Intercom Blog](https://www.intercom.com/blog/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.intercom.com/blog/feed) | 全集、工程 |
| [The JetBrains Blog](https://blog.jetbrains.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://blog.jetbrains.com/feed/) | 全集、工程 |
| [The Loop](https://www.loopinsight.com) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://www.loopinsight.com/feed) | 全集、工程 |
| [The New Stack](https://thenewstack.io/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://thenewstack.io/feed/) | 全集、工程 |
| [Tianhe Gao](https://tianheg.co/) | 主要写生活、技术。 | Engineering & Technology | [RSS](https://tianheg.co/index.xml) | 全集、中文独立博客、中文、工程 |
| [TrumanDu's Blog](http://blog.trumandu.top/atom.xml) | 主要写日记、随笔、学习、技术分享。 | Engineering & Technology | [RSS](http://blog.trumandu.top/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Turing Post](https://www.turingpost.com/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://rss.beehiiv.com/feeds/UJIoBuf5BX.xml) | 全集、工程 |
| [Tw93 Blog](https://tw93.fun) | 主要写开源、前端、分享、MacOS。 | Engineering & Technology | [RSS](https://tw93.fun/feed.xml) | 全集、中文独立博客、中文、工程 |
| [Use Case: copilot - GitHub Changelog](https://github.blog/changelog/label/copilot/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://github.blog/changelog/label/copilot/feed/) | 全集、工程 |
| [Usubeni Fantasy](https://ssshooter.com/) | 主要写前端、随想、游戏、摄影。 | Engineering & Technology | [RSS](https://ssshooter.com/rss.xml) | 全集、中文独立博客、中文、工程 |
| [UWillno's Blog](https://uwillno.com) | 主要写Qt、WASM、技术、记录。 | Engineering & Technology | [RSS](https://uwillno.com/rss.xml) | 全集、中文独立博客、中文、工程 |
| [Vercel News](https://vercel.com/atom) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://vercel.com/atom) | 全集、工程 |
| [Visual Studio Blog](https://devblogs.microsoft.com/visualstudio/) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://devblogs.microsoft.com/visualstudio/feed/) | 全集、工程 |
| [vivo互联网技术](https://wechat2rss.bestblogs.dev/feed/b3ceb5cb1e4602ca55704650a157ec9c5b2f0d31.xml) | Engineering & Technology 订阅源 | Engineering & Technology | [RSS](https://wechat2rss.bestblogs.dev/feed/b3ceb5cb1e4602ca55704650a157ec9c5b2f0d31.xml) | 全集、中文、工程 |
| [Watermelonabc的Blog](https://watermelonabc.top/) | 主要写编程、技术、笔记、生活。 | Engineering & Technology | [RSS](https://watermelonabc.top/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Weishu's Notes](https://weishu.me/) | 主要写编程。 | Engineering & Technology | [RSS](https://weishu.me/atom.xml) | 全集、中文独立博客、中文、工程 |
| [wmhwiki](https://wmhwiki.cn) | 主要写技术、生活。 | Engineering & Technology | [RSS](https://wmhwiki.cn/rss.xml) | 全集、中文独立博客、中文、工程 |
| [WuSiYu Blog](https://wusiyu.me/) | 主要写折腾、技术、DIY、Linux。 | Engineering & Technology | [RSS](https://wusiyu.me/feed/) | 全集、中文独立博客、中文、工程 |
| [x7aNote](https://xeonzilla.top/) | 主要写二次元、技术、随笔。 | Engineering & Technology | [RSS](https://xeonzilla.top/index.xml) | 全集、中文独立博客、中文、工程 |
| [XINDOO](https://zxs.io/) | 主要写算法、编程、人生。 | Engineering & Technology | [RSS](https://zxs.io/feed) | 全集、中文独立博客、中文、工程 |
| [YangXuan's Blog](https://yangxuan.ai) | 主要写AI、投资、量化。 | Engineering & Technology | [RSS](https://yangxuan.ai/feed/) | AI、全集、中文独立博客、中文、工程 |
| [yCENzh's Blog](https://fuwari.oh1.top/) | 主要写技术、随笔、笔记、乱七八糟。 | Engineering & Technology | [RSS](https://fuwari.oh1.top/rss.xml) | 全集、中文独立博客、中文、工程 |
| [YeungYeah's Context](https://scottyeung.top/) | 主要写编程、算法、随笔、玄学。 | Engineering & Technology | [RSS](http://scottyeung.top/atom.xml) | 全集、中文独立博客、中文、工程 |
| [Yi's Blog](https://ycao.net/) | 主要写编程、学习、生活。 | Engineering & Technology | [RSS](https://ycao.top/feed.xml) | 全集、中文独立博客、中文、工程 |
| [Yiran's Blog](https://zdyxry.github.io/) | 主要写编程、Linux。 | Engineering & Technology | [RSS](https://zdyxry.github.io/atom.xml) | 全集、中文独立博客、中文、工程 |
| [YOLO Blog](https://www.yolo.blue/blog) | 主要写编程、随笔、游戏、生活。 | Engineering & Technology | [RSS](https://www.yolo.blue/blog/rss.xml) | 全集、中文独立博客、中文、工程 |
| [ypingcn](https://blog.ypingcn.com/) | 主要写技术、生活、分享、火狐。 | Engineering & Technology | [RSS](https://blog.ypingcn.com/feed.xml) | 全集、中文独立博客、中文、工程 |
| [zhecydn的博客站](https://blog.zhecydn.asia) | 主要写生活、随笔、技术、分享。 | Engineering & Technology | [RSS](https://blog.zhecydn.asia/feed/) | 全集、中文独立博客、中文、工程 |
| [一纸忘忧](https://www.ikxin.com/) | 主要写编程、PHP、开箱、Linux。 | Engineering & Technology | [RSS](https://www.ikxin.com/feed/) | 全集、中文独立博客、中文、工程 |
| [东东's Blog](https://blog.yasking.org/) | 主要写编程、技术、笔记。 | Engineering & Technology | [RSS](https://blog.yasking.org/atom.xml) | 全集、中文独立博客、中文、工程 |
| [东方星痕](https://ystyle.top) | 主要写编程、技术。 | Engineering & Technology | [RSS](https://ystyle.top/atom.xml) | 全集、中文独立博客、中文、工程 |
| [中文博客 on 范叶亮 \| Leo Van](https://leovan.me/cn/) | 主要写编程、算法、数据科学、思考。 | Engineering & Technology | [RSS](https://leovan.me/cn/index.xml) | 全集、中文独立博客、中文、工程 |
| [串串狗小刊 ⭐️](https://www.ccgxk.com/) | 主要写生活、编程、科技、记录。 | Engineering & Technology | [RSS](https://www.ccgxk.com/rss.php) | 全集、中文独立博客、中文、工程 |
| [九仞之行](https://styunlen.cn) | 主要写编程、技术、人文、音乐。 | Engineering & Technology | [RSS](https://styunlen.cn/feed) | 全集、中文独立博客、中文、工程 |
| [了迹奇有没](https://whrss.com/) | 主要写编程、思考、生活随笔。 | Engineering & Technology | [RSS](https://whrss.com/feed) | 全集、中文独立博客、中文、工程 |
| [二丫讲梵](https://wiki.eryajf.net) | 主要写运维、思索、编程。 | Engineering & Technology | [RSS](https://wiki.eryajf.net/rss.xml) | 全集、中文独立博客、中文、工程 |
| [仲平](https://blog.zopiya.com/) | 主要写生活、开发、旅行、摄影。 | Engineering & Technology | [RSS](https://blog.7wate.com/rss.xml) | 全集、中文独立博客、中文、工程 |
| [任霏的个人博客网站](https://blog.renfei.net) | 主要写编程、Java、经验。 | Engineering & Technology | [RSS](https://blog.renfei.net/rss.xml) | 全集、中文独立博客、中文、工程 |
| [伪斜杠青年](https://i.lckiss.com) | 主要写技术、折腾、随记。 | Engineering & Technology | [RSS](http://i.lckiss.com/?feed=rss2) | 全集、中文独立博客、中文、工程 |
| [依云's Blog](https://blog.lilydjwg.me/) | 主要写编程。 | Engineering & Technology | [RSS](https://blog.lilydjwg.me/posts.rss) | 全集、中文独立博客、中文、工程 |
| [侯锐的思考与分享](https://www.nosuchfield.com/) | 主要写编程。 | Engineering & Technology | [RSS](https://www.nosuchfield.com/atom.xml) | 全集、中文独立博客、中文、工程 |
| [保罗的小宇宙](https://paugram.com/) | 主要写生活、随笔、前端、动漫。 | Engineering & Technology | [RSS](https://paugram.com/feed) | 全集、中文独立博客、中文、工程 |
| [傥师妹TangShiMei的小空间](https://blog.224418.xyz/) | 主要写技术、生活、随笔、折腾。 | Engineering & Technology | [RSS](https://blog.224418.xyz/rss2.xml) | 全集、中文独立博客、中文、工程 |
| [傲雪の](https://www.oxue.de/) | 主要写技术、写作、生活、随笔。 | Engineering & Technology | [RSS](https://www.oxue.de/rss.xml) | 全集、中文独立博客、中文、工程 |
| [农码生涯，无酒无花 – The coding life, no wine, no shine.](https://nicrosoft.net/blog) | 主要写编程、生活。 | Engineering & Technology | [RSS](https://nicrosoft.net/blog/feed/) | 全集、中文独立博客、中文、工程 |
| [冰冻大西瓜](https://bddxg.top/) | 主要写前端、编程、生活、AI。 | Engineering & Technology | [RSS](https://bddxg.top/feed.rss) | AI、全集、中文独立博客、中文、工程 |
| [刘郎阁](https://vjo.cc/) | 主要写编程、生活、记录、随笔。 | Engineering & Technology | [RSS](https://vjo.cc/feed/) | 全集、中文独立博客、中文、工程 |
| [创见思考——怎样度过这一生](https://www.fengcan.net) | 主要写AI、读书、医疗、人生决策。 | Engineering & Technology | [RSS](https://www.fengcan.net/feed/) | AI、全集、中文独立博客、中文、工程 |
| [初然忆](https://www.imcry.vip/) | 主要写编程、生活、记录。 | Engineering & Technology | [RSS](https://www.imcry.vip/index.xml) | 全集、中文独立博客、中文、工程 |
| [北门清燕](https://bmqy.net/) | 主要写生活、随笔、前端。 | Engineering & Technology | [RSS](https://www.bmqy.net/feed.xml) | 全集、中文独立博客、中文、工程 |
| [千古八方的博客](https://rangotec.com/feed) | 主要写编程、Android、数据私有化。 | Engineering & Technology | [RSS](https://rangotec.com/feed) | 全集、中文独立博客、中文、工程 |
| [千里之豪的格物垛](https://blog.gadore.top) | 主要写技术、生活、图片。 | Engineering & Technology | [RSS](https://blog.gadore.top/feed.xml) | 全集、中文独立博客、中文、工程 |
| [半方池水半方田](https://blog.uuanqin.top/atom.xml) | 主要写编程、生活、分享。 | Engineering & Technology | [RSS](https://uuanqin.top/atom.xml) | 全集、中文独立博客、中文、工程 |
| [博客 on Neil的自留地](https://neilmin.com/zh/posts/) | 主要写编程、生活、笔记、随想。 | Engineering & Technology | [RSS](https://neilmin.com/zh/posts/index.xml) | 全集、中文独立博客、中文、工程 |
| [卡片创作实验室](https://cnfeat.com/) | 主要写编程。 | Engineering & Technology | [RSS](https://www.cnfeat.com/feed.xml) | 全集、中文独立博客、中文、工程 |
| [卡瓦邦噶！](https://www.kawabangga.com) | 主要写编程、随笔、技术。 | Engineering & Technology | [RSS](https://www.kawabangga.com/feed) | 全集、中文独立博客、中文、工程 |
| [又耳笔记](https://youerning.top/) | 主要写技术、编程、随笔。 | Engineering & Technology | [RSS](https://youerning.top/index.xml) | 全集、中文独立博客、中文、工程 |
| [后端技术杂谈](https://www.rowkey.cn/atom.xml) | 主要写编程。 | Engineering & Technology | [RSS](https://rowkey.cn/atom.xml) | 全集、中文独立博客、中文、工程 |
| [唐巧的博客](https://blog.devtang.com/atom.xml) | 主要写编程、创业、iOS。 | Engineering & Technology | [RSS](https://blog.devtang.com/atom.xml) | 全集、中文独立博客、中文、工程 |
| [喵二の小博客](https://www.miaoer.net) | 主要写技术、生活、学习。 | Engineering & Technology | [RSS](https://www.miaoer.net/feed) | 全集、中文独立博客、中文、工程 |
| [喵喵小站・博客志](https://www.mmbkz.cn/) | 主要写生活、日常、编程、笔记。 | Engineering & Technology | [RSS](https://www.mmbkz.cn/feed) | 全集、中文独立博客、中文、工程 |
| [土木坛子](https://tumutanzi.com) | 主要写科研学习、社会人文、信息技术、国外见闻。 | Engineering & Technology | [RSS](https://tumutanzi.com/feed) | 全集、中文独立博客、中文、工程 |
| [土法炼钢兴趣小组的算法知识备份](https://quant67.com/) | 主要写编程、技术、安全。 | Engineering & Technology | [RSS](https://quant67.com/rss.xml) | 全集、中文独立博客、中文、工程 |
| [土豆不好吃](https://dmesg.app) | 主要写编程。 | Engineering & Technology | [RSS](https://dmesg.app/feed) | 全集、中文独立博客、中文、工程 |
| [坠月川](https://www.hujingnb.com) | 主要写编程、技术。 | Engineering & Technology | [RSS](https://hujingnb.com/feed) | 全集、中文独立博客、中文、工程 |
| [夜法之书](https://blog.17lai.site) | 主要写技术、开源、hexo、成长。 | Engineering & Technology | [RSS](https://blog.17lai.site/atom.xml) | 全集、中文独立博客、中文、工程 |
| [失眠海峡](https://blog.imalan.cn/) | 主要写编程、日常、二次元、读书。 | Engineering & Technology | [RSS](https://blog.imalan.cn/feed.xml) | 全集、中文独立博客、中文、工程 |
| [如有乐享](https://51.ruyo.net) | 主要写技术、分享。 | Engineering & Technology | [RSS](https://51.ruyo.net/feed) | 全集、中文独立博客、中文、工程 |
| [姓王者的博客](https://xingwangzhe.fun/) | 主要写编程，随笔，大学，生活，开源。 | Engineering & Technology | [RSS](https://xingwangzhe.fun/rss.xml) | 全集、中文独立博客、中文、工程 |
| [寒夜雨](https://www.coderlock.site/) | 主要写编程、生活、AI、随想。 | Engineering & Technology | [RSS](https://www.coderlock.site/index.php/feed/) | AI、全集、中文独立博客、中文、工程 |
| [崎径 其镜](http://www.z16388.top/atom.xml) | 主要写编程、游戏、音乐。 | Engineering & Technology | [RSS](http://www.z16388.top/atom.xml) | 全集、中文独立博客、中文、工程 |
| [嵌入式工程猫的博客](https://blog.vvzero.com) | 主要写软硬件全栈开发、生活。 | Engineering & Technology | [RSS](https://blog.vvzero.com/atom.xml) | 全集、中文独立博客、中文、工程 |
| [张戈博客](https://zhang.ge) | 主要写编程、运维。 | Engineering & Technology | [RSS](https://zhang.ge/feed) | 全集、中文独立博客、中文、工程 |
| [张洪Heo](https://blog.zhheo.com/) | 主要写设计、编程、生活、产品。 | Engineering & Technology | [RSS](https://blog.zhheo.com/rss.xml) | 全集、中文独立博客、中文、工程 |
| [张鑫旭-鑫空间-鑫生活](https://www.zhangxinxu.com/wordpress) | 主要写编程、前端。 | Engineering & Technology | [RSS](http://www.zhangxinxu.com/wordpress/?feed=rss2) | 全集、中文独立博客、中文、工程 |
| [愆伏](https://www.tortorse.com/atom.xml) | 主要写产品、前端、设计、杂谈。 | Engineering & Technology | [RSS](https://www.tortorse.com/atom.xml) | 全集、中文独立博客、中文、工程 |
| [我不是咕咕鸽](https://blog.laoda.de) | 主要写编程、技术分享、网络、容器。 | Engineering & Technology | [RSS](https://blog.laoda.de/rss.xml) | 全集、中文独立博客、中文、工程 |
| [所谓空想](https://www.alxh.page) | 主要写文学、音乐、技术。 | Engineering & Technology | [RSS](https://www.alxh.page/feed.rss) | 全集、中文独立博客、中文、工程 |
| [把酒诗代码](https://102no.com/) | 主要写编程、随笔。 | Engineering & Technology | [RSS](https://102no.com/atom.xml) | 全集、中文独立博客、中文、工程 |
| [披萨盒的赛博日志](https://blog.pushihao.com/atom.xml) | 主要写编程、AI、全栈、思考。 | Engineering & Technology | [RSS](https://blog.pushihao.com/atom.xml) | AI、全集、中文独立博客、中文、工程 |
| [敖苛记](https://blog.kayro.cn/) | 主要写生活、技术、编程、开源。 | Engineering & Technology | [RSS](https://blog.kayro.cn/atom.xml) | 全集、中文独立博客、中文、工程 |
| [文武科技柜](https://www.wangdu.site) | 主要写编程、软件、随笔、生活。 | Engineering & Technology | [RSS](https://www.wangdu.site/feed) | 全集、中文独立博客、中文、工程 |
| [文艺数学君](https://mathpretty.com) | 主要写编程、生活、数学。 | Engineering & Technology | [RSS](https://mathpretty.com/feed/) | 全集、中文独立博客、中文、工程 |
| [方永、南天紫雲](https://www.vinoca.org) | 主要写编程、随笔。 | Engineering & Technology | [RSS](https://www.vinoca.org/atom.xml) | 全集、中文独立博客、中文、工程 |
| [明立非\|Mingnify的博客](https://mingnify.com/zh/blog/atom.xml) | 主要写Indie Maker、独立开发、AI、打造产品。 | Engineering & Technology | [RSS](https://mingnify.com/zh/blog/atom.xml) | AI、全集、中文独立博客、中文、工程 |
| [星觅海的博客](https://www.xmhai.cn) | 主要写技术、生活、资源。 | Engineering & Technology | [RSS](https://www.xmhai.cn/rss.xml) | 全集、中文独立博客、中文、工程 |
| [映屿](https://blog.verdant.ee/) | 主要写技术、随笔、思考、阅读。 | Engineering & Technology | [RSS](https://www.glowisle.me/atom.xml) | 全集、中文独立博客、中文、工程 |
| [晓空blog](https://blog.moeworld.tech) | 主要写生活、开发，日常、二次元、游戏。 | Engineering & Technology | [RSS](https://blog.moeworld.tech/feed/) | 全集、中文独立博客、中文、工程 |
| [晴雀堂](https://blog.verynb.net/atom.xml) | 主要写技术、随笔、思考、成长。 | Engineering & Technology | [RSS](https://hehysh.github.io/atom.xml) | 全集、中文独立博客、中文、工程 |
| [朝舞网](https://ii74.com/) | 主要写编程、随笔。 | Engineering & Technology | [RSS](https://ii74.com/feed.php) | 全集、中文独立博客、中文、工程 |
| [杜老师说](https://dusays.com/) | 主要写运维，数码，资源。 | Engineering & Technology | [RSS](https://dusays.com/atom.xml) | 全集、中文独立博客、中文、工程 |
| [枫林灯语](https://blog.mfwt.top/) | 主要写编程、生活、技术、无线电。 | Engineering & Technology | [RSS](https://blog.mfwt.top/index.php/feed/) | 全集、中文独立博客、中文、工程 |
| [橙树志 ｜ citydatum](https://citydatum.cn) | 主要写城市、数据分析、技术、视觉。 | Engineering & Technology | [RSS](https://citydatum.cn/feed) | 全集、中文独立博客、中文、工程 |
| [欧雷流](https://ourai.ws/) | 主要写编程、前端、生活、思考。 | Engineering & Technology | [RSS](https://ourai.ws/atom.xml) | 全集、中文独立博客、中文、工程 |
| [歌词经理](https://blog.lyric.im/feed/atom) | 主要写产品、创业、编程。 | Engineering & Technology | [RSS](https://quaily.com/lyric/feed/atom) | 全集、中文独立博客、中文、工程 |
| [残页的小博客](https://blog.canyie.top/) | 主要写编程、Android、生活。 | Engineering & Technology | [RSS](https://blog.canyie.top/atom.xml) | 全集、中文独立博客、中文、工程 |
| [泠泫凝的异次元空间](https://lxnchan.cn/atom.xml) | 主要写运维、后端。 | Engineering & Technology | [RSS](https://lxnchan.cn/atom.xml) | 全集、中文独立博客、中文、工程 |
| [泫言](https://blog.cugxuan.cn/) | 主要写生活、编程、科技、记录。 | Engineering & Technology | [RSS](https://blog.cugxuan.cn/atom.xml) | 全集、中文独立博客、中文、工程 |
| [流动](https://liudon.com/) | 主要写技术、生活。 | Engineering & Technology | [RSS](https://liudon.com/index.xml) | 全集、中文独立博客、中文、工程 |
| [浅时光博客](https://www.dqzboy.com) | 主要写编程、技术分享、学习笔记。 | Engineering & Technology | [RSS](https://www.dqzboy.com/feed) | 全集、中文独立博客、中文、工程 |
| [涛叔](https://tao.zz.ac) | 主要写技术、学习、思考。 | Engineering & Technology | [RSS](https://taoshu.in/feed.xml) | 全集、中文独立博客、中文、工程 |
| [润土分享](https://runtushare.net) | 主要写编程。 | Engineering & Technology | [RSS](http://xiaix.me/rss/) | 全集、中文独立博客、中文、工程 |
| [清竹志-(原清竹茶馆)](https://blog.vadxq.com/atom.xml) | 主要写编程、前端、全栈、生活。 | Engineering & Technology | [RSS](https://blog.vadxq.com/atom.xml) | 全集、中文独立博客、中文、工程 |
| [游魂博客](https://www.iyouhun.com/) | 主要写编程、前端、技术、生活。 | Engineering & Technology | [RSS](https://www.iyouhun.com/rss.php) | 全集、中文独立博客、中文、工程 |
| [澄沨的漫游茶记](https://champhoon.xyz/) | 主要写ACG、日常、随笔、技术。 | Engineering & Technology | [RSS](https://champhoon.xyz/atom.xml) | 全集、中文独立博客、中文、工程 |
| [烧饼博客](https://u.sb/) | 主要写运维、域名。 | Engineering & Technology | [RSS](https://u.sb/rss.xml) | 全集、中文独立博客、中文、工程 |
| [猫涅的秘密结社](http://www.maonie.top/) | 主要写技术、信息安全、随笔、编程。 | Engineering & Technology | [RSS](https://www.maonie.top/atom.xml) | 全集、中文独立博客、中文、工程 |
| [猿客随笔](https://monkeyke.com/) | 主要写编程、生活、随笔。 | Engineering & Technology | [RSS](https://monkeyke.com/index.xml) | 全集、中文独立博客、中文、工程 |
| [王圆圆 - ICONPIK](https://www.iconpik.com/) | 主要写AI、编程、随笔。 | Engineering & Technology | [RSS](https://www.iconpik.com/rss/) | AI、全集、中文独立博客、中文、工程 |
| [王欣说AI](https://wangxin.io/) | 主要写后端、开源、RPC、微服务。 | Engineering & Technology | [RSS](https://wangxin.io/atom.xml) | 全集、中文独立博客、中文、工程 |
| [王登科-DK博客](https://greatdk.com) | 主要写编程、创业。 | Engineering & Technology | [RSS](https://greatdk.com/feed) | 全集、中文独立博客、中文、工程 |
| [王福强的个人博客：一个架构士的思考与沉淀](http://afoo.me) | 主要写架构、创业、思考。 | Engineering & Technology | [RSS](https://afoo.me/feeds.xml) | 全集、中文独立博客、中文、工程 |
| [瓦解的生活记事](https://hin.cool/atom.xml) | 主要写分享、记录、技术、写作。 | Engineering & Technology | [RSS](https://hin.cool/atom.xml) | 全集、中文独立博客、中文、工程 |
| [白宦成](https://www.ixiqin.com) | 主要写编程、开源。 | Engineering & Technology | [RSS](https://www.ixiqin.com/feed/) | 全集、中文独立博客、中文、工程 |
| [白菜](https://blog.baicai.me/) | 主要写随笔、技术、经验、旅行。 | Engineering & Technology | [RSS](https://blog.baicai.me/index.xml) | 全集、中文独立博客、中文、工程 |
| [皓子的小站](https://howiehz.top) | 主要写技术、编程、开源、前端。 | Engineering & Technology | [RSS](https://howiehz.top/rss.xml) | 全集、中文独立博客、中文、工程 |
| [看川博客](https://kanchuan.com/blog) | 主要写iOS、开发、产品、生活。 | Engineering & Technology | [RSS](https://kanchuan.com/feed.xml) | 全集、中文独立博客、中文、工程 |
| [码农明明桑](https://isming.me/?utm_source=rss) | 主要写技术、生活、旅行、读书。 | Engineering & Technology | [RSS](https://isming.me/index.xml) | 全集、中文独立博客、中文、工程 |
| [码录集](https://www.coderlog.net) | 主要写编程、AI、C#、.NET。 | Engineering & Technology | [RSS](https://www.coderlog.net/rss.xml) | AI、全集、中文独立博客、中文、工程 |
| [空屿](https://pinaland.cn/) | 主要写日常、二次元、动画、游戏。 | Engineering & Technology | [RSS](https://pinaland.cn/feed/) | 全集、中文独立博客、中文、工程 |
| [空鸣深语](https://blog.deepchirp.com/) | 主要写技术、生活、随笔。 | Engineering & Technology | [RSS](https://blog.deepchirp.com/atom.xml) | 全集、中文独立博客、中文、工程 |
| [竹林里有冰的博客](https://zhul.in) | 主要写技术、折腾、笔记、分享。 | Engineering & Technology | [RSS](https://zhul.in/rss.xml) | 全集、中文独立博客、中文、工程 |
| [粥里有勺糖](https://sugarat.top) | 主要写编程、大前端、开源、生活。 | Engineering & Technology | [RSS](https://sugarat.top/feed.rss) | 全集、中文独立博客、中文、工程 |
| [繁星点点](https://blog.52013120.xyz) | 主要写编程、技术、原创、网络。 | Engineering & Technology | [RSS](https://blog.52013120.xyz/rss.xml) | 全集、中文独立博客、中文、工程 |
| [维基萌](https://www.wikimoe.com) | 主要写动画、漫画、游戏、日常。 | Engineering & Technology | [RSS](https://www.wikimoe.com/rss.php) | 全集、中文独立博客、中文、工程 |
| [罗磊的独立博客](https://luolei.org) | 主要写编程、旅行。 | Engineering & Technology | [RSS](http://luolei.org/feed/) | 全集、中文独立博客、中文、工程 |
| [翔宇工作流](https://xiangyugongzuoliu.com/) | 主要写AI、编程、自动化、Claude Code。 | Engineering & Technology | [RSS](https://xiangyugongzuoliu.com/latest/rss/) | AI、全集、中文独立博客、中文、工程 |
| [老范讲故事｜AI、大模型与商业世界的故事](https://lukefan.com) | 主要写编程。 | Engineering & Technology | [RSS](http://lukefan.com/?feed=rss2) | 全集、中文独立博客、中文、工程 |
| [肘子的 Swift 记事本 ｜ Fatbobman's Blog](https://fatbobman.com/) | 主要写编程、Swift、SwiftUI。 | Engineering & Technology | [RSS](https://fatbobman.com/zh/rss.xml) | 全集、中文独立博客、中文、工程 |
| [胡涂说](https://hutusi.com) | 主要写编程、随笔、生活。 | Engineering & Technology | [RSS](https://hutusi.com/feed.xml) | 全集、中文独立博客、中文、工程 |
| [草梅友仁的博客](https://blog.cmyr.ltd/atom.xml) | 主要写编程、技术、前端、日常。 | Engineering & Technology | [RSS](https://blog.cmyr.ltd/atom.xml) | 全集、中文独立博客、中文、工程 |
| [莫尔索随笔](https://liduos.com/atom.xml) | 主要写Python、SDN、读书笔记、LLM应用开发。 | Engineering & Technology | [RSS](https://liduos.com/atom.xml) | 全集、中文独立博客、中文、工程 |
| [蒙需](https://jiangcl.com) | 主要写法律、生活、编程、工程。 | Engineering & Technology | [RSS](https://jiangcl.com/feed) | 全集、中文独立博客、中文、工程 |
| [虹墨空间站](https://www.imaegoo.com/) | 主要写编程、前端、Serverless。 | Engineering & Technology | [RSS](https://www.imaegoo.com/atom.xml) | 全集、中文独立博客、中文、工程 |
| [蚊子的前端博客](https://www.xiabingbao.com) | 主要写编程、前端。 | Engineering & Technology | [RSS](https://www.xiabingbao.com/atom.xml) | 全集、中文独立博客、中文、工程 |
| [謝懿Shine](https://www.futseyi.com/) | 主要写技术开源、大模型、AI、生活。 | Engineering & Technology | [RSS](https://xieyi.org/rss.xml) | AI、全集、中文独立博客、中文、工程 |
| [豌豆花下猫](https://pythoncat.top/) | 主要写编程、Python、翻译、随笔。 | Engineering & Technology | [RSS](https://pythoncat.top/rss.xml) | 全集、中文独立博客、中文、工程 |
| [轶哥博客](https://www.wyr.me) | 主要写编程、全栈、随笔。 | Engineering & Technology | [RSS](https://www.wyr.me/rss.xml) | 全集、中文独立博客、中文、工程 |
| [运维咖啡吧](https://blog.ops-coffee.com/atom.xml) | 主要写devops、运维、自动化开发、技术。 | Engineering & Technology | [RSS](https://blog.ops-coffee.cn/feed.xml) | 全集、中文独立博客、中文、工程 |
| [运维开发绿皮书](https://www.geekery.cn/) | 主要写技术、生活、开源。 | Engineering & Technology | [RSS](https://www.geekery.cn/rss.xml) | 全集、中文独立博客、中文、工程 |
| [远飞闲记](https://heyuanfei.com/) | 主要写阅读、思考、生活、技术。 | Engineering & Technology | [RSS](https://leonhe.cn/index.xml) | 全集、中文独立博客、中文、工程 |
| [迷途小书童的Note](https://xugaoxiang.com/) | 主要写工作、编程、技术。 | Engineering & Technology | [RSS](https://xugaoxiang.com/feed) | 全集、中文独立博客、中文、工程 |
| [逸思杂陈](https://blog.ponder.work/atom.xml) | 主要写编程、随笔。 | Engineering & Technology | [RSS](https://blog.ponder.work/atom.xml) | 全集、中文独立博客、中文、工程 |
| [酥米的小站](https://www.sumi233.top/) | 主要写生活，技术，网络，日常，随笔。 | Engineering & Technology | [RSS](https://www.sumi233.top/rss.xml) | 全集、中文独立博客、中文、工程 |
| [阁子](https://dfine.tech/atom.xml) | 主要写编程、算法、生活。 | Engineering & Technology | [RSS](https://dfine.tech/atom.xml) | 全集、中文独立博客、中文、工程 |
| [阿尔的代码屋 \| 全栈技术笔记](https://blog.algieba12.cn/) | 主要写随笔、AI、游戏开发、C++。 | Engineering & Technology | [RSS](https://blog.algieba12.cn/atom.xml) | AI、全集、中文独立博客、中文、工程 |
| [阿掖山·博客](https://blog.mountaye.com) | 主要写物理、生物、编程、摄影。 | Engineering & Technology | [RSS](https://blog.mountaye.com/feed.xml) | 全集、中文独立博客、中文、工程 |
| [雪猫社](https://www.yukicat.net) | 主要写生活、随笔、运维、思考。 | Engineering & Technology | [RSS](https://www.yukicat.net/feed/) | 全集、中文独立博客、中文、工程 |
| [雪的数字花园 ❄️](https://blog.rnm.gv.uy/) | 主要写编程、开源、前端、折腾。 | Engineering & Technology | [RSS](https://blog.rnm.gv.uy/atom.xml) | 全集、中文独立博客、中文、工程 |
| [青石坞](https://www.qs5.org/) | 主要写技术、生活。 | Engineering & Technology | [RSS](https://www.qs5.org/feed/) | 全集、中文独立博客、中文、工程 |
| [非学·派'](https://fxpai.com) | 主要写摄影、技术、随笔。 | Engineering & Technology | [RSS](https://fxpai.com/feed) | 全集、中文独立博客、中文、工程 |
| [顶尖研发](https://bestcoder.cn/) | 主要写日常、随笔、技术。 | Engineering & Technology | [RSS](https://bestcoder.cn/feed) | 全集、中文独立博客、中文、工程 |
| [首页 on black8](https://0x8.net/) | 主要写编程、技术、linux、生活。 | Engineering & Technology | [RSS](https://unixetc.com/index.xml) | 全集、中文独立博客、中文、工程 |
| [鸟窝](https://colobu.com/) | 主要写编程。 | Engineering & Technology | [RSS](https://colobu.com/atom.xml) | 全集、中文独立博客、中文、工程 |
| [黑羽的个人博客](https://blog.thetbw.xyz) | 主要写编程、随笔、生活。 | Engineering & Technology | [RSS](https://blog.thetbw.xyz/atom.xml) | 全集、中文独立博客、中文、工程 |
| [𝟞𝟙𝟡'𝕤 𝔹𝕃𝕆𝔾](https://619.pp.ua) | 主要写学习、编程、随笔。 | Engineering & Technology | [RSS](https://66619.eu.org/feed/) | 全集、中文独立博客、中文、工程 |

</details>

<details>
<summary>Research & Science · 19</summary>

| 名称 | 介绍 | 主分类 | Feed | 所属合集 |
| --- | --- | --- | --- | --- |
| [AAAS: Science: Table of Contents](https://www.science.org/loi/science?af=R) | Research & Science 订阅源 | Research & Science | [RSS](https://www.science.org/action/showFeed?type=etoc&feed=rss&jc=science) | 全集、科研 |
| [All Top News -- ScienceDaily](https://www.sciencedaily.com/news/top/) | Research & Science 订阅源 | Research & Science | [RSS](https://www.sciencedaily.com/rss/top/science.xml) | 全集、科研 |
| [Amazon Science](https://www.amazon.science/) | Research & Science 订阅源 | Research & Science | [RSS](https://www.amazon.science/index.rss) | 全集、科研 |
| [BBC News — Science](https://www.bbc.co.uk/news/science_and_environment) | Research & Science 订阅源 | Research & Science | [RSS](https://feeds.bbci.co.uk/news/science_and_environment/rss.xml) | 全集、科研 |
| [eLife: latest articles](https://elifesciences.org) | Research & Science 订阅源 | Research & Science | [RSS](https://elifesciences.org/rss/recent.xml) | 全集、科研 |
| [FlowingData](https://flowingdata.com) | Research & Science 订阅源 | Research & Science | [RSS](https://flowingdata.com/feed) | 全集、科研 |
| [Latest Science News -- ScienceDaily](https://www.sciencedaily.com/news/) | Research & Science 订阅源 | Research & Science | [RSS](https://www.sciencedaily.com/rss/all.xml) | 全集、科研 |
| [NASA](https://www.nasa.gov) | Research & Science 订阅源 | Research & Science | [RSS](https://www.nasa.gov/news-release/feed/) | 全集、科研 |
| [Nature](http://feeds.nature.com/nature/rss/current) | Research & Science 订阅源 | Research & Science | [RSS](https://www.nature.com/nature.rss) | 全集、科研 |
| [NYT > Science](https://www.nytimes.com/section/science) | Research & Science 订阅源 | Research & Science | [RSS](https://rss.nytimes.com/services/xml/rss/nyt/Science.xml) | 全集、科研 |
| [Phys.org - latest science and technology news stories](https://phys.org/) | Research & Science 订阅源 | Research & Science | [RSS](https://phys.org/rss-feed/) | 全集、科研 |
| [PLOS One](https://journals.plos.org/plosone/) | Research & Science 订阅源 | Research & Science | [RSS](https://journals.plos.org/plosone/feed/atom) | 全集、科研 |
| [Quanta Magazine](https://www.quantamagazine.org) | Research & Science 订阅源 | Research & Science | [RSS](https://www.quantamagazine.org/feed/) | 全集、科研 |
| [Science Latest](https://www.wired.com) | Research & Science 订阅源 | Research & Science | [RSS](https://www.wired.com/feed/category/science/latest/rss) | 全集、科研 |
| [Scientific American Content: Global](https://www.scientificamerican.com) | Research & Science 订阅源 | Research & Science | [RSS](http://rss.sciam.com/ScientificAmerican-Global) | 全集、科研 |
| [Space \| The Guardian](https://www.theguardian.com/science/space) | Research & Science 订阅源 | Research & Science | [RSS](https://www.theguardian.com/science/space/rss) | 全集、科研 |
| [Space – latest in science and technology \| New Scientist](https://www.newscientist.com/subject/space/) | Research & Science 订阅源 | Research & Science | [RSS](https://www.newscientist.com/subject/space/feed/) | 全集、科研 |
| [腾讯研究院](https://wechat2rss.bestblogs.dev/feed/6152301e0978bffb0a8284cab339262b9764dcfb.xml) | Research & Science 订阅源 | Research & Science | [RSS](https://wechat2rss.bestblogs.dev/feed/6152301e0978bffb0a8284cab339262b9764dcfb.xml) | 全集、中文、科研 |
| [阿里研究院](https://wechat2rss.bestblogs.dev/feed/e2f1190c120f7f3d74b630bfcfe9e58296bd535c.xml) | Research & Science 订阅源 | Research & Science | [RSS](https://wechat2rss.bestblogs.dev/feed/e2f1190c120f7f3d74b630bfcfe9e58296bd535c.xml) | 全集、中文、科研 |

</details>

<details>
<summary>News · 34</summary>

| 名称 | 介绍 | 主分类 | Feed | 所属合集 |
| --- | --- | --- | --- | --- |
| [36氪](http://36kr.com) | News 订阅源 | News | [RSS](https://www.36kr.com/feed) | 全集、中文、新闻 |
| [AIGC Weekly](https://quaily.com/op7418/feed/atom) | News 订阅源 | News | [RSS](https://quaily.com/op7418/feed/atom) | 全集、新闻 |
| [Al Jazeera – Breaking News, World News and Video from Al Jazeera](https://www.aljazeera.com) | News 订阅源 | News | [RSS](https://www.aljazeera.com/xml/rss/all.xml) | 全集、新闻 |
| [BBC News — News](https://www.bbc.co.uk/news/world) | News 订阅源 | News | [RSS](https://feeds.bbci.co.uk/news/world/rss.xml) | 全集、新闻 |
| [Cointelegraph.com News](https://cointelegraph.com) | News 订阅源 | News | [RSS](https://cointelegraph.com/rss/tag/blockchain) | 全集、新闻 |
| [Engadget - Technology News & Expert Reviews](https://www.engadget.com/) | News 订阅源 | News | [RSS](https://www.engadget.com/rss.xml) | 全集、新闻 |
| [Golang Weekly](https://golangweekly.com/) | News 订阅源 | News | [RSS](https://golangweekly.com/rss/) | 全集、新闻 |
| [HackerNews每日摘要 on SuperTechFans](https://supertechfans.com/cn/) | News 订阅源 | News | [RSS](https://www.supertechfans.com/cn/index.xml) | 全集、中文、新闻 |
| [InfoQ — News](https://www.infoq.com) | News 订阅源 | News | [RSS](https://feed.infoq.com/) | 全集、新闻 |
| [InfoQ 推荐](https://www.infoq.cn) | News 订阅源 | News | [RSS](https://plink.anyfeeder.com/infoq/recommend) | 全集、中文、新闻 |
| [IT之家](https://www.ithome.com/) | News 订阅源 | News | [RSS](https://www.ithome.com/rss/) | 全集、中文、新闻 |
| [MIT 科技评论 - 本周热榜](https://www.mittrchina.com/hot) | News 订阅源 | News | [RSS](https://rsshub.bestblogs.dev/mittrchina/hot) | 全集、中文、新闻 |
| [News from Google](https://blog.google/) | News 订阅源 | News | [RSS](https://blog.google/rss) | 全集、工程、新闻 |
| [NPR Topics: World](https://www.npr.org/templates/story/story.php?storyId=1004) | News 订阅源 | News | [RSS](https://feeds.npr.org/1004/rss.xml) | 全集、新闻 |
| [NYT > Technology](https://www.nytimes.com/section/technology) | News 订阅源 | News | [RSS](https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml) | 全集、新闻 |
| [NYT > World News](https://www.nytimes.com/section/world) | News 订阅源 | News | [RSS](https://rss.nytimes.com/services/xml/rss/nyt/World.xml) | 全集、新闻 |
| [ProPublica](https://www.propublica.org/) | News 订阅源 | News | [RSS](https://www.propublica.org/feeds/propublica/main) | 全集、新闻 |
| [TechCrunch](https://techcrunch.com/) | News 订阅源 | News | [RSS](https://techcrunch.com/feed/) | 全集、新闻 |
| [The Verge — News](https://www.theverge.com) | News 订阅源 | News | [RSS](https://www.theverge.com/rss/index.xml) | 全集、新闻 |
| [Top stories - Google News](https://news.google.com/?hl=en-US&gl=US&ceid=US:en) | News 订阅源 | News | [RSS](https://news.google.com/rss) | 全集、新闻 |
| [WIRED](https://www.wired.com) | News 订阅源 | News | [RSS](https://www.wired.com/feed/rss) | 全集、新闻 |
| [World](https://www.washingtonpost.com) | News 订阅源 | News | [RSS](https://feeds.washingtonpost.com/rss/world) | 全集、新闻 |
| [World news \| The Guardian](https://www.theguardian.com/world) | News 订阅源 | News | [RSS](https://www.theguardian.com/world/rss) | 全集、新闻 |
| [World News, Today World News, Latest International News, World Breaking News, Trending News of World - Times of India](https://timesofindia.indiatimes.com/world) | News 订阅源 | News | [RSS](https://timesofindia.indiatimes.com/rssfeeds/296589292.cms) | 全集、新闻 |
| [大橘和朋友们的周刊](https://rrorangeandfriends.de) | News 订阅源 | News | [RSS](https://rrorangeandfriends.de/feed.xml) | 全集、中文、新闻 |
| [奇客Solidot–传递最新科技情报](https://www.solidot.org) | News 订阅源 | News | [RSS](https://www.solidot.org/index.rss) | 全集、中文、新闻 |
| [安全客-有思想的安全新媒体](https://www.anquanke.com) | News 订阅源 | News | [RSS](https://api.anquanke.com/data/v1/rss) | 全集、中文、新闻 |
| [少数派](https://sspai.com) | News 订阅源 | News | [RSS](https://sspai.com/feed) | 全集、中文、新闻 |
| [掘金本周最热](https://juejin.im/recommended?sort=weekly_hottest) | News 订阅源 | News | [RSS](https://rsshub.bestblogs.dev/juejin/trending/all/weekly) | 全集、中文、新闻 |
| [潮流周刊](https://weekly.tw93.fun/) | News 订阅源 | News | [RSS](https://weekly.tw93.fun/rss.xml) | 全集、中文、新闻 |
| [站长之家](http://www.chinaz.com) | News 订阅源 | News | [RSS](https://app.chinaz.com/?app=rss) | 全集、中文、新闻 |
| [蓝点网](https://www.landian.news) | News 订阅源 | News | [RSS](https://www.landiannews.com/feed) | 全集、中文、新闻 |
| [虎嗅](https://www.huxiu.com) | News 订阅源 | News | [RSS](https://rss.huxiu.com/) | 全集、中文、新闻 |
| [钛媒体：引领未来商业与生活新知](http://www.tmtpost.com) | News 订阅源 | News | [RSS](https://www.tmtpost.com/feed) | 全集、中文、新闻 |

</details>

<details>
<summary>Product & Design · 4</summary>

| 名称 | 介绍 | 主分类 | Feed | 所属合集 |
| --- | --- | --- | --- | --- |
| [61’s life](https://61.life/) | 主要写创业、管理、产品。 | Product & Design | [RSS](https://61.life/feed.xml) | 全集、中文独立博客、中文 |
| [jax](https://cdjax.com) | 主要写产品、数码、随笔。 | Product & Design | [RSS](https://cdjax.com/?feed=rss2) | 全集、中文独立博客、中文 |
| [Velas电波站](https://www.velasx.com/) | 主要写动画、游戏、小说、设计。 | Product & Design | [RSS](https://www.velasx.com/feed) | 全集、中文独立博客、中文 |
| [拾月的博客](https://www.skyue.com/) | 主要写生活、股票投资、产品经理、软件数码。 | Product & Design | [RSS](https://www.skyue.com/feed/) | 全集、中文独立博客、中文 |

</details>

<details>
<summary>Business & Startups · 5</summary>

| 名称 | 介绍 | 主分类 | Feed | 所属合集 |
| --- | --- | --- | --- | --- |
| [Macin](https://macin.org/atom.xml) | 主要写分享、投资、学习、Crypto。 | Business & Startups | [RSS](https://www.macin.org/atom.xml) | 全集、中文独立博客、中文 |
| [扯氮集](http://weiwuhui.com) | 主要写创业、人生。 | Business & Startups | [RSS](http://weiwuhui.com/feed) | 全集、中文独立博客、中文 |
| [知足常乐-水星投资理财的基本意念](http://mercurychong.blogspot.com/) | 主要写投资。 | Business & Startups | [RSS](http://mercurychong.blogspot.com/feeds/posts/default) | 全集、中文独立博客、中文 |
| [虹线](https://1q43.blog) | 主要写商业、社科、科技、生活。 | Business & Startups | [RSS](https://1q43.blog/feed) | 全集、中文独立博客、中文 |
| [雷蒙三十｜幫助忙碌現代人的聰明工作、好好生活的生產力指南](https://raymondhouch.com) | 主要写创业、数码、数字游民、生产力工具。 | Business & Startups | [RSS](https://raymondhouch.com/feed) | 全集、中文独立博客、中文 |

</details>

<details>
<summary>Personal Blogs · 65</summary>

| 名称 | 介绍 | 主分类 | Feed | 所属合集 |
| --- | --- | --- | --- | --- |
| [ABB00717](https://blog.abb00717.com) | 主要写資訊安全、程式設計、技術、寫作。 | Personal Blogs | [RSS](https://blog.abb00717.com/index.xml) | 全集、中文独立博客、中文 |
| [Another Dayu](https://anotherdayu.com/) | 主要写日常、流行病与卫生统计、科技、数码。 | Personal Blogs | [RSS](https://anotherdayu.com/feed/) | 全集、中文独立博客、中文 |
| [Blog \| Lyunvy](https://blog.lyunvy.top/) | 主要写生活、学习。 | Personal Blogs | [RSS](https://blog.lyunvy.top/atom.xml) | 全集、中文独立博客、中文 |
| [BMPI](https://www.bmpi.dev/) | 主要写Learn、Dev、Trade。 | Personal Blogs | [RSS](https://www.bmpi.dev/index.xml) | 全集、中文独立博客、中文 |
| [by Upsangel](https://upsangel.com/) | 主要写网路硬件、NAS、单板电脑、记录。 | Personal Blogs | [RSS](https://upsangel.com/feed/) | 全集、中文独立博客、中文 |
| [Conge](https://conge.livingwithfcs.org/) | 主要写生活、跑步、阅读。 | Personal Blogs | [RSS](https://conge.github.io/feed.xml) | 全集、中文独立博客、中文 |
| [Cosmos的博客](https://cosmo-polite.com) | 主要写北美生活、思维碎片。 | Personal Blogs | [RSS](https://cosmo-polite.com/feed/) | 全集、中文独立博客、中文 |
| [David Blog](https://blog.blahaj.uk/) | 主要写生活、随笔、影评、作品集。 | Personal Blogs | [RSS](https://blog.blahaj.uk/feed) | 全集、中文独立博客、中文 |
| [Deep Router](https://deeprouter.org/) | 主要写路由器、家庭网络、工具、OpenWRT。 | Personal Blogs | [RSS](https://deeprouter.org/rss/feed.xml) | 全集、中文独立博客、中文 |
| [Dejavu's Blog](https://blog.dejavu.moe/) | 主要写折腾、学习、生活、日志。 | Personal Blogs | [RSS](https://blog.dejavu.moe/index.xml) | 全集、中文独立博客、中文 |
| [Dort 的博客](https://blog.dort.me/) | 主要写随笔、生活、记录。 | Personal Blogs | [RSS](https://blog.dort.me/rss.xml) | 全集、中文独立博客、中文 |
| [Evan's Space](https://www.evan.xin) | 主要写生活。 | Personal Blogs | [RSS](https://evan.xin/feed) | 全集、中文独立博客、中文 |
| [Fei's Tours & Tales](https://www.feifun.cn/feed.xml) | 主要写旅行、复古计算设备、随笔。 | Personal Blogs | [RSS](https://www.feifun.cn/feed.xml) | 全集、中文独立博客、中文 |
| [Fernweh](https://blog.wohin.me/) | 主要写信息安全、诗歌、随笔。 | Personal Blogs | [RSS](https://blog.wohin.me/index.xml) | 全集、中文独立博客、中文 |
| [GentleLucky](https://blog.gentlelucky.com/zh/) | 主要写随笔、思考、Java、知识管理。 | Personal Blogs | [RSS](https://blog.gentlelucky.com/zh/index.xml) | 全集、中文独立博客、中文 |
| [happy xiao](https://happyxiao.com) | 主要写个人成长。 | Personal Blogs | [RSS](https://happyxiao.com/feed) | 全集、中文独立博客、中文 |
| [ImPatrick](https://impatrick.blog) | 主要写繁中、攝影、生活、記錄。 | Personal Blogs | [RSS](https://impatrick.blog/feed/) | 全集、中文独立博客、中文 |
| [Jake blog](https://jaketao.com) | 主要写硅谷科技、主机游戏、留学旅居、跨境电商。 | Personal Blogs | [RSS](https://jaketao.com/feed/) | 全集、中文独立博客、中文 |
| [Jame](https://jame.work/) | 主要写随笔。 | Personal Blogs | [RSS](https://jame.work/feed.xml) | 全集、中文独立博客、中文 |
| [JustZht's EchoChamber](https://www.justzht.com/) | 主要写随笔。 | Personal Blogs | [RSS](https://www.justzht.com/rss/) | 全集、中文独立博客、中文 |
| [jz's ramblings](https://ramble.imzh.me/) | 主要写随笔。 | Personal Blogs | [RSS](https://ramble.imzh.me/index.xml) | 全集、中文独立博客、中文 |
| [LCZBlog](https://blog.licaoz.com/) | 主要写生活、笔记。 | Personal Blogs | [RSS](https://blog.licaoz.com/feed/) | 全集、中文独立博客、中文 |
| [LoRexxar's Blog \| 信息技术分享](https://lorexxar.cn/atom.xml) | 主要写安全。 | Personal Blogs | [RSS](https://lorexxar.cn/atom.xml) | 全集、中文独立博客、中文 |
| [M-x Chris-An-Emacser](https://chriszheng.science/) | 主要写随笔、Emacs。 | Personal Blogs | [RSS](https://chriszheng.science/atom.xml) | 全集、中文独立博客、中文 |
| [Markon Review](https://markonreview.com/) | 主要写游戏及产业评论。 | Personal Blogs | [RSS](https://markonreview.com/rss/) | 全集、中文独立博客、中文 |
| [Redish101 Blog](https://blog.redish101.top/) | 主要写Python、Java、随笔。 | Personal Blogs | [RSS](https://blog.redish101.top/atom.xml) | 全集、中文独立博客、中文 |
| [Save the Web Project](https://blog.save-web.org) | 主要写存档、备份、互联网、公益。 | Personal Blogs | [RSS](https://blog.save-web.org/feed/) | 全集、中文独立博客、中文 |
| [SEISAMUSE](https://www.seis-jun.xyz/atom.xml) | 主要写科研、学习、生活。 | Personal Blogs | [RSS](https://www.seis-jun.xyz/atom.xml) | 全集、中文独立博客、中文 |
| [Shuibaco • 水八口](http://shuiba.co/) | 主要写日常、旅途、思考。 | Personal Blogs | [RSS](https://shuiba.co/feed) | 全集、中文独立博客、中文 |
| [Spring](https://spring.io) | Personal Blogs 订阅源 | Personal Blogs | [RSS](https://spring.io/blog.atom) | 全集、工程 |
| [SuperGrey 的筆記本](https://blog.supergrey.uk) | 主要写阅读随笔、动漫影评。 | Personal Blogs | [RSS](https://supergrey.bearblog.dev/rss/) | 全集、中文独立博客、中文 |
| [tplate](https://trle5.xyz) | 主要写综合、杂谈、教程。 | Personal Blogs | [RSS](https://trle5.xyz/atom.xml) | 全集、中文独立博客、中文 |
| [whyes 的博客](http://whyes.org/) | 主要写医学、科研、临床研究、硬件。 | Personal Blogs | [RSS](https://whyes.org/feed.xml) | 全集、中文独立博客、中文 |
| [WSH](https://www.wsh233.cn) | 主要写生活、随笔、GISer、地信。 | Personal Blogs | [RSS](https://www.wsh233.cn/feed.xml) | 全集、中文独立博客、中文 |
| [Wulu's Blog](https://wulu.zone/posts/) | 主要写笔记、经验分享、学习、教育。 | Personal Blogs | [RSS](https://wulu.zone/feed/post.xml) | 全集、中文独立博客、中文 |
| [一派胡言 · Blog](https://yipai.me/blog) | 主要写胡一派、随笔、不折腾。 | Personal Blogs | [RSS](https://yipai.me/feed) | 全集、中文独立博客、中文 |
| [不吐不快](https://mianao.info/atom.xml) | 主要写生活、硬件、教程、DIY。 | Personal Blogs | [RSS](https://mianao.info/atom.xml) | 全集、中文独立博客、中文 |
| [专享生活](https://zhjwork.online) | 主要写专利、科技、随笔、法律。 | Personal Blogs | [RSS](https://zhjwork.online/feed) | 全集、中文独立博客、中文 |
| [云心怀鹤](https://bluehe.cn/) | 主要写生活、生活方式、风光摄影、科技。 | Personal Blogs | [RSS](https://bluehe.cn/feed/) | 全集、中文独立博客、中文 |
| [卢昌海个人主页](http://www.changhai.org) | 主要写物理、科普。 | Personal Blogs | [RSS](https://www.changhai.org/feed.xml) | 全集、中文独立博客、中文 |
| [印记](https://yinji.org/) | 主要写生活、随笔。 | Personal Blogs | [RSS](https://yinji.org/feed) | 全集、中文独立博客、中文 |
| [双绞麻痹](https://numb.tech/atom.xml) | 主要写随笔。 | Personal Blogs | [RSS](https://numb.tech/atom.xml) | 全集、中文独立博客、中文 |
| [叶寻的博客](https://cyrusyip.org/zh-cn/) | 主要写生活、学习。 | Personal Blogs | [RSS](https://cyrusyip.org/zh-cn/index.xml) | 全集、中文独立博客、中文 |
| [叶泯希](https://blog.418121.xyz/) | 主要写生活、摄影、教程。 | Personal Blogs | [RSS](https://blog.418121.xyz/rss2.xml) | 全集、中文独立博客、中文 |
| [同和故事匯](https://hocassian.cn/) | 主要写編程、隨筆、Galgame、雜談。 | Personal Blogs | [RSS](https://hocassian.cn/feed/) | 全集、中文独立博客、中文 |
| [四喜丸子](https://fourhappylions.com/) | 主要写养娃、家庭、海外生活。 | Personal Blogs | [RSS](https://fourhappylions.com/index.xml) | 全集、中文独立博客、中文 |
| [如鱼饮水](https://wangjiezhe.com/atom.xml) | 主要写数学、随笔。 | Personal Blogs | [RSS](https://wangjiezhe.com/atom.xml) | 全集、中文独立博客、中文 |
| [小陶持续精进](https://whyya.xyz/) | 主要写生活、生产力工具、效率、知识管理。 | Personal Blogs | [RSS](https://whyya.xyz/rss.xml) | 全集、中文独立博客、中文 |
| [局域自由博客](https://localfreedom.pages.dev/) | 主要写软件、隐私、笔记、本地化。 | Personal Blogs | [RSS](https://localfreedom.pages.dev/index.xml) | 全集、中文独立博客、中文 |
| [廊桥遗梦](https://blog.moran.im/) | 主要写随笔、生活、教程。 | Personal Blogs | [RSS](https://blog.moran.im/rss.xml) | 全集、中文独立博客、中文 |
| [懋和道人](https://blog.dao.js.cn) | 主要写李至臣、李懋和、南通道士、风水。 | Personal Blogs | [RSS](https://blog.dao.js.cn/atom.xml) | 全集、中文独立博客、中文 |
| [明天的乌云](https://blog.xlab.app/atom.xml) | 主要写安全、思考。 | Personal Blogs | [RSS](https://blog.xlab.app/atom.xml) | 全集、中文独立博客、中文 |
| [木鸟杂记](https://www.qtmuniao.com) | 主要写分布式系统、存储、boltdb、源码阅读。 | Personal Blogs | [RSS](https://www.qtmuniao.com/atom.xml) | 全集、中文独立博客、中文 |
| [林林杂语](https://www.xiaozonglin.cn/) | 主要写生活、随笔。 | Personal Blogs | [RSS](https://www.xiaozonglin.cn/feed/) | 全集、中文独立博客、中文 |
| [柴郡猫](https://www.cheshirex.com) | 主要写生活、分享、记录。 | Personal Blogs | [RSS](https://www.cheshirex.com/feed) | 全集、中文独立博客、中文 |
| [梅之夏](https://blog.mcenahle.page/) | 主要写随笔、记录、成长、学习。 | Personal Blogs | [RSS](https://blog.mcenahle.page/feed.xml) | 全集、中文独立博客、中文 |
| [涵哲子居](https://iluc.cn/) | 主要写日常、随笔、乱七八糟。 | Personal Blogs | [RSS](https://iluc.cn/rss.xml) | 全集、中文独立博客、中文 |
| [爱范儿](https://www.ifanr.com?utm_source=rss&utm_medium=rss&utm_campaign=) | Personal Blogs 订阅源 | Personal Blogs | [RSS](https://www.ifanr.com/feed) | 全集、中文、新闻 |
| [玉明-风起于青萍之末](https://xdym11235.com/) | 主要写信息安全。 | Personal Blogs | [RSS](https://xdym11235.com/feed) | 全集、中文独立博客、中文 |
| [祝融说。](https://zhurongshuo.com/) | 主要写法不净空，觉无性也。。 | Personal Blogs | [RSS](https://zhurongshuo.com/index.xml) | 全集、中文独立博客、中文 |
| [纸短情长](https://www.gtdstudy.com/) | 主要写阅读、思考。 | Personal Blogs | [RSS](http://yibie.github.io/index.xml) | 全集、中文独立博客、中文 |
| [讀角獸](https://ducorn.com) | 主要写投資、健康、判斷。 | Personal Blogs | [RSS](https://ducorn.com/feed.xml) | 全集、中文独立博客、中文 |
| [資工小廢物 - JN](https://blog.giveanornot.com/) | 主要写來自台灣、生活反思、社群媒體負面影響、開源軟體。 | Personal Blogs | [RSS](https://blog.giveanornot.com/index.xml) | 全集、中文独立博客、中文 |
| [闲人LIFE](https://www.xianrenlife.com/) | 主要写随笔、小说、书评。 | Personal Blogs | [RSS](https://www.xianrenlife.com/feeds/posts/default) | 全集、中文独立博客、中文 |
| [陈杨树下](https://demochen.com/) | 主要写阅读与思考、效率与工具、生活与成长。 | Personal Blogs | [RSS](https://www.demochen.com/atom.xml) | 全集、中文独立博客、中文 |

</details>

<details>
<summary>Communities · 1</summary>

| 名称 | 介绍 | 主分类 | Feed | 所属合集 |
| --- | --- | --- | --- | --- |
| [V2EX](https://www.v2ex.com/) | Communities 订阅源 | Communities | [RSS](https://v2ex.com/index.xml) | 全集、中文、新闻 |

</details>

<details>
<summary>Culture & Ideas · 8</summary>

| 名称 | 介绍 | 主分类 | Feed | 所属合集 |
| --- | --- | --- | --- | --- |
| [KAIX.IN](https://kaix.in/) | 主要写读书、咖啡、随笔。 | Culture & Ideas | [RSS](https://kaix.in/feed/) | 全集、中文独立博客、中文 |
| [Maohang Gao's Blog](http://kangaroogao.com/atom.xml) | 主要写游记、读书笔记、随笔。 | Culture & Ideas | [RSS](https://kangaroogao.com/atom.xml) | 全集、中文独立博客、中文 |
| [ShineKid](https://shinekid.com) | 主要写生活、影视、文学。 | Culture & Ideas | [RSS](https://shinekid.com/feed/) | 全集、中文独立博客、中文 |
| [Tripper Press - Take Photo, Think Seriously.](https://tripper.press) | 主要写摄影、文化产业、新媒体。 | Culture & Ideas | [RSS](https://tripper.press/atom.xml) | 全集、中文独立博客、中文 |
| [东评西就](https://dongjunke.cn/) | 主要写社交媒体、科技互联网、思考、读书。 | Culture & Ideas | [RSS](https://dongjunke.cn/atom.xml) | 全集、中文独立博客、中文 |
| [叉息的空中咖啡馆](https://www.xchere.xyz/atom.xml) | 主要写生活、随笔、记录、读书笔记。 | Culture & Ideas | [RSS](https://www.xchere.xyz/atom.xml) | 全集、中文独立博客、中文 |
| [赫赫文王](https://kqh.me/) | 主要写历史、人文、艺术、日常。 | Culture & Ideas | [RSS](https://kqh.me/index.xml) | 全集、中文独立博客、中文 |
| [静风说](https://www.jfsay.com) | 主要写生活、读书、电影、旅游。 | Culture & Ideas | [RSS](http://www.jfsay.com/feed) | 全集、中文独立博客、中文 |

</details>

<details>
<summary>Videos · 93</summary>

| 名称 | 介绍 | 主分类 | Feed | 所属合集 |
| --- | --- | --- | --- | --- |
| [3Blue1Brown](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCYO_jab_esuFRV4b17AJtAw) | 全集、视频 |
| [a16z](https://www.youtube.com/channel/UC9cn0TuPq4dnbTY-CBsm8XA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC9cn0TuPq4dnbTY-CBsm8XA) | 全集、视频 |
| [Acquired](https://www.youtube.com/channel/UCyFqFYfTW2VoIQKylJ04Rtw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCyFqFYfTW2VoIQKylJ04Rtw) | 全集、视频 |
| [AI Engineer](https://www.youtube.com/channel/UCLKPca3kwwd-B59HNr-_lvA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCLKPca3kwwd-B59HNr-_lvA) | AI、全集、视频 |
| [AI Explained](https://www.youtube.com/channel/UCNJ1Ymd5yFuUPtn21xtRbbw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCNJ1Ymd5yFuUPtn21xtRbbw) | AI、全集、视频 |
| [AI Master](https://www.youtube.com/channel/UC0yHbz4OxdQFwmVX2BBQqLg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC0yHbz4OxdQFwmVX2BBQqLg) | AI、全集、视频 |
| [AI Search](https://www.youtube.com/channel/UCIgnGlGkVRhd4qNFcEwLL4A) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCIgnGlGkVRhd4qNFcEwLL4A) | AI、全集、视频 |
| [AICodeKing](https://www.youtube.com/channel/UC0m81bQuthaQZmFbXEY9QSw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC0m81bQuthaQZmFbXEY9QSw) | AI、全集、视频 |
| [Alex Kantrowitz](https://www.youtube.com/channel/UCye1YedIypHffYb8k6Gp9wg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCye1YedIypHffYb8k6Gp9wg) | 全集、视频 |
| [Ali Abdaal](https://www.youtube.com/channel/UCoOae5nYA7VqaXzerajD0lg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCoOae5nYA7VqaXzerajD0lg) | 全集、视频 |
| [All-In Podcast](https://www.youtube.com/channel/UCESLZhusAkFfsNsApnjF_Cg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCESLZhusAkFfsNsApnjF_Cg) | 全集、视频 |
| [Andrej Karpathy](https://www.youtube.com/channel/UCXUPKJO5MZQN11PqgIvyuvQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCXUPKJO5MZQN11PqgIvyuvQ) | AI、全集、视频 |
| [Andrew Huberman](https://www.youtube.com/channel/UC2D2CMWXMOVWx7giW1n3LIg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC2D2CMWXMOVWx7giW1n3LIg) | 全集、视频 |
| [Android Developers](https://www.youtube.com/channel/UCVHFbqXqoYvEWM1Ddxl0QDg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?user=androiddevelopers) | 全集、视频 |
| [AssemblyAI](https://www.youtube.com/channel/UCtatfZMf-8EkIwASXM4ts0A) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCtatfZMf-8EkIwASXM4ts0A) | AI、全集、视频 |
| [BBC Earth](https://www.youtube.com/channel/UCwmZiChSryoWQCZMIQezgTg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCwmZiChSryoWQCZMIQezgTg) | 全集、视频 |
| [Beyond Coding](https://www.youtube.com/channel/UCdMz6KKEDW_1Qqas-ya7S6w) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCdMz6KKEDW_1Qqas-ya7S6w) | 全集、视频 |
| [Bloomberg Originals](https://www.youtube.com/channel/UCUMZ7gohGI9HcU9VNsr2FJQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?user=Bloomberg) | 全集、视频 |
| [Branch Education](https://www.youtube.com/channel/UCdp4_l1vPmpN-gDbUwhaRUQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCdp4_l1vPmpN-gDbUwhaRUQ) | 全集、视频 |
| [Business Insider](https://www.youtube.com/channel/UCcyq283he07B7_KUX07mmtA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?user=businessinsider) | 全集、视频 |
| [ByteByteGo](https://www.youtube.com/channel/UCZgt6AzoyjslHTC9dz0UoTw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCZgt6AzoyjslHTC9dz0UoTw) | 全集、视频 |
| [CNET](https://www.youtube.com/channel/UCOmcA3f_RrH6b9NmcNa4tdg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?user=CNETTV) | 全集、视频 |
| [Computerphile](https://www.youtube.com/channel/UC9-y-6csu5WGm29I7JiwpnA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC9-y-6csu5WGm29I7JiwpnA) | 全集、视频 |
| [Curious Refuge](https://www.youtube.com/channel/UClnFtyUEaxQOCd1s5NKYGFA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UClnFtyUEaxQOCd1s5NKYGFA) | 全集、视频 |
| [DeepLearningAI — Video](https://www.youtube.com/channel/UCcIXc5mJsHVYTZR1maL5l9w) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCcIXc5mJsHVYTZR1maL5l9w) | AI、全集、视频 |
| [Dwarkesh Patel](https://www.youtube.com/channel/UCXl4i9dYBrFOabk0xGmbkRA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCXl4i9dYBrFOabk0xGmbkRA) | 全集、视频 |
| [Elizabeth Alli - DesignerUp](https://www.youtube.com/channel/UCw2R8kz3aotYtV9utqf0uaw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCw2R8kz3aotYtV9utqf0uaw) | 全集、视频 |
| [EO](https://www.youtube.com/channel/UClWTCPVi-AU9TeCN6FkGARg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UClWTCPVi-AU9TeCN6FkGARg) | 全集、视频 |
| [Fireship](https://www.youtube.com/channel/UCsBjURrPoezykLs9EqgamOA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCsBjURrPoezykLs9EqgamOA) | 全集、视频 |
| [freeCodeCamp.org](https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC8butISFwT-Wl7EV0hUK0BQ) | 全集、视频 |
| [Google](https://www.youtube.com/channel/UCK8sQmJBp8GCxrOtXWBpyEA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCK8sQmJBp8GCxrOtXWBpyEA) | 全集、视频 |
| [Google DeepMind](https://www.youtube.com/channel/UCP7jMXSY2xbc3KCAE0MHQ-A) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCP7jMXSY2xbc3KCAE0MHQ-A) | AI、全集、视频 |
| [Greg Isenberg](https://www.youtube.com/channel/UCPjNBjflYl0-HQtUvOx0Ibw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCPjNBjflYl0-HQtUvOx0Ibw) | 全集、视频 |
| [How I AI](https://www.youtube.com/channel/UCRYY7IEbkHLH_ScJCu9eWDQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCRYY7IEbkHLH_ScJCu9eWDQ) | AI、全集、视频 |
| [Hung-yi Lee](https://www.youtube.com/channel/UC2ggjtuuWvxrHHHiaDH1dlQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC2ggjtuuWvxrHHHiaDH1dlQ) | AI、全集、视频 |
| [Hussein Nasser](https://www.youtube.com/channel/UC_ML5xP23TOWKUcc-oAE_Eg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC_ML5xP23TOWKUcc-oAE_Eg) | 全集、视频 |
| [Invest Like The Best](https://www.youtube.com/channel/UCpQBb0fToph3jrDulwz1iUQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCpQBb0fToph3jrDulwz1iUQ) | 全集、视频 |
| [Justin Sung](https://www.youtube.com/channel/UC2Zs9v2hL2qZZ7vsAENsg4w) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC2Zs9v2hL2qZZ7vsAENsg4w) | 全集、视频 |
| [Kurzgesagt – In a Nutshell](https://www.youtube.com/channel/UCsXVk37bltHxD1rDPwtNM8Q) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCsXVk37bltHxD1rDPwtNM8Q) | 全集、视频 |
| [LangChain](https://www.youtube.com/channel/UCC-lyoTfSrcJzA1ab3APAgw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCC-lyoTfSrcJzA1ab3APAgw) | AI、全集、视频 |
| [Last Week in AI — Video](https://www.youtube.com/channel/UCKARTq-t5SPMzwtft8FWwnA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCKARTq-t5SPMzwtft8FWwnA) | AI、全集、视频 |
| [leerob](https://www.youtube.com/channel/UCZMli3czZnd1uoc1ShTouQw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCZMli3czZnd1uoc1ShTouQw) | AI、全集、视频 |
| [Lenny's Podcast](https://www.youtube.com/channel/UC6t1O76G0jYXOAoYCm153dA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC6t1O76G0jYXOAoYCm153dA) | 全集、视频 |
| [Lex Fridman](https://www.youtube.com/channel/UCSHZKyawb77ixDdsGog4iWA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCSHZKyawb77ixDdsGog4iWA) | 全集、视频 |
| [Liam Ottley](https://www.youtube.com/channel/UCui4jxDaMb53Gdh-AZUTPAg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCui4jxDaMb53Gdh-AZUTPAg) | AI、全集、视频 |
| [Linus Tech Tips](https://www.youtube.com/channel/UCXuqSBlHAE6Xw-yeJA0Tunw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?user=LinusTechTips) | 全集、视频 |
| [Luma](https://www.youtube.com/channel/UC45T0I4p7A3dI0XvhivafZQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC45T0I4p7A3dI0XvhivafZQ) | 全集、视频 |
| [Machine Learning Street Talk](https://www.youtube.com/channel/UCMLtBahI5DMrt0NPvDSoIRQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCMLtBahI5DMrt0NPvDSoIRQ) | AI、全集、视频 |
| [MacRumors](https://www.youtube.com/channel/UCaFGDBmGK_jw66u3av2Ysjw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?user=macrumors) | 全集、视频 |
| [Marie Forleo](https://www.youtube.com/channel/UCuoxrRDDgk3UUnxR4tlkJYQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?user=marieforleo) | 全集、视频 |
| [Matt Wolfe](https://www.youtube.com/channel/UChpleBmo18P08aKCIgti38g) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UChpleBmo18P08aKCIgti38g) | AI、全集、视频 |
| [Matthew Berman](https://www.youtube.com/channel/UCawZsQWqfGSbCI5yjkdVkTA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCawZsQWqfGSbCI5yjkdVkTA) | AI、全集、视频 |
| [MrBeast](https://www.youtube.com/channel/UCX6OQ3DkcsbYNE6H8uQQuVA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCX6OQ3DkcsbYNE6H8uQQuVA) | 全集、视频 |
| [mrblock 區塊先生](https://www.youtube.com/channel/UCN2hSM8fBcvZBa8OOKc24eg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCN2hSM8fBcvZBa8OOKc24eg) | 全集、中文、视频 |
| [Nature on PBS](https://www.youtube.com/channel/UCcBp_9YPyma4c3HTadmRJ3Q) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCcBp_9YPyma4c3HTadmRJ3Q) | 全集、视频 |
| [nature video](https://www.youtube.com/channel/UC7c8mE90qCtu11z47U0KErg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC7c8mE90qCtu11z47U0KErg) | 全集、视频 |
| [Naval](https://www.youtube.com/channel/UCh_dVD10YuSghle8g6yjePg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCh_dVD10YuSghle8g6yjePg) | 全集、视频 |
| [Nick Saraev](https://www.youtube.com/channel/UCbo-KbSjJDG6JWQ_MTZ_rNA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCbo-KbSjJDG6JWQ_MTZ_rNA) | AI、全集、视频 |
| [Nikhil Kamath](https://www.youtube.com/channel/UCnC8SAZzQiBGYVSKZ_S3y4Q) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCnC8SAZzQiBGYVSKZ_S3y4Q) | 全集、视频 |
| [NNgroup](https://www.youtube.com/channel/UC2oCugzU6W8-h95W7eBTUEg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC2oCugzU6W8-h95W7eBTUEg) | 全集、视频 |
| [No Priors: AI, Machine Learning, Tech, & Startups](https://www.youtube.com/channel/UCSI7h9hydQ40K5MJHnCrQvw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCSI7h9hydQ40K5MJHnCrQvw) | AI、全集、视频 |
| [OpenAI](https://www.youtube.com/channel/UCXZCJLdBC09xxGZ6gcdrc6A) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCXZCJLdBC09xxGZ6gcdrc6A) | AI、全集、视频 |
| [Patrick Boyle](https://www.youtube.com/channel/UCASM0cgfkJxQ1ICmRilfHLw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCASM0cgfkJxQ1ICmRilfHLw) | 全集、视频 |
| [Pika Labs](https://www.youtube.com/channel/UC0SclYU4iiQRihtmDnak-gQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC0SclYU4iiQRihtmDnak-gQ) | AI、全集、视频 |
| [PowerfulJRE](https://www.youtube.com/channel/UCzQUP1qoWDoEbmsQxvdjxgQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCzQUP1qoWDoEbmsQxvdjxgQ) | 全集、视频 |
| [Product School](https://www.youtube.com/channel/UC6hlQ0x6kPbAGjYkoz53cvA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC6hlQ0x6kPbAGjYkoz53cvA) | 全集、视频 |
| [Real Engineering](https://www.youtube.com/channel/UCR1IuLEqb6UEA_zQ81kwXfg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCR1IuLEqb6UEA_zQ81kwXfg) | 全集、视频 |
| [Riley Brown](https://www.youtube.com/channel/UCMcoud_ZW7cfxeIugBflSBw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCMcoud_ZW7cfxeIugBflSBw) | AI、全集、视频 |
| [Runway](https://www.youtube.com/channel/UCUBqu_z5uP0AZhYtuyFZB3g) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCUBqu_z5uP0AZhYtuyFZB3g) | AI、全集、视频 |
| [Ryan Peterman](https://www.youtube.com/channel/UCzB7YGrrxDC_POenf86H3_Q) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCzB7YGrrxDC_POenf86H3_Q) | 全集、视频 |
| [Sabin Civil Engineering](https://www.youtube.com/channel/UCqZQJ4600a9wIfMPbYc60OQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCqZQJ4600a9wIfMPbYc60OQ) | 全集、视频 |
| [Sequoia Capital](https://www.youtube.com/channel/UCWrF0oN6unbXrWsTN7RctTw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCWrF0oN6unbXrWsTN7RctTw) | 全集、视频 |
| [Silicon Valley Girl](https://www.youtube.com/channel/UCiq1FIgtEK7LRAOB1JXTPig) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCiq1FIgtEK7LRAOB1JXTPig) | 全集、视频 |
| [SpaceX](https://www.youtube.com/channel/UCtI0Hodo5o5dUb67FeUjDeA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?user=spacexchannel) | 全集、视频 |
| [Spring I/O](https://www.youtube.com/channel/UCLMPXsvSrhNPN3i9h-u8PYg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCLMPXsvSrhNPN3i9h-u8PYg) | 全集、视频 |
| [StatQuest with Josh Starmer](https://www.youtube.com/channel/UCtYLUTtgS3k1Fg4y5tAhLbw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCtYLUTtgS3k1Fg4y5tAhLbw) | 全集、视频 |
| [Tao Prompts](https://www.youtube.com/channel/UCc1qMq2UBJD9cSKbeBwGoZQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCc1qMq2UBJD9cSKbeBwGoZQ) | AI、全集、视频 |
| [TED](https://www.youtube.com/channel/UCAuUUnT6oDeKwE6v1NGQxug) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCAuUUnT6oDeKwE6v1NGQxug) | 全集、视频 |
| [The AI Advantage](https://www.youtube.com/channel/UCHhYXsLBEVVnbvsq57n1MTQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCHhYXsLBEVVnbvsq57n1MTQ) | AI、全集、视频 |
| [The Futur](https://www.youtube.com/channel/UC-b3c7kxa5vU-bnmaROgvog) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC-b3c7kxa5vU-bnmaROgvog) | 全集、视频 |
| [The Knowledge Project Podcast](https://www.youtube.com/channel/UCLtTf_uKt0Itd0NG7txrwXA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCLtTf_uKt0Itd0NG7txrwXA) | 全集、视频 |
| [The Pragmatic Engineer](https://www.youtube.com/channel/UCPbwhExawYrn9xxI21TFfyw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCPbwhExawYrn9xxI21TFfyw) | 全集、视频 |
| [The Verge — Video](https://www.youtube.com/channel/UCddiUEpeqJcYeBxX1IVBKvQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?user=TheVerge) | 全集、视频 |
| [Tina Huang](https://www.youtube.com/channel/UC2UXDak6o7rBm23k3Vv5dww) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC2UXDak6o7rBm23k3Vv5dww) | AI、全集、视频 |
| [Traversy Media](https://www.youtube.com/channel/UC29ju8bIPH5as8OGnQzwJyA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC29ju8bIPH5as8OGnQzwJyA) | 全集、视频 |
| [Web Dev Simplified](https://www.youtube.com/channel/UCFbNIlppjAuEX4znoulh0Cw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCFbNIlppjAuEX4znoulh0Cw) | 全集、视频 |
| [Wes Roth](https://www.youtube.com/channel/UCqcbQf6yw5KzRoDDcZ_wBSw) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCqcbQf6yw5KzRoDDcZ_wBSw) | AI、全集、视频 |
| [Y Combinator](https://www.youtube.com/channel/UCcefcZRL2oaA_uBNeo5UOWg) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCcefcZRL2oaA_uBNeo5UOWg) | 全集、视频 |
| [Yannic Kilcher](https://www.youtube.com/channel/UCZHmQk67mSJgfCCTn7xBfew) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCZHmQk67mSJgfCCTn7xBfew) | AI、全集、视频 |
| [yobi321](https://www.youtube.com/channel/UCB_DbqNN9w30tnyWJSrIwyA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCB_DbqNN9w30tnyWJSrIwyA) | 全集、视频 |
| [一席YiXi](https://www.youtube.com/channel/UCKFB_rVEFEF3l-onQGvGx1A) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCKFB_rVEFEF3l-onQGvGx1A) | 全集、中文、视频 |
| [一条Yit](https://www.youtube.com/channel/UCulFhrW_YCwkq_BP16C82mA) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCulFhrW_YCwkq_BP16C82mA) | 全集、中文、视频 |
| [李永乐老师](https://www.youtube.com/channel/UCvNxfitQbWkmLuCd44UfrYQ) | 视频频道 | Videos | [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCvNxfitQbWkmLuCd44UfrYQ) | 全集、中文、视频 |

</details>

<details>
<summary>Podcasts · 73</summary>

| 名称 | 介绍 | 主分类 | Feed | 所属合集 |
| --- | --- | --- | --- | --- |
| [30 for 30 Podcasts](http://espnradio.espn.com/espnradio/index) | 播客节目 | Podcasts | [RSS](https://feeds.megaphone.fm/ESP5765452710) | 全集、播客 |
| [42章经 — Podcast](https://www.xiaoyuzhoufm.com/podcast/648b0b641c48983391a63f98) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/648b0b641c48983391a63f98) | 全集、中文、播客 |
| [AI炼金术 — Podcast](https://www.xiaoyuzhoufm.com/podcast/63e9ef4de99bdef7d39944c8) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/63e9ef4de99bdef7d39944c8) | AI、全集、中文、播客 |
| [Darknet Diaries](https://darknetdiaries.com/) | 播客节目 | Podcasts | [RSS](https://feeds.megaphone.fm/darknetdiaries) | 全集、播客 |
| [Discovery](http://www.bbc.co.uk/programmes/p002w557) | 播客节目 | Podcasts | [RSS](https://podcasts.files.bbci.co.uk/p002w557.rss) | 全集、播客 |
| [Fragmented - AI Developer Podcast](https://fragmentedpodcast.com/) | 播客节目 | Podcasts | [RSS](https://feeds.simplecast.com/LpAGSLnY) | AI、全集、播客 |
| [Gastropod](https://gastropod.com/) | 播客节目 | Podcasts | [RSS](https://www.omnycontent.com/d/playlist/aaea4e69-af51-495e-afc9-a9760146922b/2a195077-f014-41d2-8313-ab190186b4c2/277bcd5c-0a05-4c14-8ba6-ab190186b4d5/podcast.rss) | 全集、播客 |
| [Hacking Humans](https://thecyberwire.com/podcasts/hacking-humans) | 播客节目 | Podcasts | [RSS](https://feeds.megaphone.fm/hacking-humans) | 全集、播客 |
| [Hanselminutes with Scott Hanselman](https://www.hanselminutes.com) | 播客节目 | Podcasts | [RSS](https://feeds.simplecast.com/gvtxUiIf) | 全集、播客 |
| [Invest Like the Best with Patrick O'Shaughnessy](https://colossus.com/) | 播客节目 | Podcasts | [RSS](https://investlikethebest.libsyn.com/rss) | 全集、播客 |
| [Invisibilia](https://www.npr.org/podcasts/510307/invisibilia) | 播客节目 | Podcasts | [RSS](https://feeds.npr.org/510307/podcast.xml) | 全集、播客 |
| [Planet Money](https://www.npr.org/podcasts/510289/planet-money) | 播客节目 | Podcasts | [RSS](https://feeds.npr.org/510289/podcast.xml) | 全集、播客 |
| [Reply All](http://gimletmedia.com/shows/reply-all) | 播客节目 | Podcasts | [RSS](https://feeds.megaphone.fm/replyall) | 全集、播客 |
| [The Cynical Developer](https://cynical.dev/) | 播客节目 | Podcasts | [RSS](https://cynicaldeveloper.com/feed/podcast) | 全集、播客 |
| [The Startup Junkies Podcast](https://www.startupjunkie.org/podcast) | 播客节目 | Podcasts | [RSS](https://startupjunkie.libsyn.com/rss) | 全集、播客 |
| [The Vergecast](https://www.theverge.com/the-vergecast) | 播客节目 | Podcasts | [RSS](https://feeds.megaphone.fm/vergecast) | 全集、播客 |
| [Throughline](https://www.npr.org/podcasts/510333/throughline) | 播客节目 | Podcasts | [RSS](https://feeds.npr.org/510333/podcast.xml) | 全集、播客 |
| [TIANYU2FM — 对谈未知领域](https://www.xiaoyuzhoufm.com/podcast/5f22729f9504bbdb77253e46) | 播客节目 | Podcasts | [RSS](https://rsshub.xiaowuaiblog.com/xiaoyuzhou/podcast/5f22729f9504bbdb77253e46) | 全集、中文、播客 |
| [What's Next｜科技早知道](https://www.xiaoyuzhoufm.com/podcast/5e74b52c418a84a046ecaceb) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e74b52c418a84a046ecaceb) | 全集、中文、播客 |
| [一席](https://www.xiaoyuzhoufm.com/podcast/5e285326418a84a04627343f) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e285326418a84a04627343f) | 全集、中文、播客 |
| [三五环](https://www.xiaoyuzhoufm.com/podcast/5e280fab418a84a0461faa3c) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e280fab418a84a0461faa3c) | 全集、中文、播客 |
| [不合时宜](https://www.xiaoyuzhoufm.com/podcast/5e280fb8418a84a0461fd076) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e280fb8418a84a0461fd076) | 全集、中文、播客 |
| [东亚观察局](https://www.xiaoyuzhoufm.com/podcast/5e9a4e25418a84a046bc6156) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e9a4e25418a84a046bc6156) | 全集、中文、播客 |
| [东腔西调](https://www.xiaoyuzhoufm.com/podcast/5f72b66083c34e85dd14fde9) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5f72b66083c34e85dd14fde9) | 全集、中文、播客 |
| [乱翻书](https://www.xiaoyuzhoufm.com/podcast/61358d971c5d56efe5bcb5d2) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/61358d971c5d56efe5bcb5d2) | 全集、中文、播客 |
| [人民公园说AI](https://www.xiaoyuzhoufm.com/podcast/65257ff6e8ce9deaf70a65e9) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/65257ff6e8ce9deaf70a65e9) | AI、全集、中文、播客 |
| [保持偏见](https://www.xiaoyuzhoufm.com/podcast/663e3c95af1e22bb157dcee3) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/663e3c95af1e22bb157dcee3) | 全集、中文、播客 |
| [信号与噪声](https://www.xiaoyuzhoufm.com/podcast/6819d5a7e37664602a344e0e) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/6819d5a7e37664602a344e0e) | AI、全集、中文、播客 |
| [凹凸电波](https://www.xiaoyuzhoufm.com/podcast/5e2839ca418a84a0462431b7) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e2839ca418a84a0462431b7) | 全集、中文、播客 |
| [十字路口Crossing — Podcast](https://www.xiaoyuzhoufm.com/podcast/60502e253c92d4f62c2a9577) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/60502e253c92d4f62c2a9577) | AI、全集、中文、播客 |
| [半拿铁 \| 商业沉浮录](https://www.xiaoyuzhoufm.com/podcast/62382c1103bea1ebfffa1c00) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/62382c1103bea1ebfffa1c00) | 全集、中文、播客 |
| [卫诗婕｜漫谈Light the Star](https://www.xiaoyuzhoufm.com/podcast/6627fda4b56459544087d86a) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/6627fda4b56459544087d86a) | 全集、中文、播客 |
| [商业就是这样](https://www.xiaoyuzhoufm.com/podcast/6022a180ef5fdaddc30bb101) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/6022a180ef5fdaddc30bb101) | 全集、中文、播客 |
| [声东击西](https://www.xiaoyuzhoufm.com/podcast/5e2831ed418a84a046231c00) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e2831ed418a84a046231c00) | 全集、中文、播客 |
| [声动早咖啡](https://www.xiaoyuzhoufm.com/podcast/60de7c003dd577b40d5a40f3) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/60de7c003dd577b40d5a40f3) | 全集、中文、播客 |
| [天真不天真](https://www.xiaoyuzhoufm.com/podcast/65cef9e3cace72dff8d98de3) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/65cef9e3cace72dff8d98de3) | 全集、中文、播客 |
| [屠龙之术](https://www.xiaoyuzhoufm.com/podcast/6507bc165c88d2412626b401) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/6507bc165c88d2412626b401) | 全集、中文、播客 |
| [岩中花述](https://www.xiaoyuzhoufm.com/podcast/625635587bfca4e73e990703) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/625635587bfca4e73e990703) | 全集、中文、播客 |
| [开始连接 LinkStart](https://www.xiaoyuzhoufm.com/podcast/63ff0da51b1faf8a0b70b337) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/63ff0da51b1faf8a0b70b337) | 全集、中文、播客 |
| [张小珺Jùn｜商业访谈录](https://www.xiaoyuzhoufm.com/podcast/626b46ea9cbbf0451cf5a962) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/626b46ea9cbbf0451cf5a962) | 全集、中文、播客 |
| [忽左忽右](https://www.xiaoyuzhoufm.com/podcast/5e4ee557418a84a0466737b7) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e4ee557418a84a0466737b7) | 全集、中文、播客 |
| [慢速生长](https://www.xiaoyuzhoufm.com/podcast/668d00c38fcadceb90158ac1) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/668d00c38fcadceb90158ac1) | 全集、中文、播客 |
| [捕蛇者说](https://www.xiaoyuzhoufm.com/podcast/5e2864f7418a84a04628f2da) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e2864f7418a84a04628f2da) | 全集、中文、播客 |
| [搞钱女孩](https://www.xiaoyuzhoufm.com/podcast/63d945ece725b5378a158d29) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/63d945ece725b5378a158d29) | 全集、中文、播客 |
| [文化有限](https://www.xiaoyuzhoufm.com/podcast/5e4515bd418a84a046e2b11a) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e4515bd418a84a046e2b11a) | 全集、中文、播客 |
| [晚点聊 LateTalk](https://www.xiaoyuzhoufm.com/podcast/61933ace1b4320461e91fd55) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/61933ace1b4320461e91fd55) | 全集、中文、播客 |
| [李诞](https://www.xiaoyuzhoufm.com/podcast/65bb55f6513a776b57dedb32) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/65bb55f6513a776b57dedb32) | 全集、中文、播客 |
| [枫言枫语 — Podcast](https://www.xiaoyuzhoufm.com/podcast/5e2864f5418a84a04628e249) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e2864f5418a84a04628e249) | 全集、中文、播客 |
| [此话当真](https://www.xiaoyuzhoufm.com/podcast/646f194853a5e5ea1408d97c) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/646f194853a5e5ea1408d97c) | 全集、中文、播客 |
| [游荡集](https://www.xiaoyuzhoufm.com/podcast/6163ca67c8c1d14e83366b31) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/6163ca67c8c1d14e83366b31) | 全集、中文、播客 |
| [牛油果烤面包](https://www.xiaoyuzhoufm.com/podcast/5e7c8b2b418a84a046e3ecbc) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e7c8b2b418a84a046e3ecbc) | 全集、中文、播客 |
| [独树不成林](https://www.xiaoyuzhoufm.com/podcast/64acd33c7a3d479103fbd32d) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/64acd33c7a3d479103fbd32d) | 全集、中文、播客 |
| [疯投圈](https://www.xiaoyuzhoufm.com/podcast/5e280faf418a84a0461fbd39) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e280faf418a84a0461fbd39) | 全集、中文、播客 |
| [皮蛋漫游记](https://www.xiaoyuzhoufm.com/podcast/6281264ad22bcf3950c80b56) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/6281264ad22bcf3950c80b56) | 全集、中文、播客 |
| [看理想圆桌](https://www.xiaoyuzhoufm.com/podcast/5e4ff4c7418a84a046977618) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e4ff4c7418a84a046977618) | 全集、中文、播客 |
| [知行小酒馆](https://www.xiaoyuzhoufm.com/podcast/6013f9f58e2f7ee375cf4216) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/6013f9f58e2f7ee375cf4216) | 全集、中文、播客 |
| [硅谷101 — Podcast](https://www.xiaoyuzhoufm.com/podcast/5e5c52c9418a84a04625e6cc) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e5c52c9418a84a04625e6cc) | 全集、中文、播客 |
| [硬地骇客](https://www.xiaoyuzhoufm.com/podcast/640ee2438be5d40013fe4a87) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/640ee2438be5d40013fe4a87) | 全集、中文、播客 |
| [科技乱炖](https://www.xiaoyuzhoufm.com/podcast/5e4243cd418a84a0469573fb) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e4243cd418a84a0469573fb) | 全集、中文、播客 |
| [第一财经](https://www.xiaoyuzhoufm.com/podcast/64c75555e8176c3ff81de98c) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/64c75555e8176c3ff81de98c) | 全集、中文、播客 |
| [纵横四海](https://www.xiaoyuzhoufm.com/podcast/62694abdb221dd5908417d1e) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/62694abdb221dd5908417d1e) | 全集、中文、播客 |
| [罗永浩的十字路口](https://www.xiaoyuzhoufm.com/podcast/68981df29e7bcd326eb91d88) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/68981df29e7bcd326eb91d88) | 全集、中文、播客 |
| [肥话连篇](https://www.xiaoyuzhoufm.com/podcast/61d50d72ee197a3aac3dac42) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/61d50d72ee197a3aac3dac42) | 全集、中文、播客 |
| [自习室 STUDY ROOM](https://www.xiaoyuzhoufm.com/podcast/65a5fb7540d4ef949c0140ac) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/65a5fb7540d4ef949c0140ac) | 全集、中文、播客 |
| [自我进化论](https://www.xiaoyuzhoufm.com/podcast/5e5de5cb418a84a0467beb90) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e5de5cb418a84a0467beb90) | 全集、中文、播客 |
| [蒋方舟·一寸](https://www.xiaoyuzhoufm.com/podcast/67c7eeb07ac3e30992e75a2f) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/67c7eeb07ac3e30992e75a2f) | 全集、中文、播客 |
| [诗梳风](https://www.xiaoyuzhoufm.com/podcast/696496f4db4738160d5fabde) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/696496f4db4738160d5fabde) | 全集、中文、播客 |
| [谭立人](https://www.xiaoyuzhoufm.com/podcast/65a2d0f07242f9fc1c1df60a) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/65a2d0f07242f9fc1c1df60a) | 全集、中文、播客 |
| [起朱楼宴宾客](https://www.xiaoyuzhoufm.com/podcast/61dd99a47b29652ff572257b) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/61dd99a47b29652ff572257b) | 全集、中文、播客 |
| [跨国串门儿计划](https://www.xiaoyuzhoufm.com/podcast/670f3da40d2f24f28978736f) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/670f3da40d2f24f28978736f) | AI、全集、中文、播客 |
| [随机波动StochasticVolatility](https://www.xiaoyuzhoufm.com/podcast/5e7cc741418a84a046b0c2bd) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/5e7cc741418a84a046b0c2bd) | 全集、中文、播客 |
| [面基](https://www.xiaoyuzhoufm.com/podcast/6388760f22567e8ea6ad070f) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/6388760f22567e8ea6ad070f) | 全集、中文、播客 |
| [高能量](https://www.xiaoyuzhoufm.com/podcast/62c6ae08c4eaa82b112b9c84) | 播客节目 | Podcasts | [RSS](https://rsshub.bestblogs.dev/xiaoyuzhou/podcast/62c6ae08c4eaa82b112b9c84) | 全集、中文、播客 |

</details>

<!-- SOURCE_APPENDIX_END -->
