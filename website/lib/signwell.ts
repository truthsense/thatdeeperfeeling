/**
 * Docuseal e-signature integration (file kept as signwell.ts to avoid import churn).
 *
 * When DOCUSEAL_API_KEY is set and DOCUSEAL_MOCK is not "true",
 * sends real contracts via the Docuseal API.
 *
 * Otherwise, operates in mock mode: logs the request and returns
 * a fake document ID so the rest of the funnel can be tested
 * without a live Docuseal account.
 */

const DOCUSEAL_API_BASE = 'https://api.docuseal.com';

export interface ContractRecipient {
  name: string;
  email: string;
}

export interface ContractMetadata {
  /** "curiosity-call" | "session" | "retreat" */
  type: string;
  name: string;
  email: string;
  [key: string]: string;
}

export interface SendContractResult {
  success: boolean;
  documentId: string | null;
  mock: boolean;
  error?: string;
}

function isMockMode(): boolean {
  return (
    !process.env.DOCUSEAL_API_KEY ||
    process.env.DOCUSEAL_MOCK === 'true'
  );
}

/**
 * Send a contract to a recipient for signing via Docuseal.
 *
 * In mock mode, returns immediately with a fake document ID.
 * The calling code should check `result.mock` and, if true,
 * skip waiting for a webhook and proceed directly.
 */
export async function sendContract(
  recipient: ContractRecipient,
  metadata: ContractMetadata,
  templateId?: string,
): Promise<SendContractResult> {
  if (isMockMode()) {
    const fakeId = `mock_${Date.now()}_${Math.random().toString(36).slice(2, 8)}`;
    console.log('[Docuseal MOCK] Contract send simulated:', {
      recipient,
      metadata,
      templateId: templateId || process.env.DOCUSEAL_TEMPLATE_ID || 'none',
      documentId: fakeId,
    });
    return { success: true, documentId: fakeId, mock: true };
  }

  const apiKey = process.env.DOCUSEAL_API_KEY!;
  const tplId = templateId || process.env.DOCUSEAL_TEMPLATE_ID;

  if (!tplId) {
    console.error('[Docuseal] No template ID configured');
    return { success: false, documentId: null, mock: false, error: 'No template ID' };
  }

  try {
    const res = await fetch(`${DOCUSEAL_API_BASE}/submissions`, {
      method: 'POST',
      headers: {
        'X-Auth-Token': apiKey,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        template_id: parseInt(tplId, 10),
        submitters: [
          {
            role: 'Client',
            name: recipient.name,
            email: recipient.email,
            // Metadata flows through to the webhook payload
            metadata: metadata,
          },
        ],
      }),
    });

    if (!res.ok) {
      const text = await res.text();
      console.error('[Docuseal] API error:', res.status, text);
      return { success: false, documentId: null, mock: false, error: text };
    }

    const data = await res.json();
    // Docuseal returns an array of submitter objects; use submission id from first
    const submissionId = Array.isArray(data) ? data[0]?.submission_id : data?.id;
    console.log('[Docuseal] Contract sent:', {
      submissionId,
      recipient: recipient.email,
      type: metadata.type,
    });

    return { success: true, documentId: String(submissionId), mock: false };
  } catch (err) {
    console.error('[Docuseal] Failed to send contract:', err);
    return {
      success: false,
      documentId: null,
      mock: false,
      error: err instanceof Error ? err.message : 'Unknown error',
    };
  }
}

/**
 * Verify a Docuseal webhook by comparing the custom header value.
 * Docuseal sends a custom header (X-Webhook-Secret) with a predefined value.
 * Skip verification in mock mode or if no secret is configured.
 */
export function verifyWebhookSignature(
  _payload: string,
  headerValue: string | null,
): boolean {
  const secret = process.env.DOCUSEAL_WEBHOOK_SECRET;
  if (!secret || isMockMode()) return true;
  return headerValue === secret;
}
