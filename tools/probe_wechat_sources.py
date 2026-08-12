#!/usr/bin/env python3
"""Run two strict two-second time-to-first-byte probes for curated WeChat feeds."""

from __future__ import annotations

import argparse
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


def probe(url: str) -> dict:
    command = [
        "curl", "-L", "-sS", "--connect-timeout", "2", "--max-time", "2",
        "--range", "0-2047", "-o", "/dev/null", "-w",
        "%{http_code}\t%{content_type}\t%{time_starttransfer}\t%{time_total}", url,
    ]
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    parts = completed.stdout.strip().split("\t")
    http_code = int(parts[0]) if parts and parts[0].isdigit() else 0
    content_type = parts[1] if len(parts) > 1 else ""
    start_transfer = float(parts[2]) if len(parts) > 2 and parts[2] else 99.0
    return {
        "ok": http_code == 200 and "xml" in content_type.lower() and start_transfer <= 2,
        "http_code": http_code,
        "content_type": content_type,
        "time_to_first_byte_ms": round(start_transfer * 1000),
        "curl_exit_code": completed.returncode,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="sources/wechat-curated.json")
    parser.add_argument("--output", required=True)
    parser.add_argument("--round", type=int, required=True)
    args = parser.parse_args()
    candidates = json.loads(Path(args.input).read_text(encoding="utf-8"))
    with ThreadPoolExecutor(max_workers=8) as pool:
        checks = list(pool.map(lambda item: probe(item["feed_url"]), candidates))
    results = [
        {"title": item["title"], "feed_url": item["feed_url"], **check}
        for item, check in zip(candidates, checks, strict=True)
    ]
    payload = {"round": args.round, "criterion": "HTTP 200 XML response began within two seconds", "results": results}
    Path(args.output).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    passed = sum(item["ok"] for item in results)
    print(f"WeChat probe round {args.round}: {passed}/{len(results)} passed")


if __name__ == "__main__":
    main()
