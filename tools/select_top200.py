#!/usr/bin/env python3
"""Build the reproducible Top 200 shortlist from the canonical catalog."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit


TARGET = 200
QUOTAS = {
    "Artificial Intelligence": 19,
    "Engineering & Technology": 72,
    "Security": 8,
    "Technology Media": 10,
    "Tech Newsletters & Weeklies": 8,
    "Research & Science": 13,
    "News": 11,
    "Product & Design": 5,
    "Business & Startups": 4,
    "Personal Blogs": 24,
    "Communities": 5,
    "Culture & Ideas": 8,
    "Videos": 2,
    "Podcasts": 11,
}

# The production validation pool is intentionally wider than the final quota and
# committed as reports/top200-candidates.json. Keeping explicit limits makes the
# exact 307-feed review reproducible without relying on an undocumented multiplier.
CANDIDATE_LIMITS = {
    "Artificial Intelligence": 28,
    "Engineering & Technology": 112,
    "Security": 8,
    "Technology Media": 10,
    "Tech Newsletters & Weeklies": 9,
    "Research & Science": 18,
    "News": 16,
    "Product & Design": 5,
    "Business & Startups": 5,
    "Personal Blogs": 37,
    "Communities": 13,
    "Culture & Ideas": 10,
    "Videos": 20,
    "Podcasts": 16,
}

# Editorial reputation is deliberately explicit. It keeps a repeatable selector from
# mistaking a frequently updated release feed for an established publisher or author.
EDITORIAL_TIERS = {
    3: {
        "Anthropic News", "Apple Machine Learning Research", "Artificial Intelligence",
        "Google DeepMind News", "Hugging Face - Blog", "MIT News - Artificial intelligence",
        "OpenAI News", "Simon Willison's Weblog", "The latest research from Google", "机器之心", "量子位",
        "Articles on Smashing Magazine — For Web Designers And Developers", "AWS Architecture Blog",
        "Databricks", "Engineering at Meta", "freeCodeCamp Programming Tutorials: Python, JavaScript, Git & More",
        "Martin Fowler", "Netflix TechBlog - Medium", "Node.js Blog", "Python Insider", "Rust Blog",
        "Stack Overflow Blog", "The Cloudflare Blog", "The GitHub Blog", "The JetBrains Blog", "Vercel News",
        "张鑫旭-鑫空间-鑫生活", "鸟窝", "唐巧的博客", "阁子", "王福强的个人博客：一个架构士的思考与沉淀",
        "Krebs on Security", "Schneier on Security", "CISA", "FreeBuf 网络安全行业门户", "腾讯玄武实验室",
        "Ars Technica", "Engadget", "IT之家", "TechCrunch", "The Verge — News", "WIRED", "少数派",
        "爱范儿", "MIT Technology Review", "Last Week in AI", "The Batch", "Golang Weekly",
        "JavaScript Weekly", "This Week in Rust", "阮一峰的网络日志", "AAAS: Science: Table of Contents",
        "Amazon Science", "BBC News — Science", "eLife: latest articles", "NASA", "Nature", "PLOS One",
        "Quanta Magazine", "Scientific American Content: Global", "Al Jazeera – Breaking News, World News and Video from Al Jazeera",
        "BBC News — News", "NPR Topics: World", "NYT > Technology", "ProPublica", "World news | The Guardian",
        "奇客Solidot–传递最新科技情报", "拾月的博客", "阿里云设计中心", "扯氮集", "知足常乐-水星投资理财的基本意念",
        "SEISAMUSE", "JustZht's EchoChamber", "Shuibaco • 水八口", "Another Dayu", "KAIX.IN", "先生制造",
        "Hacker News", "Lobsters", "LINUX DO · 文档共建", "Python Core Development", "Rust Internals · Language Design",
        "OpenAI Developer Community · API", "V2EX · 技术", "3Blue1Brown", "BBC Earth",
        "Computerphile", "DeepLearningAI — Video", "Fireship", "freeCodeCamp.org", "Google DeepMind",
        "Hung-yi Lee", "Kurzgesagt – In a Nutshell", "OpenAI", "StatQuest with Josh Starmer", "TED", "李永乐老师",
        "Darknet Diaries", "Discovery", "Hanselminutes with Scott Hanselman", "Planet Money", "The Vergecast",
        "声动早咖啡", "忽左忽右", "文化有限", "硅谷101 — Podcast", "知行小酒馆",
    },
    2: {
        "AI 开发者日报", "AI", "DeepSeek", "智谱", "cs.AI updates on arXiv.org", "cs.CL updates on arXiv.org", "cs.CV updates on arXiv.org",
        "cs.LG updates on arXiv.org", "我爱计算机视觉", "新智元", "通义实验室", "腾讯混元",
        "AWS Architecture Blog", "AWS News Blog", "Canva - Engineering Blog", "Cloud Blog", "Elastic Blog - Elasticsearch, Kibana, and ELK Stack",
        "Engineering at Slack", "Etsy Engineering | Code as Craft", "Microsoft Azure Blog", "Spotify Engineering",
        "Stripe Blog", "The Airbnb Tech Blog - Medium", "Supabase Blog", "The New Stack", "Tw93 Blog", "piglei",
        "pseudoyu", "laike9m's blog", "OneV's Den", "Skywind Inside", "Weishu's Notes", "Android Performance",
        "MacTalk-池建强的 Blog", "Blog | Phodal - A Growth Engineer", "后端技术杂谈", "卡瓦邦噶！", "豌豆花下猫",
        "Security Affairs", "安全客", "ZDNET Security", "36氪", "AIGC Weekly", "大橘和朋友们的周刊", "潮流周刊",
        "FlowingData", "Phys.org - latest science and technology news stories", "Science Latest", "Space | The Guardian",
        "腾讯研究院", "InfoQ — News", "虎嗅", "钛媒体：引领未来商业与生活新知", "HackerNews每日摘要 on SuperTechFans",
        "61’s life", "Velas电波站", "虹线", "雷蒙三十｜幫助忙碌現代人的聰明工作、好好生活的生產力指南",
        "不吐不快", "如鱼饮水", "印记", "一派胡言 · Blog", "东评西就", "静风说", "Maohang Gao's Blog",
        "Kubernetes · General Discussions", "NixOS Development", "Ask HN", "Show HN", "ByteByteGo", "Real Engineering",
        "Nature on PBS", "NNgroup", "Y Combinator", "The Pragmatic Engineer", "Branch Education", "Dwarkesh Patel",
        "Fragmented - AI Developer Podcast", "Invest Like the Best with Patrick O'Shaughnessy", "Throughline", "半拿铁 | 商业沉浮录",
        "捕蛇者说", "乱翻书", "晚点聊 LateTalk", "纵横四海", "硬地骇客", "What's Next｜科技早知道",
    },
}

# Parent/child and derivative feeds that add cleanup cost without a distinct
# editorial voice. They stay in the complete and topic collections.
TOP200_EXCLUSIONS = {
    "机器之心SOTA模型": "same-publisher topic subset of 机器之心",
    "HackerNews每日摘要 on SuperTechFans": "derivative digest of the selected Hacker News community feed",
}

TITLE_PUBLISHERS = {
    "AI": "google",
    "Cloud Blog": "google",
    "Google DeepMind News": "google",
    "The latest research from Google": "google",
    "Google DeepMind": "google",
    "Artificial Intelligence": "amazon",
    "AWS Architecture Blog": "amazon",
    "AWS News Blog": "amazon",
    "Amazon Science": "amazon",
    "Hacker News": "hacker news",
    "Ask HN": "hacker news",
    "Show HN": "hacker news",
    "HackerNews每日摘要 on SuperTechFans": "hacker news",
    "机器之心": "机器之心",
    "机器之心SOTA模型": "机器之心",
}
PUBLISHER_PREFIXES = {
    "BBC ": "bbc",
    "News from Google": "google",
    "NYT > ": "new york times",
}
PUBLISHER_LIMITS = {
    "bbc": 2,
    "google": 2,
    "mit": 2,
    "new york times": 2,
    "theguardian.com": 2,
    "阿里巴巴": 2,
    "腾讯": 2,
}

SHARED_PLATFORM_HOSTS = {"www.youtube.com", "youtube.com", "rsshub.bestblogs.dev", "wechat2rss.bestblogs.dev", "wechat2rss.xlab.app"}
PROXY_HOST_MARKERS = ("rsshub.", "wechat2rss.", "anyfeeder.com")
LOW_SIGNAL_TITLE_MARKERS = ("Release notes from ", "Recent Commits to ", " - Newest: ", "本周最热", "本周热榜")


def parse_date(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)


def age_days(feed, now):
    return max(0.0, (now - parse_date(feed["latest_item_at"])).total_seconds() / 86400)


def explicit_tier(title):
    for value in (3, 2):
        if title in EDITORIAL_TIERS[value]:
            return value
    return 1


def editorial_tier(feed, blog_scores):
    value = explicit_tier(feed["title"])
    blog_score = blog_scores.get(feed["feed_url"])
    if blog_score is not None and blog_score >= 90:
        value = max(value, 2)
    return value


def source_signal(feed):
    sources = set(feed["sources"])
    return min(6.0, 1.5 * len(sources) + (2.0 if "tidings-ai-radar" in sources else 0.0))


def host(feed):
    return (urlsplit(feed["feed_url"]).hostname or "").lower()


def publisher_key(feed):
    title = feed["title"]
    if title in TITLE_PUBLISHERS:
        return TITLE_PUBLISHERS[title]
    for prefix, publisher in PUBLISHER_PREFIXES.items():
        if title.startswith(prefix):
            return publisher
    if feed.get("organization"):
        organization = feed["organization"].casefold()
        if organization in {"amazon web services", "amazon"}:
            return "amazon"
        return organization
    hostname = (urlsplit(feed.get("site_url") or feed["feed_url"]).hostname or "").lower().removeprefix("www.")
    if hostname in {"youtube.com", "xiaoyuzhoufm.com"} or hostname in SHARED_PLATFORM_HOSTS:
        return feed["title"].casefold()
    if hostname.endswith("bbci.co.uk") or hostname.endswith("bbc.co.uk"):
        return "bbc"
    return hostname or feed["title"].casefold()


def existing_blog_score(feed, blog_scores):
    value = blog_scores.get(feed["feed_url"])
    return 12.0 * value / 100.0 if value is not None else 0.0


def evidence_note(feed, blog_scores):
    registered = explicit_tier(feed["title"])
    blog_score = blog_scores.get(feed["feed_url"])
    if registered == 3:
        return "editorial registry: established institution, publisher, or long-running author"
    if registered == 2:
        return "editorial registry: recognized specialist source or independent author"
    if blog_score is not None:
        return f"Chinese blog review: {blog_score:.2f}/100 from update cadence, feed text, first-party status, and three parser rounds"
    return f"catalog evidence: {len(set(feed['sources']))} discovery list(s), recent publishing, and three parser rounds"


def base_score(feed, now, blog_scores):
    days = age_days(feed, now)
    freshness = 18 if days <= 7 else 15 if days <= 30 else 10 if days <= 90 else 4 if days <= 180 else -20
    title = feed["title"]
    value = 45 * editorial_tier(feed, blog_scores) / 3 + freshness + source_signal(feed) + existing_blog_score(feed, blog_scores)
    feed_host = host(feed)
    if not any(marker in feed_host for marker in PROXY_HOST_MARKERS):
        value += 6
    if feed["feed_url"].startswith("https://"):
        value += 2
    if any(title.startswith(marker) or marker in title for marker in LOW_SIGNAL_TITLE_MARKERS):
        value -= 24
    if feed_host == "www.youtube.com":
        value -= 5
    if "reddit.com" in feed_host or "news.google.com" in feed_host:
        value -= 22
    return round(value, 3)


def ranked_candidates(catalog, now, blog_scores):
    return sorted(
        (feed for feed in catalog["feeds"] if age_days(feed, now) <= 180),
        key=lambda feed: (feed["category"], -base_score(feed, now, blog_scores), age_days(feed, now), feed["title"].casefold()),
    )


def choose(catalog, now, blog_scores):
    selected = []
    selected_ids = set()
    publisher_counts = Counter()
    decisions = []
    for category, quota in QUOTAS.items():
        candidates = [feed for feed in ranked_candidates(catalog, now, blog_scores) if feed["category"] == category]
        category_selected = []
        for feed in candidates:
            if feed["title"] in TOP200_EXCLUSIONS:
                continue
            key = publisher_key(feed)
            allowed = PUBLISHER_LIMITS.get(key, 1)
            if publisher_counts[key] >= allowed:
                continue
            category_selected.append(feed)
            selected.append(feed)
            selected_ids.add(feed["id"])
            publisher_counts[key] += 1
            if len(category_selected) == quota:
                break
        if len(category_selected) != quota:
            raise SystemExit(f"{category}: selected {len(category_selected)}, expected {quota}")
    if len(selected) != TARGET:
        raise SystemExit(f"selected {len(selected)}, expected {TARGET}")
    ranks = {feed["id"]: index + 1 for index, feed in enumerate(sorted(selected, key=lambda f: (-base_score(f, now, blog_scores), f["title"].casefold())))}
    for feed in catalog["feeds"]:
        decisions.append({
            "id": feed["id"], "title": feed["title"], "feed_url": feed["feed_url"], "category": feed["category"],
            "selected": feed["id"] in selected_ids, "editorial_tier": editorial_tier(feed, blog_scores),
            "score": base_score(feed, now, blog_scores), "latest_item_at": feed["latest_item_at"],
            "latest_item_age_days": round(age_days(feed, now), 2), "rank": ranks.get(feed["id"]),
            "reason": "selected within category quota" if feed["id"] in selected_ids else "not selected after quality, freshness, and publisher deduplication",
        })
    return selected, decisions


def validated_choice(catalog, now, blog_scores, round_paths, video_round_paths, candidate_urls):
    rounds = [json.loads(Path(path).read_text(encoding="utf-8")) for path in round_paths]
    result_maps = [{item["feed_url"]: item for item in payload["results"]} for payload in rounds]
    video_result_maps = [
        {item["feed_url"]: item for item in json.loads(Path(path).read_text(encoding="utf-8"))["results"]}
        for path in video_round_paths
    ]
    selected = []
    selected_ids = set()
    publisher_counts = Counter()
    validation_by_url = {}
    for category, quota in QUOTAS.items():
        candidates = [
            feed for feed in ranked_candidates(catalog, now, blog_scores)
            if feed["category"] == category and feed["feed_url"] in candidate_urls
        ]
        category_selected = []
        for feed in candidates:
            if feed["title"] in TOP200_EXCLUSIONS:
                continue
            maps = video_result_maps if feed["category"] == "Videos" and video_result_maps else result_maps
            results = [items.get(feed["feed_url"], {"ok": False, "error": "not included in validation round"}) for items in maps]
            validation_by_url[feed["feed_url"]] = results
            if not all(item.get("ok") and item.get("item_count", 0) > 0 and item.get("latest_item_at") for item in results):
                continue
            key = publisher_key(feed)
            allowed = PUBLISHER_LIMITS.get(key, 1)
            if publisher_counts[key] >= allowed:
                continue
            category_selected.append(feed)
            selected.append(feed)
            selected_ids.add(feed["id"])
            publisher_counts[key] += 1
            if len(category_selected) == quota:
                break
        if len(category_selected) != quota:
            raise SystemExit(f"{category}: only {len(category_selected)} feeds passed every validation round; expected {quota}")
    decisions = []
    ranks = {feed["id"]: index + 1 for index, feed in enumerate(sorted(selected, key=lambda f: (-base_score(f, now, blog_scores), f["title"].casefold())))}
    for feed in catalog["feeds"]:
        results = validation_by_url.get(feed["feed_url"], [])
        if feed["id"] in selected_ids:
            reason = "selected after three successful Tidings parser rounds"
        elif results and not all(item.get("ok") for item in results):
            reason = "failed at least one current Tidings parser round"
        else:
            reason = "not selected after quality, freshness, and publisher deduplication"
        decision = {
            "id": feed["id"], "title": feed["title"], "feed_url": feed["feed_url"], "category": feed["category"],
            "selected": feed["id"] in selected_ids, "editorial_tier": editorial_tier(feed, blog_scores),
            "score": base_score(feed, now, blog_scores), "latest_item_at": feed["latest_item_at"],
            "latest_item_age_days": round(age_days(feed, now), 2), "rank": ranks.get(feed["id"]),
            "reason": reason,
        }
        if feed["id"] in selected_ids:
            decision["parser_rounds"] = [
                {
                    "ok": item["ok"],
                    "item_count": item["item_count"],
                    "latest_item_at": item["latest_item_at"],
                    "duration_ms": item["duration_ms"],
                }
                for item in results
            ]
            blog_score = blog_scores.get(feed["feed_url"])
            decision["selection_evidence"] = {
                "publisher": publisher_key(feed),
                "editorial_registry_tier": explicit_tier(feed["title"]),
                "chinese_blog_curation_score": round(blog_score, 2) if blog_score is not None else None,
                "discovery_list_count": len(set(feed["sources"])),
                "first_party_or_direct_endpoint": not any(marker in host(feed) for marker in PROXY_HOST_MARKERS),
                "note": evidence_note(feed, blog_scores),
            }
        decisions.append(decision)
    return selected, decisions


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", default="data/feeds.json")
    parser.add_argument("--blog-report", default="reports/chinese-blog-curation.json")
    parser.add_argument("--date", required=True)
    parser.add_argument("--output", default="reports/top200-curation.json")
    parser.add_argument("--candidates-output")
    parser.add_argument("--candidate-snapshot")
    parser.add_argument("--validation", action="append")
    parser.add_argument("--video-validation", action="append")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if args.validation and len(args.validation) != 3:
        parser.error("validated selection requires exactly three --validation reports")
    if args.validation and len(args.video_validation or []) != 3:
        parser.error("validated selection requires exactly three --video-validation reports")
    if args.validation and not args.candidate_snapshot:
        parser.error("validated selection requires --candidate-snapshot")
    catalog_path = Path(args.catalog)
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    blog_report = json.loads(Path(args.blog_report).read_text(encoding="utf-8"))
    blog_scores = {item["feed_url"]: item["score"] for item in blog_report["blogs"]}
    now = datetime.fromisoformat(args.date).replace(tzinfo=timezone.utc)
    candidate_urls = None
    if args.candidate_snapshot:
        candidate_snapshot = json.loads(Path(args.candidate_snapshot).read_text(encoding="utf-8"))
        candidate_urls = {feed["feed_url"] for feed in candidate_snapshot["candidates"]}
        if len(candidate_urls) != candidate_snapshot.get("candidate_count"):
            parser.error("candidate snapshot count or URL uniqueness is invalid")
    selected, decisions = (
        validated_choice(catalog, now, blog_scores, args.validation, args.video_validation or [], candidate_urls)
        if args.validation
        else choose(catalog, now, blog_scores)
    )
    selected_ids = {feed["id"] for feed in selected}
    if args.apply:
        for feed in catalog["feeds"]:
            packs = set(feed["packs"])
            if feed["id"] in selected_ids:
                packs.add("top200")
            else:
                packs.discard("top200")
            feed["packs"] = sorted(packs)
        catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.candidates_output:
        candidates = []
        for category, limit in CANDIDATE_LIMITS.items():
            category_candidates = [feed for feed in ranked_candidates(catalog, now, blog_scores) if feed["category"] == category]
            candidates.extend(category_candidates[:limit])
        Path(args.candidates_output).write_text(
            json.dumps({
                "generated_at": args.date,
                "profile": "top200-production-v1",
                "candidate_limits": CANDIDATE_LIMITS,
                "candidate_count": len(candidates),
                "candidates": candidates,
            }, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    report = {
        "selected_at": args.date,
        "selection_target": TARGET,
        "scope": "strict subset of data/feeds.json",
        "criteria": {
            "freshness_limit_days": 180,
            "signals": ["editorial reputation", "community-list overlap", "recent publishing", "first-party endpoint", "Chinese blog curation score"],
            "publisher_rule": "one feed per publisher by default; two only for distinct directions at selected large organizations",
            "network_preference": "official and direct endpoints preferred; obvious region-sensitive and generated query feeds penalized",
            "category_quotas": QUOTAS,
            "candidate_profile": "top200-production-v1",
            "candidate_limits": CANDIDATE_LIMITS,
            "explicit_exclusions": TOP200_EXCLUSIONS,
        },
        "selected_count": len(selected),
        "selected_by_category": dict(Counter(feed["category"] for feed in selected)),
        "selected_by_language": dict(Counter(feed["language"] for feed in selected)),
        "selected_by_kind": dict(Counter(feed["kind"] for feed in selected)),
        "selected_by_pack": dict(Counter(pack for feed in selected for pack in feed["packs"] if pack != "top200")),
        "validation": {
            "status": "passed" if args.validation else "pending",
            "engine": "Tidings parseFeedUrl",
            "required_parser_rounds": 3,
            "required_successful_rounds": 3,
            "round_reports": args.validation or [],
            "video_round_reports": args.video_validation or [],
            "video_probe_concurrency": 1 if args.video_validation else None,
            "probe_scope": "current-node direct application traffic; mainland reachability not independently verified",
        },
        "reproduction": {
            "candidate_snapshot": args.candidate_snapshot or "reports/top200-candidates.json",
            "selector": "tools/select_top200.py",
            "required_validation_reports": 3,
            "required_video_validation_reports": 3,
        },
        "decisions": decisions,
    }
    Path(args.output).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"selected {len(selected)} feeds across {len(QUOTAS)} categories -> {args.output}")


if __name__ == "__main__":
    main()
