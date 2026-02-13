'use client';

import { useState } from 'react';
import Button from '@/components/ui/Button';

export default function DivingDeeperPage() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [passcode, setPasscode] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (passcode.toLowerCase() === 'intimacy') {
      setIsAuthenticated(true);
      setError('');
    } else {
      setError('Incorrect passcode. Please try again.');
    }
  };

  if (!isAuthenticated) {
    return (
      <>
        <section className="passcode-section">
          <div className="container content-container">
            <div className="passcode-box">
              <h1>Diving Deeper</h1>
              <p className="passcode-intro">
                This page contains detailed information about working together and is accessible by invitation only.
              </p>
              <form onSubmit={handleSubmit} className="passcode-form">
                <label htmlFor="passcode" className="passcode-label">
                  Enter Passcode
                </label>
                <input
                  type="text"
                  id="passcode"
                  value={passcode}
                  onChange={(e) => setPasscode(e.target.value)}
                  className="passcode-input"
                  placeholder="Enter passcode..."
                  autoComplete="off"
                />
                {error && <p className="passcode-error">{error}</p>}
                <Button type="submit" variant="primary">
                  Enter
                </Button>
              </form>
            </div>
          </div>
        </section>

        <style jsx>{`
          .passcode-section {
            min-height: 80vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, var(--neutral-cream) 0%, var(--secondary-warm-beige) 100%);
            padding: 4rem 1.5rem;
          }

          .passcode-box {
            background: white;
            padding: 3rem;
            border-radius: 1rem;
            box-shadow: 0 20px 50px rgba(139, 58, 71, 0.15);
            max-width: 500px;
            width: 100%;
            text-align: center;
          }

          .passcode-box h1 {
            font-size: 2.5rem;
            color: var(--primary-burgundy);
            margin-bottom: 1rem;
          }

          .passcode-intro {
            font-size: 1.1rem;
            color: var(--neutral-warm-gray);
            line-height: 1.7;
            margin-bottom: 2rem;
          }

          .passcode-form {
            display: flex;
            flex-direction: column;
            gap: 1rem;
          }

          .passcode-label {
            font-size: 1rem;
            color: var(--neutral-charcoal);
            font-weight: 500;
            text-align: left;
          }

          .passcode-input {
            padding: 1rem 1.5rem;
            border: 2px solid var(--neutral-cream);
            border-radius: 0.5rem;
            font-family: var(--font-body);
            font-size: 1rem;
            transition: border-color 0.3s ease;
          }

          .passcode-input:focus {
            outline: none;
            border-color: var(--primary-burgundy);
          }

          .passcode-error {
            color: var(--primary-burgundy);
            font-size: 0.95rem;
            margin: 0;
          }
        `}</style>
      </>
    );
  }

  return (
    <>
      {/* Hero Section */}
      <section className="diving-hero">
        <div className="container content-container">
          <h1>Diving Deeper</h1>
          <p className="hero-subtitle">
            Detailed offerings for those ready to explore this work more fully.
          </p>
        </div>
      </section>

      {/* Containers Section */}
      <section className="containers-section">
        <div className="container content-container">

          {/* Return to Power */}
          <div className="offering-card">
            <h2>Return to Power</h2>
            <p className="offering-duration">6-Month Private Container</p>
            <p className="offering-tagline">
              Deep, sustained transformation for reclaiming sovereignty and embodying pleasure.
            </p>
            <p className="offering-description">
              For those ready to go all the way. This container holds space for profound shifts in how you relate to power, desire, intimacy, and your own body.
            </p>
            <div className="offering-details">
              <div className="detail-section">
                <h4>Ideal For You If:</h4>
                <p>Ready for sustained, deep work. Committed to transformation.</p>
              </div>
              <div className="detail-section">
                <h4>What&rsquo;s Included:</h4>
                <ul>
                  <li>Bi-weekly 90-minute sessions</li>
                  <li>Personalized practices & resources</li>
                  <li>Voxer support between sessions</li>
                  <li>Sacred ritual design</li>
                  <li>Embodiment homework & integration</li>
                </ul>
              </div>
              <p className="offering-cta">Reach out to discuss tailoring to the needs of your journey</p>
            </div>
          </div>

          {/* Edgewalker */}
          <div className="offering-card">
            <h2>Edgewalker</h2>
            <p className="offering-duration">3-Month Private Container</p>
            <p className="offering-tagline">
              Explore a specific edge—desire, kink dynamics, or pleasure reclamation.
            </p>
            <p className="offering-description">
              Perfect for exploring one focused area of your intimacy journey. Whether it&rsquo;s communication, power dynamics, or healing your relationship with pleasure after trauma.
            </p>
            <div className="offering-details">
              <div className="detail-section">
                <h4>Ideal For You If:</h4>
                <p>Have a specific goal or edge to explore. Want focused support.</p>
              </div>
              <div className="detail-section">
                <h4>What&rsquo;s Included:</h4>
                <ul>
                  <li>Weekly 60-minute sessions</li>
                  <li>Customized embodiment practices</li>
                  <li>Email support</li>
                  <li>Integration resources</li>
                  <li>Personalized reading & resources</li>
                </ul>
              </div>
              <p className="offering-cta">Reach out to discuss tailoring to the needs of your journey</p>
            </div>
          </div>

          {/* Sacred Eruption */}
          <div className="offering-card">
            <h2>Sacred Eruption</h2>
            <p className="offering-duration">Single Session Deep Dive</p>
            <p className="offering-tagline">
              A powerful, contained exploration for a specific breakthrough.
            </p>
            <p className="offering-description">
              One 2-hour intensive session for addressing a specific block, question, or moment of transformation. Ideal for returning clients or focused work.
            </p>
            <div className="offering-details">
              <div className="detail-section">
                <h4>Ideal For You If:</h4>
                <p>Have a specific question or block. Want a contained experience.</p>
              </div>
              <div className="detail-section">
                <h4>What&rsquo;s Included:</h4>
                <ul>
                  <li>2-hour intensive session</li>
                  <li>Pre-session intake & preparation</li>
                  <li>Integration guide & practices</li>
                  <li>Follow-up email support</li>
                </ul>
              </div>
              <p className="offering-cta">Reach out to discuss tailoring to the needs of your journey</p>
            </div>
          </div>

          {/* Flicker and Flame */}
          <div className="offering-card">
            <h2>Flicker and Flame</h2>
            <p className="offering-duration">Online Membership</p>
            <p className="offering-tagline">
              Community, resources, and monthly workshops for ongoing exploration.
            </p>
            <p className="offering-description">
              A sacred space for continuous learning, connection, and embodiment. Monthly workshops, resource library, and a private community of conscious explorers.
            </p>
            <div className="offering-details">
              <div className="detail-section">
                <h4>Ideal For You If:</h4>
                <p>Want ongoing support. Value community and continuous learning.</p>
              </div>
              <div className="detail-section">
                <h4>What&rsquo;s Included:</h4>
                <ul>
                  <li>Monthly live workshops</li>
                  <li>Private community forum</li>
                  <li>Resource library & practices</li>
                  <li>Guest expert sessions</li>
                  <li>Cancel anytime</li>
                </ul>
              </div>
              <p className="offering-cta">Reach out to discuss tailoring to the needs of your journey</p>
            </div>
          </div>

          {/* Into the Embers */}
          <div className="offering-card">
            <h2>Into the Embers</h2>
            <p className="offering-duration">In-Person Gatherings</p>
            <p className="offering-tagline">
              Sacred group containers for embodied intimacy and conscious kink exploration.
            </p>
            <p className="offering-description">
              Multi-day immersive experiences. Deep group work, somatic practices, and facilitated exploration in a trauma-informed, consent-centered container.
            </p>
            <div className="offering-details">
              <div className="detail-section">
                <h4>Ideal For You If:</h4>
                <p>Want in-person embodied work. Value group energy and connection.</p>
              </div>
              <div className="detail-section">
                <h4>What&rsquo;s Included:</h4>
                <ul>
                  <li>2-3 day immersive retreats</li>
                  <li>Somatic practices & rituals</li>
                  <li>Group facilitation & witnessing</li>
                  <li>Meals & accommodations included</li>
                  <li>Limited to 8-12 participants</li>
                </ul>
              </div>
              <p className="offering-cta">Reach out to discuss tailoring to the needs of your journey</p>
            </div>
          </div>

        </div>
      </section>

      {/* CTA Section */}
      <section className="diving-cta">
        <div className="container content-container centered">
          <h2>Ready to Explore?</h2>
          <p>
            If something here calls to you, let&rsquo;s talk. Book a Curiosity Call to explore which container might be right for you.
          </p>
          <Button href="/consult" variant="primary">
            Book a Curiosity Call
          </Button>
          <p className="cta-subtext">
            A low-pressure space to slow down, ask questions, and feel into what&rsquo;s next.
          </p>
        </div>
      </section>

      <style jsx>{`
        /* Hero */
        .diving-hero {
          background: linear-gradient(135deg, var(--primary-burgundy) 0%, var(--primary-wine) 100%);
          color: var(--neutral-soft-white);
          padding: 5rem 1.5rem 4rem;
          text-align: center;
        }

        .diving-hero h1 {
          color: var(--neutral-soft-white);
          font-size: clamp(2.5rem, 5vw, 4rem);
          margin-bottom: 1rem;
        }

        .hero-subtitle {
          font-size: clamp(1.1rem, 2vw, 1.4rem);
          color: var(--neutral-cream);
          font-style: italic;
        }

        /* Containers Section */
        .containers-section {
          background: var(--neutral-soft-white);
          padding: 5rem 0;
        }

        .offering-card {
          background: white;
          padding: 3rem;
          border-radius: 1rem;
          margin-bottom: 2.5rem;
          border-top: 4px solid var(--accent-terracotta);
          box-shadow: 0 10px 30px rgba(139, 58, 71, 0.1);
        }

        .offering-card:last-child {
          margin-bottom: 0;
        }

        .offering-card h2 {
          font-size: 2rem;
          color: var(--primary-burgundy);
          margin-bottom: 0.25rem;
        }

        .offering-duration {
          font-size: 1rem;
          color: var(--accent-terracotta);
          font-weight: 600;
          margin-bottom: 1.5rem;
        }

        .offering-tagline {
          font-size: 1.2rem;
          color: var(--neutral-charcoal);
          font-style: italic;
          margin-bottom: 1rem;
          line-height: 1.6;
        }

        .offering-description {
          font-size: 1.05rem;
          color: var(--neutral-charcoal);
          line-height: 1.7;
          margin-bottom: 2rem;
        }

        .offering-details {
          background: var(--neutral-cream);
          padding: 2rem;
          border-radius: 0.75rem;
        }

        .detail-section {
          margin-bottom: 1.5rem;
        }

        .detail-section:last-of-type {
          margin-bottom: 1.5rem;
        }

        .detail-section h4 {
          font-size: 1.1rem;
          color: var(--primary-burgundy);
          margin-bottom: 0.5rem;
        }

        .detail-section p {
          font-size: 1rem;
          color: var(--neutral-charcoal);
          line-height: 1.6;
          margin: 0;
        }

        .detail-section ul {
          list-style: none;
          padding: 0;
          margin: 0;
        }

        .detail-section li {
          padding: 0.4rem 0;
          padding-left: 1.5rem;
          position: relative;
          color: var(--neutral-charcoal);
          font-size: 1rem;
        }

        .detail-section li::before {
          content: '✓';
          position: absolute;
          left: 0;
          color: var(--accent-terracotta);
          font-weight: 700;
        }

        .offering-cta {
          font-size: 1.05rem;
          font-weight: 500;
          color: var(--primary-burgundy);
          margin: 0;
          font-style: italic;
          line-height: 1.6;
        }

        /* CTA */
        .diving-cta {
          background: var(--neutral-cream);
          padding: 5rem 0;
        }

        .centered {
          text-align: center;
        }

        .diving-cta h2 {
          font-size: clamp(2rem, 4vw, 3rem);
          color: var(--primary-burgundy);
          margin-bottom: 1rem;
        }

        .diving-cta p {
          font-size: 1.15rem;
          color: var(--neutral-charcoal);
          margin-bottom: 2rem;
          max-width: 700px;
          margin-left: auto;
          margin-right: auto;
          line-height: 1.7;
        }

        .cta-subtext {
          font-size: 0.95rem;
          color: var(--neutral-warm-gray);
          font-style: italic;
          margin-top: 0.75rem;
        }

        @media (max-width: 767px) {
          .offering-card {
            padding: 2rem 1.5rem;
          }

          .offering-details {
            padding: 1.5rem;
          }
        }
      `}</style>
    </>
  );
}
