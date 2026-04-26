"""
SPINE Framework — Coach's Guide & Practice Catalog PDF Generator
Practitioner-facing, comprehensive facilitation guide.
Deep sage cover, professional tone, full practice entries with
both client-facing and practitioner notes.
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
    DOMAIN_COLORS,
    CoverBackground, DividerLine, SectionDivider,
    DomainHeader, LeftBorderBox, ColorStripe,
    make_header_footer,
    voice_paragraph, voice_italic_paragraph,
    section_break,
)


# ─────────────────────────────────────────────
# PRACTICE CATALOG — Full entries with practitioner notes
# ─────────────────────────────────────────────

FULL_PRACTICES = [
    {
        "name": "The Daily Return",
        "domain": "Embodiment",
        "category": "Healing",
        "category_icon": "\U0001fa79",
        "weeks": "Weeks 1\u20134",
        "client_text": (
            "Before the day gets its hands on you \u2014 just after waking, "
            "while your body is still warm and unguarded \u2014 find your own "
            "hands. Let them land somewhere without deciding first. Belly. "
            "Heart. Thigh. Ribs. Wherever they go is already information.\n\n"
            "Stay there. Not to fix anything. Not to feel anything in particular. "
            "Just to notice you\u2019re here. That this body \u2014 this specific, "
            "imperfect, lived-in body \u2014 is yours. It has always been yours. "
            "Nobody ever had the right to make you a stranger inside it.\n\n"
            "Sixty seconds. One hand. One breath that\u2019s a little longer going "
            "out than coming in. And then, quietly, to yourself: I live here.\n\n"
            "Do it again before sleep. The body learns through repetition what "
            "words alone can\u2019t teach."
        ),
        "mechanism": (
            "Creating repeated, uncharged somatic contact with the body. "
            "The mechanism is simple \u2014 the nervous system learns what gets "
            "repeated. Repeated inhabitation without consequence gradually "
            "updates the threat assessment the body has around being present "
            "in itself."
        ),
        "how_to_introduce": (
            "\u201cI want to give you one practice before our next session \u2014 "
            "just one, nothing else. It takes sixty seconds. That\u2019s not "
            "metaphor \u2014 literally sixty seconds, twice a day. The only "
            "instruction is to find your own hands and let them land somewhere "
            "on your body, and stay for one breath.\u201d Pause. \u201cCan you do that?\u201d "
            "Getting a verbal yes is part of the practice \u2014 it\u2019s the first "
            "act of self-authorization."
        ),
        "what_to_watch_for": (
            "The client who reports numbness \u2014 this is the practice working, "
            "not failing. The nervous system protects through disconnection. "
            "Numbness means they\u2019re present enough to notice disconnection. "
            "The client who floods \u2014 slow down, add more grounding before the "
            "body contact, add the shame interrupt as a companion practice. "
            "The client who skips it consistently \u2014 that avoidance is the most "
            "important clinical data. Bring it to session. \u201cWhat happens when "
            "you think about doing it?\u201d Not judgment \u2014 genuine curiosity."
        ),
        "when_to_adapt": (
            "For clients with significant body shame or history of physical "
            "violation, start with hands on the clothed thighs or on the surface "
            "of a chair \u2014 anywhere that feels less charged than belly or chest. "
            "The location matters less than the contact."
        ),
        "when_to_pause": (
            "If the practice consistently produces acute distress that doesn\u2019t "
            "resolve within two to three minutes \u2014 pause and bring a somatic "
            "therapist in before continuing."
        ),
        "modality_roots": (
            "Somatic experiencing (Peter Levine), sensorimotor psychotherapy "
            "(Pat Ogden), polyvagal theory application (Deb Dana)."
        ),
    },
    {
        "name": "The Lighthouse",
        "domain": "Nourishment",
        "category": "Healing",
        "category_icon": "\U0001fa79",
        "weeks": "Weeks 3\u20138",
        "client_text": (
            "Once a day \u2014 it takes two minutes \u2014 find one moment of genuine "
            "pleasure from the last twenty-four hours. Something small is perfect. "
            "The first sip of something warm. A song that moved through you. "
            "Sunlight on skin. The specific satisfaction of a door closing behind "
            "you at the end of the day.\n\n"
            "Write it down. Just the moment and what it felt like in your body. "
            "Not an analysis. Not gratitude. Just: this happened, and my body "
            "registered it as good.\n\n"
            "Then close your eyes and let your body re-experience it for thirty "
            "seconds. Let the pleasure be as large as it wants to be.\n\n"
            "This is not a small practice. You were taught that pleasure was "
            "dangerous. You are methodically, tenderly, teaching your nervous "
            "system something different: pleasure is safe data. I am allowed to "
            "feel good.\n\n"
            "The lighthouse doesn\u2019t move toward the storm. It stands and keeps "
            "its light on. That\u2019s what this practice is \u2014 keeping the light on "
            "for the parts of you that have been navigating in the dark."
        ),
        "mechanism": (
            "Systematic pleasure sensitization. The system created a near-automatic "
            "shame interrupt that fires when pleasure registers \u2014 arousal \u2192 shame, "
            "enjoyment \u2192 guilt, receiving \u2192 unworthiness. This practice builds a "
            "new pathway: pleasure \u2192 notice \u2192 stay \u2192 record \u2192 re-experience. Each "
            "repetition is a small update to the nervous system\u2019s threat map."
        ),
        "how_to_introduce": (
            "\u201cBefore we look at the bigger landscape \u2014 can we start with something "
            "specific? What was one moment in the last week that your body registered "
            "as genuinely good? Even tiny. Even something you almost didn\u2019t notice.\u201d "
            "Let them find one. Then: \u201cThat\u2019s the practice. Once a day, find one moment "
            "like that and write it down. That\u2019s all. We\u2019re not trying to transform "
            "your relationship to pleasure in a week. We\u2019re just keeping the light on.\u201d"
        ),
        "what_to_watch_for": (
            "Clients who cannot find a single moment of pleasure \u2014 this is significant "
            "clinical data about the depth of the shutdown. Work at even smaller "
            "granularity: not pleasure but simply not-pain. A moment that was neutral "
            "or mildly okay. Build from there. Clients who find the practice and then "
            "immediately contextualize it \u2014 \u201cI enjoyed the coffee but then I felt "
            "guilty about spending the money.\u201d The guilt-following-pleasure pattern is "
            "exactly what we\u2019re tracking. Name it, gently, as information: \u201cThe pleasure "
            "arrived. And then something else arrived right behind it.\u201d"
        ),
        "when_to_adapt": (
            "For clients with acute shame around pleasure, start with non-sensory "
            "pleasure \u2014 an intellectual satisfaction, a moment of competence, a good "
            "conversation. Build toward physical/sensory pleasure gradually."
        ),
        "when_to_pause": None,
        "modality_roots": (
            "Mindfulness-based sex therapy (Lori Brotto), sensate focus (Masters "
            "and Johnson, adapted), positive neuroplasticity training (Rick Hanson\u2019s "
            "\u201ctaking in the good\u201d)."
        ),
    },
    {
        "name": "The Witnessed Voice",
        "domain": "Power",
        "category": "Healing",
        "category_icon": "\U0001fa79",
        "weeks": "Weeks 4\u20138",
        "client_text": (
            "Find a private minute. Hit record on your phone. Then say something "
            "true \u2014 something that\u2019s been living inside you without sound.\n\n"
            "It doesn\u2019t have to be profound. I\u2019m tired of performing. I want more "
            "than this. I don\u2019t actually know what I want yet and that scares me. "
            "Whatever is true right now.\n\n"
            "You don\u2019t have to listen back. You don\u2019t have to share it with anyone. "
            "The practice is simply this: your voice, speaking the true thing, into "
            "the air, where it becomes real.\n\n"
            "The system taught you that your voice \u2014 especially in dissent, in desire, "
            "in need \u2014 was dangerous. This practice disagrees. Quietly. Privately. "
            "One true sentence at a time.\n\n"
            "There\u2019s something that happens when a true thing gets spoken aloud rather "
            "than staying in the body as thought. It becomes real in a different way. "
            "It takes up space. It arrives in the world as yours.\n\n"
            "That\u2019s the whole practice. Say the true thing. Let it be real."
        ),
        "mechanism": (
            "Externalizing internal experience through voice \u2014 one of the most powerful "
            "mechanisms for integrating what has been held in isolation. The specific "
            "instruction not to listen back removes the evaluative loop (I said it \u2192 "
            "I judge how it sounded \u2192 I manage the next saying). The voice goes out "
            "without being reviewed. Over time this builds the trust between knowing "
            "and saying."
        ),
        "how_to_introduce": (
            "\u201cThere\u2019s a practice I want to offer you, and it\u2019s completely private \u2014 "
            "you don\u2019t share it with me, you don\u2019t even have to listen to it yourself. "
            "You just say one true thing into your phone and let it go into the world.\u201d "
            "Watch their response. If there\u2019s immediate resistance: \u201cWhat\u2019s coming up "
            "as I describe that?\u201d The resistance is the practice\u2019s first gift."
        ),
        "what_to_watch_for": (
            "The client who makes the recordings but fills them with qualified, careful, "
            "palatable truths. The practice should gradually move toward rawer material. "
            "If it doesn\u2019t, gently ask: \u201cWhat\u2019s the thing you haven\u2019t recorded yet?\u201d "
            "The client who cries during the first recording \u2014 this is profound release, "
            "not dysfunction. Hold it with care."
        ),
        "when_to_adapt": None,
        "when_to_pause": None,
        "modality_roots": (
            "Narrative therapy, expressive arts therapy, voice and somatic work "
            "(Nadine George Voice Work)."
        ),
    },
    {
        "name": "The Watchtower",
        "domain": "Sovereignty",
        "category": "Pattern",
        "category_icon": "\U0001f504",
        "weeks": "Weeks 5\u20138",
        "client_text": (
            "A few times a day \u2014 especially when you notice yourself monitoring, "
            "reviewing, scanning for approval \u2014 ask one question:\n\n"
            "Am I in the tower?\n\n"
            "The tower is where you go when the old surveillance program is running. "
            "You know the feeling: checking how you\u2019re coming across, rehearsing "
            "explanations, bracing for consequences that aren\u2019t actually coming. "
            "Monitoring yourself from above, through someone else\u2019s eyes.\n\n"
            "When you notice you\u2019re there: name it. I\u2019m in the tower. No judgment. "
            "Just accurate location. Then find the ground. Feet on the floor. One "
            "thing you can touch right now. One breath out that\u2019s longer than the "
            "one before it.\n\n"
            "That\u2019s the climb down. You don\u2019t have to stay at ground level forever. "
            "Just practice knowing it exists."
        ),
        "mechanism": (
            "Interrupting the hypervigilance cycle that was adaptive inside the system "
            "(constant monitoring kept people safe from punishment) and is now running "
            "as default state outside it. The naming practice (\u201cI\u2019m in the tower\u201d) "
            "activates the prefrontal cortex\u2019s observing function \u2014 you cannot name an "
            "experience without having a degree of separation from it. That separation "
            "is the beginning of choice."
        ),
        "how_to_introduce": (
            "Tell the story first. \u201cThe system trained your nervous system to stay in "
            "a watchtower \u2014 permanently scanning for evaluation, for approval, for the "
            "consequence that might be coming. That was genuinely useful then. It\u2019s "
            "what kept you safe. It\u2019s running now without the threats it was built for.\u201d "
            "Then: \u201cThe only practice is noticing. Am I in the tower right now?\u201d "
            "Ask them in session: \u201cAre you in the tower right now?\u201d Often the answer "
            "is yes, and that in-session noticing is more powerful than any homework."
        ),
        "what_to_watch_for": (
            "The client who can name the tower state intellectually but doesn\u2019t feel "
            "the descent. The naming has become another performance. Bring it to the "
            "body: \u201cWhen you\u2019re in the tower \u2014 where do you feel that physically?\u201d "
            "Then: \u201cWhat shifts, even slightly, when you feel your feet on the floor "
            "right now?\u201d"
        ),
        "when_to_adapt": None,
        "when_to_pause": None,
        "modality_roots": (
            "Polyvagal theory (Stephen Porges, Deb Dana), IFS (identifying the "
            "protector parts), mindfulness-based approaches."
        ),
    },
    {
        "name": "The Mirror Voice",
        "domain": "Power",
        "category": "Pattern",
        "category_icon": "\U0001f504",
        "weeks": "Weeks 3\u20138",
        "client_text": (
            "Stand in front of a mirror. Make real eye contact with yourself \u2014 not "
            "a glance, actual contact. Then say one true sentence out loud.\n\n"
            "Start wherever you are. I\u2019m here. I\u2019m tired. I want something I haven\u2019t "
            "let myself want yet. The words matter less than the contact \u2014 you, "
            "meeting yourself, in the mirror, with your actual voice, saying something "
            "actually true.\n\n"
            "Three times a week. Two minutes. Build from small truths to larger ones "
            "across the weeks.\n\n"
            "By week four, let yourself say something about what you need. By week six, "
            "something about desire. By week eight, something you\u2019ve wanted in your "
            "intimate life that you\u2019ve been keeping in the quiet."
        ),
        "mechanism": (
            "Building the self-as-witness capacity. The system removed the client as "
            "reliable witness to their own experience \u2014 every self-perception was "
            "filtered through the system\u2019s evaluation. The mirror practice re-installs "
            "the self as a legitimate, trustworthy witness. The progressive build from "
            "neutral to intimate content gradually expands what can be witnessed."
        ),
        "how_to_introduce": (
            "\u201cHow do you feel about mirrors generally?\u201d The answer is clinical data. "
            "Many people from these systems have a fraught relationship with mirrors \u2014 "
            "the body under evaluation. Start there if needed. \u201cWhat if the mirror was "
            "just for contact \u2014 not evaluation?\u201d Introduce the practice as experiment, "
            "not prescription."
        ),
        "what_to_watch_for": (
            "Inability to maintain eye contact \u2014 very common, important, not a problem. "
            "\u201cNotice what happens when you make eye contact with yourself. What\u2019s the "
            "first thing that comes?\u201d Laughter is often the first thing \u2014 the nervous "
            "system releasing through humor. Tears are also common. Blankness \u2014 the "
            "same disconnection present in other domains, worth noting."
        ),
        "when_to_adapt": None,
        "when_to_pause": None,
        "modality_roots": (
            "Person-centered therapy (unconditional positive regard, self-as-subject), "
            "psychodrama, mindful self-compassion (Kristin Neff)."
        ),
    },
    {
        "name": "The Deed",
        "domain": "Power",
        "category": "Pattern",
        "category_icon": "\U0001f504",
        "weeks": "Weeks 5\u20138",
        "client_text": (
            "Once a week, find something you want to do \u2014 small enough to complete "
            "in a day \u2014 that you\u2019ve been waiting for permission to do. Not dramatic. "
            "Not a declaration. Just something small that\u2019s genuinely yours.\n\n"
            "Take it. Do it. Then write three words: I chose this.\n\n"
            "Week five: claim one hour of time that\u2019s purely, specifically yours.\n"
            "Week six: hold one feeling all the way through without routing it "
            "through anyone\u2019s evaluation.\n"
            "Week seven: say one true thing you\u2019d normally keep to yourself.\n"
            "Week eight: acknowledge one desire \u2014 let it exist without acting on it "
            "or suppressing it.\n\n"
            "Each week, the territory gets a little more interior. That\u2019s intentional. "
            "You\u2019re not just practicing doing things. You\u2019re practicing being the one "
            "who decides."
        ),
        "mechanism": (
            "Graduated self-authorization practice. The progressive structure is "
            "essential \u2014 starting with time (external, behavioral) and moving toward "
            "desire (internal, relational) mirrors the natural sequence of reclaiming "
            "power. The written \u201cI chose this\u201d creates a somatic anchor for the felt "
            "sense of genuine choice \u2014 over many repetitions, the body begins to "
            "recognize genuine choosing as distinct from compliance."
        ),
        "how_to_introduce": (
            "\u201cWhat\u2019s one thing you\u2019ve wanted to do this week that you haven\u2019t given "
            "yourself permission for?\u201d Whatever they name \u2014 check: is it genuinely "
            "theirs, or is it reactive to the system? If it\u2019s reactive: \u201cIs that "
            "something you actually want, or something you\u2019ve decided you should want "
            "because the system said you shouldn\u2019t?\u201d Real want vs. pendulum swing. "
            "Both are worth exploring, but they\u2019re different practices."
        ),
        "what_to_watch_for": (
            "The client who chooses things that are still fundamentally organized "
            "around pleasing or performing \u2014 \u201cI gave myself permission to rest, but "
            "I made sure the house was clean first.\u201d The permission is real but partial. "
            "Name it gently: \u201cI notice you still had to earn it.\u201d Also: the client who "
            "can\u2019t think of anything they want. That blankness about wanting is one of "
            "the most important things to sit with."
        ),
        "when_to_adapt": None,
        "when_to_pause": None,
        "modality_roots": (
            "ACT (values clarification and committed action), behavioral activation, "
            "somatic experiencing."
        ),
    },
    {
        "name": "The Body No",
        "domain": "Power",
        "category": "Pattern",
        "category_icon": "\U0001f504",
        "weeks": "Weeks 6\u20138",
        "client_text": (
            "Your no lives in your body before it becomes a word. It might be a "
            "tightening in your chest. Your stomach pulling back. A subtle closing. "
            "A breath that holds.\n\n"
            "This practice has one instruction: find your no before you need to use it.\n\n"
            "In a low-stakes moment \u2014 someone offers you something you don\u2019t want, "
            "asks for something that doesn\u2019t feel right \u2014 don\u2019t say the no yet. "
            "Just notice the physical signal first. Name it internally, wherever it "
            "lives: there it is.\n\n"
            "Your no is not an obstacle to intimacy. It is the architecture of it. "
            "No one can trust a yes that doesn\u2019t have a no available. Including you."
        ),
        "mechanism": (
            "Rebuilding the somatic-to-verbal pathway for refusal. The system "
            "specifically damaged this pathway \u2014 saying no was spiritually, "
            "relationally, and sometimes physically dangerous. The body learned to "
            "suppress the no signal before it became conscious. This practice works "
            "at the level of signal recovery, not behavioral change \u2014 finding the "
            "signal first, before asking anything of it."
        ),
        "how_to_introduce": (
            "\u201cI want to ask you something. In your body, right now \u2014 do you know "
            "where your no lives? When you imagine declining something you don\u2019t want, "
            "where do you feel that?\u201d If they can locate it: \u201cThat\u2019s what we\u2019re going "
            "to pay attention to this week.\u201d If they can\u2019t: start more broadly with any "
            "body sensation connected to preference \u2014 yes and no begin as the same "
            "somatic vocabulary."
        ),
        "what_to_watch_for": (
            "For clients in relationships where refusal has been dangerous, the "
            "in-session practice of finding the no is sufficient for weeks six and "
            "seven. Do not rush to actual external refusal. The body knowing its own "
            "no is the entire first phase of this work."
        ),
        "when_to_adapt": (
            "For clients in relationships where refusal has been dangerous, the "
            "in-session practice of finding the no is sufficient for weeks six and "
            "seven. Do not rush to actual external refusal."
        ),
        "when_to_pause": None,
        "modality_roots": (
            "Wheel of Consent (Betty Martin), somatic experiencing, "
            "trauma-informed sex therapy."
        ),
    },
    {
        "name": "The Pleasure Minute",
        "domain": "Nourishment",
        "category": "Resourcing",
        "category_icon": "\U0001f4da",
        "weeks": "Weeks 3\u20136",
        "client_text": (
            "One minute. That\u2019s it.\n\n"
            "Find something that is purely, simply pleasurable to one of your senses. "
            "Not productive. Not meaningful. Not earned. Just: this tastes good, or "
            "this feels good on my skin, or this sound is beautiful to me.\n\n"
            "Set a timer for one minute. Stay with the pleasure. The only instruction "
            "is to stay \u2014 not to analyze it, not to catalog it, not to appreciate it. "
            "Just to be in it.\n\n"
            "When guilt arrives \u2014 and it may \u2014 let it stand at the door. It doesn\u2019t "
            "have to come in. The pleasure gets the minute. The guilt can wait.\n\n"
            "You\u2019re allowed to feel good. Not because you\u2019ve earned it. Just because "
            "you\u2019re here."
        ),
        "mechanism": (
            "Expanding the window of pleasure tolerance. Most people from these "
            "systems have a very narrow pleasure window \u2014 they can tolerate brief, "
            "earned, justified pleasure. This practice gradually widens that window "
            "through repeated small experiences of staying with pleasure past the "
            "point where the shame interrupt usually fires."
        ),
        "how_to_introduce": (
            "Make it as low-stakes as possible. \u201cSomething with a good taste or a "
            "good texture or a good sound \u2014 something genuinely sensory, not an "
            "achievement.\u201d The client who says \u201cI enjoy reading\u201d \u2014 that\u2019s cognitive "
            "pleasure. We want somatic first. Help them find something physical."
        ),
        "what_to_watch_for": None,
        "when_to_adapt": None,
        "when_to_pause": None,
        "modality_roots": (
            "Sensate focus (adapted), mindfulness-based sex therapy, "
            "somatic experiencing."
        ),
    },
    {
        "name": "The Origin Question",
        "domain": "Sovereignty",
        "category": "Resourcing",
        "category_icon": "\U0001f4da",
        "weeks": "Any week",
        "client_text": (
            "When shame arrives \u2014 and it will, because it does \u2014 ask one question "
            "before you accept it:\n\n"
            "Where did I first learn this was shameful?\n\n"
            "Not as a way to avoid the shame. Not to intellectualize your way out of it. "
            "Just to check: is this shame generated, or is this shame installed?\n\n"
            "Generated shame says: I actually did something that conflicts with my own "
            "values. That shame is useful \u2014 it\u2019s information about who I want to be.\n\n"
            "Installed shame says: someone told me this was shameful, and I absorbed "
            "the verdict before I had the capacity to question it.\n\n"
            "When the answer traces back to a doctrine, a parent\u2019s voice, a community "
            "rule, a system \u2014 that\u2019s installed shame. And installed shame has a "
            "return address."
        ),
        "mechanism": (
            "Installing a discriminatory capacity between authentic moral response "
            "and installed cultural/religious shame. This is foundational psychoeducation "
            "but delivered as a somatic practice \u2014 the client is invited to feel the "
            "difference between the two kinds of shame, not just understand it conceptually."
        ),
        "how_to_introduce": (
            "Often best introduced in session when shame is present live. \u201cCan we stay "
            "with that for a moment? When that shame arrived just now \u2014 do you know "
            "where it came from? Not where you first felt it \u2014 where it was originally "
            "taught.\u201d The in-session version is more powerful than any homework."
        ),
        "what_to_watch_for": None,
        "when_to_adapt": None,
        "when_to_pause": None,
        "modality_roots": (
            "Narrative therapy (externalizing), IFS (identifying the origin of "
            "critical/shaming parts), feminist psychology."
        ),
    },
    {
        "name": "The Want Before the Why",
        "domain": "Nourishment",
        "category": "Resourcing",
        "category_icon": "\U0001f4da",
        "weeks": "Weeks 2\u20136",
        "client_text": (
            "When a want arises \u2014 any want \u2014 practice saying it to yourself before "
            "evaluating it.\n\n"
            "I want ___.\n\n"
            "Nothing after the sentence yet. Not: I want this but I probably shouldn\u2019t. "
            "Not: I want this but it\u2019s too much. Just: I want ___.\n\n"
            "Let the want exist in the room for ten seconds before you do anything "
            "with it. Ten seconds of the want being real before the evaluation begins.\n\n"
            "Over time the ten seconds becomes twenty. Then a minute. Then you find "
            "yourself noticing what you want with a kind of spacious curiosity rather "
            "than a running moral audit.\n\n"
            "That spaciousness is your appetite coming back to life."
        ),
        "mechanism": None,
        "how_to_introduce": None,
        "what_to_watch_for": None,
        "when_to_adapt": None,
        "when_to_pause": None,
        "modality_roots": None,
    },
    {
        "name": "The Somatic Check-In",
        "domain": "All",
        "category": "Resourcing",
        "category_icon": "\U0001f4da",
        "weeks": "Every session",
        "client_text": (
            "Before any significant conversation, any intimate encounter, any moment "
            "that matters \u2014 thirty seconds.\n\n"
            "Hand on belly. Hand on heart. One breath that goes all the way down.\n\n"
            "Then ask: What\u2019s here?\n\n"
            "Not what should be here. Not what you want to be here. What\u2019s actually "
            "present in your body right now.\n\n"
            "This practice does one thing: it brings you into the room before the room "
            "begins. It makes you a participant rather than someone things happen to.\n\n"
            "Thirty seconds. One hand. One question. That\u2019s enough to change what follows."
        ),
        "mechanism": None,
        "how_to_introduce": None,
        "what_to_watch_for": None,
        "when_to_adapt": None,
        "when_to_pause": None,
        "modality_roots": None,
    },
    {
        "name": "The Return Letter",
        "domain": "Sovereignty",
        "category": "Pattern",
        "category_icon": "\U0001f504",
        "weeks": "Single session",
        "client_text": (
            "Choose one shame. One specific thing you carry that the system gave you \u2014 "
            "desire, doubt, orientation, the wanting itself, the body you live in, "
            "the questions you couldn\u2019t stop asking.\n\n"
            "Write it a letter. Three sentences is enough:\n\n"
            "This shame was handed to me. I did not choose it and I did not generate it. "
            "I return it to its source, and I reclaim the space it occupied.\n\n"
            "Read it out loud. Then do something ritual with it \u2014 burn it, bury it, "
            "tear it into small pieces and let them go. The ritual matters because the "
            "body learns through ceremony what the mind understands through information.\n\n"
            "The shame may return \u2014 installed things don\u2019t leave cleanly. But when "
            "it returns, something will be different. There\u2019s a returned letter in your "
            "history now. You\u2019ve said, on record, in your own voice: this was never mine "
            "to carry."
        ),
        "mechanism": None,
        "how_to_introduce": None,
        "what_to_watch_for": None,
        "when_to_adapt": None,
        "when_to_pause": None,
        "modality_roots": None,
    },
    {
        "name": "The Laboratory",
        "domain": "Identity / Nourishment",
        "category": "Exploring",
        "category_icon": "\U0001f331",
        "weeks": "Weeks 4 onward",
        "client_text": (
            "Something drew your attention this week. An attraction, a curiosity, "
            "a pull toward something you\u2019ve either never let yourself look at directly "
            "or something that surprised you.\n\n"
            "Write it down without evaluation. Then three questions:\n\n"
            "What drew me?\n"
            "What did I notice in my body when I paid attention?\n"
            "Would I be curious to look at this again?\n\n"
            "No conclusions. No decisions. No meaning-making yet. Just data collection.\n\n"
            "You are a hypothesis worth testing. The lab is open. What are you curious "
            "about today?"
        ),
        "mechanism": None,
        "how_to_introduce": None,
        "what_to_watch_for": None,
        "when_to_adapt": None,
        "when_to_pause": None,
        "modality_roots": None,
    },
    {
        "name": "The Arrival Practice",
        "domain": "Embodiment",
        "category": "Pattern",
        "category_icon": "\U0001f504",
        "weeks": "Before intimate encounters",
        "client_text": (
            "Before intimacy \u2014 with yourself or another person \u2014 three minutes of "
            "arriving first.\n\n"
            "Alone, before anything else begins: both hands on your body. One breath "
            "to feel your feet on the floor. One question, asked with genuine curiosity "
            "rather than evaluation: what is alive in my body right now?\n\n"
            "Not: am I ready? Not: should I want this? Just: what\u2019s actually present?\n\n"
            "This practice creates a tiny, important pause between stimulus and response "
            "\u2014 a breath of space where you exist as a subject, not an object. In that "
            "space, you can choose. From the inside.\n\n"
            "That pause is sovereignty in practice."
        ),
        "mechanism": None,
        "how_to_introduce": None,
        "what_to_watch_for": None,
        "when_to_adapt": None,
        "when_to_pause": None,
        "modality_roots": None,
    },
]


# Category colors mapping
CATEGORY_COLORS = {
    "Healing": C["healing"],
    "Pattern": C["pattern"],
    "Resourcing": C["resourcing"],
    "Exploring": C["exploring"],
}


# ─────────────────────────────────────────────
# PAGE CALLBACKS
# ─────────────────────────────────────────────

def _cover_page(canvas, doc):
    """Cover with deep sage gradient."""
    canvas.saveState()
    top = C["coach_cover"]
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
    make_header_footer(canvas, doc, section_name="Facilitator\u2019s Guide")


# ─────────────────────────────────────────────
# COVER
# ─────────────────────────────────────────────

def _build_cover():
    """Cover page: deep sage, professional."""
    elements = []
    elements.append(Spacer(1, 100))

    title_style = ParagraphStyle(
        "CoachCoverTitle", fontName=FONTS["heading"], fontSize=36, leading=42,
        textColor=C["white"], alignment=TA_LEFT, spaceAfter=8,
    )
    elements.append(Paragraph("THAT DEEPER FEELING", title_style))

    sub_style = ParagraphStyle(
        "CoachCoverSub", fontName=FONTS["body"], fontSize=14, leading=20,
        textColor=Color(0.85, 0.88, 0.84), alignment=TA_LEFT, spaceAfter=4,
    )
    elements.append(Paragraph("Conscious Intimacy Coaching", sub_style))
    elements.append(Spacer(1, 24))
    elements.append(DividerLine())
    elements.append(Spacer(1, 24))

    center_style = ParagraphStyle(
        "CoachCoverCenter", fontName=FONTS["heading_italic"], fontSize=18, leading=26,
        textColor=C["page_bg"], alignment=TA_LEFT, spaceAfter=6,
    )
    elements.append(Paragraph("The Facilitator\u2019s Guide", center_style))
    elements.append(Paragraph("& Practice Catalog", center_style))
    elements.append(Spacer(1, 24))
    elements.append(DividerLine())
    elements.append(Spacer(1, 30))

    note_style = ParagraphStyle(
        "CoachCoverNote", fontName=FONTS["body_italic"], fontSize=11, leading=16,
        textColor=Color(0.75, 0.78, 0.74), alignment=TA_LEFT,
    )
    elements.append(Paragraph(
        "For practitioners of the SPINE framework.",
        note_style
    ))
    elements.append(Paragraph(
        "This document is not client-facing.",
        note_style
    ))

    elements.append(NextPageTemplate("content"))
    elements.append(PageBreak())
    return elements


# ─────────────────────────────────────────────
# SECTION 1: THE PRACTITIONER'S POSTURE
# ─────────────────────────────────────────────

def _build_practitioners_posture():
    """Section 1: Who You Are In This Work."""
    elements = []
    elements.extend(section_break("Section 1: Who You Are In This Work"))
    elements.append(Spacer(1, 8))

    # The Practitioner's Posture
    elements.append(Paragraph("The Practitioner\u2019s Posture", STYLES["h2"]))
    elements.append(Spacer(1, 8))

    paras = [
        "You are not a therapist in this room \u2014 even if you are one outside it.",

        "The distinction matters.",

        "Therapy works primarily with what\u2019s broken. This framework works primarily "
        "with what\u2019s growing. The posture is different. The interventions are different. "
        "The relationship is different.",

        "You are the person who holds the container. You create the conditions. You model "
        "that it\u2019s safe to be unsettled \u2014 that uncertainty is survivable, that desire "
        "is allowed, that the body can be trusted.",

        "You are the evidence that leaving the system doesn\u2019t mean losing yourself.",

        "The first qualification for facilitating this work is doing it.",
    ]
    for p in paras:
        elements.append(voice_paragraph(p))
        elements.append(Spacer(1, 2))

    elements.append(PageBreak())

    # The Practitioner's Own Map
    elements.append(Paragraph("The Practitioner\u2019s Own Map", STYLES["h2"]))
    elements.append(Spacer(1, 8))

    own_map_paras = [
        "Before you facilitate this work for anyone else, complete your own SPINE "
        "assessment. Not as homework. As honest inquiry.",

        "Where is your anchor? What does your own shape look like? Where are your "
        "edges \u2014 the places where your own system-exit is still incomplete, where "
        "your own shame sources are still active?",

        "You don\u2019t need to be finished with your own work to facilitate this. "
        "You need to be in it. The client needs to sense that you\u2019re not asking "
        "them to go somewhere you haven\u2019t been willing to go yourself.",

        "Your map will also reveal your facilitation risks \u2014 the places where a "
        "client\u2019s material is most likely to activate your own. This isn\u2019t a "
        "problem. It\u2019s information. Supervised facilitators bring their own "
        "activation patterns to supervision regularly.",
    ]
    for p in own_map_paras:
        elements.append(voice_paragraph(p))
        elements.append(Spacer(1, 2))

    elements.append(Spacer(1, 12))

    # Reflection questions
    elements.append(Paragraph("Reflection questions for your own map:", STYLES["h3"]))
    elements.append(Spacer(1, 4))

    reflections = [
        "Which domain activated most strongly when you completed the assessment?",
        "Where did your body check show distress or blankness?",
        "What shame sources still carry significant charge for you?",
        "Where is the gap between your current and vision scores widest?",
        "What is the one thing you\u2019re most afraid a client will bring to session?",
    ]
    for r in reflections:
        elements.append(Paragraph(f"\u2022  {r}", STYLES["body"]))
        elements.append(Spacer(1, 4))

    elements.append(PageBreak())

    # Reading the Room
    elements.append(Paragraph("Reading the Room", STYLES["h2"]))
    elements.append(Spacer(1, 8))

    room_states = [
        ("What flooding looks like:",
         "Rapid speech, tears that won\u2019t stop, inability to track the conversation, "
         "repetitive circling over the same content, visible agitation. The nervous system "
         "is overwhelmed. Don\u2019t add content. Don\u2019t process. Ground. \u201cLet\u2019s slow down. "
         "Feel your feet. Tell me one thing you can see right now.\u201d Stay with grounding "
         "until the nervous system settles. Then ask: \u201cWhat just happened in your body?\u201d"),

        ("What shutdown looks like:",
         "Flat affect, monosyllabic responses, gaze going vacant, \u201cI don\u2019t know\u201d to "
         "everything, body going still. The nervous system has withdrawn. Don\u2019t push "
         "through. Acknowledge: \u201cSomething just shifted. Your body went somewhere else.\u201d "
         "If they can\u2019t come back: \u201cYou don\u2019t need to come back right now. I\u2019m here "
         "when you\u2019re ready.\u201d Sometimes the session\u2019s most important moment is the "
         "practitioner sitting quietly with someone who\u2019s gone offline."),

        ("What intellectualization looks like:",
         "Articulate, analytical, insightful \u2014 and completely disconnected from the "
         "body. The client can describe their patterns perfectly while maintaining "
         "total distance from the felt experience. This is the system\u2019s most sophisticated "
         "defense \u2014 understanding as avoidance. Interrupt gently: \u201cYou\u2019re describing "
         "this really clearly. Where is it living in your body right now?\u201d"),

        ("What performance looks like:",
         "The client who is \u201cdoing the work perfectly.\u201d Every practice completed, "
         "insightful observations, performative vulnerability. Watch for: the work "
         "being offered to you rather than experienced by them. \u201cWho is this for "
         "right now? Is this for you, or for me?\u201d"),
    ]

    for heading, text in room_states:
        elements.append(Paragraph(heading, STYLES["h3"]))
        elements.append(Spacer(1, 4))
        elements.append(voice_paragraph(text))
        elements.append(Spacer(1, 8))

    elements.append(PageBreak())

    # The Five Facilitation Principles
    elements.append(Paragraph("The Five Facilitation Principles", STYLES["h2"]))
    elements.append(Spacer(1, 12))

    principles = [
        ("1. Curiosity over correction",
         "You are not here to fix. You are here to wonder. When a client brings "
         "something \u2014 a shame pattern, a body response, a relational dynamic \u2014 "
         "the first move is always curiosity. \u201cTell me more about that.\u201d Not: "
         "\u201cHave you tried\u2026\u201d The moment you correct, you become the system."),

        ("2. Body before mind",
         "The insight that matters is the one the body holds. When a client "
         "understands something intellectually but the body hasn\u2019t caught up: "
         "the body is right. Always check in with the body before, during, and "
         "after any significant work. \u201cWhere does that land right now?\u201d"),

        ("3. Both irreducible moments, always",
         "Every significant shift in this framework involves two experiences: "
         "the unauthorized feeling (something true that wasn\u2019t allowed inside "
         "the system) and the non-evaluative witness (someone who receives it "
         "without judgment). Your primary job is the second one. Create the "
         "conditions for the first and then be the witness."),

        ("4. The session belongs to them",
         "Your agenda is secondary. If a client arrives with something alive "
         "and urgent, follow it \u2014 even if it means the planned work doesn\u2019t "
         "happen. The practice prescription is a guide, not a curriculum. "
         "What\u2019s alive in the room is always more important than what\u2019s "
         "planned on the page."),

        ("5. Know your edges",
         "You will encounter material that activates you. Orientation. Desire. "
         "Trauma. Theology. Know where your edges are. Know what you need to "
         "bring to supervision. The client doesn\u2019t need you to be unactivated. "
         "They need you to be honest about your activation rather than "
         "performing neutrality."),
    ]

    for heading, text in principles:
        elements.append(Paragraph(heading, STYLES["h3"]))
        elements.append(Spacer(1, 4))
        elements.append(voice_paragraph(text))
        elements.append(Spacer(1, 8))

    elements.append(PageBreak())
    return elements


# ─────────────────────────────────────────────
# SECTION 2: THE DIFFERENTIAL GUIDE
# ─────────────────────────────────────────────

def _build_differential_guide():
    """Section 2: The three categories and how to read them."""
    elements = []
    elements.extend(section_break("Section 2: The Differential Guide"))
    elements.append(Spacer(1, 8))

    intro = (
        "Every sub-dimension on the SPINE map falls into one of three categories "
        "based on the intersection of score, shame intensity, and body response. "
        "The category determines what kind of intervention is appropriate \u2014 and "
        "what kind will do harm."
    )
    elements.append(voice_paragraph(intro))
    elements.append(Spacer(1, 12))

    categories = [
        {
            "name": "Resourcing",
            "icon": "\U0001f4da",
            "color": C["resourcing"],
            "description": (
                "Score under 50%, low shame, body at curiosity or mild resistance. "
                "This territory wasn\u2019t heavily damaged \u2014 it just wasn\u2019t built. "
                "The client needs new input, new experiences, new vocabulary."
            ),
            "in_the_room": (
                "Curiosity. Openness. Energy. The client leans in when you introduce "
                "practices in this domain. They may even enjoy it. That enjoyment is "
                "real \u2014 this is the growth edge, not the wound edge."
            ),
            "what_helps": (
                "Exploration. New language. Permission. The Pleasure Minute, The "
                "Want Before the Why, The Curiosity Shelf. Practices that introduce "
                "something new rather than processing something old."
            ),
            "what_doesnt": (
                "Deep somatic processing. Intensive shame work. Trauma protocols. "
                "The territory doesn\u2019t need healing \u2014 it needs building. Treating it "
                "like a wound creates a wound where there wasn\u2019t one."
            ),
            "when_to_refer": (
                "When the apparent low shame turns out to be dissociation. If the "
                "body check is blankness rather than curiosity, re-assess: what looks "
                "like readiness may be disconnection."
            ),
        },
        {
            "name": "Pattern",
            "icon": "\U0001f504",
            "color": C["pattern"],
            "description": (
                "Score under 60%, moderate shame (3\u20134), body at resistance or "
                "significant resistance. The old system\u2019s patterns are still running \u2014 "
                "not as acute wounds but as default operating procedures. The client "
                "needs to see them, name them, and interrupt them."
            ),
            "in_the_room": (
                "Resistance that has intelligence in it. The client isn\u2019t flooding \u2014 "
                "they\u2019re bracing. They may argue, intellectualize, or deflect. The "
                "resistance is the pattern in real time. Name it, gently."
            ),
            "what_helps": (
                "Naming. Visibility. Choice points. The Watchtower, The Mirror Voice, "
                "The Deed, The Body No. Practices that interrupt the automatic sequence "
                "and insert a moment of choice."
            ),
            "what_doesnt": (
                "Pushing through the resistance. Behavioral prescriptions that bypass "
                "the body. \u201cJust try saying no more.\u201d The pattern needs to be seen and "
                "understood before it can be changed."
            ),
            "when_to_refer": (
                "When pattern work reveals deeper trauma underneath the patterns. "
                "When the resistance escalates rather than softening over multiple "
                "sessions. When the patterns are relational and require couples or "
                "family therapy to address."
            ),
        },
        {
            "name": "Healing",
            "icon": "\U0001fa79",
            "color": C["healing"],
            "description": (
                "Score under 50%, high shame (4\u20135), body at distress or blankness. "
                "This territory carries active wounding. The nervous system is in "
                "protection mode. Intervention must be slow, titrated, and "
                "trauma-informed."
            ),
            "in_the_room": (
                "Distress. Flooding. Shutdown. Tears that come before words. Body "
                "responses that are disproportionate to the content. Dissociation \u2014 "
                "the client leaves the room without physically leaving. These are "
                "not problems. They are the body saying: this territory is not safe yet."
            ),
            "what_helps": (
                "Titration. Slow, repeated, body-first practices. The Daily Return, "
                "The Lighthouse, The Witnessed Voice. Grounding before and after every "
                "session that touches this territory. Concurrent therapy for anything "
                "that activates traumatic memory."
            ),
            "what_doesnt": (
                "Moving fast. Cognitive reframing. \u201cYou\u2019re safe now\u201d (the body decides "
                "when it\u2019s safe, not the practitioner). Exposure without titration. "
                "Processing without grounding. Insight without integration."
            ),
            "when_to_refer": (
                "Always refer for concurrent therapy when a domain shows healing "
                "indicators. This work is not therapy. When stability is below 5/10, "
                "when trauma responses are acute and persistent, when suicidal ideation "
                "or self-harm is present \u2014 these require clinical containment that this "
                "framework is not designed to provide."
            ),
        },
    ]

    for cat in categories:
        elements.append(ColorStripe(cat["color"], height=6))
        elements.append(Spacer(1, 8))

        cat_h2 = ParagraphStyle(
            f"CatH2_{cat['name']}", fontName=FONTS["heading"], fontSize=20, leading=26,
            textColor=cat["color"], alignment=TA_LEFT, spaceAfter=8,
        )
        elements.append(Paragraph(f"{cat['icon']}  {cat['name']}", cat_h2))
        elements.append(voice_paragraph(cat["description"]))
        elements.append(Spacer(1, 4))

        sections = [
            ("What it looks like in the room:", cat["in_the_room"]),
            ("What helps:", cat["what_helps"]),
            ("What doesn\u2019t:", cat["what_doesnt"]),
            ("When to refer:", cat["when_to_refer"]),
        ]
        for heading, text in sections:
            elements.append(Paragraph(heading, STYLES["h3"]))
            elements.append(Spacer(1, 2))
            elements.append(Paragraph(text, STYLES["body"]))
            elements.append(Spacer(1, 6))

        elements.append(Spacer(1, 12))

    elements.append(PageBreak())
    return elements


# ─────────────────────────────────────────────
# SECTION 3: THE PRACTICE CATALOG
# ─────────────────────────────────────────────

def _build_practice_entry(practice):
    """Build a single practice entry with client and practitioner sections."""
    elements = []
    domain = practice["domain"]
    category = practice["category"]
    cat_color = CATEGORY_COLORS.get(category, C["primary"])
    domain_color = DOMAIN_COLORS.get(domain, C["primary"]) if domain != "All" and "/" not in domain else C["accent"]

    # Practice header box
    elements.append(ColorStripe(domain_color, height=4))
    elements.append(Spacer(1, 8))

    # Title
    title_style = ParagraphStyle(
        f"PractTitle_{practice['name']}", fontName=FONTS["heading"], fontSize=18, leading=24,
        textColor=C["text"], alignment=TA_LEFT, spaceAfter=4,
    )
    elements.append(Paragraph(practice["name"].upper(), title_style))

    # Meta line
    meta_style = ParagraphStyle(
        f"PractMeta_{practice['name']}", fontName=FONTS["body"], fontSize=10, leading=14,
        textColor=C["subtext"], alignment=TA_LEFT, spaceAfter=8,
    )
    elements.append(Paragraph(
        f"{practice['domain']}  \u00b7  {practice['category_icon']} {practice['category']}  \u00b7  {practice['weeks']}",
        meta_style
    ))
    elements.append(SectionDivider())
    elements.append(Spacer(1, 8))

    # FOR THE CLIENT section
    client_h = ParagraphStyle(
        f"ClientH_{practice['name']}", fontName=FONTS["heading"], fontSize=14, leading=20,
        textColor=C["accent"], alignment=TA_LEFT, spaceAfter=6,
    )
    elements.append(Paragraph("FOR THE CLIENT:", client_h))
    elements.append(Spacer(1, 4))

    # Split client text by double newlines for paragraphs
    for para in practice["client_text"].split("\n\n"):
        para = para.strip()
        if para:
            elements.append(voice_paragraph(para))
            elements.append(Spacer(1, 2))

    elements.append(Spacer(1, 12))

    # FOR THE PRACTITIONER section (only if there's content)
    has_practitioner_content = any([
        practice.get("mechanism"),
        practice.get("how_to_introduce"),
        practice.get("what_to_watch_for"),
        practice.get("when_to_adapt"),
        practice.get("when_to_pause"),
        practice.get("modality_roots"),
    ])

    if has_practitioner_content:
        pract_h = ParagraphStyle(
            f"PractH_{practice['name']}", fontName=FONTS["heading"], fontSize=14, leading=20,
            textColor=C["secondary"], alignment=TA_LEFT, spaceAfter=6,
        )
        elements.append(Paragraph("FOR THE PRACTITIONER:", pract_h))
        elements.append(Spacer(1, 4))

        note_pairs = [
            ("What this practice is actually doing:", practice.get("mechanism")),
            ("How to introduce it in session:", practice.get("how_to_introduce")),
            ("What to watch for:", practice.get("what_to_watch_for")),
            ("When to adapt it:", practice.get("when_to_adapt")),
            ("When to pause it:", practice.get("when_to_pause")),
            ("Modality roots:", practice.get("modality_roots")),
        ]

        for heading, text in note_pairs:
            if text:
                elements.append(Paragraph(heading, STYLES["h3"]))
                elements.append(Spacer(1, 2))
                elements.append(Paragraph(text, STYLES["facilitator"]))
                elements.append(Spacer(1, 6))

    elements.append(Spacer(1, 8))
    elements.append(DividerLine())
    elements.append(Spacer(1, 12))

    return elements


def _build_practice_catalog():
    """Section 3: The Complete Practice Catalog."""
    elements = []
    elements.extend(section_break("Section 3: The Complete Practice Catalog"))
    elements.append(Spacer(1, 8))

    intro = (
        "Every practice in this catalog is written twice: once in Kimberly\u2019s voice "
        "for the client, and once in clinical language for the practitioner. "
        "The client version is what gets shared. The practitioner version is what "
        "informs your facilitation."
    )
    elements.append(voice_paragraph(intro))
    elements.append(Spacer(1, 16))

    for practice in FULL_PRACTICES:
        elements.extend(_build_practice_entry(practice))

    return elements


# ─────────────────────────────────────────────
# SECTION 4: THE SESSION GUIDE
# ─────────────────────────────────────────────

def _build_session_guide():
    """Section 4: Standard Session Arc."""
    elements = []
    elements.extend(section_break("Section 4: The Session Guide"))
    elements.append(Spacer(1, 8))

    elements.append(Paragraph("Standard Session Arc", STYLES["h2"]))
    elements.append(Spacer(1, 8))

    session_blocks = [
        {
            "time": "Opening (5\u201310 minutes)",
            "content": (
                "Body check-in. One word for the body, one word for the mind. "
                "No commentary from the practitioner \u2014 just receiving. "
                "Then: \u201cWhat are you bringing today?\u201d"
            ),
        },
        {
            "time": "Practice Review (5\u201310 minutes)",
            "content": (
                "\u201cWhat did you notice?\u201d Not \u201cdid you do it\u201d \u2014 \u201cwhat did you notice?\u201d "
                "The practice is a data-collection mechanism. The data is what matters.\n\n"
                "If they didn\u2019t do it: \u201cWhat happened when you thought about doing it?\u201d "
                "Avoidance is always information. Never shame."
            ),
        },
        {
            "time": "Session Work (30\u201340 minutes)",
            "content": (
                "One axis or theme from their results map. Body-first throughout. "
                "When in doubt \u2014 \u201cwhere does that land in your body right now?\u201d"
            ),
        },
        {
            "time": "Closing (10 minutes)",
            "content": (
                "\u201cWhat\u2019s landing from today?\u201d One practice for the week \u2014 specific, "
                "achievable, connected to today\u2019s work. Grounding. \u201cWhere are you "
                "leaving from today \u2014 in your body?\u201d"
            ),
        },
    ]

    for block in session_blocks:
        elements.append(Paragraph(block["time"], STYLES["time_block"]))
        elements.append(Spacer(1, 4))
        for para in block["content"].split("\n\n"):
            para = para.strip()
            if para:
                elements.append(Paragraph(para, STYLES["body"]))
                elements.append(Spacer(1, 4))
        elements.append(Spacer(1, 10))

    return elements


# ─────────────────────────────────────────────
# MAIN GENERATOR
# ─────────────────────────────────────────────

def generate_coaches_guide(output_dir="documents"):
    """Generate the Coach's Guide & Practice Catalog PDF."""
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "coaches_guide_practice_catalog.pdf")

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
    elements.extend(_build_practitioners_posture())
    elements.extend(_build_differential_guide())
    elements.extend(_build_practice_catalog())
    elements.extend(_build_session_guide())

    doc.build(elements)
    print(f"  Generated: {output_path}")
    return output_path


if __name__ == "__main__":
    generate_coaches_guide()
