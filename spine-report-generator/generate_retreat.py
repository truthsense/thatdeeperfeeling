"""
SPINE Framework — Retreat Agenda PDF Generator
Three-day immersive retreat for women.
Full-bleed warm design, session detail, facilitator notes.
"""

import os

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
    CoverBackground, DividerLine, SectionDivider,
    LeftBorderBox, ColorStripe,
    make_header_footer,
    voice_paragraph, voice_italic_paragraph,
    section_break,
)


# ─────────────────────────────────────────────
# PAGE CALLBACKS
# ─────────────────────────────────────────────

def _cover_page(canvas, doc):
    """Cover with warm terracotta gradient."""
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
    make_header_footer(canvas, doc, section_name="Retreat Agenda")


# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────

def _time_block(time_str, title, duration):
    """Create a styled time block header."""
    elements = []
    elements.append(Spacer(1, 12))

    time_style = ParagraphStyle(
        f"TB_{time_str}", fontName=FONTS["heading"], fontSize=15, leading=20,
        textColor=C["accent"], alignment=TA_LEFT, spaceAfter=2,
    )
    elements.append(Paragraph(f"{time_str} \u2014 {title}", time_style))

    dur_style = ParagraphStyle(
        f"TBDur_{time_str}", fontName=FONTS["body_italic"], fontSize=9, leading=13,
        textColor=C["subtext"], alignment=TA_LEFT, spaceAfter=6,
    )
    elements.append(Paragraph(f"[{duration}]", dur_style))
    elements.append(Spacer(1, 4))
    return elements


def _facilitator_note(text):
    """Create a facilitator note box."""
    return LeftBorderBox(
        text,
        border_color=C["secondary"],
        bg_color=C["section_bg"],
        style=STYLES["facilitator"],
    )


# ─────────────────────────────────────────────
# COVER
# ─────────────────────────────────────────────

def _build_cover():
    """Cover page: warm, intimate."""
    elements = []
    elements.append(Spacer(1, 80))

    title_style = ParagraphStyle(
        "RetCoverTitle", fontName=FONTS["heading"], fontSize=36, leading=42,
        textColor=C["white"], alignment=TA_LEFT, spaceAfter=8,
    )
    elements.append(Paragraph("THAT DEEPER FEELING", title_style))

    elements.append(Spacer(1, 16))

    sub_style = ParagraphStyle(
        "RetCoverSub", fontName=FONTS["heading_italic"], fontSize=18, leading=26,
        textColor=C["page_bg"], alignment=TA_LEFT, spaceAfter=4,
    )
    elements.append(Paragraph("Growing the Spine", sub_style))
    elements.append(Paragraph("That Was Never Allowed to Form", sub_style))
    elements.append(Spacer(1, 24))
    elements.append(DividerLine())
    elements.append(Spacer(1, 24))

    detail_style = ParagraphStyle(
        "RetCoverDetail", fontName=FONTS["body"], fontSize=13, leading=20,
        textColor=Color(0.85, 0.82, 0.78), alignment=TA_LEFT, spaceAfter=4,
    )
    elements.append(Paragraph("A Three-Day Immersive Retreat", detail_style))
    elements.append(Paragraph("for Women", detail_style))
    elements.append(Spacer(1, 24))
    elements.append(DividerLine())
    elements.append(Spacer(1, 30))

    info_style = ParagraphStyle(
        "RetCoverInfo", fontName=FONTS["body_italic"], fontSize=11, leading=16,
        textColor=Color(0.75, 0.72, 0.68), alignment=TA_LEFT, spaceAfter=4,
    )
    elements.append(Paragraph("[Dates  \u00b7  Location]", info_style))
    elements.append(Paragraph("Facilitated by Kimberly Bryant", info_style))

    elements.append(NextPageTemplate("content"))
    elements.append(PageBreak())
    return elements


# ─────────────────────────────────────────────
# DAY ONE — ARRIVING
# ─────────────────────────────────────────────

def _build_day_one():
    """Day One: Arriving."""
    elements = []

    # Day header
    elements.append(ColorStripe(C["accent"], height=6))
    elements.append(Spacer(1, 12))

    day_h1 = ParagraphStyle(
        "DayH1_1", fontName=FONTS["heading"], fontSize=28, leading=34,
        textColor=C["accent"], alignment=TA_LEFT, spaceAfter=4,
    )
    elements.append(Paragraph("DAY ONE \u2014 ARRIVING", day_h1))

    tagline_style = ParagraphStyle(
        "DayTag_1", fontName=FONTS["heading_italic"], fontSize=14, leading=20,
        textColor=C["primary"], alignment=TA_LEFT, spaceAfter=16,
    )
    elements.append(Paragraph(
        "\u201cComing home to yourself before anything else is asked of you\u201d",
        tagline_style
    ))
    elements.append(SectionDivider())
    elements.append(Spacer(1, 4))

    # ── 3:00 PM — Arrival
    elements.extend(_time_block("3:00 PM", "Arrival & Sacred Space", "45 minutes"))
    paras = [
        "Women arrive and settle. No agenda yet. Tea, water, something warm. "
        "Soft music. The space itself doing its first work \u2014 signaling: this is "
        "different from ordinary life.",

        "Facilitator present but not facilitating. Just human. The conversations "
        "before the official beginning are often where the deepest first connections form.",
    ]
    for p in paras:
        elements.append(Paragraph(p, STYLES["body"]))
        elements.append(Spacer(1, 4))

    elements.append(Spacer(1, 4))
    elements.append(_facilitator_note(
        "Room setup: Circular seating. No tables between people. Candles. Botanicals. "
        "Warm low light. The SPINE illustration visible but not explained yet \u2014 "
        "something to be curious about."
    ))

    # ── 3:45 PM — Opening Circle
    elements.extend(_time_block("3:45 PM", "The Opening Circle", "60 minutes"))
    elements.append(voice_paragraph(
        "\u201cBefore we do anything else \u2014 just arrive. Feel your body in the chair. "
        "Your feet on the floor. You made it here. Whatever it took to get here \u2014 "
        "notice that you did it.\u201d"
    ))
    elements.append(Spacer(1, 4))

    paras = [
        "Two minutes of silence. Then the check-in: each woman shares one word for "
        "what she\u2019s carrying in, one word for what she\u2019s hoping for. No commentary "
        "from the group. Just receiving, around the circle.",

        "Then Kimberly: the framework introduction. Not a lecture. A story. The story "
        "of what the exoskeleton replaced. Fifteen minutes. Warm and specific \u2014 naming "
        "experiences the women in the room have likely had, in language that produces "
        "recognition rather than information.",
    ]
    for p in paras:
        elements.append(Paragraph(p, STYLES["body"]))
        elements.append(Spacer(1, 4))

    elements.append(Spacer(1, 4))
    elements.append(_facilitator_note(
        "Watch for: the small intake of breath, the eyes filling, the laugh of "
        "recognition. Those are the first unauthorized feelings arriving. "
        "Name them, gently: \u201cSomething is landing for some of you. Let it.\u201d"
    ))

    # ── 5:00 PM — Embodied Vision Self
    elements.extend(_time_block("5:00 PM", "The Embodied Vision Self", "75 minutes"))

    paras = [
        "Guided visualization \u2014 the most important practice of Day One.",

        "Lights lower. Soft music. Women lying down or in whatever position their "
        "body wants. Ten minutes of progressive arrival \u2014 breath, body contact, ground.",

        "Then the visualization: the free version of herself. Not perfect. Not performing "
        "wellness. Just free. What does she look like? How does she move? What does her "
        "intimate life feel like? Her emotional life? How does she stand in her own authority?",

        "Twenty minutes for the visualization. Silence after.",

        "Then: journaling. Fifteen minutes. The question: Who did you find?",

        "Then: small groups of three. Each woman shares \u2014 if she chooses \u2014 one thing "
        "she found. The group witnesses without comment, without advice, without "
        "\u201cme too\u201d in that moment. Just receives.",
    ]
    for p in paras:
        elements.append(Paragraph(p, STYLES["body"]))
        elements.append(Spacer(1, 4))

    elements.append(Spacer(1, 4))
    elements.append(_facilitator_note(
        "This visualization sometimes surfaces grief rather than vision. The free self "
        "feels impossibly distant rather than imaginable. If this happens for someone \u2014 "
        "let it. The grief is the first unauthorized feeling. It belongs here."
    ))

    # ── 6:30 PM — Dinner
    elements.extend(_time_block("6:30 PM", "Dinner Together", "90 minutes"))
    elements.append(Paragraph(
        "Shared meal. No agenda. Facilitator present and human \u2014 not leading, "
        "not processing, just being. The table is its own kind of practice.",
        STYLES["body"]
    ))

    # ── 8:00 PM — Spider Map Introduction
    elements.extend(_time_block("8:00 PM", "The Spider Map Introduction", "60 minutes"))

    elements.append(Paragraph(
        "Introduction to the SPINE framework \u2014 the five domains. Not through a lecture. "
        "Through questions.",
        STYLES["body"]
    ))
    elements.append(Spacer(1, 6))

    questions = [
        ("Sovereignty:", "\u201cWhen was the last time you had a thought or feeling and just \u2014 "
         "let it be yours, before you evaluated whether you were allowed to have it?\u201d"),
        ("Power:", "\u201cWhen did you last give yourself permission for something without "
         "waiting for someone else to grant it?\u201d"),
        ("Identity:", "\u201cWho shows up when no one is watching and no one is telling you "
         "who you should be?\u201d"),
        ("Nourishment:", "\u201cWhat have you been calling sin that might have been food?\u201d"),
        ("Embodiment:", "\u201cWhen did you last feel genuinely at home in your body?\u201d"),
    ]
    for domain, question in questions:
        elements.append(Paragraph(f"<b>{domain}</b> {question}", STYLES["body"]))
        elements.append(Spacer(1, 4))

    elements.append(Spacer(1, 4))
    elements.append(Paragraph(
        "No answers required. Just sitting with the questions. Journal time after each one. "
        "Brief introduction to the spider chart concept \u2014 not scores yet, just the visual "
        "metaphor of the two shapes and the gap between them.",
        STYLES["body"]
    ))

    # ── 9:00 PM — Evening Practice
    elements.extend(_time_block("9:00 PM", "Evening Practice & Close", "30 minutes"))
    elements.append(voice_paragraph(
        "The first Daily Return practice \u2014 done together, in the room.\n"
        "\u201cBefore you sleep tonight \u2014 find your hands. Let them land on your body "
        "without deciding where first. Stay for sixty seconds. One breath longer "
        "going out. And then: I live here.\u201d"
    ))
    elements.append(Spacer(1, 4))
    elements.append(Paragraph(
        "Practice together in the room first. Then close the day with a brief ceremony. "
        "Candle lighting \u2014 each woman lights one. The room holds their lights together "
        "for a moment before they take them to their rooms.",
        STYLES["body"]
    ))

    elements.append(PageBreak())
    return elements


# ─────────────────────────────────────────────
# DAY TWO — THE RECLAMATION
# ─────────────────────────────────────────────

def _build_day_two():
    """Day Two: The Reclamation."""
    elements = []

    elements.append(ColorStripe(C["primary"], height=6))
    elements.append(Spacer(1, 12))

    day_h1 = ParagraphStyle(
        "DayH1_2", fontName=FONTS["heading"], fontSize=28, leading=34,
        textColor=C["primary"], alignment=TA_LEFT, spaceAfter=4,
    )
    elements.append(Paragraph("DAY TWO \u2014 THE RECLAMATION", day_h1))

    tagline_style = ParagraphStyle(
        "DayTag_2", fontName=FONTS["heading_italic"], fontSize=14, leading=20,
        textColor=C["accent"], alignment=TA_LEFT, spaceAfter=16,
    )
    elements.append(Paragraph(
        "\u201cSovereignty, Power, and the things that were starved\u201d",
        tagline_style
    ))
    elements.append(SectionDivider())
    elements.append(Spacer(1, 4))

    # ── 7:30 AM — Morning Movement
    elements.extend(_time_block("7:30 AM", "Morning Movement", "45 minutes"))
    elements.append(Paragraph(
        "No words. Music. Bodies moving however they want to move. The explicit "
        "instruction: \u201cThere is no right way to do this. You cannot do this wrong.\u201d",
        STYLES["body"]
    ))
    elements.append(Spacer(1, 4))
    elements.append(_facilitator_note(
        "Many women from these systems have never moved their bodies for their own "
        "pleasure. This is the first practice of Day Two \u2014 the body expressing itself "
        "before the day asks anything of it. Kimberly moving in the room, not "
        "demonstrating a right way but modeling freedom. If someone freezes \u2014 "
        "a gentle hand on the shoulder, a quiet \u201cyour body knows\u201d if needed."
    ))

    # ── 8:30 AM — Breakfast
    elements.extend(_time_block("8:30 AM", "Breakfast", "60 minutes"))
    elements.append(Spacer(1, 4))

    # ── 9:30 AM — The Assessment
    elements.extend(_time_block("9:30 AM", "The Assessment", "90 minutes"))
    paras = [
        "The full SPINE Self-Map \u2014 completed individually, in silence. Soft music. "
        "Women working through the inventory at their own pace.",

        "Facilitator available but not hovering. Tissues available. Permission to stop "
        "if something becomes too much.",

        "After completion: each woman draws her rough shape \u2014 the meta spider chart "
        "by hand in her journal. Not precise. Just the approximate shape of where she is.",
    ]
    for p in paras:
        elements.append(Paragraph(p, STYLES["body"]))
        elements.append(Spacer(1, 4))
    elements.append(Spacer(1, 2))
    elements.append(voice_italic_paragraph(
        "Partner share (pairs): \u201cWhat does your shape show you that you already knew? "
        "What surprises you?\u201d"
    ))

    # ── 11:00 AM — Sovereignty Work
    elements.extend(_time_block("11:00 AM", "Sovereignty Work", "90 minutes"))
    elements.append(Paragraph(
        "Teaching: Interior Ownership \u2014 the specific way the system claimed your "
        "inner life, and what it looks like to begin taking it back. Twenty minutes. "
        "Stories and recognition.",
        STYLES["body"]
    ))
    elements.append(Spacer(1, 6))

    elements.append(Paragraph("Activity \u2014 The Interior Inventory:", STYLES["h3"]))
    elements.append(Paragraph(
        "Three things in my interior that feel genuinely mine. Three things I\u2019m still "
        "not sure about. Three things I\u2019ve been told belong to God, the community, my "
        "spouse, the doctrine \u2014 that I want to look at. Not to resolve. Just to look.",
        STYLES["body"]
    ))
    elements.append(Spacer(1, 8))

    elements.append(Paragraph("Activity \u2014 The Shame Source Circle:", STYLES["h3"]))
    elements.append(Paragraph(
        "Facilitator reads each shame source slowly, with space. Women silently rate "
        "their own response. Then: \u201cWithout saying what it is \u2014 raise your hand if "
        "any of these scored 4 or 5.\u201d",
        STYLES["body"]
    ))
    elements.append(Spacer(1, 4))
    elements.append(voice_italic_paragraph(
        "Nearly every hand goes up."
    ))
    elements.append(voice_italic_paragraph(
        "\u201cLook around the room.\u201d"
    ))
    elements.append(Spacer(1, 4))
    elements.append(_facilitator_note(
        "That moment \u2014 without anyone speaking a specific shame aloud \u2014 "
        "is often the most powerful of the retreat."
    ))

    # ── 12:30 PM — Lunch
    elements.extend(_time_block("12:30 PM", "Lunch", "75 minutes"))
    elements.append(Spacer(1, 4))

    # ── 2:00 PM — Power and Voice
    elements.extend(_time_block("2:00 PM", "Power and Voice", "90 minutes"))
    elements.append(Paragraph(
        "Teaching: Self-Authorization and Voice Activation \u2014 the specific targeting "
        "of your voice by the system, and what it looks like to begin speaking from "
        "your own center. Twenty minutes.",
        STYLES["body"]
    ))
    elements.append(Spacer(1, 6))

    elements.append(Paragraph("Activity \u2014 The Small Yes:", STYLES["h3"]))
    elements.append(Paragraph(
        "Each woman identifies one thing she\u2019s been waiting for permission to do. "
        "Writes it. Then says it aloud to one other person: \u201cI give myself "
        "permission to ___.\u201d",
        STYLES["body"]
    ))
    elements.append(Spacer(1, 4))
    elements.append(_facilitator_note(
        "The witnessing of another woman giving herself permission \u2014 and being "
        "witnessed doing so \u2014 is itself healing. Watch for it landing in the room."
    ))
    elements.append(Spacer(1, 8))

    elements.append(Paragraph("Activity \u2014 The Voice Practice (pairs):", STYLES["h3"]))
    elements.append(Paragraph(
        "One woman speaks, one witnesses. Speaking woman completes three sentences:",
        STYLES["body"]
    ))
    voice_prompts = [
        "\u201cSomething I\u2019ve never said out loud about what I want is ___.\u201d",
        "\u201cSomething I\u2019ve been afraid to say in an intimate context is ___.\u201d",
        "\u201cSomething I\u2019m giving myself permission to say from now on is ___.\u201d",
    ]
    for vp in voice_prompts:
        elements.append(Paragraph(vp, STYLES["callout_small"]))
        elements.append(Spacer(1, 2))
    elements.append(Spacer(1, 4))
    elements.append(Paragraph(
        "Witness\u2019s only role: be fully present. No advice. No \u201cme too\u201d in this moment. "
        "Just receive. Then switch.",
        STYLES["body"]
    ))

    # ── 3:45 PM — Break
    elements.extend(_time_block("3:45 PM", "Break", "30 minutes"))
    elements.append(Spacer(1, 4))

    # ── 4:15 PM — Nourishment
    elements.extend(_time_block("4:15 PM", "Nourishment", "90 minutes"))
    elements.append(Paragraph(
        "Teaching: The Starvation Story. What the system said about your desire. "
        "What the hunger actually is. What you\u2019ve been calling sin that was actually "
        "food. Kimberly\u2019s own story, appropriately and selectively shared, is the "
        "most powerful vehicle for this teaching.",
        STYLES["body"]
    ))
    elements.append(Spacer(1, 6))

    elements.append(Paragraph("Activity \u2014 The Want List:", STYLES["h3"]))
    elements.append(Paragraph(
        "Private writing. Everything you\u2019ve ever wanted, been curious about, been "
        "drawn to \u2014 that the system said was wrong or dangerous. Not to act on. "
        "Just to see.",
        STYLES["body"]
    ))
    elements.append(Spacer(1, 2))
    elements.append(voice_italic_paragraph(
        "\u201cIf you want to burn this list after, that\u2019s yours to choose. But first \u2014 "
        "make it. See it. Let yourself see what\u2019s actually there.\u201d"
    ))
    elements.append(Spacer(1, 8))

    elements.append(Paragraph("Activity \u2014 What Was Starved (small groups of three):", STYLES["h3"]))
    elements.append(Paragraph(
        "Each person shares \u2014 if they choose \u2014 one thing that was starved in them. "
        "The group witnesses without evaluation, advice, or silver lining.",
        STYLES["body"]
    ))
    elements.append(Spacer(1, 4))
    elements.append(_facilitator_note(
        "Facilitator models: \u201cI receive that.\u201d The group follows. This is where both "
        "irreducible moments occur simultaneously: unauthorized feeling in the speaking, "
        "non-evaluative witnessing in the receiving."
    ))

    # ── 6:00 PM — Free Time
    elements.extend(_time_block("6:00 PM", "Free Time / Rest", "90 minutes"))
    elements.append(Spacer(1, 4))

    # ── 7:30 PM — Sensory Feast
    elements.extend(_time_block("7:30 PM", "The Sensory Feast", "60 minutes"))
    elements.append(Paragraph(
        "Stations of pure sensory pleasure \u2014 taste, texture, sound, scent, warmth. "
        "Women move through at their own pace.",
        STYLES["body"]
    ))
    elements.append(Spacer(1, 2))
    elements.append(voice_italic_paragraph(
        "\u201cYour only job is to notice what you notice. Stay as long as something is "
        "interesting. Leave when it\u2019s done.\u201d"
    ))
    elements.append(Paragraph(
        "No discussion during. Journaling after.",
        STYLES["body"]
    ))

    # ── 8:30 PM — Evening Ceremony
    elements.extend(_time_block("8:30 PM", "Evening Ceremony", "45 minutes"))
    paras = [
        "The want lists from the afternoon \u2014 held, offered, burned (if chosen). "
        "Each woman chooses what to do with hers.",

        "Then: candle circle. Each woman speaks one sentence aloud: "
        "\u201cI am allowed to ___.\u201d",

        "Full circle. Witnessed by all. The room holds the collection of permissions "
        "together for a moment before closing.",
    ]
    for p in paras:
        elements.append(Paragraph(p, STYLES["body"]))
        elements.append(Spacer(1, 4))

    elements.append(PageBreak())
    return elements


# ─────────────────────────────────────────────
# DAY THREE — THE BODY IS THE HOME
# ─────────────────────────────────────────────

def _build_day_three():
    """Day Three: The Body Is the Home."""
    elements = []

    elements.append(ColorStripe(C["embodiment"], height=6))
    elements.append(Spacer(1, 12))

    day_h1 = ParagraphStyle(
        "DayH1_3", fontName=FONTS["heading"], fontSize=28, leading=34,
        textColor=C["embodiment"], alignment=TA_LEFT, spaceAfter=4,
    )
    elements.append(Paragraph("DAY THREE \u2014 THE BODY IS THE HOME", day_h1))

    tagline_style = ParagraphStyle(
        "DayTag_3", fontName=FONTS["heading_italic"], fontSize=14, leading=20,
        textColor=C["accent"], alignment=TA_LEFT, spaceAfter=16,
    )
    elements.append(Paragraph(
        "\u201cEmbodiment, integration, and the spine that is growing\u201d",
        tagline_style
    ))
    elements.append(SectionDivider())
    elements.append(Spacer(1, 4))

    # ── 7:30 AM — Embodied Morning
    elements.extend(_time_block("7:30 AM", "The Embodied Morning", "60 minutes"))
    elements.append(Paragraph(
        "Gentle yoga or somatic movement \u2014 not about achievement, about arrival. "
        "A guide who understands this population (no performance cues, no \u201cpush "
        "yourself,\u201d only invitation).",
        STYLES["body"]
    ))
    elements.append(Spacer(1, 2))
    elements.append(Paragraph(
        "Or, if no movement guide: thirty minutes of the Daily Return practice done "
        "together, followed by thirty minutes of free movement to music.",
        STYLES["body"]
    ))

    # ── 9:00 AM — Breakfast
    elements.extend(_time_block("9:00 AM", "Breakfast", "60 minutes"))
    elements.append(Spacer(1, 4))

    # ── 10:00 AM — Embodiment Work
    elements.extend(_time_block("10:00 AM", "Embodiment Work", "90 minutes"))
    elements.append(Paragraph(
        "Teaching: The Body as Home. How the system located authority in the spirit "
        "and made the body a site of danger and management. What re-embodiment "
        "actually looks like \u2014 not transcendence of the body, but return to it. "
        "Twenty minutes.",
        STYLES["body"]
    ))
    elements.append(Spacer(1, 6))

    elements.append(Paragraph("Activity \u2014 Body Gratitude (Revisioned):", STYLES["h3"]))
    elements.append(Paragraph(
        "Not \u201cthank your body for what it does for you.\u201d Instead: \u201cThank your body "
        "for what it survived. For what it held. For the desire it kept alive when "
        "you were trying to suppress it. For the no it knew before you let yourself "
        "know it. For waiting.\u201d",
        STYLES["body"]
    ))
    elements.append(Spacer(1, 2))
    elements.append(Paragraph(
        "Written, then spoken aloud \u2014 to their own body, privately, hands on the "
        "relevant part.",
        STYLES["body"]
    ))
    elements.append(Spacer(1, 8))

    elements.append(Paragraph("Activity \u2014 Felt Sense Introduction:", STYLES["h3"]))
    elements.append(Paragraph(
        "Brief introduction to the felt sense (Gendlin\u2019s Focusing, simplified). "
        "One question: \u201cIs there somewhere in your body right now that has something "
        "to say about this weekend?\u201d",
        STYLES["body"]
    ))
    elements.append(Spacer(1, 2))
    elements.append(Paragraph(
        "Let the body speak in whatever language it chooses \u2014 sensation, image, "
        "impulse, emotion. Just receive it.",
        STYLES["body"]
    ))

    # ── 11:30 AM — Integration Work
    elements.extend(_time_block("11:30 AM", "Integration Work", "90 minutes"))

    elements.append(Paragraph("Activity \u2014 The SPINE Portrait:", STYLES["h3"]))
    elements.append(Paragraph(
        "Each woman draws her own SPINE \u2014 five vertebrae, labeled, decorated "
        "according to where she is in each domain. Not for assessment. For claiming. "
        "This goes home with her.",
        STYLES["body"]
    ))
    elements.append(Spacer(1, 8))

    elements.append(Paragraph("Activity \u2014 The Practice Prescription (self-written):", STYLES["h3"]))
    elements.append(Paragraph(
        "Each woman identifies her top three practices. Writes them in her own words. "
        "Names why she\u2019s choosing these.",
        STYLES["body"]
    ))
    elements.append(Spacer(1, 8))

    elements.append(Paragraph("Small groups \u2014 The Commitment Share:", STYLES["h3"]))
    elements.append(Paragraph(
        "Each person shares her three practices. The group witnesses. No advice. "
        "\u201cI hear that you\u2019re going to ___.\u201d The public naming is part of the commitment.",
        STYLES["body"]
    ))

    # ── 1:00 PM — Lunch
    elements.extend(_time_block("1:00 PM", "Lunch & Transition", "90 minutes"))
    elements.append(Spacer(1, 4))

    # ── 2:30 PM — Closing Ceremony
    elements.extend(_time_block("2:30 PM", "The Closing Ceremony", "90 minutes"))

    elements.append(Paragraph("Activity \u2014 Letters to the Free Self:", STYLES["h3"]))
    elements.append(Paragraph(
        "Each woman writes a letter to the version of herself she described in the "
        "Day One visualization. What do you want to tell her? What are you on the "
        "way to? What do you need her to know?",
        STYLES["body"]
    ))
    elements.append(Spacer(1, 2))
    elements.append(voice_italic_paragraph(
        "Sealed. Addressed to themselves. Kimberly mails them in three months."
    ))
    elements.append(Spacer(1, 8))

    elements.append(Paragraph("The Final Circle:", STYLES["h3"]))
    elements.append(Spacer(1, 4))

    elements.append(Paragraph(
        "Each woman completes one sentence: \u201cI am taking one thing from this retreat "
        "that belongs to me now.\u201d",
        STYLES["body"]
    ))
    elements.append(Spacer(1, 8))

    # Kimberly's closing
    elements.append(SectionDivider())
    elements.append(Spacer(1, 12))

    closing_paras = [
        "You came here with a spine that was prevented from forming. "
        "Not broken \u2014 prevented. There\u2019s a difference. Broken things "
        "need repair. Prevented things need permission.",

        "Over three days you\u2019ve looked at territory that the system "
        "fenced off, locked up, or set on fire. You\u2019ve named what was "
        "starved. You\u2019ve spoken what was silenced. You\u2019ve let your body "
        "tell you something true.",

        "The spine is growing. Not all at once. Not perfectly. "
        "But it\u2019s growing. And nobody gets to stop it now.",

        "Take your practices home. Do them imperfectly. Skip days. "
        "Come back. The body is patient. It\u2019s been waiting for you "
        "to come home. It will wait a little longer if it needs to.",

        "But you started. That\u2019s the part that can\u2019t be undone.",
    ]
    for p in closing_paras:
        elements.append(voice_paragraph(p))
        elements.append(Spacer(1, 2))

    elements.append(Spacer(1, 16))
    elements.append(DividerLine())
    elements.append(Spacer(1, 12))
    elements.append(voice_italic_paragraph(
        "You are the evidence that leaving doesn\u2019t mean losing yourself. "
        "Go be evidence."
    ))
    elements.append(Spacer(1, 8))

    sig_style = ParagraphStyle(
        "RetSig", fontName=FONTS["heading_italic"], fontSize=14, leading=20,
        textColor=C["primary"], alignment=TA_LEFT,
    )
    elements.append(Paragraph("\u2014 Kimberly", sig_style))

    return elements


# ─────────────────────────────────────────────
# MAIN GENERATOR
# ─────────────────────────────────────────────

def generate_retreat(output_dir="documents"):
    """Generate the Retreat Agenda PDF."""
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "retreat_agenda.pdf")

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

    elements = []
    elements.extend(_build_cover())
    elements.extend(_build_day_one())
    elements.extend(_build_day_two())
    elements.extend(_build_day_three())

    doc.build(elements)
    print(f"  Generated: {output_path}")
    return output_path


if __name__ == "__main__":
    generate_retreat()
