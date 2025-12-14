'use client';

import Button from '@/components/ui/Button';

export default function EventsPage() {
  return (
    <>
      {/* Hero Section */}
      <section className="events-hero">
        <div className="container content-container">
          <h1>Into the Embers</h1>
          <p className="hero-subtitle">
            Curated in-person gatherings for embodied intimacy and conscious exploration.
          </p>
        </div>
      </section>

      {/* About Events */}
      <section className="events-about">
        <div className="container content-container">
          <div className="about-content">
            <h2>Sacred Group Containers</h2>
            <p className="intro-text">
              Into the Embers gatherings are multi-day immersive experiences designed for deep group work, somatic practices, and facilitated exploration in a trauma-informed, consent-centered container.
            </p>

            <div className="what-to-expect">
              <h3>What to Expect</h3>
              <ul className="expect-list">
                <li>2-3 day immersive retreats</li>
                <li>Somatic practices & sacred rituals</li>
                <li>Group facilitation & witnessing</li>
                <li>Meals & accommodations included</li>
                <li>Limited to 8-12 participants for intimacy and depth</li>
              </ul>
            </div>

            <div className="ideal-for">
              <h3>These Gatherings Are For You If:</h3>
              <p>
                You're seeking in-person embodied work. You value group energy and connection. You're ready to explore power, pleasure, and presence in community while being held in safety and consent.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Coming Soon */}
      <section className="events-coming-soon">
        <div className="container content-container centered">
          <div className="coming-soon-box">
            <h2>Nothing on the Schedule Yet</h2>
            <p className="coming-soon-text">
              The next Into the Embers gathering is currently being curated. Join the mailing list to be the first to know when dates and details are announced.
            </p>

            <div className="waitlist-form">
              <h3>Get Notified</h3>
              <p className="form-note">
                Sign up below to receive invitations and updates about upcoming gatherings.
              </p>
              <form className="newsletter-form">
                <input
                  type="email"
                  placeholder="Your email address"
                  className="newsletter-input"
                  required
                  aria-label="Email address"
                />
                <button type="submit" className="newsletter-button">
                  Join the Waitlist
                </button>
              </form>
            </div>
          </div>
        </div>
      </section>

      {/* Other Offerings */}
      <section className="events-other">
        <div className="container content-container centered">
          <h2>Ready to Work Together Now?</h2>
          <p>
            Explore private coaching containers or the Flicker and Flame online membership while you wait for the next in-person gathering.
          </p>
          <Button href="/offerings" variant="primary">
            View All Offerings
          </Button>
        </div>
      </section>

      <style jsx>{`
        /* Hero */
        .events-hero {
          background: linear-gradient(135deg, var(--primary-burgundy) 0%, var(--primary-wine) 100%);
          color: var(--neutral-soft-white);
          padding: 5rem 1.5rem 4rem;
          text-align: center;
        }

        .events-hero h1 {
          color: var(--neutral-soft-white);
          font-size: clamp(2.5rem, 5vw, 4rem);
          margin-bottom: 1rem;
        }

        .hero-subtitle {
          font-size: clamp(1.1rem, 2vw, 1.4rem);
          color: var(--neutral-cream);
          font-style: italic;
        }

        /* About Events */
        .events-about {
          background: var(--neutral-soft-white);
          padding: 5rem 0;
        }

        .about-content {
          max-width: 700px;
          margin: 0 auto;
        }

        .about-content h2 {
          text-align: center;
          font-size: clamp(2rem, 4vw, 3rem);
          margin-bottom: 1.5rem;
        }

        .intro-text {
          font-size: 1.15rem;
          line-height: 1.8;
          color: var(--neutral-charcoal);
          margin-bottom: 3rem;
          text-align: center;
        }

        .what-to-expect,
        .ideal-for {
          margin-bottom: 3rem;
        }

        .what-to-expect h3,
        .ideal-for h3 {
          font-size: 1.5rem;
          color: var(--primary-burgundy);
          margin-bottom: 1.5rem;
        }

        .expect-list {
          list-style: none;
          padding: 0;
        }

        .expect-list li {
          padding: 0.75rem 0;
          padding-left: 2rem;
          position: relative;
          font-size: 1.1rem;
          color: var(--neutral-charcoal);
        }

        .expect-list li::before {
          content: '•';
          position: absolute;
          left: 0;
          color: var(--accent-terracotta);
          font-size: 1.5rem;
          line-height: 1;
        }

        .ideal-for p {
          font-size: 1.1rem;
          line-height: 1.7;
          color: var(--neutral-charcoal);
        }

        /* Coming Soon */
        .events-coming-soon {
          background: var(--neutral-cream);
          padding: 5rem 0;
        }

        .centered {
          text-align: center;
        }

        .coming-soon-box {
          background: white;
          padding: 4rem 3rem;
          border-radius: 1rem;
          box-shadow: 0 10px 40px rgba(139, 58, 71, 0.15);
          max-width: 600px;
          margin: 0 auto;
        }

        .coming-soon-box h2 {
          font-size: clamp(1.75rem, 3vw, 2.5rem);
          margin-bottom: 1.5rem;
        }

        .coming-soon-text {
          font-size: 1.15rem;
          line-height: 1.7;
          color: var(--neutral-warm-gray);
          margin-bottom: 3rem;
        }

        .waitlist-form {
          background: var(--neutral-cream);
          padding: 2rem;
          border-radius: 0.75rem;
        }

        .waitlist-form h3 {
          font-size: 1.5rem;
          color: var(--primary-burgundy);
          margin-bottom: 0.75rem;
        }

        .form-note {
          font-size: 1rem;
          color: var(--neutral-warm-gray);
          margin-bottom: 1.5rem;
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
          font-size: 1rem;
          background: white;
          color: var(--neutral-charcoal);
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

        /* Other Offerings */
        .events-other {
          background: var(--neutral-soft-white);
          padding: 5rem 0;
        }

        .events-other h2 {
          margin-bottom: 1rem;
        }

        .events-other p {
          font-size: 1.15rem;
          color: var(--neutral-warm-gray);
          margin-bottom: 2rem;
          line-height: 1.7;
        }
      `}</style>
    </>
  );
}
