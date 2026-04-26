"""
SPINE Framework — Shared Visual Design System
Professional polish layer for all PDF documents.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import Flowable, Paragraph, Spacer, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ─────────────────────────────────────────────
# PAGE DIMENSIONS
# ─────────────────────────────────────────────
PAGE_W, PAGE_H = letter
MARGIN = 0.75 * inch
CONTENT_W = PAGE_W - 2 * MARGIN

# ─────────────────────────────────────────────
# COLORS — Full Design System
# ─────────────────────────────────────────────
C = {
    # Core brand
    "primary": HexColor("#8B6F7E"),        # mauve
    "secondary": HexColor("#4A7C6F"),      # sage
    "accent": HexColor("#C4956A"),         # terracotta
    "text": HexColor("#2C2C2C"),
    "subtext": HexColor("#6B6B6B"),
    "white": HexColor("#FFFFFF"),

    # Page backgrounds
    "page_bg": HexColor("#F9F5F2"),        # warm cream base
    "section_bg": HexColor("#F2EAE2"),     # slightly deeper cream for section headers
    "divider": HexColor("#E0D5CE"),
    "field_bg": HexColor("#E8DDD5"),       # response field shading

    # Domain colors
    "sovereignty": HexColor("#4A7C6F"),    # sage
    "power": HexColor("#8B6F7E"),          # mauve
    "identity": HexColor("#C4956A"),       # amber
    "nourishment": HexColor("#7B9BC4"),    # soft blue
    "embodiment": HexColor("#9B7BBF"),     # violet

    # Category colors
    "healing": HexColor("#7B9BC4"),
    "pattern": HexColor("#C4B47A"),
    "resourcing": HexColor("#7BBF8E"),
    "anchor": HexColor("#3D5A80"),
    "exploring": HexColor("#4A7C6F"),

    # Utility
    "light_blue_bg": HexColor("#EEF3FA"),
    "cover_dark": HexColor("#3A2A32"),     # deep terracotta-brown for covers
    "coach_cover": HexColor("#2D4A3F"),    # deep sage for coach's guide
}

DOMAIN_COLORS = {
    "Sovereignty": C["sovereignty"],
    "Power": C["power"],
    "Identity": C["identity"],
    "Nourishment": C["nourishment"],
    "Embodiment": C["embodiment"],
}

# ─────────────────────────────────────────────
# FONT REGISTRATION
# ─────────────────────────────────────────────
FONT_DIR = os.path.join(os.path.dirname(__file__), "assets", "fonts")


def register_fonts():
    """Register all custom fonts, return font name map."""
    fonts = {"heading": "Helvetica", "heading_bold": "Helvetica-Bold",
             "heading_italic": "Helvetica-Oblique",
             "body": "Helvetica", "body_bold": "Helvetica-Bold",
             "body_italic": "Helvetica-Oblique", "body_bold_italic": "Helvetica-BoldOblique",
             "mono": "Courier"}

    font_map = {
        "EBGaramond": ("EBGaramond-Regular.ttf", "heading"),
        "EBGaramond-Bold": ("EBGaramond-Bold.ttf", "heading_bold"),
        "EBGaramond-Italic": ("EBGaramond-Italic.ttf", "heading_italic"),
        "Lato": ("Lato-Regular.ttf", "body"),
        "Lato-Bold": ("Lato-Bold.ttf", "body_bold"),
        "Lato-Italic": ("Lato-Italic.ttf", "body_italic"),
        "Lato-BoldItalic": ("Lato-BoldItalic.ttf", "body_bold_italic"),
        "RobotoMono": ("RobotoMono-Regular.ttf", "mono"),
    }

    for font_name, (filename, key) in font_map.items():
        path = os.path.join(FONT_DIR, filename)
        if os.path.exists(path):
            try:
                pdfmetrics.registerFont(TTFont(font_name, path))
                fonts[key] = font_name
            except Exception:
                pass

    return fonts


FONTS = register_fonts()


# ─────────────────────────────────────────────
# PARAGRAPH STYLES — Full Typography Hierarchy
# ─────────────────────────────────────────────
def make_styles():
    """Create the complete style dictionary."""
    return {
        # Document title — H1
        "doc_title": ParagraphStyle(
            "DocTitle", fontName=FONTS["heading"], fontSize=36, leading=42,
            textColor=C["text"], alignment=TA_LEFT, spaceAfter=8,
        ),
        "doc_title_white": ParagraphStyle(
            "DocTitleWhite", fontName=FONTS["heading"], fontSize=36, leading=42,
            textColor=C["white"], alignment=TA_LEFT, spaceAfter=8,
        ),
        "doc_title_cream": ParagraphStyle(
            "DocTitleCream", fontName=FONTS["heading"], fontSize=36, leading=42,
            textColor=C["page_bg"], alignment=TA_LEFT, spaceAfter=8,
        ),
        # Section name — H2
        "h2": ParagraphStyle(
            "H2", fontName=FONTS["heading"], fontSize=22, leading=28,
            textColor=C["primary"], alignment=TA_LEFT, spaceAfter=12, spaceBefore=6,
        ),
        # Subsection — H3
        "h3": ParagraphStyle(
            "H3", fontName=FONTS["heading_italic"], fontSize=16, leading=22,
            textColor=C["text"], alignment=TA_LEFT, spaceAfter=8, spaceBefore=4,
        ),
        # Body text
        "body": ParagraphStyle(
            "Body", fontName=FONTS["body"], fontSize=11, leading=18.7,
            textColor=C["text"], alignment=TA_LEFT, spaceAfter=6,
        ),
        "body_small": ParagraphStyle(
            "BodySmall", fontName=FONTS["body"], fontSize=9, leading=14,
            textColor=C["text"], alignment=TA_LEFT, spaceAfter=4,
        ),
        # Callout/quote text
        "callout": ParagraphStyle(
            "Callout", fontName=FONTS["heading_italic"], fontSize=14, leading=22,
            textColor=C["primary"], alignment=TA_LEFT, spaceAfter=8,
        ),
        "callout_small": ParagraphStyle(
            "CalloutSmall", fontName=FONTS["heading_italic"], fontSize=12, leading=18,
            textColor=C["primary"], alignment=TA_LEFT, spaceAfter=6,
        ),
        # Data/scores
        "data": ParagraphStyle(
            "Data", fontName=FONTS["mono"], fontSize=10, leading=14,
            textColor=C["text"], alignment=TA_RIGHT,
        ),
        # Caption
        "caption": ParagraphStyle(
            "Caption", fontName=FONTS["body_italic"], fontSize=9, leading=13,
            textColor=C["subtext"], alignment=TA_LEFT,
        ),
        # Cover subtitle
        "cover_sub": ParagraphStyle(
            "CoverSub", fontName=FONTS["body"], fontSize=14, leading=20,
            textColor=C["page_bg"], alignment=TA_LEFT, spaceAfter=4,
        ),
        "cover_sub_dark": ParagraphStyle(
            "CoverSubDark", fontName=FONTS["body"], fontSize=14, leading=20,
            textColor=C["subtext"], alignment=TA_LEFT, spaceAfter=4,
        ),
        # Center aligned
        "center": ParagraphStyle(
            "Center", fontName=FONTS["body"], fontSize=11, leading=18.7,
            textColor=C["text"], alignment=TA_CENTER, spaceAfter=6,
        ),
        "center_small": ParagraphStyle(
            "CenterSmall", fontName=FONTS["body"], fontSize=9, leading=14,
            textColor=C["subtext"], alignment=TA_CENTER,
        ),
        # Kimberly's voice — warm, poetic body text
        "voice": ParagraphStyle(
            "Voice", fontName=FONTS["heading"], fontSize=12, leading=20.4,
            textColor=C["text"], alignment=TA_LEFT, spaceAfter=10,
        ),
        "voice_italic": ParagraphStyle(
            "VoiceItalic", fontName=FONTS["heading_italic"], fontSize=12, leading=20.4,
            textColor=C["text"], alignment=TA_LEFT, spaceAfter=10,
        ),
        # Practice title
        "practice_title": ParagraphStyle(
            "PracticeTitle", fontName=FONTS["heading_bold"] if FONTS["heading_bold"] != "Helvetica-Bold" else FONTS["heading"],
            fontSize=16, leading=22,
            textColor=C["text"], alignment=TA_LEFT, spaceAfter=4,
        ),
        # Facilitator notes
        "facilitator": ParagraphStyle(
            "Facilitator", fontName=FONTS["body_italic"], fontSize=10, leading=16,
            textColor=C["subtext"], alignment=TA_LEFT, spaceAfter=4,
        ),
        # Retreat time blocks
        "time_block": ParagraphStyle(
            "TimeBlock", fontName=FONTS["heading"], fontSize=14, leading=20,
            textColor=C["accent"], alignment=TA_LEFT, spaceAfter=4,
        ),
        "time_detail": ParagraphStyle(
            "TimeDetail", fontName=FONTS["body"], fontSize=10, leading=16,
            textColor=C["text"], alignment=TA_LEFT, spaceAfter=4,
        ),
    }


STYLES = make_styles()


# ─────────────────────────────────────────────
# CUSTOM FLOWABLES — Decorative Elements
# ─────────────────────────────────────────────

class WarmPageBackground(Flowable):
    """Draw warm cream background on the full page."""
    def __init__(self, color=None):
        super().__init__()
        self.bg_color = color or C["page_bg"]

    def wrap(self, availWidth, availHeight):
        return 0, 0

    def draw(self):
        self.canv.saveState()
        self.canv.setFillColor(self.bg_color)
        self.canv.rect(0, -PAGE_H, PAGE_W, PAGE_H, fill=1, stroke=0)
        self.canv.restoreState()


class CoverBackground(Flowable):
    """Full-bleed cover background with gradient effect."""
    def __init__(self, top_color=None, bottom_color=None):
        super().__init__()
        self.top_color = top_color or C["cover_dark"]
        self.bottom_color = bottom_color or C["page_bg"]

    def wrap(self, availWidth, availHeight):
        return 0, 0

    def draw(self):
        self.canv.saveState()
        steps = 60
        for i in range(steps):
            t = i / steps
            r = self.top_color.red * (1 - t) + self.bottom_color.red * t
            g = self.top_color.green * (1 - t) + self.bottom_color.green * t
            b = self.top_color.blue * (1 - t) + self.bottom_color.blue * t
            color = Color(r, g, b)
            y = PAGE_H - (i + 1) * (PAGE_H / steps)
            h = PAGE_H / steps + 1
            self.canv.setFillColor(color)
            self.canv.rect(-MARGIN, y - PAGE_H + MARGIN, PAGE_W, h, fill=1, stroke=0)
        self.canv.restoreState()


class DividerLine(Flowable):
    """Thin terracotta line with diamond ornament at center."""
    def __init__(self, width=None, color=None):
        super().__init__()
        self.line_width = width or CONTENT_W
        self.line_color = color or C["accent"]

    def wrap(self, availWidth, availHeight):
        return self.line_width, 12

    def draw(self):
        self.canv.saveState()
        mid = self.line_width / 2
        y = 6
        # Left line
        self.canv.setStrokeColor(self.line_color)
        self.canv.setLineWidth(0.5)
        self.canv.line(0, y, mid - 8, y)
        # Diamond
        self.canv.setFillColor(self.line_color)
        path = self.canv.beginPath()
        path.moveTo(mid, y + 4)
        path.lineTo(mid + 4, y)
        path.lineTo(mid, y - 4)
        path.lineTo(mid - 4, y)
        path.close()
        self.canv.drawPath(path, fill=1, stroke=0)
        # Right line
        self.canv.line(mid + 8, y, self.line_width, y)
        self.canv.restoreState()


class SectionDivider(Flowable):
    """Simple thin line divider."""
    def __init__(self, width=None, color=None):
        super().__init__()
        self.line_width = width or CONTENT_W
        self.line_color = color or C["divider"]

    def wrap(self, availWidth, availHeight):
        return self.line_width, 4

    def draw(self):
        self.canv.saveState()
        self.canv.setStrokeColor(self.line_color)
        self.canv.setLineWidth(0.5)
        self.canv.line(0, 2, self.line_width, 2)
        self.canv.restoreState()


class ColorStripe(Flowable):
    """Full-width colored bar."""
    def __init__(self, color, height=8, width=None):
        super().__init__()
        self.color = color
        self.bar_height = height
        self.bar_width = width or CONTENT_W

    def wrap(self, availWidth, availHeight):
        return self.bar_width, self.bar_height

    def draw(self):
        self.canv.setFillColor(self.color)
        self.canv.rect(0, 0, self.bar_width, self.bar_height, fill=1, stroke=0)


class LeftBorderBox(Flowable):
    """Callout box with rounded rect, left border, and soft shadow."""
    def __init__(self, text, border_color=None, bg_color=None, width=None,
                 style=None, padding=14):
        super().__init__()
        self.text = text
        self.border_color = border_color or C["primary"]
        self.bg_color = bg_color or C["page_bg"]
        self.box_width = width or CONTENT_W
        self.text_style = style or STYLES["callout_small"]
        self.padding = padding

    def wrap(self, availWidth, availHeight):
        self.box_width = min(self.box_width, availWidth)
        inner_w = self.box_width - self.padding * 2 - 6
        self._para = Paragraph(self.text, self.text_style)
        w, h = self._para.wrap(inner_w, availHeight)
        self._text_height = h
        return self.box_width, h + self.padding * 2

    def draw(self):
        total_h = self._text_height + self.padding * 2
        # Soft shadow
        self.canv.saveState()
        self.canv.setFillColor(Color(0, 0, 0, alpha=0.05))
        self.canv.roundRect(2, -2, self.box_width, total_h, 4, fill=1, stroke=0)
        # Background
        self.canv.setFillColor(self.bg_color)
        self.canv.roundRect(0, 0, self.box_width, total_h, 4, fill=1, stroke=0)
        # Left border
        self.canv.setFillColor(self.border_color)
        self.canv.rect(0, 0, 4, total_h, fill=1, stroke=0)
        self.canv.restoreState()
        # Text
        self._para.drawOn(self.canv, self.padding + 6, self.padding)


class ResponseField(Flowable):
    """Subtle shaded area for written responses."""
    def __init__(self, height=60, width=None, label=None):
        super().__init__()
        self.field_height = height
        self.field_width = width or CONTENT_W
        self.label = label

    def wrap(self, availWidth, availHeight):
        self.field_width = min(self.field_width, availWidth)
        extra = 16 if self.label else 0
        return self.field_width, self.field_height + extra

    def draw(self):
        y_offset = 0
        if self.label:
            self.canv.saveState()
            self.canv.setFillColor(C["subtext"])
            self.canv.setFont(FONTS["body_italic"], 8)
            self.canv.drawString(4, self.field_height + 4, self.label)
            self.canv.restoreState()
        self.canv.saveState()
        self.canv.setFillColor(C["field_bg"])
        self.canv.roundRect(0, 0, self.field_width, self.field_height, 4, fill=1, stroke=0)
        self.canv.restoreState()


class DomainHeader(Flowable):
    """Full-width domain header bar with domain name and color."""
    def __init__(self, domain_name, subtitle=None, width=None):
        super().__init__()
        self.domain_name = domain_name
        self.subtitle = subtitle
        self.domain_color = DOMAIN_COLORS.get(domain_name, C["primary"])
        self.bar_width = width or CONTENT_W

    def wrap(self, availWidth, availHeight):
        self.bar_width = min(self.bar_width, availWidth)
        h = 50 if self.subtitle else 36
        return self.bar_width, h

    def draw(self):
        h = 50 if self.subtitle else 36
        self.canv.saveState()
        self.canv.setFillColor(self.domain_color)
        self.canv.roundRect(0, 0, self.bar_width, h, 4, fill=1, stroke=0)
        # Domain letter
        letter = self.domain_name[0]
        self.canv.setFillColor(Color(1, 1, 1, alpha=0.3))
        self.canv.setFont(FONTS["heading"], 32)
        self.canv.drawString(12, 8 if not self.subtitle else 14, letter)
        # Domain name
        self.canv.setFillColor(C["white"])
        self.canv.setFont(FONTS["heading"], 18)
        self.canv.drawString(48, 12 if not self.subtitle else 24, self.domain_name)
        # Subtitle
        if self.subtitle:
            self.canv.setFont(FONTS["body_italic"], 10)
            self.canv.setFillColor(Color(1, 1, 1, alpha=0.8))
            self.canv.drawString(48, 8, self.subtitle)
        self.canv.restoreState()


class MarginStripe(Flowable):
    """Left margin color stripe running alongside content."""
    def __init__(self, color, height=20, width=6):
        super().__init__()
        self.color = color
        self.stripe_height = height
        self.stripe_width = width

    def wrap(self, availWidth, availHeight):
        return 0, 0  # doesn't take up flow space

    def draw(self):
        self.canv.saveState()
        self.canv.setFillColor(self.color)
        self.canv.rect(-MARGIN + 4, -self.stripe_height, self.stripe_width,
                       self.stripe_height, fill=1, stroke=0)
        self.canv.restoreState()


class ScoreBar(Flowable):
    """Horizontal score bar with optional vision marker."""
    def __init__(self, score, vision=None, color=None, width=200, height=14):
        super().__init__()
        self.score = score
        self.vision = vision
        self.bar_color = color or C["primary"]
        self.bar_width = width
        self.bar_height = height

    def wrap(self, availWidth, availHeight):
        return self.bar_width, self.bar_height + 4

    def draw(self):
        y = 2
        # Background track
        self.canv.setFillColor(C["divider"])
        self.canv.roundRect(0, y, self.bar_width, self.bar_height, 4, fill=1, stroke=0)
        # Fill
        fill_w = max(4, self.bar_width * (self.score / 100))
        self.canv.setFillColor(self.bar_color)
        self.canv.roundRect(0, y, fill_w, self.bar_height, 4, fill=1, stroke=0)
        # Vision dashed line
        if self.vision and self.vision > self.score:
            vx = self.bar_width * (self.vision / 100)
            self.canv.setStrokeColor(C["secondary"])
            self.canv.setDash(3, 2)
            self.canv.setLineWidth(1.5)
            self.canv.line(vx, y - 2, vx, y + self.bar_height + 2)
        # Score label
        self.canv.setFillColor(C["text"])
        self.canv.setFont(FONTS["mono"], 8)
        self.canv.drawString(self.bar_width + 6, y + 2, f"{self.score}%")


class RatingScale(Flowable):
    """Five circles rating scale — visual, not clinical."""
    def __init__(self, width=120, height=20):
        super().__init__()
        self.scale_width = width
        self.scale_height = height

    def wrap(self, availWidth, availHeight):
        return self.scale_width, self.scale_height

    def draw(self):
        self.canv.saveState()
        spacing = self.scale_width / 5
        labels = ["1", "2", "3", "4", "5"]
        for i in range(5):
            x = spacing * i + spacing / 2
            y = self.scale_height / 2
            # Circle
            self.canv.setStrokeColor(C["divider"])
            self.canv.setLineWidth(1)
            self.canv.setFillColor(C["white"])
            self.canv.circle(x, y, 7, fill=1, stroke=1)
            # Label
            self.canv.setFillColor(C["subtext"])
            self.canv.setFont(FONTS["body"], 7)
            self.canv.drawCentredString(x, y - 3, labels[i])
        self.canv.restoreState()


# ─────────────────────────────────────────────
# PAGE TEMPLATES — Headers & Footers
# ─────────────────────────────────────────────

def make_header_footer(canvas, doc, section_name="", show_bg=True):
    """Draw header and footer on every page (except cover)."""
    canvas.saveState()

    # Warm page background
    if show_bg:
        canvas.setFillColor(C["page_bg"])
        canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    # Header
    header_y = PAGE_H - 35
    canvas.setFont(FONTS["body_italic"], 9)
    canvas.setFillColor(C["primary"])
    canvas.drawString(MARGIN, header_y, "That Deeper Feeling")

    if section_name:
        canvas.setFont(FONTS["body"], 8)
        canvas.setFillColor(C["subtext"])
        canvas.drawCentredString(PAGE_W / 2, header_y, section_name)

    canvas.setFont(FONTS["body"], 8)
    canvas.setFillColor(C["subtext"])
    canvas.drawRightString(PAGE_W - MARGIN, header_y, str(doc.page))

    # Header line
    canvas.setStrokeColor(C["divider"])
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN, header_y - 6, PAGE_W - MARGIN, header_y - 6)

    # Footer
    footer_y = 25
    canvas.setStrokeColor(C["divider"])
    canvas.line(MARGIN, footer_y + 8, PAGE_W - MARGIN, footer_y + 8)
    canvas.setFont(FONTS["body"], 8)
    canvas.setFillColor(C["subtext"])
    canvas.drawCentredString(PAGE_W / 2, footer_y, "thatdeeperfeeling.com")

    canvas.restoreState()


def make_cover_page(canvas, doc):
    """Cover page — no header/footer, just warm bg."""
    canvas.saveState()
    canvas.setFillColor(C["page_bg"])
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.restoreState()


# ─────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────

def domain_h2(domain_name):
    """Create an H2 style colored by domain."""
    color = DOMAIN_COLORS.get(domain_name, C["primary"])
    return ParagraphStyle(
        f"H2_{domain_name}", fontName=FONTS["heading"], fontSize=22, leading=28,
        textColor=color, alignment=TA_LEFT, spaceAfter=12, spaceBefore=6,
    )


def voice_paragraph(text):
    """Create a paragraph in Kimberly's voice (EB Garamond, warm)."""
    return Paragraph(text, STYLES["voice"])


def voice_italic_paragraph(text):
    """Create an italic voice paragraph."""
    return Paragraph(text, STYLES["voice_italic"])


def section_break(title, domain_color=None):
    """Create a visual section break with title."""
    elements = []
    elements.append(Spacer(1, 20))
    elements.append(DividerLine(color=domain_color or C["accent"]))
    elements.append(Spacer(1, 12))
    color = domain_color or C["primary"]
    style = ParagraphStyle(
        "SectionBreak", fontName=FONTS["heading"], fontSize=22, leading=28,
        textColor=color, alignment=TA_CENTER, spaceAfter=12,
    )
    elements.append(Paragraph(title, style))
    elements.append(Spacer(1, 8))
    return elements
