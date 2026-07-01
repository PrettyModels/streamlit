import os
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
    page_title="PrettyModels AI | Investment Intelligence Lab",
    page_icon="images/logo.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to make the research lab positioning feel intentional inside Streamlit.
st.markdown("""
<style>
    #MainMenu, footer, header[data-testid="stHeader"],
    [data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] {
        display: none;
    }
    .block-container {padding-top: 0.9rem; padding-bottom: 5rem; max-width: 1180px;}
    h1, h2, h3 {letter-spacing: 0;}
    div[data-testid="stVerticalBlock"] {gap: 0.8rem;}
    .top-nav {
        align-items: center;
        border-bottom: 1px solid #E6EAF0;
        color: #667085;
        display: flex;
        font-size: 0.95rem;
        justify-content: space-between;
        margin-bottom: 1.65rem;
        padding-bottom: 0.65rem;
    }
    .brand-mark {
        align-items: center;
        display: flex;
        gap: 0.6rem;
    }
    .brand-dot {
        align-items: center;
        background: #0F172A;
        border-radius: 999px;
        color: #FFFFFF;
        display: inline-flex;
        font-size: 0.76rem;
        font-weight: 800;
        height: 2rem;
        justify-content: center;
        width: 2rem;
    }
    .brand-name {
        color: #172033;
        font-size: 1.05rem;
        font-weight: 800;
    }
    .nav-links {
        align-items: center;
        display: flex;
        gap: 1.2rem;
        white-space: nowrap;
    }
    .nav-links a {
        color: #526071;
        text-decoration: none;
    }
    .nav-links a:hover {
        color: #172033;
        text-decoration: underline;
    }
    .eyebrow {
        color: #FF4B4B;
        font-size: 0.78rem;
        font-weight: 800;
        letter-spacing: 0;
        margin-bottom: 0.65rem;
        text-transform: uppercase;
    }
    .hero-title {
        color: #172033;
        font-size: 2.82rem;
        font-weight: 800;
        line-height: 1.05;
        margin: 0 0 0.8rem 0;
        max-width: 760px;
    }
    .hero-copy {
        color: #4F5B6D;
        font-size: 1.06rem;
        line-height: 1.45;
        margin-bottom: 0.85rem;
        max-width: 700px;
    }
    .hero-thesis {
        background: #F7F9FC;
        border: 1px solid #E6EAF0;
        border-radius: 8px;
        color: #526071;
        font-size: 0.95rem;
        line-height: 1.45;
        margin-top: 0.55rem;
        padding: 0.65rem 0.8rem;
    }
    .hero-visual-caption {
        color: #667085;
        font-size: 0.82rem;
        line-height: 1.35;
        margin-top: 0.35rem;
    }
    .proof-strip {
        border-bottom: 1px solid #E6EAF0;
        border-top: 1px solid #E6EAF0;
        display: grid;
        gap: 0;
        grid-template-columns: 1.15fr repeat(3, 1fr);
        margin: 1rem 0 0.25rem 0;
    }
    .proof-item {
        border-right: 1px solid #E6EAF0;
        padding: 0.72rem 1rem;
    }
    .proof-item:last-child {border-right: 0;}
    .proof-label {
        color: #667085;
        font-size: 0.78rem;
        font-weight: 700;
        margin-bottom: 0.25rem;
        text-transform: uppercase;
    }
    .proof-value {
        color: #172033;
        font-size: 1.42rem;
        font-weight: 800;
        line-height: 1.1;
    }
    .proof-note {
        color: #667085;
        font-size: 0.82rem;
        line-height: 1.35;
        margin-top: 0.35rem;
    }
    .section-intro {
        color: #536171;
        font-size: 1.05rem;
        line-height: 1.5;
        max-width: 840px;
    }
    .metric-context {
        color: #667085;
        font-size: 0.86rem;
        line-height: 1.35;
        margin: -0.1rem 0 -0.45rem 0;
    }
    .section-title {
        color: #2B2D38;
        font-size: 2.25rem;
        font-weight: 800;
        line-height: 1.12;
        margin: 0.85rem 0 0.55rem 0;
    }
    .section-title.with-rule {
        border-top: 1px solid #E6EAF0;
        margin-top: 1.25rem;
        padding-top: 1.25rem;
    }
    .build-card {
        background: #F8FAFC;
        border: 1px solid #E6EAF0;
        border-radius: 8px;
        min-height: 140px;
        padding: 0.82rem;
    }
    .build-index {
        color: #FF4B4B;
        font-size: 0.78rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    .build-card h3 {
        color: #172033;
        font-size: 1rem;
        margin-bottom: 0.35rem;
    }
    .build-card p {
        color: #536171;
        font-size: 0.88rem;
        line-height: 1.45;
    }
    .process-map {
        border-bottom: 1px solid #E6EAF0;
        border-top: 1px solid #E6EAF0;
        display: grid;
        gap: 0;
        grid-template-columns: repeat(5, 1fr);
        margin-top: 1.1rem;
    }
    .process-step {
        border-right: 1px solid #E6EAF0;
        min-height: 155px;
        padding: 1rem;
    }
    .process-step:last-child {border-right: 0;}
    .process-label {
        color: #FF4B4B;
        font-size: 0.74rem;
        font-weight: 800;
        margin-bottom: 0.65rem;
        text-transform: uppercase;
    }
    .process-title {
        color: #172033;
        font-size: 1.05rem;
        font-weight: 800;
        line-height: 1.2;
        margin-bottom: 0.45rem;
    }
    .process-copy {
        color: #536171;
        font-size: 0.9rem;
        line-height: 1.4;
    }
    .process-output {
        background: #F7F9FC;
        border: 1px solid #E6EAF0;
        border-radius: 8px;
        color: #526071;
        font-size: 0.92rem;
        line-height: 1.45;
        margin-top: 0.9rem;
        padding: 0.75rem 0.9rem;
    }
    .section-kicker {
        color: #FF4B4B;
        font-size: 0.82rem;
        font-weight: 800;
        letter-spacing: 0;
        text-transform: uppercase;
    }
    .highlight {color: #FF4B4B; font-weight: bold;}
    @media (max-width: 700px) {
        .top-nav {display: block;}
        .nav-links {display: none;}
        .hero-title {font-size: 2.2rem;}
        .hero-copy {font-size: 1.05rem;}
        .section-title {font-size: 1.8rem;}
        .proof-strip {grid-template-columns: 1fr;}
        .proof-item {border-bottom: 1px solid #E6EAF0; border-right: 0;}
        .proof-item:last-child {border-bottom: 0;}
        .process-map {grid-template-columns: 1fr;}
        .process-step {border-bottom: 1px solid #E6EAF0; border-right: 0; min-height: auto;}
        .process-step:last-child {border-bottom: 0;}
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_perf_data():
    df = pd.read_csv(
        "data/marylin_performance.csv",
        sep=";",
        decimal=",",
        skipinitialspace=True,
        parse_dates=["Date"],
        dayfirst=True,
        date_format="%d.%m.%y",
    )
    df.set_index("Date", inplace=True)
    df = df[(df.index.is_month_end) | (df.index == pd.to_datetime('2024-12-27'))]
    return df


@st.cache_data
def load_wikifolio_data():
    df = pd.read_csv(
        "data/WFMARYLIN1-PriceData-20260701150456.csv",
        sep=";",
        decimal=",",
        skipinitialspace=True,
    )

    df["Begin date"] = pd.to_datetime(df["Begin date"], format="%d.%m.%y %H:%M")
    df.rename(columns={"Begin date": "Date", "Close": "Marylin Index"}, inplace=True)
    df = df[["Date", "Marylin Index"]].sort_values("Date")
    return df


df_mape = load_perf_data()
df_wiki = load_wikifolio_data()

def compute_case_metrics(perf_df, wiki_df):
    start_date = perf_df.index[0]
    end_date = perf_df.index[-1]
    prev_date = perf_df.index[-2]
    days_end = (end_date - start_date).days
    days_prev = (prev_date - start_date).days

    cum_alpha_end = perf_df["Internet"].iloc[-1]
    cum_alpha_prev = perf_df["Internet"].iloc[-2]
    ann_alpha_end = (1 + cum_alpha_end) ** (365.25 / days_end) - 1
    ann_alpha_prev = (1 + cum_alpha_prev) ** (365.25 / days_prev) - 1

    wiki_case = wiki_df[wiki_df["Date"] <= end_date]
    latest_wiki_value = wiki_case["Marylin Index"].iloc[-1]
    prev_wiki_value = wiki_df[wiki_df["Date"] <= prev_date]["Marylin Index"].iloc[-1]

    return {
        "start_date": start_date,
        "end_date": end_date,
        "prev_date": prev_date,
        "wiki_case": wiki_case,
        "case_return": latest_wiki_value / 100 - 1,
        "case_return_delta": latest_wiki_value / prev_wiki_value - 1,
        "cum_alpha_end": cum_alpha_end,
        "cum_alpha_delta": cum_alpha_end - cum_alpha_prev,
        "ann_alpha_end": ann_alpha_end,
        "ann_alpha_delta": ann_alpha_end - ann_alpha_prev,
    }


case_metrics = compute_case_metrics(df_mape, df_wiki)

st.markdown(
    """
    <div class="top-nav">
        <div class="brand-mark">
            <span class="brand-dot">PM</span>
            <span class="brand-name">PrettyModels AI</span>
        </div>
        <div class="nav-links">
            <a href="#what-we-build">Research</a>
            <a href="#marylin-case-study">Marylin</a>
            <a href="#research-console">Signals</a>
            <a href="https://docs.prettymodels.ai" target="_blank">Docs</a>
            <a href="https://tausch.capital" target="_blank">tausch.capital</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

hero_text, hero_visual = st.columns([1.12, 0.88], gap="large", vertical_alignment="center")
with hero_text:
    st.markdown('<div class="eyebrow">Applied AI investment research lab</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title">Turning market narratives into testable allocation signals.</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="hero-copy">
            PrettyModels AI develops LLM-based scoring systems, portfolio rules,
            and live validation studies for public equities. We study where
            AI-generated signals can improve allocation decisions, and where
            they fail.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="hero-thesis">
            The lab's job is simple: make qualitative market information
            measurable, comparable, and accountable to live evidence.
        </div>
        """,
        unsafe_allow_html=True,
    )

with hero_visual:
    st.image("images/allocation-pipeline.svg", width="stretch")
    st.markdown(
        '<div class="hero-visual-caption">Qualitative evidence becomes scores, weights, and testable allocation signals.</div>',
        unsafe_allow_html=True,
    )

st.markdown(
    f"""
    <div class="proof-strip">
        <div class="proof-item">
            <div class="proof-label">Live case study</div>
            <div class="proof-value">Marylin</div>
            <div class="proof-note">{case_metrics["start_date"].strftime("%b %Y")} through {case_metrics["end_date"].strftime("%b %Y")}</div>
        </div>
        <div class="proof-item">
            <div class="proof-label">Public index record</div>
            <div class="proof-value">{case_metrics["case_return"]:.1%}</div>
            <div class="proof-note">{case_metrics["case_return_delta"]:+.1%} in {case_metrics["end_date"].strftime("%B")}</div>
        </div>
        <div class="proof-item">
            <div class="proof-label">Alpha vs. Internet</div>
            <div class="proof-value">{case_metrics["cum_alpha_end"]:.1%}</div>
            <div class="proof-note">{case_metrics["cum_alpha_delta"]:+.1%} in {case_metrics["end_date"].strftime("%B")}</div>
        </div>
        <div class="proof-item">
            <div class="proof-label">Annualized alpha</div>
            <div class="proof-value">{case_metrics["ann_alpha_end"]:.1%}</div>
            <div class="proof-note">{case_metrics["ann_alpha_delta"]:+.1%} latest change</div>
        </div>
    </div>
    <div class="metric-context">
        Marylin is shown as a live validation study, not an investment recommendation.
        Asset-management material and the Wikifolio presentation belong at
        <strong>tausch.capital</strong>.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<span id="what-we-build"></span>', unsafe_allow_html=True)
st.markdown('<div class="section-title">What We Build</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="section-intro">
        The lab produces reusable research artifacts: signal definitions,
        scoring runs, portfolio rules, and validation records. Each artifact
        must be inspectable before it can influence allocation.
    </div>
    """,
    unsafe_allow_html=True,
)
build1, build2, build3, build4 = st.columns(4, gap="medium")
with build1:
    st.markdown(
        """
        <div class="build-card">
            <div class="build-index">01 / SIGNAL</div>
            <h3>Narrative Extraction</h3>
            <p>Prompt systems that read company context, market structure, and AI-era themes.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with build2:
    st.markdown(
        """
        <div class="build-card">
            <div class="build-index">02 / SCORE</div>
            <h3>Factor Scoring</h3>
            <p>Comparable scores for quality, resilience, upside, market structure, and AI exposure.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with build3:
    st.markdown(
        """
        <div class="build-card">
            <div class="build-index">03 / ALLOCATE</div>
            <h3>Portfolio Translation</h3>
            <p>Rules that turn signals into weights, concentration limits, benchmarks, and risk constraints.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with build4:
    st.markdown(
        """
        <div class="build-card">
            <div class="build-index">04 / VALIDATE</div>
            <h3>Live Evaluation</h3>
            <p>Public case studies that track model behavior against benchmarks, drawdowns, drift, and failures.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="section-title with-rule">From Language to Allocation</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="section-intro">
        The workflow is deliberately mechanical. A model can generate insight,
        but the lab only keeps what survives translation into a score, a rule,
        and an observable market record.
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class="process-map">
        <div class="process-step">
            <div class="process-label">Input</div>
            <div class="process-title">Market Narrative</div>
            <div class="process-copy">Company context, sector change, filings, sentiment, product signals, and AI-era relevance.</div>
        </div>
        <div class="process-step">
            <div class="process-label">Model</div>
            <div class="process-title">Prompted Scoring</div>
            <div class="process-copy">LLM runs convert qualitative evidence into normalized research categories.</div>
        </div>
        <div class="process-step">
            <div class="process-label">Data</div>
            <div class="process-title">Signal Table</div>
            <div class="process-copy">Scores become comparable across assets, months, categories, and model variants.</div>
        </div>
        <div class="process-step">
            <div class="process-label">Rule</div>
            <div class="process-title">Portfolio Logic</div>
            <div class="process-copy">Signals are mapped to rank, weight, conviction, benchmark, and risk constraints.</div>
        </div>
        <div class="process-step">
            <div class="process-label">Evidence</div>
            <div class="process-title">Live Record</div>
            <div class="process-copy">The strategy is tracked against market alternatives and monitored for drift or failure.</div>
        </div>
    </div>
    <div class="process-output">
        Research output: a traceable chain from qualitative evidence to allocation behavior, with Marylin as the first public validation record.
    </div>
    """,
    unsafe_allow_html=True,
)




#  MARYLIN


st.markdown('<span id="marylin-case-study"></span>', unsafe_allow_html=True)
with st.expander("Research Case Study: Marylin", icon="📈", expanded=True):
    st.markdown("# MARYLIN CASE STUDY")
    st.markdown(
        """
        Marylin is the first public validation artifact from PrettyModels AI: a
        high-conviction portfolio experiment used to study whether AI-generated
        signals can hold up in live markets. The investor-facing presentation of
        the strategy belongs to **tausch.capital**; this page keeps the research
        context, diagnostics, and limitations visible.
        """
    )

    start_date = case_metrics["start_date"]
    end_date = case_metrics["end_date"]
    df_wiki_case = case_metrics["wiki_case"]

    col1, col2, col3 = st.columns([1, 2, 1])  # Adjust the ratios if needed
    with col2:
        st.image("images/marylin6.png", width="stretch")
    with col1:
        st.markdown("##### First live **PrettyModels AI** portfolio experiment.")
        st.markdown("##### Tests high-conviction AI allocation outside a backtest.")
        st.markdown("##### Tracks alpha against public ETF-style benchmarks.")
        st.markdown("##### Public record starts on December 27, 2024.")
        st.link_button("Asset manager site", "https://tausch.capital", type="primary")
        st.link_button("Public Wikifolio record", "https://www.wikifolio.com/en/int/w/wfmarylin1")
        st.link_button("Read research story", "https://quant-unit.com/the-story-of-marylin-pt-1/")

    col3.metric(
        f"Marylin index ({start_date.strftime('%b %Y')} - {end_date.strftime('%b %Y')})",
        f"{case_metrics['case_return']:.1%}",
        f"{case_metrics['case_return_delta']:+.1%} in {end_date.strftime('%B %Y')}",
        border=True,
    )
    col3.metric(
        "Alpha vs. Internet benchmark",
        f"{case_metrics['cum_alpha_end']:.1%}",
        f"{case_metrics['cum_alpha_delta']:+.1%} in {end_date.strftime('%B %Y')}",
        border=True,
    )
    col3.metric(
        "Annualized alpha",
        f"{case_metrics['ann_alpha_end']:.1%}",
        f"{case_metrics['ann_alpha_delta']:+.1%} ({end_date.strftime('%B %Y')})",
        border=True,
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        perf_cols = df_wiki_case.columns.drop("Date").tolist()
        chart_df = df_wiki_case.melt(
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

        st.markdown("### Marylin public index record")
        st.altair_chart(final_chart, use_container_width=True)
        st.caption("Index level shown through the latest month with matching benchmark-alpha data.")

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

        st.markdown("### Benchmark-relative alpha")
        st.altair_chart(final_chart, use_container_width=True)



st.markdown('<span id="research-console"></span>', unsafe_allow_html=True)
with st.expander("Research Console", icon="✨", expanded=True):
    # DATA

    #st.divider()
    #st.write("Our [Allocation Intelligence](https://docs.prettymodels.ai) models provide 100% AI-powered asset assessments, custom-tailored for your unique investment universe.")
    st.markdown("# AI SIGNAL WATCHLIST")
    # st.markdown("This dataset is the ❤️ of all PrettyModels AI strategies.")
    st.markdown("""
    This is a lab view into monthly AI-generated signal categories for the
    public-equity universe. The table is designed for research inspection:
    compare factor structure, identify model disagreements, and stress-test
    portfolio candidates before anything becomes an asset-management story.
    """)

    # Load the data from a CSV. We're caching this so it doesn't reload every time the app
    # reruns (e.g. if the user interacts with the widgets).
    @st.cache_data
    def load_data():
        # Data contains AI-generated scores used for signal research and allocation experiments.
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
    tab0, tab1, tab2 = st.tabs(["Signal Mix", "Company Comparison", "Asset Diagnostics"])


    with tab2:
        company = st.selectbox(
        "Which asset should the lab view inspect?",
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
        st.header("Cumulative Signal Score")

        # Bar Chart
        # st.bar_chart(data=df_filtered, y=list(scores))
        scores1 = sorted(set(df_filtered.columns))
        make_bar_chart(df=df_filtered.copy(), scores=scores1, id_vars=["Asset"])


    with tab0:
        # Show a multiselect widget with the genres using `st.multiselect`.
        scores = st.multiselect(
            "Signal categories",
            all_scores,
            all_scores,
        )

        # Show a slider widget with the years using `st.slider`.
        max_rank = df_data["Rank"].max()
        ranks = st.slider("Model rank", 1, min(500, int(max_rank)), (1, 10))

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
        st.header("Cumulative Signal Score")

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


with st.expander("Research Charter", icon="📄", expanded=False):
    st.markdown("""
    ## PrettyModels AI researches investment intelligence.

    Markets are full of information that is too qualitative, fragmented, and
    narrative-heavy for classical screens alone. Large language models make it
    possible to turn more of that information into structured research inputs,
    but the result is only useful if it can be measured, compared, and tested.

    Our work is to design those translation layers: prompts, scoring systems,
    model ensembles, portfolio rules, and validation loops for public-market
    allocation. We are interested in signals that survive contact with live
    data, not just signals that look persuasive in a backtest.

    The lab follows five principles:

    1. **Research before promotion.** A strategy starts as a falsifiable
       experiment, not as a product story.
    2. **Every narrative becomes a number.** Qualitative judgment must become a
       comparable signal before it can enter an allocation model.
    3. **Benchmarks matter.** Alpha only has meaning relative to a relevant
       alternative.
    4. **Live validation beats beautiful theory.** Public records and ongoing
       diagnostics are part of the research process.
    5. **AI stays accountable.** Model outputs can be wrong, biased, stale, or
       overconfident; research discipline matters more as automation improves.
    """)

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

st.badge(label="**Version:** Marylin 1.2.5 (as of 2026-06-30)", icon=None, color="green")

st.caption(
    """
    #### Disclaimer
    
    **1. General Information & AI Nature** This website describes research by PrettyModels AI and is for informational purposes only. The strategies, scores, and diagnostics shown here are outputs of probabilistic models and large language models (LLMs). They may contain errors, hallucinations, stale assumptions, or biases.
    
    **2. No Investment Advice** Nothing contained herein constitutes financial, legal, tax, or investment advice. This content is not a recommendation to buy, sell, or hold any security or to adopt any investment strategy. It does not take into account any person's financial situation, objectives, or risk tolerance.
    
    **3. No Offer or Solicitation** This material is not an offer to sell or a solicitation of an offer to buy any securities, investment products, or services in any jurisdiction where such offer or solicitation would be unlawful.
    
    **4. Risk Warning** Past performance is not indicative of future results. All investments involve risk, including the possible loss of principal. AI-driven models are experimental; hypothetical or back-tested results may not reflect actual trading and have inherent limitations.
    
    **5. Conflict of Interest** PrettyModels AI, its affiliates, and their respective officers or employees may hold positions in, or trade, securities or instruments mentioned herein. Research outputs may align with or contradict those positions.
    
    **6. Limitation of Liability** The content is provided on an "as is" and "as available" basis without warranties of any kind, express or implied. PrettyModels AI disclaims liability for damages arising from use of, or reliance on, this information.
    
    © PrettyModels AI 2026. All rights reserved. _Further information and legal notices can be found here:_
    """
)

c1, c2, c3, c4 = st.columns([1, 1, 2, 6])
with c1:
    st.link_button("LinkedIn", "https://www.linkedin.com/company/prettymodels-ai")
with c2:
    st.link_button("More Info", "https://docs.prettymodels.ai")
with c3:
    st.link_button("tausch.capital", "https://tausch.capital")

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
