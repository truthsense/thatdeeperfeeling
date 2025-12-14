'use client';

import Button from '@/components/ui/Button';

export default function AllOfferingsPage() {
  return (
    <>
      {/* Hero */}
      <section className="offerings-hero">
        <div className="container content-container">
          <h1>Coaching Containers</h1>
          <p className="hero-subtitle">
            Intentional, consent-led spaces for deep personal reclamation. Each container supports you in reconnecting with your body, truth, and internal authority.
          </p>
        </div>
      </section>

      {/* Return to Power - 6 Months */}
      <section className="offering-detail" id="return-to-power">
        <div className="container content-container">
          <div className="offering-header">
            <span className="badge">Most Popular</span>
            <h2>Return to Power</h2>
            <p className="duration">6-Month Private Container</p>
            <p className="tagline">
              A deep, spacious journey for individuals ready to dismantle self-sacrifice patterns and reclaim embodied authority, pleasure, and truth.
            </p>
          </div>

          <div className="offering-content">
            <div className="content-section">
              <h3>Who This Is For</h3>
              <p>
                This container is for those ready to go all the way. You're committed to sustained, deep work across emotional, relational, and erotic dimensions. You're ready for long-term integration, nervous system regulation, and profound shifts in how you relate to power, desire, intimacy, and your own body.
              </p>
            </div>

            <div className="content-section">
              <h3>What's Included</h3>
              <ul className="features-list">
                <li>Bi-weekly 90-minute private sessions (12 sessions total)</li>
                <li>Personalized embodiment practices and resources</li>
                <li>Voxer voice messaging support between sessions</li>
                <li>Sacred ritual design tailored to your journey</li>
                <li>Embodiment homework and integration exercises</li>
                <li>Access to curated resources (readings, playlists, practices)</li>
              </ul>
            </div>

            <div className="content-section">
              <h3>What We'll Explore</h3>
              <p>
                Together, we'll work with self-sacrifice patterns, pleasure reclamation, power dynamics, boundaries, desire, embodied sovereignty, nervous system regulation, kink consciousness, relational patterns, and sacred sexuality.
              </p>
            </div>

            <div className="investment-box">
              <h3>Investment</h3>
              <p className="price">$3,600</p>
              <p className="payment-note">Payment plans available</p>
            </div>

            <div className="cta-section">
              <Button href="/consult" variant="primary">
                Book Consultation
              </Button>
            </div>
          </div>
        </div>
      </section>

      {/* Edgewalker - 3 Months */}
      <section className="offering-detail alt" id="edgewalker">
        <div className="container content-container">
          <div className="offering-header">
            <h2>Edgewalker</h2>
            <p className="duration">3-Month Private Container</p>
            <p className="tagline">
              An immersive, focused container for those standing at the edge of change, ready to explore a specific dimension of power, desire, or embodiment.
            </p>
          </div>

          <div className="offering-content">
            <div className="content-section">
              <h3>Who This Is For</h3>
              <p>
                Perfect for exploring one focused area of your intimacy journey. Whether it's communication in kink dynamics, reclaiming pleasure after loss or trauma, navigating a specific relationship edge, or deepening into a particular aspect of embodied sovereignty.
              </p>
            </div>

            <div className="content-section">
              <h3>What's Included</h3>
              <ul className="features-list">
                <li>Weekly 60-minute private sessions (12 sessions total)</li>
                <li>Customized embodiment practices specific to your focus</li>
                <li>Email support between sessions</li>
                <li>Integration resources and practices</li>
                <li>Personalized reading and resource recommendations</li>
              </ul>
            </div>

            <div className="content-section">
              <h3>What We'll Explore</h3>
              <p>
                This container allows for deep, focused work on a specific edge: power dynamics, communication patterns, desire reclamation, grief and pleasure, kink exploration, or embodied boundaries. You choose the focus; I hold the container.
              </p>
            </div>

            <div className="investment-box">
              <h3>Investment</h3>
              <p className="price">$2,100</p>
              <p className="payment-note">Payment plans available</p>
            </div>

            <div className="cta-section">
              <Button href="/consult" variant="primary">
                Book Consultation
              </Button>
            </div>
          </div>
        </div>
      </section>

      {/* Sacred Eruption - Single Session */}
      <section className="offering-detail" id="sacred-eruption">
        <div className="container content-container">
          <div className="offering-header">
            <h2>Sacred Eruption</h2>
            <p className="duration">Single Session Deep Dive</p>
            <p className="tagline">
              A powerful, contained exploration for those seeking clarity, release, or an embodied breakthrough without ongoing commitment.
            </p>
          </div>

          <div className="offering-content">
            <div className="content-section">
              <h3>Who This Is For</h3>
              <p>
                Ideal for addressing a specific block, question, or moment of transformation. Perfect for returning clients needing support through a particular edge, or for those exploring whether deeper container work is right for them.
              </p>
            </div>

            <div className="content-section">
              <h3>What's Included</h3>
              <ul className="features-list">
                <li>One 2-hour intensive private session</li>
                <li>Pre-session intake and preparation guidance</li>
                <li>Integration guide with practices and reflections</li>
                <li>Follow-up email support (one exchange)</li>
              </ul>
            </div>

            <div className="content-section">
              <h3>What We'll Explore</h3>
              <p>
                This session creates spacious time for a specific breakthrough, somatic release, clarity on a decision, exploration of a relational dynamic, or integration of a recent experience. It's powerful, focused, and complete in itself.
              </p>
            </div>

            <div className="investment-box">
              <h3>Investment</h3>
              <p className="price">$400</p>
            </div>

            <div className="cta-section">
              <Button href="/consult" variant="primary">
                Book Consultation
              </Button>
            </div>
          </div>
        </div>
      </section>

      {/* Flicker and Flame - Membership */}
      <section className="offering-detail alt" id="flicker-and-flame">
        <div className="container content-container">
          <div className="offering-header">
            <h2>Flicker and Flame</h2>
            <p className="duration">Online Membership</p>
            <p className="tagline">
              A lower-touch community space for ongoing reflection, embodiment practices, and relational exploration.
            </p>
          </div>

          <div className="offering-content">
            <div className="content-section">
              <h3>Who This Is For</h3>
              <p>
                Designed for those wanting continued resonance and support without private coaching. Ideal for current or former clients wanting to stay connected, or for those new to this work who prefer a community entry point.
              </p>
            </div>

            <div className="content-section">
              <h3>What's Included</h3>
              <ul className="features-list">
                <li>Monthly live workshops and group calls</li>
                <li>Private community forum for connection and questions</li>
                <li>Resource library with practices, readings, and recordings</li>
                <li>Guest expert sessions on embodiment, kink, and intimacy</li>
                <li>Cancel anytime—no long-term commitment</li>
              </ul>
            </div>

            <div className="content-section">
              <h3>What to Expect</h3>
              <p>
                A grounded, evolving space for learning, practicing, and connecting with others on similar journeys. This is not a substitute for private coaching—it's a complement or continuation of the work.
              </p>
            </div>

            <div className="investment-box">
              <h3>Investment</h3>
              <p className="price">$47/month</p>
              <p className="payment-note">Cancel anytime</p>
            </div>

            <div className="cta-section">
              <Button href="/consult" variant="primary">
                Join Waitlist
              </Button>
            </div>
          </div>
        </div>
      </section>

      {/* Into the Embers - In-Person */}
      <section className="offering-detail" id="into-the-embers">
        <div className="container content-container">
          <div className="offering-header">
            <h2>Into the Embers</h2>
            <p className="duration">In-Person Gatherings</p>
            <p className="tagline">
              Curated in-person experiences centered on presence, embodiment, connection, and conscious exploration.
            </p>
          </div>

          <div className="offering-content">
            <div className="content-section">
              <h3>Who This Is For</h3>
              <p>
                Those seeking in-person embodied work. You value group energy and connection. You're ready to explore power, pleasure, and presence in community while being held in safety and consent.
              </p>
            </div>

            <div className="content-section">
              <h3>What's Included</h3>
              <ul className="features-list">
                <li>2-3 day immersive retreats</li>
                <li>Somatic practices and sacred rituals</li>
                <li>Group facilitation and witnessing circles</li>
                <li>Meals and accommodations included</li>
                <li>Limited to 8-12 participants for intimacy and depth</li>
              </ul>
            </div>

            <div className="content-section">
              <h3>What to Expect</h3>
              <p>
                These gatherings prioritize safety, consent, and relational depth. Expect somatic movement, breathwork, ritual, group processing, and time in nature. All experiences are trauma-informed and consent-centered.
              </p>
            </div>

            <div className="investment-box">
              <h3>Investment</h3>
              <p className="price">TBD</p>
              <p className="payment-note">Pricing varies by event location and duration</p>
            </div>

            <div className="cta-section">
              <Button href="/events" variant="primary">
                View Events
              </Button>
            </div>
          </div>
        </div>
      </section>

      {/* Final CTA */}
      <section className="offerings-cta">
        <div className="container content-container centered">
          <h2>Not Sure Which Container Is Right?</h2>
          <p>
            Book a consultation and we'll explore your goals, answer questions, and help you choose the path that feels most aligned.
          </p>
          <Button href="/consult" variant="primary">
            Book Free Consultation
          </Button>
        </div>
      </section>

      <style jsx>{`
        /* Hero */
        .offerings-hero {
          background: linear-gradient(135deg, var(--neutral-cream) 0%, var(--secondary-warm-beige) 100%);
          padding: 5rem 1.5rem 4rem;
          text-align: center;
        }

        .offerings-hero h1 {
          font-size: clamp(2.5rem, 5vw, 4rem);
          margin-bottom: 1.5rem;
        }

        .hero-subtitle {
          font-size: clamp(1.1rem, 2vw, 1.3rem);
          color: var(--neutral-warm-gray);
          line-height: 1.7;
          max-width: 800px;
          margin: 0 auto;
        }

        /* Offering Detail Sections */
        .offering-detail {
          padding: 5rem 0;
          background: var(--neutral-soft-white);
        }

        .offering-detail.alt {
          background: var(--neutral-cream);
        }

        .offering-header {
          text-align: center;
          margin-bottom: 4rem;
          position: relative;
        }

        .badge {
          display: inline-block;
          background: var(--accent-terracotta);
          color: var(--neutral-soft-white);
          padding: 0.4rem 1rem;
          border-radius: 2rem;
          font-size: 0.85rem;
          font-weight: 600;
          margin-bottom: 1rem;
        }

        .offering-header h2 {
          font-size: clamp(2.5rem, 4vw, 3.5rem);
          color: var(--primary-burgundy);
          margin-bottom: 0.75rem;
        }

        .duration {
          font-size: 1.1rem;
          color: var(--neutral-warm-gray);
          font-weight: 500;
          margin-bottom: 1.5rem;
        }

        .tagline {
          font-size: clamp(1.15rem, 2vw, 1.35rem);
          color: var(--primary-wine);
          font-weight: 500;
          line-height: 1.6;
          max-width: 700px;
          margin: 0 auto;
        }

        .offering-content {
          max-width: 800px;
          margin: 0 auto;
        }

        .content-section {
          margin-bottom: 3rem;
        }

        .content-section h3 {
          font-size: 1.75rem;
          color: var(--primary-burgundy);
          margin-bottom: 1.25rem;
        }

        .content-section p {
          font-size: 1.1rem;
          line-height: 1.8;
          color: var(--neutral-charcoal);
        }

        .features-list {
          list-style: none;
          padding: 0;
        }

        .features-list li {
          padding: 0.75rem 0;
          padding-left: 2rem;
          position: relative;
          font-size: 1.1rem;
          color: var(--neutral-charcoal);
          line-height: 1.6;
        }

        .features-list li::before {
          content: '✓';
          position: absolute;
          left: 0;
          color: var(--accent-terracotta);
          font-weight: 700;
          font-size: 1.2rem;
        }

        .investment-box {
          background: white;
          padding: 2.5rem;
          border-radius: 1rem;
          text-align: center;
          margin: 3rem 0;
          border-left: 4px solid var(--accent-gold);
          box-shadow: 0 5px 20px rgba(139, 58, 71, 0.1);
        }

        .offering-detail.alt .investment-box {
          background: var(--neutral-soft-white);
        }

        .investment-box h3 {
          font-size: 1.25rem;
          color: var(--primary-wine);
          margin-bottom: 1rem;
        }

        .price {
          font-size: 2.75rem;
          font-weight: 700;
          color: var(--primary-burgundy);
          margin-bottom: 0.5rem;
          font-family: var(--font-heading);
        }

        .payment-note {
          font-size: 1rem;
          color: var(--neutral-warm-gray);
          font-style: italic;
        }

        .cta-section {
          text-align: center;
          margin-top: 3rem;
        }

        /* Final CTA */
        .offerings-cta {
          background: var(--neutral-cream);
          padding: 5rem 0;
        }

        .centered {
          text-align: center;
        }

        .offerings-cta h2 {
          margin-bottom: 1rem;
        }

        .offerings-cta p {
          font-size: 1.15rem;
          color: var(--neutral-warm-gray);
          margin-bottom: 2rem;
          line-height: 1.7;
        }
      `}</style>
    </>
  );
}
