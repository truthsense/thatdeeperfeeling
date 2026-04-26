"""
SPINE Framework — Intake & Welcome PDF Generator
Client-facing, warm, shame-aware intake document.
"""

import os
from datetime import datetime

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import Color
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame,
    Paragraph, Spacer, PageBreak,
)
from reportlab.platypus.doctemplate import NextPageTemplate

from style_system import (
    C, FONTS, STYLES, PAGE_W, PAGE_H, MARGIN, CONTENT_W,
    CoverBackground, DividerLine, LeftBorderBox, ResponseField,
    SectionDivider, make_header_footer,
    voice_paragraph, voice_italic_paragraph,
)


# ─────────────────────────────────────────────
# PAGE CALLBACKS
# ─────────────────────────────────────────────

def _cover_page(canvas, doc):
    """Cover with warm gradient."""
    canvas.saveState()
    top = C["cover_dark"]
    bottom = C["page_bg"]
    steps = 60
    for i in range(steps):
        t = i / steps
        r = top.red * (1 - t) + bottom.red * t
        g = top.green * (1 - t) + bottom.green * t
        b = top.blue * (1 - t) + bottom.blue * t
        y = PAGE_H - (i + 1) * (PAGE_H / steps)
        h = PAGE_H / steps + 1
        canvas.setFillColor(Color(r, g, b))
        canvas.rect(0, y, PAGE_W, h, fill=1, stroke=0)
    canvas.restoreState()


def _content_page(canvas, doc):
    """Content pages with header/footer."""
    make_header_footer(canvas, doc, section_name="Intake & Welcome")


# ─────────────────────────────────────────────
# COVER PAGE
# ─────────────────────────────────────────────

def _build_cover():
    """Page 1: Cover."""
    elements = []
    elements.append(Spacer(1, 100))

    # Title
    title_style = ParagraphStyle(
        "IntakeCoverTitle", fontName=FONTS["heading"], fontSize=36, leading=42,
        textColor=C["white"], alignment=TA_LEFT, spaceAfter=8,
    )
    elements.append(Paragraph("THAT DEEPER FEELING", title_style))

    sub_style = ParagraphStyle(
        "IntakeCoverSub", fontName=FONTS["body"], fontSize=14, leading=20,
        textColor=C["page_bg"], alignment=TA_LEFT, spaceAfter=4,
    )
    elements.append(Paragraph("Conscious Intimacy Coaching", sub_style))
    elements.append(Spacer(1, 24))
    elements.append(DividerLine())
    elements.append(Spacer(1, 24))

    # Central text
    center_style = ParagraphStyle(
        "IntakeCoverCenter", fontName=FONTS["heading_italic"], fontSize=16, leading=24,
        textColor=C["page_bg"], alignment=TA_LEFT, spaceAfter=8,
    )
    elements.append(Paragraph("Your SPINE Map", center_style))
    elements.append(Paragraph("begins here.", center_style))
    elements.append(Spacer(1, 24))
    elements.append(DividerLine())
    elements.append(Spacer(1, 30))

    # Client info placeholders
    info_style = ParagraphStyle(
        "IntakeCoverInfo", fontName=FONTS["body"], fontSize=12, leading=18,
        textColor=Color(0.85, 0.82, 0.78), alignment=TA_LEFT, spaceAfter=6,
    )
    elements.append(Paragraph("[Client Name]", info_style))
    elements.append(Paragraph(f"[Date]", info_style))

    elements.append(NextPageTemplate("content"))
    elements.append(PageBreak())
    return elements


# ─────────────────────────────────────────────
# THE WELCOME
# ─────────────────────────────────────────────

def _build_welcome():
    """Page 2: The Welcome — emotional tone setter."""
    elements = []
    elements.append(Spacer(1, 20))

    # Section title
    elements.append(Paragraph("Before we begin.", STYLES["h2"]))
    elements.append(Spacer(1, 16))

    paragraphs = [
        "There's something that happens when you leave "
        "a system that owned your insides.",

        "You get out. You breathe. You think \u2014 okay, "
        "now I can be myself. And then you realize "
        "you don't quite know what that means yet. "
        "Not because you're broken. Because the self "
        "you're trying to be was never given room to form.",

        "This is not a diagnostic. It's not a test. "
        "Nobody is going to read your answers and tell "
        "you what's wrong with you.",

        "What this is: a map-making exercise. "
        "You're going to look at some territory that "
        "most people spend their whole lives carefully "
        "not looking at \u2014 because the system you came "
        "from had it fenced off, locked up, or "
        "actively on fire.",

        "Some of what you find will make immediate sense. "
        "Some will surprise you. Some might make you cry "
        "or laugh or both simultaneously. All of it "
        "is information. None of it is verdict.",

        "Take your time. There are no right answers. "
        "\u201cI don't know yet\u201d is one of the most honest "
        "and useful things you can write on this page.",

        "You're safe here.",
    ]

    for para in paragraphs:
        elements.append(voice_paragraph(para))
        elements.append(Spacer(1, 4))

    elements.append(Spacer(1, 16))

    # Signature
    sig_style = ParagraphStyle(
        "Sig", fontName=FONTS["heading_italic"], fontSize=14, leading=20,
        textColor=C["primary"], alignment=TA_LEFT,
    )
    elements.append(Paragraph("\u2014 Kimberly", sig_style))

    elements.append(PageBreak())
    return elements


# ─────────────────────────────────────────────
# INTAKE QUESTIONS
# ─────────────────────────────────────────────

def _build_intake_questions():
    """Pages 3-4: Intake questions with response fields."""
    elements = []

    # ── Section 1: Who you are right now ──
    elements.append(Paragraph("Who you are right now", STYLES["h2"]))
    elements.append(Spacer(1, 8))

    questions_1 = [
        ("What name do you want me to use for you?", 30),
        ("How old are you?", 30),
        ("Are you currently in a relationship? If so, what kind?", 40),
        ("Are you currently in therapy or counseling?", 30),
    ]

    for q, h in questions_1:
        elements.append(Paragraph(q, STYLES["body"]))
        elements.append(Spacer(1, 4))
        elements.append(ResponseField(height=h))
        elements.append(Spacer(1, 12))

    elements.append(Spacer(1, 8))
    elements.append(SectionDivider())
    elements.append(Spacer(1, 12))

    # ── Section 2: How you're doing ──
    elements.append(Paragraph("How you're doing \u2014 honestly", STYLES["h2"]))
    elements.append(Spacer(1, 8))

    questions_2 = [
        ("On a scale of 1\u201310, how stable does your life feel right now?", 30),
        ("What does a typical day feel like in your body?", 60),
        ("When was the last time you felt genuinely at ease?", 60),
    ]

    for q, h in questions_2:
        elements.append(Paragraph(q, STYLES["body"]))
        elements.append(Spacer(1, 4))
        elements.append(ResponseField(height=h))
        elements.append(Spacer(1, 12))

    elements.append(Spacer(1, 8))
    elements.append(SectionDivider())
    elements.append(Spacer(1, 12))

    # ── Section 3: Your story ──
    elements.append(Paragraph("Your story in brief", STYLES["h2"]))
    elements.append(Spacer(1, 8))

    questions_3 = [
        ("What religious or high-control community did you come from?", 40),
        ("How long were you in it? When did you leave?", 40),
        ("What was the hardest thing about leaving?", 60),
    ]

    for q, h in questions_3:
        elements.append(Paragraph(q, STYLES["body"]))
        elements.append(Spacer(1, 4))
        elements.append(ResponseField(height=h))
        elements.append(Spacer(1, 12))

    elements.append(PageBreak())

    # ── Section 4: What brings you here ──
    elements.append(Paragraph("What brings you here", STYLES["h2"]))
    elements.append(Spacer(1, 8))

    questions_4 = [
        ("What made you seek this out right now?", 60),
        ("What do you most want to change, explore, or understand?", 60),
        ("Is there anything you're afraid I'll ask about?", 60),
    ]

    for q, h in questions_4:
        elements.append(Paragraph(q, STYLES["body"]))
        elements.append(Spacer(1, 4))
        elements.append(ResponseField(height=h))
        elements.append(Spacer(1, 12))

    elements.append(PageBreak())
    return elements


# ─────────────────────────────────────────────
# THE VISION SELF
# ─────────────────────────────────────────────

def _build_vision_self():
    """Page 5: The Vision Self — the most important question."""
    elements = []
    elements.append(Spacer(1, 30))

    # Section title
    elements.append(Paragraph("The most important question", STYLES["h2"]))
    elements.append(Spacer(1, 20))

    # The big question
    elements.append(Paragraph(
        "Close your eyes for a moment. Imagine the version of yourself "
        "who is completely free \u2014 not performing wellness, not performing "
        "rebellion, just free. What does she look like? How does she move "
        "through the world? What does her intimate life feel like? "
        "Her emotional life? How does she stand in her own authority?",
        STYLES["callout"]
    ))
    elements.append(Spacer(1, 20))

    # Large response area
    elements.append(ResponseField(height=260))
    elements.append(Spacer(1, 30))

    # Closing instruction
    elements.append(SectionDivider())
    elements.append(Spacer(1, 16))

    closing_paras = [
        "This is your compass.",
        "Every score, every gap, every practice "
        "points back to the person you just described.",
        "Keep her close.",
    ]

    for para in closing_paras:
        elements.append(voice_italic_paragraph(para))

    return elements


# ─────────────────────────────────────────────
# MAIN GENERATOR
# ─────────────────────────────────────────────

def generate_intake(output_dir="documents"):
    """Generate the Intake & Welcome PDF."""
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "intake_welcome.pdf")

    # Frames
    cover_frame = Frame(MARGIN, MARGIN, CONTENT_W, PAGE_H - 2 * MARGIN, id="cover")
    content_frame = Frame(MARGIN, MARGIN + 20, CONTENT_W, PAGE_H - 2 * MARGIN - 40, id="content")

    doc = BaseDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=MARGIN,
    )

    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[cover_frame], onPage=_cover_page),
        PageTemplate(id="content", frames=[content_frame], onPage=_content_page),
    ])

    # Build content
    elements = []
    elements.extend(_build_cover())
    elements.extend(_build_welcome())
    elements.extend(_build_intake_questions())
    elements.extend(_build_vision_self())

    doc.build(elements)
    print(f"  Generated: {output_path}")
    return output_path


if __name__ == "__main__":
    generate_intake()
