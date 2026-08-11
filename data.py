"""
Cached data loaders and derived metrics for the research-lab site.

All public figures and coverage dates are derived from the files in data/. The
score snapshot's date and model version live in research_metadata.json because
the score CSV itself does not contain either field; its checksum prevents that
metadata from silently drifting when the CSV is replaced.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import pandas as pd
import streamlit as st


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
PERF_CSV = DATA_DIR / "marylin_performance.csv"
SCORES_CSV = DATA_DIR / "full_weights - raw.csv"
RESEARCH_METADATA = DATA_DIR / "research_metadata.json"
WIKIFOLIO_PATTERN = "WFMARYLIN1-PriceData-*.csv"
_WIKIFOLIO_NAME = re.compile(r"WFMARYLIN1-PriceData-(\d{14})\.csv$")

INCEPTION = pd.Timestamp("2024-12-27")

# Benchmarks in marylin_performance.csv -> display labels for the alpha chart.
BENCHMARK_LABELS = {
    "Internet": "vs. Internet",
    "Nasdaq": "vs. Nasdaq",
    "Quality": "vs. Quality",
}


def _file_token(path: Path) -> tuple[str, int, int]:
    """Return cache arguments that change whenever a source file changes."""
    stat = path.stat()
    return str(path), stat.st_mtime_ns, stat.st_size


def _require_columns(df: pd.DataFrame, columns: set[str], source: Path) -> None:
    missing = columns.difference(df.columns)
    if missing:
        raise ValueError(f"{source.name} is missing columns: {', '.join(sorted(missing))}")


def _date_label(value: pd.Timestamp, *, include_time: bool = False) -> str:
    value = pd.Timestamp(value)
    if value.tzinfo is not None:
        value = value.tz_convert("Europe/Berlin")
    label = f"{value.day} {value.strftime('%B %Y')}"
    if include_time:
        label += f" at {value.strftime('%H:%M %Z')}"
    return label


def latest_wikifolio_csv() -> Path:
    """Select the newest export by the timestamp embedded in its filename."""
    candidates: list[tuple[str, Path]] = []
    for path in DATA_DIR.glob(WIKIFOLIO_PATTERN):
        match = _WIKIFOLIO_NAME.fullmatch(path.name)
        if match:
            candidates.append((match.group(1), path))
    if not candidates:
        raise FileNotFoundError(f"No {WIKIFOLIO_PATTERN} export found in {DATA_DIR}")
    return max(candidates, key=lambda item: item[0])[1]


@st.cache_data(show_spinner=False)
def _read_perf(path_str: str, _mtime_ns: int, _size: int) -> pd.DataFrame:
    source = Path(path_str)
    df = pd.read_csv(
        source,
        sep=";",
        decimal=",",
        skipinitialspace=True,
        parse_dates=["Date"],
        dayfirst=True,
        date_format="%d.%m.%y",
    )
    _require_columns(df, {"Date", *BENCHMARK_LABELS}, source)
    if df.empty or df["Date"].duplicated().any():
        raise ValueError(f"{source.name} must contain unique, non-empty dates")
    df.set_index("Date", inplace=True)
    df.sort_index(inplace=True)
    df = df[(df.index.is_month_end) | (df.index == INCEPTION)]
    if df.empty or df.index[0] != INCEPTION:
        raise ValueError(f"{source.name} must start at inception ({INCEPTION.date()})")
    if df[list(BENCHMARK_LABELS)].isna().any().any():
        raise ValueError(f"{source.name} contains missing benchmark values")
    return df


def load_perf_data() -> pd.DataFrame:
    """Cumulative return difference vs. each benchmark (month-end + inception)."""
    return _read_perf(*_file_token(PERF_CSV))


@st.cache_data(show_spinner=False)
def _read_wikifolio(path_str: str, _mtime_ns: int, _size: int) -> pd.DataFrame:
    source = Path(path_str)
    df = pd.read_csv(source, sep=";", decimal=",")
    _require_columns(df, {"Begin date", "Close"}, source)
    df["Begin date"] = pd.to_datetime(df["Begin date"], format="%d.%m.%y %H:%M")
    df.rename(columns={"Begin date": "Date", "Close": "Marylin Index"}, inplace=True)
    df = df[["Date", "Marylin Index"]].sort_values("Date").reset_index(drop=True)
    if df.empty or df["Date"].duplicated().any() or df["Marylin Index"].isna().any():
        raise ValueError(f"{source.name} must contain unique dates and complete index levels")
    if df["Date"].iloc[0].normalize() != INCEPTION:
        raise ValueError(f"{source.name} must start at inception ({INCEPTION.date()})")
    return df


def load_wikifolio_data() -> pd.DataFrame:
    """Marylin Wikifolio index level over time (nominal base 100)."""
    source = latest_wikifolio_csv()
    return _read_wikifolio(*_file_token(source))


@st.cache_data(show_spinner=False)
def _read_metadata(path_str: str, _mtime_ns: int, _size: int) -> dict:
    with Path(path_str).open(encoding="utf-8") as handle:
        metadata = json.load(handle)
    required = {"research_version", "scoring_data_as_of", "scores_sha256"}
    missing = required.difference(metadata)
    if missing:
        raise ValueError(
            f"{Path(path_str).name} is missing fields: {', '.join(sorted(missing))}"
        )
    return metadata


def research_metadata() -> dict:
    return _read_metadata(*_file_token(RESEARCH_METADATA))


@st.cache_data(show_spinner=False)
def _sha256(path_str: str, _mtime_ns: int, _size: int) -> str:
    digest = hashlib.sha256()
    with Path(path_str).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _validate_score_metadata() -> dict:
    metadata = research_metadata()
    actual = _sha256(*_file_token(SCORES_CSV))
    expected = str(metadata["scores_sha256"]).lower()
    if actual != expected:
        raise ValueError(
            f"{SCORES_CSV.name} changed without matching research metadata. "
            "Update scoring_data_as_of, research_version and scores_sha256 in "
            f"{RESEARCH_METADATA.name}."
        )
    return metadata


@st.cache_data(show_spinner=False)
def _read_scores(path_str: str, _mtime_ns: int, _size: int) -> pd.DataFrame:
    source = Path(path_str)
    df = pd.read_csv(source)
    _require_columns(df, {"Asset", "w"}, source)
    if df.empty or df["Asset"].isna().any() or df["Asset"].duplicated().any():
        raise ValueError(f"{source.name} must contain unique, non-empty assets")
    df.set_index("Asset", inplace=True, drop=True)
    df = df.sort_values("w", ascending=False)
    df.dropna(axis=0, how="any", subset=["w"], inplace=True)

    cols = [c for c in df.columns if "Cat-" in c and "Cat-XXX" not in c]
    if not cols:
        raise ValueError(f"{source.name} contains no composite Cat- columns")
    df = df[cols + ["w"]].copy()
    df.rename(columns={c: c.replace("Cat-", "") for c in cols}, inplace=True)
    df.dropna(axis=0, how="any", inplace=True)
    # Equal zero-weight names share the bottom rank, whose value must still equal
    # the row count because lab.py uses it as the slider's upper bound.
    df["Rank"] = df["w"].rank(ascending=False, method="max")
    return df


def load_scores() -> pd.DataFrame:
    """Composite-factor scores per company for the interactive tools."""
    _validate_score_metadata()
    return _read_scores(*_file_token(SCORES_CSV))


def universe_stats() -> dict:
    """Headline scale of the research universe (assets, dimensions, factors)."""
    _validate_score_metadata()
    raw = pd.read_csv(SCORES_CSV)
    dimensions = [
        c for c in raw.columns if c.endswith("Score100") or c.endswith("Probability100")
    ]
    composites = [c for c in raw.columns if c.startswith("Cat-") and "Cat-XXX" not in c]
    return {
        "n_assets": int(len(raw)),
        "n_dimensions": int(len(dimensions)),
        "n_composites": int(len(composites)),
    }


def data_freshness() -> dict:
    """Coverage dates and model metadata used by captions and disclosures."""
    metadata = _validate_score_metadata()
    scoring_at = pd.Timestamp(metadata["scoring_data_as_of"])
    if scoring_at.tzinfo is None:
        raise ValueError("scoring_data_as_of must include a UTC offset")
    performance_as_of = load_perf_data().index.max()
    reference_index_as_of = load_wikifolio_data()["Date"].max()
    latest_as_of = max(scoring_at.tz_localize(None), performance_as_of, reference_index_as_of)
    return {
        "research_version": str(metadata["research_version"]),
        "scoring_at": scoring_at,
        "scoring_as_of_label": _date_label(scoring_at),
        "performance_as_of": performance_as_of,
        "performance_as_of_label": _date_label(performance_as_of),
        "reference_index_as_of": reference_index_as_of,
        "reference_index_as_of_label": _date_label(reference_index_as_of),
        "latest_as_of": latest_as_of,
    }


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
