# Legal deployment checklist

This checklist records factual and operational items that source-code wording
cannot prove. Complete it before publishing the replacement site and whenever
the service, research process, operator details, or financial interests change.

## Provider information

- [ ] Confirm that `Christian Tausch` is the correct legal service provider and
  that `PrettyModels AI` is only a project/trade name, not a separate company.
- [ ] Add a telephone number or another genuinely rapid, direct contact method
  if required for the operator's setup. Email alone may not satisfy every
  application of § 5(1)(2) DDG.
- [ ] Add every applicable register name/number, competent supervisory
  authority, regulated-profession information, VAT ID (§ 27a UStG), or business
  identification number (§ 139c AO). Do not publish a private tax number.
- [ ] Confirm the § 36 VSBG statement is factually correct and that the website
  does not conclude consumer contracts.
- [ ] Confirm whether a data protection officer is legally required or has been
  appointed; if so, publish the officer's contact details in the privacy notice.

## Privacy and infrastructure

- [ ] Execute/retain Article 28 GDPR data-processing agreements with
  DigitalOcean and IONOS; document subprocessors and the transfer assessment.
- [ ] Confirm the DigitalOcean server region and any third-country support
  access. Retain evidence of the EU–U.S. DPF status and SCC fallback.
- [ ] Configure Nginx/application access and error logs to delete or anonymise
  after 14 days, with restricted exceptional retention for documented incidents
  or claims. The privacy notice promises this schedule.
- [ ] Verify the production process reads `.streamlit/config.toml` and that
  `browser.gatherUsageStats = false` is effective. A clean browser load must not
  contact `data.streamlit.io`, `webhooks.fivetran.com`, Google Fonts, analytics,
  advertising, or social-media pixel endpoints.
- [ ] Re-audit browser storage and cookies after every Streamlit upgrade. Only
  technically necessary session/security storage may load before consent.
- [ ] Update the privacy notice *before* enabling a form, wishlist persistence,
  account/login, newsletter, analytics, embeds, error-reporting SaaS, CDN, or a
  new data source. Add consent controls before any nonessential terminal access.
- [ ] Confirm IONOS mailbox deletion/archiving rules match section 6 of the
  privacy notice, and do not retain ordinary inquiries indefinitely.
- [ ] Maintain a GDPR processing record and an incident-response procedure even
  if no public form is offered.

## Research, performance, and financial regulation

- [ ] Obtain German/EU financial-regulatory counsel's written assessment of the
  scores, rankings, model portfolio, social posts, Wikifolio link, and trader
  remuneration under MAR Article 20 / Delegated Regulation (EU) 2016/958, WpIG,
  MiFID II, UWG, and applicable prospectus/financial-promotion rules. A
  “not investment advice” label does not decide the legal classification.
- [ ] Before each publication, record producer/editor, exact date and time,
  model/methodology version, material sources and assumptions, planned update
  frequency, corrections, and whether the output changed after issuer contact.
- [ ] Maintain an instrument-specific conflict register. Prominently disclose
  relevant personal/related-party holdings, transactions, issuer relationships,
  compensation, and any net long/short position above a regulatory threshold.
  The general conflict paragraph does not replace specific MAR disclosures.
- [ ] Confirm the Wikifolio trader's actual remuneration eligibility, current
  performance fee, certificate fee, first issue date, issuer, ISIN, and invested
  capital. Update disclosures immediately when any item changes.
- [ ] Confirm that performance data is the Wikifolio reference-index series and
  that “return difference” is calculated consistently for every benchmark.
  Preserve source downloads and calculation code for auditability.
- [ ] Keep pre-certificate reference-portfolio performance visibly separate
  from certificate-investor performance. Never describe the December 2024 start
  as the start of an investable or publicly traded certificate.
- [ ] Reconcile every headline, chart, social post, and external profile with the
  site disclosures. Remove absolute or unsubstantiated claims such as “proven,”
  “beat the market,” “compounds faster than ETFs,” or “investment manager.”
- [ ] Document human review and editorial responsibility for AI-assisted public-
  interest content, plus the AI tools and review procedure used after 2 August
  2026 (EU AI Act Article 50).

## Release

- [ ] Deploy the repository version and verify `/`, `/research-disclosures`,
  `/legal-notice`, and `/privacy-policy` without authentication or broken links.
- [ ] Inspect the raw HTML response for each route and confirm the title,
  description, canonical URL, Open Graph/Twitter card, favicon and JSON-LD are
  present before JavaScript runs. Confirm the retired “Beat the market”
  description and Streamlit crown are absent.
- [ ] Verify `/robots.txt`, `/sitemap.xml`, `/favicon.ico`, the web manifest and
  the 1200×630 social image return `200` from the canonical `www` hostname.
- [ ] Re-scrape the homepage in the LinkedIn Post Inspector and any other social
  networks used for publication so their cached preview is refreshed.
- [ ] Remove the old deployment and retired `docs.prettymodels.ai` links from all
  search profiles, social profiles, and cached navigation under the operator's
  control.
- [ ] Capture dated screenshots/network evidence of the deployed legal pages and
  retain the exact source revision that was published.
- [ ] Schedule quarterly legal/factual review and an immediate review after any
  material product, law, provider, data-flow, fee, or methodology change.
