#!/usr/bin/env python3
"""Rank repeatedly validated Chinese independent blogs with auditable evidence."""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.catalog import normalize_url


PROXY_HOSTS = {"feeds.feedburner.com", "feedburner.com", "rsshub.app"}
LOW_QUALITY_PATTERN = re.compile(
    r"(?:SEO|搜索引擎优化|网站推广|优惠码|返利|代购|菠菜|博彩|娱乐城|信用卡套现|网赚|采集站|破解软件|"
    r"免费资源|网站源码|绿色软件|资源分享博客|运营笔记|小红书运营|openSUSE 中文社区|游研社)",
    re.I,
)


def parse_date(value):
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)
    except (TypeError, ValueError):
        return None


def registrable_hint(host):
    parts = (host or "").lower().removeprefix("www.").split(".")
    return ".".join(parts[-2:]) if len(parts) >= 2 else (host or "").lower()


def freshness_points(days):
    if days <= 30:
        return 30
    if days <= 90:
        return 25
    if days <= 180:
        return 15
    if days <= 270:
        return 7
    return 2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", required=True)
    parser.add_argument("--validation", action="append", required=True)
    parser.add_argument("--date", required=True)
    parser.add_argument("--limit", type=int, default=400)
    parser.add_argument("--minimum-successful-rounds", type=int, default=2)
    parser.add_argument("--output", required=True)
    parser.add_argument("--selected", required=True)
    args = parser.parse_args()

    candidate_payload = json.loads(Path(args.candidates).read_text(encoding="utf-8"))
    candidates = candidate_payload["candidates"]
    rounds = [json.loads(Path(path).read_text(encoding="utf-8")) for path in args.validation]
    round_maps = [{normalize_url(item["feed_url"]): item for item in payload["results"]} for payload in rounds]
    now = datetime.fromisoformat(args.date).replace(tzinfo=timezone.utc)
    evidence = []

    for candidate in candidates:
        key = normalize_url(candidate["feed_url"])
        results = [items.get(key, {"ok": False, "error": "not checked"}) for items in round_maps]
        successful = [item for item in results if item.get("ok")]
        dates = sorted(
            {parsed for item in successful for value in item.get("item_dates", []) if (parsed := parse_date(value))},
            reverse=True,
        )
        latest = dates[0] if dates else None
        age = max(0, (now - latest).days) if latest else None
        recent_90 = sum((now - item).days <= 90 for item in dates)
        recent_180 = sum((now - item).days <= 180 for item in dates)
        lengths = [length for item in successful for length in item.get("text_lengths", []) if isinstance(length, int)]
        median_length = int(statistics.median(lengths)) if lengths else 0
        feed_host = (urlsplit(candidate["feed_url"]).hostname or "").lower()
        site_host = (urlsplit(candidate.get("site_url_hint", "")).hostname or "").lower()
        first_party = bool(site_host and registrable_hint(feed_host) == registrable_hint(site_host))

        rejection = ""
        titles = [title for item in successful for title in item.get("entry_titles", [])]
        feed_titles = [item.get("title", "") for item in successful]
        quality_text = " ".join([candidate.get("title_hint", ""), *candidate.get("topics", []), *feed_titles, *titles])
        if len(successful) < args.minimum_successful_rounds:
            rejection = f"fewer than {args.minimum_successful_rounds} successful parser rounds"
        elif age is None:
            rejection = "no trustworthy article dates"
        elif age > 180:
            rejection = "no article in the last 180 days"
        elif len(dates) < 2:
            rejection = "insufficient dated articles to establish activity"
        elif LOW_QUALITY_PATTERN.search(quality_text):
            rejection = "commercial or SEO content signal"

        score = 0.0
        if not rejection:
            score += 30 * len(successful) / len(rounds)
            score += freshness_points(age)
            score += min(20, recent_90 * 2 + recent_180)
            score += 10 if median_length >= 800 else 7 if median_length >= 400 else 4 if median_length >= 150 else 1
            score += 5 if first_party else 1
            score += max(0, 5 - candidate.get("upstream_rank", 9999) / 300)
            if feed_host in PROXY_HOSTS or feed_host.endswith(".rsshub.app"):
                score -= 4

        latest_result = successful[-1] if successful else {}
        evidence.append(
            {
                **candidate,
                "title": latest_result.get("title") or candidate["title_hint"],
                "site_url": latest_result.get("site_url") or candidate.get("site_url_hint", ""),
                "successful_rounds": len(successful),
                "checked_rounds": len(rounds),
                "latest_item_at": latest.isoformat().replace("+00:00", "Z") if latest else None,
                "latest_item_age_days": age,
                "dated_items": len(dates),
                "items_within_90_days": recent_90,
                "items_within_180_days": recent_180,
                "median_feed_text_length": median_length,
                "first_party_feed": first_party,
                "score": round(score, 2),
                "rejection_reason": rejection,
                "round_errors": [item.get("error", "") for item in results if not item.get("ok")],
            }
        )

    eligible = [item for item in evidence if not item["rejection_reason"]]
    eligible.sort(key=lambda item: (-item["score"], item["latest_item_age_days"], item["upstream_rank"]))
    selected = []
    selected_sites = set()
    for item in eligible:
        normalized_site = registrable_hint((urlsplit(item.get("site_url") or item.get("site_url_hint", "")).hostname or ""))
        if normalized_site and normalized_site in selected_sites:
            item["rejection_reason"] = "duplicate website with another feed"
            continue
        selected.append(item)
        if normalized_site:
            selected_sites.add(normalized_site)
        if len(selected) >= args.limit:
            break
    selected_urls = {normalize_url(item["feed_url"]) for item in selected}
    for item in evidence:
        item["selected"] = normalize_url(item["feed_url"]) in selected_urls
        if not item["selected"] and not item["rejection_reason"]:
            item["rejection_reason"] = f"ranked below top {args.limit}"

    evidence.sort(key=lambda item: (not item["selected"], -item["score"], item["upstream_rank"]))
    report = {
        "evaluated_at": args.date,
        "source": candidate_payload["source"],
        "criteria": {
            "parser_rounds": len(rounds),
            "minimum_successful_rounds": args.minimum_successful_rounds,
            "maximum_latest_item_age_days": 180,
            "minimum_dated_items": 2,
            "selection_limit": args.limit,
        },
        "candidate_count": len(candidates),
        "eligible_count": len(selected),
        "selected_count": len(selected),
        "blogs": evidence,
    }
    Path(args.output).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    Path(args.selected).write_text(
        json.dumps(
            {
                "generated_at": args.date,
                "source_candidate_count": len(candidates),
                "candidate_count": len(selected),
                "candidates": selected,
            },
            ensure_ascii=False,
            indent=2,
        ) + "\n",
        encoding="utf-8",
    )
    print(f"selected {len(selected)}/{len(candidates)} blogs ({len(eligible)} eligible) -> {args.selected}")


if __name__ == "__main__":
    main()
