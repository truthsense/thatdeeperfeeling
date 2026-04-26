"""
SPINE Framework — Narrative Generator
Generates personalized narratives, active edges, aliveness sections,
waypoint narratives, practice prescriptions, and priority stacks.
SPINE 5-domain model as primary architecture with sexual domain clusters
as mapping layer.
"""

from clients_data import (
    HEALING, PATTERN, RESOURCING,
    CLUSTER_NAMES, CLUSTER_AXES,
    SPINE_DOMAIN_ORDER, SPINE_DOMAINS, AXIS_TO_SPINE,
    get_all_axes, get_all_cluster_scores, get_cluster_score,
    get_all_spine_scores, get_highest_spine_domain,
    get_lowest_spine_domain, get_spine_domain_axes,
    get_lowest_axes, get_highest_axes, get_anchor_axis,
    get_anchor_cluster, get_stage, cluster_average,
)
from scoring_tools import (
    gap_score, spine_gap_score, pendulum_risk, sequencing_recommendation,
)
from waypoints import get_next_milestone_narrative


# ─────────────────────────────────────────────
# GAP PROFILE FRAMES
# ─────────────────────────────────────────────

GAP_PROFILE_FRAMES = {
    "embodiment_deficit": (
        "Your SPINE reveals a head-body split — Identity and Power are "
        "significantly ahead of Embodiment at {embodiment}%. You know things "
        "your body hasn't learned yet. This is the most common pattern in "
        "post-HDR clients who did intellectual deconstruction work first. "
        "The mind arrived somewhere the nervous system hasn't. "
        "The work starts in the Embodiment vertebra."
    ),
    "sovereignty_wound": (
        "Your SPINE reveals a sovereignty wound — Embodiment and Power may "
        "have some ground, but Sovereignty at {sovereignty}% tells us: "
        "your capacity to own your own desire, arousal, and erotic selfhood "
        "was the system's primary target. The work starts with reclaiming "
        "the right to want."
    ),
    "power_compression": (
        "Your SPINE reveals a power gap — Power at {power}% is lagging "
        "behind your other vertebrae. Self-knowledge and body awareness "
        "are ahead of your capacity to bring them into relationship. "
        "You know who you are; you haven't yet learned to be that person "
        "with someone else in the room."
    ),
    "nourishment_blocked": (
        "Your SPINE reveals blocked nourishment — Nourishment at "
        "{nourishment}% tells us the system shut down your capacity to "
        "receive and enjoy. Pleasure, receiving, and play were made "
        "dangerous or earned-only. The work starts with permission "
        "to receive something good without paying for it."
    ),
    "identity_searching": (
        "Your SPINE reveals an identity gap — Identity at {identity}% "
        "is still forming. The system defined you before you could define "
        "yourself, and the vision of who you're becoming in this territory "
        "is still emerging."
    ),
    "compressed": (
        "Your SPINE is compressed — all five vertebrae held tight and low, "
        "none significantly ahead of the others. This isn't scattered damage. "
        "This is what happens when the system's reach was total and thorough. "
        "The spine was prevented from forming everywhere simultaneously. "
        "Everything starts at the foundation."
    ),
    "balanced": (
        "Your SPINE is relatively balanced — all vertebrae within a close "
        "range, suggesting broad development rather than a single concentrated "
        "wound. The work can proceed on multiple fronts simultaneously."
    ),
    "mixed": (
        "Your SPINE has a unique shape that doesn't fit a standard profile. "
        "The vertebrae show an individualized pattern of development that "
        "tells us something specific about how the system impacted you. "
        "The prescription is tailored to your particular architecture."
    ),
}


# ─────────────────────────────────────────────
# EDGE INVITATIONS (per-axis invitations for active edges)
# ─────────────────────────────────────────────

EDGE_INVITATIONS = {
    "Desire Ownership": (
        "Your desire is waking up — but the chaperone is still in the room. "
        "The old system taught you that wanting was dangerous. At {score}%, "
        "you're learning to let a want exist for three seconds before the "
        "explanation arrives. That pause is the whole shift."
    ),
    "Arousal-Shame Decoupling": (
        "Arousal and shame are still fused at {score}%. One arrives and the "
        "other follows within seconds. The work here isn't eliminating shame — "
        "it's building a gap between the sensation and the verdict."
    ),
    "Pleasure Permission": (
        "At {score}%, pleasure still requires justification. The system taught "
        "you that good things are earned, not received. The work here is "
        "sixty seconds of something genuinely pleasurable with nothing "
        "required of it."
    ),
    "Body Trust": (
        "At {score}%, your body is still more stranger than home. You were "
        "trained to override its signals, ignore its wisdom, distrust its "
        "responses. The work here is learning to notice what it tells you — "
        "without immediately overriding the message."
    ),
    "Erotic Self-Acceptance": (
        "At {score}%, acknowledging your erotic self still triggers the old "
        "revulsion circuits. There is a sexual being in you. The work here "
        "is letting that sentence exist without flinching."
    ),
    "Consent Clarity": (
        "At {score}%, the system's binary — comply or rebel — is still "
        "running underneath. The work here is discovering the spectrum: "
        "your body has a yes, a no, and a maybe. Learning the difference "
        "between them is the practice."
    ),
    "Communication Capacity": (
        "At {score}%, saying something true out loud still feels dangerous. "
        "The system trained silence or performance. The work here is one "
        "true sentence, spoken without managing the listener's response."
    ),
    "Attachment Pattern Awareness": (
        "At {score}%, the pattern is running but visible. You can start to "
        "see the grab, the withdrawal, the performance. Naming the pattern "
        "isn't pathologizing yourself — it's reading your own map."
    ),
    "Boundary Sovereignty": (
        "At {score}%, boundaries still feel like selfishness. The system "
        "taught that good people don't have edges. One small no — without "
        "retracting it when the guilt arrives — is the practice."
    ),
    "Receiving Capacity": (
        "At {score}%, receiving creates debt, obligation, vulnerability. "
        "The work here is letting something good land — a compliment, a "
        "gift, a kind word — without immediately giving something back."
    ),
    "Erotic Identity Clarity": (
        "At {score}%, you're sensing there's a you underneath the system's "
        "definition. Not knowing who yet. Just knowing there's someone to "
        "discover. That sensing is the work."
    ),
    "Orientation & Preference Exploration": (
        "At {score}%, attractions still trigger the alarm bells. The work "
        "here is noticing what draws you without moral panic — not acting "
        "on it, just noticing, without emergency."
    ),
    "Conscious Exploration Capacity": (
        "At {score}%, trying something new still feels like a test with a "
        "grade attached. The work here is one small experiment experienced "
        "as curiosity rather than exam."
    ),
    "Sexual Future Vision": (
        "At {score}%, the sexual future still looks like the past — either "
        "the system's version or a reaction against it. The work here is "
        "imagining something else entirely. Even blurry counts."
    ),
    "Integration Readiness": (
        "At {score}%, the old binaries are still running — good/bad, "
        "pure/impure. The work here is holding two truths at once: "
        "this was harmful AND those people loved me. Both simultaneously."
    ),
    "Erotic Play Capacity": (
        "At {score}%, intimacy is still serious business — high stakes, "
        "cosmic consequences. The work here is discovering that laughter "
        "belongs in intimate space. That lightness is intimate."
    ),
    "Sensory Range": (
        "At {score}%, the sensory world has been narrowed to a few "
        "approved channels. The work here is noticing that pleasure lives "
        "in more places than you were taught."
    ),
    "Spontaneous Presence": (
        "At {score}%, being fully in your body still triggers the old "
        "surveillance response. The work here is thirty seconds of "
        "actually being here — not planning, not monitoring. Just: here."
    ),
    "Intimate Levity": (
        "At {score}%, joy still has a tax — good things are suspect, "
        "lightness is shallow. The work here is one moment of genuine "
        "lightness that doesn't come with a bill."
    ),
    "Embodied Curiosity": (
        "At {score}%, curiosity about the body has been shut down. "
        "The work here is a genuine 'I wonder...' about your own body. "
        "The question itself is the beginning."
    ),
}


# ─────────────────────────────────────────────
# PER-CLIENT NARRATIVES
# ─────────────────────────────────────────────

NARRATIVES = {
    "sarah": {
        "reading_your_shape": (
            "Your SPINE reveals a pattern we see often: Identity at 60% "
            "and Power at 60% are well-developed — you know who you are and "
            "you can communicate. But Sovereignty at 38% and Embodiment at "
            "30% tell the deeper story. Body Trust at 24%, Pleasure "
            "Permission at 28%, Arousal-Shame Decoupling at 32% — these "
            "aren't deficits. They're the exact vertebrae where the system "
            "installed its deepest code.\n\n"
            "There is a 30-point gap between your Identity and your "
            "Embodiment. You know things your body hasn't learned yet. "
            "The dissociation during intimacy isn't weakness — it's your "
            "nervous system solving a problem with the only tool it was "
            "given: leaving. The work is not to force staying. It's to "
            "make staying safe."
        ),
        "anchor_acknowledgment": (
            "Identity is your anchor vertebra — Erotic Identity Clarity at "
            "76% and Attachment Pattern Awareness at 72% are the strongest "
            "points on your SPINE. Four years of deconstruction and good "
            "therapy built something real here. When the Embodiment work "
            "feels overwhelming or the Sovereignty shame gets loud, this "
            "is where you return. You know who you are. Now we help the "
            "rest of your spine catch up."
        ),
        "closing": (
            "Sarah, your body isn't broken. It's protecting you with the "
            "tools it was given. The dissociation, the shutdown, the shame "
            "spiral — these are your nervous system's best attempts at "
            "keeping you intact inside a system that made your body someone "
            "else's territory.\n\n"
            "The work ahead is not dramatic. It's almost embarrassingly "
            "small. One minute of presence. One hand on your body. One "
            "breath that says: I live here. Do that enough times and the "
            "Embodiment vertebra starts to strengthen.\n\n"
            "Your Identity already arrived. Now we help Sovereignty and "
            "Embodiment find their way home."
        ),
    },
    "marcus": {
        "reading_your_shape": (
            "Your SPINE is compressed — all five domains held tight and low, "
            "none significantly ahead. Sovereignty at 24%, Nourishment at 21%, "
            "Embodiment at 14%, Power at 30%, Identity at 27%. This isn't "
            "scattered damage. This is what happens when the system's reach "
            "was total.\n\n"
            "The shame scores confirm it: 5 out of 5 on desire, fantasies, "
            "sexual history, and leaving. The system taught you that your "
            "sexuality was a beast to cage. That framing lives in your body "
            "now as a pendulum — total suppression swinging to compulsive "
            "overcorrection and back. Neither position is you. The real you "
            "is somewhere in the middle, in the space the swing never stops "
            "long enough to find.\n\n"
            "We don't start by challenging the cage. We start with Embodiment — "
            "finding ground to stand on."
        ),
        "anchor_acknowledgment": (
            "Consent Clarity at 38% is your relative anchor — the highest "
            "point on a compressed SPINE. Even in a system designed to erase "
            "your agency, something in you held onto the knowledge that "
            "choice matters. That's your Power vertebra, holding. "
            "It's not much ground yet. But it's ground. We build from here."
        ),
        "closing": (
            "Marcus, everything starts at the foundation. Your map doesn't "
            "need five plans — it needs one solid starting point. Daily Return, "
            "twice a day, hands on your body, 60 seconds. Not to fix anything. "
            "Not to overcome anything. Just to find out what it's like to be "
            "in your body without it being a battleground.\n\n"
            "The pendulum will slow. Not because you force it, but because "
            "you build the middle ground it's been swinging over. "
            "One breath at a time. With a therapist alongside you."
        ),
    },
    "elena": {
        "reading_your_shape": (
            "Your SPINE reveals Identity as the vertebra therapy built — "
            "at 63%, it's your strongest domain. Erotic Identity Clarity "
            "at 72% and Orientation & Preference Exploration at 68% prove "
            "the orientation work landed. But underneath it, your Nourishment "
            "vertebra at 44% and Embodiment at 47% tell the deeper story.\n\n"
            "Receiving Capacity at 38% and Boundary Sovereignty at 42% are "
            "your primary bottleneck — the gatekeeper wound still running "
            "in your Power vertebra at 54%. You can claim who you love. You "
            "haven't yet fully claimed your right to receive pleasure and "
            "express need. The over-pleasing isn't random. It's your nervous "
            "system trying to prevent another total loss by managing everyone's "
            "experience of you before they decide you're too much."
        ),
        "anchor_acknowledgment": (
            "Identity is your anchor vertebra — at 63%, it's the strongest "
            "point on your SPINE. Erotic Identity Clarity at 72% is the peak. "
            "Coming out at 24 and building a life from that truth took real "
            "courage. When the need-shame surfaces or the over-pleasing pulls, "
            "your Identity vertebra reminds you: you already chose yourself "
            "once. You can do it again."
        ),
        "closing": (
            "Elena, your Identity vertebra at 63% proves you know how to "
            "choose yourself. The next edge is your Nourishment vertebra — "
            "Receiving Capacity at 38%, learning that your needs aren't too "
            "much. That you can take up space in a relationship without "
            "earning it first.\n\n"
            "Start with the Body No. One small refusal a day, felt in the "
            "body. Let your 'yes' start to mean something because 'no' is "
            "available. As your Power vertebra strengthens, the over-pleasing "
            "will quiet down — not because you force it, but because you no "
            "longer need it to keep you safe."
        ),
    },
    "diane": {
        "reading_your_shape": (
            "Your SPINE is compressed and low — Embodiment at 21%, "
            "Nourishment at 24%, Sovereignty at 25%, Identity at 37%, "
            "Power at 39%. Every vertebra is asking for attention, and "
            "you're being asked to open sexually before the foundation "
            "exists to support it.\n\n"
            "Embodiment at 21% combined with Sovereignty at 25% tells us: "
            "the sexual reconnection your partner wants cannot happen safely "
            "until you have more of yourself back. The sexual dormancy isn't "
            "a problem to fix. It's your system's way of protecting you until "
            "the foundation is stronger. Distress body checks in Embodiment "
            "and Sovereignty confirm it — your body is saying 'not yet' and "
            "that response deserves to be honored, not overridden."
        ),
        "anchor_acknowledgment": (
            "Power is your anchor vertebra — at 39%, it's the strongest "
            "point on your SPINE. Attachment Pattern Awareness at 48% is "
            "the peak. There's a part of you that sees the relational "
            "patterns clearly, even when you can't yet change them. That "
            "seeing is not nothing. It's your Power vertebra, holding. "
            "It's where we'll build from."
        ),
        "closing": (
            "Diane, your body's 'not yet' is not resistance — it's wisdom. "
            "Your SPINE gives you a place to stand while the foundation "
            "strengthens underneath. Start with Daily Return. Let your "
            "Embodiment vertebra know it belongs to you before asking it "
            "to open to anyone else.\n\n"
            "The reconnection your partnership needs starts here — not in the "
            "bedroom, but in your own hands, on your own body, with your own "
            "breath. As Sovereignty and Embodiment strengthen, the rest of "
            "your SPINE will follow."
        ),
    },
}


# ─────────────────────────────────────────────
# PUBLIC FUNCTIONS
# ─────────────────────────────────────────────

def get_narrative(client_data):
    """Get narrative sections for a client."""
    key = client_data["name"].lower()
    if key in NARRATIVES:
        return NARRATIVES[key]

    # Fallback: generate from SPINE gap profile
    spine_data = spine_gap_score(client_data)
    profile = spine_data["spine_gap_profile"]
    spine_scores = get_all_spine_scores(client_data)

    frame = GAP_PROFILE_FRAMES.get(profile, GAP_PROFILE_FRAMES["mixed"])
    reading = frame.format(
        sovereignty=spine_scores.get("Sovereignty", 0),
        power=spine_scores.get("Power", 0),
        identity=spine_scores.get("Identity", 0),
        nourishment=spine_scores.get("Nourishment", 0),
        embodiment=spine_scores.get("Embodiment", 0),
    )

    anchor_domain, anchor_score = get_highest_spine_domain(client_data)
    anchor_axis_name, anchor_axis_score = get_anchor_axis(client_data)
    anchor_text = (
        f"{anchor_domain} is your anchor vertebra — at {anchor_score}%, "
        f"it's the strongest point on your SPINE. {anchor_axis_name} at "
        f"{anchor_axis_score}% is the peak. This is your resource when "
        f"the rest of the work gets hard. You built something real here."
    )

    lowest_domain, lowest_score = get_lowest_spine_domain(client_data)

    return {
        "reading_your_shape": reading,
        "anchor_acknowledgment": anchor_text,
        "closing": (
            f"Your {anchor_domain} vertebra at {anchor_score}% is real. "
            f"Start where the ground is most solid and build from there. "
            f"As {lowest_domain} strengthens, the rest of your SPINE will "
            f"follow. The work ahead is not dramatic — it's almost "
            f"embarrassingly small. And that's exactly why it works."
        ),
    }


def get_priority_stack(client_data):
    """
    Determine priority order based on cluster scores and mechanisms.
    Returns list of priority dicts with cluster, score, category, explanation.
    """
    cluster_scores = get_all_cluster_scores(client_data)
    axes = get_all_axes(client_data)
    low_axes = get_lowest_axes(client_data, 5)
    c1 = cluster_scores[1]

    priorities = []

    # 1. Foundation: any Cluster 1 axis < 30%
    c1_axes = client_data["clusters"][1]["axes"]
    has_critical = any(v < 30 for v in c1_axes.values())
    if has_critical or c1 < 35:
        priorities.append({
            "level": "Foundation",
            "cluster": 1,
            "cluster_name": "Self",
            "score": c1,
            "category": HEALING,
            "explanation": (
                f"Cluster 1 (Self) at {c1}% — below safety threshold. "
                f"ALL initial work focuses here. The body must become safe "
                f"ground before other work can hold."
            ),
            "weeks": "1-4",
        })

    # 2. Lowest non-C1 clusters
    for c in sorted(range(2, 5), key=lambda x: cluster_scores[x]):
        if len(priorities) >= 4:
            break
        score = cluster_scores[c]
        name = CLUSTER_NAMES[c]
        stage = get_stage(score)

        if score < 40:
            cat = HEALING
        elif score < 55:
            cat = PATTERN
        else:
            cat = RESOURCING

        priorities.append({
            "level": "Primary" if len(priorities) <= 1 else "Secondary",
            "cluster": c,
            "cluster_name": name,
            "score": score,
            "category": cat,
            "explanation": (
                f"Cluster {c} ({name}) at {score}% ({stage}). "
                f"This territory needs attention."
            ),
            "weeks": f"{len(priorities) * 2 + 1}-8",
        })

    return priorities[:4]


def generate_active_edges(client_data, n=3):
    """
    Return the N lowest-scoring axes with invitation narratives.
    These are the client's "active edges" — where the work lives.
    """
    low_axes = get_lowest_axes(client_data, n)
    edges = []

    for axis_name, score in low_axes:
        stage = get_stage(score)
        invitation_template = EDGE_INVITATIONS.get(axis_name, "")

        if invitation_template:
            invitation = invitation_template.format(score=score)
        else:
            invitation = (
                f"At {score}%, this axis is asking for attention. "
                f"The work here is foundational and specific."
            )

        edges.append({
            "axis": axis_name,
            "score": score,
            "stage": stage,
            "invitation": invitation,
        })

    return edges


def generate_aliveness_narrative(client_data):
    """
    Generate Cluster 4 (Aliveness) narrative with warm, mischievous tone.
    Three tiers based on cluster average: <35%, 35-55%, >55%.
    """
    c4_score = get_cluster_score(client_data, 4)
    c4_axes = client_data["clusters"][4]["axes"]
    lowest_axis = min(c4_axes, key=c4_axes.get)
    lowest_score = c4_axes[lowest_axis]
    highest_axis = max(c4_axes, key=c4_axes.get)
    highest_score = c4_axes[highest_axis]

    if c4_score < 35:
        # Tier 1: Deep suppression
        return (
            f"Aliveness at {c4_score}%. Let's be honest about what that "
            f"means: the system shut down your capacity for uncomplicated "
            f"pleasure. Play, spontaneity, lightness — these were luxuries "
            f"at best, sins at worst. Your nervous system learned that joy "
            f"is borrowed time. That good things are followed by consequences.\n\n"
            f"{lowest_axis} at {lowest_score}% is where the suppression is "
            f"deepest. But here's the thing — this isn't the last cluster "
            f"on the list because it's least important. It's here because "
            f"it's what everything else is building toward. The capacity "
            f"to enjoy being alive. Not to earn aliveness. Not to perform "
            f"it. To actually feel it.\n\n"
            f"The first work here is almost embarrassingly small: one "
            f"minute of something genuinely pleasurable, with nothing "
            f"required of it. No meaning. No significance. Just: this is "
            f"good, and that is allowed."
        )
    elif c4_score <= 55:
        # Tier 2: Emerging
        return (
            f"Aliveness at {c4_score}%. Something is stirring here — the "
            f"emergency state is loosening its grip. {highest_axis} at "
            f"{highest_score}% tells us there's a part of you that "
            f"remembers what it's like to be uncomplicated about pleasure.\n\n"
            f"The work here is expanding what's already happening. More "
            f"range. More permission. More of the moments where you "
            f"catch yourself enjoying something without immediately "
            f"checking if it's allowed. Those moments are the data. "
            f"Follow them."
        )
    else:
        # Tier 3: Active
        return (
            f"Aliveness at {c4_score}%. Now we're getting somewhere "
            f"interesting. The emergency state has loosened enough for "
            f"genuine play, curiosity, and spontaneity to show up "
            f"without apology.\n\n"
            f"{highest_axis} at {highest_score}% is leading the way. "
            f"Let it. This cluster doesn't need heavy work — it needs "
            f"invitation. More play. More lightness. More of the "
            f"uncomplicated pleasure that the system tried to make "
            f"impossible. You're proving it wrong."
        )


def generate_waypoint_narratives(client_data):
    """
    Generate waypoint narratives for the client's lowest axes.
    Returns list of dicts with axis, score, next_milestone, next_threshold, narrative.
    """
    low_axes = get_lowest_axes(client_data, 5)
    waypoints = []

    for axis_name, score in low_axes:
        wp = get_next_milestone_narrative(axis_name, score)
        if wp:
            waypoints.append(wp)

    return waypoints[:4]


def get_practices_for_report(client_data):
    """
    Select 3 practices for the report based on client data.
    Uses sequencing_recommendation and practices catalog.
    """
    from practices import PRACTICES

    seq = sequencing_recommendation(client_data)
    selected_keys = [p["key"] for p in seq["practices"]]

    # Pick top 3 from sequencing recommendation
    result = []
    for practice_info in seq["practices"][:3]:
        key = practice_info["key"]
        practice = PRACTICES.get(key)
        if not practice:
            continue

        result.append({
            "key": key,
            "name": practice["name"],
            "category": practice["category"],
            "weeks": practice["weeks"],
            "client_text": practice["client_text"],
            "what_youll_notice": practice["what_youll_notice"],
            "why_for_you": _generate_why(practice, client_data),
        })

    # If fewer than 3, pad with foundational practices
    if len(result) < 3:
        fallbacks = ["daily_return", "pleasure_minute", "the_lighthouse"]
        for fb_key in fallbacks:
            if len(result) >= 3:
                break
            if fb_key in selected_keys:
                continue
            practice = PRACTICES.get(fb_key)
            if practice:
                result.append({
                    "key": fb_key,
                    "name": practice["name"],
                    "category": practice["category"],
                    "weeks": practice["weeks"],
                    "client_text": practice["client_text"],
                    "what_youll_notice": practice["what_youll_notice"],
                    "why_for_you": _generate_why(practice, client_data),
                })

    return result[:3]


def _generate_why(practice, client_data):
    """Generate personalized 'why this for you' text."""
    name = client_data["name"]
    axes = get_all_axes(client_data)
    target_axes = practice.get("target_axes", [])

    if not target_axes:
        return f"This practice supports your foundational work."

    # Find lowest targeted axis
    targeted_scores = [
        (a, axes.get(a, 50)) for a in target_axes if a in axes
    ]
    if not targeted_scores:
        return f"This practice supports your foundational work."

    lowest = min(targeted_scores, key=lambda x: x[1])
    axis_name, score = lowest

    why_templates = {
        "daily_return": (
            f"Body Trust at {score}% tells us your body doesn't yet feel "
            f"like home. This practice rebuilds that foundation — one "
            f"breath at a time, twice a day, until your body starts to "
            f"expect you."
        ),
        "the_lighthouse": (
            f"Pleasure Permission at {score}% means pleasure has been "
            f"shut down or made dangerous. This practice teaches your "
            f"nervous system that noticing good things is safe."
        ),
        "witnessed_voice": (
            f"Communication Capacity at {score}% means your truth has "
            f"been living inside without sound. This practice gives it "
            f"air — privately, safely, on your terms."
        ),
        "the_watchtower": (
            f"Arousal-Shame Decoupling at {score}% suggests shame is "
            f"still running the show. This practice builds the sorting "
            f"mechanism — whose shame is this, actually?"
        ),
        "mirror_voice": (
            f"{axis_name} at {score}% means the connection between "
            f"knowing and speaking has been interrupted. This practice "
            f"rebuilds the bridge — eyes, voice, truth."
        ),
        "the_deed": (
            f"{axis_name} at {score}% suggests you're still waiting for "
            f"permission that isn't coming. This practice builds the "
            f"muscle of choosing for yourself."
        ),
        "body_no": (
            f"Boundary Sovereignty at {score}% means 'no' hasn't been "
            f"safe. This practice locates refusal in the body so it "
            f"becomes available when you need it."
        ),
        "pleasure_minute": (
            f"Pleasure Permission at {score}% means the body has learned "
            f"to bypass sensation. Sixty seconds of focused pleasure "
            f"begins the re-introduction."
        ),
        "want_before_why": (
            f"Desire Ownership at {score}% tells us your wants have been "
            f"filtered through 'should' for so long they've gone quiet. "
            f"This practice turns the volume back up."
        ),
        "origin_question": (
            f"{axis_name} at {score}% — the system defined this territory "
            f"before you could. This practice reclaims the origin story."
        ),
        "arrival_practice": (
            f"Spontaneous Presence at {score}% means arriving in your "
            f"body still triggers the surveillance response. This practice "
            f"makes landing safe."
        ),
        "the_laboratory": (
            f"Conscious Exploration Capacity at {score}% — trying new "
            f"things still feels like a test. This practice reframes "
            f"exploration as experiment, not exam."
        ),
        "return_letter": (
            f"Integration Readiness at {score}% — the past and present "
            f"selves haven't met yet. This practice begins the "
            f"introduction."
        ),
    }

    practice_key = practice.get("key", "")
    # Try to find key from practice name
    if not practice_key:
        from practices import PRACTICES
        for k, p in PRACTICES.items():
            if p["name"] == practice["name"]:
                practice_key = k
                break

    template = why_templates.get(practice_key)
    if template:
        return template

    return (
        f"{axis_name} at {score}% is where this practice does its work. "
        f"It addresses the specific pattern the system installed here."
    )
