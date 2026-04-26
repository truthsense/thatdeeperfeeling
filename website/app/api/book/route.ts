import { NextRequest, NextResponse } from 'next/server';
import Stripe from 'stripe';

function getStripe() {
  return new Stripe(process.env.STRIPE_SECRET_KEY!, {
    apiVersion: '2026-01-28.clover',
  });
}

/**
 * Creates a Stripe checkout session for a returning client
 * booking a Sacred Pause single session ($500).
 */
export async function POST(req: NextRequest) {
  try {
    const stripe = getStripe();
    const body = await req.json();
    const { name, email } = body;

    if (!name || !email) {
      return NextResponse.json(
        { error: 'Name and email are required.' },
        { status: 400 }
      );
    }

    const sessionPrice = parseInt(process.env.SESSION_PRICE_CENTS || '50000', 10);

    const session = await stripe.checkout.sessions.create({
      payment_method_types: ['card'],
      mode: 'payment',
      customer_email: email,
      line_items: [
        {
          price_data: {
            currency: 'usd',
            product_data: {
              name: 'Sacred Pause Session — That Deeper Feeling',
              description: '3-hour coaching container with Kimberly Bryant',
            },
            unit_amount: sessionPrice,
          },
          quantity: 1,
        },
      ],
      metadata: {
        type: 'session',
        name,
        email,
      },
      success_url: `${process.env.NEXT_PUBLIC_BASE_URL}/book/success?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${process.env.NEXT_PUBLIC_BASE_URL}/book`,
    });

    return NextResponse.json({ url: session.url });
  } catch (err) {
    console.error('Session booking checkout error:', err);
    return NextResponse.json(
      { error: 'Failed to create checkout session. Please try again.' },
      { status: 500 }
    );
  }
}
