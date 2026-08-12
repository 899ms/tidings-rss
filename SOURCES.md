# Source catalog acknowledgements

The published catalog is a new compilation: URLs were normalized, fetched, parsed through Tidings, deduplicated, and independently regrouped. Titles and website links prefer the live feed's own metadata. Upstream descriptions and category layouts are not copied.

Discovery inputs checked on 2026-07-28 and 2026-08-12:

| Input | How it was used | License / boundary |
| --- | --- | --- |
| [chinese-independent-blogs](https://github.com/timqian/chinese-independent-blogs) | Primary discovery input for the Chinese independent blog bundle; 1,331 listed feeds were independently parsed and ranked, and its tags were used to generate short topic summaries | [MIT](https://github.com/timqian/chinese-independent-blogs/blob/master/LICENSE). We preserve attribution and license notice, but independently fetch titles, dates, availability, and classification. |
| [BestBlogs](https://github.com/ginobefun/BestBlogs) | Discovery candidates from its public article, podcast, and YouTube OPML exports | The repository does not declare a catalog-wide license. We use public endpoint URLs as discovery facts, re-fetch live metadata, and do not copy its descriptions or taxonomy. |
| [awesome-rss-feeds](https://github.com/plenaryapp/awesome-rss-feeds) | Discovery candidates from relevant technology, news, and science collections | [CC0-1.0](https://github.com/plenaryapp/awesome-rss-feeds/blob/master/LICENSE) |
| [awesome-rsshub-routes](https://github.com/JackyST0/awesome-rsshub-routes) | Discovery candidates, especially Chinese technology routes | [CC0-1.0](https://github.com/JackyST0/awesome-rsshub-routes/blob/main/LICENSE) |
| [Wechat2RSS](https://github.com/ttttmr/Wechat2RSS) | Discovery candidates for the WeChat bundle; selected feeds were independently checked for responsiveness, recent articles, and Tidings compatibility | The repository has no root LICENSE and its package metadata says ISC. We link to the project and public endpoints without copying article content or claiming a license for its directory. |
| [RSSHub](https://github.com/DIYgod/RSSHub) | Feed routes for publishers that do not expose a first-party endpoint | [MIT](https://github.com/DIYgod/RSSHub/blob/master/LICENSE) |
| Tidings AI Radar OPML | Existing personal collection supplied by the project maintainer | URLs were independently revalidated and reclassified. |
| Publisher-owned feeds | A small set of official news and research endpoints | Public endpoints only; no article content is redistributed. |

## Validation boundary

The 2026-08-12 Chinese-blog review required three successful Tidings parser rounds, at least two trustworthy article dates, and a newest article no older than 180 days among the final selection. Ranking also considered activity in the last 30, 90, and 180 days, first-party hosting, feed text length, duplicate websites, and commercial or SEO signals. Existing non-blog catalog feeds had to pass two current parser rounds before they were merged. Candidate-level evidence is published in `reports/chinese-blog-curation.json`.

WeChat additions had to begin an HTTP 200 XML response within two seconds in two separate probes, then complete a Tidings parse and expose a dated article from the last 180 days. The two-second limit applies to connection and first response bytes, not full download: public WeChat XML files can be several megabytes. Candidate-level results are published in `reports/wechat-curation.json`.

The company-technology bundle is keyed by organization and technical direction. A first-party website feed wins over a WeChat bridge for the same pair; separate directions such as engineering, AI, security, and research may coexist.

This is a dated health check, not a promise of permanent uptime. Publishers can move or retire feeds, and third-party RSSHub or WeChat bridges can fail independently. The weekly workflow provides a fresh machine-readable health report without silently rewriting the curated catalog.
