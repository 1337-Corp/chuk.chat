---
title: "Datenschutzerklärung"
layout: "legal"
type: "page"
translationKey: "privacy"
updated: "Zuletzt aktualisiert: 23. November 2025"
tldr: "Ihre Chats werden auf Ihrem Gerät Ende-zu-Ende-verschlüsselt, bevor sie gespeichert werden. Wir können Ihre Nachrichten nicht lesen. Wir sammeln nur die minimal notwendigen Daten zur Bereitstellung des Dienstes."
---

## 1. Einleitung

Diese Datenschutzerklärung erklärt, wie chuk.chat ("wir", "uns" oder "unser") Ihre Informationen sammelt, verwendet und schützt, wenn Sie unsere KI-Chat-Anwendung und Dienste nutzen.

Wir nehmen Ihre Privatsphäre ernst und haben unseren Dienst mit Datenschutz als Kernprinzip entwickelt.

## 2. Informationen, die wir sammeln

### 2.1 Kontoinformationen

Wenn Sie ein Konto erstellen, sammeln wir:

- E-Mail-Adresse (in Klartext in der Supabase-Datenbank gespeichert)
- Anzeigename (optional, in Klartext gespeichert)
- Passwort (als sicherer Hash gespeichert, niemals in Klartext)

**Wichtig:** Ihre E-Mail und Ihr Benutzername werden im Standarddatenbankformat (nicht verschlüsselt) gespeichert, da dies für die Authentifizierung und E-Mail-Kommunikation erforderlich ist. Nur Ihre Chat-Nachrichten werden verschlüsselt.

### 2.2 Chat-Daten

Alle Ihre Chat-Nachrichten und Konversationen werden auf Ihrem Gerät mit AES-256-GCM-Verschlüsselung Ende-zu-Ende-verschlüsselt, bevor sie an Supabase gesendet werden. Das bedeutet:

- Ihr Verschlüsselungsschlüssel wird von Ihrem Passwort abgeleitet und verlässt niemals Ihr Gerät
- Wir speichern nur verschlüsselte Daten und können Ihre Nachrichten nicht entschlüsseln
- Nur Sie können Ihren Chat-Verlauf lesen

### 2.3 Nutzungsinformationen

Wir sammeln die folgenden Nutzungsdaten für Abrechnungs- und Dienstbetriebszwecke:

- Abonnementstatus und Zahlungsinformationen (sicher über Stripe verarbeitet)
- **Token-Nutzungsdaten:** Für jede KI-Nachricht protokollieren wir:
  - Eingabe-Tokens (Prompt-Länge)
  - Ausgabe-Tokens (Antwortlänge)
  - Verwendeter Modellname (z.B. "llama-3", "mistral-large")
  - Anbietername (z.B. "Meta", "Mistral")
  - Zeitstempel

Diese Daten werden in Supabase gespeichert, um Ihre Nutzung und Abrechnung zu berechnen. Wir speichern NICHT den tatsächlichen Nachrichteninhalt in diesen Protokollen - nur die Token-Anzahl und Metadaten.

**Wir sammeln NICHT:** Geräteinformationen, Betriebssystemdetails, App-Version, Plattformtyp, Fehlerprotokolle, Absturzberichte oder Analysedaten.

### 2.4 Drittanbieter-KI-Dienste

Wenn Sie KI-Funktionen verwenden, werden Ihre Daten von spezialisierten Drittanbieterdiensten verarbeitet:

- **Textgenerierung (LLMs):** Nachrichten werden an OpenRouter gesendet, das sie nur an Anbieter von open-weight KI-Modellen weiterleitet. **Wir unterstützen nur open-weight Modelle** (z.B. Llama, Mistral, Qwen, DeepSeek). Geschlossene/proprietäre Modelle (Claude, GPT-4, Gemini) sind nicht verfügbar. **Modelltraining ist deaktiviert**.
- **Sprach-zu-Text:** Audio wird von Whisper auf der Groq-Infrastruktur zur Transkription verarbeitet.
- **Text-zu-Sprache:** Text wird mit Inworld TTS in Sprache umgewandelt.
- **Sprach- und Videomodi (Demnächst):** Echtzeit-Sprach- und Videokommunikation wird über die LiveKit-Infrastruktur verarbeitet.

## 3. Wie wir Ihre Informationen verwenden

Wir verwenden gesammelte Informationen, um:

- Den Dienst bereitzustellen und aufrechtzuerhalten
- Die Nutzung zu berechnen und Abrechnung basierend auf Token-Verbrauch zu generieren
- Ihr Abonnement und Ihre Zahlungen zu verarbeiten
- Wichtige Dienstupdates und Sicherheitsbenachrichtigungen zu senden
- Kundensupport bereitzustellen
- Betrug oder Missbrauch zu erkennen und zu verhindern

**Wir verkaufen Ihre persönlichen Informationen nicht an Dritte.**

## 4. Datensicherheit

Wir implementieren branchenübliche Sicherheitsmaßnahmen zum Schutz Ihrer Daten:

- **Ende-zu-Ende-Verschlüsselung:** Alle Chat-Daten werden mit AES-256-GCM vor der Speicherung verschlüsselt
- **Sichere Authentifizierung:** Passwörter werden mit bcrypt mit starken Arbeitsfaktoren gehasht
- **HTTPS/TLS:** Alle Datenübertragungen werden mit TLS 1.3 verschlüsselt
- **Sichere Infrastruktur:** Gehostet auf Supabase mit SOC 2 Type II-Konformität

## 5. Datenspeicherung

- **Kontodaten:** Gespeichert, bis Sie Ihr Konto löschen
- **Chat-Daten:** Verschlüsselt gespeichert, bis Sie einzelne Chats manuell löschen
- **Token-Nutzungsprotokolle:** Für Abrechnungszwecke gespeichert und gelöscht, wenn Ihr Konto gelöscht wird
- **Zahlungsinformationen:** Sicher von Stripe gespeichert

## 6. Ihre Rechte

Sie haben das Recht auf:

- **Zugang:** Eine Kopie Ihrer personenbezogenen Daten anzufordern
- **Löschung:** Ihr Konto und alle zugehörigen Daten jederzeit zu löschen
- **Korrektur:** Ihre Kontoinformationen zu aktualisieren
- **Export:** Ihre Chat-Daten (entschlüsselt) aus der App herunterzuladen

Um diese Rechte auszuüben, kontaktieren Sie uns unter [privacy@chuk.chat](mailto:privacy@chuk.chat) oder verwenden Sie die In-App-Kontoeinstellungen.

## 7. Cookies und Tracking

Unsere Website verwendet minimale Cookies für wesentliche Funktionen:

- **Authentifizierungs-Cookies:** Um Sie eingeloggt zu halten
- **Präferenz-Cookies:** Um Ihr Theme und Ihre Einstellungen zu speichern

Wir verwenden keine Werbe-Cookies oder Tracking-Skripte von Drittanbietern.

## 8. Drittanbieterdienste

Wir verwenden die folgenden Drittanbieterdienste:

- **OpenRouter:** KI-Modell-Routing. [Datenschutz](https://openrouter.ai/privacy)
- **Groq:** Sprach-zu-Text. [Datenschutz](https://groq.com/privacy-policy/)
- **Inworld:** Text-zu-Sprache. [Datenschutz](https://www.inworld.ai/privacy-policy)
- **Supabase:** Datenbank und Authentifizierung. [Datenschutz](https://supabase.com/privacy)
- **Stripe:** Zahlungsabwicklung. [Datenschutz](https://stripe.com/privacy)
- **Lexoffice:** Rechnungserstellung. [Datenschutz](https://www.lexoffice.de/datenschutz/)
- **Hetzner:** API-Server-Hosting. [Datenschutz](https://www.hetzner.com/legal/privacy-policy)

## 9. Kontakt

E-Mail: [privacy@chuk.chat](mailto:privacy@chuk.chat)
Support: [support@chuk.chat](mailto:support@chuk.chat)
