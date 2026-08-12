#!/usr/bin/env python3
"""Convert chinese-independent-blogs CSV into validation candidates."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.catalog import normalize_url


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True)
    parser.add_argument("--date", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    candidates = []
    seen = set()
    with Path(args.csv).open(encoding="utf-8-sig", newline="") as handle:
        for rank, row in enumerate(csv.DictReader(handle), start=1):
            feed_url = row.get(" RSS feed", "").strip()
            if not feed_url.startswith(("http://", "https://")):
                continue
            normalized = normalize_url(feed_url)
            if normalized in seen:
                continue
            seen.add(normalized)
            tags = [item.strip() for item in row.get(" tags", "").split(";") if item.strip()]
            candidates.append(
                {
                    "title_hint": row.get("Introduction", "").strip(),
                    "feed_url": feed_url,
                    "site_url_hint": row.get(" Address", "").strip(),
                    "sources": ["chinese-independent-blogs"],
                    "category_hints": ["Chinese Independent Blog", *tags],
                    "kind_hints": ["article"],
                    "language_hints": ["zh"],
                    "upstream_rank": rank,
                    "topics": tags,
                }
            )

    payload = {
        "generated_at": args.date,
        "source": "https://github.com/timqian/chinese-independent-blogs",
        "candidate_count": len(candidates),
        "candidates": candidates,
    }
    Path(args.output).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"collected {len(candidates)} Chinese independent blog candidates -> {args.output}")


if __name__ == "__main__":
    main()
