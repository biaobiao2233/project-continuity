"""Synthetic two-task Git pilot; no network, user repository, or router access."""
from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


@unittest.skipUnless(shutil.which("git"), "Git is needed for the isolated worktree pilot")
class GitPilot(unittest.TestCase):
    def test_two_short_tasks_integrate_against_shared_contract(self):
        with tempfile.TemporaryDirectory(prefix="pw2-pilot-") as directory:
            root = Path(directory)
            repo, runtime, ui = root/"repo", root/"runtime", root/"ui"
            repo.mkdir()
            env = dict(os.environ)
            env.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull,
                       GIT_AUTHOR_NAME="Synthetic Pilot", GIT_COMMITTER_NAME="Synthetic Pilot",
                       GIT_AUTHOR_EMAIL="pilot@example.invalid", GIT_COMMITTER_EMAIL="pilot@example.invalid")

            def git(cwd, *args):
                result = subprocess.run(["git", "-c", "core.hooksPath="+os.devnull, "-c", "commit.gpgsign=false", *args],
                                        cwd=cwd, env=env, capture_output=True, text=True, timeout=15)
                self.assertEqual(result.returncode, 0, result.stderr)
                return result.stdout.strip()

            git(repo, "init", "-b", "main")
            contract = {"version": 1, "status_fields": ["mode", "region"]}
            (repo/"contract.json").write_text(json.dumps(contract))
            (repo/"README.md").write_text("Synthetic project; no live dependencies.\n")
            git(repo, "add", "."); git(repo, "commit", "-m", "Define shared status contract")
            base = git(repo, "rev-parse", "HEAD")
            git(repo, "worktree", "add", "-b", "task/runtime-status", str(runtime), base)
            git(repo, "worktree", "add", "-b", "task/ui-status", str(ui), base)

            (runtime/"backend.py").write_text("def status():\n    return {'mode': 'smart', 'region': 'auto'}\n")
            git(runtime, "add", "backend.py"); git(runtime, "commit", "-m", "Implement bounded status provider")
            runtime_head = git(runtime, "rev-parse", "HEAD")
            self.assertFalse((ui/"backend.py").exists())
            (ui/"frontend.py").write_text("def render(value):\n    return value['mode'] + ':' + value['region']\n")
            git(ui, "add", "frontend.py"); git(ui, "commit", "-m", "Implement bounded status consumer")
            ui_head = git(ui, "rev-parse", "HEAD")
            self.assertFalse((runtime/"frontend.py").exists())
            self.assertEqual(git(repo, "rev-parse", "HEAD"), base)

            git(repo, "merge", "--no-ff", "-m", "Integrate status provider", runtime_head)
            git(repo, "merge", "--no-ff", "-m", "Integrate status consumer", ui_head)
            result = subprocess.run([sys.executable, "-B", "-c",
                "import json;from backend import status;from frontend import render;"
                "c=json.load(open('contract.json'));s=status();"
                "assert sorted(s)==sorted(c['status_fields']);assert render(s)=='smart:auto';"
                "print('SYNTHETIC_COMBINATION_OK')"], cwd=repo, env=env, capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("SYNTHETIC_COMBINATION_OK", result.stdout)
            self.assertEqual(git(repo, "status", "--porcelain"), "")
            self.assertEqual(json.loads((repo/"contract.json").read_text()), contract)
            self.assertNotEqual(git(repo, "rev-parse", "HEAD"), base)
            git(repo, "worktree", "remove", str(runtime))
            git(repo, "worktree", "remove", str(ui))
            # TemporaryDirectory cleans only this test's isolated resources.


if __name__ == "__main__":
    unittest.main()
