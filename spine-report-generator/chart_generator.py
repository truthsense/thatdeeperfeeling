"""
SPINE Framework — Chart Generator (New Architecture)
8 chart types for the 4-cluster Sexual Domain model:
  1. Cluster Meta Spider (4-axis)
  2. Cluster Detail Spiders (5-axis each, ×4)
  3. Gap Visualization
  4. Waypoint Milestone Map
  5. Couples Overlay
  6. Restaurant Safety Profile
  7. HDR Mechanism Radar
  8. Pendulum Risk Gauge
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Wedge
from matplotlib.collections import PatchCollection
import matplotlib.patheffects as pe

from clients_data import (
    CLUSTER_NAMES, CLUSTER_AXES,
    SPINE_DOMAIN_ORDER, SPINE_DOMAINS,
    get_all_axes, get_all_vision, get_all_cluster_scores,
    get_all_spine_scores, get_spine_vision_scores,
    get_spine_domain_axes,
    get_cluster_score, cluster_average, get_stage,
)


# ─────────────────────────────────────────────
# BRAND COLORS
# ─────────────────────────────────────────────

COLORS = {
    "primary": "#8B6F7E",
    "secondary": "#4A7C6F",
    "accent": "#C4956A",
    "background": "#F9F5F2",
    "text": "#2C2C2C",
    "subtext": "#6B6B6B",
    "grid": "#E0D5CE",
    "healing": "#7B9BC4",
    "pattern": "#C4B47A",
    "resourcing": "#7BBF8E",
    "anchor": "#3D5A80",
    "cluster_1": "#8B6F7E",
    "cluster_2": "#4A7C6F",
    "cluster_3": "#C4956A",
    "cluster_4": "#7B9BC4",
    "vision": "#B8A9C9",
    "risk_low": "#7BBF8E",
    "risk_moderate": "#C4B47A",
    "risk_high": "#C47B7B",
    "white": "#FFFFFF",
}

CLUSTER_COLORS = {
    1: COLORS["cluster_1"],
    2: COLORS["cluster_2"],
    3: COLORS["cluster_3"],
    4: COLORS["cluster_4"],
}

SPINE_COLORS = {
    "Sovereignty": "#8B3A47",
    "Power": "#4A7C6F",
    "Identity": "#C4956A",
    "Nourishment": "#7BBF8E",
    "Embodiment": "#7B9BC4",
}


# ─────────────────────────────────────────────
# SHARED HELPERS
# ─────────────────────────────────────────────

def _setup_figure(figsize=(8, 8)):
    """Create a figure with brand background."""
    fig = plt.figure(figsize=figsize, facecolor=COLORS["background"])
    return fig


def _save_chart(fig, path):
    """Save chart and close figure."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fig.savefig(path, dpi=150, bbox_inches="tight",
                facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close(fig)


def _radar_chart(ax, labels, values, color, fill_alpha=0.15,
                 vision_values=None, title=None):
    """Draw a radar/spider chart on the given axes."""
    n = len(labels)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    values_plot = values + [values[0]]
    angles_plot = angles + [angles[0]]

    # Grid
    for ring in [20, 40, 60, 80, 100]:
        ring_vals = [ring] * (n + 1)
        ax.plot(angles_plot, ring_vals, color=COLORS["grid"],
                linewidth=0.5, linestyle="-", alpha=0.6)

    # Spokes
    for angle in angles:
        ax.plot([angle, angle], [0, 100], color=COLORS["grid"],
                linewidth=0.5, alpha=0.4)

    # Vision overlay
    if vision_values:
        vision_plot = vision_values + [vision_values[0]]
        ax.plot(angles_plot, vision_plot, color=COLORS["vision"],
                linewidth=1.5, linestyle="--", alpha=0.6)
        ax.fill(angles_plot, vision_plot, color=COLORS["vision"],
                alpha=0.05)

    # Main data
    ax.plot(angles_plot, values_plot, color=color, linewidth=2.5,
            path_effects=[pe.withStroke(linewidth=4, foreground=COLORS["background"])])
    ax.fill(angles_plot, values_plot, color=color, alpha=fill_alpha)

    # Data points
    ax.scatter(angles, values, color=color, s=40, zorder=5,
               edgecolors=COLORS["background"], linewidths=1.5)

    # Labels
    for i, (angle, label, value) in enumerate(zip(angles, labels, values)):
        ha = "center"
        if angle > 0 and angle < np.pi:
            ha = "left"
        elif angle > np.pi:
            ha = "right"

        # Wrap long labels
        if len(label) > 18:
            parts = label.split(" ")
            mid = len(parts) // 2
            label = " ".join(parts[:mid]) + "\n" + " ".join(parts[mid:])

        ax.text(angle, 115, f"{label}\n{value}%",
                ha=ha, va="center", fontsize=7.5,
                color=COLORS["text"], fontweight="bold")

    ax.set_ylim(0, 120)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["polar"].set_visible(False)

    if title:
        ax.set_title(title, fontsize=13, fontweight="bold",
                     color=COLORS["text"], pad=20)


# ─────────────────────────────────────────────
# SPINE MASTER SPIDER (Primary Chart)
# ─────────────────────────────────────────────

def generate_spine_spider(client_data, output_path):
    """5-axis SPINE domain spider — the master chart of every report."""
    fig = _setup_figure((9, 9))
    ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor(COLORS["background"])

    scores = get_all_spine_scores(client_data)
    vision = get_spine_vision_scores(client_data)

    labels = []
    values = []
    vision_values = []
    for domain in SPINE_DOMAIN_ORDER:
        letter = SPINE_DOMAINS[domain]["letter"]
        labels.append(f"{letter} — {domain}")
        values.append(scores[domain])
        vision_values.append(vision[domain])

    _radar_chart(ax, labels, values, COLORS["primary"],
                 vision_values=vision_values,
                 title=f"{client_data['name']} — SPINE Overview")

    # Center overall score
    overall = round(sum(values) / len(values))
    ax.text(0, 0, f"{overall}%", ha="center", va="center",
            fontsize=24, fontweight="bold", color=COLORS["primary"])

    _save_chart(fig, output_path)
    return output_path


def generate_spine_domain_spider(client_data, domain_name, output_path):
    """Spider chart for axes within a single SPINE domain."""
    fig = _setup_figure((7, 7))
    ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor(COLORS["background"])

    domain_axes = get_spine_domain_axes(client_data, domain_name)
    axes_names = list(domain_axes.keys())
    values = list(domain_axes.values())

    # Vision values
    all_vision = get_all_vision(client_data)
    vision_vals = [all_vision.get(a, v) for a, v in zip(axes_names, values)]

    color = SPINE_COLORS.get(domain_name, COLORS["primary"])
    avg = round(sum(values) / len(values)) if values else 0
    stage = get_stage(avg)
    letter = SPINE_DOMAINS[domain_name]["letter"]
    title = f"{letter} — {domain_name}: {avg}% ({stage})"

    _radar_chart(ax, axes_names, values, color,
                 vision_values=vision_vals, title=title)

    _save_chart(fig, output_path)
    return output_path


# ─────────────────────────────────────────────
# 1. CLUSTER META SPIDER (Secondary View)
# ─────────────────────────────────────────────

def generate_meta_spider(client_data, output_path):
    """4-axis spider showing cluster averages (secondary to SPINE)."""
    fig = _setup_figure((8, 8))
    ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor(COLORS["background"])

    scores = get_all_cluster_scores(client_data)
    labels = [f"C{n}: {CLUSTER_NAMES[n]}" for n in range(1, 5)]
    values = [scores[n] for n in range(1, 5)]

    _radar_chart(ax, labels, values, COLORS["primary"],
                 title=f"{client_data['name']} — Domain Overview")

    # Center score
    domain_avg = round(sum(values) / len(values))
    ax.text(0, 0, f"{domain_avg}%", ha="center", va="center",
            fontsize=24, fontweight="bold", color=COLORS["primary"])

    _save_chart(fig, output_path)
    return output_path


# ─────────────────────────────────────────────
# 2. CLUSTER DETAIL SPIDERS
# ─────────────────────────────────────────────

def generate_cluster_spider(client_data, cluster_num, output_path):
    """5-axis spider for a single cluster with vision overlay."""
    fig = _setup_figure((7, 7))
    ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor(COLORS["background"])

    cluster = client_data["clusters"][cluster_num]
    axes_names = CLUSTER_AXES[cluster_num]
    values = [cluster["axes"].get(a, 0) for a in axes_names]

    # Vision values
    vision_data = client_data.get("vision", {}).get(cluster_num, {})
    vision_values = [vision_data.get(a, v) for a, v in zip(axes_names, values)]

    color = CLUSTER_COLORS.get(cluster_num, COLORS["primary"])
    avg = cluster_average(cluster["axes"])
    stage = get_stage(avg)
    title = (
        f"Cluster {cluster_num}: {CLUSTER_NAMES[cluster_num]} "
        f"— {avg}% ({stage})"
    )

    _radar_chart(ax, axes_names, values, color,
                 vision_values=vision_values, title=title)

    _save_chart(fig, output_path)
    return output_path


# ─────────────────────────────────────────────
# 3. GAP VISUALIZATION
# ─────────────────────────────────────────────

def generate_gap_chart(client_data, output_path):
    """Horizontal bar chart showing current vs vision for each axis."""
    fig = _setup_figure((10, 12))
    ax = fig.add_subplot(111)
    ax.set_facecolor(COLORS["background"])

    all_axes = get_all_axes(client_data)
    all_vision = get_all_vision(client_data)

    # Sort by gap size
    gaps = []
    for axis_name, score in all_axes.items():
        vision = all_vision.get(axis_name, score)
        gaps.append((axis_name, score, vision, vision - score))
    gaps.sort(key=lambda x: x[3], reverse=True)

    y_pos = np.arange(len(gaps))
    names = [g[0] for g in gaps]
    current = [g[1] for g in gaps]
    vision = [g[2] for g in gaps]
    gap_vals = [g[3] for g in gaps]

    # Current bars
    ax.barh(y_pos, current, height=0.4, color=COLORS["primary"],
            alpha=0.7, label="Current")
    # Vision bars
    ax.barh(y_pos, vision, height=0.4, color=COLORS["vision"],
            alpha=0.3, label="Vision")

    # Gap labels
    for i, (name, curr, vis, gap) in enumerate(gaps):
        if gap > 0:
            ax.text(vis + 1, i, f"+{gap}", va="center",
                    fontsize=8, color=COLORS["accent"], fontweight="bold")

    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=8)
    ax.set_xlabel("Score (%)", fontsize=10)
    ax.set_xlim(0, 105)
    ax.set_title(f"{client_data['name']} — Gap Analysis",
                 fontsize=14, fontweight="bold", color=COLORS["text"])
    ax.legend(loc="lower right", fontsize=9)
    ax.invert_yaxis()

    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(left=False)
    ax.grid(axis="x", alpha=0.3, color=COLORS["grid"])

    _save_chart(fig, output_path)
    return output_path


# ─────────────────────────────────────────────
# 4. WAYPOINT MILESTONE MAP
# ─────────────────────────────────────────────

def generate_waypoint_map(client_data, output_path):
    """Visual map of waypoint milestones for all 20 axes."""
    from waypoints import WAYPOINTS

    fig = _setup_figure((12, 10))
    ax = fig.add_subplot(111)
    ax.set_facecolor(COLORS["background"])

    axes = get_all_axes(client_data)
    y = 0
    y_labels = []
    y_positions = []

    for cluster_num in range(1, 5):
        cluster_axes = CLUSTER_AXES[cluster_num]
        color = CLUSTER_COLORS[cluster_num]

        for axis_name in cluster_axes:
            score = axes.get(axis_name, 0)
            wp = WAYPOINTS.get(axis_name)
            if not wp:
                continue

            y_labels.append(axis_name)
            y_positions.append(y)

            # Draw milestone markers
            for milestone in wp["milestones"]:
                threshold = milestone["threshold"]
                reached = score >= threshold
                marker_color = color if reached else COLORS["grid"]
                marker_size = 80 if reached else 40
                marker = "o" if reached else "D"

                ax.scatter(threshold, y, s=marker_size, color=marker_color,
                           marker=marker, zorder=5,
                           edgecolors=COLORS["text"] if reached else COLORS["grid"],
                           linewidths=1)

            # Draw current position
            ax.scatter(score, y, s=120, color=color, marker="s",
                       zorder=6, edgecolors=COLORS["text"], linewidths=1.5)

            # Draw progress line
            ax.plot([0, score], [y, y], color=color, linewidth=2, alpha=0.6)
            ax.plot([score, 100], [y, y], color=COLORS["grid"],
                    linewidth=1, alpha=0.3)

            y -= 1

        # Cluster separator
        if cluster_num < 4:
            ax.axhline(y=y + 0.5, color=COLORS["grid"], linewidth=0.5,
                       linestyle="--", alpha=0.5)
            y -= 0.5

    ax.set_yticks(y_positions)
    ax.set_yticklabels(y_labels, fontsize=7.5)
    ax.set_xlim(-5, 105)
    ax.set_xlabel("Score (%)", fontsize=10)
    ax.set_title(f"{client_data['name']} — Waypoint Map",
                 fontsize=14, fontweight="bold", color=COLORS["text"])

    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(left=False)
    ax.grid(axis="x", alpha=0.2, color=COLORS["grid"])

    # Legend
    legend_elements = [
        plt.Line2D([0], [0], marker="s", color="w",
                   markerfacecolor=COLORS["primary"], markersize=10,
                   label="Current Score"),
        plt.Line2D([0], [0], marker="o", color="w",
                   markerfacecolor=COLORS["secondary"], markersize=8,
                   label="Milestone Reached"),
        plt.Line2D([0], [0], marker="D", color="w",
                   markerfacecolor=COLORS["grid"], markersize=6,
                   label="Milestone Ahead"),
    ]
    ax.legend(handles=legend_elements, loc="lower right", fontsize=8)

    _save_chart(fig, output_path)
    return output_path


# ─────────────────────────────────────────────
# 5. COUPLES OVERLAY
# ─────────────────────────────────────────────

def generate_couples_overlay(client_a, client_b, output_path):
    """Meta spider overlay showing both partners' cluster scores."""
    fig = _setup_figure((9, 9))
    ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor(COLORS["background"])

    scores_a = get_all_cluster_scores(client_a)
    scores_b = get_all_cluster_scores(client_b)

    labels = [f"C{n}: {CLUSTER_NAMES[n]}" for n in range(1, 5)]
    values_a = [scores_a[n] for n in range(1, 5)]
    values_b = [scores_b[n] for n in range(1, 5)]

    n = len(labels)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    angles_plot = angles + [angles[0]]

    # Grid
    for ring in [20, 40, 60, 80, 100]:
        ring_vals = [ring] * (n + 1)
        ax.plot(angles_plot, ring_vals, color=COLORS["grid"],
                linewidth=0.5, alpha=0.6)

    # Partner A
    vals_a = values_a + [values_a[0]]
    ax.plot(angles_plot, vals_a, color=COLORS["primary"],
            linewidth=2.5, label=client_a["name"])
    ax.fill(angles_plot, vals_a, color=COLORS["primary"], alpha=0.1)

    # Partner B
    vals_b = values_b + [values_b[0]]
    ax.plot(angles_plot, vals_b, color=COLORS["secondary"],
            linewidth=2.5, linestyle="--", label=client_b["name"])
    ax.fill(angles_plot, vals_b, color=COLORS["secondary"], alpha=0.1)

    # Labels
    for angle, label in zip(angles, labels):
        ha = "center"
        if angle > 0 and angle < np.pi:
            ha = "left"
        elif angle > np.pi:
            ha = "right"
        ax.text(angle, 115, label, ha=ha, va="center",
                fontsize=9, color=COLORS["text"], fontweight="bold")

    ax.set_ylim(0, 120)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["polar"].set_visible(False)
    ax.set_title("Couples Overlay", fontsize=14, fontweight="bold",
                 color=COLORS["text"], pad=20)
    ax.legend(loc="upper right", fontsize=10)

    _save_chart(fig, output_path)
    return output_path


# ─────────────────────────────────────────────
# 6. RESTAURANT SAFETY PROFILE
# ─────────────────────────────────────────────

def generate_safety_profile(client_data, output_path):
    """Radar chart of 6 restaurant safety dimensions."""
    fig = _setup_figure((8, 8))
    ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor(COLORS["background"])

    safety = client_data.get("restaurant_safety", {})
    labels = list(safety.keys())
    values = list(safety.values())

    if not labels:
        plt.close(fig)
        return None

    _radar_chart(ax, labels, values, COLORS["accent"],
                 title=f"{client_data['name']} — Safety Profile")

    _save_chart(fig, output_path)
    return output_path


# ─────────────────────────────────────────────
# 7. HDR MECHANISM RADAR
# ─────────────────────────────────────────────

def generate_hdr_radar(client_data, output_path):
    """Radar chart of 6 HDR mechanism scores."""
    from hdr_mechanisms import detect_mechanisms

    fig = _setup_figure((8, 8))
    ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor(COLORS["background"])

    mechanisms = detect_mechanisms(client_data)
    labels = [m["name"] for m in mechanisms]
    values = [m["score"] for m in mechanisms]

    # Color: red for met mechanisms, grey for not met
    met_flags = [m["met"] for m in mechanisms]

    n = len(labels)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    angles_plot = angles + [angles[0]]
    values_plot = values + [values[0]]

    # Grid
    for ring in [20, 40, 60, 80, 100]:
        ring_vals = [ring] * (n + 1)
        ax.plot(angles_plot, ring_vals, color=COLORS["grid"],
                linewidth=0.5, alpha=0.6)

    # Fill
    ax.plot(angles_plot, values_plot, color=COLORS["risk_high"],
            linewidth=2)
    ax.fill(angles_plot, values_plot, color=COLORS["risk_high"],
            alpha=0.15)

    # Points — red for met, grey for not met
    for i, (angle, value, met) in enumerate(zip(angles, values, met_flags)):
        color = COLORS["risk_high"] if met else COLORS["grid"]
        ax.scatter(angle, value, s=60, color=color, zorder=5,
                   edgecolors=COLORS["text"], linewidths=1)

    # Labels
    for angle, label, value in zip(angles, labels, values):
        ha = "center"
        if angle > 0 and angle < np.pi:
            ha = "left"
        elif angle > np.pi:
            ha = "right"

        # Wrap long labels
        if len(label) > 16:
            parts = label.split(" ")
            mid = len(parts) // 2
            label = " ".join(parts[:mid]) + "\n" + " ".join(parts[mid:])

        ax.text(angle, 120, f"{label}\n{value}%",
                ha=ha, va="center", fontsize=7.5,
                color=COLORS["text"], fontweight="bold")

    ax.set_ylim(0, 130)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["polar"].set_visible(False)
    ax.set_title(f"{client_data['name']} — HDR Wound Mechanisms",
                 fontsize=13, fontweight="bold", color=COLORS["text"], pad=25)

    _save_chart(fig, output_path)
    return output_path


# ─────────────────────────────────────────────
# 8. PENDULUM RISK GAUGE
# ─────────────────────────────────────────────

def generate_pendulum_gauge(client_data, output_path):
    """Semi-circular gauge showing pendulum risk level."""
    from scoring_tools import pendulum_risk as calc_pendulum

    risk = calc_pendulum(client_data)
    risk_score = risk["risk_score"]
    risk_level = risk["risk_level"]

    fig = _setup_figure((8, 5))
    ax = fig.add_subplot(111)
    ax.set_facecolor(COLORS["background"])
    ax.set_aspect("equal")

    # Draw gauge arc segments (left=low/green, center=moderate, right=high/red)
    segments = [
        (120, 180, COLORS["risk_low"], "Low"),
        (60, 120, COLORS["risk_moderate"], "Moderate"),
        (0, 60, COLORS["risk_high"], "High"),
    ]

    for start_deg, end_deg, color, label in segments:
        wedge = Wedge((0.5, 0), 0.4, start_deg, end_deg,
                      width=0.12, facecolor=color, alpha=0.6,
                      edgecolor=COLORS["background"], linewidth=2)
        ax.add_patch(wedge)

    # Needle position: low score → left (180°), high score → right (0°)
    needle_angle = 180 - (risk_score / 100) * 180
    needle_rad = np.radians(needle_angle)
    needle_x = 0.5 + 0.32 * np.cos(needle_rad)
    needle_y = 0.32 * np.sin(needle_rad)

    ax.plot([0.5, needle_x], [0, needle_y], color=COLORS["text"],
            linewidth=3, zorder=5)
    ax.scatter(0.5, 0, s=100, color=COLORS["text"], zorder=6)

    # Labels
    ax.text(0.5, -0.12, f"{risk_level.upper()} RISK",
            ha="center", va="center", fontsize=16, fontweight="bold",
            color=COLORS["text"])
    ax.text(0.5, -0.2, f"Score: {risk_score}/100",
            ha="center", va="center", fontsize=11,
            color=COLORS["subtext"])

    # Segment labels
    ax.text(0.15, 0.18, "Low", ha="center", fontsize=9,
            color=COLORS["risk_low"], fontweight="bold")
    ax.text(0.5, 0.42, "Moderate", ha="center", fontsize=9,
            color=COLORS["risk_moderate"], fontweight="bold")
    ax.text(0.85, 0.18, "High", ha="center", fontsize=9,
            color=COLORS["risk_high"], fontweight="bold")

    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-0.3, 0.55)
    ax.axis("off")
    ax.set_title(f"{client_data['name']} — Pendulum Risk",
                 fontsize=13, fontweight="bold", color=COLORS["text"])

    _save_chart(fig, output_path)
    return output_path


# ─────────────────────────────────────────────
# MASTER GENERATOR
# ─────────────────────────────────────────────

def generate_all_charts(client_data, chart_dir):
    """
    Generate all charts for a client.
    Returns dict of chart_key -> file_path.
    """
    os.makedirs(chart_dir, exist_ok=True)
    name = client_data["name"].lower()
    paths = {}

    # SPINE master spider (primary chart)
    path = os.path.join(chart_dir, f"{name}_spine_spider.png")
    paths["spine"] = generate_spine_spider(client_data, path)

    # SPINE domain detail spiders
    for domain in SPINE_DOMAIN_ORDER:
        key = f"spine_{domain.lower()}"
        path = os.path.join(chart_dir, f"{name}_{key}.png")
        paths[key] = generate_spine_domain_spider(
            client_data, domain, path
        )

    # Cluster meta spider (secondary view)
    path = os.path.join(chart_dir, f"{name}_meta_spider.png")
    paths["meta"] = generate_meta_spider(client_data, path)

    # Cluster detail spiders (secondary view)
    for c in range(1, 5):
        path = os.path.join(chart_dir, f"{name}_cluster_{c}.png")
        paths[f"cluster_{c}"] = generate_cluster_spider(
            client_data, c, path
        )

    # Gap chart
    path = os.path.join(chart_dir, f"{name}_gap.png")
    paths["gap"] = generate_gap_chart(client_data, path)

    # Waypoint map
    path = os.path.join(chart_dir, f"{name}_waypoints.png")
    paths["waypoints"] = generate_waypoint_map(client_data, path)

    # Safety profile
    path = os.path.join(chart_dir, f"{name}_safety.png")
    paths["safety"] = generate_safety_profile(client_data, path)

    # HDR radar
    path = os.path.join(chart_dir, f"{name}_hdr_radar.png")
    paths["hdr_radar"] = generate_hdr_radar(client_data, path)

    # Pendulum gauge
    path = os.path.join(chart_dir, f"{name}_pendulum.png")
    paths["pendulum"] = generate_pendulum_gauge(client_data, path)

    return paths
