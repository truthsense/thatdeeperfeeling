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
    const { name, email, phone, q1, q2, q3, q4, q5, paymentOption } = body;

    if (!name || !email || !phone) {
      return NextResponse.json(
        { error: 'Name, email, and phone are required.' },
        { status: 400 }
      );
    }

    const amount = paymentOption === 'full' ? 120000 : 50000; // cents
    const description =
      paymentOption === 'full'
        ? 'Reclaiming the Forbidden Retreat — Full Payment'
        : 'Reclaiming the Forbidden Retreat — $500 Deposit';

    const session = await stripe.checkout.sessions.create({
      payment_method_types: ['card'],
      mode: 'payment',
      customer_email: email,
      line_items: [
        {
          price_data: {
            currency: 'usd',
            product_data: {
              name: description,
              description: 'May 8–10, 2026 · St. George, Utah',
            },
            unit_amount: amount,
          },
          quantity: 1,
        },
      ],
      metadata: {
        event: 'reclaiming-the-forbidden-2026',
        name,
        email,
        phone,
        paymentOption,
        q1: q1?.substring(0, 500) || '',
        q2: q2?.substring(0, 500) || '',
        q3: q3?.substring(0, 500) || '',
        q4: q4?.substring(0, 500) || '',
        q5: q5?.substring(0, 500) || '',
      },
      success_url: `${process.env.NEXT_PUBLIC_BASE_URL}/events/register/success?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${process.env.NEXT_PUBLIC_BASE_URL}/events/register`,
    });

    return NextResponse.json({ url: session.url });
  } catch (err) {
    console.error('Stripe checkout error:', err);
    return NextResponse.json(
      { error: 'Failed to create checkout session. Please try again.' },
      { status: 500 }
    );
  }
}
