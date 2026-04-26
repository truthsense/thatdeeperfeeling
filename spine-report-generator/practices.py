"""
SPINE Framework — Complete Practice Catalog
Every practice with client text in Kimberly's voice, practitioner notes,
and mechanism alignment.
"""

HEALING = "healing"
PATTERN = "pattern"
RESOURCING = "resourcing"


PRACTICES = {
    "daily_return": {
        "name": "The Daily Return",
        "domain": "sexual",
        "spine_domain": "Embodiment",
        "category": HEALING,
        "cluster": 1,
        "target_axes": ["Body Trust", "Erotic Self-Acceptance"],
        "weeks": "1-4",
        "week_start": 1,
        "week_end": 4,
        "mechanism_alignment": ["divine_surveillance", "purity_worth_fusion"],
        "client_text": (
            "Before the day gets its hands on you — just after waking, while "
            "your body is still warm and unguarded — find your own hands. Let "
            "them land somewhere without deciding first. Belly. Heart. Thigh. "
            "Ribs. Wherever they go is already information.\n\n"
            "Stay there. Not to fix anything. Not to feel anything in particular. "
            "Just to notice you're here. That this body — this specific, imperfect, "
            "lived-in body — is yours. It has always been yours. Nobody ever had "
            "the right to make you a stranger inside it.\n\n"
            "Sixty seconds. One hand. One breath that's a little longer going out "
            "than coming in. And then, quietly, to yourself: I live here.\n\n"
            "Do it again before sleep. The body learns through repetition what "
            "words alone can't teach."
        ),
        "what_youll_notice": (
            "At first, probably not much. Maybe numbness. Maybe the urge to "
            "skip it — that urge is information too. Around week two, something "
            "might shift: a small warmth, a breath that arrives a little easier. "
            "Your body beginning to expect you. That expectation is the beginning "
            "of coming home."
        ),
        "practitioner_notes": {
            "what_this_does": (
                "Rebuilds somatic presence and body trust through consistent, "
                "non-demanding contact. Creates a daily anchor point for nervous "
                "system regulation."
            ),
            "how_to_introduce": (
                "Frame as the foundation practice — everything else builds on this. "
                "Emphasize that nothing needs to happen. No right way to feel."
            ),
            "what_to_watch": (
                "Dissociation during practice. Strong emotional responses. "
                "Avoidance patterns — forgetting, minimizing, rushing through."
            ),
            "when_to_adapt": (
                "If numbness beyond week 3, add textural element. If dissociation, "
                "reduce to one hand and 30 seconds. If distress exceeds window, "
                "pause and ground with feet-on-floor."
            ),
            "modality_roots": "Somatic Experiencing, Hakomi, polyvagal-informed touch.",
        },
    },
    "the_lighthouse": {
        "name": "The Lighthouse",
        "domain": "sexual",
        "spine_domain": "Nourishment",
        "category": HEALING,
        "cluster": 1,
        "target_axes": ["Pleasure Permission", "Sensory Range"],
        "weeks": "3-8",
        "week_start": 3,
        "week_end": 8,
        "mechanism_alignment": ["purity_worth_fusion", "eschatological_urgency"],
        "client_text": (
            "Once a day — it takes two minutes — find one moment of genuine "
            "pleasure from the last 24 hours. Something small is perfect. The "
            "first sip of something warm. A song that moved through you. "
            "Sunlight on skin. The specific satisfaction of a door closing "
            "behind you at the end of the day.\n\n"
            "Write it down. Just the moment and what it felt like in your body. "
            "Not an analysis. Not gratitude. Just: this happened, and my body "
            "registered it as good.\n\n"
            "Then close your eyes and let your body re-experience it for 30 "
            "seconds. Let the pleasure be as large as it wants to be.\n\n"
            "This is not a small practice. You were taught that pleasure was "
            "dangerous. You are methodically, tenderly, teaching your nervous "
            "system something different: pleasure is safe data. I am allowed "
            "to feel good.\n\n"
            "The lighthouse doesn't move toward the storm. It stands and keeps "
            "its light on. That's what this is — keeping the light on for the "
            "parts of you still navigating in the dark."
        ),
        "what_youll_notice": (
            "Your pleasure vocabulary will expand. Things you didn't register as "
            "pleasurable will start to surface. The body begins to trust that "
            "pleasure is allowed."
        ),
        "practitioner_notes": {
            "what_this_does": "Rebuilds pleasure permission through safe sensory pairing.",
            "how_to_introduce": "Distinguish from gratitude journaling — body-first, not mind-first.",
            "what_to_watch": "Guilt responses. Inability to identify pleasure moments.",
            "when_to_adapt": "If no pleasure found, start with 'least unpleasant.' If guilt overwhelming, reduce to 10 seconds.",
            "modality_roots": "Sensorimotor Psychotherapy, positive neuroplasticity (Rick Hanson).",
        },
    },
    "witnessed_voice": {
        "name": "The Witnessed Voice",
        "domain": "sexual",
        "spine_domain": "Power",
        "category": HEALING,
        "cluster": 2,
        "target_axes": ["Communication Capacity", "Boundary Sovereignty"],
        "weeks": "4-8",
        "week_start": 4,
        "week_end": 8,
        "mechanism_alignment": ["vertical_authority", "community_surveillance"],
        "client_text": (
            "Find a private minute. Hit record on your phone. Then say something "
            "true — something that's been living inside you without sound.\n\n"
            "It doesn't have to be profound. I'm tired of performing. I want "
            "more than this. I don't actually know what I want yet and that "
            "scares me. Whatever is true right now.\n\n"
            "You don't have to listen back. You don't have to share it. The "
            "practice is simply this: your voice, speaking the true thing, "
            "into the air, where it becomes real.\n\n"
            "The system taught you that your voice — especially in dissent, "
            "in desire, in need — was dangerous. This practice disagrees. "
            "Quietly. Privately. One true sentence at a time.\n\n"
            "There's something that happens when a true thing gets spoken aloud "
            "rather than staying in the body as thought. It becomes real in a "
            "different way. It takes up space. It arrives in the world as yours.\n\n"
            "That's the whole practice."
        ),
        "what_youll_notice": (
            "Resistance at first. Maybe tears. Eventually, a steadiness in your "
            "voice that wasn't there before. The gap between knowing and saying "
            "will start to close."
        ),
        "practitioner_notes": {
            "what_this_does": "Bridges internal knowing and external expression.",
            "how_to_introduce": "For surveillance-primary: emphasize recordings are NEVER shared.",
            "what_to_watch": "Performing rather than truth-telling. Avoiding entirely.",
            "when_to_adapt": "If voice too exposed, start with written statements read aloud.",
            "modality_roots": "Voice Dialogue, narrative therapy, expressive arts.",
        },
    },
    "the_watchtower": {
        "name": "The Watchtower",
        "domain": "sexual",
        "spine_domain": "Sovereignty",
        "category": PATTERN,
        "cluster": 1,
        "target_axes": ["Body Trust", "Arousal-Shame Decoupling"],
        "weeks": "5-8",
        "week_start": 5,
        "week_end": 8,
        "mechanism_alignment": ["divine_surveillance", "community_surveillance"],
        "client_text": (
            "A few times a day — especially when you notice yourself monitoring, "
            "reviewing, scanning for approval — ask one question:\n\n"
            "Am I in the tower?\n\n"
            "The tower is where you go when the old surveillance program is "
            "running: checking how you're coming across, rehearsing explanations, "
            "bracing for consequences that aren't actually coming. You know this "
            "feeling. You've probably lived there so long it feels like just — life.\n\n"
            "When you notice you're there: name it. I'm in the tower. No judgment. "
            "Just accurate location. Then find the ground. Feet on the floor. "
            "One thing you can touch right now. One breath out that's longer "
            "than the one before it.\n\n"
            "That's the climb down. You don't have to stay at ground level forever. "
            "Just practice knowing it exists. Practice knowing you can return to "
            "yourself — your actual self, not the monitored performance of "
            "yourself — whenever you choose to look for the stairs."
        ),
        "what_youll_notice": (
            "How often you're in the tower. That's the first revelation. "
            "Don't let that discourage you. Noticing is the practice. Over time, "
            "the climb down gets faster."
        ),
        "practitioner_notes": {
            "what_this_does": "Interrupts internalized surveillance by making it visible.",
            "how_to_introduce": "Normalize frequency. The noticing IS the intervention.",
            "what_to_watch": "Using watchtower check AS surveillance (monitoring the monitoring).",
            "when_to_adapt": "If overwhelmed by frequency, limit to twice daily.",
            "modality_roots": "IFS (manager part), MBCT, polyvagal theory.",
        },
    },
    "mirror_voice": {
        "name": "The Mirror Voice",
        "domain": "sexual",
        "spine_domain": "Identity",
        "category": PATTERN,
        "cluster": 2,
        "target_axes": ["Communication Capacity", "Erotic Identity Clarity"],
        "weeks": "3-8",
        "week_start": 3,
        "week_end": 8,
        "mechanism_alignment": ["identity_assignment", "vertical_authority"],
        "client_text": (
            "Stand in front of a mirror. Make real eye contact with yourself — "
            "not a glance, actual contact. Then say one true sentence out loud.\n\n"
            "Start wherever you are. I'm here. I'm tired. I want something I "
            "haven't let myself want yet. The words matter less than the contact "
            "— you, meeting yourself, in the mirror, with your actual voice, "
            "saying something true.\n\n"
            "Three times a week. Two minutes. Build from small truths to larger ones.\n\n"
            "By week four, say something about what you need. By week six, "
            "something about desire. By week eight, something you've wanted in "
            "your intimate life that you've been keeping in the quiet.\n\n"
            "There's a specific alchemy in this practice: the moment when the "
            "person in the mirror stops being someone you're performing for and "
            "becomes someone you're actually with. When you stop managing how "
            "you look and start actually seeing yourself.\n\n"
            "That moment is the practice arriving."
        ),
        "what_youll_notice": (
            "Difficulty maintaining eye contact at first. Emotional responses "
            "you don't expect. Over time, your voice will steady and your "
            "gaze will soften."
        ),
        "practitioner_notes": {
            "what_this_does": "Rebuilds self-witnessing capacity.",
            "how_to_introduce": "Warn of unexpected emotion. Eye contact is essential.",
            "what_to_watch": "Dissociation during mirror contact. Performing for the mirror.",
            "when_to_adapt": "If full mirror too much, start with eyes only.",
            "modality_roots": "Mirror work (adapted), self-compassion practices, SE.",
        },
    },
    "the_deed": {
        "name": "The Deed",
        "domain": "sexual",
        "spine_domain": "Power",
        "category": PATTERN,
        "cluster": 2,
        "target_axes": ["Consent Clarity", "Boundary Sovereignty"],
        "weeks": "5-8",
        "week_start": 5,
        "week_end": 8,
        "mechanism_alignment": ["vertical_authority"],
        "client_text": (
            "Once a week, find something you want to do — small enough to "
            "complete in a day — that you've been waiting for permission to do. "
            "Not dramatic. Not a declaration. Just something genuinely yours.\n\n"
            "Take it. Do it. Then write three words: I chose this.\n\n"
            "The Deed isn't about the action. It's about the felt experience "
            "of choosing from the inside rather than waiting for authorization "
            "that was never going to come anyway.\n\n"
            "Week 5: claim one hour of time that's purely, specifically yours.\n"
            "Week 6: hold one feeling all the way through without routing it "
            "through anyone's evaluation.\n"
            "Week 7: say one true thing you'd normally keep to yourself.\n"
            "Week 8: acknowledge one desire — let it exist without acting on "
            "it or suppressing it. Just: this want is mine and it's allowed.\n\n"
            "Each week, the territory gets more interior. You're not just "
            "practicing doing things. You're practicing being the one who decides."
        ),
        "what_youll_notice": (
            "The gap between wanting and doing will shrink. You'll start to "
            "notice permission patterns — where you wait for approval that "
            "isn't required."
        ),
        "practitioner_notes": {
            "what_this_does": "Rebuilds self-authorization through incremental choice.",
            "how_to_introduce": "NOT about rebellion. Small, genuine, owned.",
            "what_to_watch": "Performing rebellion rather than genuine choice.",
            "when_to_adapt": "If guilt overwhelming, start with even smaller choices.",
            "modality_roots": "Behavioral activation, self-determination theory, existential therapy.",
        },
    },
    "body_no": {
        "name": "The Body No",
        "spine_domain": "Power",
        "domain": "sexual",
        "category": PATTERN,
        "cluster": 2,
        "target_axes": ["Consent Clarity", "Boundary Sovereignty", "Receiving Capacity"],
        "weeks": "6-8",
        "week_start": 6,
        "week_end": 8,
        "mechanism_alignment": ["vertical_authority", "community_surveillance"],
        "client_text": (
            "Your no lives in your body before it becomes a word. A tightening "
            "in the chest. The stomach pulling back. A subtle closing. A breath "
            "that holds.\n\n"
            "You've felt it. You've probably overridden it hundreds of times "
            "because saying no felt more dangerous than enduring what you "
            "didn't want.\n\n"
            "This practice has one instruction: find your no before you need "
            "to use it.\n\n"
            "In a low-stakes moment — someone offers you something you don't "
            "want — don't say the no yet. Just notice the physical signal first. "
            "Name it internally, wherever it lives: there it is.\n\n"
            "Feel how your body knew before your mind had finished deciding.\n\n"
            "You don't have to say it yet. Just get familiar with where it lives. "
            "The speaking comes later — and it comes much more easily once you "
            "know what you're translating.\n\n"
            "Your no is not an obstacle to intimacy. It is the architecture of "
            "it. No one can trust a yes that doesn't have a no available. "
            "Including you."
        ),
        "what_youll_notice": (
            "'No' will start to feel less dangerous. Your body will begin to "
            "trust that refusal doesn't mean rejection. 'Yes' will start to "
            "mean more because 'no' is available."
        ),
        "practitioner_notes": {
            "what_this_does": "Rebuilds refusal capacity through somatic awareness.",
            "how_to_introduce": "Start in completely non-relational contexts.",
            "what_to_watch": "Performing no. Freezing instead of locating signal.",
            "when_to_adapt": "If freeze dominant, start with retrospective awareness.",
            "modality_roots": "SE (completing defensive responses), polyvagal, consent frameworks.",
        },
    },
    "pleasure_minute": {
        "name": "The Pleasure Minute",
        "spine_domain": "Nourishment",
        "domain": "sexual",
        "category": RESOURCING,
        "cluster": 1,
        "target_axes": ["Pleasure Permission", "Sensory Range"],
        "weeks": "3-6",
        "week_start": 3,
        "week_end": 6,
        "mechanism_alignment": ["eschatological_urgency", "purity_worth_fusion"],
        "client_text": (
            "One minute. That's it.\n\n"
            "Find something that is purely, simply pleasurable to one of your "
            "senses. Not productive. Not meaningful. Not earned. Just: this "
            "tastes good, or this feels good on my skin, or this sound is "
            "beautiful to me.\n\n"
            "Set a timer for one minute. Stay with the pleasure. The only "
            "instruction is to stay — not to analyze it, not to catalog it, "
            "not to appreciate it spiritually. Just to be in it.\n\n"
            "When guilt arrives — and it may — let it stand at the door. "
            "The pleasure gets the minute. The guilt can wait.\n\n"
            "This sounds simple. For most people who came from these systems, "
            "it is one of the hardest things on the list. Because the system "
            "didn't just regulate what you did with pleasure. It told you that "
            "wanting pleasure at all was evidence of your corruption.\n\n"
            "So one minute of uncomplicated sensory enjoyment is, quietly, "
            "an act of reclamation.\n\n"
            "You're allowed to feel good. Not because you've earned it. "
            "Just because you're here."
        ),
        "what_youll_notice": (
            "How unfamiliar it is to give yourself undivided sensory attention. "
            "How quickly the mind tries to leave. Over time, the body starts "
            "to open toward pleasure instead of bracing against it."
        ),
        "practitioner_notes": {
            "what_this_does": "Creates contained container for pleasure without overwhelm.",
            "how_to_introduce": "For Eschatological Urgency: may be FIRST practice.",
            "what_to_watch": "Choosing productive pleasures rather than purely sensory.",
            "when_to_adapt": "If one minute too long, start with 30 seconds.",
            "modality_roots": "Positive neuroplasticity, sensorimotor psychotherapy.",
        },
    },
    "want_before_why": {
        "name": "The Want Before the Why",
        "spine_domain": "Sovereignty",
        "domain": "sexual",
        "category": RESOURCING,
        "cluster": 1,
        "target_axes": ["Desire Ownership", "Erotic Self-Acceptance"],
        "weeks": "2-6",
        "week_start": 2,
        "week_end": 6,
        "mechanism_alignment": ["purity_worth_fusion", "vertical_authority"],
        "client_text": (
            "When a want arises — any want — practice saying it to yourself "
            "before evaluating it.\n\n"
            "I want ___.\n\n"
            "Nothing after the sentence yet. Not: I want this but I probably "
            "shouldn't. Not: I want this but it's too much. Just: I want ___.\n\n"
            "Let the want exist for ten seconds before you do anything with it. "
            "Ten seconds of the want being real before the evaluation begins.\n\n"
            "This sounds impossibly simple. For most people from these systems, "
            "it is genuinely one of the hardest things on this list. Because "
            "want and evaluation became simultaneous — the system trained you "
            "to evaluate desire at the moment of inception, before it could "
            "become conscious enough to be dangerous.\n\n"
            "This practice separates them. Want first. Then, if you choose, "
            "evaluation. But want first. Always want first.\n\n"
            "Over time the ten seconds becomes twenty. Then a minute. Then you "
            "find yourself noticing what you want with a kind of spacious "
            "curiosity rather than a running moral audit.\n\n"
            "That spaciousness is your appetite coming back to life."
        ),
        "what_youll_notice": (
            "How quickly your mind attaches a 'because' or 'but' to desire. "
            "Over time, wants will surface faster and feel less dangerous."
        ),
        "practitioner_notes": {
            "what_this_does": "Separates desire from moral evaluation at the neurological level.",
            "how_to_introduce": "Start with non-sexual, non-relational wants.",
            "what_to_watch": "Only identifying 'acceptable' wants. Performing wants.",
            "when_to_adapt": "If ten seconds too long, start with 'I notice a want.'",
            "modality_roots": "Focusing (Gendlin), ACT defusion, IFS.",
        },
    },
    "origin_question": {
        "name": "The Origin Question",
        "spine_domain": "Identity",
        "domain": "sexual",
        "category": RESOURCING,
        "cluster": 0,
        "target_axes": [],
        "weeks": "any",
        "week_start": 1,
        "week_end": 8,
        "mechanism_alignment": [
            "divine_surveillance", "identity_assignment", "purity_worth_fusion",
            "vertical_authority", "eschatological_urgency", "community_surveillance",
        ],
        "client_text": (
            "When shame arrives — and it will — ask one question before you "
            "accept it:\n\n"
            "Where did I first learn this was shameful?\n\n"
            "Not to avoid the shame. Not to intellectualize your way out of it. "
            "Just to check: is this shame generated, or is this shame installed?\n\n"
            "Generated shame says: I did something that conflicts with my own "
            "values. This belongs to me.\n\n"
            "Installed shame says: someone taught me this was shameful, and I "
            "absorbed the verdict before I could question it.\n\n"
            "When the trace leads back to a doctrine, a community's rule, a "
            "parent's voice — that's installed shame. And installed shame has "
            "a return address.\n\n"
            "You don't have to do anything dramatic with it. Just notice: this "
            "came from somewhere. It didn't originate in me. It was given without "
            "my consent.\n\n"
            "That noticing alone begins to loosen the hold."
        ),
        "what_youll_notice": (
            "Shame will start to have different textures. Some will feel old "
            "and borrowed. Some will feel current and yours. The sorting gets "
            "faster."
        ),
        "practitioner_notes": {
            "what_this_does": "Creates meta-cognitive framework for shame processing.",
            "how_to_introduce": "Companion practice at any point. A sorting tool.",
            "what_to_watch": "Intellectualizing away all shame. Stuck in anger at source.",
            "when_to_adapt": "If anger overwhelming, pair with Return Letter.",
            "modality_roots": "Schema therapy, narrative therapy externalization, ACT.",
        },
    },
    "arrival_practice": {
        "spine_domain": "Embodiment",
        "name": "The Arrival Practice",
        "domain": "sexual",
        "category": PATTERN,
        "cluster": 1,
        "target_axes": ["Body Trust", "Arousal-Shame Decoupling", "Spontaneous Presence"],
        "weeks": "4-8",
        "week_start": 4,
        "week_end": 8,
        "mechanism_alignment": ["divine_surveillance", "purity_worth_fusion"],
        "client_text": (
            "Before intimacy — with yourself or another — three minutes first.\n\n"
            "Hands on your body. Feet on the floor. One breath down to the belly.\n\n"
            "Then ask — with genuine curiosity, not evaluation: "
            "What is alive in my body right now?\n\n"
            "Not: am I ready? Not: should I want this? Just: what's actually present?\n\n"
            "You might find arousal. You might find tiredness. Tenderness. Anxiety. "
            "A mix of everything. Whatever is true is the right answer.\n\n"
            "This practice does one specific thing: it makes you a participant "
            "in what's about to happen rather than a surface things happen to. "
            "It brings you into the room before the room begins.\n\n"
            "In that pause — you exist as a subject, not an object. In that pause, "
            "you can choose. From the inside.\n\n"
            "That pause is sovereignty made physical."
        ),
        "what_youll_notice": (
            "The three minutes will feel awkward at first. Over time, the arrival "
            "becomes natural. You'll notice the difference between encounters "
            "where you arrived and ones where you didn't."
        ),
        "practitioner_notes": {
            "what_this_does": "Creates somatic consent check-in before intimacy.",
            "how_to_introduce": "Solo practice first. No wrong body state to arrive in.",
            "what_to_watch": "Performing the arrival without actually checking in.",
            "when_to_adapt": "If three minutes too long, start with one minute.",
            "modality_roots": "Somatic Experiencing, Sensate Focus (adapted), mindfulness.",
        },
    },
    "the_laboratory": {
        "name": "The Laboratory",
        "domain": "sexual",
        "spine_domain": "Identity",
        "category": RESOURCING,
        "cluster": 3,
        "target_axes": [
            "Erotic Identity Clarity",
            "Orientation & Preference Exploration",
            "Conscious Exploration Capacity",
        ],
        "weeks": "4+",
        "week_start": 4,
        "week_end": 8,
        "mechanism_alignment": ["identity_assignment", "purity_worth_fusion"],
        "client_text": (
            "Something drew your attention this week. An attraction, a curiosity, "
            "a pull toward something you've either never let yourself look at "
            "directly, or something that surprised you.\n\n"
            "Write it down without evaluation. Then three questions:\n\n"
            "What drew me?\n"
            "What did I notice in my body when I paid attention?\n"
            "Would I be curious to look at this again?\n\n"
            "No conclusions. No decisions. No meaning-making yet. Just data.\n\n"
            "The Laboratory isn't about arriving somewhere. It's about learning "
            "to stay in the looking — to let your own landscape be interesting "
            "rather than threatening. To discover that curiosity about yourself "
            "is one of the most intimate things you can practice.\n\n"
            "You are a hypothesis worth testing. The lab is open. "
            "What are you curious about today?"
        ),
        "what_youll_notice": (
            "Curiosity beginning to feel less dangerous. The capacity "
            "to hold a 'maybe' without needing it to become a 'yes' or 'no.' "
            "That capacity is erotic maturity arriving."
        ),
        "practitioner_notes": {
            "what_this_does": "Structured container for erotic exploration.",
            "how_to_introduce": "Only after Cluster 1 > 40%. Data, not identity work.",
            "what_to_watch": "Compulsive exploration (pendulum). Shame flooding after writing.",
            "when_to_adapt": "If shame overwhelming, add Origin Question as companion.",
            "modality_roots": "Narrative therapy, sexual health frameworks, curiosity-based.",
        },
    },
    "return_letter": {
        "name": "The Return Letter",
        "domain": "sexual",
        "spine_domain": "Sovereignty",
        "category": PATTERN,
        "cluster": 1,
        "target_axes": ["Arousal-Shame Decoupling", "Erotic Self-Acceptance"],
        "weeks": "single session",
        "week_start": 3,
        "week_end": 8,
        "mechanism_alignment": [
            "divine_surveillance", "identity_assignment", "purity_worth_fusion",
            "vertical_authority", "eschatological_urgency", "community_surveillance",
        ],
        "client_text": (
            "Choose one shame. One specific thing you carry that the system "
            "gave you — desire, doubt, orientation, your body, the wanting itself.\n\n"
            "Write it a letter. Three sentences is enough:\n\n"
            "This shame was handed to me. I did not choose it and I did not "
            "generate it. I return it to its source, and I reclaim the space "
            "it occupied.\n\n"
            "Read it out loud. Then do something ritual with it — burn it, "
            "bury it, tear it into small pieces and let go. The ritual matters "
            "because the body learns through ceremony what the mind understands "
            "through information.\n\n"
            "You're not destroying the memory. You're withdrawing your endorsement. "
            "You're closing the account.\n\n"
            "The shame may return — installed things don't leave cleanly. "
            "But when it returns, something will be different. There's a "
            "returned letter in your history now. You've said, on record, "
            "in your own voice: this was never mine to carry."
        ),
        "what_youll_notice": (
            "Relief that may surprise you. Grief underneath. The shame may "
            "return but with less authority. Each return letter makes the "
            "next one easier."
        ),
        "practitioner_notes": {
            "what_this_does": "Ritual container for shame externalization and return.",
            "how_to_introduce": "Single-session after week 3. Prepare for emotional release.",
            "what_to_watch": "Bypassing grief. Performing without engagement.",
            "when_to_adapt": "If writing too exposed, use verbal return. If ritual uncomfortable, use crumpling paper.",
            "modality_roots": "Narrative therapy externalization, ritual therapy, somatic grief.",
        },
    },
}


def get_practice(key):
    """Get a practice by its key."""
    return PRACTICES.get(key)


def get_practices_by_cluster(cluster_num):
    """Get all practices targeting a specific cluster."""
    return {k: v for k, v in PRACTICES.items()
            if v["cluster"] == cluster_num or v["cluster"] == 0}


def get_practices_by_category(category):
    """Get all practices of a given category."""
    return {k: v for k, v in PRACTICES.items() if v["category"] == category}


def get_practices_by_mechanism(mechanism_key):
    """Get all practices aligned with a given HDR mechanism."""
    return {k: v for k, v in PRACTICES.items()
            if mechanism_key in v["mechanism_alignment"]}


def get_practices_for_axes(axis_names):
    """Get practices that target any of the given axes."""
    results = {}
    for key, practice in PRACTICES.items():
        if any(axis in practice["target_axes"] for axis in axis_names):
            results[key] = practice
        elif not practice["target_axes"]:
            results[key] = practice
    return results


def get_practices_for_week_range(week_start, week_end):
    """Get practices active during the given week range."""
    return {k: v for k, v in PRACTICES.items()
            if v["week_start"] <= week_end and v["week_end"] >= week_start}


def get_practices_by_spine_domain(domain_name):
    """Get all practices under a SPINE domain."""
    return {k: v for k, v in PRACTICES.items()
            if v.get("spine_domain") == domain_name}
