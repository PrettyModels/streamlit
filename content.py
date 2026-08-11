"""All public copy for the PrettyModels AI research-lab site."""

# --- Masthead / meta ---------------------------------------------------------
BRAND = "PrettyModels AI"
TAGLINE = "AI Research Lab"
# Crawlers never wait for Streamlit's websocket, so the tags they actually read
# are injected by deploy/nginx/http-metadata-map.conf. These constants set the
# browser tab title and must be kept in step with that map's `default` values.
PAGE_TITLE = "PrettyModels AI — Testing LLMs on Public-Market Outcomes"
PAGE_ICON = "static/favicon-32x32.png"
PAGE_DESCRIPTION = (
    "Can large language models evaluate public companies consistently? An AI "
    "research lab that scores a fixed universe monthly and tests the result in public."
)
CANONICAL_URL = "https://www.prettymodels.ai/"

NAV = [
    ("Thesis", "thesis"),
    ("Method", "method"),
    ("Scoring Engine", "scoring-engine"),
    ("Validation", "validation"),
    ("Philosophy", "philosophy"),
]

# --- §0 Abstract / Hero ------------------------------------------------------
# The masthead directly above already carries the brand + lab tagline, so the
# eyebrow and lead don't repeat the introduction; the lead
# opens with the research question itself.
HERO_EYEBROW = "Research brief · Updated monthly"
HERO_HEADLINE = "Testing frontier AI against public-market outcomes."
HERO_LEAD = (
    "We study one question: can large language models evaluate public companies "
    "with enough consistency to inform investment decisions? Our process converts "
    "the qualitative record of a business (filings, disclosures, market data) "
    "into structured scores, builds a portfolio from them, and "
    "measures the result in a public reference portfolio."
)

# --- §1 Thesis ---------------------------------------------------------------
THESIS_SUBTITLE = "The premise of the research"
THESIS_BODY = [
    "Active investing has long depended on human judgment, which is subject to "
    "well-documented behavioral biases — anchoring, overconfidence, loss aversion. "
    "These biases are difficult to remove through discipline alone, and they impose a "
    "persistent, measurable cost on returns.",

    "LLMs (plus harness) are the first systems able to read the unstructured "
    "information that surrounds a company — annual reports, earnings calls, news flow — "
    "and return a structured, repeatable assessment. Whether those assessments are any "
    "good remains an empirical question, and because they are repeatable, it is one we "
    "can put to a proper test.",

    "Our research program follows from that. We translate model assessments into "
    "scores, scores into portfolio weights, and weights into positions, then evaluate "
    "the outcome against public benchmarks, out-of-sample and in the open.",
]
THESIS_PULLQUOTE = (
    """
    Each score the model produces is a hypothesis.<br>
    The market runs the experiment.
    """
)

# --- §2 Method ---------------------------------------------------------------
METHOD_SUBTITLE = "From source material to portfolio"
METHOD_INTRO = (
    "Marylin separates open-ended model judgment from deterministic portfolio "
    "construction. Around each reporting season, the same research sequence is "
    "applied across a defined universe: dated public evidence is assessed through a "
    "consistent analytical framework, converted into comparable scores, and "
    "translated by fixed portfolio rules into a reviewable monthly hypothesis. "
    "Inputs and outputs are retained for out-of-sample evaluation, while human "
    "review remains between the model portfolio and any real-world execution."
)
METHOD_STEPS = [
    ("01", "Corpus", "Source material",
     "The unstructured record of a company: annual reports, earnings-call transcripts, "
     "regulatory disclosures, and current news."),
    ("02", "Prompts", "Structured prompting",
     "A fixed set of prompts is applied to that material by large language models — the "
     "same questions, asked identically across every company and every month."),
    ("03", "Scores", "Quantification",
     "Each response is converted into a numeric score. Every company is rated from 0 to "
     "100 on {n_dim} dimensions, spanning valuation, competitive position, governance, and "
     "return potential."),
    ("04", "Weights", "Aggregation & sizing",
     "The {n_dim} dimensions are aggregated into {n_comp} composite factors, ranked across the "
     "universe, and translated into portfolio weights."),
    ("05", "Portfolio", "Monthly research output",
     "The result is a fully specified model portfolio — the month’s research "
     "hypothesis — carried forward for out-of-sample evaluation."),
]

# --- §3 Scoring Engine -------------------------------------------------------
SCORING_SUBTITLE = "Scores across the research universe, updated monthly"
SCORING_INTRO = (
    "The table below presents the current month’s output — the scores the portfolio is "
    "constructed from. Each company is summarized by {n_comp} composite factors, each "
    "derived from the {n_dim} underlying dimensions. The universe can be sorted, companies "
    "compared, and any single company examined factor by factor."
)
# Five composite factors surfaced in the interactive tools.
GLOSSARY_SUBTITLE = "The {n_comp} composite factors"
GLOSSARY = [
    ("Integrity", "Governance quality, management conduct, and the reliability of "
                  "reported earnings."),
    ("Market", "Momentum, sentiment, and indications of mispricing in the current "
               "market."),
    ("Quality", "Durability of the business model: competitive moat, scalability, and "
                "pricing power."),
    ("Resilience", "Downside protection: defensiveness and distance from financial "
                   "distress."),
    ("Upside", "Asymmetric return potential: growth, disruption, and the probability of "
               "an outsized outcome."),
]
SCORING_TABLE_CAPTION = (
    "Highlighted cells indicate the top-scoring company on each factor."
)
RESEARCH_UPDATE_FREQUENCY = "monthly"
TAB_EXPLORE = "Explore scores"
TAB_COMPARE = "Compare companies"
TAB_ANALYZE = "Analyze a company"

# --- §4 Live Validation ------------------------------------------------------
VALIDATION_SUBTITLE = "Public reference record"
VALIDATION_INTRO = (
    "Back-tests are easy to flatter: with enough tuning, most strategies look good on "
    "data they have already seen. Since 27 December 2024, Marylin has therefore been "
    "recorded as a public Wikifolio reference portfolio, with positions and changes "
    "published on the third-party platform."
)
VALIDATION_INDEX_CAPTION = (
    "Marylin Wikifolio reference-index level, shown against "
    "a nominal base of 100."
)
VALIDATION_ALPHA_CAPTION = (
    "Cumulative simple return difference versus three public benchmarks; this is not "
    "risk-adjusted or regression alpha."
)
VALIDATION_NOTE = (
    "These figures are research observations, not investor returns or a performance "
    "promise. Comparisons may differ in fees, spreads, currency, taxes, risk and "
    "investability. Past performance is not a reliable indicator of future results. "
    "Read the Research & Risk Disclosures before interpreting them."
)
VALIDATION_VERIFY = "Verify the portfolio on Wikifolio ↗"
WIKIFOLIO_URL = "https://www.wikifolio.com/en/int/w/wfmarylin1"

# Limitations coda to §4 — what the live record does not yet establish. Stated
# plainly, as a research lab should, and consistent with the no-solicitation stance.
OPEN_QUESTIONS_SUBTITLE = "Open questions"
OPEN_QUESTIONS = [
    ("01", "Durability",
     "Will the result persist through market regimes unlike the one in which the "
     "public record began?"),
    ("02", "Model risk",
     "Do consistent assessments add independent signal, or consistently reproduce "
     "biases in their evidence and training?"),
    ("03", "Attribution",
     "How much of the measured return difference is distinct from exposures already "
     "described by academic finance?"),
]
OPEN_QUESTIONS_NOTE = (
    "The record is still short. The lab keeps these questions open on purpose — and "
    "tests them where the answers can hurt: in public, out of sample."
)

# --- §5 Philosophy -----------------------------------------------------------
PHILOSOPHY_SUBTITLE = "Intelligent models for the age of cheap intelligence"
PHILOSOPHY_BODY = [
    "Machine learning ended a century of argument about whether machines could think, "
    "and it ended it rudely: engineers multiplied matrices until judgment fell out. "
    "Nobody has proven that intelligence is mathematics, but enough of it turned out "
    "to be — reading, weighing, arguing, deciding — that the distinction stopped "
    "mattering commercially. Thinking is now sold by the token and metered like "
    "electricity, and the price falls every quarter. Every earlier age treated "
    "judgment as the scarcest input in the economy. Ours is the first that must ask "
    "what changes when it is cheap.",

    "Investing feels the change first, because investing was always two jobs bundled "
    "together: knowing things and staying sane. The old masters preached that "
    "temperament beats intellect; they meant it as a warning about human nature, and "
    "we read it as an engineering specification. A machine can now do the knowing for "
    "anyone — every filing, every footnote, every cycle since records began. It also "
    "supplies the staying sane: no grudge against a position, no urge to average "
    "down, no story needed to sleep at night. Markets were never short of brains; "
    "they were short of temperament, and temperament just became manufacturable.",

    "The deeper consequence lands on everyone who has never read a filing. Financial "
    "under-education is the most expensive illiteracy there is, and an entire industry "
    "has profited by selling average products, designed for the average, at prices that "
    "are anything but. Cheap intelligence attacks that gap from "
    "below. An agent that reads every disclosure, knows its owner’s situation, and "
    "flatters nobody will soon cost less than a lunch — the first honest analyst most "
    "households will ever employ. For the young, entering markets with decades of "
    "compounding ahead of them, finance is about to become hyper-personal, and "
    "ignorance stops being the default setting of wealth.",

    "Abundance has a by-product: infinite plausible opinions. When anyone can "
    "generate a convincing investment thesis in eight seconds, theses are worth "
    "nothing and verification becomes the scarce good. That scarcity is where this "
    "lab works. We build models that place their judgments in the open and let the "
    "market grade the temperament we claim to have engineered.",
]
PHILOSOPHY_PULLQUOTE = (
    """
    All to answer one question:<br>
    Can AI beat the market?
    """
)

# --- Footer ------------------------------------------------------------------
# NOTE: rendered inside an HTML container, so links are <a> tags, not markdown.
ENTITY_NOTE = (
    """
    <h4>Ecosystem</h4>
    <a href=\"https://prettymodels.ai\">prettymodels.ai</a> conducts the research and develops the models.<br> 
    <a href=\"https://quant-unit.com\">quant-unit.com</a> is the personal blog of founder Christian Tausch.
    """
)
DISCLAIMER = """
**Important disclosures.** AI-assisted, human-reviewed research; model outputs can be
wrong. This is general, impersonal information—not personalised advice, an offer or a
performance promise. Capital is at risk. Christian Tausch also operates the Marylin
Wikifolio and may be entitled to performance-linked remuneration, creating a direct
conflict of interest. A label cannot override the legal character of the content. Read the
[Research & Risk Disclosures](/research-disclosures). © PrettyModels AI 2026.
"""

# Footer link row: external profiles plus the internal legal pages (whose
# url_paths are registered in streamlit_app.py, replacing the retired
# docs.prettymodels.ai subdomain).
FOOTER_LINKS = [
    ("LinkedIn", "https://www.linkedin.com/company/prettymodels-ai"),
    ("The Story of Marylin", "https://quant-unit.com/the-story-of-marylin-pt-1/"),
    ("Risk Disclosures", "/research-disclosures"),
    ("Legal Notice / Imprint", "/legal-notice"),
    ("Privacy", "/privacy-policy"),
]


# --- Legal pages =============================================================
# The docs.prettymodels.ai subdomain is retired; its legal notice (German
# Impressum, § 5 DDG) and privacy policy now live here as native pages that
# inherit the paper design system.
LEGAL_BACK = "← Back to the research"

# --- Legal notice / Impressum ------------------------------------------------
IMPRINT_PAGE_TITLE = "Legal Notice — PrettyModels AI"
IMPRINT_EYEBROW = "PrettyModels AI · Legal"
IMPRINT_TITLE = "Legal Notice / Impressum"
IMPRINT_UPDATED = "11 August 2026"
IMPRINT_INTRO = (
    "Provider information pursuant to § 5 DDG and editorial responsibility pursuant "
    "to § 18(2) MStV."
)
IMPRINT_SECTIONS = [
    ("Service provider and operator", [
        "Christian Tausch, operating under the project name PrettyModels AI<br>"
        "Ben-Chorin-Str. 1<br>80339 Munich<br>Germany",
        "Email: <a href='mailto:team@prettymodels.ai'>team@prettymodels.ai</a>",
        "PrettyModels AI is not identified on this site as a separate legal person. "
        "Christian Tausch is responsible for this service and its content.",
    ]),
    ("Editorial responsibility", [
        "Responsible for editorial content pursuant to § 18(2) MStV: "
        "Christian Tausch (address as above).",
    ]),
    ("Research and financial disclosures", [
        "The site publishes model research about financial instruments and links to "
        "the Marylin Wikifolio. Important information about the operator’s economic "
        "interest, model limitations, risk and performance presentation appears in "
        "the <a href='/research-disclosures'>Research &amp; Risk Disclosures</a>. "
        "Those disclosures form an integral part of every research output on this site.",
    ]),
    ("External links", [
        "External services are operated under their providers’ responsibility. A link "
        "does not mean that we adopt all third-party content as our own. If we learn "
        "that linked content is unlawful, we will review and remove the link where "
        "required.",
    ]),
    ("Copyright", [
        "Unless stated otherwise, operator-created text, graphics and code are protected "
        "by applicable copyright law. Uses beyond statutory permissions require prior "
        "consent. Quotation, private-copy and other mandatory statutory exceptions "
        "remain unaffected. Third-party names, data and marks belong to their respective "
        "owners.",
    ]),
    ("Liability", [
        "Nothing on this site creates a guarantee of accuracy, completeness, timeliness, "
        "availability or a particular result. The specific research and investment-risk "
        "limitations are set out in the Research &amp; Risk Disclosures.",
        "Nothing in these notices excludes or limits liability where exclusion is not "
        "permitted by law, including liability for intent or gross negligence, injury to "
        "life, body or health, fraudulently concealed defects, an expressly assumed "
        "guarantee, or mandatory statutory liability. Where liability for ordinary "
        "negligence may lawfully be limited, it is limited to breach of an essential "
        "obligation and to the foreseeable damage typical for that kind of breach.",
    ]),
    ("Consumer dispute resolution", [
        "No consumer contracts are concluded through this website. The operator is "
        "neither willing nor obliged to participate in dispute-resolution proceedings "
        "before a consumer arbitration board (§ 36 VSBG).",
    ]),
]

# --- Privacy policy ----------------------------------------------------------
PRIVACY_PAGE_TITLE = "Privacy Policy — PrettyModels AI"
PRIVACY_EYEBROW = "PrettyModels AI · Legal"
PRIVACY_TITLE = "Privacy Policy"
PRIVACY_UPDATED = "11 August 2026"
PRIVACY_INTRO = (
    "This notice provides the information required by Articles 12–14 GDPR. Merely "
    "visiting the site is not consent to data processing. We process only the data "
    "described below and rely on the stated legal basis for each purpose."
)
PRIVACY_SECTIONS = [
    ("1. Controller", [
        "Christian Tausch — PrettyModels AI<br>Ben-Chorin-Str. 1<br>"
        "80339 Munich, Germany<br>Email: "
        "<a href='mailto:team@prettymodels.ai'>team@prettymodels.ai</a>",
        "Privacy requests can be sent to the contact above.",
    ]),
    ("2. Website delivery and server logs", [
        "When you request a page, our server necessarily processes the IP address, date "
        "and time, requested URL and response status, amount of data transferred, "
        "referrer (if sent), and browser/operating-system and protocol information. "
        "This is required to deliver the site, keep it stable and secure, diagnose "
        "errors and investigate abuse.",
        "The legal basis is Article 6(1)(f) GDPR. Our legitimate interests are secure, "
        "reliable and efficient publication of the research service and defence against "
        "misuse and legal claims. Access and error logs under our control are scheduled "
        "for deletion or anonymisation after 14 days, unless an identified security "
        "incident or legal claim requires relevant entries to be retained until it is "
        "resolved.",
        "The server is hosted on infrastructure of DigitalOcean, LLC, 105 Edgeview "
        "Drive, Suite 425, Broomfield, CO 80021, USA, acting as a processor. See "
        "DigitalOcean’s <a href='https://www.digitalocean.com/legal/privacy-policy/' "
        "target='_blank' rel='noopener'>privacy policy</a> and "
        "<a href='https://www.digitalocean.com/legal/data-processing-agreement' "
        "target='_blank' rel='noopener'>data-processing terms</a>.",
    ]),
    ("3. Local storage, cookies and telemetry", [
        "We do not use advertising pixels, marketing cookies, audience measurement or "
        "cross-site profiling. Optional Streamlit usage telemetry is disabled in the "
        "application configuration.",
        "The Streamlit framework may use short-lived session identifiers or browser "
        "storage strictly necessary to maintain the interactive connection, preserve "
        "the state you request and protect the service. These mechanisms are not used "
        "by us to identify you across sites. To the extent information is stored in or "
        "read from your device for these necessary functions, § 25(2)(2) TDDDG applies; "
        "consent is not required for a function expressly requested by the user.",
    ]),
    ("4. Fonts, media and external links", [
        "Site fonts, images and data files are served from our own host; loading a page "
        "does not require a request to Google Fonts. Third-party services such as "
        "Wikifolio, LinkedIn and Quant-Unit are linked, not embedded. Your browser "
        "contacts those providers only if you follow a link, at which point their own "
        "privacy notices apply.",
    ]),
    ("5. Interactive research tools", [
        "Selections made in tables, sliders and charts are processed transiently in the "
        "Streamlit session so the requested view can be rendered. The public site does "
        "not require an account, assign a user profile, or intentionally store those "
        "selections after the session ends. Do not enter personal or confidential data "
        "into any interactive control.",
    ]),
    ("6. Contact by email", [
        "If you email us, we process your email address, name (if provided), message, "
        "attachments and communication metadata to answer the inquiry and keep an "
        "appropriate record. The legal basis is Article 6(1)(f) GDPR (responding to "
        "inquiries and documenting communications) or, where your request concerns a "
        "possible contract, Article 6(1)(b) GDPR. Providing this information is "
        "voluntary, but we cannot answer without a usable reply address.",
        "Email is provided by IONOS SE, Elgendorfer Str. 57, 56410 Montabaur, Germany, "
        "as a processor. Messages are deleted when the inquiry is conclusively resolved, "
        "unless they must be kept for statutory commercial or tax retention periods or "
        "for the establishment, exercise or defence of legal claims. In those cases, "
        "access is restricted and deletion follows when the applicable period expires.",
    ]),
    ("7. Recipients and disclosure", [
        "We disclose data only to the processors identified above, to professional "
        "advisers bound by confidentiality where necessary, or to public authorities "
        "when a valid legal obligation requires it. We do not sell personal data and do "
        "not use it for newsletters or behavioural advertising.",
    ]),
    ("8. Transfers outside the EEA", [
        "DigitalOcean is established in the United States. Depending on the contracted "
        "server region and support operations, personal data may be accessible from or "
        "transferred to the United States. DigitalOcean states that it participates in "
        "the EU–U.S. Data Privacy Framework and that its data-processing agreement uses "
        "the European Commission’s Standard Contractual Clauses as a fallback. Copies or "
        "information about these safeguards can be requested from us.",
    ]),
    ("9. Your GDPR rights", [
        "Subject to the statutory conditions, you have the right to access your data "
        "(Article 15), rectify inaccurate data (Article 16), erase data (Article 17), "
        "restrict processing (Article 18), receive portable data where applicable "
        "(Article 20), and object to processing based on legitimate interests "
        "(Article 21 GDPR). If processing ever relies on consent, you may withdraw it "
        "for the future at any time.",
        "<strong>Right to object:</strong> You may object at any time, on grounds "
        "relating to your particular situation, to processing based on Article 6(1)(f) "
        "GDPR. We will stop unless compelling legitimate grounds override your interests, "
        "rights and freedoms or the processing is needed for legal claims.",
        "To exercise a right, email "
        "<a href='mailto:team@prettymodels.ai'>team@prettymodels.ai</a>. We may need "
        "reasonable information to verify that the request concerns you.",
    ]),
    ("10. Right to complain", [
        "You may complain to any competent data-protection supervisory authority, in "
        "particular in the Member State of your residence, workplace or the alleged "
        "infringement. The authority responsible for private-sector controllers in "
        "Bavaria is the Bayerisches Landesamt für Datenschutzaufsicht (BayLDA), "
        "Promenade 18, 91522 Ansbach, Germany; "
        "<a href='https://www.lda.bayern.de/de/beschwerde.html' target='_blank' "
        "rel='noopener'>online complaint service</a>.",
    ]),
    ("11. Required data and automated decisions", [
        "Technical request data is necessary to deliver and secure the website; without "
        "it the service cannot be provided. Email contact is voluntary. We do not use "
        "visitor personal data for automated decisions or profiling within Article 22 "
        "GDPR. The models score public companies, not website visitors.",
    ]),
    ("12. Security and changes", [
        "We use proportionate technical and organisational safeguards, including HTTPS, "
        "access controls, updates and data minimisation. No internet service can promise "
        "absolute security. We will update this notice when processing materially "
        "changes and show the revision date above.",
    ]),
]


# --- Research and risk disclosures ------------------------------------------
DISCLOSURE_PAGE_TITLE = "Research & Risk Disclosures — PrettyModels AI"
DISCLOSURE_EYEBROW = "PrettyModels AI · Important information"
DISCLOSURE_TITLE = "Research & Risk Disclosures"
DISCLOSURE_UPDATED = "11 August 2026"
DISCLOSURE_INTRO = (
    "Read this before using any score, ranking, model output or performance figure. "
    "These disclosures are part of every research publication on this site."
)
DISCLOSURE_SECTIONS = [
    ("1. Publisher, editor and update cycle", [
        "Publisher and responsible editor: Christian Tausch, PrettyModels AI, address "
        "and contact details in the <a href='/legal-notice'>Legal Notice</a>. Model "
        f"research is ordinarily refreshed {RESEARCH_UPDATE_FREQUENCY}. The score "
        "dataset currently shown was produced on {scoring_as_of}; benchmark-comparison "
        "data runs through {performance_as_of}, and Wikifolio reference-index data runs "
        "through {reference_index_as_of}. The published research version is "
        "{research_version}. "
        "Outputs are not monitored or updated continuously between publication cycles.",
        "AI systems assist with analysis and drafting. Published material is reviewed "
        "and remains under the human editorial responsibility of Christian Tausch. "
        "The AI-assistance statement is also intended to make the origin of the material "
        "clear under the EU AI Act.",
    ]),
    ("2. General research—not personalised advice", [
        "The material is prepared for a general audience and does not take account of "
        "any person’s knowledge, financial position, objectives, loss capacity, tax "
        "position or risk tolerance. No suitability or appropriateness assessment is "
        "performed. Nothing creates an adviser, fiduciary, client or contractual "
        "relationship with the reader.",
        "The site does not accept orders or conclude transactions. It is not a "
        "prospectus, key information document, offer, invitation or personalised "
        "recommendation. Obtain independent regulated advice and review the issuer’s "
        "current legal documents before considering any financial instrument.",
        "Regulatory classification depends on the substance and context of a publication, "
        "not on a disclaimer. Public model scores, rankings or portfolio information may "
        "constitute an investment recommendation or information suggesting an investment "
        "strategy under applicable market-abuse rules. The identification, methodology, "
        "timing, risk and conflict information on this page is provided on that basis.",
    ]),
    ("3. Model and data limitations", [
        "Scores and rankings are probabilistic research outputs, not facts or trade "
        "instructions. Large language models can hallucinate, misread sources, reproduce "
        "bias, omit material information and change behaviour between versions. Public "
        "filings, transcripts, news and market data can be incomplete, delayed, revised "
        "or wrong. Human review reduces but does not eliminate these risks.",
        "The same labels can conceal different assumptions across issuers. Aggregation "
        "and portfolio sizing amplify model and data errors. No representation is made "
        "that a score measures intrinsic value, predicts a price or is statistically "
        "significant. Reproducibility can be affected by model, prompt, source-corpus and "
        "software changes.",
        "The high-level methodology is described on the main page. Material assumptions "
        "include the selected company universe, source availability, fixed prompt set, "
        "normalisation, composite-factor construction and ranking/weighting rules. The "
        "methodology may change; comparisons across versions may therefore be invalid.",
    ]),
    ("4. Investment risks", [
        "Investments can lose some or all capital. Concentrated, growth-oriented, foreign "
        "currency, small-cap and technology exposures can be especially volatile. Other "
        "risks include liquidity, valuation, model, execution, counterparty, issuer, "
        "currency, political, regulatory, tax and operational risk. Diversification does "
        "not guarantee a profit or prevent loss.",
        "No return, outperformance, level of risk or availability is promised. Past "
        "performance is not a reliable indicator of future results, and a short record "
        "or favourable market regime cannot establish durability.",
    ]),
    ("5. Marylin record and benchmark presentation", [
        "Marylin is a public Wikifolio reference portfolio operated by Christian Tausch "
        "under the profile PrettyModelsAI. The associated Wikifolio certificate is a "
        "third-party investment product. The reference portfolio began in December 2024; "
        "the certificate’s first issue date was 2 September 2025. Pre-issuance figures "
        "are therefore not actual certificate-investor returns.",
        "The chart uses downloaded Wikifolio reference-index levels. The site’s "
        "“cumulative alpha” series is a simple cumulative return difference between the "
        "Marylin series and each named benchmark; it is not regression alpha, does not "
        "control for risk or factor exposures, and carries no claim of statistical "
        "significance. Benchmarks may differ in currency, composition, risk, fees, tax, "
        "rebalancing, investability and calculation time.",
        "Certificate investors may experience a different return because of the issue "
        "date, certificate and performance fees, bid/ask spreads, purchase price, broker "
        "charges, taxes, market hours, tracking and issuer risk. The current product "
        "terms, prospectus, key information document, fees and risk factors are available "
        "only from the issuer/distributor and Wikifolio; their documents control.",
    ]),
    ("6. Material conflicts of interest", [
        "Christian Tausch both publishes this research and operates the Marylin "
        "Wikifolio. The associated certificate has a performance fee. Under Wikifolio’s "
        "published trader-remuneration model, an eligible trader may receive a "
        "performance-linked success bonus representing a share of that fee. The operator "
        "therefore has a direct economic interest in positive performance and in capital "
        "invested in the certificate. This conflicts with an entirely disinterested "
        "presentation of the strategy.",
        "The operator and related persons may also hold, buy or sell instruments discussed "
        "or held in Marylin, before or after publication, and are not required by this site "
        "to trade in line with a model output. The live Wikifolio page shows the reference "
        "portfolio’s disclosed positions and transactions; it does not disclose every "
        "personal account. Readers should assume that the publisher may benefit from "
        "favourable attention to Marylin or to an instrument held by it.",
        "No issuer is stated to have paid for a score or supplied consideration for "
        "coverage. If that changes, the affected publication must carry a specific, "
        "prominent disclosure. Instrument-specific interests that market-abuse rules "
        "require to be disclosed must likewise be added to the affected publication; "
        "this general statement is not a substitute for them.",
    ]),
    ("7. No warranty; legally permitted limits", [
        "Research is supplied without a contractual guarantee of accuracy, completeness, "
        "timeliness, availability, merchantability, fitness for purpose or non-infringement. "
        "You remain responsible for independently checking sources and decisions.",
        "Nothing excludes liability that cannot lawfully be excluded. The qualified "
        "liability provisions in the <a href='/legal-notice'>Legal Notice</a> apply.",
    ]),
]


# --- weaving computed counts into prose --------------------------------------
# The universe counts (score dimensions, composite factors) live in the data,
# not the copy: they are formatted in at render time from data.universe_stats(),
# so the prose can never drift from the actual score set the way a hard-coded
# figure would (see how the stale "37.2%" once did). Small counts are spelled
# out to keep an academic register.
_NUM_WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
              7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
              12: "twelve"}


def num_word(n: int) -> str:
    """Spell out a small integer; fall back to digits above twelve."""
    return _NUM_WORDS.get(n, str(n))


def fill(stats: dict) -> dict:
    """Return the number-bearing copy with the universe counts woven in.

    Keeps content.py the single source of copy while letting lab.py supply the
    counts computed in data.py, so figures like "31 dimensions" stay in sync
    with the score set instead of being hard-coded.
    """
    ctx = {"n_dim": stats["n_dimensions"],
           "n_comp": num_word(stats["n_composites"])}
    return {
        "method_steps": [(n, t, s, d.format(**ctx)) for n, t, s, d in METHOD_STEPS],
        "scoring_intro": SCORING_INTRO.format(**ctx),
        "glossary_subtitle": GLOSSARY_SUBTITLE.format(**ctx),
    }


def fill_disclosures(freshness: dict) -> list[tuple[str, list[str]]]:
    """Weave checksum-verified snapshot metadata into the public disclosures."""
    ctx = {
        "scoring_as_of": freshness["scoring_as_of_label"],
        "performance_as_of": freshness["performance_as_of_label"],
        "reference_index_as_of": freshness["reference_index_as_of_label"],
        "research_version": freshness["research_version"],
    }
    return [
        (heading, [paragraph.format(**ctx) for paragraph in paragraphs])
        for heading, paragraphs in DISCLOSURE_SECTIONS
    ]
