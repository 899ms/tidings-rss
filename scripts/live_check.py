#!/usr/bin/env python3
"""Dependency-free live health check for the published feed catalog."""

from __future__ import annotations

import argparse
import json
import random
import ssl
import threading
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET


MAX_BYTES = 10 * 1024 * 1024
USER_AGENT = "TidingsRSSCatalog/1.0 (+https://github.com/fuxiaoai/tidings-rss)"
HOST_LIMITS = defaultdict(lambda: threading.BoundedSemaphore(2))


def local_name(tag):
    return tag.rsplit("}", 1)[-1].split(":")[-1].lower()


def inspect_payload(payload, content_type):
    stripped = payload.lstrip()
    if "json" in content_type.lower() or stripped.startswith(b"{"):
        data = json.loads(payload)
        items = data.get("items")
        if not isinstance(items, list):
            raise ValueError("JSON response has no items array")
        return "json-feed", len(items)
    root = ET.fromstring(payload)
    root_name = local_name(root.tag)
    if root_name not in {"rss", "feed", "rdf"}:
        raise ValueError(f"unexpected XML root: {root_name}")
    item_count = sum(local_name(node.tag) in {"item", "entry"} for node in root.iter())
    return root_name, item_count


def check_feed(feed, timeout):
    started = time.monotonic()
    request = Request(
        feed["feed_url"],
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/rss+xml, application/atom+xml, application/feed+json, application/json, text/xml, application/xml, */*;q=0.1",
        },
    )
    try:
        host = (urlsplit(feed["feed_url"]).hostname or "").lower()
        with HOST_LIMITS[host]:
            for attempt in range(2):
                try:
                    with urlopen(request, timeout=timeout, context=ssl.create_default_context()) as response:
                        payload = response.read(MAX_BYTES + 1)
                        if len(payload) > MAX_BYTES:
                            raise ValueError("response exceeds 10 MiB")
                        format_name, item_count = inspect_payload(payload, response.headers.get("Content-Type", ""))
                        if item_count < 1:
                            raise ValueError("feed has no items")
                        return {
                            "id": feed["id"],
                            "title": feed["title"],
                            "feed_url": feed["feed_url"],
                            "ok": True,
                            "format": format_name,
                            "items": item_count,
                            "duration_ms": round((time.monotonic() - started) * 1000),
                        }
                except Exception:
                    if attempt == 0:
                        time.sleep(1)
                        continue
                    raise
    except Exception as error:  # noqa: BLE001 - report remote failures uniformly
        return {
            "id": feed["id"],
            "title": feed["title"],
            "feed_url": feed["feed_url"],
            "ok": False,
            "error": str(error)[:240],
            "duration_ms": round((time.monotonic() - started) * 1000),
        }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", default="data/feeds.json")
    parser.add_argument("--output", default="live-validation.json")
    parser.add_argument("--sample", type=int, default=0, help="deterministic sample size; 0 checks every feed")
    parser.add_argument("--concurrency", type=int, default=8)
    parser.add_argument("--timeout", type=int, default=20)
    parser.add_argument("--min-success-rate", type=float, default=0.70)
    args = parser.parse_args()

    catalog = json.loads(Path(args.catalog).read_text(encoding="utf-8"))
    feeds = list(catalog["feeds"])
    random.Random(catalog["generated_at"]).shuffle(feeds)
    if args.sample and args.sample < len(feeds):
        feeds = feeds[: args.sample]
    results = []
    with ThreadPoolExecutor(max_workers=max(1, args.concurrency)) as pool:
        futures = [pool.submit(check_feed, feed, args.timeout) for feed in feeds]
        for future in as_completed(futures):
            results.append(future.result())
    results.sort(key=lambda item: item["title"].casefold())
    passed = sum(item["ok"] for item in results)
    payload = {
        "catalog_date": catalog["generated_at"],
        "checked": len(results),
        "passed": passed,
        "failed": len(results) - passed,
        "success_rate": round(passed / len(results), 4) if results else 0,
        "results": results,
    }
    Path(args.output).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"live check: {passed}/{len(results)} passed ({payload['success_rate']:.1%})")
    if payload["success_rate"] < args.min_success_rate:
        raise SystemExit(f"success rate below {args.min_success_rate:.0%}")


if __name__ == "__main__":
    main()
