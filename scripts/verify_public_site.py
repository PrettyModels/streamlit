"""Verify the deployed crawler contract using only the Python standard library.

Example:
    python3 scripts/verify_public_site.py https://www.prettymodels.ai
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import seo_config as S  # noqa: E402


class HeadParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self._in_title = False
        self.meta: dict[tuple[str, str], str] = {}
        self.links: dict[str, str] = {}
        self.json_ld: list[dict] = []
        self._in_json_ld = False
        self._json_chunks: list[str] = []
        self.h1: list[str] = []
        self._in_h1 = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "meta" and values.get("content"):
            for key in ("name", "property"):
                if values.get(key):
                    self.meta[(key, values[key] or "")] = values["content"] or ""
        elif tag == "link" and values.get("rel") and values.get("href"):
            self.links[values["rel"] or ""] = values["href"] or ""
        elif tag == "script" and values.get("type") == "application/ld+json":
            self._in_json_ld = True
            self._json_chunks = []
        elif tag == "h1":
            self._in_h1 = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        elif tag == "script" and self._in_json_ld:
            self._in_json_ld = False
            self.json_ld.append(json.loads("".join(self._json_chunks)))
        elif tag == "h1":
            self._in_h1 = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data
        if self._in_json_ld:
            self._json_chunks.append(data)
        if self._in_h1 and data.strip():
            self.h1.append(data.strip())


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: ANN001
        return None


def _request(url: str, *, redirects: bool = True) -> tuple[int, str, bytes, dict]:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "User-Agent": "PrettyModels deployment verifier/1.0",
        },
    )
    opener = urllib.request.build_opener() if redirects else urllib.request.build_opener(NoRedirect)
    try:
        with opener.open(request, timeout=20) as response:
            return response.status, response.headers.get_content_type(), response.read(), dict(response.headers)
    except urllib.error.HTTPError as exc:
        return exc.code, exc.headers.get_content_type(), exc.read(), dict(exc.headers)


def verify(base_url: str) -> list[str]:
    failures: list[str] = []
    base = base_url.rstrip("/")

    for route in S.ROUTES:
        url = base + route["path"]
        status, content_type, body, _ = _request(url)
        if status != 200:
            failures.append(f"{route['path']}: expected 200, got {status}")
            continue
        if content_type != "text/html":
            failures.append(f"{route['path']}: expected text/html, got {content_type}")
            continue
        parser = HeadParser()
        parser.feed(body.decode("utf-8", errors="replace"))
        expected_canonical = base + route["path"]
        checks = {
            "title": (parser.title.strip(), route["title"]),
            "description": (parser.meta.get(("name", "description")), route["description"]),
            "robots": (
                parser.meta.get(("name", "robots")),
                "index, follow, max-image-preview:large, max-snippet:-1",
            ),
            "canonical": (parser.links.get("canonical"), expected_canonical),
            "og:url": (parser.meta.get(("property", "og:url")), expected_canonical),
        }
        for label, (actual, expected) in checks.items():
            if actual != expected:
                failures.append(f"{route['path']}: {label} is {actual!r}, expected {expected!r}")
        if not parser.h1 or route["heading"] not in parser.h1:
            failures.append(f"{route['path']}: prerender H1 missing")
        if not parser.json_ld:
            failures.append(f"{route['path']}: JSON-LD missing")
        if b'id="pm-prerender"' not in body:
            failures.append(f"{route['path']}: server-visible fallback missing")

    asset_expectations = {
        "/robots.txt": "text/plain",
        "/sitemap.xml": "application/xml",
        "/favicon.ico": "image/x-icon",
        "/site.webmanifest": "application/manifest+json",
        "/app/static/social-preview-v2.png": "image/png",
        "/app/static/research-hero.webp": "image/webp",
    }
    for path, expected_type in asset_expectations.items():
        status, content_type, body, _ = _request(base + path)
        if status != 200 or content_type != expected_type or not body:
            failures.append(
                f"{path}: expected 200 {expected_type} with a body; "
                f"got {status} {content_type} ({len(body)} bytes)"
            )

    status, _, _, _ = _request(base + "/this-route-must-not-exist")
    if status != 404:
        failures.append(f"unknown route: expected 404, got {status}")

    for route in S.ROUTES:
        if route["path"] == "/":
            continue
        status, _, _, headers = _request(base + route["path"] + "/", redirects=False)
        expected_location = route["path"]
        location = headers.get("Location") or headers.get("location")
        if status not in (301, 308) or location != expected_location:
            failures.append(
                f"{route['path']}/: expected permanent redirect to {expected_location}; "
                f"got {status} {location!r}"
            )

    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("base_url", nargs="?", default=S.SITE_URL)
    args = parser.parse_args()
    failures = verify(args.base_url)
    if failures:
        print("Public SEO verification failed:", file=sys.stderr)
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)
        return 1
    print(f"Public SEO verification passed for {args.base_url.rstrip('/')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
