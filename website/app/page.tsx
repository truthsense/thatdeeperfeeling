'use client';

import Button from '@/components/ui/Button';
import Image from 'next/image';

export default function Home() {
  return (
    <>
      {/* Hero Section */}
      <section className="hero">
        <div className="container">
          <div className="hero-layout">
            <div className="hero-content">
              <h1 className="hero-title">That Deeper Feeling</h1>
              <p className="hero-subheadline">
                I offer private coaching and immersive containers for people reclaiming their power, desire, and embodied authority after leaving high-demand systems.
              </p>
              <p className="hero-supporting">
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

      {/* Who This Is For */}
      <section className="section-who">
        <div className="container content-container">
          <h2 className="section-title">This work may be for you if you\'re:</h2>
          <ul className="who-list">
            <li>Deconstructing a high-demand religion, culture, or relational dynamic</li>
            <li>Tired of outsourcing your sense of safety, worth, or authority</li>
            <li>Disconnected from your body, desire, or inner truth</li>
            <li>Curious about intimacy, power, and presence beyond shame or performance</li>
            <li>Ready for depth, honesty, and embodied exploration</li>
          </ul>
        </div>
      </section>

      {/* Testimonial */}
      <section className="section-testimonial">
        <div className="container content-container">
          <blockquote className="testimonial">
            <p className="testimonial-text">
              "Last spring, I decided I needed to make a change—I was stuck in a rut and unsure what to do. When I saw Kimberly\'s profile on Fetlife, everything she described resonated with me. I reached out with no idea what I was getting into, but I wanted to give it a shot.
            </p>
            <p className="testimonial-text">
              Kimberly responded with clear next steps: a Zoom call and STI screening for safety. I agreed, and found her to be warm, friendly, and understanding. Our first in-person meeting involved a questionnaire to help her understand my interests and design a plan for future sessions. She also listened deeply to my past experiences—including an ex-girlfriend who had been married (unknown to me), who looked at houses with me, then suddenly ghosted. I thought I was over the pain. Kimberly knew differently.
            </p>
            <p className="testimonial-text">
              Over the next couple of sessions, she asked thoughtful questions while introducing me to things I\'d never considered, like sensory play. In the third session, Kimberly told me she wanted to do something that would probably make me cry. I was nervous, but I trusted her—and I\'m so glad I did. She did make me cry. A lot. That day, she helped me realize my ex had done far more damage to me mentally and emotionally than I\'d ever acknowledged. It had been five years, but I wasn\'t over it. I had built walls and shut down my feelings without even realizing it. Kimberly helped me begin to feel again.
            </p>
            <p className="testimonial-text">
              Since then, she\'s continued supporting me in reconnecting with my emotions. She never judged—only offered care and understanding. Kimberly has helped me enjoy my life in ways I didn\'t think were possible. She has a real gift for helping people feel again.
            </p>
            <p className="testimonial-text">
              Reaching out to Kimberly turned out to be one of the best decisions I\'ve ever made. If you\'re curious but not sure if this work is for you, I\'d recommend reaching out, talking to her, and seeing if what she offers might help you more than you think."
            </p>
            <cite className="testimonial-author">— Client, Spring 2024</cite>
          </blockquote>
        </div>
      </section>

      {/* Approach */}
      <section className="section-approach">
        <div className="container content-container">
          <p className="approach-intro">
            This work is rooted in consent-centered, body-led practices that honor nervous system awareness, pacing, and choice.
          </p>
          <p className="approach-statement">
            Rather than overriding or fixing, we listen.<br />
            Rather than outsourcing authority, we bring it home.
          </p>
        </div>
      </section>

      {/* Offerings Preview */}
      <section className="section-offerings-preview">
        <div className="container content-container">
          <p className="offerings-intro">
            I offer several ways to enter this work, including:
          </p>
          <ul className="offerings-list">
            <li>Long-term one-on-one coaching containers</li>
            <li>Shorter immersive coaching journeys</li>
            <li>One-time deep-dive sessions</li>
            <li>In-person gatherings and retreats</li>
            <li>Community-based spaces for reflection and integration</li>
          </ul>
          <p className="offerings-explore">
            You can explore all current offerings here.
          </p>
          <div className="offerings-cta">
            <Button href="/offerings" variant="secondary">
              View Offerings
            </Button>
          </div>
        </div>
      </section>

      {/* Final CTA */}
      <section className="section-final-cta">
        <div className="container content-container centered">
          <h2>Ready to Begin?</h2>
          <p className="final-cta-text">
            Book a Curiosity Call to explore working together and see if one of these containers feels aligned for where you are right now.
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
          font-size: clamp(2.5rem, 6vw, 4.5rem);
          margin-bottom: 1.5rem;
          line-height: 1.1;
          color: var(--primary-burgundy);
        }

        .hero-subheadline {
          font-size: clamp(1.1rem, 2vw, 1.3rem);
          color: var(--neutral-charcoal);
          margin-bottom: 1.5rem;
          line-height: 1.6;
          font-weight: 500;
        }

        .hero-supporting {
          font-size: clamp(0.95rem, 1.8vw, 1.1rem);
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

        /* Who This Is For */
        .section-who {
          background: var(--neutral-soft-white);
          padding: 5rem 0;
        }

        .section-title {
          font-size: clamp(1.75rem, 3vw, 2.5rem);
          margin-bottom: 2.5rem;
          text-align: center;
          color: var(--primary-burgundy);
        }

        .who-list {
          list-style: none;
          max-width: 700px;
          margin: 0 auto;
          padding: 0;
        }

        .who-list li {
          padding: 1rem 0;
          padding-left: 2rem;
          position: relative;
          font-size: 1.1rem;
          color: var(--neutral-charcoal);
          line-height: 1.7;
        }

        .who-list li::before {
          content: '•';
          position: absolute;
          left: 0;
          color: var(--accent-terracotta);
          font-size: 1.5rem;
          line-height: 1.2;
        }

        /* Testimonial */
        .section-testimonial {
          background: var(--neutral-cream);
          padding: 5rem 0;
        }

        .testimonial {
          text-align: left;
          padding: 3rem 2.5rem;
          background: white;
          border-radius: 1rem;
          box-shadow: 0 10px 30px rgba(139, 58, 71, 0.15);
          border-top: 4px solid var(--accent-terracotta);
          max-width: 900px;
          margin: 0 auto;
        }

        @media (max-width: 767px) {
          .testimonial {
            padding: 2rem 1.5rem;
          }
        }

        .testimonial-text {
          font-size: 1.05rem;
          line-height: 1.8;
          font-style: italic;
          color: var(--neutral-charcoal);
          margin-bottom: 1.25rem;
        }

        .testimonial-text:last-of-type {
          margin-bottom: 1.5rem;
        }

        .testimonial-author {
          font-size: 1rem;
          color: var(--neutral-warm-gray);
          font-style: normal;
          font-weight: 600;
          text-align: right;
          display: block;
          margin-top: 1.5rem;
        }

        /* Approach */
        .section-approach {
          background: var(--neutral-soft-white);
          padding: 5rem 0;
        }

        .approach-intro {
          font-size: 1.25rem;
          line-height: 1.8;
          color: var(--neutral-charcoal);
          text-align: center;
          margin-bottom: 2rem;
          max-width: 800px;
          margin-left: auto;
          margin-right: auto;
        }

        .approach-statement {
          font-size: 1.15rem;
          line-height: 1.9;
          color: var(--neutral-warm-gray);
          text-align: center;
          font-style: italic;
          max-width: 700px;
          margin: 0 auto;
        }

        /* Offerings Preview */
        .section-offerings-preview {
          background: var(--neutral-cream);
          padding: 5rem 0;
        }

        .offerings-intro {
          font-size: 1.15rem;
          color: var(--neutral-charcoal);
          text-align: center;
          margin-bottom: 2rem;
        }

        .offerings-list {
          list-style: none;
          max-width: 600px;
          margin: 0 auto 2rem;
          padding: 0;
        }

        .offerings-list li {
          padding: 0.75rem 0;
          padding-left: 2rem;
          position: relative;
          font-size: 1.05rem;
          color: var(--neutral-charcoal);
          line-height: 1.7;
          text-align: center;
        }

        .offerings-list li::before {
          content: '•';
          position: absolute;
          left: 50%;
          transform: translateX(-150%);
          color: var(--accent-terracotta);
          font-size: 1.3rem;
        }

        .offerings-explore {
          font-size: 1.05rem;
          color: var(--neutral-warm-gray);
          text-align: center;
          margin-bottom: 2rem;
        }

        .offerings-cta {
          text-align: center;
        }

        /* Final CTA */
        .section-final-cta {
          background: var(--neutral-soft-white);
          padding: 5rem 0;
        }

        .centered {
          text-align: center;
        }

        .section-final-cta h2 {
          font-size: clamp(2rem, 4vw, 3rem);
          color: var(--primary-burgundy);
          margin-bottom: 1.5rem;
        }

        .final-cta-text {
          font-size: 1.15rem;
          color: var(--neutral-charcoal);
          margin-bottom: 2rem;
          max-width: 700px;
          margin-left: auto;
          margin-right: auto;
          line-height: 1.7;
        }
      `}</style>
    </>
  );
}
