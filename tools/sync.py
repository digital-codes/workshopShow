#!/usr/bin/env python3
"""
Synchronise new/updated files from a set of workspace directories
(<src_root>/ws1, <src_root>/ws2, …) into matching sub‑folders under a
target HTML directory (<dst_root>/ws1, …).

Whenever any file is copied for a workspace, the central
<dst_root>/data.json file is (re)written so that each entry’s
"doc" field points to the workspace sub‑folder (e.g. "/ws1").

Run it from cron (or any scheduler) – it is safe to execute
repeatedly.
"""

import argparse
import json
import os
import shutil
import sys
from pathlib import Path
from typing import List, Dict, Any

# ----------------------------------------------------------------------
# Helper – default metadata for a workspace entry.
# Adjust titles/authors/descriptions/images as you see fit.
# ----------------------------------------------------------------------
DEFAULT_ENTRY = {
    "id": 0,                           # to be filled in per workspace
    "title": "Untitled Workspace",
    "author": "Unknown",
    "description": "",
    "doc": "doc.pdf",                     # to be filled in per workspace
    "image": "/img/default.png",   # placeholder – change per workspace if desired
}


def load_data_json(dst_root: Path) -> List[Dict[str, Any]]:
    """Read existing data.json (if any); otherwise start with an empty list."""
    data_path = dst_root / "data.json"
    if data_path.is_file():
        try:
            return json.loads(data_path.read_text(encoding="utf-8"))
        except Exception as exc:
            print(f"[WARN] Failed to parse {data_path}: {exc}", file=sys.stderr)
    return []


def save_data_json(dst_root: Path, entries: List[Dict[str, Any]]) -> None:
    """Write the JSON file with pretty indentation."""
    data_path = dst_root / "items.json"
    data_path.write_text(json.dumps(entries, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[INFO] Updated {data_path}")


def sync_workspace(src_root: Path, docs_dir: Path, dst_root: Path, workspace: str) -> bool:
    """
    Copy new/updated files from src_root/workspace → dst_root/workspace.

    Returns
    -------
    bool
        True if at least one file was copied, False otherwise.
    """
    if docs_dir is not None:
        src_dir = src_root / workspace / docs_dir 
    else:
        src_dir = src_root / workspace
    dst_dir = dst_root / workspace

    if not src_dir.is_dir():
        print(f"[WARN] Source workspace missing: {src_dir}", file=sys.stderr)
        return False

    any_copied = False

    for root, _, files in os.walk(src_dir):
        rel_root = Path(root).relative_to(src_dir)      # path relative to wsX
        target_root = dst_dir / rel_root                # matching target folder
        target_root.mkdir(parents=True, exist_ok=True)

        for fname in files:
            src_file = Path(root) / fname
            dst_file = target_root / fname

            # Copy if destination missing OR source newer
            if (not dst_file.exists()) or (src_file.stat().st_mtime > dst_file.stat().st_mtime):
                shutil.copy2(src_file, dst_file)       # preserve mtime, perms, etc.
                print(f"Copied: {src_file} → {dst_file}")
                any_copied = True

    return any_copied


def update_data_json_for_workspace(
    dst_root: Path,
    workspace: str,
    prefix: str | None,
    next_id: int,
) -> int:
    """
    Returns the new entry and the next free numeric ID (used when we need to create a new entry).
    """

    # Not found → create a brand‑new entry
    try:
        with open(dst_root / workspace / "title.txt", "r", encoding="utf-8") as f:
            title = f.read().strip()
        with open(dst_root / workspace / "author.txt", "r", encoding="utf-8") as f:
            author = f.read().strip()
        with open(dst_root / workspace / "description.txt", "r", encoding="utf-8") as f:
            description = f.read().strip()
        report_path = dst_root / workspace / "report.pdf"
        if not report_path.is_file():
            raise FileNotFoundError(f"Missing required file: {report_path}")
        logo_path = dst_root / workspace / "logo.png"
        if not logo_path.is_file():
            raise FileNotFoundError(f"Missing required file: {logo_path}")
        if prefix is None:
            prefix = ""
        else:
            prefix = prefix.rstrip("/") + "/"
        new_entry = {
            "id": next_id,
            "title": title,
            "author": author,
            "description": description,
            "doc": f"{prefix}{workspace}/report.pdf",
            "image": f"{prefix}{workspace}/logo.png",
        }
    except:
        new_entry = DEFAULT_ENTRY.copy()
        new_entry.id = next_id
        
    return new_entry, next_id + 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Synchronise workspace directories to a target HTML tree and "
            "maintain a central data.json reflecting the workspaces."
        )
    )
    parser.add_argument(
        "-s", "--src",
        required=True,
        type=Path,
        help="Root directory containing the workspaces (e.g. /home/me/projects)",
    )
    parser.add_argument(
        "-t", "--target",
        required=True,
        type=Path,
        help="Target root directory for the HTML copies (e.g. /var/www/html)",
    )
    parser.add_argument(
        "-p", "--prefix",
        default=None,
        type=str,
        help="Prefix for the target",
    )
    parser.add_argument(
        "-d", "--docs",
        default=None,
        type=str,
        help="Docs prefix for the src directory",
    )
    args = parser.parse_args()

    src_root = args.src.expanduser().resolve()
    dst_root = args.target.expanduser().resolve()
    workspaces = [d.name for d in src_root.iterdir() if d.is_dir()]

    next_id = 1

    # Process each workspace
    need_update = False
    for ws in workspaces:
        print(f"[INFO] Processing workspace: {ws}")
        copied = sync_workspace(src_root, args.docs, dst_root, ws)
        if copied:
            need_update = True

    if need_update:
        catalogue = []
        for ws in workspaces:
            print(f"[INFO] Processing workspace: {ws}")
            entry, next_id = update_data_json_for_workspace(dst_root, ws, args.prefix, next_id)
            catalogue.append(entry)
        print("Catalogue:", catalogue)
        # Write back the possibly‑modified catalogue
        save_data_json(dst_root, catalogue)

    return 0


if __name__ == "__main__":
    sys.exit(main())

# test like this:
# python sync.py --src ./src -t ../public/data/ -p data -d report
# * * * * * /usr/local/bin/ws_sync.py --src /path/to/somedir \
#                                   --target /path/to/target \
#                                   --docs report \
#                                   >> /var/log/ws_sync.log 2>&1

