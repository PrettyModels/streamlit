"""Research, financial-risk and conflict disclosures, served as a native page."""

import streamlit as st

import components as c
import content as T

st.set_page_config(
    page_title=T.DISCLOSURE_PAGE_TITLE,
    page_icon="images/logo.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)
c.inject_theme()
c.masthead(T.BRAND, T.TAGLINE, [])

st.page_link("lab.py", label=T.LEGAL_BACK)

c.eyebrow(T.DISCLOSURE_EYEBROW)
c.legal_title(T.DISCLOSURE_TITLE, T.DISCLOSURE_UPDATED)
c.lead(T.DISCLOSURE_INTRO)

for heading, paragraphs in T.DISCLOSURE_SECTIONS:
    c.legal_section(heading, paragraphs)

c.hairline()
st.page_link("lab.py", label=T.LEGAL_BACK)
