# Contributing

[简体中文](CONTRIBUTING.zh-CN.md)

Thank you for helping people discover feeds worth following. A useful contribution is small, verifiable, and respectful of publishers.

## Suggest a feed

Open a **Feed suggestion** issue or edit `data/feeds.json` in a pull request. Include:

- a public RSS, Atom, or JSON Feed URL;
- the publisher's website;
- the most appropriate category and bundle;
- a short, concrete reason the source is useful;
- evidence that the endpoint currently parses and contains at least one item.

We favor original reporting, first-party research, practitioner writing, official project blogs, and channels with a clear editorial identity. Scraped mirrors, credentialed feeds, spam, SEO farms, copied content, and sources that primarily promote affiliate links are not accepted.

Chinese independent blogs must have published within the last 180 days, return at least two reliably dated articles, and pass repeated Tidings parser checks. `tidings-blogs.opml` is capped at 400 feeds and the complete collection stays below 700; once a cap is reached, a new source must displace a weaker one.

WeChat feeds must respond quickly, expose recent articles, and parse through Tidings. For company technology feeds, include the organization and technical direction. Only one feed is kept for each organization/direction pair, and an official website RSS feed takes priority over a matching WeChat bridge.

## Update the generated files

Python 3.10 or newer is sufficient; the project has no runtime dependencies.

```bash
python scripts/catalog.py generate
python scripts/catalog.py check
python -m unittest discover -s tests -v
```

Never edit files under `opml/` or `reports/catalog-summary.md` by hand. They are deterministic outputs of `data/feeds.json`.

## Removing or correcting a feed

Removal PRs are welcome when a feed is permanently unavailable, hijacked, paywalled at the feed endpoint, empty, or no longer represents the listed publisher. A temporary timeout alone is not enough; include repeatable evidence and the date checked.

## Rights and privacy

This repository catalogs public endpoints. It does not republish article bodies. By contributing original catalog metadata, you agree to release that contribution under CC0-1.0. Feed content and publisher names remain the property of their respective owners.
