'use client';

import { useState } from 'react';
import Button from '@/components/ui/Button';
import AnimateOnScroll from '@/components/ui/AnimateOnScroll';
import Image from 'next/image';

export default function Home() {
  const [stayEmail, setStayEmail] = useState('');
  const [stayName, setStayName] = useState('');
  const [stayDone, setStayDone] = useState(false);
  const [stayLoading, setStayLoading] = useState(false);

  async function handleStaySubmit(e: React.FormEvent) {
    e.preventDefault();
    setStayLoading(true);
    try {
      await fetch('/api/subscribe', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: stayName, email: stayEmail }),
      });
    } catch { /* fail silently */ }
    setStayDone(true);
    setStayLoading(false);
  }

  return (
    <>
      {/* Hero Section */}
      <section className="hero">
        <div className="container">
          <div className="hero-layout">
            <div className="hero-content">
              <h1 className="hero-title">That Deeper Feeling</h1>
              <p className="hero-tagline">
                Where sensuality, soul and surrender meet.
              </p>
              <p className="hero-subheadline">
                For those ready to reclaim the parts of you that have been forbidden.
              </p>
              <div className="hero-poetry">
                <p>For those who learned to shrink in order to belong.</p>
                <p>For those who have felt themselves go quiet.</p>
                <p>For those who know there is more.</p>
              </div>
              <p className="hero-supporting">
                Where the power around your mental, emotional, physical, spiritual and sexual energy can be reclaimed.
              </p>
              <p className="hero-supporting">
                Where your voice, desires, power and self trust return.
              </p>
              <p className="hero-supporting">
                Through curiosity, play and embodied exploration.
              </p>
              <p className="hero-pull">
                If something in you feels that curious pull&hellip; you&rsquo;re in the right place.
              </p>
              <div className="hero-cta">
                <Button href="/consult" variant="primary">
                  Book a Curiosity Call
                </Button>
              </div>
            </div>
            <div className="hero-image">
              <Image
                src="/images/kimberly-hero.jpg"
                alt="Kimberly Bryant - Intimacy Coach specializing in conscious kink and embodied reclamation"
                width={500}
                height={600}
                priority
                sizes="(max-width: 767px) 90vw, 45vw"
                className="hero-photo"
              />
            </div>
          </div>
        </div>
      </section>

      {/* Who This Is For */}
      <section className="section-who">
        <div className="container content-container">
          <AnimateOnScroll>
            <h2 className="section-title">This work may be for you if&hellip;</h2>
            <ul className="who-list">
              <li>You&rsquo;re deconstructing something you once gave your life to</li>
              <li>You&rsquo;re tired of handing your safety, worth, or authority to someone else</li>
              <li>You feel disconnected from your desire, your voice, or your inner truth</li>
              <li>You&rsquo;re curious about intimacy, power, and presence beyond shame or performance</li>
              <li>You&rsquo;re ready for depth, honesty, and embodied exploration</li>
            </ul>
          </AnimateOnScroll>
        </div>
      </section>

      {/* Testimonial */}
      <section className="section-testimonial">
        <div className="container content-container">
          <blockquote className="testimonial">
            <p className="testimonial-text">
              &ldquo;Last spring, I decided I needed to make a change&mdash;I was stuck in a rut and unsure what to do. When I saw Kimberly&rsquo;s profile on Fetlife, everything she described resonated with me. I reached out with no idea what I was getting into, but I wanted to give it a shot.
            </p>
            <p className="testimonial-text">
              Kimberly responded with clear next steps: a Zoom call and STI screening for safety. I agreed, and found her to be warm, friendly, and understanding. Our first in-person meeting involved a questionnaire to help her understand my interests and design a plan for future sessions. She also listened deeply to my past experiences&mdash;including an ex-girlfriend who had been married (unknown to me), who looked at houses with me, then suddenly ghosted. I thought I was over the pain. Kimberly knew differently.
            </p>
            <p className="testimonial-text">
              Over the next couple of sessions, she asked thoughtful questions while introducing me to things I&rsquo;d never considered, like sensory play. In the third session, Kimberly told me she wanted to do something that would probably make me cry. I was nervous, but I trusted her&mdash;and I&rsquo;m so glad I did. She did make me cry. A lot. That day, she helped me realize my ex had done far more damage to me mentally and emotionally than I&rsquo;d ever acknowledged. It had been five years, but I wasn&rsquo;t over it. I had built walls and shut down my feelings without even realizing it. Kimberly helped me begin to feel again.
            </p>
            <p className="testimonial-text">
              Since then, she&rsquo;s continued supporting me in reconnecting with my emotions. She never judged&mdash;only offered care and understanding. Kimberly has helped me enjoy my life in ways I didn&rsquo;t think were possible. She has a real gift for helping people feel again.
            </p>
            <p className="testimonial-text">
              Reaching out to Kimberly turned out to be one of the best decisions I&rsquo;ve ever made. If you&rsquo;re curious but not sure if this work is for you, I&rsquo;d recommend reaching out, talking to her, and seeing if what she offers might help you more than you think.&rdquo;
            </p>
            <cite className="testimonial-author">— Client, Spring 2025</cite>
          </blockquote>
        </div>
      </section>

      {/* Approach */}
      <section className="section-approach">
        <div className="container content-container">
          <AnimateOnScroll>
            <p className="approach-intro">
              This work is rooted in consent-centered, body-led practices that honor nervous system awareness, pacing, and choice.
            </p>
            <p className="approach-statement">
              We slow down, move with awareness, and allow authority to be reclaimed from the inside out.
            </p>
          </AnimateOnScroll>
        </div>
      </section>

      {/* Containers Overview */}
      <section className="section-containers">
        <div className="container content-container">
          <AnimateOnScroll>
            <h2 className="containers-title">Ways We Can Work Together</h2>
          </AnimateOnScroll>

          <AnimateOnScroll delay={100}>
            <div className="container-card">
              <div className="container-header"><h4>Return to Power</h4></div>
              <p className="container-description">A six month private container for rebuilding self trust, desire, and embodied authority from the inside out.</p>
            </div>
          </AnimateOnScroll>

          <AnimateOnScroll delay={150}>
            <div className="container-card">
              <div className="container-header"><h4>Edgewalker</h4></div>
              <p className="container-description">A three month private journey for those ready to explore power, intimacy, and identity at the edge of growth.</p>
            </div>
          </AnimateOnScroll>

          <AnimateOnScroll delay={200}>
            <div className="container-card">
              <div className="container-header"><h4>Sacred Eruption</h4></div>
              <p className="container-description">A single deep dive immersion for focused, embodied breakthrough work.</p>
            </div>
          </AnimateOnScroll>

          <AnimateOnScroll delay={250}>
            <div className="container-card">
              <div className="container-header"><h4>Reclaiming the Forbidden</h4></div>
              <p className="container-description">In person workshops, retreats, and gatherings where we explore voice, desire, and power in real time.</p>
            </div>
          </AnimateOnScroll>

          <div className="containers-closing">
            <p>Rooted in choice.</p>
            <p>Held with intention.</p>
            <p>Balanced between depth and play.</p>
          </div>
        </div>
      </section>

      {/* Stay Connected — Email Capture */}
      <section className="section-stay">
        <div className="container content-container">
          <AnimateOnScroll>
            <span className="eyebrow">Stay Close</span>
            <h2 className="stay-heading">Not ready yet?</h2>
            <p className="stay-subhead">
              Receive invitations, insights, and resources for deepening your journey — in your own time.
            </p>
            {stayDone ? (
              <p className="stay-success">You&rsquo;re in. Welcome.</p>
            ) : (
              <form className="stay-form" onSubmit={handleStaySubmit}>
                <input
                  type="text"
                  placeholder="Your name"
                  className="stay-input"
                  value={stayName}
                  onChange={(e) => setStayName(e.target.value)}
                  aria-label="Your name"
                />
                <input
                  type="email"
                  placeholder="Your email"
                  className="stay-input"
                  value={stayEmail}
                  onChange={(e) => setStayEmail(e.target.value)}
                  required
                  aria-label="Your email address"
                />
                <button type="submit" className="stay-button" disabled={stayLoading}>
                  {stayLoading ? 'Sending…' : 'Stay Connected'}
                </button>
              </form>
            )}
          </AnimateOnScroll>
        </div>
      </section>

      {/* Final CTA */}
      <section className="section-final-cta">
        <div className="container content-container centered">
          <AnimateOnScroll>
            <h2>Not sure where to begin?</h2>
            <p className="final-cta-text">
              Every journey starts with a Curiosity Call.
            </p>
            <p className="final-cta-subtext">
              A slow, intentional space to get curious and feel what&rsquo;s true.
            </p>
            <Button href="/consult" variant="primary">
              Book Your Curiosity Call
            </Button>
          </AnimateOnScroll>
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

        .hero-tagline {
          font-size: clamp(1.15rem, 2.2vw, 1.45rem);
          color: var(--primary-wine);
          font-style: italic;
          margin-bottom: 2rem;
          line-height: 1.6;
        }

        .hero-subheadline {
          font-size: clamp(1.1rem, 2vw, 1.3rem);
          color: var(--neutral-charcoal);
          margin-bottom: 1.5rem;
          line-height: 1.6;
          font-weight: 500;
        }

        .hero-poetry {
          margin-bottom: 2rem;
        }

        .hero-poetry p {
          font-size: clamp(1rem, 1.8vw, 1.1rem);
          color: var(--neutral-warm-gray);
          line-height: 1.7;
          margin-bottom: 0.25rem;
          font-style: italic;
        }

        .hero-supporting {
          font-size: clamp(0.95rem, 1.8vw, 1.1rem);
          color: var(--neutral-charcoal);
          margin-bottom: 0.75rem;
          line-height: 1.7;
        }

        .hero-pull {
          font-size: clamp(1rem, 1.8vw, 1.15rem);
          color: var(--primary-wine);
          font-weight: 500;
          margin-top: 1.5rem;
          margin-bottom: 2rem;
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

        /* Containers Overview */
        .section-containers {
          background: var(--neutral-cream);
          padding: 5rem 0;
        }

        .containers-title {
          font-size: clamp(1.75rem, 3vw, 2.5rem);
          text-align: center;
          color: var(--primary-burgundy);
          margin-bottom: 3rem;
        }

        .container-card {
          background: white;
          padding: 1.75rem 2rem;
          border-radius: 1rem;
          margin-bottom: 1rem;
          border-left: 4px solid var(--accent-terracotta);
          box-shadow: 0 5px 20px rgba(139, 58, 71, 0.08);
        }

        .container-header {
          margin-bottom: 0.75rem;
        }

        .container-card h4 {
          font-size: 1.4rem;
          color: var(--primary-burgundy);
          margin: 0;
        }

        .container-description {
          font-size: 1rem;
          color: var(--neutral-charcoal);
          line-height: 1.7;
          margin: 0;
        }

        .containers-closing {
          text-align: center;
          margin-top: 3rem;
        }

        .containers-closing p {
          font-size: 1.1rem;
          line-height: 1.5;
          color: var(--neutral-warm-gray);
          font-style: italic;
          margin-bottom: 0.25rem;
        }

        /* Stay Connected */
        .section-stay {
          background: linear-gradient(135deg, var(--primary-burgundy) 0%, var(--primary-wine) 100%);
          padding: 5rem 0;
          text-align: center;
        }

        .stay-heading {
          font-size: clamp(2rem, 4vw, 3rem);
          color: var(--neutral-soft-white);
          margin-bottom: 1rem;
        }

        .stay-subhead {
          font-size: 1.1rem;
          color: var(--neutral-cream);
          font-style: italic;
          line-height: 1.7;
          margin-bottom: 2rem;
          max-width: 500px;
          margin-left: auto;
          margin-right: auto;
        }

        .stay-form {
          display: flex;
          flex-direction: column;
          gap: 0.75rem;
          max-width: 380px;
          margin: 0 auto;
        }

        .stay-input {
          padding: 0.85rem 1.25rem;
          border: 1px solid rgba(255,255,255,0.3);
          border-radius: 0.5rem;
          font-family: var(--font-body);
          font-size: 1rem;
          background: rgba(255,255,255,0.12);
          color: var(--neutral-soft-white);
          backdrop-filter: blur(4px);
        }

        .stay-input::placeholder {
          color: rgba(255,255,255,0.6);
        }

        .stay-input:focus {
          outline: none;
          border-color: var(--accent-terracotta);
          background: rgba(255,255,255,0.18);
        }

        .stay-button {
          padding: 0.9rem 1.5rem;
          background: var(--accent-terracotta);
          color: var(--neutral-soft-white);
          border: none;
          border-radius: 0.5rem;
          font-family: var(--font-body);
          font-size: 1rem;
          font-weight: 600;
          cursor: pointer;
          transition: background 0.2s, transform 0.15s;
        }

        .stay-button:hover:not(:disabled) {
          background: var(--accent-coral);
          transform: translateY(-2px);
        }

        .stay-button:disabled {
          opacity: 0.7;
          cursor: not-allowed;
        }

        .stay-success {
          font-size: 1.2rem;
          color: var(--neutral-cream);
          font-style: italic;
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
          font-size: 1.2rem;
          color: var(--neutral-charcoal);
          margin-bottom: 0.5rem;
          max-width: 700px;
          margin-left: auto;
          margin-right: auto;
          line-height: 1.7;
        }

        .final-cta-subtext {
          font-size: 1.05rem;
          color: var(--neutral-warm-gray);
          font-style: italic;
          margin-bottom: 2rem;
          line-height: 1.7;
        }
      `}</style>
    </>
  );
}
