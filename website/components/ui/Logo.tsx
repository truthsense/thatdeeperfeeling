interface LogoProps {
  variant?: 'full' | 'mark' | 'wordmark';
  className?: string;
}

export default function Logo({ variant = 'full', className = '' }: LogoProps) {
  if (variant === 'mark') {
    // Icon/mark only - stylized flame/spiral design
    return (
      <svg
        className={className}
        width="40"
        height="40"
        viewBox="0 0 40 40"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        aria-label="That Deeper Feeling logo mark"
      >
        <path
          d="M20 5C20 5 15 12 15 18C15 21.866 18.134 25 22 25C25.866 25 29 21.866 29 18C29 12 24 5 24 5C24 5 26.5 11 26.5 15.5C26.5 17.985 24.485 20 22 20C19.515 20 17.5 17.985 17.5 15.5C17.5 11 20 5 20 5Z"
          fill="var(--primary-burgundy)"
        />
        <path
          d="M22 25C22 25 19 28 19 31C19 33.209 20.791 35 23 35C25.209 35 27 33.209 27 31C27 28 24 25 24 25C24 25 25 27 25 29C25 30.105 24.105 31 23 31C21.895 31 21 30.105 21 29C21 27 22 25 22 25Z"
          fill="var(--accent-terracotta)"
        />
        <circle cx="20" cy="20" r="19" stroke="var(--primary-burgundy)" strokeWidth="2" opacity="0.2"/>
      </svg>
    );
  }

  if (variant === 'wordmark') {
    // Text only
    return (
      <div className={`logo-wordmark ${className}`}>
        <span style={{
          fontFamily: 'var(--font-heading)',
          fontSize: '1.5rem',
          fontWeight: 600,
          color: 'var(--primary-burgundy)'
        }}>
          That Deeper Feeling
        </span>
      </div>
    );
  }

  // Full logo - mark + wordmark
  return (
    <div className={`logo-full ${className}`} style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
      <svg
        width="40"
        height="40"
        viewBox="0 0 40 40"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        aria-label="That Deeper Feeling logo"
      >
        <path
          d="M20 5C20 5 15 12 15 18C15 21.866 18.134 25 22 25C25.866 25 29 21.866 29 18C29 12 24 5 24 5C24 5 26.5 11 26.5 15.5C26.5 17.985 24.485 20 22 20C19.515 20 17.5 17.985 17.5 15.5C17.5 11 20 5 20 5Z"
          fill="var(--primary-burgundy)"
        />
        <path
          d="M22 25C22 25 19 28 19 31C19 33.209 20.791 35 23 35C25.209 35 27 33.209 27 31C27 28 24 25 24 25C24 25 25 27 25 29C25 30.105 24.105 31 23 31C21.895 31 21 30.105 21 29C21 27 22 25 22 25Z"
          fill="var(--accent-terracotta)"
        />
        <circle cx="20" cy="20" r="19" stroke="var(--primary-burgundy)" strokeWidth="2" opacity="0.2"/>
      </svg>
      <div style={{ display: 'flex', flexDirection: 'column', gap: '0.125rem' }}>
        <span style={{
          fontFamily: 'var(--font-heading)',
          fontSize: '1.25rem',
          fontWeight: 600,
          color: 'var(--primary-burgundy)',
          lineHeight: 1.2
        }}>
          That Deeper Feeling
        </span>
        <span style={{
          fontFamily: 'var(--font-body)',
          fontSize: '0.7rem',
          fontWeight: 400,
          color: 'var(--neutral-warm-gray)',
          fontStyle: 'italic',
          letterSpacing: '0.05em',
          lineHeight: 1
        }}>
          CONSCIOUS INTIMACY COACHING
        </span>
      </div>
    </div>
  );
}
