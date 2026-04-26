"""
SPINE Framework — Waypoint System
Three milestones per axis: First Threshold, Activation Point, Integration Point.
Each waypoint has unlock chains, narratives, and detection logic.
"""

from clients_data import (
    CLUSTER_AXES, CLUSTER_NAMES, AXIS_TO_SPINE,
    get_all_axes, get_all_cluster_scores,
    get_cluster_score, get_stage, cluster_average,
)


# ─────────────────────────────────────────────
# WAYPOINT DEFINITIONS
# ─────────────────────────────────────────────

WAYPOINTS = {
    # ── CLUSTER 1: SELF ──────────────────────
    "Desire Ownership": {
        "cluster": 1,
        "milestones": [
            {
                "name": "First Threshold",
                "threshold": 35,
                "description": "You can name a want without immediately qualifying it.",
                "unlocks": ["The Lighthouse practice becomes available"],
                "narrative": (
                    "Right now desire arrives with a chaperone — justification, "
                    "apology, or silence. The first threshold is the moment you "
                    "notice a want and let it exist for three seconds before the "
                    "explanation arrives. That pause is the whole shift."
                ),
            },
            {
                "name": "Activation Point",
                "threshold": 55,
                "description": "Desire can be spoken to another person without collapse.",
                "unlocks": ["Witnessed Voice practice deepens", "Partner communication exercises"],
                "narrative": (
                    "Desire has moved from private flicker to something you can "
                    "hold in conversation. You can say 'I want' without the "
                    "ground disappearing. The want doesn't have to be honored — "
                    "it just has to be speakable."
                ),
            },
            {
                "name": "Integration Point",
                "threshold": 75,
                "description": "Desire is a trusted navigational signal.",
                "unlocks": ["Full erotic exploration capacity", "Advanced intimacy practices"],
                "narrative": (
                    "Desire is no longer a visitor requiring permission. It lives "
                    "here. You consult it the way you consult hunger or fatigue — "
                    "as reliable information about what you need."
                ),
            },
        ],
    },
    "Arousal-Shame Decoupling": {
        "cluster": 1,
        "milestones": [
            {
                "name": "First Threshold",
                "threshold": 30,
                "description": "You can notice arousal without immediate shame spiral.",
                "unlocks": ["Body-awareness practices deepen"],
                "narrative": (
                    "Arousal and shame are still fused — one arrives and the other "
                    "follows within seconds. The first threshold is a gap between "
                    "them. Not the absence of shame, just a pause before it lands. "
                    "That pause is where the work lives."
                ),
            },
            {
                "name": "Activation Point",
                "threshold": 50,
                "description": "Arousal can be present without moral emergency.",
                "unlocks": ["Pleasure Minute expands", "Sensory exploration practices"],
                "narrative": (
                    "The shame still visits, but it no longer runs the room. "
                    "Arousal can exist as sensation — interesting, sometimes "
                    "welcome, sometimes not — without triggering the old "
                    "emergency broadcast system."
                ),
            },
            {
                "name": "Integration Point",
                "threshold": 70,
                "description": "Arousal is experienced as morally neutral body information.",
                "unlocks": ["Full sensory and erotic range available"],
                "narrative": (
                    "Arousal is just a body signal now — no more morally loaded "
                    "than hunger or sleepiness. It can be followed, paused, or "
                    "set aside without drama. The fusion is broken."
                ),
            },
        ],
    },
    "Pleasure Permission": {
        "cluster": 1,
        "milestones": [
            {
                "name": "First Threshold",
                "threshold": 30,
                "description": "You can receive one minute of uncomplicated pleasure.",
                "unlocks": ["Pleasure Minute practice"],
                "narrative": (
                    "The system taught you that pleasure was earned, dangerous, or "
                    "selfish. The first threshold is sixty seconds of something "
                    "genuinely pleasurable — warm water, a texture, a taste — "
                    "without the tax. Without needing to deserve it first."
                ),
            },
            {
                "name": "Activation Point",
                "threshold": 50,
                "description": "Pleasure can be sought without guilt as default response.",
                "unlocks": ["Extended sensory practices", "Erotic self-exploration"],
                "narrative": (
                    "You're starting to reach for good things instead of waiting "
                    "for them to be granted. The guilt may still whisper, but "
                    "it no longer has veto power over what your body wants."
                ),
            },
            {
                "name": "Integration Point",
                "threshold": 75,
                "description": "Pleasure is a legitimate need, not an indulgence.",
                "unlocks": ["Full pleasure range", "Advanced erotic practices"],
                "narrative": (
                    "Pleasure belongs in your life the way rest does — not as "
                    "reward but as requirement. You no longer need to justify "
                    "the good things. They're just yours."
                ),
            },
        ],
    },
    "Body Trust": {
        "cluster": 1,
        "milestones": [
            {
                "name": "First Threshold",
                "threshold": 30,
                "description": "You can feel sensation without immediately overriding it.",
                "unlocks": ["Daily Return deepens", "Somatic check-in practices"],
                "narrative": (
                    "Your body has been sending signals for years that you were "
                    "trained to ignore. The first threshold is simply noticing "
                    "one — a tension, a warmth, a contraction — and letting it "
                    "stay. Not fixing it. Not interpreting it. Just: there it is."
                ),
            },
            {
                "name": "Activation Point",
                "threshold": 50,
                "description": "Body signals inform decisions alongside thoughts.",
                "unlocks": ["Somatic consent practices", "Body-led exploration"],
                "narrative": (
                    "Your body has become a source of information you actually "
                    "use. Not the only source — but a real one. When something "
                    "feels wrong in your gut, you pause. When something feels "
                    "right, you notice that too."
                ),
            },
            {
                "name": "Integration Point",
                "threshold": 75,
                "description": "The body is home — a trusted place to live.",
                "unlocks": ["Full somatic integration", "Embodied intimacy"],
                "narrative": (
                    "You live here now. Not visiting your body from somewhere "
                    "above it, not managing it from the outside. Living in it. "
                    "It's not perfect — it was never going to be — but it's yours "
                    "and you trust what it tells you."
                ),
            },
        ],
    },
    "Erotic Self-Acceptance": {
        "cluster": 1,
        "milestones": [
            {
                "name": "First Threshold",
                "threshold": 35,
                "description": "You can acknowledge having an erotic self without disgust.",
                "unlocks": ["Mirror Voice practice", "Self-reflection exercises"],
                "narrative": (
                    "There is a sexual being in you. The first threshold is "
                    "saying that sentence without flinching. Not celebrating "
                    "it yet — just allowing it to be true without the old "
                    "revulsion arriving to shut it down."
                ),
            },
            {
                "name": "Activation Point",
                "threshold": 55,
                "description": "Your erotic self can be explored with curiosity.",
                "unlocks": ["Erotic identity exploration", "Fantasy without shame work"],
                "narrative": (
                    "Curiosity has replaced disgust. You can wonder about your "
                    "own desires, notice what draws you, explore what you like — "
                    "not from a place of performance but genuine interest in "
                    "who you actually are in this territory."
                ),
            },
            {
                "name": "Integration Point",
                "threshold": 75,
                "description": "Your erotic self is an integrated part of your identity.",
                "unlocks": ["Full erotic identity integration"],
                "narrative": (
                    "This isn't a separate self anymore — compartmentalized, "
                    "hidden, or performed. Your erotic self is just part of you, "
                    "the way your humor is, or your intelligence. Present. "
                    "Integrated. Yours."
                ),
            },
        ],
    },

    # ── CLUSTER 2: BETWEEN ───────────────────
    "Consent Clarity": {
        "cluster": 2,
        "milestones": [
            {
                "name": "First Threshold",
                "threshold": 40,
                "description": "You can distinguish between yes, no, and maybe in your body.",
                "unlocks": ["Body No practice", "Consent awareness exercises"],
                "narrative": (
                    "For years, the system only had two positions: comply or "
                    "rebel. The first threshold is discovering there's a spectrum — "
                    "that your body has a yes, a no, and a maybe, and each one "
                    "feels different. Learning that difference is the work."
                ),
            },
            {
                "name": "Activation Point",
                "threshold": 60,
                "description": "Consent is a real-time process, not a one-time decision.",
                "unlocks": ["Dynamic consent practices", "Partner communication tools"],
                "narrative": (
                    "Consent has become a living thing — something you check in "
                    "with during, not just before. You can feel your yes shift "
                    "to a maybe and say so. That's not failure. That's mastery."
                ),
            },
            {
                "name": "Integration Point",
                "threshold": 80,
                "description": "Consent is embodied, fluid, and naturally communicated.",
                "unlocks": ["Advanced relational intimacy"],
                "narrative": (
                    "Your yes is full and your no is clean. Consent isn't a "
                    "negotiation anymore — it's a conversation your body has "
                    "learned to have in real time, with honesty and without fear."
                ),
            },
        ],
    },
    "Communication Capacity": {
        "cluster": 2,
        "milestones": [
            {
                "name": "First Threshold",
                "threshold": 35,
                "description": "You can name what you feel to another person.",
                "unlocks": ["Witnessed Voice practice"],
                "narrative": (
                    "The first threshold is saying something true out loud to "
                    "another person — not performing, not managing their reaction, "
                    "just: this is what I feel. The words don't have to be perfect. "
                    "They just have to be yours."
                ),
            },
            {
                "name": "Activation Point",
                "threshold": 55,
                "description": "You can express needs and boundaries in intimate contexts.",
                "unlocks": ["Partner dialogue practices", "Intimate communication tools"],
                "narrative": (
                    "Communication has entered the bedroom — and the difficult "
                    "conversations, and the vulnerable moments. You can say what "
                    "you need where it matters most, even when your voice shakes."
                ),
            },
            {
                "name": "Integration Point",
                "threshold": 75,
                "description": "Communication is a relational strength.",
                "unlocks": ["Advanced couples communication", "Conflict as connection"],
                "narrative": (
                    "Your voice has become one of your most intimate tools. "
                    "You can say hard things with care, receive hard things "
                    "without collapse, and stay present in conversations that "
                    "used to send you running."
                ),
            },
        ],
    },
    "Attachment Pattern Awareness": {
        "cluster": 2,
        "milestones": [
            {
                "name": "First Threshold",
                "threshold": 40,
                "description": "You can name your attachment pattern without judgment.",
                "unlocks": ["The Watchtower practice"],
                "narrative": (
                    "You're starting to see the pattern — how you reach for "
                    "connection, what happens when it's threatened, where you "
                    "go when it feels like too much. Naming the pattern isn't "
                    "pathologizing yourself. It's reading your own map."
                ),
            },
            {
                "name": "Activation Point",
                "threshold": 60,
                "description": "You can catch attachment patterns in real time.",
                "unlocks": ["Real-time pattern interruption", "Relational awareness tools"],
                "narrative": (
                    "The pattern still runs — but now you can see it running. "
                    "You notice the grab, the withdrawal, the performance, "
                    "in the moment instead of three days later. That awareness "
                    "is the intervention."
                ),
            },
            {
                "name": "Integration Point",
                "threshold": 80,
                "description": "Attachment patterns inform but don't control behavior.",
                "unlocks": ["Secure relating practices", "Earned security work"],
                "narrative": (
                    "Your attachment style is still yours — it doesn't disappear. "
                    "But it's information now, not instruction. You can feel the "
                    "old pull and choose a different response. That choice is "
                    "earned security."
                ),
            },
        ],
    },
    "Boundary Sovereignty": {
        "cluster": 2,
        "milestones": [
            {
                "name": "First Threshold",
                "threshold": 35,
                "description": "You can say no to something small without guilt spiral.",
                "unlocks": ["Body No practice", "Small refusal exercises"],
                "narrative": (
                    "The system taught you that boundaries were selfish — that "
                    "good people don't have edges. The first threshold is one "
                    "small no. Not a dramatic stand. Just: not that, not now. "
                    "And surviving the guilt that follows without retracting."
                ),
            },
            {
                "name": "Activation Point",
                "threshold": 55,
                "description": "Boundaries can be set in intimate and high-stakes contexts.",
                "unlocks": ["Intimate boundary practices", "The Deed deepens"],
                "narrative": (
                    "Your no has moved into the rooms that matter — the bedroom, "
                    "the family dinner, the relationship. You can hold a boundary "
                    "where the cost of holding it is real. And you hold it anyway."
                ),
            },
            {
                "name": "Integration Point",
                "threshold": 75,
                "description": "Boundaries are natural expressions of self-knowledge.",
                "unlocks": ["Relational sovereignty", "Full boundary fluency"],
                "narrative": (
                    "Boundaries aren't walls anymore — they're information about "
                    "where you end and someone else begins. You set them without "
                    "apology, adjust them without anxiety, and trust them as "
                    "expressions of care, not rejection."
                ),
            },
        ],
    },
    "Receiving Capacity": {
        "cluster": 2,
        "milestones": [
            {
                "name": "First Threshold",
                "threshold": 30,
                "description": "You can receive a compliment without deflecting.",
                "unlocks": ["Receiving practice exercises"],
                "narrative": (
                    "Receiving was dangerous in the old system — it created debt, "
                    "obligation, vulnerability. The first threshold is letting "
                    "something good land. A compliment. A gift. A kind word. "
                    "Just: thank you. Without immediately giving something back."
                ),
            },
            {
                "name": "Activation Point",
                "threshold": 50,
                "description": "You can receive pleasure, care, and attention without shutting down.",
                "unlocks": ["Receiving in intimacy", "Partner care practices"],
                "narrative": (
                    "Receiving has entered your body. You can be touched, cared "
                    "for, attended to without the internal alarm that says you "
                    "don't deserve it or need to reciprocate immediately. "
                    "Receiving is becoming its own skill."
                ),
            },
            {
                "name": "Integration Point",
                "threshold": 70,
                "description": "Receiving is as natural as giving.",
                "unlocks": ["Full relational reciprocity"],
                "narrative": (
                    "The asymmetry has resolved. You can give and receive with "
                    "equal grace. Receiving isn't selfish — it's the other half "
                    "of intimacy. You've learned that letting someone care for "
                    "you is itself a form of generosity."
                ),
            },
        ],
    },

    # ── CLUSTER 3: FORWARD ───────────────────
    "Erotic Identity Clarity": {
        "cluster": 3,
        "milestones": [
            {
                "name": "First Threshold",
                "threshold": 40,
                "description": "You have a sense that your erotic self exists separately from the system's definition.",
                "unlocks": ["Origin Question practice", "Identity exploration"],
                "narrative": (
                    "The system defined your sexuality for you — what was allowed, "
                    "what was forbidden, who you were supposed to be. The first "
                    "threshold is sensing that there's a you underneath all that "
                    "definition. Not knowing who yet. Just knowing there's someone "
                    "to discover."
                ),
            },
            {
                "name": "Activation Point",
                "threshold": 60,
                "description": "You can articulate aspects of your erotic identity with confidence.",
                "unlocks": ["Identity articulation practices", "Erotic values work"],
                "narrative": (
                    "You're starting to have words for who you are in this "
                    "territory — not the system's words, your own. What draws "
                    "you. What repels you. What feels like you and what was "
                    "installed. The picture is forming."
                ),
            },
            {
                "name": "Integration Point",
                "threshold": 80,
                "description": "Your erotic identity is clear, owned, and integrated.",
                "unlocks": ["Full erotic identity expression"],
                "narrative": (
                    "You know who you are here. Not perfectly — identity keeps "
                    "growing — but solidly enough to act from it, communicate "
                    "about it, and stand in it without apology. This is your "
                    "land. You've learned its terrain."
                ),
            },
        ],
    },
    "Orientation & Preference Exploration": {
        "cluster": 3,
        "milestones": [
            {
                "name": "First Threshold",
                "threshold": 35,
                "description": "You can notice attractions without moral panic.",
                "unlocks": ["Safe exploration practices"],
                "narrative": (
                    "Attraction was policed by the system — only certain kinds "
                    "were allowed, and even those were suspect. The first threshold "
                    "is noticing what actually draws you without the alarm bells. "
                    "Not acting on it. Just noticing, without emergency."
                ),
            },
            {
                "name": "Activation Point",
                "threshold": 55,
                "description": "Preferences can be explored with curiosity rather than fear.",
                "unlocks": ["Preference exploration", "Fantasy as information"],
                "narrative": (
                    "Curiosity has replaced terror. You can wonder about what "
                    "you like — who you're drawn to, what scenarios interest you, "
                    "what feels genuinely exciting — without the old system's "
                    "verdict following every thought."
                ),
            },
            {
                "name": "Integration Point",
                "threshold": 75,
                "description": "Orientation and preferences are known, accepted, and communicable.",
                "unlocks": ["Full orientation integration"],
                "narrative": (
                    "You know what you like and who you want. Not every detail — "
                    "discovery is ongoing — but the broad strokes are clear and "
                    "owned. You can talk about them without shame, adjust them "
                    "without crisis, and act from them without apology."
                ),
            },
        ],
    },
    "Conscious Exploration Capacity": {
        "cluster": 3,
        "milestones": [
            {
                "name": "First Threshold",
                "threshold": 35,
                "description": "You can try something new without it feeling like a test.",
                "unlocks": ["The Laboratory practice"],
                "narrative": (
                    "Exploration was forbidden or secret or shameful. The first "
                    "threshold is trying one new thing — even something tiny — "
                    "and experiencing it as experiment rather than exam. No grade. "
                    "No verdict. Just: what was that like?"
                ),
            },
            {
                "name": "Activation Point",
                "threshold": 55,
                "description": "New experiences can be sought with genuine curiosity.",
                "unlocks": ["Structured exploration practices", "Novelty without anxiety"],
                "narrative": (
                    "You're becoming someone who reaches for new experiences "
                    "instead of bracing against them. Curiosity is driving "
                    "more than anxiety. The laboratory is open."
                ),
            },
            {
                "name": "Integration Point",
                "threshold": 75,
                "description": "Exploration is a natural expression of aliveness.",
                "unlocks": ["Full exploration capacity", "Creative intimacy"],
                "narrative": (
                    "Exploration isn't scary anymore — it's how you grow. "
                    "You seek new experiences, adjust based on what you learn, "
                    "and trust that trying something doesn't commit you to "
                    "it forever. The scientist in you is thriving."
                ),
            },
        ],
    },
    "Sexual Future Vision": {
        "cluster": 3,
        "milestones": [
            {
                "name": "First Threshold",
                "threshold": 40,
                "description": "You can imagine a sexual future that isn't defined by the past.",
                "unlocks": ["Future visioning exercises"],
                "narrative": (
                    "For a long time, the future looked like the past — either "
                    "the system's version or a reaction against it. The first "
                    "threshold is imagining something else entirely. A sexual "
                    "life that's actually yours. Even if the picture is blurry, "
                    "the fact that you can see anything at all is the shift."
                ),
            },
            {
                "name": "Activation Point",
                "threshold": 60,
                "description": "Your vision has specific, personally meaningful elements.",
                "unlocks": ["Vision refinement practices", "Goal-setting in intimacy"],
                "narrative": (
                    "The picture is getting clearer. You can name specific things "
                    "you want — not just what you're leaving behind but what "
                    "you're building toward. The future has features now."
                ),
            },
            {
                "name": "Integration Point",
                "threshold": 80,
                "description": "Your sexual future vision guides present choices.",
                "unlocks": ["Vision-aligned action", "Long-term intimate planning"],
                "narrative": (
                    "Your vision of your sexual future is clear enough to act "
                    "from. Present choices are informed by where you're going, "
                    "not just where you've been. You're building, not just "
                    "recovering."
                ),
            },
        ],
    },
    "Integration Readiness": {
        "cluster": 3,
        "milestones": [
            {
                "name": "First Threshold",
                "threshold": 35,
                "description": "You can hold complexity without defaulting to old binaries.",
                "unlocks": ["Complexity tolerance exercises"],
                "narrative": (
                    "The system was binary — good/bad, pure/impure, saved/lost. "
                    "The first threshold is holding two truths at once: this was "
                    "harmful AND those people loved me. I was wounded AND I am "
                    "not broken. Both, simultaneously, without collapse."
                ),
            },
            {
                "name": "Activation Point",
                "threshold": 55,
                "description": "Past and present sexual self can coexist without conflict.",
                "unlocks": ["Integration practices", "Return Letter practice"],
                "narrative": (
                    "Your past sexual self — the one shaped by the system — and "
                    "your present self are beginning to share space. You don't "
                    "have to reject who you were to become who you are."
                ),
            },
            {
                "name": "Integration Point",
                "threshold": 75,
                "description": "All parts of your sexual history are integrated into a coherent narrative.",
                "unlocks": ["Full narrative integration", "Mentoring capacity"],
                "narrative": (
                    "Your story makes sense now — not because it was okay, but "
                    "because you can hold all of it. The wound, the healing, "
                    "the person you're becoming. It's one story, not fragments. "
                    "And it's yours to tell."
                ),
            },
        ],
    },

    # ── CLUSTER 4: ALIVENESS ─────────────────
    "Erotic Play Capacity": {
        "cluster": 4,
        "milestones": [
            {
                "name": "First Threshold",
                "threshold": 30,
                "description": "Play can exist as a concept in intimate space.",
                "unlocks": ["Playful intimacy exercises"],
                "narrative": (
                    "The system made intimacy serious — high stakes, moral "
                    "weight, cosmic consequences. The first threshold is the "
                    "moment you realize that play belongs here too. That "
                    "laughter and lightness aren't disrespectful — they're "
                    "intimate."
                ),
            },
            {
                "name": "Activation Point",
                "threshold": 50,
                "description": "You can be playful in intimate contexts without anxiety.",
                "unlocks": ["Creative play practices", "Spontaneous intimacy"],
                "narrative": (
                    "Play has entered the bedroom — and the kitchen, and the "
                    "car, and wherever intimacy lives. You can be silly, "
                    "experimental, light. The performance pressure is lifting."
                ),
            },
            {
                "name": "Integration Point",
                "threshold": 70,
                "description": "Play is a natural dimension of your erotic life.",
                "unlocks": ["Full erotic play range"],
                "narrative": (
                    "Play is just part of how you do intimacy now. Not forced, "
                    "not performative — genuine. You can laugh during sex, try "
                    "things that don't work, and enjoy the attempt as much as "
                    "the outcome."
                ),
            },
        ],
    },
    "Sensory Range": {
        "cluster": 4,
        "milestones": [
            {
                "name": "First Threshold",
                "threshold": 30,
                "description": "You can notice sensory pleasure beyond the obvious.",
                "unlocks": ["Sensory expansion exercises"],
                "narrative": (
                    "The system narrowed pleasure to a few approved channels — "
                    "or shut it down entirely. The first threshold is noticing "
                    "that pleasure lives in more places than you were taught. "
                    "A texture. A temperature. A sound. The body has a wider "
                    "range than the system allowed."
                ),
            },
            {
                "name": "Activation Point",
                "threshold": 50,
                "description": "Multiple senses contribute to erotic experience.",
                "unlocks": ["Multi-sensory practices", "Sensory mapping"],
                "narrative": (
                    "Your sensory world is expanding. Touch, sound, sight, "
                    "scent, taste — they're all participating now, not just "
                    "the ones the system approved. The experience of pleasure "
                    "is becoming richer, more dimensional."
                ),
            },
            {
                "name": "Integration Point",
                "threshold": 70,
                "description": "Full sensory aliveness in intimate contexts.",
                "unlocks": ["Full sensory integration"],
                "narrative": (
                    "All your senses are online. Intimacy is a full-body, "
                    "full-spectrum experience. You're not thinking about "
                    "sensation — you're living in it."
                ),
            },
        ],
    },
    "Spontaneous Presence": {
        "cluster": 4,
        "milestones": [
            {
                "name": "First Threshold",
                "threshold": 25,
                "description": "You can be in your body for 30 seconds without dissociating.",
                "unlocks": ["Arrival Practice"],
                "narrative": (
                    "Presence was dangerous — being fully here meant being "
                    "fully visible to the omniscient observer. The first "
                    "threshold is thirty seconds in your body. Actually here. "
                    "Not planning, not monitoring, not performing. Just: here."
                ),
            },
            {
                "name": "Activation Point",
                "threshold": 45,
                "description": "Presence can be sustained during intimate contact.",
                "unlocks": ["Partnered presence practices", "Sensory intimacy"],
                "narrative": (
                    "You can stay. Not perfectly — the drift still happens — "
                    "but you can come back. During touch, during eye contact, "
                    "during the moments that used to send you to the ceiling. "
                    "You're learning to land."
                ),
            },
            {
                "name": "Integration Point",
                "threshold": 65,
                "description": "Presence is the default, not the exception.",
                "unlocks": ["Full embodied presence"],
                "narrative": (
                    "Presence has become your home frequency. You don't have "
                    "to work to stay — you notice when you've left and come "
                    "back naturally. The body is no longer a place to escape "
                    "from. It's where you live."
                ),
            },
        ],
    },
    "Intimate Levity": {
        "cluster": 4,
        "milestones": [
            {
                "name": "First Threshold",
                "threshold": 30,
                "description": "You can experience lightness without guilt.",
                "unlocks": ["Levity practices", "Permission for joy"],
                "narrative": (
                    "Joy had a tax in the old system — good things were suspect, "
                    "lightness was shallow, pleasure was borrowed time. The first "
                    "threshold is one moment of genuine lightness that doesn't "
                    "come with a bill. Just: this is nice. And that's enough."
                ),
            },
            {
                "name": "Activation Point",
                "threshold": 50,
                "description": "Humor and lightness are natural parts of intimate connection.",
                "unlocks": ["Playful intimacy deepens", "Laughter as connection"],
                "narrative": (
                    "You can laugh here. In bed, in conversation, in the "
                    "vulnerable moments. Lightness isn't deflection — it's "
                    "another frequency of intimacy. And your range is growing."
                ),
            },
            {
                "name": "Integration Point",
                "threshold": 70,
                "description": "Levity and depth coexist naturally in intimate life.",
                "unlocks": ["Full intimate range"],
                "narrative": (
                    "Light and deep aren't opposites anymore. You can move "
                    "between them — laughter to tears to desire to silliness — "
                    "without losing connection. The full spectrum is available."
                ),
            },
        ],
    },
    "Embodied Curiosity": {
        "cluster": 4,
        "milestones": [
            {
                "name": "First Threshold",
                "threshold": 30,
                "description": "You can wonder 'what if' about your body without fear.",
                "unlocks": ["Curiosity practices", "Body wonder exercises"],
                "narrative": (
                    "The system shut down curiosity about the body — there was "
                    "nothing to discover, only rules to follow. The first "
                    "threshold is a genuine 'I wonder...' about your own body. "
                    "What does it like? What would happen if? The question is "
                    "the beginning."
                ),
            },
            {
                "name": "Activation Point",
                "threshold": 50,
                "description": "Curiosity drives exploration of new sensations and experiences.",
                "unlocks": ["Embodied exploration", "Sensation experiments"],
                "narrative": (
                    "Curiosity is leading now — not anxiety, not obligation, "
                    "not performance. You want to know what your body can do, "
                    "what it enjoys, what surprises it. The explorer in you "
                    "is waking up."
                ),
            },
            {
                "name": "Integration Point",
                "threshold": 70,
                "description": "Embodied curiosity is a permanent orientation toward aliveness.",
                "unlocks": ["Full embodied aliveness"],
                "narrative": (
                    "Curiosity has become your operating system. You approach "
                    "your body, your partner, your erotic life with the same "
                    "openness a scientist brings to the lab — interested, "
                    "attentive, ready to be surprised. The deadening is over."
                ),
            },
        ],
    },
}


# ─────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────

def get_waypoint(axis_name):
    """Return waypoint definition for an axis."""
    return WAYPOINTS.get(axis_name)


def get_current_milestone(axis_name, score):
    """
    Return the current milestone (highest one whose threshold is met or exceeded).
    Returns None if no threshold met.
    """
    wp = WAYPOINTS.get(axis_name)
    if not wp:
        return None

    current = None
    for milestone in wp["milestones"]:
        if score >= milestone["threshold"]:
            current = milestone
    return current


def get_next_milestone(axis_name, score):
    """
    Return the next milestone (first one whose threshold is NOT yet met).
    Returns None if all milestones are met.
    """
    wp = WAYPOINTS.get(axis_name)
    if not wp:
        return None

    for milestone in wp["milestones"]:
        if score < milestone["threshold"]:
            return milestone
    return None


def get_unlocks_at_score(axis_name, score):
    """Return all unlocks available at the given score."""
    wp = WAYPOINTS.get(axis_name)
    if not wp:
        return []

    unlocks = []
    for milestone in wp["milestones"]:
        if score >= milestone["threshold"]:
            unlocks.extend(milestone.get("unlocks", []))
    return unlocks


def get_next_milestone_narrative(axis_name, score):
    """
    Return dict with axis, current score, next milestone info, and narrative.
    Used by generate_report.py for the waypoint section.
    """
    wp = WAYPOINTS.get(axis_name)
    if not wp:
        return None

    next_ms = get_next_milestone(axis_name, score)
    if not next_ms:
        return None

    return {
        "axis": axis_name,
        "score": score,
        "spine_domain": AXIS_TO_SPINE.get(axis_name, ""),
        "next_milestone": next_ms["name"],
        "next_threshold": next_ms["threshold"],
        "narrative": next_ms["narrative"],
        "description": next_ms["description"],
        "unlocks": next_ms.get("unlocks", []),
    }


def get_waypoints_by_cluster(cluster_num):
    """Return all waypoints belonging to a cluster."""
    result = {}
    for axis_name, wp in WAYPOINTS.items():
        if wp["cluster"] == cluster_num:
            result[axis_name] = wp
    return result


def get_waypoints_by_spine_domain(domain_name):
    """Return all waypoints belonging to a SPINE domain."""
    result = {}
    for axis_name, wp in WAYPOINTS.items():
        if AXIS_TO_SPINE.get(axis_name) == domain_name:
            result[axis_name] = wp
    return result


def calculate_waypoint_score(client_data):
    """
    Calculate overall waypoint progress: proportion of milestones reached
    across all 20 axes.
    """
    axes = get_all_axes(client_data)
    total_milestones = 0
    reached_milestones = 0

    for axis_name, score in axes.items():
        wp = WAYPOINTS.get(axis_name)
        if not wp:
            continue
        for milestone in wp["milestones"]:
            total_milestones += 1
            if score >= milestone["threshold"]:
                reached_milestones += 1

    if total_milestones == 0:
        return 0
    return round((reached_milestones / total_milestones) * 100)
