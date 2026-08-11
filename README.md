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
