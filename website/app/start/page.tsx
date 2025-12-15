'use client';

import Button from '@/components/ui/Button';

export default function StartHerePage() {
  return (
    <>
      {/* Hero Section */}
      <section className="start-hero">
        <div className="container content-container">
          <h1>Start Here</h1>
          <p className="hero-subtitle">
            Welcome.
          </p>
          <p className="hero-subtitle">
            If you've landed here, something in you is already listening.
          </p>
        </div>
      </section>

      {/* Opening */}
      <section className="start-opening">
        <div className="container content-container">
          <p>
            Maybe you've left a high-demand religion, relationship, or culture.
            Maybe you've done the "right" things and still feel disconnected from your body, your desire, or your sense of self.
            Maybe you're successful on the outside and quietly aching on the inside.
          </p>
          <p>
            This space exists for that moment.
          </p>
        </div>
      </section>

      {/* What This Work Is */}
      <section className="start-section">
        <div className="container content-container">
          <h2>What This Work Is</h2>
          <p>
            That Deeper Feeling is not therapy.
            It's not performance.
            It's not about fixing you.
          </p>
          <p>
            I offer private coaching and immersive containers rooted in nervous-system awareness, consent-based intimacy, somatic presence, and embodied authority.
          </p>
          <p>This work is about helping you:</p>
          <ul className="start-list">
            <li>Come back into your body</li>
            <li>Reclaim your internal authority</li>
            <li>Untangle shame from desire</li>
            <li>Learn how to feel safe being fully yourself</li>
          </ul>
          <p>Slowly. Intentionally. With care.</p>
        </div>
      </section>

      {/* Who This Is For */}
      <section className="start-section alt">
        <div className="container content-container">
          <h2>Who This Is For</h2>
          <p>This work may be for you if:</p>
          <ul className="start-list">
            <li>You've left or are questioning a high-demand system and feel unmoored</li>
            <li>You struggle to trust your body, your wants, or your "yes" and "no"</li>
            <li>You feel disconnected from desire, pleasure, or aliveness</li>
            <li>You're tired of self-abandoning to stay safe or loved</li>
            <li>You want depth, honesty, and embodiment without shame or pressure</li>
          </ul>
          <p>
            You don't need to be "spiritual."
            You don't need to be kinky.
            You don't need to know the language yet.
          </p>
          <p><strong>Curiosity is enough.</strong></p>
        </div>
      </section>

      {/* What Makes This Work Different */}
      <section className="start-section">
        <div className="container content-container">
          <h2>What Makes This Work Different</h2>
          <p>
            This is kink-aware, consent-centered, trauma-trained work.
          </p>
          <div className="definition">
            <p><strong>By kink-aware, I mean:</strong></p>
            <p>
              We acknowledge power, choice, boundaries, and nervous system responses — without performance, coercion, or spectacle.
            </p>
          </div>
          <div className="definition">
            <p><strong>By consent-centered, I mean:</strong></p>
            <p>
              Your pace matters. Your body leads. Nothing is forced or rushed.
            </p>
          </div>
          <div className="definition">
            <p><strong>By embodied, I mean:</strong></p>
            <p>
              We don't just talk about change. We feel it, practice it, and integrate it.
            </p>
          </div>
          <p>This work honors both tenderness and truth.</p>
        </div>
      </section>

      {/* How to Begin */}
      <section className="start-section alt">
        <div className="container content-container">
          <h2>How to Begin</h2>
          <p>
            The best place to start is a Curiosity Call.
          </p>
          <p>This is a low-pressure conversation where we:</p>
          <ul className="start-list">
            <li>Slow things down</li>
            <li>Get clear on what you're navigating</li>
            <li>Explore whether working together feels right</li>
          </ul>
          <p>
            There is no obligation.
            No convincing.
            No pushing.
          </p>
          <p>Just a gentle entry point.</p>
        </div>
      </section>

      {/* CTA */}
      <section className="start-cta">
        <div className="container content-container centered">
          <h2>Book a Curiosity Call</h2>
          <p>
            A low-pressure space to slow down, ask questions, and feel into what's next.
          </p>
          <Button href="/consult" variant="primary">
            Book a Curiosity Call
          </Button>
        </div>
      </section>

      {/* Gentle Note */}
      <section className="start-section">
        <div className="container content-container centered">
          <h3>A Gentle Note</h3>
          <p>
            You don't need to be ready for everything.
            You don't need to know where this leads.
          </p>
          <p>
            You only need to be willing to listen to the part of you that brought you here.
          </p>
          <p><strong>That's enough.</strong></p>
        </div>
      </section>

      <style jsx>{`
        /* Hero */
        .start-hero {
          background: linear-gradient(135deg, var(--neutral-cream) 0%, var(--secondary-warm-beige) 100%);
          padding: 5rem 1.5rem 4rem;
          text-align: center;
        }

        .start-hero h1 {
          font-size: clamp(2.5rem, 5vw, 4rem);
          margin-bottom: 1.5rem;
        }

        .hero-subtitle {
          font-size: clamp(1.1rem, 2vw, 1.3rem);
          color: var(--neutral-warm-gray);
          line-height: 1.7;
          margin-bottom: 1rem;
        }

        /* Opening */
        .start-opening {
          background: var(--neutral-soft-white);
          padding: 4rem 0;
        }

        .start-opening p {
          font-size: 1.15rem;
          line-height: 1.8;
          color: var(--neutral-charcoal);
          margin-bottom: 1.5rem;
        }

        .start-opening p:last-child {
          font-style: italic;
          color: var(--primary-wine);
        }

        /* Sections */
        .start-section {
          background: var(--neutral-soft-white);
          padding: 5rem 0;
        }

        .start-section.alt {
          background: var(--neutral-cream);
        }

        .start-section h2 {
          font-size: clamp(2rem, 4vw, 3rem);
          margin-bottom: 2rem;
          color: var(--primary-burgundy);
        }

        .start-section h3 {
          font-size: clamp(1.5rem, 3vw, 2rem);
          margin-bottom: 1.5rem;
          color: var(--primary-burgundy);
        }

        .start-section p {
          font-size: 1.1rem;
          line-height: 1.8;
          color: var(--neutral-charcoal);
          margin-bottom: 1.5rem;
        }

        .start-list {
          list-style: none;
          padding: 0;
          margin: 2rem 0;
        }

        .start-list li {
          padding: 0.75rem 0;
          padding-left: 2rem;
          position: relative;
          font-size: 1.1rem;
          color: var(--neutral-charcoal);
          line-height: 1.6;
        }

        .start-list li::before {
          content: '•';
          position: absolute;
          left: 0;
          color: var(--accent-terracotta);
          font-size: 1.5rem;
          line-height: 1;
        }

        .definition {
          background: white;
          padding: 1.5rem 2rem;
          border-left: 4px solid var(--accent-terracotta);
          margin: 2rem 0;
          border-radius: 0.5rem;
        }

        .definition p {
          margin-bottom: 0.75rem;
        }

        .definition p:last-child {
          margin-bottom: 0;
        }

        /* CTA */
        .start-cta {
          background: var(--primary-burgundy);
          color: var(--neutral-soft-white);
          padding: 5rem 0;
        }

        .start-cta h2 {
          color: var(--neutral-soft-white);
          margin-bottom: 1rem;
        }

        .start-cta p {
          color: var(--neutral-cream);
          font-size: 1.15rem;
          margin-bottom: 2rem;
          line-height: 1.7;
        }

        .centered {
          text-align: center;
        }
      `}</style>
    </>
  );
}
