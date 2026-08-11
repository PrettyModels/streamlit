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
| `static/` | Optimized hero, favicon, app icons, social preview, manifest, robots and sitemap |
| `deploy/nginx/` | Crawler-visible metadata and conventional public-file routes |
| `seo_config.py` | Technical mapping from existing public copy to crawler metadata |
| `scripts/generate_seo_assets.py` | Generates Nginx metadata, prerender summaries, robots and sitemap from `seo_config.ROUTES` |
| `scripts/verify_public_site.py` | Verifies raw production HTML, assets, redirects and 404 behavior |

## Run it locally

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

## Browser and sharing metadata

Streamlit's `st.set_page_config` updates the tab title and icon only after the
app connects. Search engines and social-preview crawlers inspect the initial
HTML response instead, so production Nginx exposes metadata and a concise,
same-content HTML fallback before the websocket starts.

- Change public route metadata only in `seo_config.ROUTES`, then regenerate and
  verify the committed outputs:

  ```bash
  python3 scripts/generate_seo_assets.py
  python3 scripts/generate_seo_assets.py --check
  ```

- Enable the three checked-in snippets in the canonical HTTPS configuration:
  `deploy/nginx/http-metadata-map.conf` at `http` scope,
  `deploy/nginx/streamlit-location-metadata.conf` inside the existing
  `location /` block, and `deploy/nginx/public-files.conf` at `server` scope.
- Test with `sudo nginx -t`, reload Nginx, then verify the raw page source—not
  only the browser DOM—contains `og:title`, `og:image`, and the PM favicon.
- If the PM mark, hero or public positioning changes, regenerate the optimized
  image assets with `python3 scripts/generate_brand_assets.py` and commit them.
- After deployment, run `python3 scripts/verify_public_site.py`. This fails if
  any public document is missing metadata/prerender content, an asset has the
  wrong MIME type, an alternate trailing-slash URL does not redirect, or an
  unknown document does not return `404`.
- In Google Search Console, inspect the live rendered HTML for all sitemap URLs,
  submit `/sitemap.xml`, request recrawling after material releases, and review
  Page Indexing plus Core Web Vitals before calling a deployment SEO-ready.

The canonical public hostname is `https://www.prettymodels.ai/`; the apex domain
should continue to redirect there.

## Updating research data

- Replace `data/full_weights - raw.csv`, then update all three fields in
  `data/research_metadata.json`. The SHA-256 must match the score CSV; otherwise
  the app stops instead of publishing a stale model date or version.
- Add the new `WFMARYLIN1-PriceData-YYYYMMDDHHMMSS.csv` export and remove the old
  one. The app automatically selects the newest timestamped export.
- Append the latest month to `data/marylin_performance.csv`. Its last date is
  used automatically in chart captions and disclosures.
- Before deployment, run `python3 -m py_compile data.py content.py lab.py
  legal_disclosures.py streamlit_app.py` and start the app locally. The data
  loaders validate required columns, dates, duplicate assets and metadata.
