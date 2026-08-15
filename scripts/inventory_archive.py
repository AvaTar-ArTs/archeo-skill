#!/usr/bin/env python3
"""List archive members and classify likely project artifacts without extracting them."""

from __future__ import annotations

import argparse
import json
import tarfile
import zipfile
from pathlib import PurePosixPath


def classify(path: str) -> str:
    name = PurePosixPath(path).name.lower()
    if name.startswith("readme") or name in {"license", "licence"}:
        return "orientation"
    if name in {"package.json", "pyproject.toml", "requirements.txt", "package-lock.json", "firebase.json"}:
        return "runtime"
    if name.startswith(".env"):
        return "configuration"
    if any(token in path.lower() for token in ("test", "cypress", "spec")):
        return "tests"
    if any(token in name for token in ("render", "generate", "compose", "controller", "inference", "parser")):
        return "execution"
    if any(path.lower().endswith(ext) for ext in (".png", ".jpg", ".jpeg", ".webp", ".mp4", ".pdf")):
        return "output-or-asset"
    return "other"


def members(path: str):
    if path.lower().endswith(".zip"):
        with zipfile.ZipFile(path) as archive:
            return [{"path": info.filename, "size": info.file_size, "kind": classify(info.filename)} for info in archive.infolist()]
    if path.lower().endswith((".tar", ".tar.gz", ".tgz")):
        with tarfile.open(path) as archive:
            return [{"path": info.name, "size": info.size, "kind": classify(info.name)} for info in archive.getmembers()]
    raise ValueError("Expected .zip, .tar, .tar.gz, or .tgz archive")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("archive")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = members(args.archive)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        for item in result:
            print(f"{item['kind']:16} {item['size']:10} {item['path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
