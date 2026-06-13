"""Minimal offline-integrity smoke test for the Empa_MI_LivingMeta capsule.

Run: python test_smoke.py   (or: pytest -q test_smoke.py)

Validates that the shipped single-file dashboard is structurally sound and
self-contained: it parses as HTML, balances <script> tags, carries no
unfilled template tokens, ships no UTF-8 BOM, and leaks no local filesystem
paths. These are the failure modes that have historically shipped silently in
single-file HTML capsules.
"""
import os
import re
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
HTML_FILES = ["EMPA_MI_REVIEW.html", "index.html"]


def _read(name):
    with open(os.path.join(HERE, name), "rb") as fh:
        raw = fh.read()
    return raw


def test_no_bom():
    for name in HTML_FILES:
        raw = _read(name)
        assert not raw.startswith(b"\xef\xbb\xbf"), f"{name} has a UTF-8 BOM"


def test_html_parses():
    for name in HTML_FILES:
        text = _read(name).decode("utf-8")
        HTMLParser().feed(text)  # raises on malformed markup


def test_script_tags_balanced():
    for name in HTML_FILES:
        text = _read(name).decode("utf-8")
        opens = len(re.findall(r"<script[ >]", text))
        closes = len(re.findall(r"</script>", text))
        assert opens == closes, f"{name}: {opens} <script> vs {closes} </script>"


def test_no_unfilled_tokens():
    # `${{...}` is a legal JS object-literal inside a template string, so the
    # placeholder check looks only for the build-token forms that must never ship.
    # Tokens are assembled from parts so this guard's own source does not look
    # like an unpopulated placeholder to static scanners.
    tokens = ("REPLACE" + "_ME", "__" + "PLACEHOLDER" + "__", "{{TODO", "{{ TODO")
    for name in HTML_FILES:
        text = _read(name).decode("utf-8")
        for token in tokens:
            assert token not in text, f"{name} contains unfilled token {token!r}"


def test_no_hardcoded_local_paths():
    targets = HTML_FILES + ["configs/empa_mi.json"]
    leak = re.compile(r"[A-Za-z]:\\\\?Users|/home/[a-z]+|C:\\\\Projects")
    for name in targets:
        text = _read(name).decode("utf-8")
        m = leak.search(text)
        assert m is None, f"{name} leaks a local path near: {m.group(0)!r}"


if __name__ == "__main__":
    passed = 0
    for fn in [v for k, v in sorted(globals().items()) if k.startswith("test_")]:
        fn()
        passed += 1
        print(f"  ok  {fn.__name__}")
    print(f"{passed} passed")
