"""
data.py — cached data loaders and derived metrics for the research-lab site.

All figures shown on the site are computed here from the CSVs in data/, so the
copy never hard-codes a performance number that can drift out of date.
"""
import pandas as pd
import streamlit as st

PERF_CSV = "data/marylin_performance.csv"
WIKIFOLIO_CSV = "data/WFMARYLIN1-PriceData-20260701150456.csv"
SCORES_CSV = "data/full_weights - raw.csv"

INCEPTION = pd.to_datetime("2024-12-27")

# Benchmarks in marylin_performance.csv -> display labels for the alpha chart.
BENCHMARK_LABELS = {
    "Internet": "vs. Internet",
    "Nasdaq": "vs. Nasdaq",
    "Quality": "vs. Quality",
}


@st.cache_data
def load_perf_data() -> pd.DataFrame:
    """Cumulative return difference vs. each benchmark (month-end + inception)."""
    df = pd.read_csv(
        PERF_CSV, sep=";", decimal=",",
        parse_dates=["Date"], dayfirst=True, date_format="%d.%m.%y",
    )
    df.set_index("Date", inplace=True)
    df = df[(df.index.is_month_end) | (df.index == INCEPTION)]
    return df


@st.cache_data
def load_wikifolio_data() -> pd.DataFrame:
    """Marylin Wikifolio index level over time (base 100 at inception)."""
    df = pd.read_csv(WIKIFOLIO_CSV, sep=";", decimal=",")
    df["Begin date"] = pd.to_datetime(df["Begin date"], format="%d.%m.%y %H:%M")
    df.rename(columns={"Begin date": "Date", "Close": "Marylin Index"}, inplace=True)
    return df[["Date", "Marylin Index"]].sort_values("Date").reset_index(drop=True)


@st.cache_data
def load_scores() -> pd.DataFrame:
    """Composite-factor scores per company (the interactive tools operate on this)."""
    df = pd.read_csv(SCORES_CSV)
    df.set_index("Asset", inplace=True, drop=True)
    df = df.sort_values("w", ascending=False)
    df.dropna(axis=0, how="any", subset=["w"], inplace=True)

    cols = [c for c in df.columns if "Cat-" in c and "Cat-XXX" not in c]
    df = df[cols + ["w"]].copy()
    df.rename(columns={c: c.replace("Cat-", "") for c in cols}, inplace=True)
    df.dropna(axis=0, how="any", inplace=True)
    df["Rank"] = df["w"].rank(ascending=False)
    return df


@st.cache_data
def universe_stats() -> dict:
    """Headline scale of the research universe (assets, score dimensions, factors)."""
    raw = pd.read_csv(SCORES_CSV)
    dimensions = [c for c in raw.columns
                  if c.endswith("Score100") or c.endswith("Probability100")]
    composites = [c for c in raw.columns if c.startswith("Cat-") and "Cat-XXX" not in c]
    return {
        "n_assets": int(len(raw)),
        "n_dimensions": int(len(dimensions)),
        "n_composites": int(len(composites)),
    }


@st.cache_data
def validation_metrics() -> dict:
    """Public-track-record metrics computed from the reference-index series."""
    perf = load_perf_data()
    wiki = load_wikifolio_data()

    start, end = perf.index[0], perf.index[-1]
    days = max((end - start).days, 1)
    months = (end.year - start.year) * 12 + (end.month - start.month)

    index_return = wiki["Marylin Index"].iloc[-1] / 100.0 - 1.0

    alpha = {}
    for col in perf.columns:
        cum = float(perf[col].iloc[-1])
        ann = (1 + cum) ** (365.25 / days) - 1
        alpha[col] = {"cum": cum, "ann": ann, "label": BENCHMARK_LABELS.get(col, col)}

    # Headline difference = median benchmark, avoiding selection of the best one.
    cum_values = sorted(v["cum"] for v in alpha.values())
    headline_cum = cum_values[len(cum_values) // 2]

    return {
        "start": start,
        "end": end,
        "months": months,
        "index_return": index_return,
        "alpha": alpha,
        "headline_alpha_cum": headline_cum,
    }
