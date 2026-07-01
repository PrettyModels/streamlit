"""
components.py — the "academic paper" design system: theme/CSS injection, a
registered Altair theme so charts read as research figures, and small reusable
render helpers used by lab.py.
"""
import altair as alt
import streamlit as st

# --- palette (kept in sync with .streamlit/config.toml) ----------------------
PAPER = "#FBFAF8"
PAPER2 = "#F3F1EC"
INK = "#1A1A1A"
MUTED = "#6B6B6B"
FAINT = "#9A9A9A"
HAIRLINE = "#E4E1DA"
ACCENT = "#3A34C0"
ACCENT_SOFT = "#EDEBFF"

SERIF = "'Newsreader', Georgia, 'Times New Roman', serif"
SANS = "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
MONO = "'IBM Plex Mono', ui-monospace, 'SF Mono', Menlo, monospace"

FONT_IMPORT = (
    "@import url('https://fonts.googleapis.com/css2?"
    "family=Inter:wght@400;500;600&"
    "family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;"
    "1,6..72,400;1,6..72,500&"
    "family=IBM+Plex+Mono:wght@400;500;600&display=swap');"
)


def _md(html: str) -> None:
    st.markdown(html, unsafe_allow_html=True)


def register_altair_theme() -> None:
    """Register + enable a paper-styled Altair theme for all charts."""

    @alt.theme.register("pm_paper", enable=True)
    def _pm_paper():
        axis = {
            "labelColor": MUTED, "titleColor": MUTED,
            "labelFont": "Inter", "titleFont": "Inter",
            "labelFontSize": 11, "titleFontSize": 12,
            "gridColor": "#ECEAE4", "domainColor": HAIRLINE, "tickColor": HAIRLINE,
        }
        return {
            "config": {
                "background": PAPER,
                "font": "Inter",
                "view": {"stroke": "transparent"},
                "axis": axis,
                "axisY": {**axis, "gridDash": [2, 4]},
                "axisX": {**axis, "grid": False},
                "legend": {"labelColor": INK, "titleColor": MUTED,
                           "labelFont": "Inter", "titleFont": "Inter",
                           "titleFontSize": 11, "labelFontSize": 11},
                "title": {"color": INK, "font": "Newsreader", "fontSize": 15,
                          "fontWeight": 500, "anchor": "start"},
                "range": {
                    "category": [ACCENT, "#B08968", "#8A87B8", MUTED, "#C4B9A6", FAINT],
                    "heatmap": ["#EDEBFF", "#CFCBF2", "#A9A3E0", "#7E77CE", "#5A52C4",
                                ACCENT],
                },
            }
        }


def inject_theme() -> None:
    """Inject fonts + the full stylesheet and register the Altair theme."""
    register_altair_theme()
    _md(f"""<style>
{FONT_IMPORT}
:root {{
  --paper:{PAPER}; --paper2:{PAPER2}; --ink:{INK}; --muted:{MUTED};
  --faint:{FAINT}; --hairline:{HAIRLINE}; --accent:{ACCENT}; --accent-soft:{ACCENT_SOFT};
  --serif:{SERIF}; --sans:{SANS}; --mono:{MONO};
}}

/* shrink Streamlit's own chrome so the masthead sits at the very top */
[data-testid="stHeader"] {{ background: transparent; height: 0; }}
[data-testid="stToolbar"] {{ right: 0.5rem; }}

.stApp {{ background: var(--paper); }}
.block-container {{ max-width: 1080px; padding-top: 0.5rem; padding-bottom: 5rem; }}

html, body, [class*="st-"], .stMarkdown, p, li {{
  font-family: var(--sans); color: var(--ink);
}}
h1, h2, h3, h4, h5 {{ font-family: var(--serif) !important; color: var(--ink);
  letter-spacing: -0.01em; }}
a {{ color: var(--accent); text-decoration: none; }}
a:hover {{ text-decoration: underline; }}

/* ---- masthead ---- */
.pm-masthead {{
  position: sticky; top: 0; z-index: 999; background: var(--paper);
  display: flex; align-items: center; gap: 0.9rem;
  padding: 0.7rem 0 0.7rem; margin-bottom: 1.2rem;
  border-bottom: 1px solid var(--hairline);
}}
.pm-mark {{
  width: 34px; height: 34px; border-radius: 50%; background: var(--ink);
  color: #fff; font-family: var(--serif); font-weight: 600; font-size: 15px;
  display: flex; align-items: center; justify-content: center; flex: 0 0 auto;
}}
.pm-wordmark {{ font-family: var(--serif); font-size: 1.1rem; font-weight: 600;
  line-height: 1; }}
.pm-word-tag {{ font-family: var(--mono); font-size: 0.6rem; letter-spacing: 0.14em;
  text-transform: uppercase; color: var(--muted); margin-top: 3px; }}
.pm-nav {{ margin-left: auto; display: flex; gap: 1.15rem; flex-wrap: wrap; }}
.pm-nav a {{ font-family: var(--mono); font-size: 0.72rem; letter-spacing: 0.06em;
  text-transform: uppercase; color: var(--muted); }}
.pm-nav a:hover {{ color: var(--accent); text-decoration: none; }}

/* ---- generic ---- */
.pm-anchor {{ display: block; position: relative; top: -84px; visibility: hidden; }}
.pm-eyebrow {{ font-family: var(--mono); font-size: 0.72rem; letter-spacing: 0.16em;
  text-transform: uppercase; color: var(--muted); margin: 0 0 0.6rem; }}
.pm-eyebrow::before {{ content: ""; display: inline-block; width: 18px; height: 2px;
  background: var(--accent); vertical-align: middle; margin-right: 8px; }}
.pm-hairline {{ height: 1px; background: var(--hairline); border: 0;
  margin: 3.2rem 0 1.6rem; }}

/* ---- hero ---- */
.pm-hero-h1 {{ font-family: var(--serif); font-weight: 500; font-size: 3rem;
  line-height: 1.08; letter-spacing: -0.02em; margin: 0.2rem 0 1.1rem; }}
.pm-lead {{ font-size: 1.16rem; line-height: 1.6; color: #2b2b2b; max-width: 40em; }}

/* ---- section header ---- */
.pm-sec-num {{ font-family: var(--mono); font-size: 0.72rem; letter-spacing: 0.16em;
  color: var(--accent); text-transform: uppercase; }}
.pm-sec-title {{ font-family: var(--serif); font-weight: 500; font-size: 2rem;
  line-height: 1.12; margin: 0.35rem 0 0.35rem; letter-spacing: -0.015em; }}
.pm-sec-sub {{ font-family: var(--sans); color: var(--muted); font-size: 1.02rem;
  margin-bottom: 0.4rem; }}

.pm-body p {{ font-size: 1.05rem; line-height: 1.68; margin: 0 0 1rem; max-width: 40em; }}
.pm-body em {{ font-style: italic; }}

.pm-quote {{ font-family: var(--serif); font-style: italic; font-size: 1.6rem;
  line-height: 1.34; color: var(--ink); border-left: 3px solid var(--accent);
  padding: 0.2rem 0 0.2rem 1.2rem; margin: 1.8rem 0; max-width: 30em; }}

.pm-figcap {{ font-family: var(--serif); font-style: italic; font-size: 0.9rem;
  color: var(--muted); margin: 0.4rem 0 1.4rem; }}

/* ---- stat strip ---- */
.pm-stats {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 1px;
  background: var(--hairline); border: 1px solid var(--hairline); margin: 2rem 0 0.5rem; }}
.pm-stat {{ background: var(--paper); padding: 1.1rem 1.1rem; }}
.pm-stat-v {{ font-family: var(--mono); font-size: 1.7rem; font-weight: 500;
  color: var(--ink); line-height: 1; }}
.pm-stat-l {{ font-family: var(--sans); font-size: 0.82rem; color: var(--muted);
  margin-top: 0.4rem; }}

/* ---- method step cards ---- */
.pm-steps {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 1px;
  background: var(--hairline); border: 1px solid var(--hairline); margin: 1.6rem 0; }}
.pm-step {{ background: var(--paper); padding: 1.2rem 1rem 1.3rem; }}
.pm-step-n {{ font-family: var(--mono); font-size: 0.72rem; color: var(--accent);
  letter-spacing: 0.1em; }}
.pm-step-t {{ font-family: var(--serif); font-size: 1.18rem; font-weight: 600;
  margin: 0.5rem 0 0.1rem; }}
.pm-step-s {{ font-family: var(--mono); font-size: 0.66rem; letter-spacing: 0.08em;
  text-transform: uppercase; color: var(--faint); margin-bottom: 0.55rem; }}
.pm-step-d {{ font-size: 0.9rem; line-height: 1.5; color: #333; }}

/* ---- glossary ---- */
.pm-gloss {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 1px;
  background: var(--hairline); border: 1px solid var(--hairline); margin: 1.4rem 0; }}
.pm-gloss-i {{ background: var(--paper); padding: 1.1rem 1rem 1.2rem; }}
.pm-gloss-t {{ font-family: var(--serif); font-size: 1.1rem; font-weight: 600;
  color: var(--accent); margin-bottom: 0.4rem; }}
.pm-gloss-d {{ font-size: 0.86rem; line-height: 1.5; color: #333; }}

/* ---- footer ---- */
.pm-entity {{ font-size: 0.92rem; line-height: 1.6; color: var(--muted);
  background: var(--paper2); border: 1px solid var(--hairline); border-radius: 4px;
  padding: 0.9rem 1.1rem; margin: 0.5rem 0 1.5rem; }}

@media (max-width: 820px) {{
  .pm-stats, .pm-steps, .pm-gloss {{ grid-template-columns: repeat(2, 1fr); }}
  .pm-hero-h1 {{ font-size: 2.2rem; }}
  .pm-nav {{ display: none; }}
}}
</style>""")


# --- render helpers ----------------------------------------------------------
def masthead(brand: str, tagline: str, nav: list[tuple[str, str]]) -> None:
    links = "".join(f'<a href="#{anchor}">{label}</a>' for label, anchor in nav)
    _md(f"""<div class="pm-masthead">
  <div class="pm-mark">PM</div>
  <div><div class="pm-wordmark">{brand}</div>
       <div class="pm-word-tag">{tagline}</div></div>
  <nav class="pm-nav">{links}</nav>
</div>""")


def anchor(anchor_id: str) -> None:
    _md(f'<span class="pm-anchor" id="{anchor_id}"></span>')


def eyebrow(text: str) -> None:
    _md(f'<div class="pm-eyebrow">{text}</div>')


def section_header(anchor_id: str, num: str, title: str, subtitle: str = "") -> None:
    anchor(anchor_id)
    sub = f'<div class="pm-sec-sub">{subtitle}</div>' if subtitle else ""
    _md(f'<div class="pm-sec-num">§{num}</div>'
        f'<div class="pm-sec-title">{title}</div>{sub}')


def lead(text: str) -> None:
    _md(f'<p class="pm-lead">{text}</p>')


def body(paragraphs: list[str]) -> None:
    inner = "".join(f"<p>{_emphasis(p)}</p>" for p in paragraphs)
    _md(f'<div class="pm-body">{inner}</div>')


def _emphasis(text: str) -> str:
    # tiny markdown-ish *italic* support inside HTML paragraphs
    while "*" in text:
        text = text.replace("*", "<em>", 1).replace("*", "</em>", 1)
    return text


def pull_quote(text: str) -> None:
    _md(f'<blockquote class="pm-quote">{text}</blockquote>')


def figure_caption(text: str) -> None:
    _md(f'<div class="pm-figcap">{text}</div>')


def hairline() -> None:
    _md('<hr class="pm-hairline">')


def stat_strip(items: list[tuple[str, str]]) -> None:
    cells = "".join(
        f'<div class="pm-stat"><div class="pm-stat-v">{v}</div>'
        f'<div class="pm-stat-l">{l}</div></div>'
        for v, l in items
    )
    _md(f'<div class="pm-stats">{cells}</div>')


def step_grid(steps: list[tuple[str, str, str, str]]) -> None:
    cells = "".join(
        f'<div class="pm-step"><div class="pm-step-n">{n}</div>'
        f'<div class="pm-step-t">{t}</div><div class="pm-step-s">{s}</div>'
        f'<div class="pm-step-d">{d}</div></div>'
        for n, t, s, d in steps
    )
    _md(f'<div class="pm-steps">{cells}</div>')


def glossary_grid(items: list[tuple[str, str]]) -> None:
    cells = "".join(
        f'<div class="pm-gloss-i"><div class="pm-gloss-t">{t}</div>'
        f'<div class="pm-gloss-d">{d}</div></div>'
        for t, d in items
    )
    _md(f'<div class="pm-gloss">{cells}</div>')


def entity_note(text: str) -> None:
    _md(f'<div class="pm-entity">{text}</div>')
