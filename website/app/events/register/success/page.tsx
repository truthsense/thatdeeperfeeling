'use client';

import { useSearchParams } from 'next/navigation';
import { Suspense } from 'react';

function SuccessContent() {
  const searchParams = useSearchParams();
  const sessionId = searchParams.get('session_id');

  return (
    <>
      <section className="success-hero">
        <div className="container content-container centered">
          <div className="success-icon">&#10003;</div>
          <h1>You&rsquo;re Registered</h1>
          <p className="hero-subtitle">
            Your spot for <strong>Reclaiming the Forbidden</strong> is confirmed.
          </p>
        </div>
      </section>

      <section className="success-content">
        <div className="container content-container">
          <div className="success-card">
            <h2>What Happens Next</h2>
            <ul>
              <li>You&rsquo;ll receive a confirmation email with your payment details shortly.</li>
              <li>Kimberly will reach out personally with retreat preparation materials, lodging details, and what to expect.</li>
              <li>If you paid the $500 deposit, your remaining balance of $700 is due by <strong>April 1, 2026</strong>.</li>
              <li>Questions? Reach out at{' '}
                <a href="mailto:thatdeeperfeeling@gmail.com">thatdeeperfeeling@gmail.com</a>
              </li>
            </ul>
          </div>

          <div className="closing-message">
            <p>
              Something in you said yes to this.
            </p>
            <p>
              That&rsquo;s already the beginning.
            </p>
          </div>

          <div className="success-actions">
            <a href="/events" className="btn btn-secondary">
              Back to Event Details
            </a>
            <a href="/" className="btn btn-primary">
              Return Home
            </a>
          </div>

          {sessionId && (
            <p className="reference-id">
              Reference: {sessionId.substring(0, 20)}...
            </p>
          )}
        </div>
      </section>

      <style jsx>{`
        .success-hero {
          background: linear-gradient(135deg, var(--primary-burgundy) 0%, var(--primary-wine) 100%);
          color: var(--neutral-soft-white);
          padding: 5rem 1.5rem 4rem;
          text-align: center;
        }

        .centered {
          text-align: center;
        }

        .success-icon {
          width: 80px;
          height: 80px;
          border-radius: 50%;
          background: rgba(255, 255, 255, 0.15);
          display: flex;
          align-items: center;
          justify-content: center;
          font-size: 2.5rem;
          color: var(--neutral-soft-white);
          margin: 0 auto 1.5rem;
          border: 3px solid rgba(255, 255, 255, 0.3);
        }

        .success-hero h1 {
          font-size: clamp(2.5rem, 5vw, 3.5rem);
          color: var(--neutral-soft-white);
          margin-bottom: 1rem;
        }

        .hero-subtitle {
          font-size: 1.2rem;
          color: var(--neutral-cream);
          line-height: 1.7;
        }

        .success-content {
          background: var(--neutral-soft-white);
          padding: 5rem 0;
        }

        .success-card {
          max-width: 650px;
          margin: 0 auto 3rem;
          background: var(--neutral-cream);
          padding: 2.5rem;
          border-radius: 1rem;
          border-top: 4px solid var(--accent-terracotta);
        }

        .success-card h2 {
          font-size: 1.5rem;
          color: var(--primary-burgundy);
          margin-bottom: 1.5rem;
        }

        .success-card ul {
          list-style: none;
          padding: 0;
        }

        .success-card li {
          padding: 0.75rem 0;
          padding-left: 1.5rem;
          position: relative;
          color: var(--neutral-charcoal);
          line-height: 1.7;
          font-size: 1.05rem;
        }

        .success-card li::before {
          content: '';
          position: absolute;
          left: 0;
          top: 1rem;
          width: 6px;
          height: 6px;
          border-radius: 50%;
          background: var(--accent-terracotta);
        }

        .success-card a {
          color: var(--primary-burgundy);
          text-decoration: underline;
        }

        .closing-message {
          text-align: center;
          max-width: 500px;
          margin: 0 auto 3rem;
        }

        .closing-message p {
          font-size: 1.2rem;
          font-style: italic;
          color: var(--primary-wine);
          line-height: 1.7;
          margin-bottom: 0.5rem;
        }

        .success-actions {
          display: flex;
          gap: 1rem;
          justify-content: center;
          flex-wrap: wrap;
        }

        .reference-id {
          text-align: center;
          font-size: 0.8rem;
          color: var(--neutral-warm-gray);
          margin-top: 2rem;
          font-family: monospace;
        }
      `}</style>
    </>
  );
}

export default function SuccessPage() {
  return (
    <Suspense fallback={
      <section style={{ padding: '5rem', textAlign: 'center' }}>
        <p>Loading...</p>
      </section>
    }>
      <SuccessContent />
    </Suspense>
  );
}
