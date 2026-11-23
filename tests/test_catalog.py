import json, subprocess, sys, unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import build_readme, check_links  # noqa: E402

REQUIRED = {"name", "repo", "description", "kind", "skill_paths", "install", "works_with", "topics"}

class Catalog(unittest.TestCase):
    def setUp(self):
        self.skills = json.loads((ROOT / "skills.json").read_text())

    def test_fields_and_unique_names(self):
        names = [e["name"] for e in self.skills]
        self.assertEqual(len(names), len(set(names)))
        for e in self.skills:
            self.assertTrue(REQUIRED <= set(e), e["name"])
            self.assertIn(e["kind"], ("skill", "playbook"))
            self.assertTrue(e["skill_paths"])
            self.assertEqual({"claude", "agents", "paste"}, set(e["install"]))
            self.assertTrue(e["repo"].endswith("/" + e["name"]))

    def test_readme_is_generated_and_count_matches(self):
        self.assertEqual((ROOT / "README.md").read_text(), build_readme.build())
        self.assertIn(f"Index of {len(self.skills)} ", build_readme.build())

    def test_every_skill_in_a_table(self):
        text = build_readme.build()
        for e in self.skills:
            self.assertIn(f"[{e['name']}]({e['repo']})", text)

    def test_link_check_offline(self):
        urls = check_links.links(build_readme.build())
        self.assertGreater(len(urls), 30)
        class R:
            status = 200
            def __enter__(self): return self
            def __exit__(self, *a): return False
        self.assertEqual(check_links.status("https://github.com/x/y", opener=lambda *a, **k: R()), 200)

if __name__ == "__main__":
    unittest.main()
