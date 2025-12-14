'use client';

import Link from 'next/link';

export default function Footer() {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-content">
          {/* Brand Section */}
          <div className="footer-section">
            <h3 className="footer-brand">That Deeper Feeling</h3>
            <p className="footer-tagline">
              Where sensuality, soul, and surrender meet.
            </p>
          </div>

          {/* Quick Links */}
          <div className="footer-section">
            <h4 className="footer-heading">Explore</h4>
            <ul className="footer-links">
              <li>
                <Link href="/about">About Kimberly</Link>
              </li>
              <li>
                <Link href="/offerings">Offerings</Link>
              </li>
              <li>
                <Link href="/consult">Book Consultation</Link>
              </li>
              <li>
                <Link href="/resources">Resources</Link>
              </li>
            </ul>
          </div>

          {/* Legal & Policies */}
          <div className="footer-section">
            <h4 className="footer-heading">Legal</h4>
            <ul className="footer-links">
              <li>
                <Link href="/policies">Policies & Boundaries</Link>
              </li>
              <li>
                <Link href="/privacy">Privacy Policy</Link>
              </li>
              <li>
                <Link href="/terms">Terms of Service</Link>
              </li>
            </ul>
          </div>

          {/* Newsletter Signup */}
          <div className="footer-section">
            <h4 className="footer-heading">Stay Connected</h4>
            <p className="newsletter-text">
              Receive invitations, insights, and resources for deepening your intimacy journey.
            </p>
            <form className="newsletter-form">
              <input
                type="email"
                placeholder="Your email"
                className="newsletter-input"
                aria-label="Email address"
              />
              <button type="submit" className="newsletter-button">
                Subscribe
              </button>
            </form>

            {/* Social Links */}
            <div className="social-links">
              <a href="https://instagram.com/thatdeeperfeeling" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
                <span>IG</span>
              </a>
              <a href="https://www.facebook.com/people/That-Deeper-Feeling/61566488580618/" target="_blank" rel="noopener noreferrer" aria-label="Facebook">
                <span>FB</span>
              </a>
            </div>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="footer-bottom">
          <p className="copyright">
            © {currentYear} That Deeper Feeling. All rights reserved.
          </p>
          <p className="disclaimer">
            Coaching services are not therapy and are not a substitute for professional mental health treatment.
          </p>
        </div>
      </div>

      <style jsx>{`
        .footer {
          background: var(--neutral-cream);
          padding: 4rem 0 2rem;
          margin-top: 5rem;
        }

        .footer-content {
          display: grid;
          grid-template-columns: 1fr;
          gap: 3rem;
          margin-bottom: 3rem;
        }

        @media (min-width: 768px) {
          .footer-content {
            grid-template-columns: 2fr 1fr 1fr 1.5fr;
            gap: 2rem;
          }
        }

        .footer-section {
          display: flex;
          flex-direction: column;
          gap: 1rem;
        }

        .footer-brand {
          font-family: var(--font-heading);
          font-size: 1.5rem;
          color: var(--primary-burgundy);
          margin-bottom: 0.5rem;
        }

        .footer-tagline {
          font-size: 0.95rem;
          color: var(--neutral-warm-gray);
          line-height: 1.6;
          font-style: italic;
        }

        .footer-heading {
          font-family: var(--font-body);
          font-size: 1rem;
          font-weight: 600;
          color: var(--primary-wine);
          margin-bottom: 0.5rem;
        }

        .footer-links {
          list-style: none;
          display: flex;
          flex-direction: column;
          gap: 0.75rem;
        }

        .footer-links a {
          color: var(--neutral-charcoal);
          font-size: 0.95rem;
          text-decoration: none;
          transition: color 0.3s ease;
        }

        .footer-links a:hover {
          color: var(--primary-burgundy);
        }

        .newsletter-text {
          font-size: 0.9rem;
          color: var(--neutral-warm-gray);
          line-height: 1.5;
        }

        .newsletter-form {
          display: flex;
          flex-direction: column;
          gap: 0.75rem;
        }

        .newsletter-input {
          padding: 0.75rem 1rem;
          border: 1px solid var(--secondary-taupe);
          border-radius: 0.375rem;
          font-family: var(--font-body);
          font-size: 0.95rem;
          background: var(--neutral-soft-white);
          color: var(--neutral-charcoal);
          transition: border-color 0.3s ease;
        }

        .newsletter-input:focus {
          outline: none;
          border-color: var(--primary-burgundy);
        }

        .newsletter-button {
          padding: 0.75rem 1.5rem;
          background: var(--primary-burgundy);
          color: var(--neutral-soft-white);
          border: none;
          border-radius: 0.375rem;
          font-family: var(--font-body);
          font-weight: 500;
          cursor: pointer;
          transition: all 0.3s ease;
        }

        .newsletter-button:hover {
          background: var(--primary-wine);
          transform: translateY(-2px);
        }

        .social-links {
          display: flex;
          gap: 1rem;
          margin-top: 0.5rem;
        }

        .social-links a {
          width: 40px;
          height: 40px;
          border-radius: 50%;
          background: var(--primary-burgundy);
          color: var(--neutral-soft-white);
          display: flex;
          align-items: center;
          justify-content: center;
          text-decoration: none;
          font-size: 0.85rem;
          font-weight: 600;
          transition: all 0.3s ease;
        }

        .social-links a:hover {
          background: var(--accent-terracotta);
          transform: translateY(-3px);
        }

        .footer-bottom {
          padding-top: 2rem;
          border-top: 1px solid rgba(139, 58, 71, 0.1);
          display: flex;
          flex-direction: column;
          gap: 1rem;
          text-align: center;
        }

        @media (min-width: 768px) {
          .footer-bottom {
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
          }
        }

        .copyright,
        .disclaimer {
          font-size: 0.85rem;
          color: var(--neutral-warm-gray);
        }

        .disclaimer {
          font-style: italic;
        }
      `}</style>
    </footer>
  );
}
