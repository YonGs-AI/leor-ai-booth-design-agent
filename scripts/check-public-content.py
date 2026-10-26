#!/usr/bin/env python3
"""Validate the explicitly approved contents of this public documentation repository."""
import argparse
import json
import posixpath
import re
import subprocess
import sys

ALLOWED = frozenset((
    ".gitignore", "README.md", "INSTALL.md", "CAPABILITY-GUIDE.md",
    "EXAMPLES.md", "CHANGELOG.md", "SECURITY.md", "registry/server.json",
    "scripts/check-public-content.py",
))
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    re.compile(r"\b(?:sk-[A-Za-z0-9_-]{20,}|AIza[A-Za-z0-9_-]{30,}|gh[pousr]_[A-Za-z0-9]{25,}|github_pat_[A-Za-z0-9_]{30,}|AKIA[A-Z0-9]{16}|LTAI[A-Za-z0-9]{12,})\b"),
    re.compile(r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b"),
    re.compile(r"(?i)\b(?:postgres(?:ql)?|mysql|mongodb(?:\+srv)?|redis)://[^\s<>]+"),
    re.compile(r"(?i)\b(?:api[_-]?key|access[_-]?token|client[_-]?secret|password|secret[_-]?key)\s*[\x22\x27]?\s*[:=]\s*[\x22\x27]?([A-Za-z0-9_./+=-]{16,})"),
    re.compile(r"https?://[^\s/@:]+:[^\s/@]+@[^\s]+"),
)


def git(*args):
    return subprocess.check_output(["git", *args])


def inspect(ref, cache):
    entries = []
    for raw in git("ls-tree", "-rz", ref).split(b"\0"):
        if not raw:
            continue
        metadata, raw_path = raw.split(b"\t", 1)
        mode, kind, oid = metadata.decode().split()
        entries.append((mode, kind, oid, raw_path.decode("utf-8")))
    paths = {entry[3] for entry in entries}
    for mode, kind, oid, path in entries:
        if path not in ALLOWED or kind != "blob" or mode not in ("100644", "100755"):
            raise ValueError("Unapproved file or file mode")
        if oid not in cache:
            data = git("cat-file", "blob", oid)
            if len(data) > 256_000 or b"\0" in data:
                raise ValueError("Non-document content")
            text = data.decode("utf-8")
            if any(pattern.search(text) for pattern in SECRET_PATTERNS):
                raise ValueError("Possible credential")
            cache[oid] = text
        text = cache[oid]
        if path.endswith(".md"):
            for target in re.findall(r"\]\(([^\s)]+)\)", text):
                if target.startswith(("#", "https://", "http://", "mailto:")):
                    continue
                target = posixpath.normpath(posixpath.join(posixpath.dirname(path), target.split("#")[0]))
                if target not in paths:
                    raise ValueError("Broken document link")
        if path == "registry/server.json":
            manifest = json.loads(text)
            if manifest.get("remotes") != [{"type": "streamable-http", "url": "https://mcp.leor.cn/mcp"}]:
                raise ValueError("Registry connection changed; review required")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ref", default="HEAD")
    parser.add_argument("--base")
    args = parser.parse_args()
    refs = [args.ref]
    if args.base:
        subprocess.run(["git", "merge-base", "--is-ancestor", args.base, args.ref], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        refs.extend(git("rev-list", args.base + ".." + args.ref).decode().splitlines())
    cache = {}
    for ref in dict.fromkeys(refs):
        inspect(ref, cache)
    print("Public content safety: PASS")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, UnicodeError, subprocess.CalledProcessError):
        print("Public content safety: FAILED (unapproved content, credential, link, or history).", file=sys.stderr)
        sys.exit(1)
