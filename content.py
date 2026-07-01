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
    "PrettyModels AI is an independent research lab building AI-driven algorithms "
    "that turn frontier language models into quantitative, public-market signals."
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
    "PrettyModels AI is an independent research lab. We build algorithms that let "
    "frontier language models read the qualitative world — filings, disclosures, the "
    "narrative of a business — and distil it into quantitative conviction. Then we "
    "test that conviction the only honest way: out-of-sample, on a live, publicly "
    "traded index."
)
HERO_PLATE_CAPTION = "Plate 1 — “Marylin”, the lab’s flagship AI strategy."

# --- §1 Thesis ---------------------------------------------------------------
THESIS_SUBTITLE = "Why an AI lab for public markets"
THESIS_BODY = [
    "For a century, active investing has been limited by biology. Human analysts are "
    "flawed hardware — anchored, over-confident, moved by fear and narrative. No amount "
    "of discipline fully removes the bias, and the bias quietly erodes returns.",

    "Large language models change the terms of the problem. For the first time we have "
    "statistical engines that can digest the chaotic, qualitative noise of the world — "
    "annual reports, transcripts, news — and organise it into structured reasoning. The "
    "edge in markets is no longer held by whoever reads the most; it is held by whoever "
    "commands the superior statistical mind.",

    "This lab exists to build that mind for public markets, and to hold it to account. "
    "We turn language into scores, scores into conviction, and conviction into a signal "
    "that can be measured — in public, against the market, over time.",
]
THESIS_PULLQUOTE = (
    "The edge is shifting from the analyst who reads the most to the model that reasons "
    "the best."
)

# --- §2 Method ---------------------------------------------------------------
METHOD_SUBTITLE = "How the lab turns language into signal"
METHOD_INTRO = (
    "Every month the same pipeline runs end to end. Each stage is deterministic in "
    "structure and transparent in output, so a signal can be traced back from a "
    "portfolio weight all the way to the sentence that produced it."
)
METHOD_STEPS = [
    ("01", "Qualitative", "The raw material",
     "The unstructured world of a company: filings, disclosures, transcripts, news — "
     "the narrative that no spreadsheet captures."),
    ("02", "Prompts → AI", "Frontier models, guided",
     "Large language models read that material through structured research prompts, "
     "each posing a precise, repeatable question about the business."),
    ("03", "Scores", "Language becomes numbers",
     "Every company is rated 0–100 on 31 dimensions — valuation, moat, governance, "
     "disruption, ten-bagger odds and more — refreshed monthly."),
    ("04", "Weights", "Conviction, sized",
     "Scores are combined into five composite factors, ranked across the universe, and "
     "translated into growth-optimal conviction weights."),
    ("05", "Signal", "A testable portfolio",
     "The result is a fully specified target portfolio — the lab’s monthly signal, ready "
     "to be validated out-of-sample."),
]

# --- §3 Scoring Engine -------------------------------------------------------
SCORING_SUBTITLE = "Every month, our models score the investable universe"
SCORING_INTRO = (
    "The tables and tools below are the lab’s live output, not a static screenshot. "
    "Each company is distilled into five composite factors — themselves built from 31 "
    "underlying AI scores. Explore the universe, compare companies, or take one apart "
    "factor by factor."
)
# Five composite factors surfaced in the interactive tools.
GLOSSARY_SUBTITLE = "The five composite factors"
GLOSSARY = [
    ("Integrity", "Governance, management quality and clean, honest earnings — is the "
                  "business run for its owners?"),
    ("Market", "Momentum, sentiment and mispricing — what the market is currently "
               "saying about the name."),
    ("Quality", "Durability of the business: moat, scalability and competitive "
                "advantage that compounds."),
    ("Resilience", "Downside protection: defensiveness and distance from financial "
                   "distress when conditions turn."),
    ("Upside", "Asymmetric return potential: growth, disruption and the odds of an "
               "outsized long-run outcome."),
]
SCORING_TABLE_CAPTION = (
    "Figure 2 — Composite-factor scores across the universe (green marks the top-ranked "
    "company on each factor)."
)
TAB_EXPLORE = "Explore scores"
TAB_COMPARE = "Compare companies"
TAB_ANALYZE = "Analyze a company"

# --- §4 Live Validation ------------------------------------------------------
VALIDATION_SUBTITLE = "Out-of-sample, in public"
VALIDATION_INTRO = (
    "A backtest can always be fit to the past. To test the research honestly, we deploy "
    "the signal into a real, publicly traded index and track it forward. Since "
    "27 December 2024 the Marylin strategy has traded live as a Wikifolio index — every "
    "position public, every day marked to market."
)
VALIDATION_INDEX_CAPTION = (
    "Figure 3 — Marylin Wikifolio index level (base 100 at inception)."
)
VALIDATION_ALPHA_CAPTION = (
    "Figure 4 — Cumulative alpha of the signal versus three public benchmarks."
)
VALIDATION_NOTE = (
    "The Marylin index is operated by Until Singularity Asset Management "
    "([tausch.capital](https://tausch.capital)). Figures are shown for research "
    "transparency only. Past performance does not indicate future results and nothing "
    "here is investment advice or an offer of any product."
)
VALIDATION_VERIFY = "Verify the live index on Wikifolio ↗"
WIKIFOLIO_URL = "https://www.wikifolio.com/en/int/w/wfmarylin1"

# --- §5 Philosophy -----------------------------------------------------------
PHILOSOPHY_SUBTITLE = "Why we call them pretty models"
PHILOSOPHY_BODY = [
    "True elegance in finance is rare, because it requires the removal of the ego. For "
    "centuries people have tried to beat markets on gut instinct, confusing luck with "
    "genius and anxiety with insight. The result is usually the same: a chaotic, ugly "
    "portfolio where emotion erodes returns.",

    "We hold a different view. A model is only *pretty* when it is stripped of human "
    "folly — when nothing is left but the raw, unvarnished probability of an edge. A "
    "pretty model does not hope and does not panic. It does not care about sentiment or "
    "the narrative of the day. It weighs the evidence and it ranks.",

    "So the work of the lab is not to be the genius. It is to build the quiet, "
    "disciplined system that can be measured, questioned and improved — and to let the "
    "most beautiful model be the one that simply, and transparently, does its job.",
]
PHILOSOPHY_PULLQUOTE = (
    "A pretty model does not hope, and it does not panic. It weighs the evidence and it "
    "ranks."
)

# --- Footer ------------------------------------------------------------------
ENTITY_NOTE = (
    "PrettyModels AI is an independent research lab. It does not manage money or offer "
    "investment products. The Marylin index referenced on this site is operated "
    "separately by Until Singularity Asset Management (tausch.capital)."
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
