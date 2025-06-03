# wishlist.py
import streamlit as st
import pandas as pd
import datetime, os
import altair as alt

def wishlist():
    """
    Streamlit app to collect user wishlist for stock analysis.
    Users can select from a predefined list or enter custom tickers.
    Votes are saved to a CSV file for persistence.
    """

    # ---- 1. CONFIG -------------------------------------------------------------
    ASSETS = [
        "Palantir", "Broadcom", "Cloudflare", "Tencent", "Hermes", "Crowdstrike",
        "Microsoft", "Coinbase", "First Solar", "DigitalOcean", "MicroStrategy",
        "Uber", "Salesforce", "Reliance", "Booking", "Baidu", "Alibaba",
        "Paypal", "Ferrari", "Berkshire Hathaway", "LVMH", "Tesla",
    ]                              # <-- your predefined list
    @st.cache_data
    def load_data():
        # data contains AI-generated scores for stocks to support high-alpha portfolio creation
        df = pd.read_csv("data/full_weights - full.csv")
        df = df[df["w"] == 0]
        df = df[df["Valuation Score100"] >= 0]
        return df
    
    df = load_data()
    # st.dataframe(df)
    ASSETS = list(df["Asset"])
    DATAFILE = "wishlist_votes.csv"          # simple persistence for a PoC

    # ---- 2. FORM ---------------------------------------------------------------
    st.header("📊  Tell us which stocks you'd like us to analyze")

    with st.form("wishlist_form", clear_on_submit=True):
        picks   = st.multiselect("Choose as many as you like", ASSETS)
        other = ""
        # other   = st.text_input("Other tickers (comma-separated)")
        submit  = st.form_submit_button("Submit")

    # ---- 3. SAVE & ACK ---------------------------------------------------------
    if submit:
        # Normalise the free-text field
        extra = [
            x.strip().upper() for x in other.split(",")
            if x.strip() and x.strip().upper() not in ("OTHER", ",")
        ]
        wishlist = picks + extra
        if not wishlist:
            st.warning("Please select at least one ticker 😊")
            st.stop()

        # Append to CSV (replace with DB in prod)
        row = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "user": st.session_state.get("user_id", "anon"),
            "ticker": wishlist
        }
        # Flatten into one row per ticker
        df = pd.DataFrame(
            [{"timestamp": row["timestamp"], "user": row["user"], "ticker": t}
            for t in row["ticker"]]
        )
        df.to_csv(DATAFILE, mode="a",
                header=not os.path.exists(DATAFILE), index=False)

        st.success("Thanks for the feedback! 🎉")

    # ---- 4. OPTIONAL: DASHBOARD -----------------------------------------------
    if st.checkbox("Show live vote counts"):
        if os.path.exists(DATAFILE):
            counts = (pd.read_csv(DATAFILE)
                        .groupby("ticker").size().sort_values(ascending=False))
            counts = pd.DataFrame(counts).reset_index()
            counts.rename(columns={0: 'votes'}, inplace=True)

            chart = alt.Chart(counts).mark_bar(color='#FF4B4B').encode(
                x=alt.X('ticker:O', title=None),
                y='votes'
            )
            st.altair_chart(chart, use_container_width=True)
        else:
            st.info("No votes yet.")
