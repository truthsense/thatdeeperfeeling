"""
SPINE Framework — HDR Wound Mechanisms
Six mechanisms by which High-Demand Religious systems create damage.
Each mechanism includes assessment proxies, reclamation sequence adjustments,
and report narrative templates.
"""

import re


# ─────────────────────────────────────────────
# MECHANISM DEFINITIONS
# ─────────────────────────────────────────────

MECHANISMS = {
    "divine_surveillance": {
        "name": "Divine Surveillance",
        "spine_domains": ["Embodiment", "Sovereignty"],
        "description": (
            "The installation of an omniscient internal observer. "
            "No thought, feeling, or impulse is private. "
            "The body learns it can never be unwatched."
        ),
        "proxy_axes": {
            "Body Trust": {"threshold": 30, "direction": "below"},
            "shame_having_desire": {"threshold": 4, "direction": "at_or_above"},
            "shame_emotions": {"threshold": 4, "direction": "at_or_above"},
            "Spontaneous Presence": {"threshold": 30, "direction": "below"},
        },
        "proxy_required": 2,
        "sequence_adjustment": (
            "ALL early practices must be completely private — no sharing, "
            "no witnessing required until Body Trust > 40%. "
            "The Witnessed Voice starts with recordings never listened to. "
            "Build the experience of an unobserved interior before anything relational."
        ),
        "narrative": (
            "The system installed an observer who never left the room. "
            "Every thought, every impulse, every flicker of desire was visible "
            "to an omniscient presence keeping score. Your body learned there "
            "is no privacy — no unobserved moment, no feeling without moral "
            "consequence. Body Trust at {body_trust}% tells us that observer "
            "is still present, even now. The first work is not healing. It's "
            "finding out what it feels like to be alone in your own interior. "
            "Really alone. With no one watching."
        ),
    },
    "identity_assignment": {
        "name": "Identity Assignment",
        "spine_domains": ["Identity"],
        "description": (
            "The self is defined before it can define itself. "
            "Gender role, sexual expression, emotional range, relational hierarchy — "
            "all assigned by divine decree, often before puberty."
        ),
        "proxy_axes": {
            "Self-Authorship": {"threshold": 40, "direction": "below"},
            "Authentic Differentiation": {"threshold": 35, "direction": "below"},
            "Complexity Tolerance": {"threshold": 40, "direction": "below"},
            "Body Trust (non-binary)": {"threshold": 35, "direction": "below"},
        },
        "proxy_required": 2,
        "sequence_adjustment": (
            "For gender-assigned wound: use gender-affirming body practices "
            "BEFORE standard body trust work. 'Which parts of this body feel "
            "like mine' precedes 'what does this body want.' Identity work "
            "(Cluster 3) becomes accessible earlier than standard sequence "
            "when this is primary mechanism."
        ),
        "narrative": (
            "You were handed yourself before you could choose. The role, the "
            "gender expression, the relational position — assigned by divine "
            "decree before you had language to consent or refuse. "
            "Self-Authorship at {self_authorship}% reflects not a lack of self "
            "but a self built inside someone else's blueprint, learning now "
            "what it actually looks like on its own land, in its own light."
        ),
    },
    "purity_worth_fusion": {
        "name": "Purity-Worth Fusion",
        "spine_domains": ["Sovereignty", "Nourishment"],
        "description": (
            "Worth is structurally indexed to purity. Not as rule but as equation: "
            "pure = worthy, impure = worthless. Desire itself becomes existential "
            "threat — not just problematic but self-annihilating."
        ),
        "proxy_axes": {
            "Pleasure Permission": {"threshold": 40, "direction": "below"},
            "Erotic Self-Acceptance": {"threshold": 35, "direction": "below"},
            "Need Legitimacy": {"threshold": 40, "direction": "below"},
            "Receiving Capacity": {"threshold": 35, "direction": "below"},
            "shame_sexual_history": {"threshold": 4, "direction": "at_or_above"},
        },
        "proxy_required": 2,
        "sequence_adjustment": (
            "Worth-decoupling BEFORE desire work. The Pleasure Minute "
            "(uncomplicated sensory pleasure) before any erotic exploration. "
            "Build tolerance for receiving goodness that is unearned before "
            "approaching erotic territory where worth-fusion is most charged."
        ),
        "narrative": (
            "Your worth was indexed to your purity — not as a rule to follow "
            "but as a structural equation. Pure equals worthy. Impure equals "
            "worthless. This made desire itself a threat to your existence — "
            "not just morally problematic but self-annihilating. "
            "Pleasure Permission at {pleasure_permission}% is what remains of "
            "a protective system that was genuinely trying to keep you intact. "
            "It made sense then. The work now is not to shame the protector "
            "but to show it the equation has changed."
        ),
    },
    "vertical_authority": {
        "name": "Vertical Authority Architecture",
        "spine_domains": ["Power"],
        "description": (
            "Authority flows one direction only: God → scripture → leadership → self. "
            "The self has no legitimate internal authority. Internal signals are "
            "dismissed as selfish, demonic, or immature."
        ),
        "proxy_axes": {
            "Self-Authorization": {"threshold": 35, "direction": "below"},
            "Refusal Capacity": {"threshold": 35, "direction": "below"},
            "Choice Ownership": {"threshold": 40, "direction": "below"},
            "Boundary Sovereignty": {"threshold": 35, "direction": "below"},
        },
        "proxy_required": 2,
        "sequence_adjustment": (
            "The Deed (self-authorization practice) comes FIRST — before any "
            "body work, before any relational work. Build in completely "
            "non-sexual, non-intimate contexts first. Nervous system must "
            "learn self-authority exists before exercising it in charged territory."
        ),
        "narrative": (
            "The system was a one-way channel. Authority flowed down — God to "
            "scripture to leadership to you. Your own internal signals — desires, "
            "hesitations, refusals, preferences — were noise at best, spiritual "
            "failure at worst. Self-Authorization at {self_authorization}% is "
            "the result of years of training that your own knowing is not a "
            "reliable source. The reclamation begins with the smallest possible "
            "act of self-authority: not a declaration, just a choice. One small, "
            "genuine choice, owned completely. Then another."
        ),
    },
    "eschatological_urgency": {
        "name": "Eschatological Urgency",
        "spine_domains": ["Embodiment", "Nourishment"],
        "description": (
            "The world is ending. The judgment is coming. The stakes are always "
            "infinite. This creates permanent threat-state that prevents the "
            "nervous system from resting into pleasure or play."
        ),
        "proxy_axes": {
            "Intimate Levity": {"threshold": 30, "direction": "below"},
            "Spontaneous Presence": {"threshold": 30, "direction": "below"},
            "Erotic Play Capacity": {"threshold": 30, "direction": "below"},
            "Pleasure Permission": {"threshold": 35, "direction": "below"},
        },
        "proxy_required": 2,
        "sequence_adjustment": (
            "Cluster 4 (Aliveness) practices come EARLIER than standard "
            "sequence — the nervous system needs evidence that good things "
            "can be uncomplicated BEFORE deeper healing work feels survivable. "
            "Begin with smallest possible uncomplicated pleasure — literally "
            "one minute — as foundational practice."
        ),
        "narrative": (
            "Everything was a cosmic emergency. The stakes were always infinite, "
            "the judgment always imminent. Your nervous system learned that "
            "pleasure without punishment doesn't exist — that joy is borrowed "
            "time, that good things are followed by consequences. "
            "Intimate Levity at {intimate_levity}% tells us that emergency "
            "state is still running even after the doctrine left. The first "
            "work here is almost embarrassingly small: one minute of something "
            "genuinely pleasurable, with nothing required of it. No meaning. "
            "No significance. Just: this is good, and that is allowed."
        ),
    },
    "community_surveillance": {
        "name": "Community Surveillance",
        "spine_domains": ["Power"],
        "description": (
            "The community enforced the system. Belonging was conditional on "
            "compliance. Leaving meant losing everything — family, friends, "
            "identity, sometimes housing. This creates relational terror around "
            "authenticity that operates independently of belief."
        ),
        "proxy_axes": {
            "Boundary Sovereignty": {"threshold": 40, "direction": "below"},
            "Communication Capacity": {"threshold": 40, "direction": "below"},
            "Receiving Capacity": {"threshold": 35, "direction": "below"},
        },
        "proxy_required": 2,
        "sequence_adjustment": (
            "Witnessed Voice starts completely private — recordings not shared. "
            "No partner homework in first 6 weeks. Build the private self "
            "before the witnessed self. Relational practices begin ONLY after "
            "Boundary Sovereignty reaches 40%."
        ),
        "narrative": (
            "The community was the system's enforcement mechanism. Belonging "
            "was conditional — on compliance, on performance, on visible purity. "
            "Leaving didn't just mean changing beliefs. It meant losing everything "
            "at once. Your over-pleasing, your boundary collapse with new partners "
            "or communities — this isn't weakness. It's your nervous system trying "
            "to prevent another total loss by managing everyone's experience of "
            "you before they decide you're too much. The work is not to stop "
            "caring about belonging. It's to find out what belonging feels like "
            "when it isn't conditional."
        ),
    },
}


# ─────────────────────────────────────────────
# CLOSING NARRATIVE (appended to mechanism section)
# ─────────────────────────────────────────────

MECHANISM_CLOSING = (
    "This is the wound's architecture. Knowing how it was built is the "
    "beginning of knowing how to unbuild it — not with force, but with "
    "the specific tools the specific structure requires."
)


# ─────────────────────────────────────────────
# DETECTION FUNCTIONS
# ─────────────────────────────────────────────

def _check_proxy(client_data, axis_name, proxy_config):
    """Check if a single proxy condition is met."""
    threshold = proxy_config["threshold"]
    direction = proxy_config["direction"]

    # Check shame sources first
    shame_map = {
        "shame_having_desire": "Having desire at all",
        "shame_emotions": "emotions",
        "shame_sexual_history": "Sexual history",
    }
    if axis_name in shame_map:
        shame_key = shame_map[axis_name]
        shame_sources = client_data.get("shame_sources", {})
        for key, val in shame_sources.items():
            if shame_key.lower() in key.lower():
                if direction == "at_or_above":
                    return val >= threshold
                return val < threshold
        return False

    # Handle non-binary specific proxy
    if axis_name.endswith("(non-binary)"):
        base_axis = axis_name.replace(" (non-binary)", "")
        gender = client_data.get("gender_identity", "").lower()
        if gender not in ("non-binary", "nonbinary", "genderqueer"):
            return False
        axis_name = base_axis

    # Check cluster axes
    clusters = client_data.get("clusters", {})
    for cluster_num, cluster_data in clusters.items():
        axes = cluster_data.get("axes", {})
        if axis_name in axes:
            score = axes[axis_name]
            if direction == "below":
                return score < threshold
            elif direction == "at_or_above":
                return score >= threshold
            elif direction == "above":
                return score > threshold

    return False


def detect_mechanisms(client_data):
    """
    Score each of 6 mechanisms 0-100 based on proxy threshold matching.
    Returns list of all mechanisms with scores, sorted by confidence.
    """
    results = []

    for mech_key, mech in MECHANISMS.items():
        proxies = mech["proxy_axes"]
        required = mech["proxy_required"]

        matches = 0
        total = len(proxies)

        for axis_name, proxy_config in proxies.items():
            if _check_proxy(client_data, axis_name, proxy_config):
                matches += 1

        # Score: proportion of matches * 100, with bonus for exceeding required
        if matches >= required:
            base_score = (matches / total) * 80
            bonus = min(20, (matches - required) * 10)
            score = min(100, base_score + bonus)
        elif matches > 0:
            score = (matches / total) * 40
        else:
            score = 0

        results.append({
            "key": mech_key,
            "name": mech["name"],
            "score": round(score),
            "matches": matches,
            "total": total,
            "required": required,
            "met": matches >= required,
            "description": mech["description"],
            "narrative": mech["narrative"],
            "sequence_adjustment": mech["sequence_adjustment"],
            "spine_domains": mech.get("spine_domains", []),
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results


def get_primary_mechanisms(client_data, top_n=2):
    """Return top N detected mechanisms with confidence scores."""
    all_mechs = detect_mechanisms(client_data)
    return [m for m in all_mechs[:top_n] if m["met"]]


def format_mechanism_narrative(mechanism_result, client_data):
    """Format a mechanism's narrative with client-specific scores."""
    narrative = mechanism_result["narrative"]

    # Build replacement dict from client data
    clusters = client_data.get("clusters", {})
    replacements = {}

    for cluster_num, cluster_data in clusters.items():
        axes = cluster_data.get("axes", {})
        for axis_name, score in axes.items():
            key = axis_name.lower().replace(" ", "_").replace("-", "_")
            replacements[key] = score

    # Replace what we can, leave placeholders for missing
    def replace_match(match):
        key = match.group(1)
        return str(replacements.get(key, f"[{key}]"))

    return re.sub(r'\{(\w+)\}', replace_match, narrative)


def get_mechanism_report_section(client_data):
    """
    Generate the complete 'What Was Done To You' report section.
    Returns dict with primary mechanisms, narratives, and closing.
    """
    primary = get_primary_mechanisms(client_data)

    sections = []
    for mech in primary:
        sections.append({
            "name": mech["name"],
            "score": mech["score"],
            "narrative": format_mechanism_narrative(mech, client_data),
            "sequence_adjustment": mech["sequence_adjustment"],
        })

    return {
        "mechanisms": sections,
        "closing": MECHANISM_CLOSING,
        "all_scores": detect_mechanisms(client_data),
    }
