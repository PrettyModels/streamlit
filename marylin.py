import altair as alt
import pandas as pd
import streamlit as st

# Show the page title and description.
# st.set_page_config(page_title="Marylin", page_icon="images/logo.png", layout="wide")

st.title("PrettyModels AI - Marylin")
st.write(
    """
    This app visualizes data from [Marylin](https://docs.prettymodels.ai/public-investment-ai/marylin).
    It shows 100% AI-based assessments of many stocks. 

    Just click on the widgets below to explore!
    """
)

st.logo("images/logo.png", size="large")


# Load the data from a CSV. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    # data contains AI-generated scores for stocks to support high-alpha portfolio creation
    df = pd.read_csv("data/full_weights - full.csv")
    df.set_index("Asset", inplace=True, drop=True)
    df = df.sort_values("w", ascending=False)
    df['Rank'] = df['w'].rank(ascending=False)
    cols = df.columns.tolist()                     # get current column order
    cols.insert(0, cols.pop(cols.index("Rank")))   # remove "Rank" and re-insert at pos 2
    df = df[cols]                                  # reindex the DataFrame’s columns
    df.columns = df.columns.str.replace(' Score100', '', regex=False)
    df['Tenbagger'] = df['Tenbagger Probability100'].rank(pct=True)
    df['Growth'] = df["Growth Rate100"].rank(pct=True)
    df['Return'] = df["Return100"].rank(pct=True)
    cols2drop = ['Tenbagger Probability100', "Growth Rate100", "Return100", "iKelly-weight", "t-value"]
    df.drop(cols2drop, axis=1, inplace=True)
    df.rename(columns={"Alpha": "Alpha (vs. Tech)"}, inplace=True)

    return df


df = load_data()

# Show a multiselect widget with the genres using `st.multiselect`.

scores = st.multiselect(
    "Scores",
    sorted(set(df.columns).symmetric_difference(["w", "Rank", "hard-sell"])),
    ["Alpha (vs. Tech)", "Valuation", "Risk"],
)

# Show a slider widget with the years using `st.slider`.
max_rank = df["Rank"].max()
ranks = st.slider("Rank", 1, min(50, int(max_rank)), (1, 10))

# Filter the dataframe based on the widget input and reshape it.
cols = ["Rank"] + list(scores)
df_filtered = df.loc[df["Rank"].between(ranks[0], ranks[1]), cols]


# Display the data as a table using `st.dataframe`.
d_column_config = {col: st.column_config.NumberColumn(col, format="percent") for col in scores}
d_column_config["Rank"] = st.column_config.NumberColumn("Rank", format="plain")

# Dataframe
st.dataframe(
    df_filtered.style.highlight_max(axis=0, subset=scores, color="green"),
    use_container_width=True,
    column_config=d_column_config,
)

# Cumulative Score Chart
st.header("Cumulative Score")

# Bar Chart
# st.bar_chart(data=df_filtered, y=list(scores))

# Altair Chart Approach
df = df_filtered.copy()
df["Asset"] = df.index
if len(scores) == 0:
    scores = ["Rank"]
    df["Rank"] = 1 / df["Rank"]

# Compute row sums and sort
df['row_sum'] = df[scores].sum(axis=1)
df = df.sort_values('row_sum', ascending=False)

# Melt the DataFrame to long format for Altair
df_long = df.melt(id_vars=['Asset'], value_vars=scores,
                  var_name='Metric', value_name='Sum of Scores')

# Altair bar chart with fixed x-axis order
order = df['Asset'].tolist()

chart = alt.Chart(df_long).mark_bar().encode(
    x=alt.X('Asset:N', sort=order),
    y='Sum of Scores:Q',
    color='Metric:N'
).properties(width=600)

st.altair_chart(chart, use_container_width=True)

# Wikifolio Performance
# with st.expander("Click to see Wikifolio"):
show_section = st.checkbox("Check real-world portfolio")

if show_section:
    #st.balloons()
    st.toast('Thank you for investing $100!', icon='😍')
    st.header("Wikifolio Performance")

    st.markdown("Statistics of real-world Wikifolio: [Marylin](https://www.wikifolio.com/en/int/w/wfmarylin1)")

    a, b, c = st.columns(3)
    a.metric("Alpha (since Inception)", "1%", "1% (April-May 2025)", border=True)
    b.metric("Number of Holdings", "19", "6 (April-May 2025)", border=True)
    c.metric("Number of Trades", "110", "19 (April-May 2025)", border=True)

# Disclaimer

st.divider()  # 👈 Draws a horizontal rule

st.badge(label="**Version:** Marylin 1.1.2 (as of 2025-05-04)", icon=None, color="green")

st.caption(
    """
    This content has been generated using artificial intelligence (AI) models and is intended for informational purposes only.
    While every effort has been made to ensure the accuracy and reliability of the information provided, PrettyModels.ai and its affiliates make no representations or warranties, either express or implied, about the completeness, timeliness, or suitability of the information contained herein.
    
    The investment strategies and recommendations outlined in this report are based on proprietary algorithms and data inputs from leading large language models (LLMs).
    However, past performance is not indicative of future results, and all investments carry inherent risks, including potential loss of principal.
    Readers should not consider this content as personalized investment advice or as an endorsement of any specific securities or strategies.

    PrettyModels.ai disclaims any responsibility or liability for any actions taken based on the information contained in this report.
    PrettyModels.ai disclaims any responsibility or liability for any actions taken based on the information contained in this report.
    Investors are strongly advised to conduct their own research, consult with financial professionals, and carefully consider their own financial circumstances before making any investment decisions.

    This content is confidential and intended solely for the recipient's internal use.
    Unauthorized distribution, replication, or use of this content in whole or in part is strictly prohibited.
    By accessing or using this content, the recipient acknowledges and accepts these terms.

    """
)

