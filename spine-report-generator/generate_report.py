"""
SPINE Framework — Pattern Recognition Report PDF Generator
Generates complete branded PDF reports per client.
New system: Sexual domain with 4 clusters, HDR mechanisms,
waypoint narratives, and aliveness-specific voice.
"""

import os
import sys
import argparse
from datetime import datetime, timedelta

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame,
    Paragraph, Spacer, Image, Table, TableStyle,
    PageBreak, KeepTogether, Flowable,
)
from reportlab.platypus.doctemplate import NextPageTemplate
from reportlab.graphics.shapes import Drawing, Rect, String, Line

from clients_data import (
    get_client, get_all_axes, get_all_cluster_scores,
    get_cluster_score, get_lowest_axes, get_highest_axes,
    get_anchor_axis, get_anchor_cluster, get_stage,
    CLUSTER_NAMES, CLUSTER_AXES, cluster_average,
    HEALING, PATTERN, RESOURCING,
    SPINE_DOMAIN_ORDER, SPINE_DOMAINS,
    get_all_spine_scores, get_spine_domain_axes,
    get_highest_spine_domain, get_lowest_spine_domain,
)
from chart_generator import generate_all_charts
from narrative_generator import (
    get_narrative, get_priority_stack, generate_active_edges,
    generate_aliveness_narrative, generate_waypoint_narratives,
    get_practices_for_report,
)
from style_system import (
    C, FONTS, STYLES, PAGE_W, PAGE_H, MARGIN, CONTENT_W,
    CoverBackground, DividerLine, ColorStripe, LeftBorderBox,
    ScoreBar, SectionDivider, make_header_footer,
)


# ─────────────────────────────────────────────
# CATEGORY MAPS
# ─────────────────────────────────────────────

CATEGORY_COLORS = {
    HEALING: C["healing"],
    PATTERN: C["pattern"],
    RESOURCING: C["resourcing"],
}

CATEGORY_LABELS = {
    HEALING: "Healing",
    PATTERN: "Pattern",
    RESOURCING: "Resourcing",
}


# ─────────────────────────────────────────────
# LOCAL STYLES
# ─────────────────────────────────────────────

_STYLES = {
    "title_white": ParagraphStyle(
        "RptTitleWhite", fontName=FONTS["heading"], fontSize=28, leading=34,
        textColor=C["white"], alignment=TA_LEFT, spaceAfter=6,
    ),
    "h1": ParagraphStyle(
        "RptH1", fontName=FONTS["heading"], fontSize=22, leading=28,
        textColor=C["primary"], alignment=TA_LEFT, spaceAfter=12, spaceBefore=6,
    ),
    "h2": ParagraphStyle(
        "RptH2", fontName=FONTS["heading"], fontSize=16, leading=22,
        textColor=C["primary"], alignment=TA_LEFT, spaceAfter=8, spaceBefore=4,
    ),
    "h3": ParagraphStyle(
        "RptH3", fontName=FONTS["heading_italic"], fontSize=13, leading=18,
        textColor=C["text"], alignment=TA_LEFT, spaceAfter=6,
    ),
    "body": ParagraphStyle(
        "RptBody", fontName=FONTS["body"], fontSize=11, leading=18.7,
        textColor=C["text"], alignment=TA_LEFT, spaceAfter=6,
    ),
    "body_small": ParagraphStyle(
        "RptBodySmall", fontName=FONTS["body"], fontSize=9, leading=14,
        textColor=C["text"], alignment=TA_LEFT, spaceAfter=4,
    ),
    "caption": ParagraphStyle(
        "RptCaption", fontName=FONTS["body_italic"], fontSize=8, leading=11,
        textColor=C["subtext"], alignment=TA_LEFT,
    ),
    "voice": ParagraphStyle(
        "RptVoice", fontName=FONTS["heading"], fontSize=12, leading=20,
        textColor=C["text"], alignment=TA_LEFT, spaceAfter=8,
    ),
    "voice_warm": ParagraphStyle(
        "RptVoiceWarm", fontName=FONTS["heading_italic"], fontSize=12, leading=20,
        textColor=C["accent"], alignment=TA_LEFT, spaceAfter=8,
    ),
    "subtitle": ParagraphStyle(
        "RptSubtitle", fontName=FONTS["body"], fontSize=14, leading=20,
        textColor=C["subtext"], alignment=TA_LEFT, spaceAfter=4,
    ),
}


# ─────────────────────────────────────────────
# CUSTOM FLOWABLES
# ─────────────────────────────────────────────

class QuoteBox(Flowable):
    """Pull quote with left border and soft shadow."""
    def __init__(self, text, border_color=None, bg_color=None, width=None):
        super().__init__()
        self.text = text
        self.border_color = border_color or C["primary"]
        self.bg_color = bg_color or C["page_bg"]
        self.box_width = width or CONTENT_W

    def wrap(self, availWidth, availHeight):
        self.box_width = min(self.box_width, availWidth)
        style = ParagraphStyle(
            "rptquote", fontName=FONTS["heading_italic"], fontSize=11,
            leading=18, textColor=C["text"]
        )
        p = Paragraph(self.text, style)
        w, h = p.wrap(self.box_width - 34, availHeight)
        self._para = p
        self._text_height = h
        return self.box_width, h + 24

    def draw(self):
        total_h = self._text_height + 24
        self.canv.saveState()
        self.canv.setFillColor(Color(0, 0, 0, alpha=0.04))
        self.canv.roundRect(2, -2, self.box_width, total_h, 4, fill=1, stroke=0)
        self.canv.setFillColor(self.bg_color)
        self.canv.roundRect(0, 0, self.box_width, total_h, 4, fill=1, stroke=0)
        self.canv.setFillColor(self.border_color)
        self.canv.rect(0, 0, 4, total_h, fill=1, stroke=0)
        self.canv.restoreState()
        self._para.drawOn(self.canv, 18, 12)


class SpecialNoteBox(Flowable):
    """Prominent box for therapy recommendations or couples notes."""
    def __init__(self, title, text, border_color=None, bg_color=None, width=None):
        super().__init__()
        self.note_title = title
        self.text = text
        self.border_color = border_color or C["healing"]
        self.bg_color = bg_color or C["light_blue_bg"]
        self.box_width = width or CONTENT_W

    def wrap(self, availWidth, availHeight):
        self.box_width = min(self.box_width, availWidth)
        title_style = ParagraphStyle(
            "rptnt", fontName=FONTS["heading"], fontSize=12,
            leading=16, textColor=C["text"]
        )
        body_style = ParagraphStyle(
            "rptnb", fontName=FONTS["body"], fontSize=10,
            leading=16, textColor=C["text"]
        )
        self._title_para = Paragraph(f"<b>{self.note_title}</b>", title_style)
        self._body_para = Paragraph(self.text, body_style)
        tw, th = self._title_para.wrap(self.box_width - 34, availHeight)
        bw, bh = self._body_para.wrap(self.box_width - 34, availHeight)
        self._title_h = th
        self._body_h = bh
        return self.box_width, th + bh + 34

    def draw(self):
        total_h = self._title_h + self._body_h + 34
        self.canv.saveState()
        self.canv.setFillColor(Color(0, 0, 0, alpha=0.04))
        self.canv.roundRect(2, -2, self.box_width, total_h, 6, fill=1, stroke=0)
        self.canv.setFillColor(self.bg_color)
        self.canv.roundRect(0, 0, self.box_width, total_h, 6, fill=1, stroke=0)
        self.canv.setFillColor(self.border_color)
        self.canv.rect(0, 0, 4, total_h, fill=1, stroke=0)
        self.canv.restoreState()
        self._title_para.drawOn(self.canv, 18, total_h - self._title_h - 12)
        self._body_para.drawOn(self.canv, 18, 12)


# ─────────────────────────────────────────────
# PAGE CALLBACKS
# ─────────────────────────────────────────────

def _cover_page(canvas, doc):
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
    make_header_footer(canvas, doc, section_name="Pattern Recognition Report")


# ─────────────────────────────────────────────
# PAGE BUILDERS
# ─────────────────────────────────────────────

def _page_cover(client_data, report_date, reassess_date):
    """Cover page."""
    elements = []
    elements.append(Spacer(1, 80))
    elements.append(Paragraph(client_data["name"], _STYLES["title_white"]))
    elements.append(Spacer(1, 8))

    cover_sub = ParagraphStyle(
        "CoverSub2", fontName=FONTS["heading"], fontSize=22, leading=28,
        textColor=C["page_bg"], alignment=TA_LEFT,
    )
    elements.append(Paragraph("Your Pattern Recognition Report", cover_sub))
    elements.append(Spacer(1, 16))
    elements.append(DividerLine())
    elements.append(Spacer(1, 16))

    date_style = ParagraphStyle(
        "CoverDate", fontName=FONTS["body"], fontSize=11, leading=16,
        textColor=Color(0.9, 0.88, 0.85), alignment=TA_LEFT,
    )
    elements.append(Paragraph(f"Assessment Date: {report_date}", date_style))
    elements.append(Paragraph(f"Reassessment Date: {reassess_date}", date_style))
    elements.append(Spacer(1, 30))

    spine_img = os.path.join(
        os.path.dirname(__file__), "assets", "images", "spine_illustration.png"
    )
    if os.path.exists(spine_img):
        elements.append(Image(spine_img, width=140, height=245))
    elements.append(Spacer(1, 30))

    tagline = ParagraphStyle(
        "CoverTag", fontName=FONTS["heading_italic"], fontSize=13,
        leading=20, textColor=C["page_bg"], alignment=TA_CENTER,
    )
    elements.append(Paragraph(
        "Growing the spine that was never allowed to form.", tagline
    ))
    elements.append(Spacer(1, 20))
    elements.append(DividerLine())
    elements.append(NextPageTemplate("content"))
    elements.append(PageBreak())
    return elements


def _page_mechanism(client_data):
    """What Was Done To You — HDR mechanism section."""
    from hdr_mechanisms import get_mechanism_report_section

    elements = []
    elements.append(Paragraph("What Was Done To You", _STYLES["h1"]))
    elements.append(Spacer(1, 8))

    report = get_mechanism_report_section(client_data)

    for mech in report["mechanisms"]:
        elements.append(Paragraph(
            f"<b>{mech['name']}</b>",
            _STYLES["h3"]
        ))
        # Split narrative into paragraphs for better formatting
        for para in mech["narrative"].split("\n\n"):
            if para.strip():
                elements.append(Paragraph(para.strip(), _STYLES["voice"]))
        elements.append(Spacer(1, 8))

    # Closing
    elements.append(Spacer(1, 8))
    elements.append(QuoteBox(report["closing"], C["accent"]))
    elements.append(PageBreak())
    return elements


def _page_spine_overview(client_data, chart_paths):
    """SPINE Overview — master 5-domain spider chart + domain table."""
    elements = []
    elements.append(Paragraph("Your SPINE", _STYLES["h1"]))
    elements.append(Spacer(1, 8))

    spine_scores = get_all_spine_scores(client_data)
    highest_domain, highest_score = get_highest_spine_domain(client_data)
    lowest_domain, lowest_score = get_lowest_spine_domain(client_data)

    intro = (
        f"Your SPINE reveals {highest_domain} at {highest_score}% as your "
        f"strongest vertebra and {lowest_domain} at {lowest_score}% as the "
        f"vertebra asking for the most attention. This is your starting "
        f"point, not your destination."
    )
    elements.append(Paragraph(intro, _STYLES["body"]))
    elements.append(Spacer(1, 12))

    # SPINE master spider chart
    spine_path = chart_paths.get("spine")
    if spine_path and os.path.exists(spine_path):
        elements.append(Image(spine_path, width=CONTENT_W, height=CONTENT_W * 0.85))
    elements.append(Spacer(1, 12))

    # SPINE domain summary table
    table_data = [["Vertebra", "Score", "Stage", "Description"]]
    for domain_name in SPINE_DOMAIN_ORDER:
        score = spine_scores[domain_name]
        stage = get_stage(score)
        letter = SPINE_DOMAINS[domain_name]["letter"]
        desc = SPINE_DOMAINS[domain_name]["description"]
        # Truncate description for table
        short_desc = desc[:80] + "..." if len(desc) > 80 else desc
        table_data.append([
            f"{letter} — {domain_name}", f"{score}%", stage, short_desc
        ])

    col_widths = [110, 50, 100, 180]
    t = Table(table_data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, 0), FONTS["heading"]),
        ("FONTSIZE", (0, 0), (-1, 0), 10),
        ("FONTNAME", (0, 1), (-1, -1), FONTS["body"]),
        ("FONTSIZE", (0, 1), (-1, -1), 8),
        ("TEXTCOLOR", (0, 0), (-1, -1), C["text"]),
        ("ALIGN", (1, 0), (2, -1), "CENTER"),
        ("ALIGN", (0, 0), (0, -1), "LEFT"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("LINEBELOW", (0, 0), (-1, 0), 1, C["divider"]),
        ("LINEBELOW", (0, -1), (-1, -1), 1, C["divider"]),
    ]))
    elements.append(t)
    elements.append(PageBreak())
    return elements


def _page_spine_domain_detail(client_data, chart_paths):
    """SPINE domain detail pages with per-domain spider charts."""
    elements = []
    elements.append(Paragraph("SPINE Domain Detail", _STYLES["h1"]))
    elements.append(Spacer(1, 8))

    domain_colors = {
        "Sovereignty": C.get("sovereignty", C["secondary"]),
        "Power": C.get("power", C["primary"]),
        "Identity": C.get("identity", C["accent"]),
        "Nourishment": C.get("nourishment", C["primary"]),
        "Embodiment": C.get("embodiment", C["primary"]),
    }

    for domain_name in SPINE_DOMAIN_ORDER:
        domain_info = SPINE_DOMAINS[domain_name]
        axes = get_spine_domain_axes(client_data, domain_name)
        avg = round(sum(axes.values()) / len(axes)) if axes else 0
        stage = get_stage(avg)

        # Domain header
        elements.append(Paragraph(
            f"<b>{domain_info['letter']} — {domain_name}</b> — {avg}% ({stage})",
            _STYLES["h2"]
        ))
        elements.append(Paragraph(domain_info["description"], _STYLES["body_small"]))
        elements.append(Spacer(1, 4))

        # Domain spider chart
        chart_key = f"spine_{domain_name.lower()}"
        chart_path = chart_paths.get(chart_key)
        if chart_path and os.path.exists(chart_path):
            elements.append(Image(chart_path, width=CONTENT_W * 0.5,
                                  height=CONTENT_W * 0.5))

        # Axis scores with vision gaps
        vision = client_data.get("vision", {})
        all_vision = {}
        for v in vision.values():
            all_vision.update(v)

        for axis_name, score in axes.items():
            vis = all_vision.get(axis_name, score)
            gap = vis - score
            elements.append(Paragraph(
                f"{axis_name}: {score}% → {vis}% (gap: {gap})",
                _STYLES["body_small"]
            ))

        elements.append(Spacer(1, 10))
        elements.append(SectionDivider())
        elements.append(Spacer(1, 8))

    elements.append(PageBreak())
    return elements


def _page_overview(client_data, chart_paths):
    """Map Overview with meta spider and cluster table."""
    elements = []
    elements.append(Paragraph("Your Map", _STYLES["h1"]))
    elements.append(Spacer(1, 8))

    cluster_scores = get_all_cluster_scores(client_data)
    anchor_num, anchor_name, anchor_score = get_anchor_cluster(client_data)

    intro = (
        f"Your map reveals a unique shape — {anchor_name} at "
        f"{anchor_score}% as your strongest cluster and "
    )
    lowest_num = min(cluster_scores, key=cluster_scores.get)
    lowest_name = CLUSTER_NAMES[lowest_num]
    lowest_score = cluster_scores[lowest_num]
    intro += (
        f"{lowest_name} at {lowest_score}% as the cluster asking for "
        f"the most attention. This is your starting point, not your destination."
    )
    elements.append(Paragraph(intro, _STYLES["body"]))
    elements.append(Spacer(1, 12))

    # Meta spider chart
    meta_path = chart_paths.get("meta")
    if meta_path and os.path.exists(meta_path):
        elements.append(Image(meta_path, width=CONTENT_W, height=CONTENT_W * 0.85))
    elements.append(Spacer(1, 12))

    # Cluster summary table
    table_data = [["Cluster", "Score", "Stage", "Lowest Axis"]]
    for c in range(1, 5):
        cname = CLUSTER_NAMES[c]
        score = cluster_scores[c]
        stage = get_stage(score)
        axes = client_data["clusters"][c]["axes"]
        lowest_axis = min(axes, key=axes.get)
        lowest_val = axes[lowest_axis]
        table_data.append([
            cname, f"{score}%", stage,
            f"{lowest_axis} ({lowest_val}%)"
        ])

    col_widths = [80, 60, 100, 200]
    t = Table(table_data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, 0), FONTS["heading"]),
        ("FONTSIZE", (0, 0), (-1, 0), 10),
        ("FONTNAME", (0, 1), (-1, -1), FONTS["body"]),
        ("FONTSIZE", (0, 1), (-1, -1), 9),
        ("TEXTCOLOR", (0, 0), (-1, -1), C["text"]),
        ("ALIGN", (1, 0), (2, -1), "CENTER"),
        ("ALIGN", (0, 0), (0, -1), "LEFT"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("LINEBELOW", (0, 0), (-1, 0), 1, C["divider"]),
        ("LINEBELOW", (0, -1), (-1, -1), 1, C["divider"]),
    ]))
    elements.append(t)
    elements.append(PageBreak())
    return elements


def _page_reading(client_data, narrative):
    """Reading Your Shape — map narrative + anchor."""
    elements = []
    elements.append(Paragraph("Reading Your Shape", _STYLES["h1"]))
    elements.append(Paragraph("What your map is telling you", _STYLES["subtitle"]))
    elements.append(Spacer(1, 12))

    # Split narrative into paragraphs
    reading = narrative.get("reading_your_shape", "")
    for para in reading.split("\n\n"):
        if para.strip():
            elements.append(Paragraph(para.strip(), _STYLES["voice"]))

    elements.append(Spacer(1, 12))

    # Central tension quote
    elements.append(QuoteBox(client_data["central_tension"], C["primary"]))
    elements.append(Spacer(1, 12))

    # Special note
    if client_data.get("special_note"):
        note = client_data["special_note"]
        border = C["healing"] if note["type"] == "therapy_recommendation" else C["accent"]
        bg = C["light_blue_bg"] if note["type"] == "therapy_recommendation" else C["page_bg"]
        elements.append(SpecialNoteBox(note["title"], note["text"], border, bg))
        elements.append(Spacer(1, 12))

    # Anchor acknowledgment
    anchor_text = narrative.get("anchor_acknowledgment", "")
    anchor_name, anchor_score = get_anchor_axis(client_data)
    elements.append(QuoteBox(
        f"<b>Your anchor: {anchor_name} ({anchor_score}%)</b><br/><br/>"
        + anchor_text,
        C["anchor"] if "anchor" in C else C["secondary"],
    ))

    elements.append(PageBreak())
    return elements


def _page_active_edges(client_data):
    """Active Edges + Aliveness section."""
    elements = []
    elements.append(Paragraph("Your Active Edges", _STYLES["h1"]))
    elements.append(Spacer(1, 8))

    edges = generate_active_edges(client_data, 3)
    for edge in edges:
        elements.append(Paragraph(
            f"<b>{edge['axis']}</b> — {edge['score']}% "
            f"({edge['stage']})",
            _STYLES["h3"]
        ))
        elements.append(Paragraph(edge["invitation"], _STYLES["voice"]))
        elements.append(Spacer(1, 8))

    # Aliveness section
    elements.append(Spacer(1, 12))
    elements.append(DividerLine())
    elements.append(Spacer(1, 12))
    elements.append(Paragraph("Aliveness & Play", _STYLES["h2"]))

    aliveness_text = generate_aliveness_narrative(client_data)
    for para in aliveness_text.split("\n\n"):
        if para.strip():
            elements.append(Paragraph(para.strip(), _STYLES["voice_warm"]))

    elements.append(PageBreak())
    return elements


def _page_cluster_detail(client_data, chart_paths):
    """Cluster detail with spider charts."""
    elements = []
    elements.append(Paragraph("Cluster Detail", _STYLES["h1"]))
    elements.append(Spacer(1, 8))

    for c in range(1, 5):
        cluster_data = client_data["clusters"][c]
        cname = CLUSTER_NAMES[c]
        axes = cluster_data["axes"]
        avg = cluster_average(axes)
        stage = get_stage(avg)
        body_check = cluster_data.get("body_check", "")

        # Cluster header
        elements.append(Paragraph(
            f"<b>Cluster {c}: {cname}</b> — {avg}% ({stage})",
            _STYLES["h2"]
        ))

        # Chart
        chart_key = f"cluster_{c}"
        chart_path = chart_paths.get(chart_key)
        if chart_path and os.path.exists(chart_path):
            elements.append(Image(chart_path, width=CONTENT_W * 0.6,
                                  height=CONTENT_W * 0.6))

        # Axis scores
        vision_data = client_data.get("vision", {}).get(c, {})
        for axis_name, score in axes.items():
            vis = vision_data.get(axis_name, score)
            gap = vis - score
            elements.append(Paragraph(
                f"{axis_name}: {score}% → {vis}% (gap: {gap})",
                _STYLES["body_small"]
            ))

        elements.append(Paragraph(
            f"Body check: {body_check}", _STYLES["caption"]
        ))
        elements.append(Spacer(1, 12))
        elements.append(SectionDivider())
        elements.append(Spacer(1, 8))

    elements.append(PageBreak())
    return elements


def _page_hdr_pendulum(client_data, chart_paths):
    """HDR Mechanism Radar + Pendulum Risk Gauge."""
    elements = []

    # HDR Radar
    elements.append(Paragraph("Your Wound Architecture", _STYLES["h1"]))
    elements.append(Spacer(1, 8))

    hdr_path = chart_paths.get("hdr_radar")
    if hdr_path and os.path.exists(hdr_path):
        elements.append(Image(hdr_path, width=CONTENT_W * 0.7,
                              height=CONTENT_W * 0.7))
    elements.append(Spacer(1, 12))

    # Pendulum Risk
    elements.append(Paragraph("Pendulum Risk", _STYLES["h2"]))
    pendulum_path = chart_paths.get("pendulum")
    if pendulum_path and os.path.exists(pendulum_path):
        elements.append(Image(pendulum_path, width=CONTENT_W * 0.6,
                              height=CONTENT_W * 0.3))
    elements.append(Spacer(1, 8))

    from scoring_tools import pendulum_risk
    risk = pendulum_risk(client_data)
    elements.append(Paragraph(risk["risk_note"], _STYLES["body"]))

    elements.append(PageBreak())
    return elements


def _page_waypoints(client_data):
    """Waypoint narratives for primary axes."""
    elements = []
    elements.append(Paragraph("Your First Milestones", _STYLES["h1"]))
    elements.append(Paragraph(
        "What the next shifts will feel like", _STYLES["subtitle"]
    ))
    elements.append(Spacer(1, 12))

    waypoint_narrs = generate_waypoint_narratives(client_data)
    for wp in waypoint_narrs:
        elements.append(Paragraph(
            f"<b>{wp['axis']}</b> — toward {wp['next_milestone']} "
            f"({wp['next_threshold']}%)",
            _STYLES["h3"]
        ))
        elements.append(Paragraph(wp["narrative"], _STYLES["voice"]))
        elements.append(Spacer(1, 10))

    elements.append(PageBreak())
    return elements


def _page_practices(client_data, narrative):
    """Practice prescription."""
    elements = []
    elements.append(Paragraph("Your Practice Prescription", _STYLES["h1"]))
    elements.append(Spacer(1, 12))

    practices = get_practices_for_report(client_data)

    for practice in practices:
        cat = practice.get("category", "")
        cat_color = CATEGORY_COLORS.get(cat, C["primary"])
        cat_label = CATEGORY_LABELS.get(cat, "")

        title_text = (
            f"<b>{practice['name']}</b> &nbsp; "
            f"<font size='9' color='#{cat_color.hexval()[2:]}'>"
            f"{cat_label}</font>"
            f" &nbsp; <font size='9' color='#6B6B6B'>"
            f"Weeks {practice['weeks']}</font>"
        )

        card_content = []
        card_content.append([Paragraph(title_text, _STYLES["h3"])])

        # Client text (truncated for report — first two paragraphs)
        client_text = practice.get("client_text", "")
        paras = client_text.split("\n\n")
        display_text = "\n\n".join(paras[:2]) if len(paras) > 2 else client_text
        card_content.append([Paragraph(display_text, _STYLES["body_small"])])

        if practice.get("why_for_you"):
            card_content.append([Paragraph(
                f"<b>Why this for you:</b> {practice['why_for_you']}",
                _STYLES["body_small"]
            )])

        card_content.append([Paragraph(
            f"<b>What you'll notice:</b> {practice['what_youll_notice']}",
            _STYLES["body_small"]
        )])

        card_w = CONTENT_W
        card = Table(card_content, colWidths=[card_w - 14])
        card.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), C["white"]),
            ("BOX", (0, 0), (-1, -1), 0.5, C["divider"]),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ("LEFTPADDING", (0, 0), (-1, -1), 12),
            ("RIGHTPADDING", (0, 0), (-1, -1), 12),
            ("LINEABOVE", (0, 0), (-1, 0), 3, cat_color),
        ]))
        elements.append(card)
        elements.append(Spacer(1, 14))

    # Closing
    elements.append(Spacer(1, 12))
    elements.append(DividerLine())
    elements.append(Spacer(1, 12))

    closing = narrative.get("closing", "")
    for para in closing.split("\n\n"):
        if para.strip():
            elements.append(Paragraph(para.strip(), _STYLES["voice"]))

    elements.append(Spacer(1, 16))
    elements.append(Paragraph(
        "A reassessment is recommended at 10 weeks to track movement, "
        "celebrate progress, and adjust your practice prescription.",
        _STYLES["caption"]
    ))

    return elements


# ─────────────────────────────────────────────
# MAIN GENERATOR
# ─────────────────────────────────────────────

def generate_report(client_data, output_dir="reports"):
    """Generate complete Pattern Recognition Report PDF."""
    os.makedirs(output_dir, exist_ok=True)
    name = client_data["name"].lower()
    output_path = os.path.join(output_dir, f"{name}_spine_report.pdf")

    # Dates
    now = datetime.now()
    report_date = now.strftime("%B %d, %Y")
    reassess_date = (now + timedelta(weeks=10)).strftime("%B %d, %Y")

    # Generate charts
    chart_dir = os.path.join(output_dir, f"{name}_charts")
    chart_paths = generate_all_charts(client_data, chart_dir)

    # Get narratives
    narrative = get_narrative(client_data)

    # Build PDF
    cover_frame = Frame(MARGIN, MARGIN, CONTENT_W, PAGE_H - 2 * MARGIN, id="cover")
    content_frame = Frame(
        MARGIN, MARGIN + 20, CONTENT_W, PAGE_H - 2 * MARGIN - 40, id="content"
    )

    doc = BaseDocTemplate(
        output_path, pagesize=letter,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN, bottomMargin=MARGIN,
    )

    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[cover_frame], onPage=_cover_page),
        PageTemplate(id="content", frames=[content_frame], onPage=_content_page),
    ])

    elements = []

    # Build pages — SPINE overview leads, then narrative, then detail
    elements.extend(_page_cover(client_data, report_date, reassess_date))
    elements.extend(_page_spine_overview(client_data, chart_paths))
    elements.extend(_page_reading(client_data, narrative))
    elements.extend(_page_mechanism(client_data))
    elements.extend(_page_spine_domain_detail(client_data, chart_paths))
    elements.extend(_page_active_edges(client_data))
    elements.extend(_page_hdr_pendulum(client_data, chart_paths))
    elements.extend(_page_waypoints(client_data))
    elements.extend(_page_practices(client_data, narrative))

    doc.build(elements)
    print(f"  Generated: {output_path}")
    return output_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate SPINE report")
    parser.add_argument(
        "--client", type=str, required=True,
        help="Client name (sarah, marcus, elena, diane)"
    )
    args = parser.parse_args()

    client = get_client(args.client)
    generate_report(client)
