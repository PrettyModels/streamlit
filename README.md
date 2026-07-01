# PrettyModels AI — Research Lab

The public site for **PrettyModels AI**, an independent research lab building
AI-driven algorithms that turn frontier language models into quantitative,
public-market signals. The signal is validated out-of-sample on a live Wikifolio
index ("Marylin").

Live site: [prettymodels.ai](https://prettymodels.ai/)

> Note: PrettyModels AI is a research lab. It does not manage money or offer
> investment products. The Marylin index is operated separately by
> Until Singularity Asset Management ([tausch.capital](https://tausch.capital)).

## Structure

| File | Purpose |
|------|---------|
| `streamlit_app.py` | Entry point / navigation |
| `lab.py` | The single-page site; orchestrates the sections |
| `components.py` | Design system: theme/CSS, Altair chart theme, render helpers |
| `content.py` | All copy, kept separate from layout |
| `data.py` | Cached CSV loaders and computed metrics (from `data/`) |
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
