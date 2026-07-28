#!/usr/bin/env python3
"""Turn Tidings validation results into the canonical curated catalog."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


AI_PATTERN = re.compile(
    r"(?:\b(?:ai|llm|ml|machine learning|deep learning|openai|anthropic|deepmind|hugging face|langchain|llamaindex|generative ai)\b|"
    r"人工智能|机器学习|深度学习|大模型|智能体|模型社区|机器之心|量子位|智谱|通义|混元|月之暗面|阶跃星辰|deepseek)",
    re.I,
)
RESEARCH_PATTERN = re.compile(
    r"(?:\b(?:research|science|scientific|journal|university|laboratory|academic|papers?|arxiv|nature|space|nasa|cern|plos|elife|quantum|astronomy)\b|"
    r"科研|科学|学术|论文|研究院|实验室|预印本|天文|航天)",
    re.I,
)
RESEARCH_PACK_PATTERN = re.compile(
    r"(?:\b(?:research|science|scientific|journal|university|laboratory|academic|papers?|arxiv|nasa|cern|plos|elife|phys\.org|quantamagazine|new scientist)\b|"
    r"科研|科学|学术|论文|研究院|实验室|预印本|航天)",
    re.I,
)
NEWS_PATTERN = re.compile(
    r"(?:\b(?:news|headlines|breaking|world|media|daily|weekly|current affairs|investigative)\b|"
    r"新闻|资讯|日报|周报|周刊|热点|媒体|晚点|36氪|少数派|爱范儿)",
    re.I,
)
ENGINEERING_PATTERN = re.compile(
    r"(?:\b(?:engineering|programming|developer|development|software|cloud|database|security|frontend|backend|web development|ios|android|devops|architecture)\b|"
    r"技术|编程|开发|架构|前端|后端|安全|数据库|开源)",
    re.I,
)
PRODUCT_PATTERN = re.compile(r"(?:\b(?:product|design|ui|ux|indie|creator)\b|产品|设计|独立开发)", re.I)
BUSINESS_PATTERN = re.compile(r"(?:\b(?:business|startup|economy|finance|venture|founder)\b|商业|创业|财经|投资|创投)", re.I)
COMMUNITY_PATTERN = re.compile(r"(?:\b(?:community|forum|v2ex|hacker news)\b|社区|论坛)", re.I)
CJK_PATTERN = re.compile(r"[\u3400-\u9fff]")
NEWS_PACK_EXCLUDED_TITLES = {"David Heinemeier Hansson"}
E2E_EXCLUDED_URLS = {
    "https://www.freebuf.com/feed",
    "https://www.microsoft.com/en-us/research/feed",
    "https://www.microsoft.com/en-us/research/blog/feed?from=https%3A%2F%2Fresearch.microsoft.com%2Frss%2Fnews.xml&type=rss",
    "https://research.microsoft.com/rss/news.xml",
}

CATEGORY_ORDER = [
    "Artificial Intelligence",
    "Engineering & Technology",
    "Research & Science",
    "News",
    "Product & Design",
    "Business & Startups",
    "Personal Blogs",
    "Communities",
    "Culture & Ideas",
    "Videos",
    "Podcasts",
]


def normalize_url(value: str) -> str:
    parsed = urlsplit(value.strip())
    host = (parsed.hostname or "").lower()
    port = parsed.port
    if port and not ((parsed.scheme == "http" and port == 80) or (parsed.scheme == "https" and port == 443)):
        host = f"{host}:{port}"
    path = re.sub(r"/{2,}", "/", parsed.path or "/")
    if path != "/":
        path = path.rstrip("/")
    return urlunsplit((parsed.scheme.lower(), host, path, parsed.query, ""))


def clean_text(value: str, fallback: str) -> str:
    cleaned = re.sub(r"\s+", " ", str(value or "")).strip()
    return (cleaned or fallback)[:160]


def parse_time(value):
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)
    except (TypeError, ValueError):
        return None


def age_days(value, now):
    parsed = parse_time(value)
    return max(0, (now - parsed).days) if parsed else None


def combined_text(candidate, title):
    return " ".join(
        [title, candidate.get("title_hint", ""), candidate.get("feed_url", ""), *candidate.get("category_hints", [])]
    )


def classify(candidate, title, kind):
    text = combined_text(candidate, title)
    hints = " ".join(candidate.get("category_hints", []))
    if kind == "video":
        return "Videos"
    if kind == "podcast":
        return "Podcasts"
    if AI_PATTERN.search(text):
        return "Artificial Intelligence"
    if RESEARCH_PATTERN.search(text):
        return "Research & Science"
    if NEWS_PATTERN.search(hints) or "热点资讯" in hints or "科技自媒体" in hints:
        return "News"
    if PRODUCT_PATTERN.search(text) or "产品与独立开发" in hints:
        return "Product & Design"
    if BUSINESS_PATTERN.search(text):
        return "Business & Startups"
    if COMMUNITY_PATTERN.search(text) or "社区" in hints:
        return "Communities"
    if ENGINEERING_PATTERN.search(text) or "技术博客" in hints or "技术周刊" in hints:
        return "Engineering & Technology"
    if "个人博客" in hints:
        return "Personal Blogs"
    if any(value in hints for value in ("Books", "History")):
        return "Culture & Ideas"
    return "Personal Blogs" if "bestblogs" in candidate.get("sources", []) else "Engineering & Technology"


def infer_kind(candidate):
    hints = candidate.get("kind_hints", [])
    text = combined_text(candidate, candidate.get("title_hint", ""))
    if "video" in hints:
        return "video"
    if "podcast" in hints:
        return "podcast"
    if "youtube.com/feeds/videos" in text:
        return "video"
    if re.search(r"podcast|simplecast|libsyn|omnycontent|megaphone|buzzsprout|podbean|feeds\.npr\.org/510", text, re.I):
        return "podcast"
    return "article"


def infer_language(candidate, title):
    hints = candidate.get("language_hints", [])
    if "zh" in hints or CJK_PATTERN.search(title) or CJK_PATTERN.search(candidate.get("title_hint", "")):
        return "zh"
    return "en"


def determine_packs(candidate, title, category, kind, freshness):
    text = combined_text(candidate, title)
    packs = {"all"}
    if AI_PATTERN.search(text) or "Artificial Intelligence" in " ".join(candidate.get("category_hints", [])):
        packs.add("ai")
    if kind == "video" and (freshness is None or freshness <= 730):
        packs.add("videos")
    if kind == "podcast" and (freshness is None or freshness <= 730):
        packs.add("podcasts")
    news_hints = " ".join(candidate.get("category_hints", []))
    strong_news = bool(
        NEWS_PATTERN.search(f"{title} {candidate.get('feed_url', '')}")
        or re.search(r"(?:\bNews\b|热点资讯|新闻资讯|科技媒体|安全资讯)", news_hints, re.I)
    )
    if (
        category == "News"
        and title not in NEWS_PACK_EXCLUDED_TITLES
        and strong_news
        and freshness is not None
        and freshness <= 21
    ):
        packs.add("news")
    research_hints = " ".join(candidate.get("category_hints", []))
    strong_research_hint = any(
        hint in research_hints
        for hint in ("AI Research", "University Research Lab", "Academic Papers", "Scientific Journal", "Research Institution", "Space Research", "Science News", "学术论文")
    )
    if (
        kind == "article"
        and "reddit.com" not in candidate.get("feed_url", "")
        and (strong_research_hint or RESEARCH_PACK_PATTERN.search(text))
        and (freshness is None or freshness <= 730)
    ):
        packs.add("research")
    if kind == "article" and category not in {"News", "Communities"} and (freshness is None or freshness <= 730):
        packs.add("blogs")
    if category in {"Engineering & Technology", "Artificial Intelligence"} and kind == "article":
        packs.add("engineering")
    return packs


def choose_duplicate(left, right):
    def score(item):
        return (
            item["feed_url"].startswith("https://"),
            bool(item.get("latest_item_at")),
            len(item.get("sources", [])),
        )

    winner, loser = (right, left) if score(right) > score(left) else (left, right)
    winner["sources"] = sorted(set(winner["sources"]) | set(loser["sources"]))
    winner["packs"] = sorted(set(winner["packs"]) | set(loser["packs"]))
    return winner


def curate(args):
    candidates_payload = json.loads(Path(args.candidates).read_text(encoding="utf-8"))
    validation = json.loads(Path(args.validation).read_text(encoding="utf-8"))
    candidates = {item["feed_url"]: item for item in candidates_payload["candidates"]}
    https_results = {}
    if args.https_validation:
        https_payload = json.loads(Path(args.https_validation).read_text(encoding="utf-8"))
        https_results = {item["feed_url"]: item for item in https_payload["results"]}
    now = datetime.fromisoformat(args.date).replace(tzinfo=timezone.utc)
    retained = []
    stale = []
    failures = []
    e2e_failures = []
    https_upgraded = 0
    effective_passed = 0

    for original_result in validation["results"]:
        candidate = candidates[original_result["feed_url"]]
        result = original_result
        if candidate["feed_url"].startswith("http://"):
            https_url = "https://" + candidate["feed_url"][7:]
            https_result = https_results.get(https_url)
            if https_result and https_result.get("ok"):
                candidate = {**candidate, "feed_url": https_url}
                result = https_result
                https_upgraded += 1
        if not result.get("ok"):
            failures.append(result)
            continue
        effective_passed += 1
        if normalize_url(candidate["feed_url"]) in E2E_EXCLUDED_URLS:
            e2e_failures.append(candidate["feed_url"])
            continue
        freshness = age_days(result.get("latest_item_at"), now)
        if freshness is not None and freshness > 730:
            stale.append(result)
            continue
        kind = infer_kind(candidate)
        title = clean_text(result.get("title"), candidate.get("title_hint") or candidate["feed_url"])
        category = classify(candidate, title, kind)
        language = infer_language(candidate, title)
        packs = determine_packs(candidate, title, category, kind, freshness)
        if language == "zh":
            packs.add("chinese")
        normalized = normalize_url(candidate["feed_url"])
        retained.append(
            {
                "id": hashlib.sha256(normalized.encode()).hexdigest()[:12],
                "title": title,
                "feed_url": candidate["feed_url"].split("#", 1)[0],
                "site_url": clean_text(result.get("site_url"), candidate.get("site_url_hint", "")),
                "category": category,
                "kind": kind,
                "language": language,
                "packs": sorted(packs),
                "sources": sorted(candidate.get("sources", [])),
                "validated_at": args.date,
                "latest_item_at": result.get("latest_item_at"),
            }
        )

    deduped = {}
    duplicate_count = 0
    for item in retained:
        site = normalize_url(item["site_url"]) if item["site_url"].startswith(("http://", "https://")) else ""
        key = (item["title"].casefold(), site or normalize_url(item["feed_url"]))
        if site and key in deduped:
            deduped[key] = choose_duplicate(deduped[key], item)
            duplicate_count += 1
        else:
            deduped[key] = item

    feeds = list(deduped.values())
    titles = defaultdict(list)
    for item in feeds:
        titles[item["title"].casefold()].append(item)
    disambiguated_titles = 0
    for matches in titles.values():
        if len(matches) < 2:
            continue
        for item in matches:
            suffix = ""
            if item["kind"] == "video":
                suffix = "Video"
            elif item["kind"] == "podcast":
                suffix = "Podcast"
            elif item["language"] == "zh":
                suffix = "中文"
            elif item["category"] == "Research & Science":
                suffix = "Science"
            elif item["category"] == "News":
                suffix = "News"
            if suffix:
                item["title"] = f"{item['title']} — {suffix}"
                disambiguated_titles += 1
    feeds.sort(key=lambda item: (CATEGORY_ORDER.index(item["category"]), item["title"].casefold()))
    catalog = {
        "version": 1,
        "generated_at": args.date,
        "validation": {
            "engine": validation.get("engine", "Tidings parseFeedUrl"),
            "criteria": "Feed parsed successfully with at least one item; dated feeds older than 730 days and persistent in-app import failures were excluded.",
            "candidate_count": len(candidates),
            "parser_passed": effective_passed,
            "retained_count": len(feeds),
        },
        "feeds": feeds,
    }
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    error_counts = Counter(re.sub(r"\b\d{3,}\b", "N", item.get("error", "unknown"))[:160] for item in failures)
    summary = {
        "validated_at": args.date,
        "engine": validation.get("engine", "Tidings parseFeedUrl"),
        "candidates": len(candidates),
        "parser_passed": effective_passed,
        "parser_failed": len(failures),
        "http_urls_upgraded_to_https": https_upgraded,
        "excluded_stale": len(stale),
        "excluded_after_e2e_import": len(e2e_failures),
        "canonical_duplicates_removed": duplicate_count,
        "duplicate_titles_disambiguated": disambiguated_titles,
        "published": len(feeds),
        "unknown_latest_item_date": sum(1 for item in feeds if not item["latest_item_at"]),
        "remaining_http_feeds": sum(item["feed_url"].startswith("http://") for item in feeds),
        "by_source": dict(sorted(Counter(source for item in feeds for source in item["sources"]).items())),
        "by_category": {category: sum(item["category"] == category for item in feeds) for category in CATEGORY_ORDER},
        "by_pack": dict(sorted(Counter(pack for item in feeds for pack in item["packs"]).items())),
        "top_failure_reasons": [{"reason": reason, "count": count} for reason, count in error_counts.most_common(15)],
    }
    Path(args.summary).parent.mkdir(parents=True, exist_ok=True)
    Path(args.summary).write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"published {len(feeds)} feeds; excluded {len(failures)} failed, {len(stale)} stale, {duplicate_count} duplicates")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", required=True)
    parser.add_argument("--validation", required=True)
    parser.add_argument("--https-validation")
    parser.add_argument("--date", required=True)
    parser.add_argument("--output", default="data/feeds.json")
    parser.add_argument("--summary", default="reports/validation-summary.json")
    curate(parser.parse_args())


if __name__ == "__main__":
    main()
