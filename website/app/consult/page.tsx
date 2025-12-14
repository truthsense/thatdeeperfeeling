'use client';

export default function ConsultPage() {
  return (
    <>
      {/* Hero Section */}
      <section className="consult-hero">
        <div className="container content-container">
          <h1>Book Your Consultation</h1>
          <p className="hero-subtitle">
            A grounded, spacious conversation—not a sales call.
          </p>
        </div>
      </section>

      {/* Consultation Details */}
      <section className="consult-details">
        <div className="container content-container">
          <div className="details-content">
            <p className="intro-text">
              The consultation is a place for us to explore what you're navigating, what you're longing for, and whether my work is the right support for you.
            </p>

            <div className="explore-section">
              <h2>During the Consultation, We'll Explore:</h2>
              <ul className="explore-list">
                <li>What's bringing you here</li>
                <li>What kind of support you're seeking</li>
                <li>Which container may best serve you</li>
                <li>Boundaries, expectations, and next steps</li>
              </ul>
            </div>

            <div className="investment-box">
              <h3>Investment</h3>
              <p className="price">$125</p>
              <p className="investment-note">
                This fee honors both our time and energy.
              </p>
            </div>

            <div className="outcome-text">
              <p>
                If we feel aligned, we'll discuss options for working together.
              </p>
              <p>
                If not, you'll still leave with clarity.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Calendly Embed */}
      <section className="consult-booking">
        <div className="container">
          <h2 className="booking-heading">Step Into That Deeper Feeling</h2>

          <div className="calendly-container">
            <div
              className="calendly-inline-widget"
              data-url="https://calendly.com/kimberlymmbryant/that-deeper-feeling?hide_gdpr_banner=1&background_color=F5F1E8&text_color=3A3530&primary_color=8B3A47"
              style={{
                minWidth: '320px',
                height: '700px',
              }}
            ></div>
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
              <h3>Confirmation</h3>
              <p>
                You'll receive a confirmation email with your Zoom link and a brief intake form.
              </p>
            </div>
            <div className="step">
              <div className="step-number">2</div>
              <h3>Preparation</h3>
              <p>
                Take a few moments to reflect on what's bringing you to this work and what you're hoping to explore.
              </p>
            </div>
            <div className="step">
              <div className="step-number">3</div>
              <h3>Our Conversation</h3>
              <p>
                We'll meet for 60 minutes to explore your needs, answer questions, and see if we're a good fit.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Load Calendly Script */}
      <script
        type="text/javascript"
        src="https://assets.calendly.com/assets/external/widget.js"
        async
      ></script>

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
          content: '•';
          position: absolute;
          left: 0;
          color: var(--accent-terracotta);
          font-size: 1.5rem;
          line-height: 1;
        }

        .investment-box {
          background: var(--neutral-cream);
          padding: 2.5rem;
          border-radius: 1rem;
          text-align: center;
          margin-bottom: 3rem;
          border-left: 4px solid var(--accent-gold);
        }

        .investment-box h3 {
          font-size: 1.25rem;
          color: var(--primary-wine);
          margin-bottom: 1rem;
        }

        .price {
          font-size: 2.5rem;
          font-weight: 700;
          color: var(--primary-burgundy);
          margin-bottom: 0.5rem;
          font-family: var(--font-heading);
        }

        .investment-note {
          font-size: 1rem;
          color: var(--neutral-warm-gray);
          font-style: italic;
          margin: 0;
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

        .booking-heading {
          text-align: center;
          font-size: clamp(2rem, 4vw, 3rem);
          color: var(--primary-wine);
          margin-bottom: 3rem;
        }

        .calendly-container {
          max-width: 900px;
          margin: 0 auto;
          background: white;
          border-radius: 1rem;
          overflow: hidden;
          box-shadow: 0 10px 40px rgba(139, 58, 71, 0.15);
        }

        :global(.calendly-inline-widget) {
          width: 100%;
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
