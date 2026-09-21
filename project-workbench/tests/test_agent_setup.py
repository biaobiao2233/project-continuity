import subprocess
import sys
import tempfile
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts' / 'install_agent_setup.py'
MARKER = 'AUTO-GENERATED from `~/.agents/guidance/project-workbench-v2-core.md`'


class AgentSetupTests(unittest.TestCase):
    def run_setup(self, home, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), '--home', str(home), *args],
            cwd=ROOT.parent,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_dry_run_does_not_write(self):
        with tempfile.TemporaryDirectory() as td:
            home = Path(td)
            result = self.run_setup(home)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('DRY_RUN_COMPLETE', result.stdout)
            self.assertFalse((home / '.agents').exists())

    def test_apply_and_second_apply_are_safe(self):
        with tempfile.TemporaryDirectory() as td:
            home = Path(td)
            first = self.run_setup(home, '--apply', '--link-antigravity')
            self.assertEqual(first.returncode, 0, first.stderr)
            shared = home / '.agents' / 'skills' / 'project-workbench'
            self.assertEqual(
                (shared / 'VERSION').read_text(encoding='utf-8').strip(),
                (ROOT / 'VERSION').read_text(encoding='utf-8').strip(),
            )

            prompts = [
                home / '.codex' / 'AGENTS.md',
                home / '.config' / 'opencode' / 'AGENTS.md',
                home / '.zcode' / 'AGENTS.md',
                home / '.gemini' / 'GEMINI.md',
                home / '.claude' / 'CLAUDE.md',
            ]
            for prompt in prompts:
                self.assertTrue(prompt.is_file(), prompt)
                self.assertIn(MARKER, prompt.read_text(encoding='utf-8'))

            self.assertFalse((home / '.config' / 'opencode' / 'skills' / 'project-workbench').exists())
            for link in [
                home / '.gemini' / 'config' / 'skills' / 'project-workbench',
                home / '.gemini' / 'antigravity-cli' / 'skills' / 'project-workbench',
            ]:
                self.assertTrue(link.exists(), link)
                self.assertEqual(link.resolve(), shared.resolve())

            second = self.run_setup(home, '--apply', '--link-antigravity')
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertGreaterEqual(second.stdout.count('LINK_ALREADY_OK'), 2)

    def test_unmanaged_global_guidance_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as td:
            home = Path(td)
            target = home / '.codex' / 'AGENTS.md'
            target.parent.mkdir(parents=True)
            target.write_text('my unrelated instructions\n', encoding='utf-8')
            result = self.run_setup(home, '--apply', '--guidance-only')
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('refusing to overwrite unmanaged guidance', result.stderr)
            self.assertEqual(target.read_text(encoding='utf-8'), 'my unrelated instructions\n')


if __name__ == '__main__':
    unittest.main()
