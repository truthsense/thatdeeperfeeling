"""
SPINE Framework — Self-Map Assessment PDF Generator
The full inventory, beautifully formatted.
Client-facing document with all five domains, 100 questions,
flag questions, body checks, and shame source locator.
"""

import os

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import Color
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame,
    Paragraph, Spacer, PageBreak, Table, TableStyle,
)
from reportlab.platypus.doctemplate import NextPageTemplate

from style_system import (
    C, FONTS, STYLES, PAGE_W, PAGE_H, MARGIN, CONTENT_W,
    DOMAIN_COLORS,
    CoverBackground, DividerLine, SectionDivider,
    DomainHeader, RatingScale, LeftBorderBox,
    make_header_footer,
    voice_paragraph, voice_italic_paragraph,
)


# ─────────────────────────────────────────────
# ASSESSMENT QUESTIONS — Complete Inventory
# ─────────────────────────────────────────────

DOMAIN_SUBTITLES = {
    "Sovereignty": "Your inner territory \u2014 the parts of you that belong to you",
    "Power": "Your capacity to act, speak, choose, and refuse from your own center",
    "Identity": "Who you are when no one is telling you who to be",
    "Nourishment": "What you need, want, and are allowed to enjoy",
    "Embodiment": "Your relationship with the body you actually live in",
}

ASSESSMENT_QUESTIONS = {
    "Sovereignty": {
        "Interior Ownership": [
            "My thoughts feel like they belong to me.",
            "I can have a feeling without immediately evaluating whether it's acceptable.",
            "I can sit with an idea that contradicts what I was taught without panic.",
            "I trust my own internal responses as valid data.",
            "I don't need someone else to confirm what I'm experiencing before I believe it.",
        ],
        "Shame Jurisdiction": [
            "When shame arrives, I can usually tell whether it's mine or installed.",
            "I can feel shame without it defining me.",
            "I can trace most of my shame responses back to a specific origin.",
            "I no longer automatically believe that shame means I've done something wrong.",
            "I can distinguish between guilt I've earned and shame I was given.",
        ],
        "Boundary Recognition": [
            "I can tell the difference between my feelings and someone else's expectations.",
            "I know when I'm doing something because I want to versus because I should.",
            "I can feel where I end and another person begins in a conversation.",
            "I notice when someone is projecting their needs onto me.",
            "I can hold my own perspective even when someone I respect disagrees.",
        ],
        "Doubt Permission": [
            "I can hold a question without needing to resolve it immediately.",
            "Uncertainty doesn't feel like a moral failure to me.",
            "I can say 'I don't know' without it feeling dangerous.",
            "I'm comfortable with the idea that I might change my mind about important things.",
            "I can explore a new idea without deciding whether it's right or wrong first.",
        ],
    },
    "Power": {
        "Self-Authorization": [
            "I give myself permission for things without waiting for someone else to approve.",
            "I can make a decision without checking if it's okay with everyone first.",
            "I act on my own judgment even when it might displease someone.",
            "I don't need external validation to feel confident in a choice.",
            "I can start something new without asking whether I'm allowed to.",
        ],
        "Voice Activation": [
            "I speak up when something matters to me, even if my voice shakes.",
            "I can say what I actually think in a group without rehearsing first.",
            "My voice feels like it belongs to me when I use it.",
            "I can express disagreement without feeling like I'm being destructive.",
            "I say the true thing more often than the safe thing.",
        ],
        "Choice Ownership": [
            "I feel like the author of my own daily choices.",
            "I can own a decision without immediately defending it.",
            "I choose things for myself rather than defaulting to what's expected.",
            "I take responsibility for my choices without excessive guilt.",
            "I can choose something that only benefits me without feeling selfish.",
        ],
        "Refusal Capacity": [
            "I can say no to something I don't want without extensive justification.",
            "My body gives me clear signals when something isn't right for me.",
            "I can decline an invitation or request without guilt taking over.",
            "I trust my no as much as I trust my yes.",
            "I can refuse something even when the other person will be disappointed.",
        ],
    },
    "Identity": {
        "Self-Authorship": [
            "I have a clear sense of who I am apart from what I was taught to be.",
            "My values feel chosen rather than inherited.",
            "I can describe myself without referencing what I used to believe.",
            "I'm building an identity that feels genuinely mine.",
            "I know what I stand for, even if it's different from what I was raised with.",
        ],
        "Authentic Differentiation": [
            "I can be close to someone without losing myself.",
            "I can love someone whose beliefs are different from mine without it threatening my identity.",
            "I know the difference between being influenced and being controlled.",
            "I can be part of a group without performing agreement I don't feel.",
            "My closest relationships allow me to be fully myself.",
        ],
        "Complexity Tolerance": [
            "I can hold two contradictory ideas without needing to resolve them immediately.",
            "I'm comfortable with people who are different from me.",
            "I don't need things to be all good or all bad to understand them.",
            "I can appreciate something about a system I ultimately left.",
            "I can sit with ambiguity without it feeling like a crisis.",
        ],
        "Evolutionary Relationship": [
            "I see my past self with compassion rather than contempt.",
            "I can integrate parts of my history without being defined by them.",
            "I'm curious about who I'm becoming rather than anxious about it.",
            "I allow myself to change without feeling like I'm betraying who I was.",
            "My sense of self feels like it's growing rather than fracturing.",
        ],
    },
    "Nourishment": {
        "Desire Recognition": [
            "I can name what I want without immediately evaluating whether I should want it.",
            "I notice my desires as they arise rather than after I've already suppressed them.",
            "I can distinguish between what I genuinely want and what I think I should want.",
            "My wants feel like valid information about who I am.",
            "I can sit with a desire without acting on it or killing it \u2014 just letting it be.",
        ],
        "Pleasure Capacity": [
            "I can experience physical pleasure without guilt arriving immediately after.",
            "My body knows how to relax into something that feels good.",
            "I can stay present during a pleasurable experience without dissociating or numbing.",
            "I give myself permission to enjoy things that have no productive purpose.",
            "Pleasure feels safe to me most of the time.",
        ],
        "Need Legitimacy": [
            "I believe my needs are valid even when they're inconvenient for others.",
            "I can ask for what I need without feeling like I'm being too much.",
            "I don't minimize my own needs to make other people more comfortable.",
            "I can receive care without feeling like I have to earn it first.",
            "I trust that needing things is a normal part of being human, not a weakness.",
        ],
        "Erotic Reclamation": [
            "I can think about my own sexuality without shame taking over.",
            "My erotic life feels like it belongs to me.",
            "I can explore what turns me on without judging myself for it.",
            "I can be sexually present \u2014 with myself or a partner \u2014 without leaving my body.",
            "My sexuality feels like a natural part of who I am rather than something to manage.",
        ],
    },
    "Embodiment": {
        "Somatic Presence": [
            "I can feel my body from the inside \u2014 not just see it from the outside.",
            "I notice physical sensations as they happen rather than hours later.",
            "I can stay present in my body during an emotional conversation.",
            "My body feels like a place I live rather than a thing I operate.",
            "I trust the information my body gives me.",
        ],
        "Body Trust": [
            "I trust my body's signals about what it needs.",
            "I can feel hunger, tiredness, or discomfort without overriding it.",
            "My body feels like an ally rather than an obstacle.",
            "I don't manage my body as if it's something that might betray me.",
            "I listen to my body before I listen to the rules about my body.",
        ],
        "Pleasure Residency": [
            "I can feel pleasure in my body without immediately analyzing it.",
            "My body remembers how to feel good, even if it took time to get here.",
            "I can be touched (by myself or others) without bracing.",
            "Physical warmth, softness, and comfort feel safe to receive.",
            "I can stay in my body when it starts to feel something good.",
        ],
        "Integrated Knowing": [
            "My body and my mind usually agree about what's true.",
            "I can make decisions using gut feeling alongside logic.",
            "When I check in with my body, I get useful information.",
            "I trust my body's 'yes' and 'no' as much as my rational assessment.",
            "My physical responses and my conscious thoughts are starting to align.",
        ],
    },
}

FLAG_QUESTIONS = {
    "Sovereignty": {
        "Interior Ownership": "When I think about owning my inner life completely, my body responds with:",
        "Shame Jurisdiction": "When I imagine returning shame to its source, my body responds with:",
        "Boundary Recognition": "When I hold my own boundary clearly, my body responds with:",
        "Doubt Permission": "When I let myself not know something important, my body responds with:",
    },
    "Power": {
        "Self-Authorization": "When I imagine giving myself full permission, my body responds with:",
        "Voice Activation": "When I imagine speaking my full truth, my body responds with:",
        "Choice Ownership": "When I own a choice that might displease someone, my body responds with:",
        "Refusal Capacity": "When I imagine saying no to someone I care about, my body responds with:",
    },
    "Identity": {
        "Self-Authorship": "When I imagine being fully self-defined, my body responds with:",
        "Authentic Differentiation": "When I hold my own perspective against pressure, my body responds with:",
        "Complexity Tolerance": "When I sit with genuine ambiguity, my body responds with:",
        "Evolutionary Relationship": "When I allow myself to be different from who I was, my body responds with:",
    },
    "Nourishment": {
        "Desire Recognition": "When I let a desire exist without evaluating it, my body responds with:",
        "Pleasure Capacity": "When I let myself enjoy something fully, my body responds with:",
        "Need Legitimacy": "When I ask for something I need, my body responds with:",
        "Erotic Reclamation": "When I think about my sexuality as mine, my body responds with:",
    },
    "Embodiment": {
        "Somatic Presence": "When I try to feel my body from the inside, my body responds with:",
        "Body Trust": "When I trust my body completely, my body responds with:",
        "Pleasure Residency": "When pleasure arrives in my body, my body responds with:",
        "Integrated Knowing": "When my body says something different from my mind, my body responds with:",
    },
}

BODY_CHECK_QUESTIONS = {
    "Sovereignty": "After sitting with these questions about your inner territory, what is your body doing right now?",
    "Power": "After exploring your relationship to power, voice, and choice, what is your body doing right now?",
    "Identity": "After looking at who you are apart from the system, what is your body doing right now?",
    "Nourishment": "After sitting with questions about desire, pleasure, and need, what is your body doing right now?",
    "Embodiment": "After exploring your relationship with your own body, what is your body doing right now?",
}

BODY_CHECK_OPTIONS = [
    "Curiosity \u2014 open, interested, maybe a little energized",
    "Mild resistance \u2014 some tightening, but I can stay with it",
    "Resistance \u2014 wanting to move away, close the document, do something else",
    "Significant resistance \u2014 tension, constriction, bracing",
    "Distress \u2014 flooding, rapid heartbeat, wanting to shut down",
    "Blankness \u2014 nothing, numbness, an absence of response",
]

SHAME_SOURCES = [
    "Having desire at all",
    "Specific desires or fantasies",
    "My sexual history",
    "My body's appearance or physical responses",
    "My orientation or attractions",
    "Having strong emotions",
    "Doubting or leaving the system",
    "Choices I made inside the system",
    "How much I need from other people",
    "Speaking up or using my voice",
]


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
    make_header_footer(canvas, doc, section_name="SPINE Self-Map Assessment")


# ─────────────────────────────────────────────
# COVER PAGE
# ─────────────────────────────────────────────

def _build_cover():
    """Page 1: Cover."""
    elements = []
    elements.append(Spacer(1, 100))

    title_style = ParagraphStyle(
        "AssessCoverTitle", fontName=FONTS["heading"], fontSize=36, leading=42,
        textColor=C["white"], alignment=TA_LEFT, spaceAfter=8,
    )
    elements.append(Paragraph("THAT DEEPER FEELING", title_style))

    sub_style = ParagraphStyle(
        "AssessCoverSub", fontName=FONTS["body"], fontSize=14, leading=20,
        textColor=C["page_bg"], alignment=TA_LEFT, spaceAfter=4,
    )
    elements.append(Paragraph("Conscious Intimacy Coaching", sub_style))
    elements.append(Spacer(1, 24))
    elements.append(DividerLine())
    elements.append(Spacer(1, 24))

    center_style = ParagraphStyle(
        "AssessCoverCenter", fontName=FONTS["heading_italic"], fontSize=18, leading=26,
        textColor=C["page_bg"], alignment=TA_LEFT, spaceAfter=6,
    )
    elements.append(Paragraph("Your SPINE Self-Map", center_style))
    elements.append(Spacer(1, 6))

    tagline_style = ParagraphStyle(
        "AssessCoverTag", fontName=FONTS["heading_italic"], fontSize=13, leading=20,
        textColor=Color(0.85, 0.82, 0.78), alignment=TA_LEFT,
    )
    elements.append(Paragraph(
        "A curious person\u2019s guide to their own territory",
        tagline_style
    ))
    elements.append(Spacer(1, 24))
    elements.append(DividerLine())

    elements.append(NextPageTemplate("content"))
    elements.append(PageBreak())
    return elements


# ─────────────────────────────────────────────
# HOW THIS WORKS
# ─────────────────────────────────────────────

def _build_how_this_works():
    """Page 2: Warm instructions."""
    elements = []
    elements.append(Spacer(1, 20))
    elements.append(Paragraph("How this works", STYLES["h2"]))
    elements.append(Spacer(1, 12))

    paras = [
        "These questions are designed to make you think. "
        "Some will feel obvious. Some might make you "
        "squirm a little. Good. That squirm is information.",

        "Rate each statement honestly \u2014 not where you "
        "want to be, not where you think you should be. "
        "Where you actually are, right now.",
    ]
    for p in paras:
        elements.append(voice_paragraph(p))
        elements.append(Spacer(1, 4))

    elements.append(Spacer(1, 12))

    # Rating scale explanation
    scale_style = ParagraphStyle(
        "ScaleExplain", fontName=FONTS["heading"], fontSize=14, leading=24,
        textColor=C["text"], alignment=TA_LEFT, spaceAfter=4,
    )
    scale_items = [
        ("<b>1</b>  \u00b7  Barely ever",),
        ("<b>2</b>  \u00b7  Occasionally",),
        ("<b>3</b>  \u00b7  Sometimes",),
        ("<b>4</b>  \u00b7  Pretty often",),
        ("<b>5</b>  \u00b7  Almost always",),
    ]
    for item in scale_items:
        elements.append(Paragraph(item[0], scale_style))

    elements.append(Spacer(1, 16))

    closing = (
        "After each section: one more question. "
        "That one question changes how everything "
        "gets read. Don\u2019t skip it."
    )
    elements.append(voice_italic_paragraph(closing))

    elements.append(PageBreak())
    return elements


# ─────────────────────────────────────────────
# DOMAIN QUESTION PAGES
# ─────────────────────────────────────────────

def _build_rating_row(question_num, question_text):
    """Build a single question row with rating circles."""
    elements = []
    q_style = ParagraphStyle(
        "AssessQ", fontName=FONTS["body"], fontSize=10.5, leading=16,
        textColor=C["text"], alignment=TA_LEFT,
    )
    # Question with number
    q_text = f"<b>{question_num}.</b>  {question_text}"
    elements.append(Paragraph(q_text, q_style))
    elements.append(Spacer(1, 2))
    elements.append(RatingScale())
    elements.append(Spacer(1, 10))
    return elements


def _build_flag_question(flag_text):
    """Build a flag question with body response options."""
    elements = []
    elements.append(Spacer(1, 8))
    elements.append(SectionDivider())
    elements.append(Spacer(1, 8))

    flag_style = ParagraphStyle(
        "FlagQ", fontName=FONTS["heading_italic"], fontSize=11, leading=17,
        textColor=C["primary"], alignment=TA_LEFT, spaceAfter=6,
    )
    elements.append(Paragraph(flag_text, flag_style))

    option_style = ParagraphStyle(
        "FlagOption", fontName=FONTS["body"], fontSize=9.5, leading=15,
        textColor=C["text"], alignment=TA_LEFT, leftIndent=14,
    )
    for option in BODY_CHECK_OPTIONS:
        elements.append(Paragraph(f"\u25cb  {option}", option_style))
        elements.append(Spacer(1, 2))

    elements.append(Spacer(1, 8))
    return elements


def _build_domain_section(domain_name):
    """Build a complete domain section with all questions."""
    elements = []
    subtitle = DOMAIN_SUBTITLES.get(domain_name, "")

    # Domain header bar
    elements.append(DomainHeader(domain_name, subtitle=subtitle))
    elements.append(Spacer(1, 16))

    question_num = 1
    sub_dims = ASSESSMENT_QUESTIONS[domain_name]

    for sub_name, questions in sub_dims.items():
        # Sub-dimension header
        sub_color = DOMAIN_COLORS.get(domain_name, C["primary"])
        sub_h3 = ParagraphStyle(
            f"SubH3_{domain_name}_{sub_name}",
            fontName=FONTS["heading_italic"], fontSize=14, leading=20,
            textColor=sub_color, alignment=TA_LEFT, spaceAfter=8,
        )
        elements.append(Paragraph(sub_name, sub_h3))
        elements.append(Spacer(1, 4))

        # Questions
        for q_text in questions:
            elements.extend(_build_rating_row(question_num, q_text))
            question_num += 1

        # Flag question after each sub-section
        flag_text = FLAG_QUESTIONS[domain_name][sub_name]
        elements.extend(_build_flag_question(flag_text))

    # Body check at end of domain
    elements.append(Spacer(1, 12))
    elements.append(SectionDivider())
    elements.append(Spacer(1, 8))

    check_style = ParagraphStyle(
        f"BodyCheck_{domain_name}",
        fontName=FONTS["heading_italic"], fontSize=12, leading=18,
        textColor=C["accent"], alignment=TA_LEFT, spaceAfter=8,
    )
    elements.append(Paragraph(
        f"Body check \u2014 {domain_name}",
        check_style
    ))
    elements.append(Paragraph(
        BODY_CHECK_QUESTIONS[domain_name],
        STYLES["body"]
    ))
    elements.append(Spacer(1, 4))

    option_style = ParagraphStyle(
        "BodyCheckOpt", fontName=FONTS["body"], fontSize=10, leading=16,
        textColor=C["text"], alignment=TA_LEFT, leftIndent=14,
    )
    for option in BODY_CHECK_OPTIONS:
        elements.append(Paragraph(f"\u25cb  {option}", option_style))
        elements.append(Spacer(1, 2))

    elements.append(PageBreak())
    return elements


# ─────────────────────────────────────────────
# SHAME SOURCE LOCATOR
# ─────────────────────────────────────────────

def _build_shame_locator():
    """Build the Shame Source Locator section."""
    elements = []

    # Special warm header
    header_style = ParagraphStyle(
        "ShameHeader", fontName=FONTS["heading"], fontSize=22, leading=28,
        textColor=C["accent"], alignment=TA_LEFT, spaceAfter=12,
    )
    elements.append(Paragraph("The Shame Source Locator", header_style))
    elements.append(Spacer(1, 8))

    intro_paras = [
        "Last section. Worth sitting with.",

        "These are the places where shame doesn\u2019t "
        "announce itself \u2014 it just arrives faster "
        "than you can notice it.",

        "Somewhere in the body, right now, "
        "something may have already responded "
        "to the word \u201cshame\u201d before you even "
        "read the next sentence.",

        "That response is the beginning of the map.",
    ]
    for p in intro_paras:
        elements.append(voice_paragraph(p))
        elements.append(Spacer(1, 2))

    elements.append(Spacer(1, 12))

    # Instructions
    inst_style = ParagraphStyle(
        "ShameInst", fontName=FONTS["heading_italic"], fontSize=12, leading=18,
        textColor=C["primary"], alignment=TA_LEFT, spaceAfter=8,
    )
    elements.append(Paragraph(
        "For each source below, rate how much shame your body carries \u2014 "
        "not how much you think you should feel, but how much actually arrives.",
        inst_style
    ))
    elements.append(Spacer(1, 4))

    scale_style = ParagraphStyle(
        "ShameScale", fontName=FONTS["body"], fontSize=10, leading=16,
        textColor=C["subtext"], alignment=TA_LEFT, spaceAfter=8,
    )
    elements.append(Paragraph(
        "1 \u00b7 Almost none &nbsp;&nbsp; 2 \u00b7 A little &nbsp;&nbsp; "
        "3 \u00b7 Moderate &nbsp;&nbsp; 4 \u00b7 Significant &nbsp;&nbsp; "
        "5 \u00b7 Overwhelming",
        scale_style
    ))
    elements.append(Spacer(1, 8))

    # Shame sources with rating circles
    source_style = ParagraphStyle(
        "ShameSource", fontName=FONTS["body"], fontSize=11, leading=17,
        textColor=C["text"], alignment=TA_LEFT,
    )

    for i, source in enumerate(SHAME_SOURCES, 1):
        elements.append(Paragraph(f"<b>{i}.</b>  {source}", source_style))
        elements.append(Spacer(1, 2))
        elements.append(RatingScale())
        elements.append(Spacer(1, 10))

    elements.append(Spacer(1, 16))
    elements.append(SectionDivider())
    elements.append(Spacer(1, 12))

    # Closing body check
    elements.append(Paragraph(
        "After sitting with these shame sources, notice your body. "
        "What is it doing right now? Where is the sensation strongest?",
        STYLES["callout"]
    ))

    elements.append(PageBreak())
    return elements


# ─────────────────────────────────────────────
# CLOSING PAGE
# ─────────────────────────────────────────────

def _build_closing():
    """Final page: warm closing."""
    elements = []
    elements.append(Spacer(1, 40))

    elements.append(Paragraph("You\u2019re done.", STYLES["h2"]))
    elements.append(Spacer(1, 16))

    closing_paras = [
        "Take a breath. A real one \u2014 not performative, "
        "not strategic. Just a breath because you just looked "
        "at some territory that most people spend their whole "
        "lives carefully not looking at.",

        "Whatever you found in there \u2014 the high scores, "
        "the low ones, the places that made you squirm, "
        "the places that surprised you with how much they\u2019ve "
        "healed \u2014 all of it is information. None of it is verdict.",

        "This map doesn\u2019t tell you what\u2019s wrong with you. "
        "It shows you where you are. And where you are "
        "is the only place the work can begin.",

        "Your report will translate these numbers into something "
        "you can actually use \u2014 a shape, a story, a set of "
        "practices chosen specifically for your landscape.",

        "Until then: be gentle with yourself today. "
        "You just did something brave.",
    ]

    for p in closing_paras:
        elements.append(voice_paragraph(p))
        elements.append(Spacer(1, 4))

    elements.append(Spacer(1, 24))
    elements.append(DividerLine())
    elements.append(Spacer(1, 16))
    elements.append(voice_italic_paragraph(
        "Your body held all of that. Thank it."
    ))

    return elements


# ─────────────────────────────────────────────
# MAIN GENERATOR
# ─────────────────────────────────────────────

def generate_assessment(output_dir="documents"):
    """Generate the SPINE Self-Map Assessment PDF."""
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "spine_self_map_assessment.pdf")

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
    elements.extend(_build_how_this_works())

    # Five domain sections
    for domain_name in ["Sovereignty", "Power", "Identity", "Nourishment", "Embodiment"]:
        elements.extend(_build_domain_section(domain_name))

    # Shame Source Locator
    elements.extend(_build_shame_locator())

    # Closing
    elements.extend(_build_closing())

    doc.build(elements)
    print(f"  Generated: {output_path}")
    return output_path


if __name__ == "__main__":
    generate_assessment()
