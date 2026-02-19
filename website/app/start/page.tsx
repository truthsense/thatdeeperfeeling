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
            If you&rsquo;ve landed here, something in you is already listening.
          </p>
        </div>
      </section>

      {/* Opening */}
      <section className="start-opening">
        <div className="container content-container">
          <p>
            Maybe you&rsquo;ve left a high-demand religion, relationship, or culture.
            Maybe you&rsquo;ve done the &ldquo;right&rdquo; things and still feel disconnected from your body, your desire, or your sense of self.
            Maybe you feel successful on the outside and quietly aching on the inside.
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
            That Deeper Feeling is not therapy. It&rsquo;s not performance. It&rsquo;s not about fixing you.
          </p>
          <p>
            I offer private coaching and immersive containers rooted in nervous-system awareness, consent-based intimacy, somatic presence, embodied authority, and conscious exploration of power, desire, and erotic energy.
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
            <li>You&rsquo;ve left or are questioning a high-demand system</li>
            <li>You struggle to trust your body, your wants, or your &ldquo;yes&rdquo; and &ldquo;no&rdquo;</li>
            <li>You feel disconnected from desire, pleasure, or aliveness</li>
            <li>You&rsquo;re tired of self-abandoning to stay safe or loved</li>
            <li>You want depth, honesty, and embodiment</li>
          </ul>
          <p>You don&rsquo;t need to know the language yet.</p>
          <p><strong>If something in you feels that curious pull&hellip; that&rsquo;s enough.</strong></p>
        </div>
      </section>

      {/* What Makes This Work Different */}
      <section className="start-section">
        <div className="container content-container">
          <h2>What Makes This Work Different</h2>
          <p>
            This is kink-aware, consent-centered, trauma-informed work.
          </p>
          <div className="definition">
            <p><strong>By kink-aware, I mean:</strong></p>
            <p>
              We acknowledge power, choice, boundaries, nervous system responses, and erotic energy as living dynamics that can be explored consciously, playfully, and with deep respect.
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
              We don&rsquo;t just talk about change. We feel it. We practice it.
            </p>
          </div>
          <p>This work honors tenderness and truth.</p>
          <div className="permission-list">
            <p>We make space for play.</p>
            <p>For curiosity.</p>
            <p>For connection.</p>
            <p>For choice.</p>
            <p>For feeling.</p>
            <p>For permission.</p>
            <p>For moving slowly and intentionally into the parts of you that were once labeled &ldquo;too much&rdquo; or &ldquo;not allowed.&rdquo;</p>
          </div>
        </div>
      </section>

      {/* How to Begin */}
      <section className="start-section alt">
        <div className="container content-container">
          <h2>How to Begin</h2>
          <p>
            The best place to start is a Curiosity Call.
          </p>
          <p>
            If something in you feels that curious pull&hellip;
          </p>
        </div>
      </section>

      {/* Curiosity Call CTA */}
      <section className="start-cta">
        <div className="container content-container centered">
          <h2>Every journey begins with a Curiosity Call.</h2>
          <div className="cta-poetry">
            <p>A slow, intentional space.</p>
            <p>Rooted in play.</p>
            <p>Curiosity.</p>
            <p>Connection.</p>
            <p>Permission.</p>
            <p>Choice.</p>
          </div>
          <div className="cta-grounding">
            <p>We listen.</p>
            <p>We feel.</p>
            <p>We explore what&rsquo;s true.</p>
          </div>
          <div className="cta-investment">
            <p className="investment-amount">Investment: $125</p>
            <p className="investment-note">Applied toward your chosen container.</p>
          </div>
          <Button href="/consult" variant="primary">
            Book Your Curiosity Call
          </Button>
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

        .permission-list {
          margin: 2rem 0;
          text-align: center;
        }

        .permission-list p {
          font-size: 1.1rem;
          line-height: 1.6;
          color: var(--neutral-charcoal);
          margin-bottom: 0.25rem;
          font-style: italic;
        }

        .permission-list p:last-child {
          margin-top: 1rem;
          font-style: normal;
          font-size: 1.05rem;
          line-height: 1.8;
        }

        .cta-poetry {
          margin: 2rem 0 1.5rem;
        }

        .cta-poetry p {
          font-size: 1.1rem;
          line-height: 1.4;
          margin-bottom: 0.25rem;
          color: var(--neutral-cream);
          font-style: italic;
        }

        .cta-grounding {
          margin-bottom: 2rem;
        }

        .cta-grounding p {
          font-size: 1.15rem;
          line-height: 1.4;
          margin-bottom: 0.25rem;
          color: var(--neutral-soft-white);
        }

        .cta-investment {
          margin-bottom: 2rem;
        }

        .investment-amount {
          font-size: 1.3rem;
          font-weight: 600;
          color: var(--neutral-soft-white);
          margin-bottom: 0.25rem;
        }

        .investment-note {
          font-size: 0.95rem;
          color: var(--neutral-cream);
          font-style: italic;
        }
      `}</style>
    </>
  );
}
