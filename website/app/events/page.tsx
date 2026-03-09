'use client';

import Button from '@/components/ui/Button';
import Image from 'next/image';

export default function EventsPage() {
  return (
    <>
      {/* Hero Section */}
      <section className="retreat-hero">
        <div className="container content-container">
          <h1>Reclaiming the Forbidden</h1>
          <p className="hero-tagline">
            A Women&rsquo;s Retreat
          </p>
          <div className="hero-details">
            <p className="hero-date">April 24&ndash;26, 2026</p>
            <p className="hero-location">St. George, Utah</p>
          </div>
          <p className="hero-hook">
            If being a &ldquo;good girl&rdquo; kept you safe but cost you your truth&hellip;
          </p>
          <p className="hero-declaration">this weekend is for you.</p>
          <Button href="/events/register" variant="primary">
            Reserve Your Spot
          </Button>
        </div>
      </section>

      {/* About the Retreat */}
      <section className="retreat-about">
        <div className="container content-container">
          <div className="about-layout">
            <div className="about-inner">
              <h2>About the Retreat</h2>
              <p>
                Reclaiming the Forbidden is a three-day immersive retreat for women navigating life after high-demand religion, rigid belief systems, or environments where obedience was prioritized over self-trust.
              </p>
              <p className="emphasis-line">This isn&rsquo;t about rebellion for rebellion&rsquo;s sake.</p>
              <p className="emphasis-line">It&rsquo;s about reclamation.</p>
              <p>
                It&rsquo;s about discovering that you don&rsquo;t have to white-knuckle obedience or free-fall into chaos. There is a third path.
              </p>
            </div>
            <div className="about-image">
              <Image
                src="/images/retreat-rear.jpg"
                alt="Private luxury retreat home with pool at sunset"
                width={600}
                height={400}
                className="section-photo"
              />
            </div>
          </div>
        </div>
      </section>

      {/* What We'll Explore */}
      <section className="retreat-explore">
        <div className="container content-container">
          <h2>What We&rsquo;ll Explore</h2>
          <p className="explore-intro">Over the course of the weekend, we will:</p>
          <ul className="explore-list">
            <li>Reconnect to the body through somatic and embodiment practices</li>
            <li>Untangle shame from identity</li>
            <li>Explore the Pendulum Framework (locked &rarr; severed &rarr; contained)</li>
            <li>Reclaim internal authority</li>
            <li>Experience Eros as life force, not performance</li>
            <li>Integrate through guided teaching, small groups, and intentional reflection</li>
          </ul>

          <h3 className="and-yes-heading">And yes&hellip; there will be:</h3>
          <ul className="and-yes-list">
            <li>A dance party like it&rsquo;s 1999</li>
            <li>Slumber party energy and sisterhood</li>
            <li>Nourishing meals</li>
            <li>Slow mornings</li>
            <li>Real conversations</li>
            <li>Play, depth, and containment</li>
          </ul>

          <div className="retreat-philosophy">
            <p>This retreat is intentionally balanced between depth and joy.</p>
            <p className="emphasis-line">We move slowly.</p>
            <p className="emphasis-line">We prioritize nervous system safety.</p>
            <p className="emphasis-line">We build trust before exploration.</p>
            <p>You will not be forced to share.</p>
            <p>You will not be pushed beyond your edge.</p>
            <p className="emphasis-line">You will be invited into yourself.</p>
          </div>
        </div>
      </section>

      {/* The Framework Behind This Work */}
      <section className="retreat-framework">
        <div className="container content-container">
          <h2>The Framework Behind This Work</h2>
          <p>This retreat draws from the foundational framework behind That Deeper Feeling.</p>
          <p>Through my own journey of leaving high-demand religion and navigating the space between identities, I began noticing something important.</p>
          <p className="emphasis-line">Most systems treat the human experience in pieces.</p>
          <div className="framework-separations">
            <p>Mental health is separated from emotional healing.</p>
            <p>Spirituality is separated from sexuality.</p>
            <p>The body is separated from belief.</p>
          </div>
          <p>But in real life, these parts of us are deeply connected.</p>
          <div className="framework-connections">
            <p>A belief system can shape our sexuality.</p>
            <p>Emotional wounds can live in the body.</p>
            <p>Spiritual identity can influence personal power.</p>
          </div>
          <p>The work I guide people through explores the full human experience across five core energies:</p>
          <ul className="energy-list">
            <li>Mental</li>
            <li>Emotional</li>
            <li>Physical</li>
            <li>Spiritual</li>
            <li>Sexual</li>
          </ul>
          <p>These energies are constantly interacting with one another.</p>
          <p>When one area shifts, the others often begin to move as well.</p>

          <h3 className="spine-heading">The SPINE Pathway</h3>
          <p>The larger body of work behind That Deeper Feeling is structured through a pathway called SPINE.</p>
          <ul className="spine-list">
            <li><strong>S</strong>overeignty</li>
            <li><strong>P</strong>lay</li>
            <li><strong>I</strong>ntegration</li>
            <li><strong>N</strong>avigation</li>
            <li><strong>E</strong>quilibrium</li>
          </ul>
          <p>This retreat focuses primarily on the first two stages of that journey.</p>
          <div className="spine-focus">
            <div className="spine-stage">
              <h4>Sovereignty</h4>
              <p>Reclaiming authority over your life, your voice, your body, and your choices.</p>
            </div>
            <div className="spine-stage">
              <h4>Play</h4>
              <p>Exploring curiosity, embodiment, and rediscovery without shame or rigidity.</p>
            </div>
          </div>
          <p>For many women leaving high-demand systems or rigid identities, these are the first two doors that begin opening again.</p>
          <p className="emphasis-line">The return to self-trust and the rediscovery of aliveness in the body.</p>

          <h3 className="why-heading">Why This Matters</h3>
          <p>Many women who come to this work are navigating seasons of transition.</p>
          <ul className="transition-list">
            <li>Leaving high-demand religion</li>
            <li>Divorce or relationship shifts</li>
            <li>Motherhood and rediscovering themselves again</li>
            <li>Midlife awakenings</li>
            <li>Career changes</li>
            <li>The quiet realization that the life they built no longer fits the person they&rsquo;re becoming</li>
          </ul>
          <p>This retreat is designed to hold space for that in-between.</p>
          <p className="emphasis-line">Not rushing toward answers.</p>
          <p>But allowing curiosity, embodiment, connection, and community to guide the process.</p>
        </div>
      </section>

      {/* Guest Facilitator */}
      <section className="retreat-facilitator">
        <div className="container content-container">
          <div className="facilitator-content">
            <h2>Guest Facilitator: Dr. Somer Nicole</h2>
            <p>
              Dr. Somer Nicole is a Sensual Somatic Therapist, Nervous System Educator, and S Factor Teacher with over 20 years of experience bridging science and soul. A Doctor of Physical Therapy, she specializes in restoring physiological safety, embodied presence, and the reclamation of personal power. Embodying the Somatic Dominatrix, her work merges nervous system science, somatic ritual, and feminine embodiment, guiding clients to meet resistance, reclaim instinct, and transmute fear into vitality while integrating both shadow and light as sacred expressions of wholeness.
            </p>
            <div className="sfactor-note">
              <h3>What is S Factor?</h3>
              <p>
                S Factor is a sensual movement practice designed to reconnect women to their bodies, their instinct, and their life-force energy through embodied movement.
              </p>
              <p className="emphasis-line">It is not choreography or performance.</p>
              <p>
                It is an invitation to listen to the body and allow movement to become a pathway back to presence, pleasure, and personal power.
              </p>
            </div>
          </div>
          <div className="facilitator-images">
            <Image
              src="/images/retreat-gathering.jpeg"
              alt="Spacious gathering area with comfortable seating"
              width={600}
              height={400}
              className="section-photo"
            />
            <Image
              src="/images/retreat-lounge.jpeg"
              alt="Lounge area with desert views and sunset light"
              width={600}
              height={400}
              className="section-photo"
            />
          </div>
        </div>
      </section>

      {/* Location */}
      <section className="retreat-location">
        <div className="container content-container">
          <h2>Location</h2>
          <p>Hosted in a private luxury home in St. George, Utah.</p>
          <p className="location-features">
            Desert views. Pool. Firepit. Spacious gathering areas.
          </p>
          <div className="location-gallery">
            <Image
              src="/images/retreat-rear.jpg"
              alt="Private luxury retreat home with pool at sunset"
              width={800}
              height={600}
              className="location-photo-hero"
            />
            <div className="location-gallery-row">
              <Image
                src="/images/retreat-pool.jpg"
                alt="Pool with rock waterfall feature at sunset"
                width={600}
                height={400}
                className="section-photo"
              />
              <Image
                src="/images/retreat-hottub.jpg"
                alt="Rooftop patio with fire pit and hot tub"
                width={600}
                height={400}
                className="section-photo"
              />
            </div>
          </div>
          <p className="location-note">Exact address provided upon registration.</p>
        </div>
      </section>

      {/* Investment */}
      <section className="retreat-investment">
        <div className="container content-container">
          <div className="investment-inner">
            <h2>Investment</h2>

            <div className="price-card">
              <h3>Retreat Ticket: $1,250*</h3>
              <div className="includes">
                <h4>Includes:</h4>
                <ul>
                  <li>Full retreat access (Friday&ndash;Sunday)</li>
                  <li>Saturday hot breakfast &amp; lunch and a sit-down 5-course meal made by a private chef</li>
                  <li>Sunday breakfast</li>
                  <li>Friday evening refreshments</li>
                </ul>
              </div>
              <div className="dining-image">
                <Image
                  src="/images/retreat-dining.png"
                  alt="Elegant dining area set for a private chef dinner"
                  width={600}
                  height={400}
                  className="section-photo"
                />
              </div>
            </div>

            <div className="deposit-card">
              <h3>Payment &amp; Deposit Structure</h3>
              <div className="deposit-highlight">
                <p className="deposit-amount">$500 non-refundable deposit to reserve your spot</p>
              </div>
              <ul className="deposit-details">
                <li>All balances must be paid in full by <strong>April 10, 2026</strong></li>
              </ul>
              <p className="payment-plan-note">*$1,450 if paid via payment plan ($500 deposit required)</p>
            </div>

            <div className="accommodation-card">
              <h3>On-Site Immersive Lodging (Add-On)</h3>
              <p className="lodging-note">Lodging is optional and separate from retreat tuition. Limited availability. First come, first served. All lodging payments are non-refundable.</p>

              <h4 className="housing-option-title">Private King En-Suite · $995</h4>
              <ul>
                <li>3 nights, single occupancy (Friday&ndash;Monday morning)</li>
                <li>Includes extended access through Sunday evening with departure Monday morning</li>
                <li>Double occupancy may be available upon request for women attending together. Email <a href="mailto:Kimberly@thatdeeperfeeling.com">Kimberly@thatdeeperfeeling.com</a> for details.</li>
              </ul>

              <h4 className="housing-option-title">The Slumber Party Room · $495 per bed</h4>
              <ul>
                <li>3 nights, community style (Friday&ndash;Monday morning)</li>
                <li>Three triple queen bunk beds create a cozy, intimate, sisterhood-style experience</li>
                <li>Best suited for women who value connection, shared energy, and playful closeness</li>
              </ul>

              <div className="housing-note">
                <p>Retreat programming concludes Sunday at noon. For those staying on-site, Sunday afternoon and evening are intentionally unstructured integration time. Guests are welcome to enjoy the pool, hot tub, fire pit, and connection at their own pace.</p>
                <p>Meals Sunday afternoon/evening and Monday morning are self-directed.</p>
              </div>
            </div>

            <div className="policy-card">
              <p>
                Due to the intimate and curated nature of this retreat, all payments are non-refundable. If you are unable to attend, you may transfer your ticket to another eligible woman with prior approval.
              </p>
            </div>

            <p className="limited-note">Limited to 20&ndash;25 women.</p>

            <Button href="/events/register" variant="primary">
              Reserve Your Spot
            </Button>
          </div>
        </div>
      </section>

      {/* Is This For You */}
      <section className="retreat-for-you">
        <div className="container content-container">
          <h2>Is This For You?</h2>
          <p className="for-you-intro">This retreat may be for you if:</p>
          <ul className="for-you-list">
            <li>You&rsquo;re deconstructing or have left a high-demand religion</li>
            <li>You&rsquo;re tired of performing &ldquo;goodness&rdquo;</li>
            <li>You want to reconnect with your body without losing yourself</li>
            <li>You crave community without hierarchy</li>
            <li>You&rsquo;re ready for reclamation, not reaction</li>
          </ul>
          <p className="for-you-closing">
            This is for the woman who is ready to reclaim what was once labeled &ldquo;forbidden&rdquo;&hellip;
            and discover it was power all along.
          </p>
          <Button href="/events/register" variant="primary">
            Register Now
          </Button>
        </div>
      </section>

      {/* FAQ */}
      <section className="retreat-faq">
        <div className="container content-container">
          <h2>Frequently Asked Questions</h2>
          <div className="faq-list">

            <div className="faq-item">
              <h3>Who is this retreat for?</h3>
              <p>
                This retreat is for women navigating life after high-demand religion, rigid belief systems, or identities that required self-erasure to belong.
              </p>
              <p>
                It&rsquo;s for women who feel ready to explore embodiment, internal authority, and reclamation in a contained, intentional environment.
              </p>
              <p>
                You do not need to identify with any specific religion to attend. The common thread is untangling obedience culture and reconnecting to yourself.
              </p>
            </div>

            <div className="faq-item">
              <h3>Is this retreat religious?</h3>
              <p>No. This is not a religious retreat.</p>
              <p>
                While many attendees may be deconstructing from religious systems, this space is not anti-religion, anti-faith, or centered on debate. It is centered on personal sovereignty and embodied reclamation.
              </p>
            </div>

            <div className="faq-item">
              <h3>Is this a kink retreat?</h3>
              <p>No.</p>
              <p>
                Conscious kink is one modality Kimberly works with in her broader practice, but participation in kink-related exploration is not required and is not the focus of this retreat.
              </p>
              <p>
                All practices are optional. This weekend centers on embodiment, personal authority, and contained exploration.
              </p>
            </div>

            <div className="faq-item">
              <h3>What does &ldquo;embodiment&rdquo; mean in this context?</h3>
              <p>
                Embodiment means reconnecting with your body as a source of wisdom rather than something to control or override.
              </p>
              <p>
                You will be guided through somatic practices, movement, breathwork, and reflective exercises. Nothing is forced. You participate at your own pace.
              </p>
            </div>

            <div className="faq-item">
              <h3>Will there be nudity?</h3>
              <p>No nudity is required.</p>
              <p>
                Participants are invited to dress in ways that feel expressive and comfortable, but all exercises are structured to maintain personal choice and autonomy.
              </p>
            </div>

            <div className="faq-item">
              <h3>I feel nervous. Is that normal?</h3>
              <p>Yes.</p>
              <p>
                Many women attending will be stepping outside familiar belief systems or roles. Nervousness is common and welcomed.
              </p>
              <p>You are never required to share more than you want to share.</p>
            </div>

            <div className="faq-item">
              <h3>What if I become emotionally overwhelmed?</h3>
              <p>Emotional responses are normal in spaces of reclamation.</p>
              <p>
                There will be structured support throughout the weekend, and you are always allowed to step out, pause, or take space as needed.
              </p>
              <p>This is not therapy, but it is a thoughtfully facilitated container.</p>
            </div>

            <div className="faq-item">
              <h3>What is included in the base ticket?</h3>
              <p>The base ticket includes:</p>
              <ul>
                <li>Full retreat access (Friday evening through Sunday midday)</li>
                <li>Saturday breakfast and lunch</li>
                <li>Saturday sit-down dinner</li>
                <li>Sunday breakfast</li>
                <li>Friday evening light refreshments</li>
              </ul>
              <p>Accommodation is separate and optional.</p>
            </div>

            <div className="faq-item">
              <h3>Can I stay on-site?</h3>
              <p>Yes.</p>
              <p>Limited on-site accommodations are available:</p>
              <ul>
                <li>Premium King Suites (single or double occupancy)</li>
                <li>&ldquo;Slumber Party&rdquo; Bunk Room option for group bookings</li>
              </ul>
              <p>On-site spots are limited and available on a first-come basis.</p>
            </div>

            <div className="faq-item">
              <h3>Do you offer payment plans?</h3>
              <p>Yes. Payment plans are available at checkout.</p>
            </div>

            <div className="faq-item">
              <h3>What is your cancellation policy?</h3>
              <p>
                Due to the intimate and curated nature of this retreat, all payments are non-refundable.
              </p>
              <p>
                If you are unable to attend, you may transfer your ticket to another eligible woman with prior approval.
              </p>
            </div>

            <div className="faq-item">
              <h3>What kind of space is this?</h3>
              <p>
                This retreat is built on mutual respect, personal responsibility, and contained exploration.
              </p>
              <p>We gather without hierarchy, without persuasion, and without pressure.</p>
              <p>
                There is no agenda to convert, convince, or dismantle anyone&rsquo;s beliefs. Each woman is responsible for her own process and pace.
              </p>
              <p>
                We honor different stories, different stages of deconstruction, and different relationships to faith, sexuality, and identity.
              </p>
              <p>
                This is a space for permission. Permission to feel, to question, to soften, to expand, and to come home to yourself in your own time.
              </p>
            </div>

          </div>
        </div>
      </section>

      <style jsx>{`
        /* Hero */
        .retreat-hero {
          background: linear-gradient(135deg, var(--primary-burgundy) 0%, var(--primary-wine) 100%);
          color: var(--neutral-soft-white);
          padding: 6rem 1.5rem 5rem;
          text-align: center;
        }

        .retreat-hero h1 {
          color: var(--neutral-soft-white);
          font-size: clamp(2.5rem, 5vw, 4rem);
          margin-bottom: 0.5rem;
        }

        .hero-tagline {
          font-size: clamp(1.1rem, 2.2vw, 1.5rem);
          color: var(--neutral-cream);
          font-style: italic;
          margin-bottom: 2rem;
        }

        .hero-details {
          margin-bottom: 2.5rem;
        }

        .hero-date {
          font-size: 1.2rem;
          font-weight: 600;
          color: var(--neutral-soft-white);
          margin-bottom: 0.25rem;
          letter-spacing: 0.05em;
        }

        .hero-location {
          font-size: 1.1rem;
          color: var(--neutral-cream);
          margin: 0;
        }

        .hero-hook {
          font-size: clamp(1.05rem, 2vw, 1.25rem);
          color: var(--neutral-cream);
          max-width: 600px;
          margin: 0 auto 1rem;
          line-height: 1.7;
        }

        .hero-declaration {
          font-size: clamp(1.2rem, 2.5vw, 1.5rem);
          font-weight: 600;
          color: var(--neutral-soft-white);
          margin-bottom: 2.5rem;
          font-family: var(--font-heading);
        }

        /* About */
        .retreat-about {
          background: var(--neutral-soft-white);
          padding: 5rem 0;
        }

        .about-layout {
          display: grid;
          grid-template-columns: 1fr;
          gap: 3rem;
          align-items: center;
        }

        @media (min-width: 768px) {
          .about-layout {
            grid-template-columns: 1.2fr 1fr;
            gap: 4rem;
          }
        }

        .about-inner {
          max-width: 700px;
        }

        .about-image {
          display: flex;
          justify-content: center;
        }

        .retreat-about h2 {
          font-size: clamp(2rem, 4vw, 3rem);
          margin-bottom: 2rem;
        }

        @media (max-width: 767px) {
          .retreat-about h2 {
            text-align: center;
          }
        }

        .retreat-about p {
          font-size: 1.15rem;
          line-height: 1.8;
          color: var(--neutral-charcoal);
          margin-bottom: 1.25rem;
        }

        .emphasis-line {
          font-style: italic;
          color: var(--primary-burgundy) !important;
          font-weight: 500;
        }

        /* Section photos */
        :global(.section-photo) {
          border-radius: 0.75rem;
          box-shadow: 0 10px 30px rgba(139, 58, 71, 0.15);
          object-fit: cover;
          width: 100%;
          height: auto;
        }

        :global(.location-photo-hero) {
          border-radius: 0.75rem;
          box-shadow: 0 15px 40px rgba(0, 0, 0, 0.25);
          object-fit: cover;
          width: 100%;
          height: auto;
        }

        /* Explore */
        .retreat-explore {
          background: var(--neutral-cream);
          padding: 5rem 0;
        }

        .retreat-explore h2 {
          text-align: center;
          font-size: clamp(2rem, 4vw, 3rem);
          margin-bottom: 2.5rem;
        }

        .explore-list {
          list-style: none;
          padding: 0;
          max-width: 550px;
          margin: 0 auto 2.5rem;
        }

        .explore-list li {
          padding: 0.75rem 0;
          padding-left: 2rem;
          position: relative;
          font-size: 1.15rem;
          color: var(--neutral-charcoal);
        }

        .explore-list li::before {
          content: '•';
          position: absolute;
          left: 0;
          color: var(--accent-terracotta);
          font-size: 1.5rem;
          line-height: 1;
        }

        .explore-intro {
          text-align: center;
          font-size: 1.15rem;
          color: var(--neutral-charcoal);
          margin-bottom: 1.5rem;
        }

        .and-yes-heading {
          text-align: center;
          font-size: 1.5rem;
          color: var(--primary-burgundy);
          margin: 2rem 0 1.5rem;
          font-style: italic;
        }

        .and-yes-list {
          list-style: none;
          padding: 0;
          max-width: 550px;
          margin: 0 auto 2.5rem;
        }

        .and-yes-list li {
          padding: 0.5rem 0;
          padding-left: 2rem;
          position: relative;
          font-size: 1.15rem;
          color: var(--neutral-charcoal);
        }

        .and-yes-list li::before {
          content: '•';
          position: absolute;
          left: 0;
          color: var(--accent-terracotta);
          font-size: 1.5rem;
          line-height: 1;
        }

        .retreat-philosophy {
          text-align: center;
          max-width: 650px;
          margin: 0 auto;
          padding: 2rem 0;
        }

        .retreat-philosophy p {
          font-size: 1.1rem;
          line-height: 1.8;
          color: var(--neutral-charcoal);
          margin-bottom: 0.5rem;
        }

        /* Framework */
        .retreat-framework {
          background: var(--neutral-soft-white);
          padding: 5rem 0;
        }

        .retreat-framework h2 {
          text-align: center;
          font-size: clamp(2rem, 4vw, 3rem);
          margin-bottom: 2rem;
        }

        .retreat-framework > div > p {
          font-size: 1.15rem;
          line-height: 1.8;
          color: var(--neutral-charcoal);
          max-width: 700px;
          margin: 0 auto 1.25rem;
          text-align: center;
        }

        .framework-separations,
        .framework-connections {
          max-width: 700px;
          margin: 1.5rem auto;
          text-align: center;
        }

        .framework-separations p,
        .framework-connections p {
          font-size: 1.1rem;
          line-height: 1.8;
          color: var(--neutral-charcoal);
          margin-bottom: 0.5rem;
        }

        .energy-list {
          list-style: none;
          padding: 0;
          max-width: 300px;
          margin: 1.5rem auto 2rem;
          text-align: center;
        }

        .energy-list li {
          padding: 0.5rem 0;
          font-size: 1.15rem;
          font-weight: 500;
          color: var(--primary-burgundy);
        }

        .spine-heading,
        .why-heading {
          text-align: center;
          font-size: 1.75rem;
          color: var(--primary-burgundy);
          margin: 3rem 0 1.5rem;
        }

        .spine-list {
          list-style: none;
          padding: 0;
          max-width: 300px;
          margin: 1.5rem auto 2rem;
          text-align: center;
        }

        .spine-list li {
          padding: 0.5rem 0;
          font-size: 1.15rem;
          color: var(--neutral-charcoal);
        }

        .spine-list li strong {
          color: var(--primary-burgundy);
          font-size: 1.25rem;
        }

        .spine-focus {
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 2rem;
          max-width: 700px;
          margin: 2rem auto;
        }

        .spine-stage {
          background: var(--neutral-cream);
          padding: 2rem;
          border-radius: 0.75rem;
          border-top: 3px solid var(--accent-terracotta);
          text-align: center;
        }

        .spine-stage h4 {
          font-size: 1.25rem;
          color: var(--primary-burgundy);
          margin-bottom: 0.75rem;
        }

        .spine-stage p {
          font-size: 1.05rem;
          line-height: 1.7;
          color: var(--neutral-charcoal);
          margin: 0;
        }

        .transition-list {
          list-style: none;
          padding: 0;
          max-width: 550px;
          margin: 1.5rem auto 2rem;
        }

        .transition-list li {
          padding: 0.6rem 0;
          padding-left: 2rem;
          position: relative;
          font-size: 1.1rem;
          color: var(--neutral-charcoal);
          line-height: 1.6;
        }

        .transition-list li::before {
          content: '•';
          position: absolute;
          left: 0;
          color: var(--accent-terracotta);
          font-size: 1.5rem;
          line-height: 1;
        }

        @media (max-width: 768px) {
          .spine-focus {
            grid-template-columns: 1fr;
          }
        }

        /* Guest Facilitator */
        .retreat-facilitator {
          background: var(--neutral-cream);
          padding: 5rem 0;
        }

        .retreat-facilitator h2 {
          font-size: clamp(1.75rem, 3.5vw, 2.5rem);
          margin-bottom: 1.5rem;
          text-align: center;
        }

        .facilitator-content {
          max-width: 700px;
          margin: 0 auto 2.5rem;
        }

        .facilitator-content > p {
          font-size: 1.1rem;
          line-height: 1.8;
          color: var(--neutral-charcoal);
          margin-bottom: 1.25rem;
        }

        .sfactor-note {
          background: white;
          padding: 2rem 2.5rem;
          border-radius: 0.75rem;
          border-top: 3px solid var(--accent-terracotta);
          margin-top: 2rem;
        }

        .sfactor-note h3 {
          font-size: 1.35rem;
          color: var(--primary-burgundy);
          margin-bottom: 1rem;
          text-align: center;
        }

        .sfactor-note p {
          font-size: 1.05rem;
          line-height: 1.7;
          color: var(--neutral-charcoal);
          margin-bottom: 0.75rem;
        }

        .sfactor-note p:last-child {
          margin-bottom: 0;
        }

        .facilitator-images {
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 2rem;
          max-width: 900px;
          margin: 0 auto;
        }

        @media (max-width: 768px) {
          .facilitator-images {
            grid-template-columns: 1fr;
          }
        }

        /* Location */
        .retreat-location {
          background: linear-gradient(135deg, var(--primary-wine) 0%, var(--primary-burgundy) 100%);
          color: var(--neutral-soft-white);
          padding: 5rem 0;
          text-align: center;
        }

        .retreat-location h2 {
          color: var(--neutral-soft-white);
          font-size: clamp(2rem, 4vw, 3rem);
          margin-bottom: 1.5rem;
        }

        .retreat-location p {
          font-size: 1.15rem;
          color: var(--neutral-cream);
          margin-bottom: 0.75rem;
        }

        .location-features {
          font-weight: 500;
          font-size: 1.2rem !important;
          color: var(--neutral-soft-white) !important;
          letter-spacing: 0.02em;
        }

        .location-gallery {
          max-width: 900px;
          margin: 2.5rem auto;
        }

        .location-gallery-row {
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 1.5rem;
          margin-top: 1.5rem;
        }

        @media (max-width: 768px) {
          .location-gallery-row {
            grid-template-columns: 1fr;
          }
        }

        .location-note {
          font-style: italic;
          font-size: 1rem !important;
          margin-top: 0;
        }

        /* Investment */
        .retreat-investment {
          background: var(--neutral-cream);
          padding: 5rem 0;
        }

        .investment-inner {
          max-width: 650px;
          margin: 0 auto;
          text-align: center;
        }

        .retreat-investment h2 {
          font-size: clamp(2rem, 4vw, 3rem);
          margin-bottom: 2.5rem;
        }

        .price-card {
          background: white;
          padding: 2.5rem;
          border-radius: 0.75rem;
          box-shadow: 0 10px 40px rgba(139, 58, 71, 0.1);
          margin-bottom: 2rem;
          text-align: left;
        }

        .price-card h3 {
          font-size: 1.5rem;
          color: var(--primary-burgundy);
          margin-bottom: 1.5rem;
          text-align: center;
        }

        .includes h4 {
          font-size: 1.1rem;
          color: var(--neutral-charcoal);
          margin-bottom: 0.75rem;
          font-weight: 600;
        }

        .includes ul,
        .accommodation-card ul {
          list-style: none;
          padding: 0;
        }

        .includes ul li,
        .accommodation-card ul li {
          padding: 0.5rem 0;
          padding-left: 1.5rem;
          position: relative;
          font-size: 1.05rem;
          color: var(--neutral-charcoal);
          line-height: 1.6;
        }

        .includes ul li::before,
        .accommodation-card ul li::before {
          content: '•';
          position: absolute;
          left: 0;
          color: var(--accent-terracotta);
          font-size: 1.25rem;
          line-height: 1;
        }

        .dining-image {
          margin-top: 1.5rem;
        }

        .deposit-card {
          background: white;
          padding: 2.5rem;
          border-radius: 0.75rem;
          box-shadow: 0 10px 40px rgba(139, 58, 71, 0.1);
          margin-bottom: 2rem;
          text-align: left;
          border-top: 3px solid var(--accent-terracotta);
        }

        .deposit-card h3 {
          font-size: 1.35rem;
          color: var(--primary-burgundy);
          margin-bottom: 1.5rem;
          text-align: center;
        }

        .deposit-highlight {
          background: var(--neutral-cream);
          padding: 1.25rem 1.5rem;
          border-radius: 0.5rem;
          margin-bottom: 1.5rem;
          text-align: center;
        }

        .deposit-amount {
          font-size: 1.15rem;
          font-weight: 600;
          color: var(--primary-burgundy);
          margin: 0;
        }

        .deposit-details {
          list-style: none;
          padding: 0;
        }

        .deposit-details li {
          padding: 0.5rem 0;
          padding-left: 1.5rem;
          position: relative;
          font-size: 1.05rem;
          color: var(--neutral-charcoal);
          line-height: 1.6;
        }

        .deposit-details li::before {
          content: '•';
          position: absolute;
          left: 0;
          color: var(--accent-terracotta);
          font-size: 1.25rem;
          line-height: 1;
        }

        .payment-plan-note {
          font-size: 0.9rem;
          color: var(--neutral-warm-gray);
          font-style: italic;
          margin-top: 1rem;
          text-align: center;
        }

        .accommodation-card {
          background: white;
          padding: 2rem 2.5rem;
          border-radius: 0.75rem;
          box-shadow: 0 10px 40px rgba(139, 58, 71, 0.1);
          margin-bottom: 2rem;
          text-align: left;
        }

        .accommodation-card h3 {
          font-size: 1.25rem;
          color: var(--primary-burgundy);
          margin-bottom: 0.75rem;
        }

        .lodging-note {
          font-size: 0.95rem;
          color: var(--neutral-warm-gray);
          font-style: italic;
          margin-bottom: 1.5rem;
        }

        .housing-option-title {
          font-size: 1.1rem;
          color: var(--primary-burgundy);
          font-weight: 600;
          margin: 1.5rem 0 0.75rem;
        }

        .accommodation-card a {
          color: var(--primary-burgundy);
          text-decoration: underline;
          text-underline-offset: 2px;
        }

        .accommodation-card a:hover {
          color: var(--accent-terracotta);
        }

        .housing-note {
          margin-top: 1.5rem;
          padding: 1.25rem 1.5rem;
          background: var(--neutral-cream);
          border-radius: 0.5rem;
          border-left: 3px solid var(--accent-gold);
        }

        .housing-note p {
          font-size: 0.95rem;
          color: var(--neutral-warm-gray);
          line-height: 1.7;
          margin: 0 0 0.75rem;
        }

        .housing-note p:last-child {
          margin-bottom: 0;
        }

        .policy-card {
          background: var(--neutral-soft-white);
          padding: 1.5rem 2rem;
          border-radius: 0.5rem;
          margin-bottom: 2rem;
          border-left: 3px solid var(--secondary-taupe);
        }

        .policy-card p {
          font-size: 0.95rem;
          color: var(--neutral-warm-gray);
          line-height: 1.7;
          margin: 0;
          text-align: left;
        }

        .limited-note {
          font-weight: 600;
          font-size: 1.1rem;
          color: var(--primary-burgundy);
          margin-bottom: 2rem;
        }

        /* Is This For You */
        .retreat-for-you {
          background: var(--neutral-soft-white);
          padding: 5rem 0;
          text-align: center;
        }

        .retreat-for-you h2 {
          font-size: clamp(2rem, 4vw, 3rem);
          margin-bottom: 1.5rem;
        }

        .for-you-intro {
          font-size: 1.15rem;
          color: var(--neutral-charcoal);
          margin-bottom: 2rem;
        }

        .for-you-list {
          list-style: none;
          padding: 0;
          max-width: 550px;
          margin: 0 auto 2.5rem;
          text-align: left;
        }

        .for-you-list li {
          padding: 0.75rem 0;
          padding-left: 2rem;
          position: relative;
          font-size: 1.1rem;
          color: var(--neutral-charcoal);
          line-height: 1.6;
        }

        .for-you-list li::before {
          content: '•';
          position: absolute;
          left: 0;
          color: var(--accent-terracotta);
          font-size: 1.5rem;
          line-height: 1;
        }

        .for-you-closing {
          font-size: 1.15rem;
          font-style: italic;
          color: var(--primary-burgundy);
          line-height: 1.8;
          margin-bottom: 2.5rem;
        }

        /* FAQ */
        .retreat-faq {
          background: var(--neutral-cream);
          padding: 5rem 0;
        }

        .retreat-faq h2 {
          text-align: center;
          font-size: clamp(2rem, 4vw, 3rem);
          margin-bottom: 3rem;
        }

        .faq-list {
          max-width: 700px;
          margin: 0 auto;
        }

        .faq-item {
          background: white;
          padding: 2rem 2.5rem;
          border-radius: 0.75rem;
          margin-bottom: 1.5rem;
          box-shadow: 0 4px 20px rgba(139, 58, 71, 0.08);
        }

        .faq-item h3 {
          font-size: 1.2rem;
          color: var(--primary-burgundy);
          margin-bottom: 1rem;
        }

        .faq-item p {
          font-size: 1.05rem;
          line-height: 1.7;
          color: var(--neutral-charcoal);
          margin-bottom: 0.75rem;
        }

        .faq-item p:last-child {
          margin-bottom: 0;
        }

        .faq-item ul {
          list-style: none;
          padding: 0;
          margin-bottom: 0.75rem;
        }

        .faq-item ul li {
          padding: 0.4rem 0;
          padding-left: 1.5rem;
          position: relative;
          font-size: 1.05rem;
          color: var(--neutral-charcoal);
          line-height: 1.6;
        }

        .faq-item ul li::before {
          content: '•';
          position: absolute;
          left: 0;
          color: var(--accent-terracotta);
          font-size: 1.25rem;
          line-height: 1;
        }
      `}</style>
    </>
  );
}
