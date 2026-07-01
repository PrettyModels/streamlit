import streamlit as st
# streamlit run streamlit_app.py

lab_page = st.Page("lab.py", title="PrettyModels AI — Research Lab")

pg = st.navigation([lab_page], position="hidden")
pg.run()
