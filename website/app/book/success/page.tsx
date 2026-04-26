'use client';

import Button from '@/components/ui/Button';

export default function BookSuccessPage() {
  return (
    <>
      <section className="success-section">
        <div className="container content-container">
          <div className="success-content">
            <h1>Payment Received</h1>
            <p className="success-subtitle">Thank you for choosing to step into this work.</p>

            <div className="next-steps">
              <h2>What Happens Next</h2>
              <ul>
                <li>You&rsquo;ll receive a <strong>participant agreement</strong> via email shortly. Please review and sign it.</li>
                <li>Once your agreement is signed, you&rsquo;ll receive a <strong>scheduling link</strong> to book your session time.</li>
                <li>Questions? Reach out at{' '}
                  <a href="mailto:kimberly@thatdeeperfeeling.com">kimberly@thatdeeperfeeling.com</a>
                </li>
              </ul>
            </div>

            <Button href="/" variant="secondary">
              Return Home
            </Button>
          </div>
        </div>
      </section>

      <style jsx>{`
        .success-section {
          min-height: 70vh;
          display: flex;
          align-items: center;
          background: var(--neutral-soft-white);
          padding: 5rem 0;
        }

        .success-content {
          max-width: 550px;
          margin: 0 auto;
          text-align: center;
        }

        h1 {
          font-size: clamp(2rem, 4vw, 2.75rem);
          margin-bottom: 0.75rem;
        }

        .success-subtitle {
          font-size: 1.15rem;
          color: var(--neutral-warm-gray);
          font-style: italic;
          margin-bottom: 2.5rem;
        }

        .next-steps {
          background: var(--neutral-cream);
          padding: 2rem 2.5rem;
          border-radius: 0.75rem;
          text-align: left;
          margin-bottom: 2.5rem;
          border-top: 3px solid var(--accent-terracotta);
        }

        .next-steps h2 {
          font-size: 1.35rem;
          margin-bottom: 1rem;
          text-align: center;
        }

        .next-steps ul {
          list-style: none;
          padding: 0;
        }

        .next-steps li {
          padding: 0.65rem 0;
          padding-left: 1.5rem;
          position: relative;
          font-size: 1.05rem;
          color: var(--neutral-charcoal);
          line-height: 1.6;
        }

        .next-steps li::before {
          content: '•';
          position: absolute;
          left: 0;
          color: var(--accent-terracotta);
          font-size: 1.25rem;
          line-height: 1;
        }

        .next-steps a {
          color: var(--primary-burgundy);
          text-decoration: underline;
          text-underline-offset: 2px;
        }
      `}</style>
    </>
  );
}
