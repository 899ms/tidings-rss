import re
import json
import unittest
from pathlib import Path

from scripts.catalog import PACKS


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_FILES = [
    ROOT / "README.md",
    ROOT / "README.zh-CN.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "CONTRIBUTING.zh-CN.md",
    ROOT / "SOURCES.md",
]


class RepositoryTests(unittest.TestCase):
    def test_local_markdown_targets_exist(self):
        missing = []
        for markdown in MARKDOWN_FILES:
            text = markdown.read_text(encoding="utf-8")
            targets = re.findall(r"!?\[[^]]*\]\(([^)]+)\)", text)
            targets += re.findall(r"\bsrc=[\"']([^\"']+)[\"']", text)
            for target in targets:
                target = target.strip().split("#", 1)[0]
                if not target or target.startswith(("http://", "https://", "mailto:")):
                    continue
                resolved = (markdown.parent / target).resolve()
                if not resolved.exists():
                    missing.append(f"{markdown.name}: {target}")
        self.assertEqual(missing, [])

    def test_readmes_have_no_unresolved_count_tokens(self):
        for name in ("README.md", "README.zh-CN.md"):
            self.assertNotIn("__COUNT_", (ROOT / name).read_text(encoding="utf-8"))

    def test_every_bundle_has_a_latest_release_download(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for filename, _title in PACKS.values():
            self.assertIn(f"releases/latest/download/{filename}", readme)

    def test_readme_bundle_counts_match_catalog(self):
        catalog = json.loads((ROOT / "data/feeds.json").read_text(encoding="utf-8"))
        expected = {
            filename: sum(pack in feed["packs"] for feed in catalog["feeds"])
            for pack, (filename, _title) in PACKS.items()
        }
        for name in ("README.md", "README.zh-CN.md"):
            text = (ROOT / name).read_text(encoding="utf-8")
            found = {
                filename: int(count)
                for count, filename in re.findall(
                    r"\|\s*`(\d+)`\s*\|[^\n]*releases/latest/download/(tidings-[a-z-]+\.opml)",
                    text,
                )
            }
            self.assertEqual(found, expected)

    def test_real_import_report_matches_news_and_research_bundles(self):
        catalog = json.loads((ROOT / "data/feeds.json").read_text(encoding="utf-8"))
        report = json.loads((ROOT / "reports/import-verification.json").read_text(encoding="utf-8"))
        imports = {item["file"]: item for item in report["imports"]}
        expected = {
            "tidings-news.opml": sum("news" in feed["packs"] for feed in catalog["feeds"]),
            "tidings-research.opml": sum("research" in feed["packs"] for feed in catalog["feeds"]),
        }
        self.assertEqual({name: imports[name]["imported"] for name in expected}, expected)
        self.assertTrue(all(imports[name]["final_refresh_failed"] == 0 for name in expected))
        self.assertEqual(report["failed_feeds"], [])
        expected_unique = len(
            {feed["id"] for feed in catalog["feeds"] if "news" in feed["packs"] or "research" in feed["packs"]}
        )
        self.assertEqual(report["unique_feeds"], expected_unique)
        self.assertGreater(report["visible_articles"], 0)
        self.assertTrue((ROOT / report["screenshot"]).is_file())


if __name__ == "__main__":
    unittest.main()
