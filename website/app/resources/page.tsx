'use client';

export default function ResourcesPage() {
  return (
    <>
      <section className="resources-hero">
        <div className="container content-container">
          <h1>Community Offerings</h1>
          <p className="hero-subtitle">
            This space is being built with intention. Community offerings, curated resources,
            and social spaces are on their way.
          </p>
        </div>
      </section>

      <section className="resources-content">
        <div className="container content-container">
          <div className="coming-soon-card">
            <div className="icon-wrapper">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
                <circle cx="12" cy="12" r="10" />
                <path d="M12 6v6l4 2" />
              </svg>
            </div>
            <h2>In the Works</h2>
            <p>
              We are curating something meaningful for this space. Expect community circles,
              guided resources, and ways to stay connected between sessions and retreats.
            </p>
          </div>

          <div className="offerings-grid">
            <div className="offering-item">
              <h3>Social Community</h3>
              <p>
                Private social media groups for women in the That Deeper Feeling community
                to connect, share, and support one another between containers.
              </p>
            </div>
            <div className="offering-item">
              <h3>Curated Resources</h3>
              <p>
                Recommended readings, practices, and tools to deepen your embodiment
                journey on your own time.
              </p>
            </div>
            <div className="offering-item">
              <h3>Community Circles</h3>
              <p>
                Virtual and in-person gatherings to maintain connection and continue
                the work beyond retreats and sessions.
              </p>
            </div>
          </div>

          <div className="stay-connected">
            <h2>Stay Connected</h2>
            <p>
              Follow along and join the conversation as this space takes shape.
            </p>
            <div className="social-links">
              <a
                href="https://www.instagram.com/thatdeeperfeeling"
                target="_blank"
                rel="noopener noreferrer"
                className="social-link"
              >
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
                </svg>
                Instagram
              </a>
            </div>
            <div className="newsletter-cta">
              <p>Want to be the first to know when new offerings drop?</p>
              <a href="/#newsletter" className="btn btn-primary">
                Join the Newsletter
              </a>
            </div>
          </div>
        </div>
      </section>

      <style jsx>{`
        .resources-hero {
          background: linear-gradient(135deg, var(--neutral-cream) 0%, var(--secondary-warm-beige) 100%);
          padding: 5rem 1.5rem 4rem;
          text-align: center;
        }

        .resources-hero h1 {
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

        .resources-content {
          background: var(--neutral-soft-white);
          padding: 5rem 0;
        }

        .coming-soon-card {
          text-align: center;
          padding: 3rem 2rem;
          margin-bottom: 3rem;
        }

        .icon-wrapper {
          color: var(--accent-terracotta);
          margin-bottom: 1.5rem;
        }

        .coming-soon-card h2 {
          font-size: 1.75rem;
          color: var(--primary-burgundy);
          margin-bottom: 1rem;
        }

        .coming-soon-card p {
          font-size: 1.1rem;
          line-height: 1.8;
          color: var(--neutral-warm-gray);
          max-width: 600px;
          margin: 0 auto;
        }

        .offerings-grid {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          gap: 2rem;
          margin-bottom: 4rem;
        }

        .offering-item {
          background: white;
          padding: 2rem;
          border-radius: 0.75rem;
          box-shadow: 0 4px 20px rgba(139, 58, 71, 0.06);
          border-top: 3px solid var(--accent-terracotta);
        }

        .offering-item h3 {
          font-size: 1.2rem;
          color: var(--primary-burgundy);
          margin-bottom: 0.75rem;
        }

        .offering-item p {
          font-size: 1rem;
          line-height: 1.7;
          color: var(--neutral-warm-gray);
        }

        .stay-connected {
          text-align: center;
          padding: 3rem 2rem;
          background: var(--neutral-cream);
          border-radius: 1rem;
        }

        .stay-connected h2 {
          font-size: 1.5rem;
          color: var(--primary-burgundy);
          margin-bottom: 0.75rem;
        }

        .stay-connected > p {
          font-size: 1.05rem;
          color: var(--neutral-warm-gray);
          margin-bottom: 1.5rem;
        }

        .social-links {
          display: flex;
          justify-content: center;
          gap: 1rem;
          margin-bottom: 2rem;
        }

        .social-link {
          display: inline-flex;
          align-items: center;
          gap: 0.5rem;
          padding: 0.75rem 1.5rem;
          background: white;
          border-radius: 2rem;
          color: var(--primary-burgundy);
          font-size: 1rem;
          font-weight: 500;
          text-decoration: none;
          transition: all 0.3s ease;
          box-shadow: 0 2px 10px rgba(139, 58, 71, 0.08);
        }

        .social-link:hover {
          background: var(--primary-burgundy);
          color: var(--neutral-soft-white);
          transform: translateY(-2px);
          box-shadow: 0 6px 20px rgba(139, 58, 71, 0.2);
        }

        .newsletter-cta {
          margin-top: 1.5rem;
        }

        .newsletter-cta p {
          font-size: 1rem;
          color: var(--neutral-warm-gray);
          margin-bottom: 1rem;
        }

        .newsletter-cta a:global(.btn-primary) {
          color: var(--neutral-soft-white);
          text-decoration: none;
        }

        @media (max-width: 768px) {
          .offerings-grid {
            grid-template-columns: 1fr;
            gap: 1.5rem;
          }
        }
      `}</style>
    </>
  );
}
