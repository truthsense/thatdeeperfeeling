'use client';

export default function PrivacyPolicyPage() {
  return (
    <>
      <section className="policy-hero">
        <div className="container content-container">
          <h1>Privacy Policy</h1>
          <p className="hero-subtitle">
            Your privacy matters. This policy explains how That Deeper Feeling collects,
            uses, and protects your personal information.
          </p>
          <p className="effective-date">Effective Date: February 17, 2026</p>
        </div>
      </section>

      <section className="policy-content">
        <div className="container content-container">
          <div className="policy-section">
            <h2>1. Who We Are</h2>
            <p>
              That Deeper Feeling is an intimacy and embodiment coaching practice operated by
              Kimberly Bryant. This privacy policy applies to all services offered through
              thatdeeperfeeling.com, including one-on-one coaching, group programs, retreats,
              and digital resources.
            </p>
          </div>

          <div className="policy-section">
            <h2>2. Information We Collect</h2>

            <h3>Information You Provide Directly</h3>
            <ul>
              <li><strong>Contact information:</strong> Name, email address, and phone number when you book a consultation, subscribe to our newsletter, or reach out through our contact form.</li>
              <li><strong>Intake form responses:</strong> Information you share through our client intake form, including your goals, background, and areas of focus.</li>
              <li><strong>Session content:</strong> Topics discussed during coaching sessions. Brief session notes may be kept to support continuity of care.</li>
              <li><strong>Payment information:</strong> Billing details processed securely through Stripe. We do not store your full credit card number.</li>
              <li><strong>Retreat registration:</strong> Dietary preferences, accessibility needs, emergency contact, and other information relevant to retreat participation.</li>
            </ul>

            <h3>Information Collected Automatically</h3>
            <ul>
              <li><strong>Website analytics:</strong> Pages visited, time on site, referring URLs, and general geographic region. This data is collected in aggregate and is not used to identify you personally.</li>
              <li><strong>Cookies:</strong> Our website uses essential cookies for site functionality. Third-party services (Calendly, Stripe, Google Forms) may set their own cookies when you interact with their embedded tools.</li>
            </ul>
          </div>

          <div className="policy-section">
            <h2>3. How We Use Your Information</h2>
            <ul>
              <li>To provide and personalize coaching services</li>
              <li>To schedule and manage appointments</li>
              <li>To process payments and send receipts</li>
              <li>To communicate about your sessions, programs, or retreat logistics</li>
              <li>To send newsletters and resources you have opted into</li>
              <li>To improve our website and services</li>
              <li>To comply with legal obligations</li>
            </ul>
          </div>

          <div className="policy-section">
            <h2>4. How We Protect Your Information</h2>
            <p>
              Given the sensitive and intimate nature of this work, we take your privacy
              seriously. Your information is protected through:
            </p>
            <ul>
              <li>Secure, encrypted connections (HTTPS) on our website</li>
              <li>PCI-compliant payment processing through Stripe</li>
              <li>Limited access&mdash;only Kimberly has access to session notes and intake forms</li>
              <li>Secure storage of digital records</li>
              <li>No sharing of client names, testimonials, or session details without explicit written consent</li>
            </ul>
          </div>

          <div className="policy-section">
            <h2>5. Sensitive Information</h2>
            <p>
              We recognize that the nature of intimacy and embodiment coaching means you may
              share deeply personal information&mdash;including details about your sexuality,
              relationships, trauma history, or spiritual practices. This information is:
            </p>
            <ul>
              <li>Held in strict confidence</li>
              <li>Never shared with third parties</li>
              <li>Never used for marketing purposes</li>
              <li>Only disclosed if there is imminent risk of harm to yourself or others, as required by law</li>
            </ul>
          </div>

          <div className="policy-section">
            <h2>6. Third-Party Services</h2>
            <p>We use the following third-party services to deliver our work:</p>
            <ul>
              <li><strong>Calendly</strong> &mdash; Scheduling consultations and sessions</li>
              <li><strong>Stripe</strong> &mdash; Payment processing</li>
              <li><strong>Google Forms</strong> &mdash; Client intake forms</li>
              <li><strong>Zoom</strong> &mdash; Video sessions</li>
              <li><strong>Voxer</strong> &mdash; Between-session voice messaging (for applicable containers)</li>
              <li><strong>Vercel</strong> &mdash; Website hosting</li>
            </ul>
            <p>
              Each of these services has its own privacy policy. We encourage you to review
              them. We select tools that prioritize security and confidentiality, but we cannot
              control their data practices.
            </p>
          </div>

          <div className="policy-section">
            <h2>7. Your Rights</h2>
            <p>You have the right to:</p>
            <ul>
              <li><strong>Access</strong> the personal information we hold about you</li>
              <li><strong>Correct</strong> any inaccurate information</li>
              <li><strong>Delete</strong> your personal data (subject to legal retention requirements)</li>
              <li><strong>Opt out</strong> of marketing communications at any time</li>
              <li><strong>Request a copy</strong> of your data in a portable format</li>
            </ul>
            <p>
              To exercise any of these rights, contact us at{' '}
              <a href="mailto:kimberly@thatdeeperfeeling.com">kimberly@thatdeeperfeeling.com</a>.
            </p>
          </div>

          <div className="policy-section">
            <h2>8. Data Retention</h2>
            <p>
              We retain your personal information only as long as necessary to provide our
              services and fulfill the purposes described in this policy. Session notes are
              retained for the duration of our coaching relationship and for up to one year
              after our last session, unless you request earlier deletion. Financial records
              are retained as required by tax and accounting regulations.
            </p>
          </div>

          <div className="policy-section">
            <h2>9. Children&rsquo;s Privacy</h2>
            <p>
              Our services are intended for adults 18 years of age and older. We do not
              knowingly collect information from anyone under 18. If we learn that we have
              collected personal information from a minor, we will delete it promptly.
            </p>
          </div>

          <div className="policy-section">
            <h2>10. Changes to This Policy</h2>
            <p>
              We may update this privacy policy from time to time. Changes will be posted on
              this page with an updated effective date. Continued use of our services after
              changes are posted constitutes acceptance of the updated policy.
            </p>
          </div>

          <div className="policy-section">
            <h2>11. Contact</h2>
            <p>
              If you have questions or concerns about this privacy policy or how your data is
              handled, please reach out:
            </p>
            <p>
              <strong>Email:</strong>{' '}
              <a href="mailto:kimberly@thatdeeperfeeling.com">kimberly@thatdeeperfeeling.com</a>
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

        .policy-section h3 {
          font-size: 1.15rem;
          color: var(--primary-wine);
          margin: 1.5rem 0 0.75rem;
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
      `}</style>
    </>
  );
}
