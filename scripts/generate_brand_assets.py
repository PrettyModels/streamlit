"""Generate checked-in browser and social-sharing assets from the PM mark.

Run this script after changing ``images/logo.png`` or the public positioning.
Pillow is only a development dependency; generated files are served as-is.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
STATIC = ROOT / "static"
PAPER = "#FBFAF8"
INK = "#1A1A1A"
MUTED = "#6B6B6B"
HAIRLINE = "#E4E1DA"
ACCENT = "#3A34C0"


def _font(candidates: list[str], size: int) -> ImageFont.FreeTypeFont:
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    raise FileNotFoundError(f"No suitable font found in: {candidates}")


SERIF_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Georgia.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
]
SERIF_BOLD_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
]
SANS_CANDIDATES = [
    "/System/Library/Fonts/SFNS.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]
SANS_BOLD_CANDIDATES = [
    "/System/Library/Fonts/SFNS.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def _fit_logo(source: Image.Image, size: int, padding: int = 0) -> Image.Image:
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    mark = source.resize((size - 2 * padding, size - 2 * padding), Image.Resampling.LANCZOS)
    canvas.alpha_composite(mark, (padding, padding))
    return canvas


def generate_icons(logo: Image.Image) -> None:
    for size in (16, 32):
        _fit_logo(logo, size).save(STATIC / f"favicon-{size}x{size}.png", optimize=True)

    _fit_logo(logo, 180, padding=10).convert("RGB").save(
        STATIC / "apple-touch-icon.png", optimize=True
    )
    _fit_logo(logo, 192, padding=8).save(STATIC / "icon-192.png", optimize=True)
    _fit_logo(logo, 512, padding=20).save(STATIC / "icon-512.png", optimize=True)

    logo.save(
        STATIC / "favicon.ico",
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48)],
    )


def generate_social_preview(logo: Image.Image) -> None:
    canvas = Image.new("RGB", (1200, 630), PAPER)
    draw = ImageDraw.Draw(canvas)

    # An institutional research cover: one question, one mark, no ornamental
    # dashboards or invented data visualisations.
    draw.rectangle((0, 0, 1200, 8), fill=ACCENT)

    brand_font = _font(SERIF_BOLD_CANDIDATES, 30)
    label_font = _font(SANS_BOLD_CANDIDATES, 14)
    headline_font = _font(SERIF_CANDIDATES, 59)
    subhead_font = _font(SANS_CANDIDATES, 20)
    footer_font = _font(SANS_CANDIDATES, 16)

    draw.text((68, 51), "PrettyModels AI", font=brand_font, fill=INK)
    draw.text((69, 94), "AI RESEARCH LAB", font=label_font, fill=MUTED)
    brief = "RESEARCH BRIEF · UPDATED MONTHLY"
    brief_box = draw.textbbox((0, 0), brief, font=label_font)
    draw.text((1132 - (brief_box[2] - brief_box[0]), 69), brief, font=label_font, fill=ACCENT)
    draw.line((68, 132, 1132, 132), fill=HAIRLINE, width=2)

    draw.text((68, 182), "Can AI evaluate", font=headline_font, fill=INK)
    draw.text((68, 250), "public companies", font=headline_font, fill=INK)
    draw.text((68, 318), "consistently?", font=headline_font, fill=INK)
    draw.text(
        (71, 415),
        "A public, out-of-sample test of model judgment.",
        font=subhead_font,
        fill=MUTED,
    )

    draw.line((806, 176, 806, 462), fill=HAIRLINE, width=2)
    mark = _fit_logo(logo, 228)
    canvas.paste(mark, (884, 202), mark)

    draw.line((68, 536, 1132, 536), fill=HAIRLINE, width=2)
    draw.text((68, 570), "PRETTYMODELS.AI", font=label_font, fill=INK)
    footer = "PUBLIC MODEL RESEARCH"
    footer_box = draw.textbbox((0, 0), footer, font=footer_font)
    draw.text((1132 - (footer_box[2] - footer_box[0]), 568), footer, font=footer_font, fill=MUTED)

    canvas.save(STATIC / "social-preview.png", optimize=True)


def main() -> None:
    STATIC.mkdir(exist_ok=True)
    logo = Image.open(ROOT / "images" / "logo.png").convert("RGBA")
    generate_icons(logo)
    generate_social_preview(logo)


if __name__ == "__main__":
    main()
