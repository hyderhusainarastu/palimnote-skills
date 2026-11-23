#!/usr/bin/env python3
"""Check that every github.com link in README.md resolves (HTTP 200).

--list  print the links and exit without any network call.
"""
import re, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def links(text):
    found = re.findall(r"https://github\.com/[A-Za-z0-9._/-]+", text)
    return sorted({u.rstrip(".,)") for u in found})

def status(url, opener=urllib.request.urlopen):
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "link-check"})
    try:
        with opener(req, timeout=20) as r:
            return r.status
    except Exception as e:  # noqa: BLE001
        return getattr(e, "code", 0)

def main(argv):
    urls = links((ROOT / "README.md").read_text())
    if "--list" in argv:
        print("\n".join(urls))
        return 0
    bad = [(u, s) for u in urls if (s := status(u)) != 200]
    for u, s in bad:
        print(f"{s}\t{u}")
    print(f"{len(urls)} links, {len(bad)} not 200")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
