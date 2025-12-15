'use client';

import Button from '@/components/ui/Button';
import Image from 'next/image';
import Link from 'next/link';

export default function Home() {
  return (
    <>
      {/* Role Descriptor */}
      <section className="role-descriptor">
        <div className="container">
          <p className="descriptor-text">
            I offer private coaching and immersive containers for people reclaiming their power, desire, and embodied authority after leaving high-demand systems.
          </p>
        </div>
      </section>

      {/* Hero Section */}
      <section className="hero">
        <div className="container">
          <div className="hero-layout">
            <div className="hero-content">
              <h1 className="hero-title">
                Where Sensuality, Soul,
                <br />
                <span className="gradient-text">and Surrender Meet</span>
              </h1>
              <p className="hero-subtitle">
                Guiding individuals out of spiritual codependency and back into internal peace through embodiment, Eros, and sacred interdependence.
              </p>
              <p className="hero-subtitle">
                For those unraveling the binds of high-demand religion, culture, or conditioning and reclaiming trust in the body, desire, and inner truth.
              </p>
              <div className="hero-cta">
                <Button href="/consult" variant="primary">
                  Book a Curiosity Call
                </Button>
                <p className="cta-subtext">
                  A low-pressure space to slow down, ask questions, and feel into what's next.
                </p>
              </div>
            </div>
            <div className="hero-image">
              <Image
                src="/images/kimberly-hero.jpg"
                alt="Kimberly Bryant - Intimacy Coach specializing in conscious kink and embodied reclamation"
                width={500}
                height={600}
                priority
                className="hero-photo"
              />
            </div>
          </div>
        </div>
      </section>

      {/* Testimonial Highlight */}
      <section className="section-testimonial-hero">
        <div className="container content-container">
          <blockquote className="testimonial-hero">
            <p className="testimonial-hero-text">
              "Working with Kimberly helped me reclaim parts of myself I thought were lost. I feel safer in my body and bolder in my desires than I ever imagined possible."
            </p>
            <cite className="testimonial-hero-author">— Sarah M., Return to Power Client</cite>
          </blockquote>
        </div>
      </section>

      {/* Who This Is For */}
      <section className="section-who">
        <div className="container content-container">
          <h2 className="section-title">This Work Is For You If...</h2>
          <div className="who-grid">
            <div className="who-card">
              <h3>You're Ready to Explore</h3>
              <p>
                You feel the pull toward deeper intimacy, conscious kink, or reclaiming pleasure—but need guidance that honors your pace and boundaries.
              </p>
            </div>
            <div className="who-card">
              <h3>You're Ready to Reclaim Your Power</h3>
              <p>
                You're done with self-sacrifice patterns and ready to embody your truth in relationships, desire, and life.
              </p>
            </div>
            <div className="who-card">
              <h3>You Seek Safety + Depth</h3>
              <p>
                You want to go deep without re-traumatizing. You need a container that's both sacred and grounded in consent culture.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section className="section-how">
        <div className="container">
          <h2 className="section-title centered">How We Work Together</h2>
          <div className="steps-grid">
            <div className="step">
              <div className="step-number">1</div>
              <h3>Book a Consultation</h3>
              <p>
                We'll meet for a 30-minute consultation to explore your goals, answer questions, and ensure we're a good fit.
              </p>
            </div>
            <div className="step">
              <div className="step-number">2</div>
              <h3>Choose Your Container</h3>
              <p>
                Select the coaching program that aligns with your intentions, whether it's a 6-month container, 3-month exploration, single session, or a completely customizable approach.
              </p>
            </div>
            <div className="step">
              <div className="step-number">3</div>
              <h3>Begin Your Journey</h3>
              <p>
                Step into a kink-aware, consent-centered space where you'll be supported in reclaiming pleasure, power, and authentic connection.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Featured Offerings */}
      <section className="section-offerings">
        <div className="container">
          <h2 className="section-title centered">Coaching Containers</h2>
          <p className="section-intro centered">
            Choose the pathway that calls to you. Each container is designed to honor your unique journey while providing structure, support, and sacred space.
          </p>
          <div className="offerings-grid">
            <div className="offering-card featured">
              <div className="offering-badge">Most Popular</div>
              <h3>Return to Power</h3>
              <p className="offering-duration">6-Month Private Container</p>
              <p className="offering-description">
                A deep, spacious journey for individuals ready to dismantle self-sacrifice patterns and reclaim embodied authority, pleasure, and truth.
              </p>
              <ul className="offering-features">
                <li>Bi-weekly 90-minute private sessions (12 sessions total)</li>
                <li>Personalized embodiment practices and resources</li>
                <li>Voxer voice messaging support between sessions</li>
                <li>Sacred ritual design tailored to your journey</li>
              </ul>
              <Button href="/consult" variant="primary" fullWidth>
                Book a Curiosity Call
              </Button>
            </div>

            <div className="offering-card">
              <h3>Edgewalker</h3>
              <p className="offering-duration">3-Month Private Container</p>
              <p className="offering-description">
                An immersive, focused container for those standing at the edge of change, ready to explore a specific dimension of power, desire, or embodiment.
              </p>
              <ul className="offering-features">
                <li>Weekly 60-minute private sessions (12 sessions total)</li>
                <li>Customized embodiment practices specific to your focus</li>
                <li>Email support between sessions</li>
                <li>Integration resources and practices</li>
              </ul>
              <Button href="/consult" variant="secondary" fullWidth>
                Book a Curiosity Call
              </Button>
            </div>

            <div className="offering-card">
              <h3>Sacred Eruption</h3>
              <p className="offering-duration">Single Session Deep Dive</p>
              <p className="offering-description">
                A powerful, contained exploration for those seeking clarity, release, or an embodied breakthrough without ongoing commitment.
              </p>
              <ul className="offering-features">
                <li>One 2-hour intensive private session</li>
                <li>Pre-session intake and preparation guidance</li>
                <li>Integration guide with practices and reflections</li>
                <li>Follow-up email support (one exchange)</li>
              </ul>
              <Button href="/consult" variant="secondary" fullWidth>
                Book a Curiosity Call
              </Button>
            </div>
          </div>
          <div className="cta-centered">
            <Button href="/offerings" variant="accent">
              View All Offerings
            </Button>
          </div>
        </div>
      </section>

      {/* Philosophy & Safety */}
      <section className="section-philosophy">
        <div className="container content-container">
          <h2 className="section-title">Grounded in Consent & Safety</h2>
          <p className="philosophy-intro">
            This work is kink-aware and rooted in consent culture. You'll never be pushed beyond your edges, only invited to explore them with curiosity and care.
          </p>
          <div className="philosophy-values">
            <div className="value">
              <h4>Somatic & Embodied</h4>
              <p>Honoring your nervous system, pacing, and boundaries at every step.</p>
            </div>
            <div className="value">
              <h4>Consent-Centered</h4>
              <p>Clear communication, enthusiastic yes's, and the right to change your mind, always.</p>
            </div>
            <div className="value">
              <h4>Kink-Aware</h4>
              <p>BDSM-positive, sex-positive, and deeply respectful of alternative relationship structures.</p>
            </div>
            <div className="value">
              <h4>Professionally Boundaried</h4>
              <p>This is coaching, not therapy. I'll refer you to appropriate resources when needed.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Testimonials */}
      <section className="section-testimonials">
        <div className="container">
          <h2 className="section-title centered">What Clients Say</h2>
          <div className="testimonials-grid">
            <blockquote className="testimonial">
              <p className="testimonial-text">
                "Working with Kimberly helped me reclaim parts of myself I thought were lost. I feel safer in my body and bolder in my desires than I ever imagined possible."
              </p>
              <cite className="testimonial-author">— Sarah M., Return to Power Client</cite>
            </blockquote>
            <blockquote className="testimonial">
              <p className="testimonial-text">
                "Kimberly holds space with such grace and clarity. I finally understand what conscious kink means—and it's changed everything about how I show up in relationships."
              </p>
              <cite className="testimonial-author">— J.L., Edgewalker Client</cite>
            </blockquote>
            <blockquote className="testimonial">
              <p className="testimonial-text">
                "The single session deep dive was exactly what I needed. Kimberly helped me move through a block I'd been stuck on for years. I left feeling lighter and more alive."
              </p>
              <cite className="testimonial-author">— Marcus T., Sacred Eruption Client</cite>
            </blockquote>
          </div>
        </div>
      </section>

      {/* Email Capture / Lead Magnet */}
      <section className="section-lead-magnet">
        <div className="container content-container">
          <div className="lead-magnet-box">
            <h2>Reclaiming the Forbidden</h2>
            <p>
              Download your free starter guide: <em>3 Ways Self-Sacrifice Culture Shows Up in Your Body (And How to Begin Releasing It)</em>
            </p>
            <form className="lead-form">
              <input
                type="email"
                placeholder="Your email address"
                className="lead-input"
                required
                aria-label="Email address"
              />
              <Button type="submit" variant="primary">
                Get the Guide
              </Button>
            </form>
            <p className="privacy-note">
              Your email is sacred. No spam, ever. Unsubscribe anytime.
            </p>
          </div>
        </div>
      </section>

      {/* Final CTA */}
      <section className="section-final-cta">
        <div className="container content-container centered">
          <h2>Ready to Begin?</h2>
          <p>
            Book a Curiosity Call and take the first step toward deeper intimacy, embodied power, and conscious pleasure.
          </p>
          <Button href="/consult" variant="primary">
            Book a Curiosity Call
          </Button>
          <p className="cta-subtext-footer">
            A low-pressure space to slow down, ask questions, and feel into what's next.
          </p>
        </div>
      </section>

      <style jsx>{`
        /* Role Descriptor */
        .role-descriptor {
          background: var(--neutral-soft-white);
          padding: 1.25rem 1.5rem;
          border-bottom: 1px solid rgba(139, 58, 71, 0.08);
        }

        .descriptor-text {
          font-size: clamp(0.9rem, 1.5vw, 1rem);
          color: var(--neutral-charcoal);
          text-align: center;
          line-height: 1.5;
          font-weight: 500;
          max-width: 900px;
          margin: 0 auto;
        }

        /* Hero Section */
        .hero {
          min-height: 80vh;
          display: flex;
          align-items: center;
          justify-content: center;
          background: linear-gradient(135deg, var(--neutral-cream) 0%, var(--secondary-warm-beige) 100%);
          padding: 4rem 1.5rem;
        }

        .hero-layout {
          display: grid;
          grid-template-columns: 1fr;
          gap: 3rem;
          align-items: center;
          max-width: 1200px;
          margin: 0 auto;
        }

        @media (min-width: 768px) {
          .hero-layout {
            grid-template-columns: 1.1fr 1fr;
            gap: 4rem;
          }
        }

        .hero-content {
          max-width: 600px;
        }

        @media (max-width: 767px) {
          .hero-content {
            text-align: center;
          }
        }

        .hero-title {
          font-size: clamp(2.5rem, 6vw, 5rem);
          margin-bottom: 1.5rem;
          line-height: 1.1;
        }

        .gradient-text {
          background: linear-gradient(135deg, var(--primary-burgundy) 0%, var(--accent-terracotta) 100%);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
          background-clip: text;
        }

        .hero-subtitle {
          font-size: clamp(1.1rem, 2vw, 1.35rem);
          color: var(--neutral-warm-gray);
          margin-bottom: 2.5rem;
          line-height: 1.7;
        }

        .hero-cta {
          display: flex;
          flex-direction: column;
          gap: 0.75rem;
          align-items: flex-start;
        }

        @media (max-width: 767px) {
          .hero-cta {
            align-items: center;
          }
        }

        .cta-subtext {
          font-size: 0.95rem;
          color: var(--neutral-warm-gray);
          font-style: italic;
          margin: 0;
        }

        .cta-subtext-footer {
          font-size: 0.95rem;
          color: var(--neutral-warm-gray);
          font-style: italic;
          margin-top: 0.75rem;
        }

        .hero-image {
          display: flex;
          justify-content: center;
        }

        :global(.hero-photo) {
          border-radius: 1rem;
          box-shadow: 0 20px 50px rgba(139, 58, 71, 0.3);
          object-fit: cover;
          width: 100%;
          height: auto;
          max-width: 500px;
        }

        /* Section Styles */
        .section-title {
          font-size: clamp(2rem, 4vw, 3rem);
          margin-bottom: 2rem;
          text-align: center;
        }

        .section-title.centered {
          text-align: center;
        }

        .section-intro {
          font-size: 1.15rem;
          color: var(--neutral-warm-gray);
          max-width: 700px;
          margin: 0 auto 3rem;
          line-height: 1.7;
        }

        .section-intro.centered {
          text-align: center;
        }

        /* Who This Is For */
        .section-who {
          background: var(--neutral-soft-white);
        }

        .who-grid {
          display: grid;
          grid-template-columns: 1fr;
          gap: 2rem;
          margin-top: 3rem;
        }

        @media (min-width: 768px) {
          .who-grid {
            grid-template-columns: repeat(3, 1fr);
          }
        }

        .who-card {
          padding: 2rem;
          background: var(--neutral-cream);
          border-radius: 1rem;
          transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .who-card:hover {
          transform: translateY(-5px);
          box-shadow: 0 10px 30px rgba(139, 58, 71, 0.15);
        }

        .who-card h3 {
          color: var(--primary-burgundy);
          font-size: 1.5rem;
          margin-bottom: 1rem;
        }

        .who-card p {
          color: var(--neutral-charcoal);
          line-height: 1.7;
        }

        /* How It Works */
        .section-how {
          background: linear-gradient(135deg, var(--primary-burgundy) 0%, var(--primary-wine) 100%);
          color: var(--neutral-soft-white);
        }

        .section-how .section-title {
          color: var(--neutral-soft-white);
        }

        .steps-grid {
          display: grid;
          grid-template-columns: 1fr;
          gap: 3rem;
          margin-top: 3rem;
        }

        @media (min-width: 768px) {
          .steps-grid {
            grid-template-columns: repeat(3, 1fr);
          }
        }

        .step {
          text-align: center;
        }

        .step-number {
          width: 60px;
          height: 60px;
          border-radius: 50%;
          background: var(--accent-terracotta);
          color: var(--neutral-soft-white);
          font-size: 1.75rem;
          font-weight: 700;
          display: flex;
          align-items: center;
          justify-content: center;
          margin: 0 auto 1.5rem;
          font-family: var(--font-heading);
        }

        .step h3 {
          color: var(--neutral-soft-white);
          font-size: 1.5rem;
          margin-bottom: 1rem;
        }

        .step p {
          color: var(--neutral-cream);
          line-height: 1.7;
        }

        /* Offerings */
        .section-offerings {
          background: var(--neutral-soft-white);
        }

        .offerings-grid {
          display: grid;
          grid-template-columns: 1fr;
          gap: 2rem;
          margin: 3rem 0;
        }

        @media (min-width: 768px) {
          .offerings-grid {
            grid-template-columns: repeat(3, 1fr);
          }
        }

        .offering-card {
          padding: 2.5rem 2rem;
          background: white;
          border: 2px solid var(--neutral-cream);
          border-radius: 1rem;
          display: flex;
          flex-direction: column;
          position: relative;
          transition: all 0.3s ease;
        }

        .offering-card:hover {
          border-color: var(--primary-burgundy);
          box-shadow: 0 15px 40px rgba(139, 58, 71, 0.2);
          transform: translateY(-8px);
        }

        .offering-card.featured {
          border-color: var(--primary-burgundy);
          background: linear-gradient(135deg, var(--neutral-soft-white) 0%, var(--neutral-cream) 100%);
        }

        .offering-badge {
          position: absolute;
          top: -12px;
          right: 20px;
          background: var(--accent-terracotta);
          color: var(--neutral-soft-white);
          padding: 0.4rem 1rem;
          border-radius: 2rem;
          font-size: 0.85rem;
          font-weight: 600;
        }

        .offering-card h3 {
          font-size: 1.75rem;
          color: var(--primary-burgundy);
          margin-bottom: 0.5rem;
        }

        .offering-duration {
          font-size: 0.95rem;
          color: var(--neutral-warm-gray);
          margin-bottom: 1.5rem;
          font-weight: 500;
        }

        .offering-description {
          font-size: 1rem;
          line-height: 1.7;
          margin-bottom: 1.5rem;
          flex-grow: 1;
        }

        .offering-features {
          list-style: none;
          margin-bottom: 1.5rem;
        }

        .offering-features li {
          padding: 0.5rem 0;
          padding-left: 1.5rem;
          position: relative;
          color: var(--neutral-charcoal);
          font-size: 0.95rem;
        }

        .offering-features li::before {
          content: '✓';
          position: absolute;
          left: 0;
          color: var(--accent-terracotta);
          font-weight: 700;
        }

        .offering-price {
          font-size: 1.25rem;
          font-weight: 600;
          color: var(--primary-burgundy);
          margin-bottom: 1.5rem;
        }

        .cta-centered {
          text-align: center;
          margin-top: 3rem;
        }

        /* Philosophy */
        .section-philosophy {
          background: var(--neutral-cream);
        }

        .philosophy-intro {
          font-size: 1.15rem;
          line-height: 1.8;
          margin-bottom: 3rem;
          color: var(--neutral-charcoal);
        }

        .philosophy-values {
          display: grid;
          grid-template-columns: 1fr;
          gap: 2rem;
        }

        @media (min-width: 768px) {
          .philosophy-values {
            grid-template-columns: repeat(2, 1fr);
          }
        }

        .value {
          padding: 1.5rem;
          background: var(--neutral-soft-white);
          border-left: 4px solid var(--accent-terracotta);
          border-radius: 0.5rem;
        }

        .value h4 {
          color: var(--primary-burgundy);
          font-size: 1.25rem;
          margin-bottom: 0.75rem;
        }

        .value p {
          color: var(--neutral-charcoal);
          line-height: 1.6;
        }

        /* Testimonial Hero */
        .section-testimonial-hero {
          background: var(--neutral-cream);
          padding: 4rem 0;
        }

        .testimonial-hero {
          text-align: center;
          padding: 3rem 2rem;
          background: white;
          border-radius: 1rem;
          box-shadow: 0 10px 30px rgba(139, 58, 71, 0.15);
          border-top: 4px solid var(--accent-terracotta);
          max-width: 800px;
          margin: 0 auto;
        }

        .testimonial-hero-text {
          font-size: 1.3rem;
          line-height: 1.7;
          font-style: italic;
          color: var(--neutral-charcoal);
          margin-bottom: 1.5rem;
        }

        .testimonial-hero-author {
          font-size: 1rem;
          color: var(--neutral-warm-gray);
          font-style: normal;
          font-weight: 600;
        }

        /* Testimonials */
        .section-testimonials {
          background: var(--neutral-soft-white);
        }

        .testimonials-grid {
          display: grid;
          grid-template-columns: 1fr;
          gap: 2rem;
          margin-top: 3rem;
        }

        @media (min-width: 768px) {
          .testimonials-grid {
            grid-template-columns: repeat(3, 1fr);
          }
        }

        .testimonial {
          padding: 2rem;
          background: white;
          border-radius: 1rem;
          box-shadow: 0 5px 20px rgba(139, 58, 71, 0.1);
          border-top: 4px solid var(--accent-terracotta);
        }

        .testimonial-text {
          font-size: 1.05rem;
          line-height: 1.7;
          font-style: italic;
          color: var(--neutral-charcoal);
          margin-bottom: 1.5rem;
        }

        .testimonial-author {
          font-size: 0.95rem;
          color: var(--neutral-warm-gray);
          font-style: normal;
          font-weight: 600;
        }

        /* Lead Magnet */
        .section-lead-magnet {
          background: linear-gradient(135deg, var(--accent-terracotta) 0%, var(--accent-coral) 100%);
          color: var(--neutral-soft-white);
        }

        .lead-magnet-box {
          text-align: center;
          padding: 3rem 2rem;
        }

        .lead-magnet-box h2 {
          color: var(--neutral-soft-white);
          margin-bottom: 1rem;
        }

        .lead-magnet-box p {
          font-size: 1.15rem;
          margin-bottom: 2rem;
          color: var(--neutral-soft-white);
        }

        .lead-form {
          display: flex;
          gap: 1rem;
          max-width: 500px;
          margin: 0 auto 1rem;
          flex-direction: column;
        }

        @media (min-width: 768px) {
          .lead-form {
            flex-direction: row;
          }
        }

        .lead-input {
          flex: 1;
          padding: 1rem 1.5rem;
          border: none;
          border-radius: 0.5rem;
          font-family: var(--font-body);
          font-size: 1rem;
        }

        .privacy-note {
          font-size: 0.85rem;
          color: rgba(255, 255, 255, 0.8);
          font-style: italic;
        }

        /* Final CTA */
        .section-final-cta {
          background: var(--neutral-cream);
          text-align: center;
        }

        .centered {
          text-align: center;
        }

        .section-final-cta h2 {
          margin-bottom: 1rem;
        }

        .section-final-cta p {
          font-size: 1.15rem;
          color: var(--neutral-warm-gray);
          margin-bottom: 2rem;
        }
      `}</style>
    </>
  );
}
