from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class BundleChecks(unittest.TestCase):
    def test_one_entrypoint(self):
        self.assertEqual([p.relative_to(ROOT).as_posix() for p in ROOT.rglob('SKILL.md')], ['SKILL.md'])

    def test_entrypoint_is_compact(self):
        self.assertLessEqual(len((ROOT/'SKILL.md').read_text().splitlines()), 150)

    def test_local_markdown_links_resolve(self):
        for path in ROOT.rglob('*.md'):
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
                if '://' in target or target.startswith('#'):
                    continue
                target_path = (path.parent / target.split('#', 1)[0]).resolve()
                self.assertTrue(target_path.is_relative_to(ROOT.resolve()), (path.name, target))
                self.assertTrue(target_path.exists(), (path.name, target))

    def test_full_and_compact_prompt_limits(self):
        for filename, limit in [('personalization-v2.txt', 5000), ('personalization-v2-compact.txt', 1500)]:
            content = (ROOT/'assets'/filename).read_text()
            self.assertLessEqual(len(content), limit)
            for marker in ['GitHub', 'RECORD_SYNC_PENDING', 'worktree', 'EverOS', 'gate']:
                self.assertIn(marker, content)

    def test_platform_adapters_preserve_distinct_policy(self):
        self.assertIn('allow_implicit_invocation: true', (ROOT/'agents/openai.yaml').read_text())
        self.assertIn('allow_implicit_invocation: false', (ROOT/'assets/adapters/codex-openai.yaml').read_text())
        self.assertTrue((ROOT/'assets/icon.svg').is_file())


if __name__ == '__main__':
    unittest.main()
