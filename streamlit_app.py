import streamlit as st
# streamlit run streamlit_app.py


marylin_page = st.Page("marylin.py", title="PrettyModels AI")
# test_page = st.Page("test_page.py", title="Test Page")

pg = st.navigation([marylin_page])


if False:
    with st.sidebar:
        st.header("PrettyModels.ai")
        st.subheader("Advanced AI/ML models for public markets.")
        st.text("text")

pg.run()
