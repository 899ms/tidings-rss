# Changelog

## v1.2.0 — 2026-08-12

- Added eight recently active community feeds: LINUX DO documentation, a combined Reddit technology feed, Lobsters, Python Core Development, Rust Internals, NixOS Development, the OpenAI Developer Community, and Kubernetes discussions. Every addition passed three Tidings production-parser rounds.
- Added separately downloadable WeChat and company-technology bundles, with two-second response probes, current-article checks, and organization/direction deduplication that prefers first-party website feeds.
- Rewrote both homepages around choosing, downloading, and reading the collections; moved discovery projects into a short reference section and removed internal pipeline narration from the reader path.
- Rebuilt the catalog as 707 checked feeds, including 348 Chinese independent blogs selected from 1,331 candidates.
- Required three successful Tidings parser rounds and recent, reliably dated publishing activity for the Chinese blog bundle; removed duplicate sites and promotional or SEO-oriented sources.
- Rechecked the existing catalog twice and removed repeatedly failing feeds before merging.
- Added hard limits of 400 blogs and 720 complete-collection feeds.
- Rewrote both project homepages and added a generated, tested appendix listing every source, description, Feed URL, primary category, and bundle membership.
- Published the candidate-level Chinese blog curation evidence and added a reproducible collection, scoring, and catalog-build pipeline.

## v1.1.0 — 2026-07-28

- Rebuilt the English and Chinese project story around author curation, category-by-category source highlights, and reader value.
- Moved the Tidings recommendation to the final chapter and expanded it with real import, AI Radar, AI summary, article Q&A, bilingual, video, and forum screenshots.
- Replaced the previous loading-state preview with a gated, reproducible capture of a fully fetched MIT Technology Review article with a loaded lead image and no visible fetch errors.
- Replaced the persistently slow BAIR endpoint with the current official Amazon Science feed after validating it through the Tidings production parser.
- Routed the real-import preview through GitHub Camo via a version-pinned CDN URL to avoid intermittent Raw-domain blank images while keeping the original file in the repository.

## v1.0.0 — 2026-07-28

Initial public release of Tidings RSS.

- Published 627 live, deduplicated feeds across nine OPML bundles.
- Added focused AI (74), News (44), Research & Science (28), Video (93), and Podcast (86) downloads.
- Added broader Blogs (374), Chinese (239), Engineering (186), and Complete (627) collections.
- Validated 884 normalized candidates with the Tidings production parser; excluded 196 parser failures, 32 stale feeds, four persistent in-app import failures, and 25 canonical duplicates.
- Upgraded 67 working HTTP endpoints to independently verified HTTPS equivalents.
- Added deterministic OPML generation, SHA-256 checksums, unit tests, pull-request validation, and a weekly live health workflow.
- Added English and Simplified Chinese documentation, source/license boundaries, contribution templates, official Tidings product imagery, and a reproducible real-import screenshot.
