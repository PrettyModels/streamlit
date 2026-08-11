# PrettyModels AI — Research Lab

The public site for **PrettyModels AI**, an AI research lab testing whether
frontier language models can evaluate public companies consistently. Model
outputs are evaluated against the public Marylin Wikifolio reference portfolio.

Live site: [prettymodels.ai](https://prettymodels.ai/)

> Important: Christian Tausch publishes the research and operates the Marylin
> Wikifolio. An associated third-party certificate exists, and the trader may be
> eligible for performance-linked remuneration. See the site's Research & Risk
> Disclosures.

## Structure

| File | Purpose |
|------|---------|
| `streamlit_app.py` | Entry point / navigation |
| `lab.py` | The single-page site; orchestrates the sections |
| `components.py` | Design system: theme/CSS, Altair chart theme, render helpers |
| `content.py` | All copy, kept separate from layout |
| `data.py` | Cached CSV loaders and computed metrics (from `data/`) |
| `data/research_metadata.json` | Score snapshot date, model version and checksum guard |
| `legal_disclosures.py` | Research, financial-risk, performance and conflict disclosures |
| `legal_imprint.py` | DDG/MStV provider and editorial notice |
| `legal_privacy.py` | GDPR/TDDDG privacy notice |
| `LEGAL_DEPLOYMENT_CHECKLIST.md` | Required factual, infrastructure and counsel checks before release |
| `.streamlit/config.toml` | "Academic paper" theme (colors, fonts, chart palette) |

## Run it locally

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

## Updating research data

- Replace `data/full_weights - raw.csv`, then update all three fields in
  `data/research_metadata.json`. The SHA-256 must match the score CSV; otherwise
  the app stops instead of publishing a stale model date or version.
- Add the new `WFMARYLIN1-PriceData-YYYYMMDDHHMMSS.csv` export and remove the old
  one. The app automatically selects the newest timestamped export.
- Append the latest month to `data/marylin_performance.csv`. Its last date is
  used automatically in chart captions and disclosures.
- Before deployment, run `python -m py_compile data.py content.py lab.py
  legal_disclosures.py streamlit_app.py` and start the app locally. The data
  loaders validate required columns, dates, duplicate assets and metadata.
