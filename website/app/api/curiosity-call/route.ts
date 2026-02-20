import { NextRequest, NextResponse } from 'next/server';
import Stripe from 'stripe';

function getStripe() {
  return new Stripe(process.env.STRIPE_SECRET_KEY!, {
    apiVersion: '2026-01-28.clover',
  });
}

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

    const session = await stripe.checkout.sessions.create({
      payment_method_types: ['card'],
      mode: 'payment',
      customer_email: email,
      line_items: [
        {
          price_data: {
            currency: 'usd',
            product_data: {
              name: 'Curiosity Call — That Deeper Feeling',
              description: '60-minute consultation with Kimberly Bryant',
            },
            unit_amount: 12500, // $125
          },
          quantity: 1,
        },
      ],
      metadata: {
        type: 'curiosity-call',
        name,
        email,
      },
      success_url: `${process.env.NEXT_PUBLIC_BASE_URL}/consult/success?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${process.env.NEXT_PUBLIC_BASE_URL}/consult`,
    });

    return NextResponse.json({ url: session.url });
  } catch (err) {
    console.error('Curiosity call checkout error:', err);
    return NextResponse.json(
      { error: 'Failed to create checkout session. Please try again.' },
      { status: 500 }
    );
  }
}
