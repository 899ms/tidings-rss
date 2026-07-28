# Changelog

## v1.0.0 — 2026-07-28

Initial public release of Tidings RSS.

- Published 627 live, deduplicated feeds across nine OPML bundles.
- Added focused AI (74), News (44), Research & Science (28), Video (93), and Podcast (86) downloads that each fit within Tidings Free's 150-feed limit.
- Added broader Blogs (374), Chinese (239), Engineering (186), and Complete (627) collections.
- Validated 884 normalized candidates with the Tidings production parser; excluded 196 parser failures, 32 stale feeds, four persistent in-app import failures, and 25 canonical duplicates.
- Upgraded 67 working HTTP endpoints to independently verified HTTPS equivalents.
- Added deterministic OPML generation, SHA-256 checksums, unit tests, pull-request validation, and a weekly live health workflow.
- Added English and Simplified Chinese documentation, source/license boundaries, contribution templates, official Tidings product imagery, and a reproducible real-import screenshot.
