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
# The masthead directly above already carries the brand + "Independent AI Research
# Lab" tagline, so the eyebrow and lead don't repeat the introduction; the lead
# opens with the research question itself.
HERO_EYEBROW = "Research brief · Updated monthly"
HERO_HEADLINE = "Turning frontier AI into public-market investment signals."
HERO_LEAD = (
    "We study one question: can large language models evaluate public companies "
    "with enough consistency to inform investment decisions? Our process converts "
    "the qualitative record of a business — filings, disclosures, market "
    "data — into structured scores, builds a portfolio from them, and "
    "measures the result on a live, publicly traded index."
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
    "and return a structured, repeatable assessment. Whether those assessments are any "
    "good remains an empirical question, and because they are repeatable, it is one we "
    "can put to a proper test.",

    "Our research program follows from that. We translate model assessments into "
    "scores, scores into portfolio weights, and weights into positions, then evaluate "
    "the outcome against public benchmarks, out-of-sample and in the open.",
]
THESIS_PULLQUOTE = (
    "Each score the model produces is a hypothesis; the market runs the experiment."
)

# --- §2 Method ---------------------------------------------------------------
METHOD_SUBTITLE = "From source material to portfolio"
METHOD_INTRO = (
    "The same process runs each month, end to end. It is designed to be auditable: "
    "every position can be traced back through its factor weights and scores to the "
    "source material the model evaluated."
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
    ("05", "Signal", "Monthly output",
     "The result is a fully specified target portfolio — the month’s signal — carried "
     "forward for out-of-sample evaluation."),
]

# --- §3 Scoring Engine -------------------------------------------------------
SCORING_SUBTITLE = "Scores across the investable universe, updated monthly"
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
TAB_EXPLORE = "Explore scores"
TAB_COMPARE = "Compare companies"
TAB_ANALYZE = "Analyze a company"

# --- §4 Live Validation ------------------------------------------------------
VALIDATION_SUBTITLE = "Out-of-sample, in public"
VALIDATION_INTRO = (
    "Back-tests are easy to flatter: with enough tuning, most strategies look good on "
    "data they have already seen. Since 27 December 2024 the Marylin strategy has "
    "therefore run as a live, publicly traded Wikifolio index — every position "
    "disclosed, priced daily, and impossible to revise after the fact. Everything "
    "below is out-of-sample."
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

# Limitations coda to §4 — what the live record does not yet establish. Stated
# plainly, as a research lab should, and consistent with the no-solicitation stance.
OPEN_QUESTIONS_SUBTITLE = "Open questions"
OPEN_QUESTIONS_BODY = [
    "The live series is short, and one favorable market cycle proves little about "
    "durability. A consistent model can still be consistently wrong, or can faithfully "
    "reproduce whatever biases its training data carries. And part of the measured "
    "alpha may turn out to be exposure to factors that academic finance named decades "
    "ago.",

    "The lab keeps these questions open on purpose, and keeps testing them where the "
    "answers can hurt: in public, out-of-sample.",
]

# --- §5 Philosophy -----------------------------------------------------------
PHILOSOPHY_SUBTITLE = "Pretty models for the age of cheap intelligence"
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
    "under-education is the most expensive illiteracy there is, and a whole industry "
    "has quietly billed it by the hour. Cheap intelligence attacks that gap from "
    "below. An agent that reads every disclosure, knows its owner’s situation, and "
    "flatters nobody will soon cost less than a lunch — the first honest analyst most "
    "households will ever employ. For the young, entering markets with decades of "
    "compounding ahead of them, finance is about to become hyper-personal, and "
    "ignorance stops being the default setting of wealth.",

    "Abundance has a by-product: infinite plausible opinions. When anyone can "
    "generate a convincing investment thesis in eight seconds, theses are worth "
    "nothing and verification becomes the scarce good. That scarcity is where this "
    "lab works. We build models that place their judgments in the open and let the "
    "market grade the temperament we claim to have engineered. A *pretty* model, in "
    "the age of cheap intelligence, is one that keeps its figure in public — every "
    "position disclosed, every month scored. Marylin is ours; her scoreboard is §4.",
]
PHILOSOPHY_PULLQUOTE = (
    "Intelligence is now sold by the token. A track record still has to be earned "
    "the slow way."
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

# Footer link row: external profiles plus the internal legal pages (whose
# url_paths are registered in streamlit_app.py, replacing the retired
# docs.prettymodels.ai subdomain).
FOOTER_LINKS = [
    ("LinkedIn", "https://www.linkedin.com/company/prettymodels-ai"),
    ("The Story of Marylin", "https://quant-unit.com/the-story-of-marylin-pt-1/"),
    ("Legal Notice", "/legal-notice"),
    ("Privacy", "/privacy-policy"),
]


# --- Legal pages =============================================================
# The docs.prettymodels.ai subdomain is retired; its legal notice (German
# Impressum, § 5 TMG) and privacy policy now live here as native pages that
# inherit the paper design system.
LEGAL_BACK = "← Back to the research"

# --- Legal notice / Impressum ------------------------------------------------
IMPRINT_PAGE_TITLE = "Legal Notice — PrettyModels AI"
IMPRINT_EYEBROW = "PrettyModels AI · Legal"
IMPRINT_TITLE = "Legal Notice"
IMPRINT_INTRO = (
    "Information pursuant to § 5 TMG (German Telemedia Act) and § 18(2) MStV."
)
IMPRINT_SECTIONS = [
    ("Operator", [
        "Christian Tausch — PrettyModels AI<br>"
        "Ben-Chorin-Str. 1<br>80339 Munich<br>Germany",
        "Contact: <a href='mailto:team@prettymodels.ai'>team@prettymodels.ai</a>",
    ]),
    ("Responsible for content", [
        "Responsible for editorial content pursuant to § 18(2) MStV: "
        "Christian Tausch (address as above).",
    ]),
    ("Liability for content", [
        "As a service provider we are responsible for our own content on these "
        "pages under general law, in accordance with § 7(1) TMG. Under §§ 8 to 10 "
        "TMG, however, we are not obliged to monitor transmitted or stored "
        "third-party information, or to investigate circumstances that indicate "
        "unlawful activity.",
        "Obligations to remove or block the use of information under general law "
        "remain unaffected. Any liability in this respect is only possible from "
        "the point in time at which we become aware of a specific infringement. "
        "Upon notification of such violations, we will remove the content "
        "concerned without delay.",
    ]),
    ("Liability for links", [
        "Our site contains links to external third-party websites over whose "
        "content we have no influence. We therefore accept no liability for this "
        "external content. The respective provider or operator of the linked "
        "pages is always responsible for their content.",
        "The linked pages were checked for possible legal violations at the time "
        "of linking; no unlawful content was recognizable. A permanent monitoring "
        "of the content of the linked pages is not reasonable without concrete "
        "evidence of an infringement. Upon notification of violations, we will "
        "remove such links without delay.",
    ]),
    ("Copyright", [
        "The content and works created by the operator on these pages are subject "
        "to German copyright law. Reproduction, editing, distribution and any form "
        "of commercial exploitation beyond the scope of copyright law require the "
        "prior written consent of the operator. Downloads and copies of this site "
        "are permitted only for private, non-commercial use.",
        "Insofar as the content on this site was not created by the operator, the "
        "copyrights of third parties are respected. Should you nevertheless become "
        "aware of a copyright infringement, please let us know accordingly. Upon "
        "notification of violations, we will remove such content without delay.",
    ]),
    ("Availability & technical disclaimer", [
        "We assume no liability for the uninterrupted availability of this website "
        "or for its freedom from technical errors, malware or other harmful "
        "components. Use of the site is at your own risk.",
    ]),
    ("Applicable law & dispute resolution", [
        "German law applies. We are neither willing nor obliged to participate in "
        "dispute-resolution proceedings before a consumer arbitration board within "
        "the meaning of § 36 VSBG.",
    ]),
    ("Reporting violations", [
        "If you believe that content on this site infringes your rights, please "
        "contact us directly at "
        "<a href='mailto:team@prettymodels.ai'>team@prettymodels.ai</a> before "
        "instructing a lawyer. This allows us to resolve the matter quickly and "
        "without unnecessary cost; the costs of a legal warning issued without "
        "prior contact will not be recognized as justified.",
    ]),
]

# --- Privacy policy ----------------------------------------------------------
PRIVACY_PAGE_TITLE = "Privacy Policy — PrettyModels AI"
PRIVACY_EYEBROW = "PrettyModels AI · Legal"
PRIVACY_TITLE = "Privacy Policy"
PRIVACY_UPDATED = "29 January 2025"
PRIVACY_INTRO = (
    "Your privacy is important to us. This Privacy Policy explains how PrettyModels "
    "AI (“we”, “us” or “our”) collects, uses, discloses "
    "and safeguards your personal information when you interact with this site. By "
    "accessing or using our website, services or any contact form, you consent to "
    "the practices described below."
)
PRIVACY_SECTIONS = [
    ("1. Information we collect", [
        "<strong>Information you provide.</strong> When you contact us or use a "
        "form, we may collect personal information such as your full name, email "
        "address, company name, job title, phone number (if provided) and any "
        "additional information you choose to submit.",
        "<strong>Automatically collected information.</strong> We may automatically "
        "collect your IP address, browser type and version, device information, "
        "operating system, referral source, pages viewed and time spent on the "
        "site, and clickstream and user-behaviour analytics.",
        "<strong>Cookies and tracking technologies.</strong> We use cookies, pixels "
        "and similar technologies to improve the user experience, analyze trends "
        "and personalize content. You can manage cookie preferences through your "
        "browser settings.",
    ]),
    ("2. How we use your information", [
        "We use the information we collect to respond to inquiries and facilitate "
        "potential business relationships; to send newsletters and promotional "
        "material and personalize marketing content; to analyze website usage and "
        "monitor performance and security; and to comply with legal obligations "
        "and enforce our terms of service.",
    ]),
    ("3. How we share your information", [
        "We do not sell, rent or trade your personal information.",
        "We may share information with service providers and business partners — "
        "such as cloud storage providers, email-marketing platforms and analytics "
        "tools — that are required to maintain its confidentiality. We may also "
        "disclose information where required by law, to comply with legal "
        "obligations, or to protect safety and security.",
    ]),
    ("4. Your choices and rights", [
        "<strong>Marketing opt-out.</strong> You can unsubscribe at any time via "
        "the links in our emails or by contacting us directly.",
        "<strong>Access, correction and deletion.</strong> Depending on your "
        "jurisdiction, you may access, correct or request deletion of your "
        "personal data by contacting "
        "<a href='mailto:team@prettymodels.ai'>team@prettymodels.ai</a>.",
        "<strong>Managing cookies.</strong> You can modify cookie settings in your "
        "browser, though disabling certain cookies may affect site functionality.",
    ]),
    ("5. Data security and retention", [
        "We implement industry-standard security measures to protect your personal "
        "information from unauthorized access, disclosure or misuse. We retain "
        "personal data for as long as necessary to fulfil the purposes described "
        "here or as required by law.",
    ]),
    ("6. International data transfers", [
        "Your information may be transferred to, stored and processed in the United "
        "States or other countries where our service providers operate.",
    ]),
    ("7. Children’s privacy", [
        "Our services are not intended for individuals under 18 years of age, and "
        "we do not knowingly collect personal data from minors.",
    ]),
    ("8. Changes to this policy", [
        "We may update this Privacy Policy from time to time. Material changes will "
        "be reflected by an updated “Last updated” date and, where "
        "appropriate, additional notice.",
    ]),
    ("9. Contact us", [
        "PrettyModels AI<br>"
        "Email: <a href='mailto:team@prettymodels.ai'>team@prettymodels.ai</a>",
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
