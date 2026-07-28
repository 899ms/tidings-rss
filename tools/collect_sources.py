#!/usr/bin/env python3
"""Collect feed candidates from upstream OPML catalogs without vendoring them."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit
from xml.etree import ElementTree as ET


PLENARY_CATEGORIES = {
    "Android Development",
    "Apple",
    "Books",
    "Business & Economy",
    "Cyber security",
    "Environment",
    "History",
    "Nature",
    "News",
    "Personal finance",
    "Programming",
    "Science",
    "Space",
    "Startups",
    "Tech",
    "UI - UX",
    "Web Development",
    "iOS Development",
}


def normalize_url(value: str) -> str:
    value = value.strip()
    parsed = urlsplit(value)
    host = (parsed.hostname or "").lower()
    port = parsed.port
    if port and not ((parsed.scheme == "http" and port == 80) or (parsed.scheme == "https" and port == 443)):
        host = f"{host}:{port}"
    path = re.sub(r"/{2,}", "/", parsed.path or "/")
    if path != "/":
        path = path.rstrip("/")
    return urlunsplit((parsed.scheme.lower(), host, path, parsed.query, ""))


def iter_opml(path: Path):
    root = ET.parse(path).getroot()
    body = root.find("body")
    if body is None:
        return

    def visit(node, trail):
        url = (node.get("xmlUrl") or "").strip()
        label = (node.get("title") or node.get("text") or "").strip()
        if url:
            yield {
                "title_hint": label,
                "feed_url": url,
                "site_url_hint": (node.get("htmlUrl") or "").strip(),
                "category_hints": trail,
            }
            return
        next_trail = [*trail, label] if label else trail
        for child in node.findall("outline"):
            yield from visit(child, next_trail)

    for child in body.findall("outline"):
        yield from visit(child, [])


def add_file(store, path: Path, source: str, kind: str, category_prefix: str = ""):
    for item in iter_opml(path):
        hints = [hint for hint in item["category_hints"] if hint]
        if category_prefix:
            hints.insert(0, category_prefix)
        add_candidate(store, item, source, kind, hints)


def add_candidate(store, item, source: str, kind: str, hints):
    raw_url = item["feed_url"].strip()
    if not raw_url.startswith(("http://", "https://")):
        return
    key = normalize_url(raw_url)
    existing = store.setdefault(
        key,
        {
            "title_hint": item.get("title_hint", "").strip(),
            "feed_url": raw_url.split("#", 1)[0],
            "site_url_hint": item.get("site_url_hint", "").strip(),
            "sources": [],
            "category_hints": [],
            "kind_hints": [],
            "language_hints": [],
        },
    )
    if source not in existing["sources"]:
        existing["sources"].append(source)
    for hint in hints:
        if hint and hint not in existing["category_hints"]:
            existing["category_hints"].append(hint)
    if kind and kind not in existing["kind_hints"]:
        existing["kind_hints"].append(kind)
    language = item.get("language", "")
    if language and language not in existing["language_hints"]:
        existing["language_hints"].append(language)
    if not existing["site_url_hint"] and item.get("site_url_hint"):
        existing["site_url_hint"] = item["site_url_hint"].strip()


def collect(args):
    store = {}
    local = Path(args.local_opml).expanduser()
    bestblogs = Path(args.bestblogs)
    plenary = Path(args.plenary)
    rsshub = Path(args.rsshub)

    add_file(store, local, "tidings-ai-radar", "article")
    add_file(store, bestblogs / "BestBlogs_RSS_Articles.opml", "bestblogs", "article")
    add_file(
        store,
        bestblogs / "opml/bestblogs_youtube_opml_all.opml",
        "bestblogs",
        "video",
        "Video",
    )
    add_file(
        store,
        bestblogs / "opml/bestblogs_podcast_opml_all.opml",
        "bestblogs",
        "podcast",
        "Podcast",
    )

    recommended = plenary / "recommended/with_category"
    for category in sorted(PLENARY_CATEGORIES):
        path = recommended / f"{category}.opml"
        if path.exists():
            add_file(store, path, "awesome-rss-feeds", "article", category)

    add_file(store, rsshub / "feeds.opml", "awesome-rsshub-routes", "article")

    manual = json.loads(Path(args.manual).read_text(encoding="utf-8"))
    for item in manual:
        add_candidate(
            store,
            item,
            "manual",
            item.get("kind", "article"),
            [item.get("category_hint", "")],
        )

    candidates = sorted(store.values(), key=lambda item: normalize_url(item["feed_url"]))
    payload = {
        "generated_at": args.date,
        "candidate_count": len(candidates),
        "candidates": candidates,
    }
    Path(args.output).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"collected {len(candidates)} unique candidates -> {args.output}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bestblogs", required=True)
    parser.add_argument("--plenary", required=True)
    parser.add_argument("--rsshub", required=True)
    parser.add_argument("--local-opml", required=True)
    parser.add_argument("--manual", default="sources/manual.json")
    parser.add_argument("--date", required=True)
    parser.add_argument("--output", required=True)
    collect(parser.parse_args())


if __name__ == "__main__":
    main()
