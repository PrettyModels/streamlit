"""
legal_imprint.py — Legal notice / Impressum (§ 5 DDG), served as a native page.

Replaces the retired docs.prettymodels.ai legal-notice page. Copy lives in
content.py; the design system (theme + render helpers) in components.py.
"""
import streamlit as st

import components as c
import content as T

st.set_page_config(
    page_title=T.IMPRINT_PAGE_TITLE,
    page_icon=T.PAGE_ICON,
    layout="wide",
    initial_sidebar_state="collapsed",
)
c.inject_theme()
c.masthead(T.BRAND, T.TAGLINE, [])

st.page_link("lab.py", label=T.LEGAL_BACK)

c.eyebrow(T.IMPRINT_EYEBROW)
c.legal_title(T.IMPRINT_TITLE, T.IMPRINT_UPDATED)
c.lead(T.IMPRINT_INTRO)

for heading, paragraphs in T.IMPRINT_SECTIONS:
    c.legal_section(heading, paragraphs)

c.hairline()
st.page_link("lab.py", label=T.LEGAL_BACK)
