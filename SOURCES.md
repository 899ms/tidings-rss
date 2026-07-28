# Source catalog acknowledgements

The published catalog is a new compilation: URLs were normalized, fetched, parsed through Tidings, deduplicated, and independently regrouped. Titles and website links prefer the live feed's own metadata. Upstream descriptions and category layouts are not copied.

Discovery inputs checked on 2026-07-28:

| Input | How it was used | License / boundary |
| --- | --- | --- |
| [BestBlogs](https://github.com/ginobefun/BestBlogs) | Discovery candidates from its public article, podcast, and YouTube OPML exports | The repository does not declare a catalog-wide license. We use public endpoint URLs as discovery facts, re-fetch live metadata, and do not copy its descriptions or taxonomy. |
| [awesome-rss-feeds](https://github.com/plenaryapp/awesome-rss-feeds) | Discovery candidates from relevant technology, news, and science collections | [CC0-1.0](https://github.com/plenaryapp/awesome-rss-feeds/blob/master/LICENSE) |
| [awesome-rsshub-routes](https://github.com/JackyST0/awesome-rsshub-routes) | Discovery candidates, especially Chinese technology routes | [CC0-1.0](https://github.com/JackyST0/awesome-rsshub-routes/blob/main/LICENSE) |
| Tidings AI Radar OPML | Existing personal collection supplied by the project maintainer | URLs were independently revalidated and reclassified. |
| Publisher-owned feeds | A small set of official news and research endpoints | Public endpoints only; no article content is redistributed. |

## Validation boundary

A feed was included only when the Tidings production parser successfully parsed it and returned at least one item on 2026-07-28. Dated feeds whose newest returned item was more than two years old were excluded. The news bundle is stricter: it only includes sources whose newest returned item was no more than 21 days old. Persistent failures found during the isolated in-app News and Research OPML import were removed from every bundle before release.

This is a dated health check, not a promise of permanent uptime. Publishers can move or retire feeds, and third-party RSSHub or WeChat bridges can fail independently. The weekly workflow provides a fresh machine-readable health report without silently rewriting the curated catalog.
