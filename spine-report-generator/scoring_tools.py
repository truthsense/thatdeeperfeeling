"""
SPINE Framework — Scoring Tools
Gap analysis, HDR mechanism detection, pendulum risk,
restaurant safety collision, sequencing, and therapy recommendations.
"""

from clients_data import (
    CLUSTER_NAMES, CLUSTER_AXES,
    SPINE_DOMAIN_ORDER, SPINE_DOMAINS,
    get_all_axes, get_all_vision, get_cluster_score,
    get_all_cluster_scores, get_lowest_axes, get_anchor_cluster,
    get_all_spine_scores, get_spine_vision_scores,
    get_lowest_spine_domain, get_highest_spine_domain,
    cluster_average,
)


# ─────────────────────────────────────────────
# GAP SCORING
# ─────────────────────────────────────────────

def gap_score(client_data):
    """
    Per axis: vision% - current%.
    Returns axis_gaps, max_gap_axis, avg_gap, gap_profile.
    """
    axes = get_all_axes(client_data)
    vision = get_all_vision(client_data)

    axis_gaps = {}
    for axis_name, score in axes.items():
        v = vision.get(axis_name, score)
        axis_gaps[axis_name] = v - score

    max_gap_axis = max(axis_gaps, key=axis_gaps.get) if axis_gaps else ""
    avg_gap = round(sum(axis_gaps.values()) / len(axis_gaps)) if axis_gaps else 0

    # Calculate cluster-level gaps
    cluster_gaps = {}
    for cluster_num in range(1, 5):
        cluster_axes = CLUSTER_AXES.get(cluster_num, [])
        gaps = [axis_gaps.get(a, 0) for a in cluster_axes if a in axis_gaps]
        cluster_gaps[cluster_num] = round(sum(gaps) / len(gaps)) if gaps else 0

    cluster_scores = get_all_cluster_scores(client_data)

    # Determine gap profile
    gap_profile = _determine_gap_profile(
        cluster_gaps, cluster_scores, axis_gaps
    )

    return {
        "axis_gaps": axis_gaps,
        "max_gap_axis": max_gap_axis,
        "avg_gap": avg_gap,
        "cluster_gaps": cluster_gaps,
        "gap_profile": gap_profile,
    }


def _determine_gap_profile(cluster_gaps, cluster_scores, axis_gaps):
    """Determine the gap profile type."""
    c1_gap = cluster_gaps.get(1, 0)
    c2_gap = cluster_gaps.get(2, 0)
    c3_gap = cluster_gaps.get(3, 0)
    c4_gap = cluster_gaps.get(4, 0)

    c1_score = cluster_scores.get(1, 0)
    c2_score = cluster_scores.get(2, 0)
    c3_score = cluster_scores.get(3, 0)
    c4_score = cluster_scores.get(4, 0)

    all_gaps = list(cluster_gaps.values())
    gap_range = max(all_gaps) - min(all_gaps) if all_gaps else 0
    all_scores = list(cluster_scores.values())

    # Head-body split: Cluster 1 avg gap > Cluster 2 avg gap by 20+ points
    if c1_gap > c2_gap + 20:
        return "head_body_split"

    # Relational gap: Cluster 2 avg gap > Cluster 1 avg gap by 20+ points
    if c2_gap > c1_gap + 20:
        return "relational_gap"

    # Forward gap: Cluster 3 avg gap > 35
    if c3_gap > 35:
        return "forward_gap"

    # Compressed: all cluster gaps within 10 AND all scores below 45%
    if gap_range <= 10 and all(s < 45 for s in all_scores):
        return "compressed"

    # Aliveness gap: Cluster 4 avg gap > 40 AND Cluster 4 score < 35%
    if c4_gap > 40 and c4_score < 35:
        return "aliveness_gap"

    # Even: all cluster gaps within 10 AND scores above 40%
    if gap_range <= 10 and all(s >= 40 for s in all_scores):
        return "even"

    return "mixed"


# ─────────────────────────────────────────────
# SPINE DOMAIN GAP SCORING
# ─────────────────────────────────────────────

def spine_gap_score(client_data):
    """
    Per SPINE domain: vision% - current%.
    Returns domain_gaps and spine_gap_profile.
    """
    scores = get_all_spine_scores(client_data)
    vision = get_spine_vision_scores(client_data)

    domain_gaps = {}
    for domain in SPINE_DOMAIN_ORDER:
        domain_gaps[domain] = vision[domain] - scores[domain]

    profile = _determine_spine_gap_profile(scores)

    return {
        "domain_scores": scores,
        "domain_gaps": domain_gaps,
        "spine_gap_profile": profile,
    }


def _determine_spine_gap_profile(scores):
    """Determine SPINE-level gap profile."""
    s = scores.get("Sovereignty", 0)
    p = scores.get("Power", 0)
    i = scores.get("Identity", 0)
    n = scores.get("Nourishment", 0)
    e = scores.get("Embodiment", 0)
    all_scores = [s, p, i, n, e]
    score_range = max(all_scores) - min(all_scores)

    # Embodiment deficit: E is lowest by 15+ points
    if e == min(all_scores) and (sorted(all_scores)[1] - e) >= 15:
        return "embodiment_deficit"

    # Sovereignty wound: S is lowest
    if s == min(all_scores) and (sorted(all_scores)[1] - s) >= 10:
        return "sovereignty_wound"

    # Power compression: P is lowest
    if p == min(all_scores) and (sorted(all_scores)[1] - p) >= 10:
        return "power_compression"

    # Nourishment blocked: N is lowest
    if n == min(all_scores) and (sorted(all_scores)[1] - n) >= 10:
        return "nourishment_blocked"

    # Identity searching: I is lowest but above 40%
    if i == min(all_scores) and i >= 40:
        return "identity_searching"

    # Compressed: all within 10 and below 40%
    if score_range <= 10 and all(x < 40 for x in all_scores):
        return "compressed"

    # Balanced: all within 10 and above 50%
    if score_range <= 10 and all(x >= 50 for x in all_scores):
        return "balanced"

    return "mixed"


# ─────────────────────────────────────────────
# HDR MECHANISM DETECTION
# ─────────────────────────────────────────────

def detect_hdr_mechanisms(client_data):
    """
    Score each of 6 mechanisms 0-100 based on proxy threshold matching.
    Return all mechanisms sorted by score.
    """
    from hdr_mechanisms import detect_mechanisms
    return detect_mechanisms(client_data)


def get_primary_mechanisms(client_data, top_n=2):
    """Return top N detected mechanisms with confidence scores."""
    from hdr_mechanisms import get_primary_mechanisms as _get_primary
    return _get_primary(client_data, top_n)


# ─────────────────────────────────────────────
# PENDULUM RISK
# ─────────────────────────────────────────────

def pendulum_risk(client_data):
    """
    Assess pendulum risk (swing from suppression to overcorrection).

    The pendulum model describes the nervous system's tendency to swing
    between two extremes when the middle ground hasn't been built:
      - SUPPRESSION: Total shutdown of desire, pleasure, and erotic selfhood.
        The system's original position. "I will feel nothing."
      - OVERCORRECTION: Compulsive, shame-driven acting out — often
        experienced as "losing control." The pendulum's opposite swing.
        "I will feel everything, all at once, before it's taken away."

    Neither position is chosen. Neither is the real self. The real self
    lives in the middle — in integrated, conscious desire — but the
    nervous system has never been given the ground to find that center.

    High risk indicators:
      - Arousal-Shame Decoupling < 25% (Sovereignty domain)
      - Any axis below 20%
      - Sovereignty domain avg below 30%
      - History of compulsive sexual behavior
    """
    axes = get_all_axes(client_data)
    spine_scores = get_all_spine_scores(client_data)
    sovereignty_score = spine_scores.get("Sovereignty", 50)
    embodiment_score = spine_scores.get("Embodiment", 50)

    risk_factors = []

    # Check Arousal-Shame Decoupling (Sovereignty domain)
    asd = axes.get("Arousal-Shame Decoupling", 50)
    if asd < 25:
        risk_factors.append(
            f"Arousal-Shame Decoupling at {asd}% (Sovereignty) — "
            f"desire and shame are still fused, creating swing risk"
        )

    # Check for any axis below 20%
    very_low = [(name, score) for name, score in axes.items() if score < 20]
    if very_low:
        names = ", ".join(f"{n} ({s}%)" for n, s in very_low)
        risk_factors.append(f"Axes below 20%: {names}")

    # Sovereignty domain average
    if sovereignty_score < 30:
        risk_factors.append(
            f"Sovereignty domain at {sovereignty_score}% — insufficient "
            f"ownership of desire and arousal for safe exploration"
        )

    # Embodiment domain check
    if embodiment_score < 25:
        risk_factors.append(
            f"Embodiment domain at {embodiment_score}% — the body is "
            f"not yet safe ground for the pendulum to slow"
        )

    # Check background for compulsive behavior keywords
    bg = client_data.get("background", "").lower()
    compulsive_markers = [
        "compulsive", "addiction", "pornography", "shame cycle",
        "beast to cage", "on fire or frozen",
    ]
    if any(marker in bg for marker in compulsive_markers):
        risk_factors.append(
            "Background indicates compulsive-suppressive cycling pattern"
        )

    # Determine risk level
    if len(risk_factors) >= 3:
        risk_level = "high"
        risk_score = min(100, 40 + len(risk_factors) * 15)
    elif len(risk_factors) >= 1:
        risk_level = "moderate"
        risk_score = 30 + len(risk_factors) * 10
    else:
        risk_level = "low"
        risk_score = 10

    # Generate narrative — explain what pendulum risk means for this person
    if risk_level == "high":
        risk_note = (
            "The pendulum is active. Your nervous system is caught between "
            "two positions — total suppression and compulsive overcorrection — "
            "and it swings between them because the middle ground hasn't "
            "been built yet. This isn't a moral failure. It's a nervous "
            "system pattern: the same mechanism that kept you 'pure' now "
            "drives the 'out of control' moments. They're not opposites. "
            "They're the same wound, expressing in two directions.\n\n"
            "The work is not to stop the swing by force — that just creates "
            "a harder rebound. The work is to build the middle ground: "
            "integrated, chosen, conscious desire. Sovereignty and Embodiment "
            "are where this ground gets built. As those domains strengthen, "
            "the pendulum naturally slows — not because you controlled it, "
            "but because you finally have somewhere to stand."
        )
        practitioner_note = (
            "HIGH PENDULUM RISK. Do not introduce exploration practices "
            "until Sovereignty domain exceeds 35%. Pleasure Minute and "
            "Daily Return only for first 4 weeks. Monitor for shame-"
            "driven acting out after sessions. Concurrent therapy "
            "strongly recommended."
        )
    elif risk_level == "moderate":
        risk_note = (
            "There's some swing risk here — the space between suppression "
            "and expression is still narrow. Your Sovereignty domain "
            f"at {sovereignty_score}% tells us the ownership of desire "
            "is emerging but not yet stable. The practices are designed "
            "to widen that space gradually, building the middle ground "
            "where conscious, chosen desire can live.\n\n"
            "The pendulum may still move — that's expected. What changes "
            "is the arc: shorter swings, faster returns to center, less "
            "shame after each movement. That narrowing is the progress."
        )
        practitioner_note = (
            "MODERATE PENDULUM RISK. Proceed with standard sequencing but "
            "monitor for overcorrection patterns. Check in about behaviors "
            "between sessions. Watch Sovereignty and Embodiment domains."
        )
    else:
        risk_note = (
            "The pendulum risk is low. Your Sovereignty and Embodiment "
            "domains have enough ground to hold the work without "
            "significant swing risk. This means your nervous system "
            "has the foundation to explore without the suppression-"
            "overcorrection cycle taking over.\n\n"
            "This doesn't mean the pendulum never moves — it means "
            "when it does, you have the internal ground to notice the "
            "movement and come back to center. That ground is real."
        )
        practitioner_note = (
            "LOW PENDULUM RISK. Standard sequencing appropriate. "
            "Sovereignty and Embodiment foundations are stable."
        )

    return {
        "risk_level": risk_level,
        "risk_score": risk_score,
        "risk_factors": risk_factors,
        "risk_note": risk_note,
        "practitioner_note": practitioner_note,
    }


# ─────────────────────────────────────────────
# RESTAURANT SAFETY COLLISION (Couples)
# ─────────────────────────────────────────────

SAFETY_TYPES = [
    "Structural Safety",
    "Social Safety",
    "Autonomy Safety",
    "Environmental Safety",
    "Informational Safety",
    "Relational Safety",
]

COLLISION_PAIRS = {
    ("Structural Safety", "Autonomy Safety"): {
        "name": "Structure vs Freedom",
        "note": (
            "One partner needs clear structure and predictability to feel safe. "
            "The other needs freedom and spontaneity. This is the most common "
            "collision in post-HDR couples — it's not a values conflict, it's "
            "two different nervous systems solving the same safety equation "
            "with opposite answers. The negotiation is in finding which "
            "structures serve freedom and which freedoms create structure."
        ),
    },
    ("Social Safety", "Autonomy Safety"): {
        "name": "Togetherness vs Independence",
        "note": (
            "One partner feels safe through connection and shared experience. "
            "The other feels safe through independence and personal space. "
            "Neither is wrong. The work is finding the rhythm between "
            "together and apart that serves both."
        ),
    },
    ("Informational Safety", "Autonomy Safety"): {
        "name": "Knowing vs Discovering",
        "note": (
            "One partner needs information and transparency to feel safe. "
            "The other needs mystery and spontaneity. This shows up in "
            "intimate contexts as a tension between planning and surprise."
        ),
    },
}


def restaurant_safety_collision(client_a, client_b):
    """
    Find dominant safety type per person and identify collision pairs.
    """
    safety_a = client_a.get("restaurant_safety", {})
    safety_b = client_b.get("restaurant_safety", {})

    if not safety_a or not safety_b:
        return {"collision": None, "note": "Safety data not available."}

    # Find dominant type for each
    dom_a = max(safety_a, key=safety_a.get)
    dom_b = max(safety_b, key=safety_b.get)

    # Find divergences > 25 points
    divergences = []
    for safety_type in SAFETY_TYPES:
        score_a = safety_a.get(safety_type, 50)
        score_b = safety_b.get(safety_type, 50)
        diff = abs(score_a - score_b)
        if diff > 25:
            divergences.append({
                "type": safety_type,
                "score_a": score_a,
                "score_b": score_b,
                "difference": diff,
            })

    # Check for known collision pairs
    collision = None
    collision_note = None
    for (type_1, type_2), info in COLLISION_PAIRS.items():
        if (dom_a == type_1 and dom_b == type_2) or \
           (dom_a == type_2 and dom_b == type_1):
            collision = info["name"]
            collision_note = info["note"]
            break

    return {
        "dominant_a": dom_a,
        "dominant_b": dom_b,
        "collision": collision,
        "collision_note": collision_note,
        "divergences": divergences,
    }


# ─────────────────────────────────────────────
# SEQUENCING RECOMMENDATION
# ─────────────────────────────────────────────

def sequencing_recommendation(client_data):
    """
    Generate ordered practice list with week assignments and rationale.
    Standard rules:
      - Any Cluster 1 axis < 30% → start there only
      - Cluster 1 avg must reach 40% before Cluster 2 work productive
      - Cluster 3 requires: Cluster 1 > 45% AND Cluster 2 > 40%
      - Cluster 4 begins when Cluster 1 > 50%
        (earlier if Eschatological Urgency is primary mechanism)
    """
    from practices import PRACTICES

    cluster_scores = get_all_cluster_scores(client_data)
    axes = get_all_axes(client_data)
    c1 = cluster_scores[1]
    c2 = cluster_scores[2]

    # Detect mechanisms for sequence adjustments
    mechanisms = get_primary_mechanisms(client_data)
    mech_keys = [m["key"] for m in mechanisms]

    # Determine available clusters
    available_clusters = {1}  # always start with cluster 1

    if c1 >= 40:
        available_clusters.add(2)
    if c1 >= 45 and c2 >= 40:
        available_clusters.add(3)
    if c1 >= 50:
        available_clusters.add(4)

    # Mechanism-specific adjustments
    if "eschatological_urgency" in mech_keys:
        available_clusters.add(4)  # Aliveness earlier

    if "vertical_authority" in mech_keys:
        # The Deed comes first
        available_clusters.add(2)

    if "identity_assignment" in mech_keys:
        available_clusters.add(3)  # Identity work earlier

    # Find lowest axes that need work
    low_axes = get_lowest_axes(client_data, 5)

    # Select practices
    selected = []
    used_keys = set()

    for practice_key, practice in PRACTICES.items():
        if practice_key in used_keys:
            continue
        if practice["cluster"] != 0 and \
           practice["cluster"] not in available_clusters:
            continue

        # Check if practice targets any low axis
        targets_low = any(
            axis_name in [a[0] for a in low_axes]
            for axis_name in practice["target_axes"]
        )
        # Check mechanism alignment
        aligns_mechanism = any(
            m in mech_keys
            for m in practice["mechanism_alignment"]
        )

        if targets_low or aligns_mechanism or not practice["target_axes"]:
            selected.append({
                "key": practice_key,
                "name": practice["name"],
                "cluster": practice["cluster"],
                "category": practice["category"],
                "weeks": practice["weeks"],
                "week_start": practice["week_start"],
                "week_end": practice["week_end"],
                "target_axes": practice["target_axes"],
                "mechanism_alignment": practice["mechanism_alignment"],
            })
            used_keys.add(practice_key)

    # Sort by week_start, then by category priority
    cat_order = {"healing": 0, "pattern": 1, "resourcing": 2}
    selected.sort(key=lambda p: (
        p["week_start"],
        cat_order.get(p["category"], 3),
    ))

    # Generate rationale
    rationale = _build_rationale(
        client_data, cluster_scores, mechanisms, available_clusters
    )

    return {
        "practices": selected[:8],
        "available_clusters": sorted(available_clusters),
        "rationale": rationale,
        "mechanisms": mech_keys,
    }


def _build_rationale(client_data, cluster_scores, mechanisms, available):
    """Build the sequencing rationale text."""
    c1 = cluster_scores[1]
    parts = []

    if c1 < 30:
        parts.append(
            f"Cluster 1 (Self) at {c1}% — below 30% threshold. "
            f"ALL initial work focuses here. No relational or "
            f"exploration practices until Self foundation strengthens."
        )
    elif c1 < 40:
        parts.append(
            f"Cluster 1 (Self) at {c1}% — approaching readiness for "
            f"Cluster 2 work. Continue Self practices while beginning "
            f"to introduce relational elements."
        )

    for mech in mechanisms:
        parts.append(
            f"{mech['name']} detected: {mech['sequence_adjustment']}"
        )

    if not parts:
        parts.append(
            "Standard sequencing applies. Self foundation is stable "
            "enough to support multi-cluster work."
        )

    return " | ".join(parts)


# ─────────────────────────────────────────────
# THERAPY RECOMMENDATION
# ─────────────────────────────────────────────

def therapy_recommendation(client_data):
    """
    Determine if concurrent therapy is recommended.
    Required if:
      - Cluster 1 avg < 30%
      - Any axis < 20%
      - Active dissociation reported
      - Cluster 1 gap score > 30 points
      - Stability score < 5/10
    """
    axes = get_all_axes(client_data)
    c1 = get_cluster_score(client_data, 1)
    stability = client_data.get("stability", 10)
    bg = client_data.get("background", "").lower()
    already_in_therapy = client_data.get("in_therapy", False)

    reasons = []

    if c1 < 30:
        reasons.append(f"Cluster 1 (Self) average at {c1}%")

    very_low = [n for n, s in axes.items() if s < 20]
    if very_low:
        reasons.append(f"Axes below 20%: {', '.join(very_low)}")

    if "dissociat" in bg:
        reasons.append("Active dissociation reported")

    # Check cluster 1 gap
    gap_data = gap_score(client_data)
    c1_gap = gap_data["cluster_gaps"].get(1, 0)
    if c1_gap > 30:
        reasons.append(f"Cluster 1 gap of {c1_gap} points")

    if stability < 5:
        reasons.append(f"Stability score of {stability}/10")

    recommended = len(reasons) >= 1
    urgency = "high" if len(reasons) >= 3 else (
        "moderate" if len(reasons) >= 1 else "low"
    )

    if recommended and not already_in_therapy:
        note = (
            "This map strongly indicates concurrent therapeutic support. "
            "This is not a barrier to the work — it is the most direct "
            "path to the work holding. A therapist who understands "
            "religious trauma can hold the container while you build "
            "the foundation."
        )
    elif recommended and already_in_therapy:
        note = (
            "You're already in therapy — good. This work is designed "
            "to complement, not replace, that relationship. Consider "
            "sharing this report with your therapist so they can "
            "support the somatic work this framework introduces."
        )
    else:
        note = (
            "No immediate therapy recommendation. Your stability and "
            "scores suggest this framework can proceed independently, "
            "though therapeutic support is always welcome."
        )

    return {
        "recommended": recommended,
        "urgency": urgency,
        "reasons": reasons,
        "note": note,
        "already_in_therapy": already_in_therapy,
    }


# ─────────────────────────────────────────────
# COUPLES READINESS
# ─────────────────────────────────────────────

def couples_readiness(client_a, client_b):
    """
    Both must meet:
      - Cluster 1 avg > 35%
      - Cluster 1 scores within 20 points

    If not met: name what individual work is needed FIRST.
    """
    c1_a = get_cluster_score(client_a, 1)
    c1_b = get_cluster_score(client_b, 1)

    name_a = client_a.get("name", "Person A")
    name_b = client_b.get("name", "Person B")

    issues = []

    if c1_a < 35:
        issues.append(
            f"{name_a}'s Self cluster at {c1_a}% needs to reach 35% "
            f"before couples work can hold"
        )
    if c1_b < 35:
        issues.append(
            f"{name_b}'s Self cluster at {c1_b}% needs to reach 35% "
            f"before couples work can hold"
        )

    gap = abs(c1_a - c1_b)
    if gap > 20:
        ahead = name_a if c1_a > c1_b else name_b
        behind = name_b if c1_a > c1_b else name_a
        issues.append(
            f"{gap}-point gap between partners' Self clusters. "
            f"{ahead} is further along. {behind} needs individual "
            f"foundation work before couples work is productive."
        )

    ready = len(issues) == 0

    if ready:
        note = (
            "Both partners meet the readiness threshold for couples work. "
            "Proceed with the Restaurant Safety Profile and couples overlay."
        )
    else:
        note = (
            "Not yet — and that's not a verdict, it's a pathway. "
            "The individual work named here IS the most intimate thing "
            "you can do for your relationship right now. Building your "
            "own foundation is not a detour from connection. It's the "
            "most direct route."
        )

    return {
        "ready": ready,
        "issues": issues,
        "note": note,
        "score_a": c1_a,
        "score_b": c1_b,
        "gap": gap,
    }
