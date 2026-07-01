import streamlit as st
# streamlit run streamlit_app.py

lab_page = st.Page("lab.py", title="PrettyModels AI — Research Lab", default=True)
imprint_page = st.Page("legal_imprint.py", title="Legal Notice",
                       url_path="legal-notice")
privacy_page = st.Page("legal_privacy.py", title="Privacy Policy",
                       url_path="privacy-policy")

pg = st.navigation([lab_page, imprint_page, privacy_page], position="hidden")
pg.run()
