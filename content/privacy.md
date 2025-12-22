---
title: "Privacy Policy"
layout: "legal"
type: "page"
translationKey: "privacy"
updated: "Last Updated: November 23, 2025"
tldr: "Your chats are encrypted end-to-end on your device before being stored. We cannot read your messages. We collect minimal data necessary to provide the service."
---

## 1. Introduction

This Privacy Policy explains how chuk.chat ("we," "us," or "our") collects, uses, and protects your information when you use our AI chat application and services.

We take your privacy seriously and have designed our service with privacy as a core principle.

## 2. Information We Collect

### 2.1 Account Information

When you create an account, we collect:

- Email address (stored in plaintext in Supabase database)
- Display name (optional, stored in plaintext)
- Password (stored as a secure hash, never in plaintext)

**Important:** Your email and username are stored in standard database format (not encrypted) as this is necessary for authentication and email communication. Only your chat messages are encrypted.

### 2.2 Chat Data

All your chat messages and conversations are encrypted end-to-end using AES-256-GCM encryption on your device before being sent to Supabase. This means:

- Your encryption key is derived from your password and never leaves your device
- We store only encrypted data and cannot decrypt your messages
- Only you can read your chat history

### 2.3 Usage Information

We collect the following usage data for billing and service operation:

- Subscription status and payment information (processed securely via Stripe)
- **Token Usage Data:** For each AI message, we log:
  - Input tokens (prompt length)
  - Output tokens (response length)
  - Model name used (e.g., "gpt-4", "claude-3.5-sonnet")
  - Provider name (e.g., "OpenAI", "Anthropic")
  - Timestamp

This data is stored in Supabase to calculate your usage and billing. We do NOT store the actual message content in these logs - only the token counts and metadata.

**We do NOT collect:** Device information, operating system details, app version, platform type, error logs, crash reports, or analytics data.

### 2.4 Third-Party AI Services

When you use AI features, your data is processed by specialized third-party services:

- **Text Generation (LLMs):** Messages are sent to OpenRouter, which routes them to open-weight AI model providers only. **We only support open-weight models** (e.g., Llama, Mistral, Qwen, DeepSeek). Closed/proprietary models (Claude, GPT-4, Gemini) are not available. **Model training is disabled** - your data is not used to train AI models.
- **Speech-to-Text:** Audio is processed by Whisper running on Groq infrastructure for transcription. Audio is not stored after transcription.
- **Text-to-Speech:** Text is converted to speech using Inworld TTS. Generated audio is delivered to you but not permanently stored.
- **Voice and Video Modes (Coming Soon):** Real-time voice and video communication will be processed through LiveKit infrastructure. Audio/video streams are transmitted in real-time but not permanently stored.

**Important:** Your prompts and AI responses pass through our API but are not stored in plaintext in Supabase (encrypted only). We recommend not sharing sensitive personal information in AI conversations.

## 3. How We Use Your Information

We use collected information to:

- Provide and maintain the Service
- Calculate usage and generate billing based on token consumption (input/output tokens per model)
- Process your subscription and payments
- Send important service updates and security notifications
- Improve and optimize the Service
- Provide customer support
- Detect and prevent fraud or abuse

**We do not sell your personal information to third parties.**

## 4. Data Security

We implement industry-standard security measures to protect your data:

- **End-to-End Encryption:** All chat data is encrypted with AES-256-GCM before storage
- **Secure Authentication:** Passwords are hashed using bcrypt with strong work factors
- **HTTPS/TLS:** All data transmission is encrypted using TLS 1.3
- **Secure Infrastructure:** Hosted on Supabase with SOC 2 Type II compliance
- **Regular Security Audits:** We regularly review our security practices

## 5. Data Retention

We retain your data as follows:

- **Account Data:** Retained until you delete your account
- **Chat Data:** Stored encrypted until you manually delete individual chats
- **Token Usage Logs:** Retained for billing purposes and deleted when your account is deleted
- **Payment Information:** Stored securely by Stripe (our payment processor)

We do not retain error logs, crash reports, or access logs in Supabase.

## 6. Your Rights

You have the right to:

- **Access:** Request a copy of your personal data
- **Deletion:** Delete your account and all associated data at any time
- **Correction:** Update your account information
- **Export:** Download your chat data (decrypted) from within the app

To exercise these rights, contact us at [privacy@chuk.chat](mailto:privacy@chuk.chat) or use the in-app account settings.

## 7. Cookies and Tracking

Our website uses minimal cookies for essential functionality:

- **Authentication cookies:** To keep you logged in
- **Preference cookies:** To remember your theme and settings

We do not use advertising cookies or third-party tracking scripts.

## 8. Children's Privacy

Our Service is not intended for children under the age of 13. We do not knowingly collect personal information from children under 13. If you believe we have collected information from a child under 13, please contact us immediately.

## 9. International Data Transfers

Your data may be stored and processed in Supabase infrastructure located in different countries. We ensure appropriate safeguards are in place to protect your data in accordance with this Privacy Policy.

## 10. Third-Party Services

We use the following third-party services:

- **OpenRouter:** AI model routing and access. [Privacy Policy](https://openrouter.ai/privacy)
- **Groq:** Speech-to-text transcription. [Privacy Policy](https://groq.com/privacy-policy/)
- **Inworld:** Text-to-speech generation. [Privacy Policy](https://www.inworld.ai/privacy-policy)
- **LiveKit:** Real-time voice and video (coming soon). [Privacy Policy](https://livekit.io/legal/privacy)
- **Supabase:** Database and authentication. [Privacy Policy](https://supabase.com/privacy)
- **Stripe:** Payment processing. [Privacy Policy](https://stripe.com/privacy)
- **Lexoffice:** Invoice generation. [Privacy Policy](https://www.lexoffice.de/datenschutz/)
- **Mailbox.org:** Email service. [Privacy Policy](https://mailbox.org/en/data-protection)
- **Hetzner:** API server hosting. [Privacy Policy](https://www.hetzner.com/legal/privacy-policy)

## 11. Changes to This Privacy Policy

We may update this Privacy Policy from time to time. We will notify you of significant changes by email or through the app. Continued use of the Service after changes constitutes acceptance of the updated policy.

## 12. Contact Us

If you have questions or concerns about this Privacy Policy or our data practices, please contact us:

Email: [privacy@chuk.chat](mailto:privacy@chuk.chat)
Support: [support@chuk.chat](mailto:support@chuk.chat)
