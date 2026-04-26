import { NextRequest, NextResponse } from 'next/server';
import { verifyWebhookSignature } from '@/lib/signwell';
import {
  sendCalendlyEmail,
  notifyKimberlyContractSigned,
} from '@/lib/emails';

/**
 * Docuseal webhook endpoint.
 * Called when a participant signs their agreement.
 * Triggers the Calendly scheduling email.
 */
export async function POST(req: NextRequest) {
  const body = await req.text();
  // Docuseal sends a custom header with our predefined secret value
  const signature = req.headers.get('x-webhook-secret');

  if (!verifyWebhookSignature(body, signature)) {
    console.error('[contract-signed] Invalid webhook signature');
    return NextResponse.json({ error: 'Invalid signature' }, { status: 401 });
  }

  let payload: Record<string, unknown>;
  try {
    payload = JSON.parse(body);
  } catch {
    return NextResponse.json({ error: 'Invalid JSON' }, { status: 400 });
  }

  // Docuseal event types: submission_completed, etc.
  const eventType = payload.event_type as string | undefined;
  if (eventType !== 'submission_completed') {
    return NextResponse.json({ received: true, ignored: eventType });
  }

  // Extract metadata we attached when sending the contract.
  // Docuseal nests submitters inside data.submission.submitters
  // or directly as data.submitters depending on version.
  const submission =
    (payload.data as Record<string, unknown>)?.submission as Record<string, unknown> | undefined
    ?? payload.data as Record<string, unknown> | undefined;

  const submitters = submission?.submitters as Array<Record<string, unknown>> | undefined;
  const firstSubmitter = Array.isArray(submitters) ? submitters[0] : undefined;
  const metadata = (firstSubmitter?.metadata ?? {}) as Record<string, string>;

  const name = metadata.name || (firstSubmitter?.name as string) || 'Guest';
  const email = metadata.email || (firstSubmitter?.email as string) || '';
  const type = metadata.type || 'session';

  if (!email) {
    console.error('[contract-signed] No email in payload:', JSON.stringify(payload));
    return NextResponse.json({ error: 'No email in payload' }, { status: 400 });
  }

  console.log(`[contract-signed] Agreement signed: ${name} (${email}), type: ${type}`);

  const callType = type === 'curiosity-call' ? 'curiosity-call' : 'session';
  await sendCalendlyEmail(name, email, callType);
  await notifyKimberlyContractSigned(name, email, type);

  return NextResponse.json({ received: true, processed: true });
}
