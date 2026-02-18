'use client';

import { useState } from 'react';

export default function EventRegisterPage() {
  const [form, setForm] = useState({
    name: '',
    email: '',
    phone: '',
    q1: '',
    q2: '',
    q3: '',
    q4: '',
    q5: '',
  });
  const [paymentOption, setPaymentOption] = useState<'deposit' | 'full'>('deposit');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const res = await fetch('/api/checkout', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          ...form,
          paymentOption,
        }),
      });

      const data = await res.json();

      if (!res.ok) {
        throw new Error(data.error || 'Something went wrong');
      }

      if (data.url) {
        window.location.href = data.url;
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Something went wrong. Please try again.');
      setLoading(false);
    }
  };

  const questions = [
    {
      name: 'q1',
      label: 'Where in your life are you still performing \u201Cgood\u201D\u2026 and what part of you is quietly asking for more?',
    },
    {
      name: 'q2',
      label: 'What part of your Eros \u2014 your life force, your play, your desire \u2014 feels ready to come back online?',
    },
    {
      name: 'q3',
      label: 'If you gave yourself full permission for one weekend\u2026 what might you discover about yourself?',
    },
    {
      name: 'q4',
      label: 'What part of you has been labeled \u201Ctoo much\u201D\u2026 that might actually be your power?',
    },
    {
      name: 'q5',
      label: 'Where have you been obedient at the expense of your own aliveness?',
    },
  ];

  return (
    <>
      {/* Hero */}
      <section className="register-hero">
        <div className="container content-container">
          <h1>Register for Reclaiming the Forbidden</h1>
          <p className="hero-tagline">May 8&ndash;10, 2026 &middot; St. George, Utah</p>
          <p className="hero-subtitle">
            A 3-day immersive retreat for women navigating life after high-demand religion,
            rigid belief systems, or identities that required self-erasure to belong.
          </p>
        </div>
      </section>

      {/* Event Details Summary */}
      <section className="register-details">
        <div className="container content-container">
          <div className="details-grid">
            <div className="detail-card">
              <h3>What&rsquo;s Included</h3>
              <ul>
                <li>3 days of guided somatic workshops</li>
                <li>Embodiment practices &amp; sacred ritual</li>
                <li>Community circle with fellow women</li>
                <li>Opening &amp; closing ceremonies</li>
                <li>Post-retreat integration resources</li>
              </ul>
            </div>
            <div className="detail-card">
              <h3>Retreat Details</h3>
              <ul>
                <li><strong>Dates:</strong> May 8&ndash;10, 2026</li>
                <li><strong>Location:</strong> Private residence, St. George, Utah</li>
                <li><strong>Group Size:</strong> Limited to 20&ndash;25 women</li>
                <li><strong>Lodging:</strong> Separate purchase (details provided after registration)</li>
              </ul>
            </div>
            <div className="detail-card">
              <h3>Investment</h3>
              <ul>
                <li><strong>Full Price:</strong> $1,200</li>
                <li><strong>Deposit:</strong> $500 non-refundable to reserve your spot</li>
                <li><strong>Balance Due:</strong> April 1, 2026</li>
                <li>All payments are non-refundable</li>
                <li>Spot transfers available with approval</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* Registration Form */}
      <section className="register-form-section">
        <div className="container content-container">
          <h2>Your Information</h2>
          <p className="form-intro">
            Complete the form below to begin your registration. After submitting, you&rsquo;ll
            be directed to our secure payment page.
          </p>

          <form onSubmit={handleSubmit} className="register-form">
            {/* Contact Info */}
            <div className="form-group">
              <label htmlFor="name">Full Name *</label>
              <input
                type="text"
                id="name"
                name="name"
                value={form.name}
                onChange={handleChange}
                required
                placeholder="Your full name"
              />
            </div>

            <div className="form-row">
              <div className="form-group">
                <label htmlFor="email">Email Address *</label>
                <input
                  type="email"
                  id="email"
                  name="email"
                  value={form.email}
                  onChange={handleChange}
                  required
                  placeholder="you@example.com"
                />
              </div>
              <div className="form-group">
                <label htmlFor="phone">Phone Number *</label>
                <input
                  type="tel"
                  id="phone"
                  name="phone"
                  value={form.phone}
                  onChange={handleChange}
                  required
                  placeholder="(555) 123-4567"
                />
              </div>
            </div>

            {/* Reflection Questions */}
            <div className="questions-section">
              <h3>A Few Reflections</h3>
              <p className="questions-intro">
                These questions are for Kimberly to understand where you are in your journey.
                There are no right answers &mdash; just your honest truth.
              </p>

              {questions.map((q) => (
                <div className="form-group" key={q.name}>
                  <label htmlFor={q.name}>{q.label}</label>
                  <textarea
                    id={q.name}
                    name={q.name}
                    value={form[q.name as keyof typeof form]}
                    onChange={handleChange}
                    rows={3}
                    placeholder="Share whatever feels true..."
                  />
                </div>
              ))}
            </div>

            {/* Payment Option */}
            <div className="payment-section">
              <h3>Choose Your Payment</h3>

              <div className="payment-options">
                <label
                  className={`payment-option ${paymentOption === 'deposit' ? 'selected' : ''}`}
                >
                  <input
                    type="radio"
                    name="paymentOption"
                    value="deposit"
                    checked={paymentOption === 'deposit'}
                    onChange={() => setPaymentOption('deposit')}
                  />
                  <div className="payment-option-content">
                    <span className="payment-option-title">$500 Deposit</span>
                    <span className="payment-option-desc">
                      Reserve your spot now. Remaining $700 due by April 1, 2026.
                    </span>
                  </div>
                </label>

                <label
                  className={`payment-option ${paymentOption === 'full' ? 'selected' : ''}`}
                >
                  <input
                    type="radio"
                    name="paymentOption"
                    value="full"
                    checked={paymentOption === 'full'}
                    onChange={() => setPaymentOption('full')}
                  />
                  <div className="payment-option-content">
                    <span className="payment-option-title">$1,200 Pay in Full</span>
                    <span className="payment-option-desc">
                      Complete your registration in one payment.
                    </span>
                  </div>
                </label>
              </div>
            </div>

            {/* Policy Agreement */}
            <div className="policy-note">
              <p>
                By registering, you agree to our{' '}
                <a href="/terms" target="_blank">Terms of Service</a>,{' '}
                <a href="/policies" target="_blank">Policies &amp; Boundaries</a>, and{' '}
                <a href="/privacy" target="_blank">Privacy Policy</a>.
                All payments are non-refundable. Spot transfers are available with prior approval
                up to 30 days before the event.
              </p>
            </div>

            {error && <p className="error-message">{error}</p>}

            <button type="submit" className="btn btn-primary submit-btn" disabled={loading}>
              {loading ? 'Processing...' : `Proceed to Payment — $${paymentOption === 'deposit' ? '500' : '1,200'}`}
            </button>
          </form>
        </div>
      </section>

      <style jsx>{`
        .register-hero {
          background: linear-gradient(135deg, var(--primary-burgundy) 0%, var(--primary-wine) 100%);
          color: var(--neutral-soft-white);
          padding: 5rem 1.5rem 4rem;
          text-align: center;
        }

        .register-hero h1 {
          font-size: clamp(2rem, 4.5vw, 3.5rem);
          color: var(--neutral-soft-white);
          margin-bottom: 1rem;
        }

        .hero-tagline {
          font-size: 1.2rem;
          color: var(--neutral-cream);
          font-weight: 500;
          margin-bottom: 1rem;
        }

        .hero-subtitle {
          font-size: 1.1rem;
          color: var(--neutral-cream);
          line-height: 1.7;
          max-width: 700px;
          margin: 0 auto;
          opacity: 0.9;
        }

        /* Details Section */
        .register-details {
          background: var(--neutral-cream);
          padding: 5rem 0;
        }

        .details-grid {
          display: grid;
          grid-template-columns: 1fr;
          gap: 2rem;
        }

        @media (min-width: 768px) {
          .details-grid {
            grid-template-columns: repeat(3, 1fr);
          }
        }

        .detail-card {
          background: var(--neutral-soft-white);
          padding: 2rem;
          border-radius: 1rem;
          border-top: 4px solid var(--accent-terracotta);
        }

        .detail-card h3 {
          color: var(--primary-burgundy);
          font-size: 1.3rem;
          margin-bottom: 1.25rem;
        }

        .detail-card ul {
          list-style: none;
          padding: 0;
        }

        .detail-card li {
          padding: 0.5rem 0;
          padding-left: 1.25rem;
          position: relative;
          color: var(--neutral-charcoal);
          line-height: 1.6;
          font-size: 0.95rem;
        }

        .detail-card li::before {
          content: '';
          position: absolute;
          left: 0;
          top: 0.75rem;
          width: 5px;
          height: 5px;
          border-radius: 50%;
          background: var(--accent-terracotta);
        }

        /* Form Section */
        .register-form-section {
          background: var(--neutral-soft-white);
          padding: 5rem 0;
        }

        .register-form-section h2 {
          text-align: center;
          margin-bottom: 1rem;
        }

        .form-intro {
          text-align: center;
          font-size: 1.1rem;
          color: var(--neutral-warm-gray);
          line-height: 1.7;
          max-width: 600px;
          margin: 0 auto 3rem;
        }

        .register-form {
          max-width: 700px;
          margin: 0 auto;
        }

        .form-group {
          margin-bottom: 1.75rem;
        }

        .form-group label {
          display: block;
          font-weight: 500;
          color: var(--neutral-charcoal);
          margin-bottom: 0.5rem;
          font-size: 0.95rem;
          line-height: 1.5;
        }

        .form-group input,
        .form-group textarea {
          width: 100%;
          padding: 0.875rem 1rem;
          border: 1px solid var(--secondary-taupe);
          border-radius: 0.5rem;
          font-family: var(--font-body);
          font-size: 1rem;
          color: var(--neutral-charcoal);
          background: white;
          transition: border-color 0.3s ease, box-shadow 0.3s ease;
          box-sizing: border-box;
        }

        .form-group input:focus,
        .form-group textarea:focus {
          outline: none;
          border-color: var(--primary-burgundy);
          box-shadow: 0 0 0 3px rgba(139, 58, 71, 0.1);
        }

        .form-group textarea {
          resize: vertical;
          min-height: 80px;
        }

        .form-row {
          display: grid;
          grid-template-columns: 1fr;
          gap: 1.75rem;
        }

        @media (min-width: 600px) {
          .form-row {
            grid-template-columns: 1fr 1fr;
          }
        }

        /* Questions */
        .questions-section {
          margin-top: 3rem;
          padding-top: 3rem;
          border-top: 1px solid rgba(139, 58, 71, 0.1);
        }

        .questions-section h3 {
          font-size: 1.4rem;
          color: var(--primary-burgundy);
          margin-bottom: 0.75rem;
        }

        .questions-intro {
          font-size: 1rem;
          color: var(--neutral-warm-gray);
          line-height: 1.6;
          margin-bottom: 2rem;
          font-style: italic;
        }

        /* Payment Options */
        .payment-section {
          margin-top: 3rem;
          padding-top: 3rem;
          border-top: 1px solid rgba(139, 58, 71, 0.1);
        }

        .payment-section h3 {
          font-size: 1.4rem;
          color: var(--primary-burgundy);
          margin-bottom: 1.5rem;
        }

        .payment-options {
          display: flex;
          flex-direction: column;
          gap: 1rem;
        }

        .payment-option {
          display: flex;
          align-items: flex-start;
          gap: 1rem;
          padding: 1.5rem;
          border: 2px solid var(--secondary-taupe);
          border-radius: 0.75rem;
          cursor: pointer;
          transition: all 0.3s ease;
          background: white;
        }

        .payment-option:hover {
          border-color: var(--primary-burgundy);
        }

        .payment-option.selected {
          border-color: var(--primary-burgundy);
          background: rgba(139, 58, 71, 0.03);
          box-shadow: 0 0 0 3px rgba(139, 58, 71, 0.1);
        }

        .payment-option input[type="radio"] {
          margin-top: 0.25rem;
          accent-color: var(--primary-burgundy);
          width: 18px;
          height: 18px;
          flex-shrink: 0;
        }

        .payment-option-content {
          display: flex;
          flex-direction: column;
          gap: 0.25rem;
        }

        .payment-option-title {
          font-weight: 600;
          font-size: 1.15rem;
          color: var(--primary-burgundy);
        }

        .payment-option-desc {
          font-size: 0.9rem;
          color: var(--neutral-warm-gray);
          line-height: 1.5;
        }

        /* Policy Note */
        .policy-note {
          margin-top: 2rem;
          padding: 1.25rem 1.5rem;
          background: var(--neutral-cream);
          border-radius: 0.5rem;
          border-left: 3px solid var(--accent-gold);
        }

        .policy-note p {
          font-size: 0.9rem;
          color: var(--neutral-warm-gray);
          line-height: 1.6;
          margin: 0;
        }

        .policy-note a {
          color: var(--primary-burgundy);
          text-decoration: underline;
          text-underline-offset: 2px;
        }

        .policy-note a:hover {
          color: var(--accent-terracotta);
        }

        /* Error */
        .error-message {
          color: #c0392b;
          font-size: 0.95rem;
          margin-top: 1rem;
          padding: 0.75rem 1rem;
          background: #fdf0ef;
          border-radius: 0.5rem;
          border: 1px solid #f5c6cb;
        }

        /* Submit */
        .submit-btn {
          display: block;
          width: 100%;
          margin-top: 2rem;
          padding: 1.125rem 2rem;
          font-size: 1.1rem;
          font-weight: 600;
          text-align: center;
        }

        .submit-btn:disabled {
          opacity: 0.7;
          cursor: not-allowed;
        }
      `}</style>
    </>
  );
}
