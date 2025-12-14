'use client';

import Button from '@/components/ui/Button';

export default function OfferingsPage() {
  const offerings = [
    {
      title: 'Return to Power',
      slug: 'return-to-power',
      duration: '6-Month Private Container',
      price: '$3,600',
      tagline: 'Deep, sustained transformation for reclaiming sovereignty and embodying pleasure.',
      description: 'For those ready to go all the way. This container holds space for profound shifts in how you relate to power, desire, intimacy, and your own body.',
      ideal: 'Ready for sustained, deep work. Committed to transformation.',
      features: [
        'Bi-weekly 90-minute sessions',
        'Personalized practices & resources',
        'Voxer support between sessions',
        'Sacred ritual design',
        'Embodiment homework & integration',
      ],
      badge: 'Most Popular',
    },
    {
      title: 'Edgewalker',
      slug: 'edgewalker',
      duration: '3-Month Private Container',
      price: '$2,100',
      tagline: 'Explore a specific edge—desire, kink dynamics, or pleasure reclamation.',
      description: 'Perfect for exploring one focused area of your intimacy journey. Whether it\'s communication, power dynamics, or healing your relationship with pleasure after trauma.',
      ideal: 'Have a specific goal or edge to explore. Want focused support.',
      features: [
        'Weekly 60-minute sessions',
        'Customized embodiment practices',
        'Email support',
        'Integration resources',
        'Personalized reading & resources',
      ],
    },
    {
      title: 'Sacred Eruption',
      slug: 'sacred-eruption',
      duration: 'Single Session Deep Dive',
      price: '$400',
      tagline: 'A powerful, contained exploration for a specific breakthrough.',
      description: 'One 2-hour intensive session for addressing a specific block, question, or moment of transformation. Ideal for returning clients or focused work.',
      ideal: 'Have a specific question or block. Want a contained experience.',
      features: [
        '2-hour intensive session',
        'Pre-session intake & preparation',
        'Integration guide & practices',
        'Follow-up email support',
      ],
    },
    {
      title: 'Flicker and Flame',
      slug: 'flicker-and-flame',
      duration: 'Online Membership',
      price: '$47/month',
      tagline: 'Community, resources, and monthly workshops for ongoing exploration.',
      description: 'A sacred space for continuous learning, connection, and embodiment. Monthly workshops, resource library, and a private community of conscious explorers.',
      ideal: 'Want ongoing support. Value community and continuous learning.',
      features: [
        'Monthly live workshops',
        'Private community forum',
        'Resource library & practices',
        'Guest expert sessions',
        'Cancel anytime',
      ],
    },
    {
      title: 'Into the Embers',
      slug: 'into-the-embers',
      duration: 'In-Person Gatherings',
      price: 'TBD',
      tagline: 'Sacred group containers for embodied intimacy and conscious kink exploration.',
      description: 'Multi-day immersive experiences. Deep group work, somatic practices, and facilitated exploration in a trauma-informed, consent-centered container.',
      ideal: 'Want in-person embodied work. Value group energy and connection.',
      features: [
        '2-3 day immersive retreats',
        'Somatic practices & rituals',
        'Group facilitation & witnessing',
        'Meals & accommodations included',
        'Limited to 8-12 participants',
      ],
    },
  ];

  return (
    <>
      {/* Hero */}
      <section className="offerings-hero">
        <div className="container content-container">
          <h1>Choose Your Container</h1>
          <p className="hero-subtitle">
            Each offering is designed to honor your unique journey while providing structure, support, and sacred space for transformation.
          </p>
        </div>
      </section>

      {/* Offerings Grid */}
      <section className="offerings-section">
        <div className="container">
          <div className="offerings-grid">
            {offerings.map((offering, index) => (
              <div key={offering.slug} className={`offering-card ${index === 0 ? 'featured' : ''}`}>
                {offering.badge && <div className="badge">{offering.badge}</div>}
                <h2>{offering.title}</h2>
                <p className="duration">{offering.duration}</p>
                <p className="tagline">{offering.tagline}</p>
                <p className="description">{offering.description}</p>

                <div className="ideal-for">
                  <h4>Ideal For You If:</h4>
                  <p>{offering.ideal}</p>
                </div>

                <div className="features">
                  <h4>What's Included:</h4>
                  <ul>
                    {offering.features.map((feature, i) => (
                      <li key={i}>{feature}</li>
                    ))}
                  </ul>
                </div>

                <p className="price">{offering.price}</p>
                <Button href={`/offerings/${offering.slug}`} variant="primary" fullWidth>
                  Learn More
                </Button>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* How to Choose */}
      <section className="how-to-choose">
        <div className="container content-container">
          <h2>Not Sure Which Container Is Right for You?</h2>
          <p className="choose-intro">
            Book a free consultation and we'll explore your goals, answer your questions, and help you choose the path that feels most aligned.
          </p>
          <div className="choose-cta">
            <Button href="/consult" variant="primary">
              Schedule Free Consultation
            </Button>
          </div>
        </div>
      </section>

      <style jsx>{`
        /* Hero */
        .offerings-hero {
          background: linear-gradient(135deg, var(--neutral-cream) 0%, var(--secondary-warm-beige) 100%);
          padding: 5rem 1.5rem 4rem;
          text-align: center;
        }

        .offerings-hero h1 {
          font-size: clamp(2.5rem, 5vw, 4rem);
          margin-bottom: 1.5rem;
        }

        .hero-subtitle {
          font-size: clamp(1.1rem, 2vw, 1.3rem);
          color: var(--neutral-warm-gray);
          line-height: 1.7;
        }

        /* Offerings Grid */
        .offerings-section {
          background: var(--neutral-soft-white);
          padding: 5rem 0;
        }

        .offerings-grid {
          display: grid;
          grid-template-columns: 1fr;
          gap: 3rem;
        }

        @media (min-width: 768px) {
          .offerings-grid {
            grid-template-columns: repeat(2, 1fr);
          }
        }

        @media (min-width: 1024px) {
          .offerings-grid {
            grid-template-columns: repeat(2, 1fr);
          }
        }

        .offering-card {
          background: white;
          border: 2px solid var(--neutral-cream);
          border-radius: 1rem;
          padding: 2.5rem 2rem;
          display: flex;
          flex-direction: column;
          position: relative;
          transition: all 0.3s ease;
        }

        .offering-card:hover {
          border-color: var(--primary-burgundy);
          box-shadow: 0 15px 40px rgba(139, 58, 71, 0.2);
          transform: translateY(-8px);
        }

        .offering-card.featured {
          border-color: var(--primary-burgundy);
          background: linear-gradient(135deg, var(--neutral-soft-white) 0%, var(--neutral-cream) 100%);
        }

        .badge {
          position: absolute;
          top: -12px;
          right: 20px;
          background: var(--accent-terracotta);
          color: var(--neutral-soft-white);
          padding: 0.4rem 1rem;
          border-radius: 2rem;
          font-size: 0.85rem;
          font-weight: 600;
        }

        .offering-card h2 {
          font-size: 1.9rem;
          color: var(--primary-burgundy);
          margin-bottom: 0.5rem;
        }

        .duration {
          font-size: 0.95rem;
          color: var(--neutral-warm-gray);
          font-weight: 500;
          margin-bottom: 1.5rem;
        }

        .tagline {
          font-size: 1.1rem;
          color: var(--primary-wine);
          font-weight: 500;
          margin-bottom: 1rem;
          line-height: 1.5;
        }

        .description {
          font-size: 1rem;
          line-height: 1.7;
          color: var(--neutral-charcoal);
          margin-bottom: 1.5rem;
        }

        .ideal-for {
          background: var(--neutral-cream);
          padding: 1.25rem;
          border-radius: 0.5rem;
          margin-bottom: 1.5rem;
        }

        .ideal-for h4 {
          font-size: 0.95rem;
          color: var(--primary-burgundy);
          margin-bottom: 0.5rem;
          font-weight: 600;
        }

        .ideal-for p {
          font-size: 0.95rem;
          color: var(--neutral-charcoal);
          margin: 0;
          line-height: 1.6;
        }

        .features {
          margin-bottom: 1.5rem;
        }

        .features h4 {
          font-size: 0.95rem;
          color: var(--primary-wine);
          margin-bottom: 0.75rem;
          font-weight: 600;
        }

        .features ul {
          list-style: none;
          padding: 0;
        }

        .features li {
          padding: 0.4rem 0;
          padding-left: 1.5rem;
          position: relative;
          font-size: 0.95rem;
          color: var(--neutral-charcoal);
        }

        .features li::before {
          content: '✓';
          position: absolute;
          left: 0;
          color: var(--accent-terracotta);
          font-weight: 700;
        }

        .price {
          font-size: 1.4rem;
          font-weight: 700;
          color: var(--primary-burgundy);
          margin-bottom: 1.5rem;
        }

        /* How to Choose */
        .how-to-choose {
          background: var(--neutral-cream);
          padding: 5rem 0;
          text-align: center;
        }

        .how-to-choose h2 {
          margin-bottom: 1.5rem;
        }

        .choose-intro {
          font-size: 1.15rem;
          color: var(--neutral-warm-gray);
          margin-bottom: 2.5rem;
          line-height: 1.7;
        }

        .choose-cta {
          display: flex;
          justify-content: center;
        }
      `}</style>
    </>
  );
}
