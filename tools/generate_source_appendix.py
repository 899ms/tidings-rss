#!/usr/bin/env python3
"""Generate the complete source appendix embedded in both READMEs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


START = "<!-- SOURCE_APPENDIX_START -->"
END = "<!-- SOURCE_APPENDIX_END -->"
PACK_ZH = {
    "all": "全集",
    "blogs": "中文独立博客",
    "ai": "AI",
    "news": "新闻",
    "research": "科研",
    "engineering": "工程",
    "videos": "视频",
    "podcasts": "播客",
    "chinese": "中文",
    "company-tech": "大厂技术号",
    "wechat": "微信公众号",
}
CATEGORY_ZH = {
    "Artificial Intelligence": "人工智能",
    "Engineering & Technology": "工程与技术",
    "Research & Science": "科研与科学",
    "News": "新闻",
    "Product & Design": "产品与设计",
    "Business & Startups": "商业与创业",
    "Personal Blogs": "个人博客",
    "Communities": "社区",
    "Culture & Ideas": "文化与思想",
    "Videos": "视频",
    "Podcasts": "播客",
}
CATEGORY_INTRO_ZH = {
    "Artificial Intelligence": "人工智能内容",
    "Engineering & Technology": "工程与技术内容",
    "Research & Science": "科研与科学内容",
    "News": "新闻资讯",
    "Product & Design": "产品与设计内容",
    "Business & Startups": "商业与创业内容",
    "Personal Blogs": "个人博客",
    "Communities": "社区讨论",
    "Culture & Ideas": "文化与思想内容",
    "Videos": "视频频道",
    "Podcasts": "播客节目",
}
CATEGORY_INTRO_EN = {
    "Artificial Intelligence": "Artificial intelligence feed.",
    "Engineering & Technology": "Engineering and technology feed.",
    "Research & Science": "Research and science feed.",
    "News": "News feed.",
    "Product & Design": "Product and design feed.",
    "Business & Startups": "Business and startup feed.",
    "Personal Blogs": "Independent blog.",
    "Communities": "Community feed.",
    "Culture & Ideas": "Culture and ideas feed.",
    "Videos": "Video channel.",
    "Podcasts": "Podcast.",
}


def localized_description(feed, chinese):
    if not chinese and feed.get("description_en"):
        return feed["description_en"]
    value = feed["description"]
    generic = value in {f"{name} 订阅源" for name in CATEGORY_ZH} or value in {"视频频道", "播客节目"}
    if generic:
        return CATEGORY_INTRO_ZH[feed["category"]] if chinese else CATEGORY_INTRO_EN[feed["category"]]
    if chinese:
        return value
    if value.startswith("主要写"):
        return "Chinese independent blog."
    if value.startswith("公众号，主要关注"):
        topic = value.removeprefix("公众号，主要关注").removesuffix("。")
        return f"WeChat article feed covering {topic}."
    return value


def appendix(catalog, chinese):
    grouped = {}
    for feed in catalog["feeds"]:
        grouped.setdefault(feed["category"], []).append(feed)
    title = "## 全量源清单" if chinese else "## Complete source directory"
    intro = (
        f"下面列出全集中的 {len(catalog['feeds'])} 个订阅源。每项都标明主分类与所属合集；内容由 `data/feeds.json` 生成。"
        if chinese
        else f"All {len(catalog['feeds'])} feeds in the complete collection are listed below with their primary category and bundles. This appendix is generated from `data/feeds.json`."
    )
    lines = [START, title, "", intro, ""]
    for category, feeds in grouped.items():
        group_name = CATEGORY_ZH.get(category, category) if chinese else category
        lines.extend(
            [
                f"<details>",
                f"<summary>{group_name} · {len(feeds)}</summary>",
                "",
                "| 名称 | 介绍 | 主分类 | Feed | 所属合集 |" if chinese else "| Source | Description | Primary category | Feed | Bundles |",
                "| --- | --- | --- | --- | --- |",
            ]
        )
        for feed in feeds:
            name = feed["title"].replace("|", "\\|")
            description = localized_description(feed, chinese).replace("|", "\\|")
            site = feed["site_url"] if feed["site_url"].startswith(("http://", "https://")) else feed["feed_url"]
            packs = "、".join(PACK_ZH.get(pack, pack) for pack in feed["packs"]) if chinese else ", ".join(feed["packs"])
            category_name = CATEGORY_ZH.get(feed["category"], feed["category"]) if chinese else feed["category"]
            lines.append(f"| [{name}]({site}) | {description} | {category_name} | [RSS]({feed['feed_url']}) | {packs} |")
        lines.extend(["", "</details>", ""])
    lines.append(END)
    return "\n".join(lines)


def replace(path, content):
    text = path.read_text(encoding="utf-8")
    if START in text and END in text:
        before, rest = text.split(START, 1)
        _old, after = rest.split(END, 1)
        text = before.rstrip() + "\n\n" + content + after
    else:
        text = text.rstrip() + "\n\n" + content + "\n"
    path.write_text(text, encoding="utf-8")


def rendered(path, content):
    text = path.read_text(encoding="utf-8")
    if START not in text or END not in text:
        return text.rstrip() + "\n\n" + content + "\n"
    before, rest = text.split(START, 1)
    _old, after = rest.split(END, 1)
    return before.rstrip() + "\n\n" + content + after


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", default="data/feeds.json")
    parser.add_argument("--readme", default="README.md")
    parser.add_argument("--readme-zh", default="README.zh-CN.md")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    catalog = json.loads(Path(args.catalog).read_text(encoding="utf-8"))
    targets = ((Path(args.readme), appendix(catalog, False)), (Path(args.readme_zh), appendix(catalog, True)))
    if args.check:
        stale = [str(path) for path, content in targets if path.read_text(encoding="utf-8") != rendered(path, content)]
        if stale:
            raise SystemExit("stale README source appendix: " + ", ".join(stale))
        print(f"README appendices valid for {len(catalog['feeds'])} feeds")
        return
    for path, content in targets:
        replace(path, content)
    print(f"generated README appendices for {len(catalog['feeds'])} feeds")


if __name__ == "__main__":
    main()
