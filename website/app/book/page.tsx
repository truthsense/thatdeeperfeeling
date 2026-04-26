'use client';

import { useState } from 'react';

export default function BookSessionPage() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const res = await fetch('/api/book', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email }),
      });

      const data = await res.json();

      if (!res.ok) {
        setError(data.error || 'Something went wrong. Please try again.');
        setLoading(false);
        return;
      }

      if (data.url) {
        window.location.href = data.url;
      }
    } catch {
      setError('Something went wrong. Please try again.');
      setLoading(false);
    }
  }

  return (
    <>
      <section className="book-hero">
        <div className="container content-container">
          <h1>Book Your Session</h1>
          <p className="hero-subtitle">
            A 3-hour Sacred Pause container with Kimberly.
          </p>
        </div>
      </section>

      <section className="book-form-section">
        <div className="container content-container">
          <div className="book-intro">
            <p>
              This is your space to slow down, reconnect, and reclaim.
              A 3-hour embodied coaching session designed to meet you
              exactly where you are.
            </p>
            <div className="session-details">
              <p><strong>Investment:</strong> $500</p>
              <p><strong>Format:</strong> Zoom or mutually agreed platform</p>
              <p><strong>Includes:</strong> One week of post-session text-based integration support</p>
            </div>
          </div>

          <form onSubmit={handleSubmit} className="book-form">
            <div className="form-group">
              <label htmlFor="name">Full Name</label>
              <input
                type="text"
                id="name"
                value={name}
                onChange={(e) => setName(e.target.value)}
                required
                placeholder="Your full name"
              />
            </div>

            <div className="form-group">
              <label htmlFor="email">Email Address</label>
              <input
                type="email"
                id="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                placeholder="you@example.com"
              />
            </div>

            {error && <p className="error-message">{error}</p>}

            <button type="submit" className="book-submit" disabled={loading}>
              {loading ? 'Redirecting to payment...' : 'Continue to Payment — $500'}
            </button>
          </form>

          <p className="book-note">
            After payment, you&rsquo;ll receive a participant agreement to sign.
            Once signed, you&rsquo;ll get a link to schedule your session time.
          </p>
        </div>
      </section>

      <style jsx>{`
        .book-hero {
          background: linear-gradient(135deg, var(--primary-burgundy) 0%, var(--primary-wine) 100%);
          color: var(--neutral-soft-white);
          padding: 5rem 1.5rem 4rem;
          text-align: center;
        }

        .book-hero h1 {
          color: var(--neutral-soft-white);
          font-size: clamp(2rem, 4vw, 3rem);
          margin-bottom: 0.5rem;
        }

        .hero-subtitle {
          font-size: 1.15rem;
          color: var(--neutral-cream);
          font-style: italic;
        }

        .book-form-section {
          background: var(--neutral-soft-white);
          padding: 4rem 0;
        }

        .book-intro {
          max-width: 550px;
          margin: 0 auto 3rem;
          text-align: center;
        }

        .book-intro > p {
          font-size: 1.15rem;
          line-height: 1.8;
          color: var(--neutral-charcoal);
          margin-bottom: 1.5rem;
        }

        .session-details {
          background: var(--neutral-cream);
          padding: 1.5rem 2rem;
          border-radius: 0.75rem;
          border-left: 3px solid var(--accent-terracotta);
        }

        .session-details p {
          font-size: 1.05rem;
          color: var(--neutral-charcoal);
          margin: 0.5rem 0;
        }

        .book-form {
          max-width: 450px;
          margin: 0 auto;
        }

        .form-group {
          margin-bottom: 1.5rem;
        }

        .form-group label {
          display: block;
          font-weight: 600;
          margin-bottom: 0.5rem;
          color: var(--neutral-charcoal);
          font-size: 0.95rem;
        }

        .form-group input {
          width: 100%;
          padding: 0.85rem 1rem;
          border: 1px solid var(--secondary-taupe);
          border-radius: 0.5rem;
          font-size: 1rem;
          color: var(--neutral-charcoal);
          background: white;
          transition: border-color 0.2s;
        }

        .form-group input:focus {
          outline: none;
          border-color: var(--primary-burgundy);
          box-shadow: 0 0 0 3px rgba(139, 58, 71, 0.1);
        }

        .error-message {
          color: #c0392b;
          font-size: 0.95rem;
          margin-bottom: 1rem;
          text-align: center;
        }

        .book-submit {
          width: 100%;
          padding: 1rem;
          background: var(--primary-burgundy);
          color: var(--neutral-soft-white);
          border: none;
          border-radius: 0.5rem;
          font-size: 1.1rem;
          font-weight: 600;
          font-family: var(--font-heading);
          cursor: pointer;
          transition: background-color 0.2s, transform 0.1s;
        }

        .book-submit:hover:not(:disabled) {
          background: var(--primary-wine);
          transform: translateY(-1px);
        }

        .book-submit:disabled {
          opacity: 0.7;
          cursor: not-allowed;
        }

        .book-note {
          max-width: 450px;
          margin: 2rem auto 0;
          text-align: center;
          font-size: 0.9rem;
          color: var(--neutral-warm-gray);
          font-style: italic;
          line-height: 1.7;
        }
      `}</style>
    </>
  );
}
