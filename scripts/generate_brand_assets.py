"""Generate checked-in browser and social-sharing assets from the PM mark.

Run this script after changing ``images/logo.png``, the public positioning, or
the monthly score data — the social preview draws its figure from
``data/full_weights - raw.csv``, so a new scoring run changes the card.
Pillow is only a development dependency; generated files are served as-is.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
STATIC = ROOT / "static"
SCORES_CSV = ROOT / "data" / "full_weights - raw.csv"
HERO_SOURCE = ROOT / "images" / "marylin6.png"

PAPER = "#FBFAF8"
INK = "#1A1A1A"
MUTED = "#6B6B6B"
ACCENT = "#3A34C0"

# Reversed-out counterparts for the ink field the social card is drawn on.
DARK_MUTED = "#A3A19B"
DARK_RULE = "#3C3C3C"
DARK_GRID = "#2E2E36"
DARK_BAND = "#3B3B6E"
ACCENT_LIGHT = "#A5A0F2"


SERIF_CANDIDATES = [
    "/System/Library/Fonts/NewYork.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
]
SANS_CANDIDATES = [
    "/System/Library/Fonts/SFNS.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]
# A real bold face first, so the Linux fallback still renders bold; on macOS the
# variable SFNS is picked up and the named instance below does the work.
SANS_BOLD_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/System/Library/Fonts/SFNS.ttf",
]


def _font(candidates: list[str], size: int, weight: str = "Regular") -> ImageFont.FreeTypeFont:
    """Load the first available face, applying a variable-font weight if supported.

    macOS ships SFNS and New York as variable fonts, where the named instance is
    the only thing that actually produces a bold face — pointing at the same
    ``.ttf`` twice, as an earlier revision did, silently rendered everything at
    regular weight.
    """
    for candidate in candidates:
        path = Path(candidate)
        if not path.exists():
            continue
        font = ImageFont.truetype(str(path), size=size)
        if weight != "Regular":
            try:
                font.set_variation_by_name(weight)
            except OSError:
                pass  # static face: the file itself already carries the weight
        return font
    raise FileNotFoundError(f"No suitable font found in: {candidates}")


def _tracked(
    draw: ImageDraw.ImageDraw,
    xy: tuple[float, float],
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: str,
    tracking: float = 0.0,
    anchor_right: bool = False,
) -> float:
    """Draw letter-spaced text and return its width.

    Pillow is built without raqm here, so tracking has to be applied by hand;
    without it the small-caps labels lose the 0.16em rhythm the site uses.
    """
    extra = tracking * font.size
    widths = [draw.textlength(char, font=font) for char in text]
    total = sum(widths) + extra * max(len(text) - 1, 0)
    x, y = xy
    if anchor_right:
        x -= total
    for char, width in zip(text, widths):
        draw.text((x, y), char, font=font, fill=fill)
        x += width + extra
    return total


def _fit_logo(source: Image.Image, size: int, padding: int = 0) -> Image.Image:
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    mark = source.resize((size - 2 * padding, size - 2 * padding), Image.Resampling.LANCZOS)
    canvas.alpha_composite(mark, (padding, padding))
    return canvas


def _on_paper(source: Image.Image) -> Image.Image:
    """Flatten onto the paper tone.

    Icons that are shown on an opaque tile must not be flattened onto Pillow's
    default black: converting the transparent canvas straight to RGB turned the
    apple-touch icon into a black square and erased the disc entirely.
    """
    backdrop = Image.new("RGB", source.size, PAPER)
    backdrop.paste(source, (0, 0), source)
    return backdrop


def _reversed_mark(source: Image.Image) -> Image.Image:
    """Swap the mark's black disc and white letters for use on the ink field."""
    rgba = source.convert("RGBA")
    alpha = rgba.getchannel("A")
    letters = rgba.convert("L").point(lambda v: 255 if v > 128 else 0).convert("L")
    letters = Image.composite(letters, Image.new("L", rgba.size, 0), alpha)
    out = Image.new("RGBA", rgba.size, (0, 0, 0, 0))
    out.paste(Image.new("RGBA", rgba.size, PAPER), (0, 0), alpha)
    out.paste(Image.new("RGBA", rgba.size, INK), (0, 0), letters)
    out.putalpha(alpha)
    return out


def generate_icons(logo: Image.Image) -> None:
    # Browser favicons keep their transparency; tab backgrounds vary.
    for size in (16, 32):
        _fit_logo(logo, size).save(STATIC / f"favicon-{size}x{size}.png", optimize=True)

    # Home-screen and launcher icons are composited onto an opaque tile.
    _on_paper(_fit_logo(logo, 180, padding=10)).save(
        STATIC / "apple-touch-icon.png", optimize=True
    )
    _on_paper(_fit_logo(logo, 192, padding=8)).save(STATIC / "icon-192.png", optimize=True)
    _on_paper(_fit_logo(logo, 512, padding=20)).save(STATIC / "icon-512.png", optimize=True)

    logo.save(
        STATIC / "favicon.ico",
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48)],
    )


def generate_research_hero() -> None:
    """Export the above-the-fold illustration with dimensions and browser compression.

    The original remains the editable source. The page uses this checked-in WebP
    directly through Nginx, avoiding Streamlit's media proxy and reserving the
    final aspect ratio before it downloads.
    """
    hero = Image.open(HERO_SOURCE).convert("RGBA")
    hero = hero.resize((750, 663), Image.Resampling.LANCZOS)
    hero.save(
        STATIC / "research-hero.webp",
        format="WEBP",
        quality=84,
        method=6,
        exact=True,
    )


def load_figure_data() -> tuple[pd.DataFrame, int, int]:
    """Composite-factor ranks per company, plus the universe counts on the card.

    The ``Cat-*`` columns are already percentile ranks across the universe, so
    the figure plots stored values directly — nothing is rescaled for display.
    """
    raw = pd.read_csv(SCORES_CSV)
    factors = [c for c in raw.columns if c.startswith("Cat-") and "Cat-XXX" not in c]
    dimensions = [
        c for c in raw.columns if c.endswith("Score100") or c.endswith("Probability100")
    ]
    if not factors or not dimensions:
        raise ValueError(f"{SCORES_CSV.name} has no recognisable factor/dimension columns")
    return raw[factors].astype(float), len(raw), len(dimensions)


def _draw_factor_spread(
    canvas: Image.Image, box: tuple[int, int, int, int], ranks: pd.DataFrame
) -> None:
    """One column per company: the range its factor ranks cover, and their mean.

    Ordering by the mean is a display convention only. It lets the card show the
    real finding at a glance — the ordering is coherent, yet most companies span
    a wide band, because the factors disagree about the same business.
    """
    x0, y0, x1, y1 = box
    mean = ranks.mean(axis=1)
    order = mean.sort_values().index
    low = ranks.min(axis=1).loc[order].to_numpy()
    high = ranks.max(axis=1).loc[order].to_numpy()
    centre = mean.loc[order].to_numpy()

    draw = ImageDraw.Draw(canvas)
    height = y1 - y0
    step = (x1 - x0) / len(order)

    for fraction in (0.25, 0.5, 0.75, 1.0):
        gridline = y1 - fraction * height
        draw.line((x0, gridline, x1, gridline), fill=DARK_GRID, width=1)

    for index in range(len(order)):
        centre_x = x0 + index * step + step / 2
        draw.rectangle(
            (centre_x - 3, y1 - high[index] * height, centre_x + 3, y1 - low[index] * height),
            fill=DARK_BAND,
        )
    for index in range(len(order)):
        centre_x = x0 + index * step + step / 2
        centre_y = y1 - centre[index] * height
        draw.rectangle(
            (centre_x - 4, centre_y - 2, centre_x + 4, centre_y + 2), fill=ACCENT_LIGHT
        )

    draw.line((x0, y1, x1, y1), fill=DARK_RULE, width=2)


def generate_social_preview(logo: Image.Image) -> None:
    """An ink-field research cover: the lab's claim, and the figure behind it.

    The card is drawn dark because every feed it lands in is light grey — a
    paper-white card dissolves into the timeline around it.
    """
    ranks, n_assets, n_dimensions = load_figure_data()

    canvas = Image.new("RGB", (1200, 630), INK)
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((0, 0, 1200, 7), fill=ACCENT)

    mark = _fit_logo(_reversed_mark(logo), 34)
    canvas.paste(mark, (72, 56), mark)

    label_font = _font(SANS_BOLD_CANDIDATES, 15, "Bold")
    _tracked(draw, (120, 65), "PRETTYMODELS AI", label_font, PAPER, 0.14)
    _tracked(draw, (1128, 65), "AI RESEARCH LAB", label_font, DARK_MUTED, 0.14, anchor_right=True)
    draw.line((72, 112, 1128, 112), fill=DARK_RULE, width=2)

    headline_font = _font(SERIF_CANDIDATES, 50)
    draw.text((72, 152), "Each score is a hypothesis.", font=headline_font, fill=PAPER)
    draw.text((72, 212), "The market runs the experiment.", font=headline_font, fill=PAPER)

    subhead_font = _font(SANS_CANDIDATES, 20)
    draw.text(
        (73, 292),
        f"{n_assets} companies scored on {n_dimensions} dimensions by frontier LLMs, "
        "every month.",
        font=subhead_font,
        fill=DARK_MUTED,
    )

    _draw_factor_spread(canvas, (72, 378, 1128, 540), ranks)

    caption_font = _font(SANS_BOLD_CANDIDATES, 14, "Semibold")
    _tracked(
        draw,
        (72, 566),
        f"FIG. 1  ·  RANGE AND MEAN OF {ranks.shape[1]} COMPOSITE FACTOR RANKS, PER COMPANY",
        caption_font,
        DARK_MUTED,
        0.10,
    )
    _tracked(draw, (1128, 566), "PRETTYMODELS.AI", caption_font, ACCENT_LIGHT, 0.12,
             anchor_right=True)

    # Social platforms cache og:image by URL indefinitely, so the tags point at
    # the versioned name. The unversioned file is kept in step for any link
    # already sitting in a crawler cache.
    canvas.save(STATIC / "social-preview-v2.png", optimize=True)
    canvas.save(STATIC / "social-preview.png", optimize=True)


def main() -> None:
    STATIC.mkdir(exist_ok=True)
    logo = Image.open(ROOT / "images" / "logo.png").convert("RGBA")
    generate_icons(logo)
    generate_research_hero()
    generate_social_preview(logo)


if __name__ == "__main__":
    main()
