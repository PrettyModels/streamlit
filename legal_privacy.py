"""
legal_privacy.py — Privacy policy, served as a native page.

Replaces the retired docs.prettymodels.ai privacy-policy page. Copy lives in
content.py; the design system (theme + render helpers) in components.py.
"""
import streamlit as st

import components as c
import content as T

st.set_page_config(
    page_title=T.PRIVACY_PAGE_TITLE,
    page_icon=T.PAGE_ICON,
    layout="wide",
    initial_sidebar_state="collapsed",
)
c.inject_theme()
c.masthead(T.BRAND, T.TAGLINE, [])

st.page_link("lab.py", label=T.LEGAL_BACK)

c.eyebrow(T.PRIVACY_EYEBROW)
c.legal_title(T.PRIVACY_TITLE, T.PRIVACY_UPDATED)
c.lead(T.PRIVACY_INTRO)

for heading, paragraphs in T.PRIVACY_SECTIONS:
    c.legal_section(heading, paragraphs)

c.hairline()
st.page_link("lab.py", label=T.LEGAL_BACK)
