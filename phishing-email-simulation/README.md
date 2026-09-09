# Phishing Email Simulation

A Flask-based web application for simulating phishing attacks in a controlled, educational environment. This tool helps organizations conduct security awareness training by simulating realistic phishing campaigns and tracking user interactions.

## Features

- **Multiple Phishing Campaigns**: Three realistic phishing scenarios:
  1. Fake Invoice Payment Request
  2. HR Policy Update Notification  
  3. Password Reset Required
- **Email Preview**: View what the phishing email would look like
- **Landing Pages**: Simulated phishing landing pages that capture clicks (no actual credential collection)
- **Click Tracking**: Logs user interactions for training metrics
- **Dashboard**: View raw click data for analysis
- **Educational Focus**: Designed for security awareness training only

## How It Works

### Campaign Structure
Each campaign consists of:
1. **Email Template**: The phishing email that users would receive
2. **Landing Page**: The fake website users are directed to when clicking links in the email
3. **Tracking**: When a user visits the landing page, their interaction is logged (campaign, timestamp, IP address)

### User Flow
1. User visits the home page and sees available campaigns
2. User can preview what the phishing email looks like
3. If user clicks through to the landing page, their click is logged
4. Landing page displays educational content about identifying phishing attempts
5. Administrator can view click data via the dashboard

## Important Disclaimers

⚠️ **EDUCATIONAL USE ONLY**: This tool is designed for security awareness training in controlled environments.

- **No Credential Collection**: This simulation does NOT collect or store any real credentials
- **Local Use Only**: Intended for deployment on internal networks for training purposes
- **Explicit Authorization Required**: Only use against systems and users who have given explicit consent for security training
- **Compliance**: Ensure use complies with your organization's policies and applicable laws

## Requirements

```
Flask==2.3.2
```

Install with:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
python main.py
```

2. Open your browser to `http://127.0.0.1:5002`

3. Use the web interface to:
   - Preview different phishing email templates
   - Understand what makes each email suspicious
   - (Optional) Deploy internally for security awareness training with proper authorization

4. Access the dashboard at `http://127.0.0.1:5002/dashboard` to view click logs

## Campaigns Included

### 1. Fake Invoice Payment Request
- **Subject**: Invoice #INV-2026-08942 - Payment Overdue
- **Tactics**: Urgency, financial pressure, fake invoice details
- **Educational Points**: Check sender address, verify invoices through official channels

### 2. HR Policy Update Notification
- **Subject**: Important: New Work-From-House Policy Effective Today
- **Tactics**: Authority impersonation (HR), policy changes, required action
- **Educational Points**: Verify policy changes through official HR channels, be wary of urgent policy updates

### 3. Password Reset Required
- **Subject**: Verify Your Identity to Avoid Account Suspension
- **Tactics**: Fear of account loss, urgency, credential harvesting pretext
- **Educational Points**: Legitimate services rarely ask for passwords via email, use official password reset procedures

## Files

- `main.py`: Flask application with routing and click logging
- `templates/`: HTML templates for emails and landing pages
  - `index.html`: Home page listing campaigns
  - `fake_invoice.html`: Fake invoice email template
  - `fake_invoice_landing.html`: Educational landing page for invoice scam
  - `hr_policy.html`: HR policy email template
  - `hr_policy_landing.html`: Educational landing page for HR scam
  - `sample_email_1.html`: Password reset email template
  - `landing.html`: Educational landing page for password reset scam
- `click_log.json`: JSON file storing click interactions (generated at runtime)
- `session_log.json`: Additional logging file
- `analyze_clicks.py`: Optional script for analyzing click data
- `requirements.txt`: Python dependencies

## Educational Purpose

This tool helps users learn to:
- Identify common phishing tactics (urgency, authority impersonation, fear)
- Check email headers and sender addresses for inconsistencies
- Hover over links to see actual destinations before clicking
- Verify unexpected requests through official channels
- Report suspicious emails to IT/security teams
- Understand that legitimate organizations won't ask for passwords via email

## Best Practices for Deployment

1. **Get Authorization**: Obtain explicit permission before deploying for training
2. **Inform Users**: Tell participants this is a training exercise beforehand
3. **Debrief**: Conduct training sessions after showing what to look for
4. **Monitor**: Keep logs secure and delete after training period
5. **Variance**: Use different scenarios for different groups to avoid pattern recognition
6. **Legal Compliance**: Ensure compliance with local laws and organizational policies

## Customization

To add new campaigns:
1. Add email and landing page templates to the `templates/` folder
2. Add an entry to the `CAMPAIGNS` dictionary in `main.py`
3. Ensure the template and landing keys match your new files