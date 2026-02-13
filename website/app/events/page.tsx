'use client';

import Button from '@/components/ui/Button';
import Image from 'next/image';

export default function EventsPage() {
  return (
    <>
      {/* Hero Section */}
      <section className="retreat-hero">
        <div className="container content-container">
          <h1>Reclaiming the Forbidden</h1>
          <p className="hero-tagline">
            Where Sensuality, Soul &amp; Surrender Meet
          </p>
          <div className="hero-details">
            <p className="hero-date">May 8&ndash;10, 2026</p>
            <p className="hero-location">St. George, Utah</p>
          </div>
          <p className="hero-hook">
            If being a &ldquo;good girl&rdquo; kept you safe&hellip; but somewhere along the way you lost pieces of yourself&hellip;
          </p>
          <p className="hero-declaration">This weekend is for you.</p>
          <Button href="/consult" variant="primary">
            Reserve Your Spot
          </Button>
        </div>
      </section>

      {/* About the Retreat */}
      <section className="retreat-about">
        <div className="container content-container">
          <div className="about-layout">
            <div className="about-inner">
              <h2>About the Retreat</h2>
              <p>
                Reclaiming the Forbidden is a 3-day immersive retreat for women navigating life after high-demand religion, rigid belief systems, or identities that required self-erasure to belong.
              </p>
              <p className="emphasis-line">This isn&rsquo;t about burning everything down.</p>
              <p className="emphasis-line">And it&rsquo;s not about performing rebellion.</p>
              <p>
                It&rsquo;s about reclaiming yourself &mdash; slowly, intentionally, on your terms.
              </p>
              <p>
                Over the weekend we explore embodiment, internal authority, shame untangling, and what it means to walk the third path between obedience and chaos.
              </p>
              <p>This work is grounded, contained, and deeply intentional.</p>
              <p className="emphasis-line">Nothing is forced.</p>
              <p className="emphasis-line">Everything is optional.</p>
            </div>
            <div className="about-image">
              <Image
                src="/images/retreat-views.jpeg"
                alt="Desert mountain views from the retreat venue"
                width={600}
                height={400}
                className="section-photo"
              />
            </div>
          </div>
        </div>
      </section>

      {/* What We'll Explore */}
      <section className="retreat-explore">
        <div className="container content-container">
          <h2>What We&rsquo;ll Explore</h2>
          <ul className="explore-list">
            <li>Embodiment &amp; somatic awareness</li>
            <li>Untangling shame from identity</li>
            <li>Reclaiming internal authority</li>
            <li>Eros as life force (not performance)</li>
            <li>The &ldquo;two-degree shift&rdquo; toward sovereignty</li>
          </ul>
          <p className="explore-note">
            Through guided teaching, somatic movement, group dialogue, ritual, and intentional connection, you&rsquo;ll experience reclamation in a way that is embodied, clear, and sustainable.
          </p>
        </div>
      </section>

      {/* Retreat Flow */}
      <section className="retreat-flow">
        <div className="container content-container">
          <h2>Retreat Flow</h2>
          <div className="flow-grid">
            <div className="flow-day">
              <h3>Friday Evening</h3>
              <p>Opening ceremony and container agreements</p>
              <p>Followed by a nostalgic dance party &mdash; slumber party energy, music, laughter, movement</p>
            </div>
            <div className="flow-day">
              <h3>Saturday</h3>
              <ul>
                <li>Nourishing breakfast</li>
                <li>Somatic embodiment session with guest facilitator Sommer (S-Factor + trauma-informed somatics)</li>
                <li>Guided frameworks and integration</li>
                <li>Intentional lunch</li>
                <li>High-end sit-down dinner</li>
                <li>Evening connection and slumber-party-style gathering</li>
              </ul>
            </div>
            <div className="flow-day">
              <h3>Sunday</h3>
              <ul>
                <li>Grounded integration</li>
                <li>Closing ceremony</li>
                <li>Departure by midday</li>
              </ul>
            </div>
          </div>
          <div className="flow-images">
            <Image
              src="/images/retreat-gathering.jpeg"
              alt="Spacious gathering area with comfortable seating"
              width={600}
              height={400}
              className="section-photo"
            />
            <Image
              src="/images/retreat-lounge.jpeg"
              alt="Lounge area with desert views and sunset light"
              width={600}
              height={400}
              className="section-photo"
            />
          </div>
        </div>
      </section>

      {/* Location */}
      <section className="retreat-location">
        <div className="container content-container">
          <h2>Location</h2>
          <p>Hosted in a private luxury home in St. George, Utah.</p>
          <p className="location-features">
            Desert views. Pool. Firepit. Spacious gathering areas.
          </p>
          <div className="location-gallery">
            <Image
              src="/images/retreat-rear.jpg"
              alt="Private luxury retreat home with pool at sunset"
              width={800}
              height={600}
              className="location-photo-hero"
            />
            <div className="location-gallery-row">
              <Image
                src="/images/retreat-pool.jpg"
                alt="Pool with rock waterfall feature at sunset"
                width={600}
                height={400}
                className="section-photo"
              />
              <Image
                src="/images/retreat-hottub.jpg"
                alt="Rooftop patio with fire pit and hot tub"
                width={600}
                height={400}
                className="section-photo"
              />
            </div>
          </div>
          <p className="location-note">Exact address provided upon registration.</p>
        </div>
      </section>

      {/* Investment */}
      <section className="retreat-investment">
        <div className="container content-container">
          <div className="investment-inner">
            <h2>Investment</h2>

            <div className="price-card">
              <h3>Retreat Ticket: $1,200</h3>
              <div className="includes">
                <h4>Includes:</h4>
                <ul>
                  <li>Full weekend programming (Friday&ndash;Sunday)</li>
                  <li>Saturday hot breakfast &amp; lunch and a sit-down 5-course meal made by a private chef</li>
                  <li>Sunday breakfast</li>
                  <li>Friday evening refreshments</li>
                </ul>
              </div>
              <div className="dining-image">
                <Image
                  src="/images/retreat-dining.png"
                  alt="Elegant dining area set for a private chef dinner"
                  width={600}
                  height={400}
                  className="section-photo"
                />
              </div>
            </div>

            <div className="deposit-card">
              <h3>Payment &amp; Deposit Structure</h3>
              <div className="deposit-highlight">
                <p className="deposit-amount">$500 non-refundable deposit to reserve your spot</p>
              </div>
              <ul className="deposit-details">
                <li>Remaining balance due by <strong>April 1, 2026</strong></li>
                <li>Payment plans available at checkout</li>
                <li>All balances must be paid in full by <strong>April 1, 2026</strong></li>
              </ul>
            </div>

            <div className="accommodation-card">
              <h3>On-Site Lodging (Separate Purchase)</h3>
              <p className="lodging-note">Lodging is optional and purchased separately from your retreat ticket.</p>
              <ul>
                <li><strong>Premium King Suites</strong> &mdash; Single &amp; Double Occupancy</li>
                <li><strong>&ldquo;Slumber Party&rdquo; Bunk Room</strong> option for group bookings</li>
              </ul>
            </div>

            <div className="policy-card">
              <p>
                Due to the intimate and curated nature of this retreat, all payments are non-refundable. If you are unable to attend, you may transfer your ticket to another eligible woman with prior approval.
              </p>
            </div>

            <p className="limited-note">Limited to 20&ndash;25 women.</p>

            <Button href="/consult" variant="primary">
              Reserve Your Spot
            </Button>
          </div>
        </div>
      </section>

      {/* Is This For You */}
      <section className="retreat-for-you">
        <div className="container content-container">
          <h2>Is This For You?</h2>
          <p className="for-you-intro">This retreat may be for you if:</p>
          <ul className="for-you-list">
            <li>You&rsquo;re deconstructing or have left a high-demand religion</li>
            <li>You&rsquo;re tired of performing &ldquo;goodness&rdquo;</li>
            <li>You want to reconnect with your body without losing yourself</li>
            <li>You crave community without hierarchy</li>
            <li>You&rsquo;re ready for reclamation &mdash; not reaction</li>
          </ul>
          <p className="for-you-closing">
            If something in your body softened reading this&hellip;<br />
            this may be your invitation.
          </p>
          <Button href="/consult" variant="primary">
            Apply or Register
          </Button>
        </div>
      </section>

      {/* FAQ */}
      <section className="retreat-faq">
        <div className="container content-container">
          <h2>Frequently Asked Questions</h2>
          <div className="faq-list">

            <div className="faq-item">
              <h3>Who is this retreat for?</h3>
              <p>
                This retreat is for women navigating life after high-demand religion, rigid belief systems, or identities that required self-erasure to belong.
              </p>
              <p>
                It&rsquo;s for women who feel ready to explore embodiment, internal authority, and reclamation in a contained, intentional environment.
              </p>
              <p>
                You do not need to identify with any specific religion to attend. The common thread is untangling obedience culture and reconnecting to yourself.
              </p>
            </div>

            <div className="faq-item">
              <h3>Is this retreat religious?</h3>
              <p>No. This is not a religious retreat.</p>
              <p>
                While many attendees may be deconstructing from religious systems, this space is not anti-religion, anti-faith, or centered on debate. It is centered on personal sovereignty and embodied reclamation.
              </p>
            </div>

            <div className="faq-item">
              <h3>Is this a kink retreat?</h3>
              <p>No.</p>
              <p>
                Conscious kink is one modality Kimberly works with in her broader practice, but participation in kink-related exploration is not required and is not the focus of this retreat.
              </p>
              <p>
                All practices are optional. This weekend centers on embodiment, personal authority, and contained exploration.
              </p>
            </div>

            <div className="faq-item">
              <h3>What does &ldquo;embodiment&rdquo; mean in this context?</h3>
              <p>
                Embodiment means reconnecting with your body as a source of wisdom rather than something to control or override.
              </p>
              <p>
                You will be guided through somatic practices, movement, breathwork, and reflective exercises. Nothing is forced. You participate at your own pace.
              </p>
            </div>

            <div className="faq-item">
              <h3>Will there be nudity?</h3>
              <p>No nudity is required.</p>
              <p>
                Participants are invited to dress in ways that feel expressive and comfortable, but all exercises are structured to maintain personal choice and autonomy.
              </p>
            </div>

            <div className="faq-item">
              <h3>I feel nervous. Is that normal?</h3>
              <p>Yes.</p>
              <p>
                Many women attending will be stepping outside familiar belief systems or roles. Nervousness is common and welcomed.
              </p>
              <p>You are never required to share more than you want to share.</p>
            </div>

            <div className="faq-item">
              <h3>What if I become emotionally overwhelmed?</h3>
              <p>Emotional responses are normal in spaces of reclamation.</p>
              <p>
                There will be structured support throughout the weekend, and you are always allowed to step out, pause, or take space as needed.
              </p>
              <p>This is not therapy, but it is a thoughtfully facilitated container.</p>
            </div>

            <div className="faq-item">
              <h3>What is included in the base ticket?</h3>
              <p>The base ticket includes:</p>
              <ul>
                <li>Full weekend programming (Friday evening through Sunday midday)</li>
                <li>Saturday breakfast and lunch</li>
                <li>Saturday sit-down dinner</li>
                <li>Sunday breakfast</li>
                <li>Friday evening light refreshments</li>
              </ul>
              <p>Accommodation is separate and optional.</p>
            </div>

            <div className="faq-item">
              <h3>Can I stay on-site?</h3>
              <p>Yes.</p>
              <p>Limited on-site accommodations are available:</p>
              <ul>
                <li>Premium King Suites (single or double occupancy)</li>
                <li>&ldquo;Slumber Party&rdquo; Bunk Room option for group bookings</li>
              </ul>
              <p>On-site spots are limited and available on a first-come basis.</p>
            </div>

            <div className="faq-item">
              <h3>Do you offer payment plans?</h3>
              <p>Yes. Payment plans are available at checkout.</p>
            </div>

            <div className="faq-item">
              <h3>What is your cancellation policy?</h3>
              <p>
                Due to the intimate and curated nature of this retreat, all payments are non-refundable.
              </p>
              <p>
                If you are unable to attend, you may transfer your ticket to another eligible woman with prior approval.
              </p>
            </div>

            <div className="faq-item">
              <h3>What kind of space is this?</h3>
              <p>
                This retreat is built on mutual respect, personal responsibility, and contained exploration.
              </p>
              <p>We gather without hierarchy, without persuasion, and without pressure.</p>
              <p>
                There is no agenda to convert, convince, or dismantle anyone&rsquo;s beliefs. Each woman is responsible for her own process and pace.
              </p>
              <p>
                We honor different stories, different stages of deconstruction, and different relationships to faith, sexuality, and identity.
              </p>
              <p>
                This is a space for permission &mdash; permission to feel, to question, to soften, to expand, and to come home to yourself in your own time.
              </p>
            </div>

          </div>
        </div>
      </section>

      <style jsx>{`
        /* Hero */
        .retreat-hero {
          background: linear-gradient(135deg, var(--primary-burgundy) 0%, var(--primary-wine) 100%);
          color: var(--neutral-soft-white);
          padding: 6rem 1.5rem 5rem;
          text-align: center;
        }

        .retreat-hero h1 {
          color: var(--neutral-soft-white);
          font-size: clamp(2.5rem, 5vw, 4rem);
          margin-bottom: 0.5rem;
        }

        .hero-tagline {
          font-size: clamp(1.1rem, 2.2vw, 1.5rem);
          color: var(--neutral-cream);
          font-style: italic;
          margin-bottom: 2rem;
        }

        .hero-details {
          margin-bottom: 2.5rem;
        }

        .hero-date {
          font-size: 1.2rem;
          font-weight: 600;
          color: var(--neutral-soft-white);
          margin-bottom: 0.25rem;
          letter-spacing: 0.05em;
        }

        .hero-location {
          font-size: 1.1rem;
          color: var(--neutral-cream);
          margin: 0;
        }

        .hero-hook {
          font-size: clamp(1.05rem, 2vw, 1.25rem);
          color: var(--neutral-cream);
          max-width: 600px;
          margin: 0 auto 1rem;
          line-height: 1.7;
        }

        .hero-declaration {
          font-size: clamp(1.2rem, 2.5vw, 1.5rem);
          font-weight: 600;
          color: var(--neutral-soft-white);
          margin-bottom: 2.5rem;
          font-family: var(--font-heading);
        }

        /* About */
        .retreat-about {
          background: var(--neutral-soft-white);
          padding: 5rem 0;
        }

        .about-layout {
          display: grid;
          grid-template-columns: 1fr;
          gap: 3rem;
          align-items: center;
        }

        @media (min-width: 768px) {
          .about-layout {
            grid-template-columns: 1.2fr 1fr;
            gap: 4rem;
          }
        }

        .about-inner {
          max-width: 700px;
        }

        .about-image {
          display: flex;
          justify-content: center;
        }

        .retreat-about h2 {
          font-size: clamp(2rem, 4vw, 3rem);
          margin-bottom: 2rem;
        }

        @media (max-width: 767px) {
          .retreat-about h2 {
            text-align: center;
          }
        }

        .retreat-about p {
          font-size: 1.15rem;
          line-height: 1.8;
          color: var(--neutral-charcoal);
          margin-bottom: 1.25rem;
        }

        .emphasis-line {
          font-style: italic;
          color: var(--primary-burgundy) !important;
          font-weight: 500;
        }

        /* Section photos */
        :global(.section-photo) {
          border-radius: 0.75rem;
          box-shadow: 0 10px 30px rgba(139, 58, 71, 0.15);
          object-fit: cover;
          width: 100%;
          height: auto;
        }

        :global(.location-photo-hero) {
          border-radius: 0.75rem;
          box-shadow: 0 15px 40px rgba(0, 0, 0, 0.25);
          object-fit: cover;
          width: 100%;
          height: auto;
        }

        /* Explore */
        .retreat-explore {
          background: var(--neutral-cream);
          padding: 5rem 0;
        }

        .retreat-explore h2 {
          text-align: center;
          font-size: clamp(2rem, 4vw, 3rem);
          margin-bottom: 2.5rem;
        }

        .explore-list {
          list-style: none;
          padding: 0;
          max-width: 550px;
          margin: 0 auto 2.5rem;
        }

        .explore-list li {
          padding: 0.75rem 0;
          padding-left: 2rem;
          position: relative;
          font-size: 1.15rem;
          color: var(--neutral-charcoal);
        }

        .explore-list li::before {
          content: '•';
          position: absolute;
          left: 0;
          color: var(--accent-terracotta);
          font-size: 1.5rem;
          line-height: 1;
        }

        .explore-note {
          text-align: center;
          font-size: 1.1rem;
          line-height: 1.8;
          color: var(--neutral-warm-gray);
          max-width: 650px;
          margin: 0 auto;
          font-style: italic;
        }

        /* Retreat Flow */
        .retreat-flow {
          background: var(--neutral-soft-white);
          padding: 5rem 0;
        }

        .retreat-flow h2 {
          text-align: center;
          font-size: clamp(2rem, 4vw, 3rem);
          margin-bottom: 3rem;
        }

        .flow-grid {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          gap: 2rem;
          max-width: 900px;
          margin: 0 auto;
        }

        .flow-day {
          background: var(--neutral-cream);
          padding: 2rem;
          border-radius: 0.75rem;
          border-top: 3px solid var(--accent-terracotta);
        }

        .flow-day h3 {
          font-size: 1.35rem;
          color: var(--primary-burgundy);
          margin-bottom: 1rem;
        }

        .flow-day p {
          font-size: 1.05rem;
          line-height: 1.7;
          color: var(--neutral-charcoal);
          margin-bottom: 0.75rem;
        }

        .flow-day ul {
          list-style: none;
          padding: 0;
        }

        .flow-day ul li {
          padding: 0.5rem 0;
          padding-left: 1.5rem;
          position: relative;
          font-size: 1.05rem;
          color: var(--neutral-charcoal);
          line-height: 1.6;
        }

        .flow-day ul li::before {
          content: '•';
          position: absolute;
          left: 0;
          color: var(--accent-terracotta);
          font-size: 1.25rem;
          line-height: 1;
        }

        .flow-images {
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 2rem;
          max-width: 900px;
          margin: 3rem auto 0;
        }

        @media (max-width: 768px) {
          .flow-grid {
            grid-template-columns: 1fr;
          }
          .flow-images {
            grid-template-columns: 1fr;
          }
        }

        /* Location */
        .retreat-location {
          background: linear-gradient(135deg, var(--primary-wine) 0%, var(--primary-burgundy) 100%);
          color: var(--neutral-soft-white);
          padding: 5rem 0;
          text-align: center;
        }

        .retreat-location h2 {
          color: var(--neutral-soft-white);
          font-size: clamp(2rem, 4vw, 3rem);
          margin-bottom: 1.5rem;
        }

        .retreat-location p {
          font-size: 1.15rem;
          color: var(--neutral-cream);
          margin-bottom: 0.75rem;
        }

        .location-features {
          font-weight: 500;
          font-size: 1.2rem !important;
          color: var(--neutral-soft-white) !important;
          letter-spacing: 0.02em;
        }

        .location-gallery {
          max-width: 900px;
          margin: 2.5rem auto;
        }

        .location-gallery-row {
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 1.5rem;
          margin-top: 1.5rem;
        }

        @media (max-width: 768px) {
          .location-gallery-row {
            grid-template-columns: 1fr;
          }
        }

        .location-note {
          font-style: italic;
          font-size: 1rem !important;
          margin-top: 0;
        }

        /* Investment */
        .retreat-investment {
          background: var(--neutral-cream);
          padding: 5rem 0;
        }

        .investment-inner {
          max-width: 650px;
          margin: 0 auto;
          text-align: center;
        }

        .retreat-investment h2 {
          font-size: clamp(2rem, 4vw, 3rem);
          margin-bottom: 2.5rem;
        }

        .price-card {
          background: white;
          padding: 2.5rem;
          border-radius: 0.75rem;
          box-shadow: 0 10px 40px rgba(139, 58, 71, 0.1);
          margin-bottom: 2rem;
          text-align: left;
        }

        .price-card h3 {
          font-size: 1.5rem;
          color: var(--primary-burgundy);
          margin-bottom: 1.5rem;
          text-align: center;
        }

        .includes h4 {
          font-size: 1.1rem;
          color: var(--neutral-charcoal);
          margin-bottom: 0.75rem;
          font-weight: 600;
        }

        .includes ul,
        .accommodation-card ul {
          list-style: none;
          padding: 0;
        }

        .includes ul li,
        .accommodation-card ul li {
          padding: 0.5rem 0;
          padding-left: 1.5rem;
          position: relative;
          font-size: 1.05rem;
          color: var(--neutral-charcoal);
          line-height: 1.6;
        }

        .includes ul li::before,
        .accommodation-card ul li::before {
          content: '•';
          position: absolute;
          left: 0;
          color: var(--accent-terracotta);
          font-size: 1.25rem;
          line-height: 1;
        }

        .dining-image {
          margin-top: 1.5rem;
        }

        .deposit-card {
          background: white;
          padding: 2.5rem;
          border-radius: 0.75rem;
          box-shadow: 0 10px 40px rgba(139, 58, 71, 0.1);
          margin-bottom: 2rem;
          text-align: left;
          border-top: 3px solid var(--accent-terracotta);
        }

        .deposit-card h3 {
          font-size: 1.35rem;
          color: var(--primary-burgundy);
          margin-bottom: 1.5rem;
          text-align: center;
        }

        .deposit-highlight {
          background: var(--neutral-cream);
          padding: 1.25rem 1.5rem;
          border-radius: 0.5rem;
          margin-bottom: 1.5rem;
          text-align: center;
        }

        .deposit-amount {
          font-size: 1.15rem;
          font-weight: 600;
          color: var(--primary-burgundy);
          margin: 0;
        }

        .deposit-details {
          list-style: none;
          padding: 0;
        }

        .deposit-details li {
          padding: 0.5rem 0;
          padding-left: 1.5rem;
          position: relative;
          font-size: 1.05rem;
          color: var(--neutral-charcoal);
          line-height: 1.6;
        }

        .deposit-details li::before {
          content: '•';
          position: absolute;
          left: 0;
          color: var(--accent-terracotta);
          font-size: 1.25rem;
          line-height: 1;
        }

        .accommodation-card {
          background: white;
          padding: 2rem 2.5rem;
          border-radius: 0.75rem;
          box-shadow: 0 10px 40px rgba(139, 58, 71, 0.1);
          margin-bottom: 2rem;
          text-align: left;
        }

        .accommodation-card h3 {
          font-size: 1.25rem;
          color: var(--primary-burgundy);
          margin-bottom: 0.75rem;
        }

        .lodging-note {
          font-size: 0.95rem;
          color: var(--neutral-warm-gray);
          font-style: italic;
          margin-bottom: 1rem;
        }

        .policy-card {
          background: var(--neutral-soft-white);
          padding: 1.5rem 2rem;
          border-radius: 0.5rem;
          margin-bottom: 2rem;
          border-left: 3px solid var(--secondary-taupe);
        }

        .policy-card p {
          font-size: 0.95rem;
          color: var(--neutral-warm-gray);
          line-height: 1.7;
          margin: 0;
          text-align: left;
        }

        .limited-note {
          font-weight: 600;
          font-size: 1.1rem;
          color: var(--primary-burgundy);
          margin-bottom: 2rem;
        }

        /* Is This For You */
        .retreat-for-you {
          background: var(--neutral-soft-white);
          padding: 5rem 0;
          text-align: center;
        }

        .retreat-for-you h2 {
          font-size: clamp(2rem, 4vw, 3rem);
          margin-bottom: 1.5rem;
        }

        .for-you-intro {
          font-size: 1.15rem;
          color: var(--neutral-charcoal);
          margin-bottom: 2rem;
        }

        .for-you-list {
          list-style: none;
          padding: 0;
          max-width: 550px;
          margin: 0 auto 2.5rem;
          text-align: left;
        }

        .for-you-list li {
          padding: 0.75rem 0;
          padding-left: 2rem;
          position: relative;
          font-size: 1.1rem;
          color: var(--neutral-charcoal);
          line-height: 1.6;
        }

        .for-you-list li::before {
          content: '•';
          position: absolute;
          left: 0;
          color: var(--accent-terracotta);
          font-size: 1.5rem;
          line-height: 1;
        }

        .for-you-closing {
          font-size: 1.15rem;
          font-style: italic;
          color: var(--primary-burgundy);
          line-height: 1.8;
          margin-bottom: 2.5rem;
        }

        /* FAQ */
        .retreat-faq {
          background: var(--neutral-cream);
          padding: 5rem 0;
        }

        .retreat-faq h2 {
          text-align: center;
          font-size: clamp(2rem, 4vw, 3rem);
          margin-bottom: 3rem;
        }

        .faq-list {
          max-width: 700px;
          margin: 0 auto;
        }

        .faq-item {
          background: white;
          padding: 2rem 2.5rem;
          border-radius: 0.75rem;
          margin-bottom: 1.5rem;
          box-shadow: 0 4px 20px rgba(139, 58, 71, 0.08);
        }

        .faq-item h3 {
          font-size: 1.2rem;
          color: var(--primary-burgundy);
          margin-bottom: 1rem;
        }

        .faq-item p {
          font-size: 1.05rem;
          line-height: 1.7;
          color: var(--neutral-charcoal);
          margin-bottom: 0.75rem;
        }

        .faq-item p:last-child {
          margin-bottom: 0;
        }

        .faq-item ul {
          list-style: none;
          padding: 0;
          margin-bottom: 0.75rem;
        }

        .faq-item ul li {
          padding: 0.4rem 0;
          padding-left: 1.5rem;
          position: relative;
          font-size: 1.05rem;
          color: var(--neutral-charcoal);
          line-height: 1.6;
        }

        .faq-item ul li::before {
          content: '•';
          position: absolute;
          left: 0;
          color: var(--accent-terracotta);
          font-size: 1.25rem;
          line-height: 1;
        }
      `}</style>
    </>
  );
}
