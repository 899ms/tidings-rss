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
}


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
        lines.extend(
            [
                f"<details>",
                f"<summary>{category} · {len(feeds)}</summary>",
                "",
                "| 名称 | 介绍 | 主分类 | Feed | 所属合集 |" if chinese else "| Source | Description | Primary category | Feed | Bundles |",
                "| --- | --- | --- | --- | --- |",
            ]
        )
        for feed in feeds:
            name = feed["title"].replace("|", "\\|")
            description = feed["description"].replace("|", "\\|")
            site = feed["site_url"] if feed["site_url"].startswith(("http://", "https://")) else feed["feed_url"]
            packs = "、".join(PACK_ZH.get(pack, pack) for pack in feed["packs"]) if chinese else ", ".join(feed["packs"])
            lines.append(f"| [{name}]({site}) | {description} | {feed['category']} | [RSS]({feed['feed_url']}) | {packs} |")
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
