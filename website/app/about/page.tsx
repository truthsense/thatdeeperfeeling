'use client';

import Button from '@/components/ui/Button';
import Image from 'next/image';

export default function AboutPage() {
  return (
    <>
      {/* Hero Section */}
      <section className="about-hero">
        <div className="container">
          <div className="about-hero-layout">
            <div className="about-hero-content">
              <h1>Meet Kimberly</h1>
              <p className="tagline">
                Guiding you home to your body, your power, and your deepest pleasure.
              </p>
            </div>
            <div className="about-hero-image">
              <Image
                src="/images/kimberly-professional.jpg"
                alt="Kimberly Bryant - Trauma-Informed Intimacy Coach"
                width={500}
                height={600}
                priority
                className="hero-professional-photo"
              />
            </div>
          </div>
        </div>
      </section>

      {/* Story Section */}
      <section className="about-story">
        <div className="container content-container">
          <div className="story-layout">
            <div className="story-content">
              <h2>My Work</h2>
              <p>
                I help people reclaim their power and pleasure—usually after they've been taught to fear both.
              </p>
              <p>
                My work exists to support individuals who are deconstructing high-demand religions, relationships, and cultures, and who are ready to return to their bodies, their truth, and their internal authority.
              </p>
              <p>
                Through embodied coaching, conscious kink principles, nervous system regulation, and sacred ritual, I create spaces where people can slow down, feel safely, and explore the parts of themselves that were once silenced, shamed, or forbidden.
              </p>
              <p>
                This work is not about fixing you. It's about remembering who you are—and learning how to live, relate, and choose from that place.
              </p>
            </div>

            {/* Featured Photo */}
            <div className="story-featured-image">
              <Image
                src="/images/kimberly-hero.jpg"
                alt="Kimberly Bryant - Intimacy and Sovereignty Coach"
                width={500}
                height={600}
                className="featured-photo"
              />
            </div>
          </div>

          {/* Additional Photos */}
          <div className="story-images">
            <div className="story-image-primary">
              <Image
                src="/images/kimberly-about-main.jpg"
                alt="Kimberly Bryant - Intimacy Coach"
                width={600}
                height={700}
                className="about-photo"
              />
            </div>
            <div className="story-image-secondary">
              <Image
                src="/images/kimberly-about-secondary.jpg"
                alt="Kimberly Bryant"
                width={600}
                height={700}
                className="about-photo"
              />
            </div>
          </div>
        </div>
      </section>

      {/* Philosophy Section */}
      <section className="about-philosophy">
        <div className="container content-container">
          <h2>My Approach</h2>
          <p className="philosophy-intro">
            My work is rooted in three core principles: trauma-trained care, consent culture, and embodied wisdom.
          </p>
          <div className="philosophy-grid">
            <div className="philosophy-item">
              <h3>Trauma-Trained</h3>
              <p>
                I honor your nervous system, your pacing, and your boundaries. Healing isn't linear, and neither is pleasure. We move at the speed of safety.
              </p>
            </div>
            <div className="philosophy-item">
              <h3>Consent-Centered</h3>
              <p>
                Clear communication, enthusiastic yes's, and the absolute right to change your mind. Consent isn't just a checkbox—it's a practice we cultivate together.
              </p>
            </div>
            <div className="philosophy-item">
              <h3>Kink-Aware & Sex-Positive</h3>
              <p>
                BDSM, power exchange, and alternative relationship structures are honored here. Your desires aren't something to fix—they're portals to deeper knowing.
              </p>
            </div>
            <div className="philosophy-item">
              <h3>Embodied Wisdom</h3>
              <p>
                Your body holds answers your mind hasn't found yet. We work somatically, honoring sensation, intuition, and the intelligence of your felt experience.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Credentials Section */}
      <section className="about-credentials">
        <div className="container content-container">
          <h2>Training & Experience</h2>
          <div className="credentials-content">
            <div className="credential-item">
              <h4>Certifications & Training</h4>
              <ul>
                <li>Certified Somatic Intimacy Coach</li>
                <li>Trauma-Trained Coaching (training completed)</li>
                <li>Kink-Aware Professionals (KAP) Training</li>
                <li>BDSM Education & Communication Specialist</li>
                <li>Consent Culture Facilitator</li>
              </ul>
            </div>
            <div className="credential-item">
              <h4>Experience</h4>
              <ul>
                <li>8+ years coaching individuals and couples</li>
                <li>Specialization in conscious kink & power dynamics</li>
                <li>Workshop facilitator for intimacy & embodiment</li>
                <li>Guest speaker on conscious sexuality podcasts</li>
              </ul>
            </div>
          </div>
          <div className="disclaimer">
            <p>
              <strong>Important:</strong> I am a coach, not a therapist. If you're currently experiencing untreated PTSD, active suicidal ideation, or severe mental health crises, I'll happily refer you to appropriate trauma therapy resources.
            </p>
          </div>
        </div>
      </section>

      {/* Who I Work With */}
      <section className="about-who">
        <div className="container content-container">
          <h2>Who I Work With</h2>
          <p className="who-intro">
            I work with individuals and couples who are:
          </p>
          <div className="who-grid">
            <div className="who-item">
              <h4>Curious Explorers</h4>
              <p>You're new to kink or conscious sexuality and want guidance that's grounded, safe, and free of judgment.</p>
            </div>
            <div className="who-item">
              <h4>Seasoned Practitioners</h4>
              <p>You've explored kink before but want to deepen your practice, heal old patterns, or integrate new dimensions of power and pleasure.</p>
            </div>
            <div className="who-item">
              <h4>Trauma Survivors</h4>
              <p>You're reclaiming your relationship with your body, desire, and intimacy after trauma. You need a container that honors your pace.</p>
            </div>
            <div className="who-item">
              <h4>Sovereignty Seekers</h4>
              <p>You're done with self-sacrifice, people-pleasing, and shrinking. You're ready to embody your full power in intimacy and life.</p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="about-cta">
        <div className="container content-container centered">
          <h2>Ready to Work Together?</h2>
          <p>
            A low-pressure space to slow down, ask questions, and feel into what's next.
          </p>
          <Button href="/consult" variant="primary">
            Book a Curiosity Call
          </Button>
        </div>
      </section>

      <style jsx>{`
        /* Hero */
        .about-hero {
          background: linear-gradient(135deg, var(--primary-burgundy) 0%, var(--primary-wine) 100%);
          color: var(--neutral-soft-white);
          padding: 5rem 1.5rem;
        }

        .about-hero-layout {
          display: grid;
          grid-template-columns: 1fr;
          gap: 3rem;
          align-items: center;
          max-width: 1200px;
          margin: 0 auto;
        }

        @media (min-width: 768px) {
          .about-hero-layout {
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
          }
        }

        .about-hero-content {
          text-align: center;
        }

        @media (min-width: 768px) {
          .about-hero-content {
            text-align: left;
          }
        }

        .about-hero-content h1 {
          color: var(--neutral-soft-white);
          font-size: clamp(2.5rem, 5vw, 4rem);
          margin-bottom: 1rem;
        }

        .tagline {
          font-size: clamp(1.1rem, 2vw, 1.4rem);
          color: var(--neutral-cream);
          font-style: italic;
          line-height: 1.6;
        }

        .about-hero-image {
          display: flex;
          justify-content: center;
        }

        :global(.hero-professional-photo) {
          border-radius: 1rem;
          box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
          object-fit: cover;
          width: 100%;
          height: auto;
          max-width: 500px;
        }

        /* Story */
        .about-story {
          background: var(--neutral-soft-white);
        }

        .story-layout {
          display: grid;
          grid-template-columns: 1fr;
          gap: 3rem;
          align-items: start;
          margin-bottom: 4rem;
        }

        @media (min-width: 768px) {
          .story-layout {
            grid-template-columns: 1.2fr 1fr;
            gap: 4rem;
          }
        }

        .story-content h2 {
          margin-bottom: 2rem;
        }

        .story-content p {
          font-size: 1.1rem;
          line-height: 1.8;
          margin-bottom: 1.5rem;
          color: var(--neutral-charcoal);
        }

        .story-featured-image {
          display: flex;
          justify-content: center;
          position: sticky;
          top: 100px;
        }

        @media (max-width: 767px) {
          .story-featured-image {
            position: relative;
            top: 0;
          }
        }

        :global(.featured-photo) {
          border-radius: 1rem;
          box-shadow: 0 20px 50px rgba(139, 58, 71, 0.25);
          object-fit: cover;
          width: 100%;
          height: auto;
          max-width: 450px;
        }

        .story-images {
          display: grid;
          grid-template-columns: 1fr;
          gap: 2rem;
          margin-top: 3rem;
        }

        @media (min-width: 768px) {
          .story-images {
            grid-template-columns: repeat(2, 1fr);
          }
        }

        .story-image-primary,
        .story-image-secondary {
          border-radius: 1rem;
          overflow: hidden;
          box-shadow: 0 15px 40px rgba(139, 58, 71, 0.2);
        }

        :global(.about-photo) {
          width: 100%;
          height: auto;
          object-fit: cover;
          transition: transform 0.3s ease;
        }

        :global(.about-photo:hover) {
          transform: scale(1.02);
        }

        /* Philosophy */
        .about-philosophy {
          background: var(--neutral-cream);
        }

        .about-philosophy h2 {
          text-align: center;
          margin-bottom: 1.5rem;
        }

        .philosophy-intro {
          text-align: center;
          font-size: 1.15rem;
          color: var(--neutral-warm-gray);
          margin-bottom: 3rem;
        }

        .philosophy-grid {
          display: grid;
          grid-template-columns: 1fr;
          gap: 2rem;
        }

        @media (min-width: 768px) {
          .philosophy-grid {
            grid-template-columns: repeat(2, 1fr);
          }
        }

        .philosophy-item {
          padding: 2rem;
          background: var(--neutral-soft-white);
          border-radius: 1rem;
          border-left: 4px solid var(--accent-terracotta);
        }

        .philosophy-item h3 {
          color: var(--primary-burgundy);
          font-size: 1.4rem;
          margin-bottom: 1rem;
        }

        .philosophy-item p {
          color: var(--neutral-charcoal);
          line-height: 1.7;
        }

        /* Credentials */
        .about-credentials {
          background: var(--neutral-soft-white);
        }

        .about-credentials h2 {
          text-align: center;
          margin-bottom: 3rem;
        }

        .credentials-content {
          display: grid;
          grid-template-columns: 1fr;
          gap: 2rem;
          margin-bottom: 3rem;
        }

        @media (min-width: 768px) {
          .credentials-content {
            grid-template-columns: repeat(2, 1fr);
          }
        }

        .credential-item h4 {
          color: var(--primary-burgundy);
          font-size: 1.3rem;
          margin-bottom: 1rem;
        }

        .credential-item ul {
          list-style: none;
          padding-left: 0;
        }

        .credential-item li {
          padding: 0.5rem 0;
          padding-left: 1.5rem;
          position: relative;
          color: var(--neutral-charcoal);
        }

        .credential-item li::before {
          content: '•';
          position: absolute;
          left: 0;
          color: var(--accent-terracotta);
          font-size: 1.5rem;
          line-height: 1;
        }

        .disclaimer {
          background: var(--neutral-cream);
          padding: 2rem;
          border-radius: 0.5rem;
          border-left: 4px solid var(--accent-gold);
        }

        .disclaimer p {
          margin: 0;
          color: var(--neutral-charcoal);
          line-height: 1.6;
        }

        .disclaimer strong {
          color: var(--primary-burgundy);
        }

        /* Who I Work With */
        .about-who {
          background: var(--neutral-cream);
        }

        .about-who h2 {
          text-align: center;
          margin-bottom: 1.5rem;
        }

        .who-intro {
          text-align: center;
          font-size: 1.15rem;
          color: var(--neutral-warm-gray);
          margin-bottom: 3rem;
        }

        .who-grid {
          display: grid;
          grid-template-columns: 1fr;
          gap: 2rem;
        }

        @media (min-width: 768px) {
          .who-grid {
            grid-template-columns: repeat(2, 1fr);
          }
        }

        .who-item {
          padding: 2rem;
          background: var(--neutral-soft-white);
          border-radius: 1rem;
          transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .who-item:hover {
          transform: translateY(-5px);
          box-shadow: 0 10px 30px rgba(139, 58, 71, 0.15);
        }

        .who-item h4 {
          color: var(--primary-burgundy);
          font-size: 1.25rem;
          margin-bottom: 0.75rem;
        }

        .who-item p {
          color: var(--neutral-charcoal);
          line-height: 1.7;
        }

        /* CTA */
        .about-cta {
          background: var(--neutral-soft-white);
        }

        .centered {
          text-align: center;
        }

        .about-cta h2 {
          margin-bottom: 1rem;
        }

        .about-cta p {
          font-size: 1.15rem;
          color: var(--neutral-warm-gray);
          margin-bottom: 2rem;
        }
      `}</style>
    </>
  );
}
