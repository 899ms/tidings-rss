import json
import tempfile
import unittest
from pathlib import Path
from xml.etree import ElementTree as ET

from scripts.catalog import generate, normalize_url, validate_catalog


def sample_catalog():
    return {
        "version": 1,
        "generated_at": "2026-07-28",
        "validation": {"engine": "test", "criteria": "test", "candidate_count": 1, "parser_passed": 1, "retained_count": 1},
        "feeds": [
            {
                "id": "abc123",
                "title": "Example AI Lab",
                "feed_url": "https://example.com/feed.xml",
                "site_url": "https://example.com/",
                "category": "Artificial Intelligence",
                "kind": "article",
                "language": "en",
                "packs": ["ai", "all", "blogs", "engineering", "research"],
                "sources": ["manual"],
                "validated_at": "2026-07-28",
                "latest_item_at": "2026-07-28T00:00:00.000Z",
            }
        ],
    }


class CatalogTests(unittest.TestCase):
    def test_normalize_url_removes_fragment_and_trailing_slash(self):
        self.assertEqual(normalize_url("HTTPS://Example.COM:443/feed/#section"), "https://example.com/feed")

    def test_duplicate_normalized_url_is_rejected(self):
        catalog = sample_catalog()
        duplicate = dict(catalog["feeds"][0], id="second", feed_url="https://example.com/feed.xml#copy")
        catalog["feeds"].append(duplicate)
        self.assertTrue(any("duplicate normalized feed_url" in error for error in validate_catalog(catalog)))

    def test_generate_writes_parseable_pack_with_exact_feed(self):
        catalog = sample_catalog()
        with tempfile.TemporaryDirectory() as temp:
            generate(catalog, Path(temp))
            root = ET.parse(Path(temp) / "opml/tidings-ai.opml").getroot()
            feeds = [node for node in root.iter("outline") if node.get("xmlUrl")]
            self.assertEqual([node.get("xmlUrl") for node in feeds], ["https://example.com/feed.xml"])
            news = ET.parse(Path(temp) / "opml/tidings-news.opml").getroot()
            self.assertFalse([node for node in news.iter("outline") if node.get("xmlUrl")])


if __name__ == "__main__":
    unittest.main()
