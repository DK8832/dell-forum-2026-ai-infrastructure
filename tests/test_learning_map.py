import json
import unittest

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from build_learning_map import build_map


class LearningMapTest(unittest.TestCase):
    def test_five_unique_layers(self):
        result = build_map()
        ids = [item["id"] for item in result["layers"]]
        self.assertEqual(5, len(ids))
        self.assertEqual(len(ids), len(set(ids)))

    def test_every_layer_has_question_and_practice(self):
        for item in build_map()["layers"]:
            self.assertTrue(item["question"].endswith("?"))
            self.assertGreater(len(item["practice"]), 20)

    def test_event_fact_is_explicit(self):
        facts = json.loads((ROOT / "data" / "event_facts.json").read_text(encoding="utf-8"))
        self.assertEqual("2026-08-25", facts["date"])
        self.assertEqual("서울 코엑스 그랜드볼룸", facts["venue"])


if __name__ == "__main__":
    unittest.main()


