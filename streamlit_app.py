import altair as alt
import pandas as pd
import streamlit as st


marylin_page = st.Page("marylin.py", title="Marylin")
test_page = st.Page("test_page.py", title="Test Page")

pg = st.navigation([marylin_page])

# Show the page title and description.
st.set_page_config(page_title="Marylin", page_icon="images/logo.png", layout="wide")

if False:
    with st.sidebar:
        st.header("PrettyModels.ai")
        st.subheader("Advanced AI/ML models for public markets.")
        st.text("text")

pg.run()
