import { NextRequest, NextResponse } from 'next/server';
import Stripe from 'stripe';
import { Resend } from 'resend';
import { sendContract } from '@/lib/signwell';
import {
  sendCalendlyEmail,
  notifyKimberlyNewBooking,
  notifyKimberlyContractSent,
} from '@/lib/emails';

function getStripe() {
  return new Stripe(process.env.STRIPE_SECRET_KEY!, {
    apiVersion: '2026-01-28.clover',
  });
}

function getResend() {
  return new Resend(process.env.RESEND_API_KEY);
}

function getHousingLabel(housing: string): string {
  if (housing === 'bunk') return 'The Slumber Party Room ($495)';
  if (housing === 'king') return 'Private King En-Suite ($995)';
  return 'None — arranging own accommodations';
}

export async function POST(req: NextRequest) {
  const stripe = getStripe();
  const resend = getResend();
  const body = await req.text();
  const signature = req.headers.get('stripe-signature')!;

  let event: Stripe.Event;

  try {
    event = stripe.webhooks.constructEvent(
      body,
      signature,
      process.env.STRIPE_WEBHOOK_SECRET!
    );
  } catch (err) {
    console.error('Webhook signature verification failed:', err);
    return NextResponse.json({ error: 'Invalid signature' }, { status: 400 });
  }

  if (event.type === 'checkout.session.completed') {
    const session = event.data.object as Stripe.Checkout.Session;
    const metadata = session.metadata || {};

    // ─────────────────────────────────────────────
    // CURIOSITY CALL — Path A (new client)
    // ─────────────────────────────────────────────
    if (metadata.type === 'curiosity-call') {
      const name = metadata.name || 'Guest';
      const email = metadata.email || session.customer_email || '';

      if (email) {
        // Send contract via SignWell
        const result = await sendContract(
          { name, email },
          { type: 'curiosity-call', name, email },
        );

        if (result.mock) {
          // Mock mode: no real contract — send Calendly email immediately
          // (preserves current behavior when SignWell isn't configured)
          await sendCalendlyEmail(name, email, 'curiosity-call');
        } else if (result.success) {
          // Live mode: contract sent — Calendly email will be triggered
          // by the /api/contract-signed webhook after client signs
          await notifyKimberlyContractSent(name, email, 'curiosity-call');
        } else {
          // SignWell failed — fall back to sending Calendly directly
          console.error('[webhook] SignWell failed, falling back to direct Calendly send');
          await sendCalendlyEmail(name, email, 'curiosity-call');
        }

        // Notify Kimberly of the booking
        await notifyKimberlyNewBooking(name, email, 'curiosity-call', '$125.00');
      }

      return NextResponse.json({ received: true });
    }

    // ────────────────────────��────────────────────
    // SESSION BOOKING — Path B (returning client)
    // ─────���──────���────────────────────────────────
    if (metadata.type === 'session') {
      const name = metadata.name || 'Guest';
      const email = metadata.email || session.customer_email || '';
      const amount = session.amount_total
        ? `$${(session.amount_total / 100).toFixed(2)}`
        : '$500.00';

      if (email) {
        // Send contract via SignWell
        const result = await sendContract(
          { name, email },
          { type: 'session', name, email },
        );

        if (result.mock) {
          // Mock mode: send Calendly email immediately
          await sendCalendlyEmail(name, email, 'session');
        } else if (result.success) {
          // Live mode: Calendly email sent after client signs
          await notifyKimberlyContractSent(name, email, 'session');
        } else {
          // SignWell failed — fall back
          console.error('[webhook] SignWell failed, falling back to direct Calendly send');
          await sendCalendlyEmail(name, email, 'session');
        }

        // Notify Kimberly
        await notifyKimberlyNewBooking(name, email, 'session', amount);
      }

      return NextResponse.json({ received: true });
    }

    // ──────────────────��──────────────────────────
    // RETREAT REGISTRATION (unchanged)
    // ─────────────────────────────────────────────
    const name = metadata.name || 'Guest';
    const email = metadata.email || session.customer_email || '';
    const phone = metadata.phone || '';
    const paymentOption = metadata.paymentOption || 'deposit';
    const housing = metadata.housing || 'none';
    const amountPaid = session.amount_total ? `$${(session.amount_total / 100).toFixed(2)}` : '';
    const housingLabel = getHousingLabel(housing);

    // Email to attendee
    if (email) {
      try {
        await resend.emails.send({
          from: 'That Deeper Feeling <noreply@thatdeeperfeeling.com>',
          to: email,
          subject: 'Registration Confirmed — Reclaiming the Forbidden',
          html: `
            <div style="font-family: Georgia, serif; max-width: 600px; margin: 0 auto; color: #2d2d2d;">
              <div style="background: linear-gradient(135deg, #8B3A47 0%, #6B2D3E 100%); padding: 2rem; text-align: center; border-radius: 8px 8px 0 0;">
                <h1 style="color: #FAF8F5; font-size: 1.75rem; margin: 0;">You're In.</h1>
                <p style="color: #F5EDE3; margin: 0.5rem 0 0; font-style: italic;">Reclaiming the Forbidden</p>
              </div>
              <div style="padding: 2rem; background: #FAF8F5; border-radius: 0 0 8px 8px;">
                <p>Dear ${name},</p>
                <p>Your registration for <strong>Reclaiming the Forbidden</strong> has been confirmed.</p>
                <table style="width: 100%; margin: 1.5rem 0; border-collapse: collapse;">
                  <tr>
                    <td style="padding: 0.5rem 0; color: #888;"><strong>Event:</strong></td>
                    <td style="padding: 0.5rem 0;">Reclaiming the Forbidden</td>
                  </tr>
                  <tr>
                    <td style="padding: 0.5rem 0; color: #888;"><strong>Dates:</strong></td>
                    <td style="padding: 0.5rem 0;">April 24–26, 2026</td>
                  </tr>
                  <tr>
                    <td style="padding: 0.5rem 0; color: #888;"><strong>Location:</strong></td>
                    <td style="padding: 0.5rem 0;">St. George, Utah</td>
                  </tr>
                  <tr>
                    <td style="padding: 0.5rem 0; color: #888;"><strong>Payment:</strong></td>
                    <td style="padding: 0.5rem 0;">${amountPaid} (${paymentOption === 'full' ? 'Paid in Full' : 'Deposit — Balance of $950 due by April 10, 2026'})</td>
                  </tr>
                  <tr>
                    <td style="padding: 0.5rem 0; color: #888;"><strong>Housing:</strong></td>
                    <td style="padding: 0.5rem 0;">${housingLabel}</td>
                  </tr>
                </table>
                ${paymentOption === 'deposit' ? '<p style="background: #F5EDE3; padding: 1rem; border-radius: 6px; border-left: 3px solid #C4956A;"><strong>Reminder:</strong> Your remaining retreat balance of $950 is due by April 10, 2026. You will receive a payment link closer to the due date.</p>' : ''}
                ${housing !== 'none' ? '<p style="background: #F5EDE3; padding: 1rem; border-radius: 6px; border-left: 3px solid #C4956A;">Your on-site housing includes an optional Sunday evening stay for unstructured rest, connection, and integration with free use of pool, hot tub, and all common areas.</p>' : ''}
                <p>Kimberly will be in touch with retreat details, lodging information, and preparation materials as we get closer to the date.</p>
                <p style="margin-top: 2rem;">With warmth,<br /><strong>Kimberly Bryant</strong><br /><em>That Deeper Feeling</em></p>
              </div>
            </div>
          `,
        });
      } catch (emailErr) {
        console.error('Failed to send attendee confirmation email:', emailErr);
      }
    }

    // Email to Kimberly
    try {
      const questionsHtml = [
        { label: 'Where in your life are you still performing "good"… and what part of you is quietly asking for more?', answer: metadata.q1 },
        { label: 'What part of your Eros — your life force, your play, your desire — feels ready to come back online?', answer: metadata.q2 },
        { label: 'If you gave yourself full permission for one weekend… what might you discover about yourself?', answer: metadata.q3 },
        { label: 'What part of you has been labeled "too much"… that might actually be your power?', answer: metadata.q4 },
        { label: 'Where have you been obedient at the expense of your own aliveness?', answer: metadata.q5 },
      ]
        .filter((q) => q.answer)
        .map(
          (q) =>
            `<div style="margin-bottom: 1rem; padding: 1rem; background: #F5EDE3; border-radius: 6px;">
              <p style="font-weight: bold; color: #8B3A47; margin: 0 0 0.5rem;">${q.label}</p>
              <p style="margin: 0; white-space: pre-wrap;">${q.answer}</p>
            </div>`
        )
        .join('');

      await resend.emails.send({
        from: 'That Deeper Feeling <noreply@thatdeeperfeeling.com>',
        to: process.env.KIMBERLY_EMAIL || 'kimberly@thatdeeperfeeling.com',
        subject: `New Retreat Registration: ${name}`,
        html: `
          <div style="font-family: Georgia, serif; max-width: 600px; margin: 0 auto; color: #2d2d2d;">
            <h2 style="color: #8B3A47;">New Registration — Reclaiming the Forbidden</h2>
            <table style="width: 100%; margin: 1rem 0; border-collapse: collapse;">
              <tr><td style="padding: 0.5rem 0; color: #888;"><strong>Name:</strong></td><td style="padding: 0.5rem 0;">${name}</td></tr>
              <tr><td style="padding: 0.5rem 0; color: #888;"><strong>Email:</strong></td><td style="padding: 0.5rem 0;"><a href="mailto:${email}">${email}</a></td></tr>
              <tr><td style="padding: 0.5rem 0; color: #888;"><strong>Phone:</strong></td><td style="padding: 0.5rem 0;">${phone}</td></tr>
              <tr><td style="padding: 0.5rem 0; color: #888;"><strong>Payment:</strong></td><td style="padding: 0.5rem 0;">${amountPaid} (${paymentOption === 'full' ? 'Paid in Full' : 'Deposit'})</td></tr>
              <tr><td style="padding: 0.5rem 0; color: #888;"><strong>Housing:</strong></td><td style="padding: 0.5rem 0;">${housingLabel}</td></tr>
            </table>
            ${questionsHtml ? `<h3 style="color: #8B3A47; margin-top: 2rem;">Reflection Responses</h3>${questionsHtml}` : ''}
          </div>
        `,
      });
    } catch (emailErr) {
      console.error('Failed to send Kimberly notification email:', emailErr);
    }
  }

  return NextResponse.json({ received: true });
}
