import { NextRequest, NextResponse } from 'next/server';
import Stripe from 'stripe';

function getStripe() {
  return new Stripe(process.env.STRIPE_SECRET_KEY!, {
    apiVersion: '2026-01-28.clover',
  });
}

async function getKingSuitesSold(stripe: Stripe): Promise<number> {
  const sessions = await stripe.checkout.sessions.list({
    status: 'complete',
    limit: 100,
  });
  return sessions.data.filter(
    (s) => s.metadata?.housing === 'king' && s.metadata?.event === 'reclaiming-the-forbidden-2026'
  ).length;
}

export async function POST(req: NextRequest) {
  try {
    const stripe = getStripe();
    const body = await req.json();
    const { name, email, phone, q1, q2, q3, q4, q5, paymentOption, housing } = body;

    if (!name || !email || !phone) {
      return NextResponse.json(
        { error: 'Name, email, and phone are required.' },
        { status: 400 }
      );
    }

    // Check king suite availability
    if (housing === 'king') {
      const sold = await getKingSuitesSold(stripe);
      if (sold >= 3) {
        return NextResponse.json(
          { error: 'All Luxury King Suites have been reserved. Please select a different housing option.' },
          { status: 400 }
        );
      }
    }

    const retreatAmount = paymentOption === 'full' ? 125000 : 50000; // cents
    const retreatDescription =
      paymentOption === 'full'
        ? 'Reclaiming the Forbidden Retreat — Full Payment ($1,250)'
        : 'Reclaiming the Forbidden Retreat — $500 Deposit';

    const lineItems: Stripe.Checkout.SessionCreateParams.LineItem[] = [
      {
        price_data: {
          currency: 'usd',
          product_data: {
            name: retreatDescription,
            description: 'May 8–10, 2026 · St. George, Utah',
          },
          unit_amount: retreatAmount,
        },
        quantity: 1,
      },
    ];

    // Add housing line item if selected
    if (housing === 'bunk') {
      lineItems.push({
        price_data: {
          currency: 'usd',
          product_data: {
            name: 'On-Site Lodging — The Slumber Party Room',
            description: '3 nights · Friday–Monday morning',
          },
          unit_amount: 49500, // $495
        },
        quantity: 1,
      });
    } else if (housing === 'king') {
      lineItems.push({
        price_data: {
          currency: 'usd',
          product_data: {
            name: 'On-Site Lodging — Private King En-Suite',
            description: '3 nights · Friday–Monday morning',
          },
          unit_amount: 99500, // $995
        },
        quantity: 1,
      });
    }

    const session = await stripe.checkout.sessions.create({
      payment_method_types: ['card'],
      mode: 'payment',
      customer_email: email,
      line_items: lineItems,
      metadata: {
        event: 'reclaiming-the-forbidden-2026',
        name,
        email,
        phone,
        paymentOption,
        housing: housing || 'none',
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
