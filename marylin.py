import os
import time
import altair as alt
import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# streamlit run marylin.py

# Show the page title and description.
# st.set_page_config(page_title="Marylin", page_icon="images/logo.png", layout="wide")
# st.set_page_config(page_title="PrettyModels AI", page_icon="images/logo.png", layout="wide")

# 1. Page Configuration
st.set_page_config(
    page_title="PrettyModels AI | Beat the Market",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to make it look more like a landing page and less like a data app
st.markdown("""
<style>
    .main-header {font-size: 3rem; font-weight: 700; color: #483ae0; margin-bottom: 0px;}
    .sub-header {font-size: 1.5rem; color: #4F4F4F; margin-bottom: 2rem;}
    .highlight {color: #FF4B4B; font-weight: bold;}
    .block-container {padding-top: 2rem; padding-bottom: 5rem;}
</style>
""", unsafe_allow_html=True)

st.logo("images/logo.png", size="large")

st.title("PrettyModels AI")
#st.header("Advanced AI models for public equity investors.")
#st.markdown('<div class="main-header">Advanced AI models for asset management.</div>', unsafe_allow_html=True)
st.markdown('<div class="main-header">Don’t Settle for Average Returns.</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-header">Beat the market with an AI investment manager that compounds your wealth faster than ETFs.</div>',
    unsafe_allow_html=True)

if False:
    text = "Don’t Settle for Average Returns."

    placeholder = st.empty()
    rendered = ""

    for ch in text:
        rendered += ch
        placeholder.markdown(
            f'<div class="main-header">{rendered}</div>',
            unsafe_allow_html=True
        )
        time.sleep(0.03)  # adjust speed

    text = "Beat the market with an AI investment manager that compounds your wealth faster than ETFs."

    placeholder = st.empty()
    rendered = ""

    for ch in text:
        rendered += ch
        placeholder.markdown(
            f'<div class="sub-header">{rendered}</div>',
            unsafe_allow_html=True
        )
        time.sleep(0.01)



@st.cache_data
def load_perf_data():
    df = pd.read_csv(
        "data/marylin_performance.csv",
        sep=";",
        decimal=",",
        parse_dates=["Date"],
        dayfirst=True,
        date_format="%d.%m.%y",
    )
    df.set_index("Date", inplace=True)
    df = df[(df.index.is_month_end) + (df.index == pd.to_datetime('2024-12-27'))]
    return df


df_mape = load_perf_data()

if True:
    col1, col2 = st.columns([1, 1])  # Adjust the ratios if needed

    if True:
        with col2:
            st.markdown("#### ✔️ Outperform your public benchmark")
            st.markdown("#### ✔️ Based on tailored AI-driven strategies")
            st.markdown("#### ✔️ With proven public market track record")

    with col1:
        # st.image("images/sisters14.png", width='stretch')
        # Marylin's Out-Performance

        # If you have multiple performance columns (e.g. 'Rate', 'Growth', ...)
        # they’ll all be melted into a single 'Metric' + 'Value' column.
        perf_cols = df_mape.columns.tolist()
        chart_df = (
            df_mape
            .reset_index()
            .melt(id_vars=["Date"], value_vars=perf_cols,
                  var_name="Metric", value_name="Value")
        )

        # Build the Altair chart:
        chart = (
            alt.Chart(chart_df)
            .mark_line(point=alt.OverlayMarkDef(size=10), strokeWidth=6, strokeCap="round", color="red")
            .encode(
                x=alt.X("Date:T", axis=alt.Axis(labels=False, grid=False), title=""),
                y=alt.Y("Value:Q", axis=alt.Axis(format="%", labels=False, grid=False), title=""),
                color=alt.Color("Metric:N",
                                legend=None,
                                scale=alt.Scale(
                                    range=["#00FFC6", "#ff1fc7", "#483ae0"],
                                    #range=["#FB0A26", "#F50A1C", "#E60000"],
                                    #range=["#007BFF", "#0057D8", "#1E9CE6"]
                                    )
                                ),
                tooltip=[
                    alt.Tooltip("Date:T", title="Date"),
                    alt.Tooltip("Metric:N", title="Benchmark"),
                    alt.Tooltip("Value:Q", format=".1%", title="Alpha")
                ]
            )
            .properties(width=700, height=400)
        )

        # Add a dashed grey horizontal line at y = 0
        zero_line_data = pd.DataFrame({"y": [0], "label": ["market"]})

        # 2. Define the Rule (The grey dashed line)
        rule = (
            alt.Chart(zero_line_data)
            .mark_rule(color="grey", strokeWidth=2)
            .encode(y="y:Q")
        )

        # 3. Define the Text (The label on the right)
        text = (
            alt.Chart(zero_line_data)
            .mark_text(
                align="right",  # Anchors the text to its right edge
                dx=-5,  # Nudges it 5 pixels to the left so it's not touching the border
                dy=14,  # Nudges it 10 pixels above the line
                fontSize=20,
                fontWeight="bold",
                color="grey"
            )
            .encode(
                y="y:Q",
                x=alt.value(510),  # Positions it at the 700px mark (your chart width)
                text="label:N"
            )
        )

        # Combine the main chart with the combined zero elements
        final_chart = chart + rule + text

        st.altair_chart(final_chart, use_container_width=True)



# Text


col1, col2, = st.columns([1, 1])
with col1:
    st.markdown("# Our mission is simple.")
with col2:
    st.markdown("# Beat the market with AI.")

st.markdown("##### _Most investors are stuck in the slow lane with standard ETFs. At PrettyModels AI, we use advanced algorithms to remove human bias and outperform the market, so you can build meaningful wealth faster without the stress of managing it yourself._")

if True:
    col1, col2, = st.columns([1, 1])
    with col1:
        st.image("images/info2-bg.png", width='stretch')
    with col2:
        st.image("images/info-bg.png", width='stretch')




#  MARYLIN


with st.expander("Real-World Performance", icon="📈", expanded=True):
    #st.balloons()
    #st.toast('Thank you for investing!', icon='😍')
    #st.divider()
    st.markdown("# MARYLIN PORTFOLIO")
    #st.header("Wikifolio Performance", divider=False)

    col1, col2, col3 = st.columns([1, 2, 1])  # Adjust the ratios if needed
    with col2:
        st.image("images/marylin6.png", width='stretch')
    with col1:
        # st.markdown("##### Marylin is our first **PrettyModels AI** release. She pursues a bold, growth-aggressive investment style derived from her goal to outperform the market in a _growth-optimal_ way. She is willing to take high risks to kick-start her wealth generation in young years.")
        st.markdown("##### Marylin is our first **PrettyModels AI** release.")
        st.markdown("##### She pursues a high-conviction investment style.")
        st.markdown("##### Her goal is to outperform the market in a _growth-optimal_ way.")
        # st.markdown("##### She is willing to take high risks to kick-start her wealth generation in young years.")
        st.markdown("##### We track Marylin's performance by a Wikifolio since December 27, 2024.")
        #st.markdown("##### Wikifolio index certificate issued at September 2, 2025.")
        #st.markdown("##### Visit her now!")
        st.link_button("Visit Wikifolio", "https://www.wikifolio.com/en/int/w/wfmarylin1", type="primary")
        st.link_button("Read Full Story", "https://quant-unit.com/the-story-of-marylin-pt-1/")

    # st.markdown("Statistics of real-world Wikifolio: [Marylin](https://www.wikifolio.com/en/int/w/wfmarylin1)")

    # Calc annualized alpha of the df_mape Internet column for the total period and the difference to the previous period
    start_date = df_mape.index[0]
    end_date = df_mape.index[-1]
    prev_date = df_mape.index[-2]

    days_end = (end_date - start_date).days
    days_prev = (prev_date - start_date).days

    cum_alpha_end = df_mape["Internet"].iloc[-1]
    cum_alpha_prev = df_mape["Internet"].iloc[-2]

    ann_alpha_end = (1 + cum_alpha_end) ** (365.25 / days_end) - 1
    ann_alpha_prev = (1 + cum_alpha_prev) ** (365.25 / days_prev) - 1
    ann_alpha_diff = ann_alpha_end - ann_alpha_prev

    col3.metric("Performance (Dec 2024 - April 2026)", "37.2%", "+15.2% (April 2026)", border=True)
    col3.metric("Alpha (Dec 2024 - April 2026)", "29.7%", "0.7% (April 2026)", border=True)
    #col3.metric("Number of Trades (Total)", "220", "5 (March 2026)", border=True)
    col3.metric("Alpha (Annualized)", f"{ann_alpha_end:.1%}", f"{ann_alpha_diff:+.1%} ({end_date.strftime('%B %Y')})", border=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        # Wikifolio Chart
        @st.cache_data
        def load_wikifolio_data():
            df = pd.read_csv(
                "data/WFMARYLIN1-PriceData-April2026.csv",
                sep=";",
                decimal=",",  # <-- IMPORTANT: your file uses comma decimals
            )

            # Parse the timestamp explicitly (your file is like: 27.12.24 00:00)
            df["Begin date"] = pd.to_datetime(df["Begin date"], format="%d.%m.%y %H:%M")

            df.rename(columns={"Begin date": "Date", "Close": "Marylin Index"}, inplace=True)
            df = df[["Date", "Marylin Index"]].sort_values("Date")
            return df

        df_wiki = load_wikifolio_data()

        perf_cols = df_wiki.columns.drop("Date").tolist()
        chart_df = df_wiki.melt(
            id_vars=["Date"],
            value_vars=perf_cols,
            var_name="Metric",
            value_name="Value",
        )

        # y-axis minimum = minimum of the time series (and include baseline if you want it visible)
        y_min = float(chart_df["Value"].min()) - 5
        baseline = 100.0
        y_domain_min = min(y_min, baseline)  # use y_min if you don't need the baseline line

        chart = (
            alt.Chart(chart_df)
            .mark_line(strokeWidth=3, strokeCap="round")  # <-- line only, no points
            .encode(
                x=alt.X("Date:T", title=""),
                y=alt.Y(
                    "Value:Q",
                    title="",
                    axis=alt.Axis(format=",.2f"),
                    scale=alt.Scale(domainMin=y_domain_min, nice=False, zero=False),
                ),
                color=alt.Color("Metric:N", legend=None),
                tooltip=[
                    alt.Tooltip("Date:T", title="Date"),
                    alt.Tooltip("Metric:N", title="Series"),
                    alt.Tooltip("Value:Q", format=",.2f", title="Index level"),
                ],
            )
            .properties(height=400)
        )

        zero_line = (
            alt.Chart(pd.DataFrame({"Value": [baseline]}))
            .mark_rule(color="grey", strokeDash=[4, 4], strokeWidth=2)
            .encode(y="Value:Q")
        )

        final_chart = (
            alt.layer(zero_line, chart)
            .properties(
                height=400,
                padding={"bottom": 40, "left": 10, "right": 10, "top": 10},
            )
        )

        st.markdown("### Marylin Wikifolio Index")
        st.altair_chart(final_chart, use_container_width=True)

    with col2:
        # Marylin's Out-Performance

        # If you have multiple performance columns (e.g. 'Rate', 'Growth', ...)
        # they’ll all be melted into a single 'Metric' + 'Value' column.
        perf_cols = df_mape.columns.tolist()
        chart_df = (
            df_mape
            .reset_index()
            .melt(id_vars=["Date"], value_vars=perf_cols,
                  var_name="Metric", value_name="Value")
        )

        # Build the Altair chart:
        chart = (
            alt.Chart(chart_df)
            .mark_line(point=alt.OverlayMarkDef(size=10), strokeWidth=3, strokeCap="round")
            .encode(
                x=alt.X("Date:T", title=""),
                y=alt.Y("Value:Q", axis=alt.Axis(format="%"), title=""),
                color=alt.Color("Metric:N", title="Alpha vs. ETFs:",
                                scale=alt.Scale(
                                    range=["#00FFC6", "#ff1fc7", "#483ae0"],
                                    )
                                ),
                tooltip=[
                    alt.Tooltip("Date:T", title="Date"),
                    alt.Tooltip("Metric:N", title="Benchmark"),
                    alt.Tooltip("Value:Q", format=".1%", title="Alpha")
                ]
            )
            .properties(width=700, height=400)
        )

        # Add a dashed grey horizontal line at y = 0
        zero_line = (
            alt.Chart(pd.DataFrame({"y": [0]}))
            .mark_rule(color="grey", strokeDash=[4, 4], strokeWidth=4)
            .encode(y="y:Q")
        )

        # Combine the two layers
        final_chart = chart + zero_line

        st.markdown("### Marylin's Alpha vs. ETFs")
        st.altair_chart(final_chart, use_container_width=True)


with st.expander("Manifesto", icon="📄", expanded=True):
    st.markdown("""
    ## Pretty, Models, AI
    
    True elegance in finance is rare because it requires the absolute removal of the ego. For centuries, men have tried to beat markets with gut instinct, confusing their luck with genius and their anxiety with insight. The result is always the same: a chaotic, ugly portfolio where emotions erode returns. At PrettyModels AI, we hold a different view. We believe that a financial model is only "pretty" when it is stripped of human folly, leaving behind nothing but the raw, unvarnished probability of Alpha.

    The modern financial industry has convinced the world that mediocrity is a virtue. You are told to buy the index, accept average returns, and be grateful. This is excellent advice for the fearful, the financially illiterate, and the wealthy who merely wish to stay wealthy. But for the ambitious individual with limited capital, the safety of the herd is a mathematical trap. You cannot compound a fortune by mimicking the average; to build life-changing wealth, you must deviate from the mean. You must be right when the consensus is wrong.

    The tragedy of the active investor has always been biology. We are flawed hardware, plagued by cognitive biases that no amount of discipline can fully erase. But we are currently standing at the precipice of a new epoch. We are witnessing the rise of Large Language Models—not merely as chat bots, but as the first truly "smart" statistical engines in history. These are systems that digest the chaotic noise of the world and organize it into reasoning. As we accelerate toward superintelligence, the edge in markets will no longer belong to the person who can read the most annual reports, but to the person who commands the superior statistical mind.

    The question you must ask yourself regarding the next twenty years is uncomfortable but necessary: Who is the better steward of your future? Is it "I," with all my doubts and erratic impulses? Or is it "AI," a system capable of cold, relentless execution? A pretty model does not hope, and it does not panic. It does not care about market sentiment or media narratives. It cares only about Alpha. It hunts for asymmetry with a precision no human brain can match.

    At PrettyModels AI, our philosophy is simple: the era of the gut feeling is over. We are building the architecture for high-conviction, automated intelligence because we know that the greatest risk to your wealth is your own interference. The smartest investment decision you will ever make is to stop trying to be the genius, and instead, align yourself with one. The future belongs to those who recognize that the most beautiful model is the one that simply, quietly, and ruthlessly outperforms.
    """)

    if False:
        st.markdown("""
        # Our mission is simple.
        # Beat the market with AI.

        Most investors are stuck in the slow lane with standard ETFs. At PrettyModels AI, we use advanced algorithms to remove human bias and outperform the market, so you can build meaningful wealth faster without the stress of managing it yourself.

        If you have high ambitions and less than one million Euro/Dollar, typically ETFs won't do the trick to make you rich.
        You have to consistently outperform diversified ETFs to achieve meaningful compounding of returns.
        In the long run, is outperforming ETFs an easier task for you or an AI-powered algorithm?
        In other words, who will be the better active investment manager for the next 10 or 20 years? I or AI?

        Given the current progress with LLMs, a properly designed AI-driven algorithm can help you stay committed to faster wealth generation without losing money due to human biases or emotions.
        To achieve extraordinary investment success, you presumably want to spend your time identifying the most capable AI systems than trying to pick stocks on your own.
        The smartest way to manage your wealth in the future will be to use the AI that is most aligned with you investment goals (and simply let it work for you).

        # ALLOCATION INTELLIGENCE
        ##### We build proprietary AI-powered algorithms to unlock new investment strategies.
        ##### We transform chaotic qualitative information into robust quantitative signals.
        ##### We explore different AI models to assess what really beats the market in the long run.
        ##### We aim at high-conviction strategies to create wealth faster.
        ##### We track our performance by publicly traded portfolios.

        ## Our Principles:
        ##### 🔥 **Prompted for Outperformance**
        ##### 🔥 **100% AI-Powered (LLMs)**
        ##### 🔥 **Quantitative Output**
        ##### 🔥 **Statistical Approach**
        ##### 🔥 **High Conviction**
        """)

with st.expander("Proprietary Model Data", icon="⚙️"):
    # DATA

    #st.divider()
    #st.write("Our [Allocation Intelligence](https://docs.prettymodels.ai) models provide 100% AI-powered asset assessments, custom-tailored for your unique investment universe.")
    st.markdown("# MODEL DATA")
    st.markdown("This dataset is the ❤️ of all PrettyModels AI strategies.")
    st.markdown("""
    We use AI to estimate scores for all stocks in our universe on a monthly basis.
    
    Our scores fall into five categories: 
     💞 Integrity, 📈 Market, ✨ Quality, ⛓️ Resilience, 🚀 Upside. 
     
     Feel free to take a look! You can analyze the data here via interactive charts or simply download the data table. ⬇️
    """)

    # Load the data from a CSV. We're caching this so it doesn't reload every time the app
    # reruns (e.g. if the user interacts with the widgets).
    @st.cache_data
    def load_data():
        # data contains AI-generated scores for stocks to support high-alpha portfolio creation
        df = pd.read_csv("data/full_weights - raw.csv")
        df.set_index("Asset", inplace=True, drop=True)
        df = df.sort_values("w", ascending=False)
        df.columns = df.columns.str.replace(' Score100', '', regex=False)
        df['Tenbagger'] = df['Tenbagger Probability100'].rank(pct=True)
        df['Growth'] = df["Growth Rate100"].rank(pct=True)
        df['Return'] = df["Return100"].rank(pct=True)
        df['Bankruptcy'] = df["Bankruptcy"].rank(pct=True)
        cols2drop = ['Tenbagger Probability100', "Growth Rate100", "Return100", "iKelly-weight", "t-value"]
        df.drop(cols2drop, axis=1, inplace=True)
        dict_rename = {"Alpha": "Alpha (vs. Tech)",
                       "Market Disruptor": "Disruptor",
                       "Good Governance": "Governance",
                       "Good Business": "Business",
                       "Future Moat": "Moat",
                       }
        df.rename(columns=dict_rename, inplace=True)
        # df = df[df["w"] > 0]
        df.dropna(axis=0, how='any', inplace=True)
        df['Rank'] = df['w'].rank(ascending=False)

        # Final Filter
        cols = [c for c in df.columns if "Cat-" in c] + ["w", "Rank"]
        cols = [c for c in cols if "Cat-XXX" not in c]
        df = df[cols]
        dict_rename = {c: c.replace("Cat-","") for c in df.columns if "Cat-" in c}
        df = df.rename(columns=dict_rename)

        return df


    df_data = load_data()

    d_column_config = {col: st.column_config.NumberColumn(col, format="percent") for col in df_data.columns}

    # Dataframe
    st.dataframe(
        df_data.drop(columns=["Rank", "w"]).sort_index().style.highlight_max(axis=0, color="green"),
        width='stretch',
        column_config=d_column_config,
    )

    def make_bar_chart(df, scores, id_vars):
        # Altair Chart Approach
        # df = df_filtered.copy()

        df["Asset"] = df.index
        if len(scores) == 0:
            scores = ["Rank"]
            df["Rank"] = 1 / df["Rank"]

        # Compute row sums and sort
        df['row_sum'] = df[scores].sum(axis=1)
        df = df.sort_values('row_sum', ascending=False)

        # Melt the DataFrame to long format for Altair
        df_long = df.melt(id_vars=id_vars, value_vars=scores,
                        var_name='Score', value_name='Score Value')

        # Altair bar chart with fixed x-axis order
        order = df['Asset'].tolist()

        chart = alt.Chart(df_long).mark_bar().encode(
            x=alt.X('Asset:N', sort=order, axis=alt.Axis(title=None)),
            y=alt.Y('Score Value:Q', axis=alt.Axis(title=None)),
            color='Score:N'
        ).properties(width=600)

        st.altair_chart(chart, use_container_width=True)


    # Define all scores available in the dataset.
    all_scores = sorted(set(df_data.columns).symmetric_difference(["w", "Rank"]))


    # Make Tabs
    tab0, tab1, tab2 = st.tabs(["Asset Analyzer", "Compare Companies", "Select Scores"])


    with tab0:
        company = st.selectbox(
        "Which asset do you want to analyze?",
        sorted(set(df_data.index)),
        )

        s = df_data.loc[company,all_scores].copy()

        # Convert Series to DataFrame
        df1 = s.reset_index()
        company = company.replace(",", " ").replace(".", "-")
        df1.columns = ['Score', company]
        df1.sort_values(by=company, ascending=False, inplace=True)

        # compute min/max (optional if you know the domain already)
        min_score, max_score = df1[company].min(), df1[company].max()
        min_score = 0
        max_score = 1

        # Create Altair chart with color gradient
        chart = alt.Chart(df1).mark_bar().encode(
            x=alt.X('Score:N', sort='-y', axis=alt.Axis(title=None)),
            y=alt.Y(f'{company}:Q', axis=alt.Axis(title=None), scale=alt.Scale(domain=[0, 1])),
            color=alt.Color(
                f'{company}:Q',
                scale=alt.Scale(
                    domain=[min_score, max_score],     # data range
                    range=['red', 'green']             # low→high colors
                ),
                legend=alt.Legend(title=None)
            )
        )

        st.altair_chart(chart, use_container_width=True)

        # Wishlist
        # wishlist()


    with tab1:
        # Show a multiselect widget with the genres using `st.multiselect`.
        default_companies = df_data.nlargest(6, 'w').sort_index().index

        companies = st.multiselect(
            "Companies",
            sorted(set(df_data.index)),
            default_companies,
        )

        # Filter the dataframe based on the widget input and reshape it.
        df_filtered = df_data.loc[companies, :].copy()
        df_filtered.drop(columns=["w", "Rank"], inplace=True)

        if False:
            # Display the data as a table using `st.dataframe`.
            d_column_config = {col: st.column_config.NumberColumn(col, format="percent") for col in df_filtered.columns}

            # Dataframe
            st.dataframe(
                df_filtered.style.highlight_max(axis=0, subset=all_scores, color="green"),
                width='stretch',
                column_config=d_column_config,
            )

        # Cumulative Score Chart
        st.header("Cumulative Score")

        # Bar Chart
        # st.bar_chart(data=df_filtered, y=list(scores))
        scores1 = sorted(set(df_filtered.columns))
        make_bar_chart(df=df_filtered.copy(), scores=scores1, id_vars=["Asset"])


    with tab2:
        # Show a multiselect widget with the genres using `st.multiselect`.
        scores = st.multiselect(
            "Scores",
            all_scores,
            all_scores,
        )

        # Show a slider widget with the years using `st.slider`.
        max_rank = df_data["Rank"].max()
        ranks = st.slider("Rank", 1, min(500, int(max_rank)), (1, 10))

        # Filter the dataframe based on the widget input and reshape it.
        cols = ["Rank"] + list(scores)
        df_filtered = df_data.loc[df_data["Rank"].between(ranks[0], ranks[1]), cols]


        if False:
            # Display the data as a table using `st.dataframe`.
            d_column_config = {col: st.column_config.NumberColumn(col, format="percent") for col in scores}
            d_column_config["Rank"] = st.column_config.NumberColumn("Rank", format="plain")

            # Dataframe
            st.dataframe(
                df_filtered.style.highlight_max(axis=0, subset=scores, color="green"),
                width='stretch',
                column_config=d_column_config,
            )

        # Cumulative Score Chart
        st.header("Cumulative Score")

        # Bar Chart
        # st.bar_chart(data=df_filtered, y=list(scores))
        make_bar_chart(df=df_filtered.copy(), scores=scores, id_vars=["Asset"])

        # Heatmap with PCA

        if len(scores) > 1:
            st.header("Principal Component Analysis")

            # 1) Select only numeric score columns (drop 'w' and 'hard-sell')
            pca_features = df_filtered.drop(columns=["Rank"]).columns.tolist()
            X = df_filtered[pca_features].dropna().copy()

            # 2) Standardize
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)

            # 3) Fit PCA (one component per feature)
            n_comp = min(len(df_filtered), len(pca_features))

            n_comp = st.slider("Number of Principal Components", 1, n_comp, n_comp)

            pca = PCA(n_components=n_comp)
            pca.fit(X_scaled)

            # 4) Build loadings DataFrame (index=original features, columns=PC1, PC2, ...)
            pcs = [f"PC {i+1}" for i in range(n_comp)]
            loadings = pd.DataFrame(
                pca.components_.T,
                index=pca_features,
                columns=pcs,
            )

            # 5) Altair Heatmap
            df_long = loadings.reset_index().melt(id_vars='index')
            df_long.columns = ['Scores', 'PCAs', 'Value']

            # Create Altair heatmap chart
            chart = alt.Chart(df_long).mark_rect().encode(
                x=alt.X('PCAs:O', title=None),
                y=alt.Y('Scores:O', title=None),
                color=alt.Color('Value:Q', scale=alt.Scale(scheme='reds')),
                tooltip=['PCAs', 'Scores', 'Value']
            ).properties(
                width=300,
                height=300
            )

            st.altair_chart(chart, use_container_width=True)


if False:
    # Contact Form
    col1, col2, col3 = st.columns([1, 2, 1])  # Adjust the ratios if needed


    with col2:
        st.markdown("# Wanna talk to us?")
        st.markdown("""
        ### We always can have a chat about models, data, customization and more!
        """)

        # Crisp Chatbot Integration
        chat_url = "https://go.crisp.chat/chat/embed/?website_id=4a5016c9-b741-4e78-a0df-793321048d6b"

        if st.button("Open Live Chat"):
            st.components.v1.iframe(
                src=chat_url,
                height=400,
                scrolling=True,
                #sandbox="allow-scripts allow-same-origin"
            )

# with st.expander("Slides", icon="📂"):
#     st.pdf("2025 PM Slides.pdf", height=500)

if False:
    # The Poetry of Kong

    # File path
    file_path = "data/hong.txt"

    # Check if file exists and read it
    if os.path.exists(file_path):

        try:
            # Read the file content
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # Display content in expander with code formatting
            #with st.expander("📖 The Poetry of Kong", expanded=True):
            #    st.code(content, language=None, line_numbers=True)

            # Optional: Display without line numbers
            with st.expander("The Poetry of Kong", icon="📄"):
                st.markdown("#### Example of the AI going crazy... or poetic.")
                st.markdown("Instead of estimating the **Upside Score** for Alibaba, Qwen crafted this modern poem about her mother. 😁")
                st.code(content, language=None, line_numbers=False)
                st.markdown("##### I guess that when we no longer have to care about money, we all become poets. 👩‍🎨")

        except Exception as e:
            st.error(f"❌ Error reading file: {str(e)}")

# Disclaimer

st.divider()  # 👈 Draws a horizontal rule

st.badge(label="**Version:** Marylin 1.2.3 (as of 2026-04-30)", icon=None, color="green")

st.caption(
    """
    #### Disclaimer
    
    **1. General Information & AI Nature** This content is generated by artificial intelligence (AI) and is for informational purposes only. While PrettyModels.ai strives for accuracy, the "strategies" and "scorings" are outputs of probabilistic models and large language models (LLMs). These may contain errors, hallucinations, or biases. Do not rely on this content as a definitive source of truth.
    
    **2. No Investment Advice** Nothing contained herein constitutes financial, legal, tax, or investment advice. This content is not a recommendation to buy, sell, or hold any security or to adopt any investment strategy. It does not take into account your specific financial situation, objectives, or risk tolerance. Always consult a qualified financial professional before making investment decisions.
    
    **3. No Offer or Solicitation** This material is not an offer to sell or a solicitation of an offer to buy any securities, investment products, or services in any jurisdiction where such offer or solicitation would be unlawful.
    
    **4. Risk Warning** Past performance is not indicative of future results. All investments involve significant risk, including the total loss of principal. AI-driven models are experimental; hypothetical or back-tested results presented may not reflect actual trading and have inherent limitations.
    
    **5. Conflict of Interest** PrettyModels.ai, its affiliates, and their respective officers or employees may hold positions in, or trade, the securities or instruments mentioned herein. Our proprietary algorithms may generate outputs that align with or contradict these internal positions.
    
    **6. Limitation of Liability** The content is provided on an "as is" and "as available" basis without warranties of any kind, express or implied. PrettyModels.ai expressly disclaims liability for any direct, indirect, consequential, or incidental damages arising from the use of, or reliance on, this information. You assume full responsibility for your use of this content.
    
    **7. Confidentiality & Use** This material is strictly confidential and intended solely for the recipient’s internal use. Unauthorized reproduction, distribution, or public display of this content, in whole or in part, is strictly prohibited. By accessing this content, you agree to these terms.
    
    © PrettyModels.ai 2026. All rights reserved. _Further information and legal notices can be found here:_
    """
)

c1, c2, c3, c4 = st.columns([1, 1, 2, 6])
with c1:
    st.link_button("LinkedIn", "https://www.linkedin.com/company/prettymodels-ai")
with c2:
    st.link_button("More Info", "https://docs.prettymodels.ai")

if False:
    with c3:
        # Load the PDF file
        with open("data/2025-07-01-marylin_report.pdf", "rb") as f:
            pdf_data = f.read()

        # Create a download button
        st.download_button(
            label="📄 Download PDF",
            data=pdf_data,
            file_name="marylin_report.pdf",
            mime="application/pdf"
        )
