"""
content.py — all copy for the PrettyModels AI research-lab site, kept separate
from layout. Nothing here solicits investment or offers a product: PrettyModels
AI is a research lab; the Marylin index is shown only as out-of-sample research
validation.
"""

# --- Masthead / meta ---------------------------------------------------------
BRAND = "PrettyModels AI"
TAGLINE = "Independent AI Research Lab"
PAGE_TITLE = "PrettyModels AI — Independent AI Research Lab"
PAGE_DESCRIPTION = (
    "PrettyModels AI is an independent research lab studying whether large language "
    "models can evaluate public companies consistently enough to inform investment "
    "decisions, validated on a live public index."
)

NAV = [
    ("Thesis", "thesis"),
    ("Method", "method"),
    ("Scoring Engine", "scoring-engine"),
    ("Validation", "validation"),
    ("Philosophy", "philosophy"),
]

# --- §0 Abstract / Hero ------------------------------------------------------
HERO_EYEBROW = "PrettyModels AI · Independent Research Lab"
HERO_HEADLINE = "Turning frontier AI into public-market investment signals."
HERO_LEAD = (
    "PrettyModels AI is an independent research lab. We study whether large language "
    "models can evaluate public companies with enough consistency to inform investment "
    "decisions. Our process converts the qualitative record of a business — filings, "
    "disclosures, management commentary — into structured scores, combines those scores "
    "into a portfolio, and measures the result on a live, publicly traded index."
)

# --- §1 Thesis ---------------------------------------------------------------
THESIS_SUBTITLE = "The premise of the research"
THESIS_BODY = [
    "Active investing has long depended on human judgment, which is subject to "
    "well-documented behavioral biases — anchoring, overconfidence, loss aversion. "
    "These biases are difficult to remove through discipline alone, and they impose a "
    "persistent, measurable cost on returns.",

    "Large language models are the first systems able to read the unstructured "
    "information that surrounds a company — annual reports, earnings calls, news flow — "
    "and return a structured, repeatable assessment. This does not make their judgments "
    "correct. It makes them consistent, and consistency is what can be measured.",

    "Our research program follows from that distinction. We translate model assessments "
    "into scores, scores into portfolio weights, and weights into positions, then "
    "evaluate the outcome against public benchmarks, out-of-sample and in the open.",
]
THESIS_PULLQUOTE = (
    "A model’s judgment is not an answer. It is a hypothesis, to be tested against the "
    "market."
)

# --- §2 Method ---------------------------------------------------------------
METHOD_SUBTITLE = "From source material to portfolio"
METHOD_INTRO = (
    "The same process runs each month, end to end. It is designed to be fully "
    "traceable: every position in the portfolio can be followed back through its factor "
    "weights and scores to the source material the model was asked to evaluate."
)
METHOD_STEPS = [
    ("01", "Qualitative", "Source material",
     "The unstructured record of a company: annual reports, earnings-call transcripts, "
     "regulatory disclosures, and current news."),
    ("02", "Prompts → AI", "Structured prompting",
     "A fixed set of prompts is applied to that material by large language models — the "
     "same questions, asked identically across every company and every month."),
    ("03", "Scores", "Quantification",
     "Each response is converted into a numeric score. Every company is rated from 0 to "
     "100 on 31 dimensions, spanning valuation, competitive position, governance, and "
     "return potential."),
    ("04", "Weights", "Aggregation & sizing",
     "The 31 dimensions are aggregated into five composite factors, ranked across the "
     "universe, and translated into portfolio weights."),
    ("05", "Signal", "Monthly output",
     "The result is a fully specified target portfolio — the month’s signal — carried "
     "forward for out-of-sample evaluation."),
]

# --- §3 Scoring Engine -------------------------------------------------------
SCORING_SUBTITLE = "Scores across the investable universe, updated monthly"
SCORING_INTRO = (
    "The tables below present the current month’s output — the scores the portfolio is "
    "constructed from. Each company is summarized by five composite factors, each "
    "derived from the 31 underlying scores. The universe can be sorted, companies "
    "compared, and any single company examined factor by factor."
)
# Five composite factors surfaced in the interactive tools.
GLOSSARY_SUBTITLE = "The five composite factors"
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
TAB_EXPLORE = "Explore scores"
TAB_COMPARE = "Compare companies"
TAB_ANALYZE = "Analyze a company"

# --- §4 Live Validation ------------------------------------------------------
VALIDATION_SUBTITLE = "Out-of-sample, in public"
VALIDATION_INTRO = (
    "A back-test can be fitted to historical data; a forward test cannot. Since "
    "27 December 2024 the Marylin strategy has been implemented as a live, publicly "
    "traded Wikifolio index, with every position disclosed and priced daily. The results "
    "below are therefore out-of-sample."
)
VALIDATION_INDEX_CAPTION = "Marylin index level, indexed to 100 at inception."
VALIDATION_ALPHA_CAPTION = (
    "Cumulative alpha of the strategy relative to three public benchmarks."
)
VALIDATION_NOTE = (
    "These figures are presented for research transparency. Past performance is not "
    "indicative of future results, and nothing on this page constitutes investment "
    "advice or an offer of any product."
)
VALIDATION_VERIFY = "View the live index on Wikifolio ↗"
WIKIFOLIO_URL = "https://www.wikifolio.com/en/int/w/wfmarylin1"

# --- §5 Philosophy -----------------------------------------------------------
PHILOSOPHY_SUBTITLE = "The principle behind the name"
PHILOSOPHY_BODY = [
    "In statistical modeling, elegance is not decoration. A model that must be supported "
    "by special cases, manual overrides, and the modeler’s conviction is fragile; a "
    "model that reaches the same conclusion from the evidence alone is robust. We use "
    "the word *pretty* in that narrower, technical sense: a model reduced to what the "
    "data supports, and no more.",

    "The same principle governs the behavior a model removes. Human investors carry "
    "biases that are difficult to suppress — attachment to existing positions, the need "
    "to be proven right, the impulse to sell under pressure. A model carries none of "
    "them. It evaluates the available evidence and ranks it, and the discipline this "
    "imposes is the point of the exercise.",

    "The lab is therefore not organized around a single insight or forecast. It is "
    "organized to produce models that can be examined, challenged, and improved, and to "
    "let performance be settled in public rather than asserted. Marylin, the strategy we "
    "run live, is the current expression of that approach.",
]
PHILOSOPHY_PULLQUOTE = (
    "Elegance, in a model, is the absence of everything the evidence does not require."
)

# --- Footer ------------------------------------------------------------------
# NOTE: rendered inside an HTML container, so the link is an <a> tag, not markdown.
ENTITY_NOTE = (
    "PrettyModels AI conducts the research and develops the models.<br> The Marylin strategy "
    "is operated as a live portfolio by <a href=\"https://tausch.capital\">tausch.capital</a>."
)
DISCLAIMER = """
**Disclaimer**

**1. General information & AI nature.** This content is generated with the help of
artificial intelligence and is for informational and research purposes only. The
"scores", "factors" and "signals" are outputs of probabilistic models and large language
models, and may contain errors, hallucinations or biases. Do not rely on this content as
a definitive source of truth.

**2. No investment advice.** Nothing here constitutes financial, legal, tax or investment
advice, nor a recommendation to buy, sell or hold any security or to adopt any strategy.
It does not consider your circumstances, objectives or risk tolerance. Consult a
qualified professional before making any investment decision.

**3. No offer or solicitation.** This material is not an offer to sell or a solicitation
of an offer to buy any security, investment product or service in any jurisdiction.

**4. Risk warning.** Past performance is not indicative of future results. All investment
involves significant risk, including total loss of principal. AI-driven models are
experimental; any hypothetical or back-tested results shown have inherent limitations.

**5. Conflicts of interest.** PrettyModels AI, its affiliates and their officers may hold
positions in, or transact in, the securities or instruments discussed. The lab's outputs
may align with or contradict those positions.

**6. Limitation of liability.** Content is provided "as is", without warranties of any
kind. PrettyModels AI disclaims liability for any direct, indirect, consequential or
incidental damages arising from use of, or reliance on, this information.

© PrettyModels AI 2026. All rights reserved.
"""

LINK_LINKEDIN = ("LinkedIn", "https://www.linkedin.com/company/prettymodels-ai")
LINK_DOCS = ("Research notes", "https://docs.prettymodels.ai")
LINK_STORY = ("The story of Marylin", "https://quant-unit.com/the-story-of-marylin-pt-1/")
