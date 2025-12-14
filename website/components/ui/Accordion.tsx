'use client';

import { useState } from 'react';

interface AccordionItemProps {
  question: string;
  answer: string;
}

interface AccordionProps {
  items: AccordionItemProps[];
}

export default function Accordion({ items }: AccordionProps) {
  const [openIndex, setOpenIndex] = useState<number | null>(null);

  const toggleItem = (index: number) => {
    setOpenIndex(openIndex === index ? null : index);
  };

  return (
    <div className="accordion">
      {items.map((item, index) => (
        <div key={index} className={`accordion-item ${openIndex === index ? 'open' : ''}`}>
          <button
            className="accordion-question"
            onClick={() => toggleItem(index)}
            aria-expanded={openIndex === index}
          >
            <span>{item.question}</span>
            <span className="accordion-icon">{openIndex === index ? '−' : '+'}</span>
          </button>
          {openIndex === index && (
            <div className="accordion-answer">
              <p>{item.answer}</p>
            </div>
          )}
        </div>
      ))}

      <style jsx>{`
        .accordion {
          display: flex;
          flex-direction: column;
          gap: 1rem;
        }

        .accordion-item {
          background: white;
          border: 2px solid var(--neutral-cream);
          border-radius: 0.75rem;
          overflow: hidden;
          transition: all 0.3s ease;
        }

        .accordion-item.open {
          border-color: var(--primary-burgundy);
        }

        .accordion-question {
          width: 100%;
          text-align: left;
          padding: 1.5rem;
          background: transparent;
          border: none;
          font-family: var(--font-heading);
          font-size: 1.2rem;
          font-weight: 600;
          color: var(--primary-wine);
          cursor: pointer;
          display: flex;
          justify-content: space-between;
          align-items: center;
          transition: color 0.3s ease;
        }

        .accordion-question:hover {
          color: var(--primary-burgundy);
        }

        .accordion-icon {
          font-size: 1.5rem;
          font-weight: 400;
          color: var(--accent-terracotta);
          transition: transform 0.3s ease;
        }

        .accordion-item.open .accordion-icon {
          transform: rotate(180deg);
        }

        .accordion-answer {
          padding: 0 1.5rem 1.5rem;
          animation: slideDown 0.3s ease;
        }

        .accordion-answer p {
          font-size: 1.05rem;
          line-height: 1.7;
          color: var(--neutral-charcoal);
          margin: 0;
        }

        @keyframes slideDown {
          from {
            opacity: 0;
            transform: translateY(-10px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
      `}</style>
    </div>
  );
}
