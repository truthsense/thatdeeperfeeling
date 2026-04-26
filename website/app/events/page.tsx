'use client';

import Button from '@/components/ui/Button';

export default function EventsPage() {
  return (
    <>
      <section className="events-hero">
        <div className="container content-container">
          <p className="events-eyebrow">Gatherings &amp; Retreats</p>
          <h1>Something Is Being Prepared</h1>
          <p className="events-subhead">
            Intentional spaces for women ready to come home to themselves.
          </p>
        </div>
      </section>

      <section className="events-body">
        <div className="container content-container">
          <div className="events-inner">
            <p className="events-lead">
              Future retreats and group containers are in the planning stages.
            </p>
            <p>
              These gatherings are designed to be small, curated, and deeply held &mdash;
              spaces where depth and joy exist together, and where no woman has to
              perform in order to belong.
            </p>
            <p>
              When the next event is ready, it will be announced here and through
              Kimberly&rsquo;s community. The best way to stay connected is to reach out
              directly or begin with a Curiosity Call.
            </p>

            <div className="events-cta-group">
              <Button href="/start" variant="primary">
                Start with a Curiosity Call
              </Button>
              <Button href="/contact" variant="secondary">
                Get in Touch
              </Button>
            </div>

            <div className="events-what-to-expect">
              <h2>What These Spaces Are Built For</h2>
              <ul className="expect-list">
                <li>Women navigating life after high-demand religion or rigid belief systems</li>
                <li>Reconnecting to the body through somatic and embodiment practices</li>
                <li>Reclaiming internal authority and personal power</li>
                <li>Community without hierarchy &mdash; depth without performance</li>
                <li>Integration, play, and the return to aliveness</li>
              </ul>
            </div>

            <p className="events-closing">
              If you feel called to this work and don&rsquo;t want to wait &mdash;
              the one-on-one container is open now.
            </p>
          </div>
        </div>
      </section>

      <style jsx>{`
        .events-hero {
          background: linear-gradient(135deg, var(--primary-burgundy) 0%, var(--primary-wine) 100%);
          color: var(--neutral-soft-white);
          padding: 6rem 1.5rem 5rem;
          text-align: center;
        }

        .events-eyebrow {
          font-size: 0.9rem;
          letter-spacing: 0.12em;
          text-transform: uppercase;
          color: var(--accent-terracotta);
          margin-bottom: 1rem;
          font-weight: 600;
        }

        .events-hero h1 {
          color: var(--neutral-soft-white);
          font-size: clamp(2.25rem, 5vw, 3.75rem);
          margin-bottom: 1rem;
        }

        .events-subhead {
          font-size: clamp(1.05rem, 2vw, 1.3rem);
          color: var(--neutral-cream);
          font-style: italic;
          max-width: 520px;
          margin: 0 auto;
          line-height: 1.7;
        }

        .events-body {
          background: var(--neutral-soft-white);
          padding: 5rem 0;
        }

        .events-inner {
          max-width: 620px;
          margin: 0 auto;
        }

        .events-lead {
          font-size: 1.25rem;
          font-weight: 500;
          color: var(--primary-burgundy);
          font-style: italic;
          margin-bottom: 1.5rem;
          line-height: 1.7;
        }

        .events-inner p {
          font-size: 1.1rem;
          line-height: 1.8;
          color: var(--neutral-charcoal);
          margin-bottom: 1.25rem;
        }

        .events-cta-group {
          display: flex;
          gap: 1rem;
          flex-wrap: wrap;
          margin: 2.5rem 0;
        }

        .events-what-to-expect {
          background: var(--neutral-cream);
          padding: 2rem 2.5rem;
          border-radius: 0.75rem;
          border-top: 3px solid var(--accent-terracotta);
          margin: 2.5rem 0;
        }

        .events-what-to-expect h2 {
          font-size: 1.35rem;
          color: var(--primary-burgundy);
          margin-bottom: 1.25rem;
        }

        .expect-list {
          list-style: none;
          padding: 0;
          margin: 0;
        }

        .expect-list li {
          padding: 0.6rem 0;
          padding-left: 1.75rem;
          position: relative;
          font-size: 1.05rem;
          color: var(--neutral-charcoal);
          line-height: 1.6;
        }

        .expect-list li::before {
          content: '•';
          position: absolute;
          left: 0;
          color: var(--accent-terracotta);
          font-size: 1.25rem;
          line-height: 1;
        }

        .events-closing {
          font-style: italic;
          color: var(--primary-burgundy) !important;
          font-size: 1.1rem !important;
          margin-top: 2rem;
        }
      `}</style>
    </>
  );
}
