"""
lab.py — PrettyModels AI, the research-lab landing page.

Layout is an "academic paper": a numbered, single-scroll essay. Copy lives in
content.py, data loaders/metrics in data.py, and the design system (theme + render
helpers) in components.py. This module only orchestrates.
"""
import altair as alt
import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

import components as c
import content as T
import data as D

# --- page setup --------------------------------------------------------------
st.set_page_config(
    page_title=T.PAGE_TITLE,
    page_icon="images/logo.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)
c.inject_theme()
c.masthead(T.BRAND, T.TAGLINE, T.NAV)

# =============================================================================
# §0 — Abstract / Hero
# =============================================================================
stats = D.universe_stats()
metrics = D.validation_metrics()
copy = T.fill(stats)  # copy with the universe counts (31 dims, 5 factors) woven in

hero_l, hero_r = st.columns([1.3, 1], vertical_alignment="center")
with hero_l:
    c.eyebrow(T.HERO_EYEBROW)
    st.markdown(f'<div class="pm-hero-h1">{T.HERO_HEADLINE}</div>',
                unsafe_allow_html=True)
    c.lead(T.HERO_LEAD)
with hero_r:
    st.image("images/marylin6.png", width="stretch")

c.stat_strip([
    (str(stats["n_assets"]), "companies scored monthly"),
    (str(stats["n_dimensions"]), "AI score dimensions"),
    (str(stats["n_composites"]), "composite factors"),
    (f'{metrics["months"]}', "months publicly tracked"),
])

# =============================================================================
# §1 — Thesis
# =============================================================================
c.hairline()
c.section_header("thesis", "1", "Thesis", T.THESIS_SUBTITLE)
c.body(T.THESIS_BODY)
c.pull_quote(T.THESIS_PULLQUOTE)

# =============================================================================
# §2 — Method
# =============================================================================
c.hairline()
c.section_header("method", "2", "Method", T.METHOD_SUBTITLE)
c.lead(T.METHOD_INTRO)
c.step_grid(copy["method_steps"])

# =============================================================================
# §3 — The Scoring Engine
# =============================================================================
c.hairline()
c.section_header("scoring-engine", "3", "The Scoring Engine", T.SCORING_SUBTITLE)
c.lead(copy["scoring_intro"])

c.eyebrow(copy["glossary_subtitle"])
c.glossary_grid(T.GLOSSARY)

df_scores = D.load_scores()
all_scores = sorted(set(df_scores.columns).symmetric_difference(["w", "Rank"]))


def _bar_chart(df: pd.DataFrame, scores: list[str], id_vars: list[str]) -> None:
    df = df.copy()
    df["Asset"] = df.index
    if not scores:
        scores = ["Rank"]
        df["Rank"] = 1 / df["Rank"]
    df["row_sum"] = df[scores].sum(axis=1)
    df = df.sort_values("row_sum", ascending=False)
    order = df["Asset"].tolist()
    df_long = df.melt(id_vars=id_vars, value_vars=scores,
                      var_name="Factor", value_name="Score")
    chart = (
        alt.Chart(df_long)
        .mark_bar()
        .encode(
            x=alt.X("Asset:N", sort=order, axis=alt.Axis(title=None, labelAngle=-40)),
            y=alt.Y("Score:Q", axis=alt.Axis(title=None)),
            color=alt.Color("Factor:N", legend=alt.Legend(title=None, orient="top")),
        )
    )
    st.altair_chart(chart, use_container_width=True)


# score table
col_cfg = {col: st.column_config.NumberColumn(col, format="percent")
           for col in df_scores.columns if col not in ("w", "Rank")}
st.dataframe(
    df_scores.drop(columns=["Rank", "w"]).sort_index()
    .style.highlight_max(axis=0, props=f"background-color:{c.ACCENT_SOFT};"),
    width="stretch",
    column_config=col_cfg,
)
c.figure_caption(T.SCORING_TABLE_CAPTION)
st.caption(
    f"Model-output date: {T.SCORING_DATA_AS_OF} · "
    f"Scheduled update frequency: {T.RESEARCH_UPDATE_FREQUENCY}"
)

tab_explore, tab_compare, tab_analyze = st.tabs(
    [T.TAB_EXPLORE, T.TAB_COMPARE, T.TAB_ANALYZE]
)

with tab_explore:
    scores = st.multiselect("Factors", all_scores, all_scores)
    max_rank = int(df_scores["Rank"].max())
    no_of_companies = len(df_scores)
    ranks = st.slider("Conviction rank", 1, min(500, max_rank), (1, no_of_companies))
    df_f = df_scores.loc[df_scores["Rank"].between(ranks[0], ranks[1]),
                         ["Rank"] + list(scores)]
    st.markdown("###### Cumulative factor score")
    _bar_chart(df_f.copy(), scores, ["Asset"])

    if len(scores) > 1:
        st.markdown("###### Principal component analysis")
        feats = df_f.drop(columns=["Rank"]).columns.tolist()
        X = df_f[feats].dropna().copy()
        X_scaled = StandardScaler().fit_transform(X)
        n_max = min(len(df_f), len(feats))
        n_comp = st.slider("Principal components", 1, n_max, n_max)
        pca = PCA(n_components=n_comp).fit(X_scaled)
        loadings = pd.DataFrame(pca.components_.T, index=feats,
                                columns=[f"PC {i+1}" for i in range(n_comp)])
        df_long = loadings.reset_index().melt(id_vars="index")
        df_long.columns = ["Factor", "Component", "Loading"]
        heat = (
            alt.Chart(df_long)
            .mark_rect()
            .encode(
                x=alt.X("Component:O", title=None),
                y=alt.Y("Factor:O", title=None),
                color=alt.Color("Loading:Q", legend=alt.Legend(title=None)),
                tooltip=["Component", "Factor", "Loading"],
            )
            # left padding: keep the longest y label from clipping at the edge
            .properties(height=280, padding={"left": 12, "top": 5, "right": 5,
                                             "bottom": 5})
        )
        st.altair_chart(heat, use_container_width=True)

with tab_compare:
    default = df_scores.nlargest(6, "w").sort_index().index
    picks = st.multiselect("Companies", sorted(set(df_scores.index)), default)
    df_f = df_scores.loc[picks, :].drop(columns=["w", "Rank"]).copy()
    st.markdown("###### Cumulative factor score")
    _bar_chart(df_f.copy(), sorted(df_f.columns), ["Asset"])

with tab_analyze:
    company = st.selectbox("Company", sorted(set(df_scores.index)))
    s = df_scores.loc[company, all_scores].copy()
    df1 = s.reset_index()
    label = company.replace(",", " ").replace(".", "-")
    df1.columns = ["Factor", label]
    df1.sort_values(by=label, ascending=False, inplace=True)
    chart = (
        alt.Chart(df1)
        .mark_bar()
        .encode(
            x=alt.X("Factor:N", sort="-y", axis=alt.Axis(title=None)),
            y=alt.Y(f"{label}:Q", axis=alt.Axis(title=None, format="%"),
                    scale=alt.Scale(domain=[0, 1])),
            color=alt.Color(f"{label}:Q",
                            scale=alt.Scale(scheme="purples"),
                            legend=alt.Legend(title=None)),
        )
    )
    st.altair_chart(chart, use_container_width=True)

# =============================================================================
# §4 — Live Validation
# =============================================================================
c.hairline()
c.section_header("validation", "4", "Live Validation", T.VALIDATION_SUBTITLE)
c.lead(T.VALIDATION_INTRO)

a = metrics["alpha"]
c.stat_strip([
    (f'{metrics["index_return"]:+.0%}', "reference-index return since inception"),
    (f'{a["Internet"]["cum"]:+.0%}', "return difference vs. Internet"),
    (f'{a["Nasdaq"]["cum"]:+.0%}', "return difference vs. Nasdaq"),
    (f'{a["Quality"]["cum"]:+.0%}', "return difference vs. Quality"),
])

fig_l, fig_r = st.columns(2)

with fig_l:
    df_wiki = D.load_wikifolio_data()
    line = (
        alt.Chart(df_wiki)
        .mark_line(strokeWidth=2.5, strokeCap="round", color=c.ACCENT)
        .encode(
            x=alt.X("Date:T", title=""),
            y=alt.Y("Marylin Index:Q", title="",
                    scale=alt.Scale(zero=False, nice=False)),
            tooltip=[alt.Tooltip("Date:T"),
                     alt.Tooltip("Marylin Index:Q", format=",.2f")],
        )
        .properties(height=340)
    )
    base = (
        alt.Chart(pd.DataFrame({"y": [100.0]}))
        .mark_rule(color=c.FAINT, strokeDash=[3, 4], strokeWidth=1.5)
        .encode(y="y:Q")
    )
    st.altair_chart(base + line, use_container_width=True)
    c.figure_caption(T.VALIDATION_INDEX_CAPTION)

with fig_r:
    df_perf = D.load_perf_data().reset_index().rename(columns=D.BENCHMARK_LABELS)
    perf_cols = [D.BENCHMARK_LABELS[k] for k in D.BENCHMARK_LABELS]
    chart_df = df_perf.melt(id_vars=["Date"], value_vars=perf_cols,
                            var_name="Benchmark", value_name="Alpha")
    line = (
        alt.Chart(chart_df)
        .mark_line(strokeWidth=2.5, strokeCap="round")
        .encode(
            x=alt.X("Date:T", title=""),
            y=alt.Y("Alpha:Q", axis=alt.Axis(format="%"), title=""),
            color=alt.Color("Benchmark:N", legend=alt.Legend(title=None, orient="top")),
            tooltip=[alt.Tooltip("Date:T"), alt.Tooltip("Benchmark:N"),
                     alt.Tooltip("Alpha:Q", format=".1%")],
        )
        .properties(height=340)
    )
    zero = (
        alt.Chart(pd.DataFrame({"y": [0]}))
        .mark_rule(color=c.FAINT, strokeDash=[3, 4], strokeWidth=1.5)
        .encode(y="y:Q")
    )
    st.altair_chart(zero + line, use_container_width=True)
    c.figure_caption(T.VALIDATION_ALPHA_CAPTION)

c.eyebrow(T.OPEN_QUESTIONS_SUBTITLE)
c.body(T.OPEN_QUESTIONS_BODY)

st.markdown(T.VALIDATION_NOTE)
st.link_button(T.VALIDATION_VERIFY, T.WIKIFOLIO_URL)
st.page_link("legal_disclosures.py", label="Read the Research & Risk Disclosures")

# =============================================================================
# §5 — Philosophy
# =============================================================================
c.hairline()
c.section_header("philosophy", "5", "Philosophy", T.PHILOSOPHY_SUBTITLE)
c.body(T.PHILOSOPHY_BODY)
c.pull_quote(T.PHILOSOPHY_PULLQUOTE)

# =============================================================================
# Footer
# =============================================================================
c.hairline()
c.entity_note(T.ENTITY_NOTE)
st.caption(T.DISCLAIMER)
c.footer_links(
    T.FOOTER_LINKS,
    meta=(f"Research log · {T.RESEARCH_VERSION} · "
          f"updated {metrics['end'].strftime('%Y-%m-%d')}"),
)
