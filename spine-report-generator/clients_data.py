"""
SPINE Framework — Client Assessment Data
Sexual domain with 4 clusters × 5 axes each.
All four case study clients with complete scoring data.
"""

# Category constants
HEALING = "healing"
PATTERN = "pattern"
RESOURCING = "resourcing"
ANCHOR = "anchor"
EXPLORING = "exploring"

# Body check constants
CURIOSITY = "curiosity"
MILD_RESISTANCE = "mild resistance"
RESISTANCE = "resistance"
SIGNIFICANT_RESISTANCE = "significant resistance"
DISTRESS = "distress"
BLANKNESS = "blankness"

# Stage thresholds (per cluster score)
STAGES = [
    (0, 25, "Blank Page"),
    (26, 35, "Foundational"),
    (36, 45, "Excavation"),
    (46, 55, "Emergence"),
    (56, 65, "Recognition/Practice"),
    (66, 75, "Composition"),
    (76, 85, "Authorship"),
    (86, 100, "Integration"),
]


def get_stage(score):
    """Return stage name for a given percentage score."""
    for low, high, name in STAGES:
        if low <= score <= high:
            return name
    return "Integration" if score > 100 else "Blank Page"


# ─────────────────────────────────────────────
# SEXUAL DOMAIN — CLUSTER/AXIS DEFINITIONS
# ─────────────────────────────────────────────

CLUSTER_NAMES = {
    1: "Self",
    2: "Between",
    3: "Forward",
    4: "Aliveness",
}

CLUSTER_AXES = {
    1: [
        "Desire Ownership",
        "Arousal-Shame Decoupling",
        "Pleasure Permission",
        "Body Trust",
        "Erotic Self-Acceptance",
    ],
    2: [
        "Consent Clarity",
        "Communication Capacity",
        "Attachment Pattern Awareness",
        "Boundary Sovereignty",
        "Receiving Capacity",
    ],
    3: [
        "Erotic Identity Clarity",
        "Orientation & Preference Exploration",
        "Conscious Exploration Capacity",
        "Sexual Future Vision",
        "Integration Readiness",
    ],
    4: [
        "Erotic Play Capacity",
        "Sensory Range",
        "Spontaneous Presence",
        "Intimate Levity",
        "Embodied Curiosity",
    ],
}

# ─────────────────────────────────────────────
# SPINE 5-DOMAIN FRAMEWORK (Primary Architecture)
# Sexual axes map onto SPINE domains as the master view.
# ─────────────────────────────────────────────

SPINE_DOMAIN_ORDER = ["Sovereignty", "Power", "Identity", "Nourishment", "Embodiment"]

SPINE_DOMAINS = {
    "Sovereignty": {
        "letter": "S",
        "description": (
            "The capacity to own your own interior — desire, arousal, "
            "and erotic selfhood without external permission."
        ),
        "axes": [
            "Desire Ownership",
            "Arousal-Shame Decoupling",
            "Erotic Self-Acceptance",
        ],
    },
    "Power": {
        "letter": "P",
        "description": (
            "The capacity to act from your own authority — consent, "
            "communication, boundaries, and relational awareness."
        ),
        "axes": [
            "Consent Clarity",
            "Communication Capacity",
            "Boundary Sovereignty",
            "Attachment Pattern Awareness",
        ],
    },
    "Identity": {
        "letter": "I",
        "description": (
            "The capacity to know and define yourself — erotic identity, "
            "orientation, exploration, vision, and integration."
        ),
        "axes": [
            "Erotic Identity Clarity",
            "Orientation & Preference Exploration",
            "Conscious Exploration Capacity",
            "Sexual Future Vision",
            "Integration Readiness",
        ],
    },
    "Nourishment": {
        "letter": "N",
        "description": (
            "The capacity to receive and enjoy — pleasure, receiving, "
            "and erotic play without earning it first."
        ),
        "axes": [
            "Pleasure Permission",
            "Receiving Capacity",
            "Erotic Play Capacity",
        ],
    },
    "Embodiment": {
        "letter": "E",
        "description": (
            "The capacity to live in and trust your body — somatic "
            "presence, sensory range, spontaneity, levity, and curiosity."
        ),
        "axes": [
            "Body Trust",
            "Sensory Range",
            "Spontaneous Presence",
            "Intimate Levity",
            "Embodied Curiosity",
        ],
    },
}

# Reverse lookup: axis name → SPINE domain name
AXIS_TO_SPINE = {}
for _domain_name, _domain_info in SPINE_DOMAINS.items():
    for _axis in _domain_info["axes"]:
        AXIS_TO_SPINE[_axis] = _domain_name

# Reverse lookup: axis name → cluster number
AXIS_TO_CLUSTER = {}
for _cnum, _caxes in CLUSTER_AXES.items():
    for _axis in _caxes:
        AXIS_TO_CLUSTER[_axis] = _cnum


# Emotional domain — scaffold only
EMOTIONAL_CLUSTERS = {
    1: {
        "name": "Emotional Self",
        "axes": [
            "Emotional Ownership", "Grief Permission", "Anger Legitimacy",
            "Joy Without Guilt", "Emotional Complexity Tolerance",
        ],
    },
    2: {
        "name": "Emotional Between",
        "axes": [
            "Emotional Communication", "Receiving Care", "Conflict Tolerance",
            "Emotional Repair", "Vulnerability Capacity",
        ],
    },
    3: {
        "name": "Emotional Forward",
        "axes": [
            "Emotional Range", "Emotional Creativity", "Post-Traumatic Growth",
            "Integrated Emotional History", "Authentic Expression",
        ],
    },
    4: {
        "name": "Emotional Aliveness",
        "axes": [
            "Spontaneous Feeling", "Playful Emotionality", "Emotional Curiosity",
            "Felt Sense Access", "Expressive Freedom",
        ],
    },
}

# Spiritual domain — scaffold only
SPIRITUAL_CLUSTERS = {
    1: {
        "name": "Spiritual Self",
        "axes": [
            "Divine Attachment Grief", "Spiritual Authority Reclamation",
            "Sacred Body Recognition", "Mystical Capacity",
            "Sacred Intimacy Transfer",
        ],
    },
    2: {
        "name": "Spiritual Between",
        "axes": [
            "Community Without Surrender", "Spiritual Conversation Capacity",
            "Ritual Reclamation", "Spiritual Disagreement Tolerance",
            "Sacred Presence with Others",
        ],
    },
    3: {
        "name": "Spiritual Forward",
        "axes": [
            "Personal Theology", "Meaning-Making Capacity",
            "Spiritual Future Vision", "Erotic-Sacred Integration",
            "Transcendence Ownership",
        ],
    },
    4: {
        "name": "Spiritual Aliveness",
        "axes": [
            "Awe Capacity", "Spiritual Play", "Embodied Transcendence",
            "Sacred Ordinary", "Wonder Without Doctrine",
        ],
    },
}


def cluster_average(axes_dict):
    """Calculate cluster average from axes dict."""
    if not axes_dict:
        return 0
    return round(sum(axes_dict.values()) / len(axes_dict))


def domain_average(clusters_dict):
    """Calculate domain average from clusters dict."""
    avgs = []
    for cluster_data in clusters_dict.values():
        axes = cluster_data.get("axes", {})
        if axes:
            avgs.append(cluster_average(axes))
    return round(sum(avgs) / len(avgs)) if avgs else 0


# ─────────────────────────────────────────────
# CLIENT DATA
# ─────────────────────────────────────────────

CLIENTS = {}

# ─────────────────────────────────────────────
# CLIENT 1: SARAH, 38
# ─────────────────────────────────────────────
CLIENTS["sarah"] = {
    "name": "Sarah",
    "age": 38,
    "background": (
        "Grew up in a conservative Baptist household, married at 22 within "
        "the church community, left the church at 34 after her husband began "
        "his own deconstruction. Has two children. Currently in individual "
        "therapy (CBT-focused). Has been 'deconstructing' intellectually for "
        "four years but describes her body as 'still living in the old house.' "
        "Reports that sex within her marriage has improved but she frequently "
        "dissociates during intimacy and has never experienced orgasm. Identifies "
        "as heterosexual but has occasionally noticed attraction to women that "
        "she immediately shuts down."
    ),
    "entry_point": (
        "Referred by her therapist who recognized the religious-specific "
        "sexual wound pattern wasn't being addressed in CBT work."
    ),
    "stability": 7,
    "in_therapy": True,
    "date": None,
    "gender_identity": "female",

    "shame_sources": {
        "Having desire at all": 5,
        "Specific desires or fantasies": 4,
        "Sexual history": 3,
        "Body appearance/response": 5,
        "Orientation or attractions": 2,
        "Having strong emotions": 4,
        "Doubting or leaving the system": 4,
        "Choices inside the system": 3,
        "How much I need from other people": 3,
        "Speaking up or using my voice": 4,
    },

    "clusters": {
        1: {
            "name": "Self",
            "axes": {
                "Desire Ownership": 56,
                "Arousal-Shame Decoupling": 32,
                "Pleasure Permission": 28,
                "Body Trust": 24,
                "Erotic Self-Acceptance": 35,
            },
            "body_check": DISTRESS,
        },
        2: {
            "name": "Between",
            "axes": {
                "Consent Clarity": 64,
                "Communication Capacity": 48,
                "Attachment Pattern Awareness": 72,
                "Boundary Sovereignty": 56,
                "Receiving Capacity": 60,
            },
            "body_check": MILD_RESISTANCE,
        },
        3: {
            "name": "Forward",
            "axes": {
                "Erotic Identity Clarity": 76,
                "Orientation & Preference Exploration": 44,
                "Conscious Exploration Capacity": 52,
                "Sexual Future Vision": 68,
                "Integration Readiness": 60,
            },
            "body_check": CURIOSITY,
        },
        4: {
            "name": "Aliveness",
            "axes": {
                "Erotic Play Capacity": 28,
                "Sensory Range": 32,
                "Spontaneous Presence": 24,
                "Intimate Levity": 36,
                "Embodied Curiosity": 30,
            },
            "body_check": MILD_RESISTANCE,
        },
    },

    "vision": {
        1: {
            "Desire Ownership": 80,
            "Arousal-Shame Decoupling": 70,
            "Pleasure Permission": 75,
            "Body Trust": 72,
            "Erotic Self-Acceptance": 75,
        },
        2: {
            "Consent Clarity": 80,
            "Communication Capacity": 78,
            "Attachment Pattern Awareness": 85,
            "Boundary Sovereignty": 78,
            "Receiving Capacity": 80,
        },
        3: {
            "Erotic Identity Clarity": 88,
            "Orientation & Preference Exploration": 75,
            "Conscious Exploration Capacity": 78,
            "Sexual Future Vision": 85,
            "Integration Readiness": 80,
        },
        4: {
            "Erotic Play Capacity": 70,
            "Sensory Range": 72,
            "Spontaneous Presence": 68,
            "Intimate Levity": 72,
            "Embodied Curiosity": 70,
        },
    },

    "restaurant_safety": {
        "Structural Safety": 72,
        "Social Safety": 58,
        "Autonomy Safety": 45,
        "Environmental Safety": 65,
        "Informational Safety": 68,
        "Relational Safety": 52,
    },

    "central_tension": (
        "Your mind arrived somewhere your nervous system hasn't. "
        "25-point gap between Forward/Between (60%) and Self (35%). "
        "The self you've built conceptually hasn't been invited "
        "into the body yet."
    ),

    "special_note": None,
}

# ─────────────────────────────────────────────
# CLIENT 2: MARCUS, 44
# ─────────────────────────────────────────────
CLIENTS["marcus"] = {
    "name": "Marcus",
    "age": 44,
    "background": (
        "Former evangelical worship leader, left at 40, divorced. "
        "Pornography shame cycle — describes sexuality as 'a beast to cage.' "
        "Four years post-exit. No therapy. Significant shame across all "
        "domains. Reports compulsive sexual behavior alternating with "
        "complete shutdown. Describes himself as 'either on fire or frozen.'"
    ),
    "entry_point": (
        "Self-referred after reading about religious trauma and sexuality. "
        "Reports feeling stuck in a cycle he can't break."
    ),
    "stability": 4,
    "in_therapy": False,
    "date": None,
    "gender_identity": "male",

    "shame_sources": {
        "Having desire at all": 5,
        "Specific desires or fantasies": 5,
        "Sexual history": 5,
        "Body appearance/response": 4,
        "Orientation or attractions": 3,
        "Having strong emotions": 4,
        "Doubting or leaving the system": 5,
        "Choices inside the system": 5,
        "How much I need from other people": 4,
        "Speaking up or using my voice": 4,
    },

    "clusters": {
        1: {
            "name": "Self",
            "axes": {
                "Desire Ownership": 22,
                "Arousal-Shame Decoupling": 15,
                "Pleasure Permission": 18,
                "Body Trust": 20,
                "Erotic Self-Acceptance": 16,
            },
            "body_check": DISTRESS,
        },
        2: {
            "name": "Between",
            "axes": {
                "Consent Clarity": 38,
                "Communication Capacity": 30,
                "Attachment Pattern Awareness": 35,
                "Boundary Sovereignty": 25,
                "Receiving Capacity": 22,
            },
            "body_check": DISTRESS,
        },
        3: {
            "name": "Forward",
            "axes": {
                "Erotic Identity Clarity": 28,
                "Orientation & Preference Exploration": 32,
                "Conscious Exploration Capacity": 20,
                "Sexual Future Vision": 35,
                "Integration Readiness": 18,
            },
            "body_check": SIGNIFICANT_RESISTANCE,
        },
        4: {
            "name": "Aliveness",
            "axes": {
                "Erotic Play Capacity": 12,
                "Sensory Range": 18,
                "Spontaneous Presence": 15,
                "Intimate Levity": 10,
                "Embodied Curiosity": 14,
            },
            "body_check": DISTRESS,
        },
    },

    "vision": {
        1: {
            "Desire Ownership": 65,
            "Arousal-Shame Decoupling": 60,
            "Pleasure Permission": 65,
            "Body Trust": 62,
            "Erotic Self-Acceptance": 60,
        },
        2: {
            "Consent Clarity": 70,
            "Communication Capacity": 68,
            "Attachment Pattern Awareness": 70,
            "Boundary Sovereignty": 65,
            "Receiving Capacity": 65,
        },
        3: {
            "Erotic Identity Clarity": 65,
            "Orientation & Preference Exploration": 60,
            "Conscious Exploration Capacity": 62,
            "Sexual Future Vision": 68,
            "Integration Readiness": 58,
        },
        4: {
            "Erotic Play Capacity": 55,
            "Sensory Range": 58,
            "Spontaneous Presence": 55,
            "Intimate Levity": 52,
            "Embodied Curiosity": 55,
        },
    },

    "restaurant_safety": {
        "Structural Safety": 42,
        "Social Safety": 35,
        "Autonomy Safety": 55,
        "Environmental Safety": 48,
        "Informational Safety": 38,
        "Relational Safety": 30,
    },

    "central_tension": (
        "Even compression across all four clusters — the system's impact "
        "was total and thorough. No cluster significantly ahead of others. "
        "The spine was prevented from forming everywhere simultaneously. "
        "Everything starts at the foundation."
    ),

    "special_note": {
        "type": "therapy_recommendation",
        "title": "Concurrent Therapeutic Support Recommended",
        "text": (
            "Marcus, this map strongly indicates concurrent therapeutic "
            "support is needed alongside this framework. Stability score "
            "of 4/10 and distress responses across all clusters suggest "
            "this work needs a therapeutic container. The pendulum pattern "
            "(compulsive-then-shutdown) requires professional support to "
            "navigate safely. This is not a barrier — it is the most "
            "direct path to the work holding."
        ),
    },
}

# ─────────────────────────────────────────────
# CLIENT 3: ELENA, 29
# ─────────────────────────────────────────────
CLIENTS["elena"] = {
    "name": "Elena",
    "age": 29,
    "background": (
        "Catholic upbringing, came out bisexual at 24, 2 years affirming "
        "therapy. In first same-sex relationship. Over-pleasing partner. "
        "Shame responses persist despite intellectual processing. Reports "
        "that therapy addressed orientation but not the deeper purity wound "
        "underneath. Describes a pattern of giving everything to partners "
        "and then collapsing."
    ),
    "entry_point": (
        "Referred by her affirming therapist who noted the relational "
        "pattern wasn't shifting despite good therapeutic progress on "
        "orientation acceptance."
    ),
    "stability": 7,
    "in_therapy": True,
    "date": None,
    "gender_identity": "female",

    "shame_sources": {
        "Having desire at all": 2,
        "Specific desires or fantasies": 3,
        "Sexual history": 2,
        "Body appearance/response": 3,
        "Orientation or attractions": 4,
        "Having strong emotions": 2,
        "Doubting or leaving the system": 3,
        "Choices inside the system": 2,
        "How much I need from other people": 4,
        "Speaking up or using my voice": 3,
    },

    "clusters": {
        1: {
            "name": "Self",
            "axes": {
                "Desire Ownership": 62,
                "Arousal-Shame Decoupling": 52,
                "Pleasure Permission": 48,
                "Body Trust": 44,
                "Erotic Self-Acceptance": 58,
            },
            "body_check": MILD_RESISTANCE,
        },
        2: {
            "name": "Between",
            "axes": {
                "Consent Clarity": 56,
                "Communication Capacity": 52,
                "Attachment Pattern Awareness": 65,
                "Boundary Sovereignty": 42,
                "Receiving Capacity": 38,
            },
            "body_check": MILD_RESISTANCE,
        },
        3: {
            "name": "Forward",
            "axes": {
                "Erotic Identity Clarity": 72,
                "Orientation & Preference Exploration": 68,
                "Conscious Exploration Capacity": 58,
                "Sexual Future Vision": 65,
                "Integration Readiness": 52,
            },
            "body_check": CURIOSITY,
        },
        4: {
            "name": "Aliveness",
            "axes": {
                "Erotic Play Capacity": 45,
                "Sensory Range": 50,
                "Spontaneous Presence": 42,
                "Intimate Levity": 48,
                "Embodied Curiosity": 52,
            },
            "body_check": CURIOSITY,
        },
    },

    "vision": {
        1: {
            "Desire Ownership": 82,
            "Arousal-Shame Decoupling": 78,
            "Pleasure Permission": 80,
            "Body Trust": 75,
            "Erotic Self-Acceptance": 82,
        },
        2: {
            "Consent Clarity": 80,
            "Communication Capacity": 78,
            "Attachment Pattern Awareness": 82,
            "Boundary Sovereignty": 78,
            "Receiving Capacity": 75,
        },
        3: {
            "Erotic Identity Clarity": 88,
            "Orientation & Preference Exploration": 85,
            "Conscious Exploration Capacity": 80,
            "Sexual Future Vision": 82,
            "Integration Readiness": 78,
        },
        4: {
            "Erotic Play Capacity": 75,
            "Sensory Range": 78,
            "Spontaneous Presence": 72,
            "Intimate Levity": 75,
            "Embodied Curiosity": 78,
        },
    },

    "restaurant_safety": {
        "Structural Safety": 62,
        "Social Safety": 72,
        "Autonomy Safety": 40,
        "Environmental Safety": 68,
        "Informational Safety": 55,
        "Relational Safety": 65,
    },

    "central_tension": (
        "Elena's map is forward-leading — her Forward cluster (63%) and "
        "Aliveness (47%) are well ahead of her Between (51%) and Self (53%). "
        "Therapy addressed orientation shame but not purity-worth fusion "
        "underneath. She can claim who she loves; she hasn't yet fully "
        "claimed her right to receive pleasure and express need. "
        "Boundary Sovereignty (42%) and Receiving Capacity (38%) are her "
        "primary bottleneck — the gatekeeper wound still running."
    ),

    "special_note": None,
}

# ─────────────────────────────────────────────
# CLIENT 4: DIANE, 52
# ─────────────────────────────────────────────
CLIENTS["diane"] = {
    "name": "Diane",
    "age": 52,
    "background": (
        "Mormon, left with husband 3 years ago. Sexual relationship dormant "
        "18 months. Husband's deconstruction significantly ahead of hers. "
        "Feels pressure to reconnect sexually before she's ready. Describes "
        "herself as 'going through the motions of leaving without actually "
        "arriving anywhere new.' Two adult children, one still active in the "
        "church."
    ),
    "entry_point": (
        "Self-referred after partner suggested they work with someone who "
        "understands religious sexual trauma. Reports feeling pressured by "
        "partner's timeline."
    ),
    "stability": 5,
    "in_therapy": True,
    "date": None,
    "gender_identity": "female",

    "shame_sources": {
        "Having desire at all": 4,
        "Specific desires or fantasies": 3,
        "Sexual history": 3,
        "Body appearance/response": 4,
        "Orientation or attractions": 2,
        "Having strong emotions": 3,
        "Doubting or leaving the system": 4,
        "Choices inside the system": 4,
        "How much I need from other people": 3,
        "Speaking up or using my voice": 4,
    },

    "clusters": {
        1: {
            "name": "Self",
            "axes": {
                "Desire Ownership": 30,
                "Arousal-Shame Decoupling": 22,
                "Pleasure Permission": 25,
                "Body Trust": 28,
                "Erotic Self-Acceptance": 24,
            },
            "body_check": DISTRESS,
        },
        2: {
            "name": "Between",
            "axes": {
                "Consent Clarity": 42,
                "Communication Capacity": 35,
                "Attachment Pattern Awareness": 48,
                "Boundary Sovereignty": 32,
                "Receiving Capacity": 30,
            },
            "body_check": SIGNIFICANT_RESISTANCE,
        },
        3: {
            "name": "Forward",
            "axes": {
                "Erotic Identity Clarity": 38,
                "Orientation & Preference Exploration": 42,
                "Conscious Exploration Capacity": 32,
                "Sexual Future Vision": 45,
                "Integration Readiness": 28,
            },
            "body_check": MILD_RESISTANCE,
        },
        4: {
            "name": "Aliveness",
            "axes": {
                "Erotic Play Capacity": 18,
                "Sensory Range": 22,
                "Spontaneous Presence": 20,
                "Intimate Levity": 15,
                "Embodied Curiosity": 20,
            },
            "body_check": DISTRESS,
        },
    },

    "vision": {
        1: {
            "Desire Ownership": 68,
            "Arousal-Shame Decoupling": 62,
            "Pleasure Permission": 65,
            "Body Trust": 65,
            "Erotic Self-Acceptance": 62,
        },
        2: {
            "Consent Clarity": 72,
            "Communication Capacity": 70,
            "Attachment Pattern Awareness": 72,
            "Boundary Sovereignty": 68,
            "Receiving Capacity": 65,
        },
        3: {
            "Erotic Identity Clarity": 70,
            "Orientation & Preference Exploration": 65,
            "Conscious Exploration Capacity": 65,
            "Sexual Future Vision": 72,
            "Integration Readiness": 62,
        },
        4: {
            "Erotic Play Capacity": 58,
            "Sensory Range": 60,
            "Spontaneous Presence": 55,
            "Intimate Levity": 55,
            "Embodied Curiosity": 58,
        },
    },

    "restaurant_safety": {
        "Structural Safety": 55,
        "Social Safety": 68,
        "Autonomy Safety": 32,
        "Environmental Safety": 58,
        "Informational Safety": 48,
        "Relational Safety": 45,
    },

    "central_tension": (
        "Diane's map shows someone in survival mode — holding four clusters "
        "in a tight, compressed shape while being asked to open sexually "
        "before the foundation exists to support it. Her lowest cluster "
        "(Aliveness at 19%) combined with Self at 26% tells us: the sexual "
        "reconnection her partner wants cannot happen safely until Diane "
        "has more of herself back. This is not resistance to intimacy. "
        "This is wisdom."
    ),

    "special_note": {
        "type": "couples_note",
        "title": "A Note for Couples Work",
        "text": (
            "Diane and her partner's maps show a significant Forward Gap — "
            "he is further along in his reclamation than she is in hers. "
            "This is not a problem to solve. It is a timing difference to "
            "honor. Pushing toward intimate reconnection before Diane's "
            "Self and Between foundations are stronger risks replicating "
            "the system's pattern — compliance rather than genuine desire. "
            "The most intimate thing her partner can do right now is wait, "
            "with her, without pressure."
        ),
    },
}


# ─────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────

def get_client(name: str) -> dict:
    """Retrieve a client by lowercase name."""
    key = name.lower().strip()
    if key not in CLIENTS:
        available = ", ".join(CLIENTS.keys())
        raise ValueError(f"Client '{name}' not found. Available: {available}")
    return CLIENTS[key]


def get_all_clients() -> dict:
    """Return all client data."""
    return CLIENTS


def get_cluster_score(client_data: dict, cluster_num: int) -> int:
    """Calculate cluster average for a client."""
    cluster = client_data["clusters"].get(cluster_num, {})
    axes = cluster.get("axes", {})
    return cluster_average(axes)


def get_all_cluster_scores(client_data: dict) -> dict:
    """Get all cluster averages."""
    return {
        num: get_cluster_score(client_data, num)
        for num in range(1, 5)
    }


def get_domain_score(client_data: dict) -> int:
    """Calculate overall sexual domain score."""
    return domain_average(client_data["clusters"])


def get_axis_score(client_data: dict, axis_name: str) -> int:
    """Get a specific axis score."""
    for cluster_data in client_data["clusters"].values():
        axes = cluster_data.get("axes", {})
        if axis_name in axes:
            return axes[axis_name]
    return 0


def get_axis_vision(client_data: dict, axis_name: str) -> int:
    """Get a specific axis vision score."""
    vision = client_data.get("vision", {})
    for cluster_vision in vision.values():
        if axis_name in cluster_vision:
            return cluster_vision[axis_name]
    return 0


def get_all_axes(client_data: dict) -> dict:
    """Get all axis scores as a flat dict."""
    result = {}
    for cluster_data in client_data["clusters"].values():
        result.update(cluster_data.get("axes", {}))
    return result


def get_all_vision(client_data: dict) -> dict:
    """Get all vision scores as a flat dict."""
    result = {}
    for cluster_vision in client_data.get("vision", {}).values():
        result.update(cluster_vision)
    return result


def get_lowest_axes(client_data: dict, n: int = 3) -> list:
    """Get the N lowest-scoring axes."""
    all_axes = get_all_axes(client_data)
    sorted_axes = sorted(all_axes.items(), key=lambda x: x[1])
    return sorted_axes[:n]


def get_highest_axes(client_data: dict, n: int = 3) -> list:
    """Get the N highest-scoring axes."""
    all_axes = get_all_axes(client_data)
    sorted_axes = sorted(all_axes.items(), key=lambda x: x[1], reverse=True)
    return sorted_axes[:n]


def get_anchor_axis(client_data: dict) -> tuple:
    """Return (axis_name, score) for the highest scoring axis."""
    all_axes = get_all_axes(client_data)
    if not all_axes:
        return ("", 0)
    best = max(all_axes.items(), key=lambda x: x[1])
    return best


def get_anchor_cluster(client_data: dict) -> tuple:
    """Return (cluster_num, cluster_name, score) for the highest cluster."""
    scores = get_all_cluster_scores(client_data)
    best_num = max(scores, key=scores.get)
    return best_num, CLUSTER_NAMES[best_num], scores[best_num]


# ─────────────────────────────────────────────
# SPINE DOMAIN SCORING
# ─────────────────────────────────────────────

def get_spine_domain_score(client_data: dict, domain_name: str) -> int:
    """Calculate SPINE domain score as average of mapped axes."""
    axes = get_all_axes(client_data)
    domain_axes = SPINE_DOMAINS[domain_name]["axes"]
    scores = [axes[a] for a in domain_axes if a in axes]
    return round(sum(scores) / len(scores)) if scores else 0


def get_all_spine_scores(client_data: dict) -> dict:
    """Get all 5 SPINE domain scores."""
    return {
        name: get_spine_domain_score(client_data, name)
        for name in SPINE_DOMAIN_ORDER
    }


def get_spine_domain_axes(client_data: dict, domain_name: str) -> dict:
    """Get {axis_name: score} for all axes in a SPINE domain."""
    axes = get_all_axes(client_data)
    domain_axes = SPINE_DOMAINS[domain_name]["axes"]
    return {a: axes[a] for a in domain_axes if a in axes}


def get_spine_vision_scores(client_data: dict) -> dict:
    """Get SPINE domain vision score averages."""
    vision = get_all_vision(client_data)
    result = {}
    for name in SPINE_DOMAIN_ORDER:
        domain_axes = SPINE_DOMAINS[name]["axes"]
        scores = [vision[a] for a in domain_axes if a in vision]
        result[name] = round(sum(scores) / len(scores)) if scores else 0
    return result


def get_lowest_spine_domain(client_data: dict) -> tuple:
    """Return (domain_name, score) for the lowest SPINE domain."""
    scores = get_all_spine_scores(client_data)
    lowest = min(scores, key=scores.get)
    return lowest, scores[lowest]


def get_highest_spine_domain(client_data: dict) -> tuple:
    """Return (domain_name, score) for the highest SPINE domain."""
    scores = get_all_spine_scores(client_data)
    highest = max(scores, key=scores.get)
    return highest, scores[highest]


def get_anchor_spine_domain(client_data: dict) -> tuple:
    """Return (domain_name, score, letter) for the anchor SPINE domain."""
    name, score = get_highest_spine_domain(client_data)
    return name, score, SPINE_DOMAINS[name]["letter"]
