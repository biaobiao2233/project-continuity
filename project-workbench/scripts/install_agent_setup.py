#!/usr/bin/env python3
'''Install/sync Project Workbench and global guidance for the user's coding agents.

Dry-run by default. Use --apply to write. Standard library only.
'''

from __future__ import annotations

import argparse
import datetime as dt
import os
from pathlib import Path
import shutil
import stat
import subprocess

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
GUIDANCE_SRC = PACKAGE_ROOT / 'assets' / 'global-guidance'
MANAGED_MARKER = 'AUTO-GENERATED from `~/.agents/guidance/project-workbench-v2-core.md`'

TARGETS = {
    'codex': (Path('.codex') / 'AGENTS.md', '# Codex Global Guidance'),
    'opencode': (Path('.config') / 'opencode' / 'AGENTS.md', '# OpenCode Global Guidance'),
    'zcode': (Path('.zcode') / 'AGENTS.md', '# ZCode Global Guidance'),
    'antigravity': (Path('.gemini') / 'GEMINI.md', '# Global Antigravity Operating Rules'),
    'claude': (Path('.claude') / 'CLAUDE.md', '# Claude Code Global Guidance'),
}

ANTIGRAVITY_LINKS = [
    Path('.gemini') / 'config' / 'skills' / 'project-workbench',
    Path('.gemini') / 'antigravity-cli' / 'skills' / 'project-workbench',
]


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--apply', action='store_true', help='perform writes; default is dry-run')
    p.add_argument('--home', type=Path, default=Path.home(), help='target home directory')
    p.add_argument('--guidance-only', action='store_true', help='do not replace the shared Skill')
    p.add_argument('--link-antigravity', action='store_true', help='create native Antigravity links to the shared Skill')
    p.add_argument('--force-guidance', action='store_true', help='replace an existing unmanaged global guidance file after backup')
    p.add_argument('--force-links', action='store_true', help='replace an existing non-link Antigravity Skill directory after backup')
    return p.parse_args()


def render(name, title):
    core = (GUIDANCE_SRC / 'core.md').read_text(encoding='utf-8').strip()
    adapter = (GUIDANCE_SRC / 'adapters' / f'{name}.md').read_text(encoding='utf-8').strip()
    return (
        f'{title}\n\n'
        f'> {MANAGED_MARKER} + `{name}.md`. Edit the sources, then rerun the sync script.\n\n'
        f'{adapter}\n\n{core}\n'
    )


def is_junction(path):
    checker = getattr(path, 'is_junction', None)
    if checker and checker():
        return True
    if os.name == 'nt':
        try:
            attrs = os.lstat(path).st_file_attributes
            return bool(attrs & stat.FILE_ATTRIBUTE_REPARSE_POINT) and path.is_dir()
        except (AttributeError, FileNotFoundError, OSError):
            return False
    return False


def is_linklike(path):
    return path.is_symlink() or is_junction(path)


def remove_path(path):
    if is_linklike(path):
        if path.is_dir():
            path.rmdir()
        else:
            path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)
    elif path.exists():
        path.unlink()


def backup_rel(path, home):
    try:
        return path.resolve(strict=False).relative_to(home.resolve(strict=False))
    except Exception:
        safe = str(path).replace(':', '').replace('\\', '/').lstrip('/')
        return Path('_external') / safe


def safe_backup(path, home, backup_root):
    if not path.exists() and not is_linklike(path):
        return
    dest = backup_root / backup_rel(path, home)
    dest.parent.mkdir(parents=True, exist_ok=True)
    if is_linklike(path):
        meta = dest.with_suffix(dest.suffix + '.link.txt')
        try:
            target = os.readlink(path)
        except OSError:
            target = path.resolve(strict=False)
        meta.write_text(str(target), encoding='utf-8')
    elif path.is_dir():
        shutil.copytree(path, dest, dirs_exist_ok=True)
    else:
        shutil.copy2(path, dest)


def replace_dir(src, dst, home, backup_root):
    if src.resolve() == dst.resolve(strict=False):
        print('SKILL_ALREADY_CANONICAL', dst)
        return
    safe_backup(dst, home, backup_root)
    stage = dst.with_name(dst.name + '.installing')
    old = dst.with_name(dst.name + '.old')
    for p in (stage, old):
        if p.exists() or is_linklike(p):
            remove_path(p)
    shutil.copytree(src, stage, ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.git'))
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists() or is_linklike(dst):
        dst.rename(old)
    stage.rename(dst)
    if old.exists() or is_linklike(old):
        remove_path(old)


def write_text(path, content, home, backup_root, force_guidance=False):
    if path.exists():
        current = path.read_text(encoding='utf-8', errors='replace')
        if MANAGED_MARKER not in current and not force_guidance:
            raise RuntimeError(f'refusing to overwrite unmanaged guidance: {path}; inspect it or use --force-guidance')
    safe_backup(path, home, backup_root)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8', newline='\n')


def make_link(link, target, home, backup_root, force_links=False):
    if link.exists() or is_linklike(link):
        if is_linklike(link):
            try:
                if link.resolve() == target.resolve():
                    print('LINK_ALREADY_OK', link)
                    return
            except OSError:
                pass
        elif not force_links:
            raise RuntimeError(f'refusing to replace non-link Skill directory: {link}; inspect it or use --force-links')
        safe_backup(link, home, backup_root)
        remove_path(link)
    link.parent.mkdir(parents=True, exist_ok=True)
    if os.name == 'nt':
        subprocess.run(['cmd', '/c', 'mklink', '/J', str(link), str(target)], check=True)
    else:
        link.symlink_to(target, target_is_directory=True)


def main():
    args = parse_args()
    home = args.home.expanduser().resolve()
    skill_dst = home / '.agents' / 'skills' / 'project-workbench'
    guidance_dst = home / '.agents' / 'guidance'
    stamp = dt.datetime.now().strftime('%Y%m%d-%H%M%S')
    backup_root = home / '.agents' / 'backups' / 'project-workbench-agent-setup' / stamp

    print('MODE=', 'APPLY' if args.apply else 'DRY_RUN')
    print('HOME=', home)
    print('SKILL_SOURCE=', PACKAGE_ROOT)
    print('SKILL_TARGET=', skill_dst)
    print('BACKUP_ROOT=', backup_root)

    if not args.guidance_only:
        print('PLAN install_skill', skill_dst)
    print('PLAN sync_guidance_sources', guidance_dst)
    for name, (rel, _) in TARGETS.items():
        print('PLAN generate_' + name, home / rel)
    if args.link_antigravity:
        for rel in ANTIGRAVITY_LINKS:
            print('PLAN link_antigravity', home / rel)

    if not args.apply:
        print('DRY_RUN_COMPLETE')
        return 0

    if not args.guidance_only:
        replace_dir(PACKAGE_ROOT, skill_dst, home, backup_root)

    core_src = GUIDANCE_SRC / 'core.md'
    core_target = guidance_dst / 'project-workbench-v2-core.md'
    safe_backup(core_target, home, backup_root)
    core_target.parent.mkdir(parents=True, exist_ok=True)
    core_target.write_text(core_src.read_text(encoding='utf-8'), encoding='utf-8', newline='\n')

    for src in sorted((GUIDANCE_SRC / 'adapters').glob('*.md')):
        target = guidance_dst / 'adapters' / src.name
        safe_backup(target, home, backup_root)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(src.read_text(encoding='utf-8'), encoding='utf-8', newline='\n')

    for name, (rel, title) in TARGETS.items():
        write_text(home / rel, render(name, title), home, backup_root, args.force_guidance)

    if args.link_antigravity:
        for rel in ANTIGRAVITY_LINKS:
            make_link(home / rel, skill_dst, home, backup_root, args.force_links)

    print('APPLY_COMPLETE')
    version = skill_dst / 'VERSION'
    print('INSTALLED_VERSION=', version.read_text(encoding='utf-8').strip() if version.exists() else 'unknown')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
