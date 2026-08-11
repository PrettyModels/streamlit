"""Crawler metadata assembled from the site's existing public copy.

This module does not introduce website copy. It maps the four existing
Streamlit documents to their current titles, descriptions and raw-HTML fallback
text for the generated Nginx configuration.
"""

import content as T


SITE_URL = "https://www.prettymodels.ai"
SITE_UPDATED_ISO = "2026-08-11"
AUTHOR_NAME = "Christian Tausch"
AUTHOR_URL = f"{SITE_URL}/legal-notice"

ROUTES = [
    {
        "path": "/",
        "title": T.PAGE_TITLE,
        "description": T.PAGE_DESCRIPTION,
        "heading": T.HERO_HEADLINE,
        "summary": T.HERO_LEAD,
        "fallback_paragraphs": [T.METHOD_INTRO, T.VALIDATION_NOTE],
        "lastmod": SITE_UPDATED_ISO,
    },
    {
        "path": "/research-disclosures",
        "title": T.DISCLOSURE_PAGE_TITLE,
        "description": T.DISCLOSURE_INTRO,
        "heading": T.DISCLOSURE_TITLE,
        "summary": T.DISCLOSURE_INTRO,
        "fallback_paragraphs": [T.DISCLOSURE_SECTIONS[2][1][0]],
        "lastmod": SITE_UPDATED_ISO,
    },
    {
        "path": "/legal-notice",
        "title": T.IMPRINT_PAGE_TITLE,
        "description": T.IMPRINT_INTRO,
        "heading": T.IMPRINT_TITLE,
        "summary": T.IMPRINT_INTRO,
        "fallback_paragraphs": [],
        "lastmod": SITE_UPDATED_ISO,
    },
    {
        "path": "/privacy-policy",
        "title": T.PRIVACY_PAGE_TITLE,
        "description": T.PRIVACY_INTRO,
        "heading": T.PRIVACY_TITLE,
        "summary": T.PRIVACY_INTRO,
        "fallback_paragraphs": [],
        "lastmod": SITE_UPDATED_ISO,
    },
]
