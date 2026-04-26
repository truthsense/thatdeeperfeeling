import { NextRequest, NextResponse } from 'next/server';
import { Resend } from 'resend';

function getResend() {
  return new Resend(process.env.RESEND_API_KEY);
}

export async function POST(req: NextRequest) {
  try {
    const { name, email } = await req.json();

    if (!email || !email.includes('@')) {
      return NextResponse.json({ error: 'Valid email required.' }, { status: 400 });
    }

    const resend = getResend();
    const displayName = name || 'Someone';

    // Notify Kimberly
    await resend.emails.send({
      from: 'That Deeper Feeling <noreply@thatdeeperfeeling.com>',
      to: process.env.KIMBERLY_EMAIL || 'kimberly@thatdeeperfeeling.com',
      subject: `New Email Subscriber: ${displayName}`,
      html: `
        <div style="font-family: Georgia, serif; max-width: 600px; margin: 0 auto; color: #2d2d2d;">
          <h2 style="color: #8B3A47;">New Subscriber</h2>
          <table style="width: 100%; border-collapse: collapse;">
            <tr><td style="padding: 0.5rem 0; color: #888;"><strong>Name:</strong></td><td style="padding: 0.5rem 0;">${displayName}</td></tr>
            <tr><td style="padding: 0.5rem 0; color: #888;"><strong>Email:</strong></td><td style="padding: 0.5rem 0;"><a href="mailto:${email}">${email}</a></td></tr>
          </table>
          <p style="margin-top: 1.5rem; color: #888; font-size: 0.9rem;">Add to your list in ConvertKit/Beehiiv when ready.</p>
        </div>
      `,
    });

    // Send welcome email to subscriber
    await resend.emails.send({
      from: 'Kimberly Bryant <noreply@thatdeeperfeeling.com>',
      to: email,
      subject: 'You\'re in. Welcome.',
      html: `
        <div style="font-family: Georgia, serif; max-width: 600px; margin: 0 auto; color: #2d2d2d;">
          <div style="background: linear-gradient(135deg, #8B3A47 0%, #6B2D3E 100%); padding: 2rem; text-align: center; border-radius: 8px 8px 0 0;">
            <h1 style="color: #FAF8F5; font-size: 1.75rem; margin: 0;">That Deeper Feeling</h1>
            <p style="color: #F5EDE3; margin: 0.5rem 0 0; font-style: italic;">Where sensuality, soul, and surrender meet.</p>
          </div>
          <div style="padding: 2rem; background: #FAF8F5; border-radius: 0 0 8px 8px;">
            <p>Hi ${displayName},</p>
            <p>You're in. I'm glad you're here.</p>
            <p>I'll be in touch with invitations, insights, and resources for deepening your intimacy journey — in your own time, at your own pace.</p>
            <p>If something is already pulling at you, you're always welcome to start with a <a href="https://www.thatdeeperfeeling.com/start" style="color: #8B3A47;">Curiosity Call</a>.</p>
            <p style="margin-top: 2rem;">With warmth,<br /><strong>Kimberly Bryant</strong><br /><em>That Deeper Feeling</em></p>
          </div>
        </div>
      `,
    });

    return NextResponse.json({ success: true });
  } catch (err) {
    console.error('[subscribe] Error:', err);
    return NextResponse.json({ error: 'Something went wrong.' }, { status: 500 });
  }
}
