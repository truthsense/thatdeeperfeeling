'use client';

import Accordion from '@/components/ui/Accordion';

export default function FAQPage() {
  const faqItems = [
    {
      question: 'What is the difference between coaching and therapy?',
      answer:
        'Coaching is future-focused, action-oriented work that helps you achieve specific goals around intimacy, pleasure, and power dynamics. Therapy focuses on diagnosing and treating mental health conditions. I am a coach, not a therapist. If you have untreated PTSD or active mental health crises, I will refer you to appropriate trauma therapy resources.',
    },
    {
      question: 'What does a typical session look like?',
      answer:
        'Sessions blend conversation, somatic practices, and embodied exploration. We might work with breath, movement, or guided visualization. You\'ll always have full agency over what you explore and how deep we go. Sessions are conducted over Zoom (or in-person for Into the Embers gatherings).',
    },
    {
      question: 'Is this work only for people interested in BDSM?',
      answer:
        'No. While I specialize in conscious kink and power dynamics, many clients come to explore broader themes: reclaiming pleasure after trauma, deepening intimacy, embodying sovereignty, or healing self-sacrifice patterns. You don\'t need to identify as kinky to benefit from this work.',
    },
    {
      question: 'How do I know which container is right for me?',
      answer:
        'Book a free consultation and we\'ll explore your goals together. Return to Power is ideal for deep, sustained transformation. Edgewalker works well for focused exploration of a specific edge. Sacred Eruption is perfect for addressing a single block or breakthrough. I\'ll help you choose what feels most aligned.',
    },
    {
      question: 'What if I\'ve experienced sexual trauma?',
      answer:
        'I work with many trauma survivors. This work is trauma-informed, which means we honor your nervous system, pacing, and boundaries. We move at the speed of safety. If you have untreated PTSD or need trauma therapy, I\'ll refer you to appropriate resources and we can coordinate care if desired.',
    },
    {
      question: 'Is my information kept confidential?',
      answer:
        'Yes. Everything we discuss is held in complete confidence, except in cases where there is imminent risk of harm to yourself or others (as required by law). I do not share client information, testimonials, or details without explicit written consent.',
    },
    {
      question: 'What is your cancellation and refund policy?',
      answer:
        'You can cancel or reschedule sessions with 48 hours notice. Sessions cancelled with less than 48 hours notice will be forfeited. For multi-month containers, refunds are available on a prorated basis within the first 30 days. After 30 days, no refunds are offered, but we can pause your container if needed.',
    },
    {
      question: 'Do you work with couples?',
      answer:
        'Yes, I work with couples exploring conscious kink, power dynamics, communication, and intimacy. Couples work follows the same containers (Return to Power, Edgewalker) with sessions structured for both partners. Pricing for couples work is 1.5x the individual rate.',
    },
    {
      question: 'Are you LGBTQ+ affirming?',
      answer:
        'Absolutely. I work with clients of all genders, sexual orientations, and relationship structures. This work is queer-affirming, poly-friendly, and deeply respectful of alternative relationship dynamics.',
    },
    {
      question: 'What if I\'m not sure I\'m ready?',
      answer:
        'That\'s completely normal. Book a consultation—there\'s no pressure to commit. We\'ll talk through your hesitations, answer questions, and you can take all the time you need to decide if this work feels right for you.',
    },
    {
      question: 'How do I pay for sessions?',
      answer:
        'Payment is processed securely through Stripe. You can pay with credit card, debit card, or bank transfer. Payment plans are available for Return to Power and Edgewalker containers.',
    },
    {
      question: 'What happens after I book a consultation?',
      answer:
        'After booking, you\'ll receive a confirmation email with a Zoom link and a brief intake form. The consultation is 60 minutes, and we\'ll use that time to explore your goals, answer questions, and determine if we\'re a good fit. There\'s no obligation to continue after the consultation.',
    },
  ];

  return (
    <>
      <section className="faq-hero">
        <div className="container content-container">
          <h1>Frequently Asked Questions</h1>
          <p className="hero-subtitle">
            Everything you need to know about working together, policies, and getting started.
          </p>
        </div>
      </section>

      <section className="faq-content">
        <div className="container content-container">
          <Accordion items={faqItems} />
        </div>
      </section>

      <section className="faq-cta">
        <div className="container content-container centered">
          <h2>Still Have Questions?</h2>
          <p>
            Book a free consultation or send me a message. I\'m here to answer anything that\'s on your mind.
          </p>
          <div className="cta-buttons">
            <a href="/consult" className="btn btn-primary">
              Schedule Consultation
            </a>
            <a href="/contact" className="btn btn-secondary">
              Send a Message
            </a>
          </div>
        </div>
      </section>

      <style jsx>{`
        .faq-hero {
          background: linear-gradient(135deg, var(--neutral-cream) 0%, var(--secondary-warm-beige) 100%);
          padding: 5rem 1.5rem 4rem;
          text-align: center;
        }

        .faq-hero h1 {
          font-size: clamp(2.5rem, 5vw, 4rem);
          margin-bottom: 1.5rem;
        }

        .hero-subtitle {
          font-size: clamp(1.1rem, 2vw, 1.3rem);
          color: var(--neutral-warm-gray);
          line-height: 1.7;
        }

        .faq-content {
          background: var(--neutral-soft-white);
          padding: 5rem 0;
        }

        .faq-cta {
          background: var(--neutral-cream);
          padding: 5rem 0;
        }

        .centered {
          text-align: center;
        }

        .faq-cta h2 {
          margin-bottom: 1rem;
        }

        .faq-cta p {
          font-size: 1.15rem;
          color: var(--neutral-warm-gray);
          margin-bottom: 2.5rem;
          line-height: 1.7;
        }

        .cta-buttons {
          display: flex;
          gap: 1rem;
          justify-content: center;
          flex-wrap: wrap;
        }
      `}</style>
    </>
  );
}
