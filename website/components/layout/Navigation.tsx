'use client';

import Link from 'next/link';
import { useState } from 'react';
import Logo from '../ui/Logo';

export default function Navigation() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const navigationItems = [
    { label: 'Home', href: '/' },
    { label: 'About', href: '/about' },
    { label: 'Offerings', href: '/offerings' },
    { label: 'Consult', href: '/consult' },
    { label: 'Events', href: '/events' },
    { label: 'Resources', href: '/resources' },
    { label: 'Contact', href: '/contact' },
  ];

  return (
    <nav className="navigation">
      <div className="container">
        <div className="nav-wrapper">
          {/* Logo / Brand */}
          <Link href="/" className="logo-link">
            <Logo variant="wordmark" />
          </Link>

          {/* Desktop Navigation */}
          <ul className="nav-menu desktop-menu">
            {navigationItems.map((item) => (
              <li key={item.href}>
                <Link href={item.href} className="nav-link">
                  {item.label}
                </Link>
              </li>
            ))}
          </ul>

          {/* Mobile Menu Toggle */}
          <button
            className="mobile-menu-toggle"
            onClick={() => setIsMenuOpen(!isMenuOpen)}
            aria-label="Toggle menu"
            aria-expanded={isMenuOpen}
          >
            <span className={`hamburger ${isMenuOpen ? 'open' : ''}`}>
              <span></span>
              <span></span>
              <span></span>
            </span>
          </button>
        </div>

        {/* Mobile Navigation */}
        {isMenuOpen && (
          <ul className="nav-menu mobile-menu">
            {navigationItems.map((item) => (
              <li key={item.href}>
                <Link
                  href={item.href}
                  className="nav-link"
                  onClick={() => setIsMenuOpen(false)}
                >
                  {item.label}
                </Link>
              </li>
            ))}
          </ul>
        )}
      </div>

      <style jsx>{`
        .navigation {
          position: sticky;
          top: 0;
          background: var(--neutral-soft-white);
          border-bottom: 1px solid rgba(139, 58, 71, 0.1);
          z-index: 1000;
          backdrop-filter: blur(10px);
          background: rgba(253, 252, 249, 0.95);
        }

        .nav-wrapper {
          display: flex;
          justify-content: space-between;
          align-items: center;
          padding: 1.5rem 0;
        }

        .logo {
          font-family: var(--font-heading);
          font-size: 1.5rem;
          font-weight: 600;
          color: var(--primary-burgundy);
          text-decoration: none;
          transition: color 0.3s ease;
        }

        .logo:hover {
          color: var(--accent-terracotta);
        }

        .logo-text {
          display: inline-block;
        }

        .nav-menu {
          display: flex;
          list-style: none;
          gap: 2.5rem;
          align-items: center;
        }

        .desktop-menu {
          display: none;
        }

        @media (min-width: 768px) {
          .desktop-menu {
            display: flex;
          }
        }

        .nav-link {
          font-family: var(--font-body);
          font-size: 1rem;
          font-weight: 400;
          color: var(--neutral-charcoal);
          text-decoration: none;
          position: relative;
          transition: color 0.3s ease;
        }

        .nav-link::after {
          content: '';
          position: absolute;
          bottom: -5px;
          left: 0;
          width: 0;
          height: 2px;
          background: var(--accent-terracotta);
          transition: width 0.3s ease;
        }

        .nav-link:hover {
          color: var(--primary-burgundy);
        }

        .nav-link:hover::after {
          width: 100%;
        }

        /* Mobile Menu */
        .mobile-menu-toggle {
          display: block;
          background: none;
          border: none;
          cursor: pointer;
          padding: 0.5rem;
        }

        @media (min-width: 768px) {
          .mobile-menu-toggle {
            display: none;
          }
        }

        .hamburger {
          display: flex;
          flex-direction: column;
          gap: 5px;
          width: 28px;
          height: 20px;
        }

        .hamburger span {
          display: block;
          width: 100%;
          height: 2px;
          background: var(--primary-burgundy);
          transition: all 0.3s ease;
        }

        .hamburger.open span:nth-child(1) {
          transform: rotate(45deg) translate(7px, 7px);
        }

        .hamburger.open span:nth-child(2) {
          opacity: 0;
        }

        .hamburger.open span:nth-child(3) {
          transform: rotate(-45deg) translate(7px, -7px);
        }

        .mobile-menu {
          flex-direction: column;
          gap: 1.5rem;
          padding: 2rem 0;
          align-items: flex-start;
          animation: slideDown 0.3s ease;
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

        @media (min-width: 768px) {
          .mobile-menu {
            display: none;
          }
        }
      `}</style>
    </nav>
  );
}
