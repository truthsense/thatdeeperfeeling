'use client';

export default function TermsOfServicePage() {
  return (
    <>
      <section className="policy-hero">
        <div className="container content-container">
          <h1>Terms &amp; Conditions</h1>
          <p className="hero-subtitle">
            These Terms and Conditions govern your use of the website thatdeeperfeeling.com
            and any services, programs, retreats, coaching containers, sessions, or digital
            offerings provided by Kimberly Bryant, Founder of That Deeper Feeling.
          </p>
          <p className="effective-date">Effective Date: February 17, 2026</p>
        </div>
      </section>

      <section className="policy-content">
        <div className="container content-container">
          <div className="policy-section">
            <p>
              By accessing this website or purchasing any service, you agree to the following terms.
            </p>
          </div>

          <div className="policy-section">
            <h2>Scope of Practice</h2>
            <p>Kimberly Bryant is an intimacy and embodiment coach.</p>
            <p>
              Her work may overlap with themes commonly explored in therapy; however, she is not a
              licensed therapist, psychologist, psychoanalyst, counselor, medical provider, or mental
              health professional.
            </p>
            <p>
              All services provided are educational, experiential, and coaching-based in nature.
            </p>
            <div className="important-notice">
              <p>
                Nothing on this website or within any offering constitutes medical, psychological,
                or psychiatric advice, diagnosis, or treatment.
              </p>
              <p>
                If you are experiencing a mental health crisis, you are encouraged to seek support
                from a licensed provider or emergency services.
              </p>
            </div>
          </div>

          <div className="policy-section">
            <h2>Personal Responsibility</h2>
            <p>
              By participating in any offering, you acknowledge that you are voluntarily engaging
              in personal development work and accept full responsibility for your emotional,
              physical, psychological, and spiritual well-being.
            </p>
            <p>
              You agree that you are responsible for your own decisions, actions, and results.
            </p>
          </div>

          <div className="policy-section">
            <h2>Assumption of Risk</h2>
            <p>
              Participation in embodiment practices, movement exercises, breathwork, group discussion,
              and retreat experiences involves inherent emotional and physical risk.
            </p>
            <p>You voluntarily assume all risks associated with participation.</p>
          </div>

          <div className="policy-section">
            <h2>Payment Terms</h2>
            <ul>
              <li>All payments are due as stated at the time of purchase.</li>
              <li>Deposits are non-refundable unless otherwise stated in writing.</li>
              <li>Payment plans must be completed according to agreed schedule. Failure to complete payments may result in forfeiture of participation.</li>
            </ul>
          </div>

          <div className="policy-section">
            <h2>Refund Policy</h2>
            <p>
              Due to the intimate and curated nature of retreats and coaching containers, all sales
              are final.
            </p>
            <p>No refunds will be issued.</p>
            <p>
              Retreat tickets may be transferred to another eligible participant with prior written
              approval.
            </p>
          </div>

          <div className="policy-section">
            <h2>Intellectual Property</h2>
            <p>
              All content, teachings, frameworks, written materials, recordings, and intellectual
              property shared through That Deeper Feeling remain the sole property of Kimberly Bryant.
            </p>
            <p>Materials may not be copied, distributed, reproduced, or shared without written permission.</p>
          </div>

          <div className="policy-section">
            <h2>Limitation of Liability</h2>
            <p>
              To the fullest extent permitted under New York law, Kimberly Bryant and That Deeper
              Feeling shall not be liable for any direct, indirect, incidental, consequential, or
              special damages arising from participation in any offering.
            </p>
          </div>

          <div className="policy-section">
            <h2>Confidentiality</h2>
            <p>
              Group programs and retreats encourage confidentiality among participants; however,
              confidentiality in group settings cannot be guaranteed.
            </p>
            <p>
              Participants are responsible for maintaining discretion regarding what is shared within
              the container.
            </p>
          </div>

          <div className="policy-section">
            <h2>Governing Law</h2>
            <p>
              These Terms shall be governed by and construed in accordance with the laws of the
              State of New York.
            </p>
            <p>
              Any disputes arising out of these Terms shall be resolved within the State of New York.
            </p>
          </div>

          <div className="policy-section">
            <h2>Contact</h2>
            <p>
              If you have questions about these terms, please reach out:
            </p>
            <p>
              <strong>Email:</strong>{' '}
              <a href="mailto:thatdeeperfeeling@gmail.com">thatdeeperfeeling@gmail.com</a>
            </p>
          </div>
        </div>
      </section>

      <style jsx>{`
        .policy-hero {
          background: linear-gradient(135deg, var(--neutral-cream) 0%, var(--secondary-warm-beige) 100%);
          padding: 5rem 1.5rem 4rem;
          text-align: center;
        }

        .policy-hero h1 {
          font-size: clamp(2.5rem, 5vw, 4rem);
          margin-bottom: 1.5rem;
        }

        .hero-subtitle {
          font-size: clamp(1.1rem, 2vw, 1.3rem);
          color: var(--neutral-warm-gray);
          line-height: 1.7;
          max-width: 700px;
          margin: 0 auto;
        }

        .effective-date {
          font-size: 0.95rem;
          color: var(--neutral-warm-gray);
          margin-top: 1.5rem;
          font-style: italic;
        }

        .policy-content {
          background: var(--neutral-soft-white);
          padding: 5rem 0;
        }

        .policy-section {
          margin-bottom: 3rem;
          padding-bottom: 2rem;
          border-bottom: 1px solid rgba(139, 58, 71, 0.08);
        }

        .policy-section:last-child {
          border-bottom: none;
          margin-bottom: 0;
          padding-bottom: 0;
        }

        .policy-section h2 {
          font-size: 1.5rem;
          color: var(--primary-burgundy);
          margin-bottom: 1.25rem;
        }

        .policy-section p {
          font-size: 1.05rem;
          line-height: 1.8;
          color: var(--neutral-charcoal);
          margin-bottom: 1rem;
        }

        .policy-section ul {
          list-style: none;
          padding: 0;
          margin: 1rem 0;
        }

        .policy-section ul li {
          position: relative;
          padding-left: 1.5rem;
          margin-bottom: 0.75rem;
          font-size: 1.05rem;
          line-height: 1.7;
          color: var(--neutral-charcoal);
        }

        .policy-section ul li::before {
          content: '';
          position: absolute;
          left: 0;
          top: 0.6rem;
          width: 6px;
          height: 6px;
          border-radius: 50%;
          background: var(--accent-terracotta);
        }

        .policy-section a {
          color: var(--primary-burgundy);
          text-decoration: underline;
          text-underline-offset: 2px;
          transition: color 0.3s ease;
        }

        .policy-section a:hover {
          color: var(--accent-terracotta);
        }

        .important-notice {
          background: var(--neutral-cream);
          border-left: 4px solid var(--accent-terracotta);
          padding: 1.5rem 2rem;
          border-radius: 0 0.5rem 0.5rem 0;
          margin: 1.5rem 0;
        }

        .important-notice p {
          margin-bottom: 0.75rem;
        }

        .important-notice p:last-child {
          margin-bottom: 0;
        }
      `}</style>
    </>
  );
}
