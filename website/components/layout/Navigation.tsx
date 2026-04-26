'use client';

import Link from 'next/link';
import { useState } from 'react';
import { usePathname } from 'next/navigation';
import Logo from '../ui/Logo';

const navItems = [
  { label: 'Home', href: '/' },
  { label: 'Start Here', href: '/start' },
  { label: 'About', href: '/about' },
  { label: 'Consult', href: '/consult' },
  { label: 'Events', href: '/events' },
  { label: 'Resources', href: '/resources' },
  { label: 'Contact', href: '/contact' },
];

function InstagramIcon() {
  return (
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
      <rect x="2" y="2" width="20" height="20" rx="5" ry="5" />
      <circle cx="12" cy="12" r="4" />
      <circle cx="17.5" cy="6.5" r="0.5" fill="currentColor" stroke="none" />
    </svg>
  );
}

function FacebookIcon() {
  return (
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
      <path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z" />
    </svg>
  );
}

export default function Navigation() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const pathname = usePathname();

  const isActive = (href: string) =>
    href === '/' ? pathname === '/' : pathname.startsWith(href);

  return (
    <nav className="navigation">
      <div className="container">
        <div className="nav-wrapper">
          <Link href="/" className="logo-link" onClick={() => setIsMenuOpen(false)}>
            <Logo variant="wordmark" />
          </Link>

          {/* Desktop nav */}
          <ul className="nav-menu desktop-menu">
            {navItems.map((item) => (
              <li key={item.href}>
                <Link
                  href={item.href}
                  className={`nav-link ${isActive(item.href) ? 'active' : ''}`}
                >
                  {item.label}
                </Link>
              </li>
            ))}
          </ul>

          {/* Desktop social icons */}
          <div className="nav-social desktop-social">
            <a href="https://instagram.com/thatdeeperfeeling" target="_blank" rel="noopener noreferrer" aria-label="Instagram" className="social-icon">
              <InstagramIcon />
            </a>
            <a href="https://www.facebook.com/people/That-Deeper-Feeling/61566488580618/" target="_blank" rel="noopener noreferrer" aria-label="Facebook" className="social-icon">
              <FacebookIcon />
            </a>
          </div>

          {/* Mobile toggle */}
          <button
            className="mobile-menu-toggle"
            onClick={() => setIsMenuOpen(!isMenuOpen)}
            aria-label={isMenuOpen ? 'Close menu' : 'Open menu'}
            aria-expanded={isMenuOpen}
          >
            <span className={`hamburger ${isMenuOpen ? 'open' : ''}`}>
              <span></span>
              <span></span>
              <span></span>
            </span>
          </button>
        </div>
      </div>

      {/* Mobile full-screen overlay */}
      <div className={`mobile-overlay ${isMenuOpen ? 'open' : ''}`} aria-hidden={!isMenuOpen}>
        <ul className="mobile-nav-list">
          {navItems.map((item) => (
            <li key={item.href}>
              <Link
                href={item.href}
                className={`mobile-nav-link ${isActive(item.href) ? 'active' : ''}`}
                onClick={() => setIsMenuOpen(false)}
              >
                {item.label}
              </Link>
            </li>
          ))}
        </ul>
        <div className="mobile-social">
          <a href="https://instagram.com/thatdeeperfeeling" target="_blank" rel="noopener noreferrer" aria-label="Instagram" className="mobile-social-icon">
            <InstagramIcon />
          </a>
          <a href="https://www.facebook.com/people/That-Deeper-Feeling/61566488580618/" target="_blank" rel="noopener noreferrer" aria-label="Facebook" className="mobile-social-icon">
            <FacebookIcon />
          </a>
        </div>
      </div>

      <style jsx>{`
        .navigation {
          position: sticky;
          top: 0;
          background: rgba(253, 252, 249, 0.95);
          border-bottom: 1px solid rgba(139, 58, 71, 0.1);
          z-index: 1000;
          backdrop-filter: blur(10px);
        }

        .nav-wrapper {
          display: flex;
          justify-content: space-between;
          align-items: center;
          padding: 1.25rem 0;
          gap: 1.5rem;
        }

        .logo-link {
          flex-shrink: 0;
          z-index: 1100;
          position: relative;
        }

        /* Desktop nav */
        .desktop-menu {
          display: none;
          list-style: none;
          gap: 2rem;
          align-items: center;
          flex: 1;
          justify-content: center;
        }

        @media (min-width: 900px) {
          .desktop-menu {
            display: flex;
          }
        }

        .nav-link {
          font-family: var(--font-body);
          font-size: 0.95rem;
          font-weight: 400;
          color: var(--neutral-charcoal);
          text-decoration: none;
          position: relative;
          padding-bottom: 2px;
          transition: color 0.2s;
        }

        .nav-link::after {
          content: '';
          position: absolute;
          bottom: -3px;
          left: 0;
          width: 0;
          height: 2px;
          background: var(--accent-terracotta);
          transition: width 0.25s ease;
        }

        .nav-link:hover,
        .nav-link.active {
          color: var(--primary-burgundy);
        }

        .nav-link:hover::after,
        .nav-link.active::after {
          width: 100%;
        }

        /* Desktop social */
        .desktop-social {
          display: none;
          gap: 0.75rem;
          align-items: center;
          flex-shrink: 0;
        }

        @media (min-width: 900px) {
          .desktop-social {
            display: flex;
          }
        }

        .social-icon {
          color: var(--neutral-warm-gray);
          transition: color 0.2s, transform 0.2s;
          display: flex;
          align-items: center;
        }

        .social-icon:hover {
          color: var(--primary-burgundy);
          transform: translateY(-2px);
        }

        /* Mobile toggle */
        .mobile-menu-toggle {
          display: flex;
          background: none;
          border: none;
          cursor: pointer;
          padding: 0.5rem;
          z-index: 1100;
          position: relative;
        }

        @media (min-width: 900px) {
          .mobile-menu-toggle {
            display: none;
          }
        }

        .hamburger {
          display: flex;
          flex-direction: column;
          gap: 5px;
          width: 26px;
        }

        .hamburger span {
          display: block;
          width: 100%;
          height: 2px;
          background: var(--primary-burgundy);
          transition: all 0.3s ease;
          transform-origin: center;
        }

        .hamburger.open span:nth-child(1) {
          transform: rotate(45deg) translate(5px, 5px);
        }

        .hamburger.open span:nth-child(2) {
          opacity: 0;
          transform: scaleX(0);
        }

        .hamburger.open span:nth-child(3) {
          transform: rotate(-45deg) translate(5px, -5px);
        }

        /* Full-screen mobile overlay */
        .mobile-overlay {
          position: fixed;
          inset: 0;
          background: var(--primary-wine);
          z-index: 1050;
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          gap: 0;
          opacity: 0;
          pointer-events: none;
          transition: opacity 0.3s ease;
        }

        .mobile-overlay.open {
          opacity: 1;
          pointer-events: all;
        }

        @media (min-width: 900px) {
          .mobile-overlay {
            display: none;
          }
        }

        .mobile-nav-list {
          list-style: none;
          display: flex;
          flex-direction: column;
          align-items: center;
          gap: 0.25rem;
          margin-bottom: 3rem;
        }

        .mobile-nav-link {
          display: block;
          font-family: var(--font-heading);
          font-size: clamp(1.75rem, 6vw, 2.5rem);
          font-weight: 600;
          color: var(--neutral-cream);
          text-decoration: none;
          padding: 0.6rem 1rem;
          letter-spacing: 0.01em;
          transition: color 0.2s;
          text-align: center;
        }

        .mobile-nav-link:hover,
        .mobile-nav-link.active {
          color: var(--accent-terracotta);
        }

        .mobile-social {
          display: flex;
          gap: 1.5rem;
          align-items: center;
        }

        .mobile-social-icon {
          color: rgba(245, 241, 232, 0.6);
          transition: color 0.2s;
          display: flex;
          align-items: center;
        }

        .mobile-social-icon:hover {
          color: var(--accent-terracotta);
        }
      `}</style>
    </nav>
  );
}
