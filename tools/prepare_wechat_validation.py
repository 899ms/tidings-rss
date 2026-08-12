#!/usr/bin/env python3
"""Keep WeChat candidates that passed both two-second probes."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sources", default="sources/wechat-curated.json")
    parser.add_argument("--probe", action="append", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    sources = json.loads(Path(args.sources).read_text(encoding="utf-8"))
    rounds = [json.loads(Path(path).read_text(encoding="utf-8")) for path in args.probe]
    passed = [
        item for item in sources
        if all(next(result for result in report["results"] if result["feed_url"] == item["feed_url"])["ok"] for report in rounds)
    ]
    payload = {
        "candidates": [
            {
                "title_hint": item["title"],
                "feed_url": item["feed_url"],
                "site_url_hint": item["feed_url"],
                "kind": "article",
                "language": "zh",
            }
            for item in passed
        ]
    }
    Path(args.output).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"prepared {len(passed)}/{len(sources)} WeChat feeds for Tidings validation")


if __name__ == "__main__":
    main()
