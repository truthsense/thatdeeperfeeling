/**
 * Shared email templates for the client funnel.
 * Used by both the Stripe webhook (mock mode) and
 * the contract-signed webhook (live mode).
 */

import { Resend } from 'resend';

let resendInstance: Resend | null = null;

function getResend(): Resend {
  if (!resendInstance) {
    resendInstance = new Resend(process.env.RESEND_API_KEY);
  }
  return resendInstance;
}

const FROM = 'That Deeper Feeling <noreply@thatdeeperfeeling.com>';
const KIMBERLY_EMAIL = () =>
  process.env.KIMBERLY_EMAIL || 'kimberly@thatdeeperfeeling.com';
const CALENDLY_URL = () =>
  process.env.CALENDLY_URL || 'https://calendly.com/kimberlymmbryant/that-deeper-feeling';

/**
 * Send the Calendly scheduling link to a client after
 * payment + contract signing (or mock mode skip).
 */
export async function sendCalendlyEmail(
  name: string,
  email: string,
  type: 'curiosity-call' | 'session',
): Promise<void> {
  const resend = getResend();
  const calendlyUrl = CALENDLY_URL();

  const isCuriosity = type === 'curiosity-call';
  const subject = isCuriosity
    ? 'Your Curiosity Call — Schedule Your Session'
    : 'Your Session — Schedule Your Time';
  const heading = isCuriosity ? 'Your Curiosity Call' : 'Your Session';
  const buttonText = isCuriosity
    ? 'Schedule Your Curiosity Call'
    : 'Schedule Your Session';
  const description = isCuriosity
    ? 'This is a 60-minute conversation. Come as you are. There is nothing to prepare, no right answers, and no pressure.'
    : 'This is your 3-hour coaching container. Come as you are. There is nothing to prepare — just your willingness to show up for yourself.';
  const priceNote = isCuriosity
    ? 'This $125 investment is applied toward any container you choose to step into.'
    : '';

  try {
    await resend.emails.send({
      from: FROM,
      to: email,
      subject,
      html: `
        <div style="font-family: Georgia, serif; max-width: 600px; margin: 0 auto; color: #2d2d2d;">
          <div style="background: linear-gradient(135deg, #8B3A47 0%, #6B2D3E 100%); padding: 2rem; text-align: center; border-radius: 8px 8px 0 0;">
            <h1 style="color: #FAF8F5; font-size: 1.75rem; margin: 0;">${heading}</h1>
            <p style="color: #F5EDE3; margin: 0.5rem 0 0; font-style: italic;">That Deeper Feeling</p>
          </div>
          <div style="padding: 2rem; background: #FAF8F5; border-radius: 0 0 8px 8px;">
            <p>Dear ${name},</p>
            <p>Your agreement has been received. Your next step is to choose a time that works for you:</p>
            <div style="text-align: center; margin: 2rem 0;">
              <a href="${calendlyUrl}" style="display: inline-block; background: #8B3A47; color: #FAF8F5; padding: 1rem 2.5rem; border-radius: 6px; text-decoration: none; font-size: 1.1rem; font-weight: 600;">${buttonText}</a>
            </div>
            <p style="background: #F5EDE3; padding: 1rem; border-radius: 6px; border-left: 3px solid #C4956A;">${description}</p>
            ${priceNote ? `<p>${priceNote}</p>` : ''}
            <p style="margin-top: 2rem;">With warmth,<br /><strong>Kimberly Bryant</strong><br /><em>That Deeper Feeling</em></p>
          </div>
        </div>
      `,
    });
  } catch (err) {
    console.error(`Failed to send ${type} Calendly email to ${email}:`, err);
  }
}

/**
 * Notify Kimberly that a contract was sent (pending signature).
 */
export async function notifyKimberlyContractSent(
  clientName: string,
  clientEmail: string,
  type: string,
): Promise<void> {
  const resend = getResend();
  const label = type === 'curiosity-call' ? 'Curiosity Call' : 'Session';

  try {
    await resend.emails.send({
      from: FROM,
      to: KIMBERLY_EMAIL(),
      subject: `Agreement Sent: ${clientName} (${label})`,
      html: `
        <div style="font-family: Georgia, serif; max-width: 600px; margin: 0 auto; color: #2d2d2d;">
          <h2 style="color: #8B3A47;">Agreement Sent — Awaiting Signature</h2>
          <table style="width: 100%; margin: 1rem 0; border-collapse: collapse;">
            <tr><td style="padding: 0.5rem 0; color: #888;"><strong>Name:</strong></td><td style="padding: 0.5rem 0;">${clientName}</td></tr>
            <tr><td style="padding: 0.5rem 0; color: #888;"><strong>Email:</strong></td><td style="padding: 0.5rem 0;"><a href="mailto:${clientEmail}">${clientEmail}</a></td></tr>
            <tr><td style="padding: 0.5rem 0; color: #888;"><strong>Type:</strong></td><td style="padding: 0.5rem 0;">${label}</td></tr>
          </table>
          <p>The participant agreement has been sent via Docuseal. Once they sign, they will automatically receive the scheduling link.</p>
        </div>
      `,
    });
  } catch (err) {
    console.error('Failed to notify Kimberly of contract sent:', err);
  }
}

/**
 * Notify Kimberly that a contract was signed and scheduling link sent.
 */
export async function notifyKimberlyContractSigned(
  clientName: string,
  clientEmail: string,
  type: string,
): Promise<void> {
  const resend = getResend();
  const label = type === 'curiosity-call' ? 'Curiosity Call' : 'Session';

  try {
    await resend.emails.send({
      from: FROM,
      to: KIMBERLY_EMAIL(),
      subject: `Agreement Signed: ${clientName} (${label}) — Scheduling Link Sent`,
      html: `
        <div style="font-family: Georgia, serif; max-width: 600px; margin: 0 auto; color: #2d2d2d;">
          <h2 style="color: #8B3A47;">Agreement Signed</h2>
          <table style="width: 100%; margin: 1rem 0; border-collapse: collapse;">
            <tr><td style="padding: 0.5rem 0; color: #888;"><strong>Name:</strong></td><td style="padding: 0.5rem 0;">${clientName}</td></tr>
            <tr><td style="padding: 0.5rem 0; color: #888;"><strong>Email:</strong></td><td style="padding: 0.5rem 0;"><a href="mailto:${clientEmail}">${clientEmail}</a></td></tr>
            <tr><td style="padding: 0.5rem 0; color: #888;"><strong>Type:</strong></td><td style="padding: 0.5rem 0;">${label}</td></tr>
          </table>
          <p>${clientName} has signed their agreement and has been sent the Calendly link to schedule.</p>
        </div>
      `,
    });
  } catch (err) {
    console.error('Failed to notify Kimberly of contract signed:', err);
  }
}

/**
 * Notify Kimberly of a new session booking (initial payment received).
 */
export async function notifyKimberlyNewBooking(
  clientName: string,
  clientEmail: string,
  type: string,
  amount: string,
): Promise<void> {
  const resend = getResend();
  const label = type === 'curiosity-call' ? 'Curiosity Call' : 'Session';

  try {
    await resend.emails.send({
      from: FROM,
      to: KIMBERLY_EMAIL(),
      subject: `New ${label} Booking: ${clientName}`,
      html: `
        <div style="font-family: Georgia, serif; max-width: 600px; margin: 0 auto; color: #2d2d2d;">
          <h2 style="color: #8B3A47;">New ${label} Booking</h2>
          <table style="width: 100%; margin: 1rem 0; border-collapse: collapse;">
            <tr><td style="padding: 0.5rem 0; color: #888;"><strong>Name:</strong></td><td style="padding: 0.5rem 0;">${clientName}</td></tr>
            <tr><td style="padding: 0.5rem 0; color: #888;"><strong>Email:</strong></td><td style="padding: 0.5rem 0;"><a href="mailto:${clientEmail}">${clientEmail}</a></td></tr>
            <tr><td style="padding: 0.5rem 0; color: #888;"><strong>Payment:</strong></td><td style="padding: 0.5rem 0;">${amount}</td></tr>
          </table>
          <p>Agreement has been sent. Once signed, they will receive the scheduling link automatically.</p>
        </div>
      `,
    });
  } catch (err) {
    console.error('Failed to notify Kimberly of new booking:', err);
  }
}
