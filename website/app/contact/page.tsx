'use client';

export default function ContactPage() {
  return (
    <>
      {/* Hero Section */}
      <section className="contact-hero">
        <div className="container content-container">
          <h1>Get In Touch</h1>
          <p className="hero-subtitle">
            For inquiries about coaching, speaking engagements, or collaborations.
          </p>
        </div>
      </section>

      {/* Contact Methods */}
      <section className="contact-methods">
        <div className="container content-container">
          <div className="methods-grid">
            <div className="method-card">
              <h3>Book a Consultation</h3>
              <p>
                Ready to explore working together? Schedule a consultation to discuss your goals and see if we're a good fit.
              </p>
              <a href="/consult" className="btn btn-primary">
                Book Consultation
              </a>
            </div>

            <div className="method-card">
              <h3>Email</h3>
              <p>
                For general inquiries, press, or collaboration opportunities.
              </p>
              <a href="mailto:thatdeeperfeeling@gmail.com" className="btn btn-secondary">
                thatdeeperfeeling@gmail.com
              </a>
            </div>

            <div className="method-card">
              <h3>Follow Along</h3>
              <p>
                Connect on Instagram and Facebook for insights, invitations, and embodied reflections.
              </p>
              <div style={{display: 'flex', flexDirection: 'column', gap: '0.75rem'}}>
                <a href="https://instagram.com/thatdeeperfeeling" target="_blank" rel="noopener noreferrer" className="btn btn-secondary">
                  Instagram
                </a>
                <a href="https://www.facebook.com/people/That-Deeper-Feeling/61566488580618/" target="_blank" rel="noopener noreferrer" className="btn btn-secondary">
                  Facebook
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Intake Form */}
      <section className="contact-intake">
        <div className="container">
          <div className="intake-header">
            <h2>Client Intake Form</h2>
            <p className="intake-intro">
              If you've already booked a consultation, please complete this intake form to help me prepare for our conversation.
            </p>
          </div>

          <div className="form-container">
            <iframe
              src="https://docs.google.com/forms/d/e/1FAIpQLSdF5XTGJzBRcuYJ4dzUkRuWNp_cKNslVMNzVgw605qiAPEYCQ/viewform?embedded=true"
              width="100%"
              height="1200"
              frameBorder="0"
              marginHeight={0}
              marginWidth={0}
              title="Client Intake Form"
            >
              Loading…
            </iframe>
          </div>
        </div>
      </section>

      {/* FAQ Link */}
      <section className="contact-faq">
        <div className="container content-container centered">
          <h2>Have Questions?</h2>
          <p>
            Check out the FAQ page for answers to common questions about coaching, containers, and how we work together.
          </p>
          <a href="/faq" className="btn btn-accent">
            View FAQ
          </a>
        </div>
      </section>

      <style jsx>{`
        /* Hero */
        .contact-hero {
          background: linear-gradient(135deg, var(--neutral-cream) 0%, var(--secondary-warm-beige) 100%);
          padding: 5rem 1.5rem 4rem;
          text-align: center;
        }

        .contact-hero h1 {
          font-size: clamp(2.5rem, 5vw, 4rem);
          margin-bottom: 1.5rem;
        }

        .hero-subtitle {
          font-size: clamp(1.1rem, 2vw, 1.3rem);
          color: var(--neutral-warm-gray);
          line-height: 1.7;
        }

        /* Contact Methods */
        .contact-methods {
          background: var(--neutral-soft-white);
          padding: 5rem 0;
        }

        .methods-grid {
          display: grid;
          grid-template-columns: 1fr;
          gap: 2rem;
        }

        @media (min-width: 768px) {
          .methods-grid {
            grid-template-columns: repeat(3, 1fr);
          }
        }

        .method-card {
          padding: 2.5rem 2rem;
          background: var(--neutral-cream);
          border-radius: 1rem;
          text-align: center;
          display: flex;
          flex-direction: column;
          gap: 1.5rem;
          transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .method-card:hover {
          transform: translateY(-5px);
          box-shadow: 0 15px 40px rgba(139, 58, 71, 0.2);
        }

        .method-card h3 {
          color: var(--primary-burgundy);
          font-size: 1.5rem;
          margin-bottom: 0.5rem;
        }

        .method-card p {
          color: var(--neutral-charcoal);
          line-height: 1.6;
          flex-grow: 1;
        }

        /* Intake Form */
        .contact-intake {
          background: var(--neutral-cream);
          padding: 5rem 0;
        }

        .intake-header {
          text-align: center;
          max-width: 700px;
          margin: 0 auto 3rem;
        }

        .intake-header h2 {
          font-size: clamp(2rem, 4vw, 3rem);
          margin-bottom: 1rem;
        }

        .intake-intro {
          font-size: 1.15rem;
          color: var(--neutral-warm-gray);
          line-height: 1.7;
        }

        .form-container {
          max-width: 800px;
          margin: 0 auto;
          background: white;
          border-radius: 1rem;
          overflow: hidden;
          box-shadow: 0 10px 40px rgba(139, 58, 71, 0.15);
        }

        .form-container iframe {
          display: block;
          border: none;
        }

        /* FAQ Section */
        .contact-faq {
          background: var(--neutral-soft-white);
          padding: 5rem 0;
        }

        .centered {
          text-align: center;
        }

        .contact-faq h2 {
          margin-bottom: 1rem;
        }

        .contact-faq p {
          font-size: 1.15rem;
          color: var(--neutral-warm-gray);
          margin-bottom: 2rem;
          line-height: 1.7;
        }
      `}</style>
    </>
  );
}
