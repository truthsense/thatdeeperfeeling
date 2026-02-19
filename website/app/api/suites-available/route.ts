import { NextResponse } from 'next/server';
import Stripe from 'stripe';

function getStripe() {
  return new Stripe(process.env.STRIPE_SECRET_KEY!, {
    apiVersion: '2026-01-28.clover',
  });
}

const TOTAL_KING_SUITES = 3;

export async function GET() {
  try {
    const stripe = getStripe();
    const sessions = await stripe.checkout.sessions.list({
      status: 'complete',
      limit: 100,
    });
    const sold = sessions.data.filter(
      (s) => s.metadata?.housing === 'king' && s.metadata?.event === 'reclaiming-the-forbidden-2026'
    ).length;
    const remaining = Math.max(0, TOTAL_KING_SUITES - sold);
    return NextResponse.json({ remaining, sold, total: TOTAL_KING_SUITES });
  } catch (err) {
    console.error('Error checking suite availability:', err);
    return NextResponse.json({ remaining: 0, sold: 0, total: TOTAL_KING_SUITES });
  }
}
