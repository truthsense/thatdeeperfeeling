'use client';

import { useState } from 'react';

export default function ConsultPage() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const res = await fetch('/api/curiosity-call', {
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
      {/* Hero Section */}
      <section className="consult-hero">
        <div className="container content-container">
          <h1>Book Your Curiosity Call</h1>
          <p className="hero-subtitle">
            A grounded, spacious conversation&mdash;not a sales call.
          </p>
        </div>
      </section>

      {/* Consultation Details */}
      <section className="consult-details">
        <div className="container content-container">
          <div className="details-content">
            <p className="intro-text">
              The Curiosity Call is a place for us to explore what you&rsquo;re navigating, what you&rsquo;re longing for, and whether my work is the right support for you.
            </p>

            <div className="explore-section">
              <h2>During the Call, We&rsquo;ll Explore:</h2>
              <ul className="explore-list">
                <li>What&rsquo;s bringing you here</li>
                <li>What kind of support you&rsquo;re seeking</li>
                <li>Which container may best serve you</li>
                <li>Boundaries, expectations, and next steps</li>
              </ul>
            </div>

            <div className="outcome-text">
              <p>
                If we feel aligned, we&rsquo;ll discuss options for working together.
              </p>
              <p>
                If not, you&rsquo;ll still leave with clarity.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Payment Section */}
      <section className="consult-booking">
        <div className="container content-container">
          <div className="booking-card">
            <h2>Step Into That Deeper Feeling</h2>

            <div className="investment-box">
              <p className="price">$125</p>
              <p className="investment-note">
                60-minute conversation with Kimberly
              </p>
              <p className="investment-applied">
                Applied toward your chosen container.
              </p>
            </div>

            <form onSubmit={handleSubmit} className="booking-form">
              <div className="form-group">
                <label htmlFor="name">Name</label>
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
                <label htmlFor="email">Email</label>
                <input
                  type="email"
                  id="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                  placeholder="Your email address"
                />
              </div>

              {error && <p className="error-message">{error}</p>}

              <button type="submit" className="btn btn-primary submit-btn" disabled={loading}>
                {loading ? 'Processing...' : 'Book Your Curiosity Call — $125'}
              </button>
            </form>

            <p className="secure-note">
              Secure payment via Stripe. After payment, you&rsquo;ll receive a scheduling link by email.
            </p>
          </div>
        </div>
      </section>

      {/* What Happens Next */}
      <section className="consult-next-steps">
        <div className="container content-container">
          <h2>What Happens After You Book</h2>
          <div className="steps-grid">
            <div className="step">
              <div className="step-number">1</div>
              <h3>Payment</h3>
              <p>
                Complete your $125 payment securely through Stripe.
              </p>
            </div>
            <div className="step">
              <div className="step-number">2</div>
              <h3>Schedule</h3>
              <p>
                You&rsquo;ll receive an email with a link to choose a time that works for you.
              </p>
            </div>
            <div className="step">
              <div className="step-number">3</div>
              <h3>Our Conversation</h3>
              <p>
                We&rsquo;ll meet for 60 minutes to explore your needs, answer questions, and see if we&rsquo;re a good fit.
              </p>
            </div>
          </div>
        </div>
      </section>

      <style jsx>{`
        /* Hero */
        .consult-hero {
          background: linear-gradient(135deg, var(--primary-burgundy) 0%, var(--primary-wine) 100%);
          color: var(--neutral-soft-white);
          padding: 5rem 1.5rem 4rem;
          text-align: center;
        }

        .consult-hero h1 {
          color: var(--neutral-soft-white);
          font-size: clamp(2.5rem, 5vw, 4rem);
          margin-bottom: 1rem;
        }

        .hero-subtitle {
          font-size: clamp(1.1rem, 2vw, 1.4rem);
          color: var(--neutral-cream);
          font-style: italic;
        }

        /* Details */
        .consult-details {
          background: var(--neutral-soft-white);
          padding: 5rem 0;
        }

        .details-content {
          max-width: 700px;
          margin: 0 auto;
        }

        .intro-text {
          font-size: 1.2rem;
          line-height: 1.8;
          color: var(--neutral-charcoal);
          margin-bottom: 3rem;
        }

        .explore-section {
          margin-bottom: 3rem;
        }

        .explore-section h2 {
          font-size: 1.75rem;
          color: var(--primary-burgundy);
          margin-bottom: 1.5rem;
        }

        .explore-list {
          list-style: none;
          padding: 0;
        }

        .explore-list li {
          padding: 0.75rem 0;
          padding-left: 2rem;
          position: relative;
          font-size: 1.1rem;
          color: var(--neutral-charcoal);
          line-height: 1.6;
        }

        .explore-list li::before {
          content: '';
          position: absolute;
          left: 0;
          color: var(--accent-terracotta);
          font-size: 1.5rem;
          line-height: 1;
        }

        .outcome-text {
          font-size: 1.1rem;
          line-height: 1.8;
          color: var(--neutral-charcoal);
        }

        .outcome-text p {
          margin-bottom: 1rem;
        }

        /* Booking Section */
        .consult-booking {
          background: var(--neutral-cream);
          padding: 5rem 0;
        }

        .booking-card {
          max-width: 550px;
          margin: 0 auto;
          background: white;
          border-radius: 1rem;
          padding: 3rem;
          box-shadow: 0 10px 40px rgba(139, 58, 71, 0.12);
          text-align: center;
        }

        .booking-card h2 {
          font-size: clamp(1.75rem, 3vw, 2.25rem);
          color: var(--primary-wine);
          margin-bottom: 2rem;
        }

        .investment-box {
          margin-bottom: 2.5rem;
        }

        .price {
          font-size: 3rem;
          font-weight: 700;
          color: var(--primary-burgundy);
          margin-bottom: 0.25rem;
          font-family: var(--font-heading);
        }

        .investment-note {
          font-size: 1.05rem;
          color: var(--neutral-warm-gray);
          margin-bottom: 0.25rem;
        }

        .investment-applied {
          font-size: 0.95rem;
          color: var(--neutral-warm-gray);
          font-style: italic;
        }

        /* Form */
        .booking-form {
          text-align: left;
        }

        .form-group {
          margin-bottom: 1.5rem;
        }

        .form-group label {
          display: block;
          font-size: 0.95rem;
          font-weight: 500;
          color: var(--neutral-charcoal);
          margin-bottom: 0.5rem;
        }

        .form-group input {
          width: 100%;
          padding: 0.85rem 1rem;
          border: 1.5px solid var(--secondary-taupe);
          border-radius: 0.5rem;
          font-size: 1rem;
          font-family: var(--font-body);
          color: var(--neutral-charcoal);
          background: var(--neutral-soft-white);
          transition: border-color 0.3s ease;
        }

        .form-group input:focus {
          outline: none;
          border-color: var(--primary-burgundy);
        }

        .form-group input::placeholder {
          color: var(--neutral-warm-gray);
        }

        .error-message {
          color: #c0392b;
          font-size: 0.95rem;
          margin-bottom: 1rem;
          text-align: center;
        }

        .submit-btn {
          width: 100%;
          padding: 1rem;
          font-size: 1.1rem;
          cursor: pointer;
          border: none;
          margin-top: 0.5rem;
        }

        .submit-btn:disabled {
          opacity: 0.7;
          cursor: not-allowed;
        }

        .secure-note {
          font-size: 0.85rem;
          color: var(--neutral-warm-gray);
          margin-top: 1.5rem;
          font-style: italic;
        }

        /* Next Steps */
        .consult-next-steps {
          background: var(--neutral-soft-white);
          padding: 5rem 0;
        }

        .consult-next-steps h2 {
          text-align: center;
          font-size: clamp(2rem, 4vw, 3rem);
          margin-bottom: 3rem;
        }

        .steps-grid {
          display: grid;
          grid-template-columns: 1fr;
          gap: 2rem;
          max-width: 900px;
          margin: 0 auto;
        }

        @media (min-width: 768px) {
          .steps-grid {
            grid-template-columns: repeat(3, 1fr);
          }
        }

        .step {
          text-align: center;
          padding: 2rem;
          background: var(--neutral-cream);
          border-radius: 1rem;
          transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .step:hover {
          transform: translateY(-5px);
          box-shadow: 0 10px 30px rgba(139, 58, 71, 0.15);
        }

        .step-number {
          width: 60px;
          height: 60px;
          border-radius: 50%;
          background: var(--accent-terracotta);
          color: var(--neutral-soft-white);
          font-size: 1.75rem;
          font-weight: 700;
          display: flex;
          align-items: center;
          justify-content: center;
          margin: 0 auto 1.5rem;
          font-family: var(--font-heading);
        }

        .step h3 {
          font-size: 1.4rem;
          color: var(--primary-burgundy);
          margin-bottom: 1rem;
        }

        .step p {
          font-size: 1rem;
          color: var(--neutral-charcoal);
          line-height: 1.6;
        }
      `}</style>
    </>
  );
}
