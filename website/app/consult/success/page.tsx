'use client';

export default function ConsultSuccessPage() {
  return (
    <>
      <section className="success-hero">
        <div className="container content-container">
          <h1>You&rsquo;re In.</h1>
          <p className="hero-subtitle">
            Your Curiosity Call has been booked.
          </p>
        </div>
      </section>

      <section className="success-content">
        <div className="container content-container">
          <div className="success-card">
            <h2>Check Your Email</h2>
            <p>
              A confirmation email has been sent with a link to schedule your 60-minute Curiosity Call at a time that works for you.
            </p>
            <div className="next-steps">
              <div className="step-item">
                <span className="step-num">1</span>
                <p>Open the email from <strong>That Deeper Feeling</strong></p>
              </div>
              <div className="step-item">
                <span className="step-num">2</span>
                <p>Click the scheduling link to choose your time</p>
              </div>
              <div className="step-item">
                <span className="step-num">3</span>
                <p>Show up as you are. There is nothing to prepare.</p>
              </div>
            </div>
            <div className="reminder-box">
              <p>
                Your $125 investment is applied toward any container you choose to step into.
              </p>
            </div>
            <p className="closing">
              Questions? Reach out at{' '}
              <a href="mailto:kimberly@thatdeeperfeeling.com">kimberly@thatdeeperfeeling.com</a>
            </p>
          </div>
        </div>
      </section>

      <style jsx>{`
        .success-hero {
          background: linear-gradient(135deg, var(--primary-burgundy) 0%, var(--primary-wine) 100%);
          color: var(--neutral-soft-white);
          padding: 5rem 1.5rem 4rem;
          text-align: center;
        }

        .success-hero h1 {
          color: var(--neutral-soft-white);
          font-size: clamp(2.5rem, 5vw, 4rem);
          margin-bottom: 0.75rem;
        }

        .hero-subtitle {
          font-size: clamp(1.1rem, 2vw, 1.4rem);
          color: var(--neutral-cream);
          font-style: italic;
        }

        .success-content {
          background: var(--neutral-soft-white);
          padding: 5rem 0;
        }

        .success-card {
          max-width: 650px;
          margin: 0 auto;
          text-align: center;
        }

        .success-card h2 {
          font-size: 2rem;
          color: var(--primary-burgundy);
          margin-bottom: 1.5rem;
        }

        .success-card > p {
          font-size: 1.1rem;
          line-height: 1.8;
          color: var(--neutral-charcoal);
          margin-bottom: 2.5rem;
        }

        .next-steps {
          display: flex;
          flex-direction: column;
          gap: 1.25rem;
          margin-bottom: 2.5rem;
          text-align: left;
        }

        .step-item {
          display: flex;
          align-items: flex-start;
          gap: 1rem;
          padding: 1rem 1.5rem;
          background: var(--neutral-cream);
          border-radius: 0.75rem;
        }

        .step-num {
          flex-shrink: 0;
          width: 32px;
          height: 32px;
          border-radius: 50%;
          background: var(--accent-terracotta);
          color: var(--neutral-soft-white);
          font-size: 0.95rem;
          font-weight: 700;
          display: flex;
          align-items: center;
          justify-content: center;
          font-family: var(--font-heading);
        }

        .step-item p {
          font-size: 1.05rem;
          color: var(--neutral-charcoal);
          margin: 0;
          line-height: 1.6;
          padding-top: 0.2rem;
        }

        .reminder-box {
          background: var(--neutral-cream);
          border-left: 4px solid var(--accent-gold);
          padding: 1.25rem 1.5rem;
          border-radius: 0 0.5rem 0.5rem 0;
          margin-bottom: 2rem;
        }

        .reminder-box p {
          font-size: 1rem;
          color: var(--neutral-charcoal);
          margin: 0;
          font-style: italic;
        }

        .closing {
          font-size: 0.95rem;
          color: var(--neutral-warm-gray);
        }

        .closing a {
          color: var(--primary-burgundy);
          text-decoration: underline;
          text-underline-offset: 2px;
        }

        .closing a:hover {
          color: var(--accent-terracotta);
        }
      `}</style>
    </>
  );
}
