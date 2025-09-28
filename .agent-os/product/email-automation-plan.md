# Email Automation Plan

## Overview

This document outlines the recommended email automation architecture for the Airtable Event Management System using Gmail API and GitHub Actions.

---

## Architecture Decision

### **Selected Approach: Gmail API + GitHub Actions**

**Rationale:**
- Leverages existing Google Workspace infrastructure
- Zero additional monthly costs
- Emails sent from official Democrats Abroad domain (better deliverability)
- GitHub Actions provides free scheduling and execution
- No server maintenance required
- Secure credential storage via GitHub Secrets

**Rejected Alternatives:**
- **SendGrid/Mailgun**: Additional cost ($15-50/month), third-party sender
- **Google Apps Script**: Limited execution time, poor Airtable integration
- **Self-hosted server**: Requires maintenance, hosting costs, complexity

---

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Airtable Base                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │ Events Master│  │  Speakers DB │  │    Tasks     │ │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘ │
│         │                  │                  │         │
│         └──────────────────┴──────────────────┘         │
└─────────────────────────┬───────────────────────────────┘
                          │
                          │ API Query
                          ↓
┌─────────────────────────────────────────────────────────┐
│              GitHub Actions Workflow                    │
│  ┌─────────────────────────────────────────────────┐   │
│  │  Scheduled Trigger: Daily at 9 AM ET            │   │
│  │  Manual Trigger: workflow_dispatch              │   │
│  └─────────────────────┬───────────────────────────┘   │
│                        │                                │
│  ┌─────────────────────▼───────────────────────────┐   │
│  │  Python Email Automation Script                 │   │
│  │  - Query Airtable for upcoming events           │   │
│  │  - Check what emails need to be sent            │   │
│  │  - Load email templates                         │   │
│  │  - Personalize content per recipient            │   │
│  └─────────────────────┬───────────────────────────┘   │
└────────────────────────┼───────────────────────────────┘
                         │
                         │ Authenticate & Send
                         ↓
┌─────────────────────────────────────────────────────────┐
│              Gmail API (Google Workspace)               │
│  - Sends emails from events@democratsabroad.org         │
│  - Supports attachments, HTML, threading                │
│  - Daily limit: 2,000 emails                            │
└─────────────────────────┬───────────────────────────────┘
                          │
                          │ Log activity
                          ↓
┌─────────────────────────────────────────────────────────┐
│         Airtable: Email Communications Table            │
│  - Email type, subject, recipients                      │
│  - Sent timestamp, template used                        │
│  - Delivery status, related event                       │
└─────────────────────────────────────────────────────────┘
```

---

## Email Types & Automation Triggers

### Pre-Event Emails

| Email Type | Trigger Condition | Timing | Recipients | Template |
|-----------|------------------|---------|-----------|----------|
| **Speaker Intake Form** | Speaker added to approved event | 7 days before event | Speaker email | `speaker_intake_form.html` |
| **Event Announcement** | Event status = Approved | 7 days before event | Member mailing list | `event_announcement.html` |
| **Calendar Invite** | Event status = Scheduled | 3 days before event | Member mailing list | `calendar_invite.ics` |
| **Panelist Zoom Links** | Zoom links generated | 3 days before event | All event speakers | `panelist_zoom_link.html` |
| **Run of Show** | Run of Show URL populated | 2 days before event | Speakers + moderator | `run_of_show_share.html` |
| **1-Day Reminder** | Event tomorrow | 1 day before event | Registered attendees (from Zoom) | `event_reminder.html` |

### Post-Event Emails

| Email Type | Trigger Condition | Timing | Recipients | Template |
|-----------|------------------|---------|-----------|----------|
| **Thank You** | Event status = Completed | 1 day after event | All speakers | `speaker_thank_you.html` |
| **Post-Event Survey** | Event status = Completed | 3 days after event | Attendees (from Zoom data) | `post_event_survey.html` |
| **Recording Available** | YouTube URL populated | 3 days after event | Registered attendees | `recording_available.html` |

---

## GitHub Actions Workflow

### Daily Scheduled Check

```yaml
name: Daily Email Automation

on:
  schedule:
    # Runs daily at 9:00 AM Eastern (14:00 UTC)
    - cron: '0 14 * * *'
  workflow_dispatch:  # Allow manual trigger

jobs:
  check-and-send-emails:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python 3.11
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Check for emails to send
        env:
          AIRTABLE_API_KEY: ${{ secrets.AIRTABLE_API_KEY }}
          AIRTABLE_BASE_ID: ${{ secrets.AIRTABLE_BASE_ID }}
          GMAIL_SERVICE_ACCOUNT_JSON: ${{ secrets.GMAIL_SERVICE_ACCOUNT_JSON }}
          GMAIL_DELEGATED_USER: ${{ secrets.GMAIL_DELEGATED_USER }}
        run: |
          python scripts/email_automation.py --check-all

      - name: Upload logs
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: email-logs
          path: logs/email_*.log
```

### Event-Triggered Workflow (Optional)

For immediate emails when critical actions happen:

```yaml
name: Event Email Trigger

on:
  workflow_dispatch:
    inputs:
      email_type:
        description: 'Type of email to send'
        required: true
        type: choice
        options:
          - speaker_intake_form
          - panelist_zoom_link
          - thank_you
      event_id:
        description: 'Airtable Event ID'
        required: true
        type: string
```

---

## Gmail API Setup Process

### 1. Google Cloud Console Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create new project: "DA-Event-Automation"
3. Enable Gmail API
4. Create Service Account with domain-wide delegation
5. Download JSON credentials
6. Grant service account domain-wide authority in Google Workspace Admin

### 2. Required OAuth Scopes

```
https://www.googleapis.com/auth/gmail.send
https://www.googleapis.com/auth/gmail.compose
https://www.googleapis.com/auth/gmail.readonly
```

### 3. GitHub Secrets Configuration

Store these secrets in GitHub repository settings:

| Secret Name | Description | Example |
|------------|-------------|---------|
| `AIRTABLE_API_KEY` | Airtable Personal Access Token | `patAbc123...` |
| `AIRTABLE_BASE_ID` | Base ID for event management | `appXyz789...` |
| `GMAIL_SERVICE_ACCOUNT_JSON` | Full JSON credentials file | `{"type":"service_account",...}` |
| `GMAIL_DELEGATED_USER` | Email to send from | `events@democratsabroad.org` |

---

## Email Template System

### Template Storage Options

**Option A: Airtable Table** (Recommended for non-technical users)
- Create "Email Templates" table
- Fields: Template Name, Subject, Body (HTML), Variables
- Easy to edit without code deployment

**Option B: File-based** (Recommended for version control)
- Store templates in `templates/emails/` directory
- Use Jinja2 for variable substitution
- Commit changes via Git

### Template Variables

All templates support these standard variables:

```python
{
    'event_name': 'Event Title',
    'event_date': 'October 22, 2024',
    'event_time': '9:00 AM ET',
    'speaker_name': 'Jane Smith',
    'speaker_email': 'jane@example.com',
    'zoom_link': 'https://zoom.us/j/...',
    'panelist_link': 'https://zoom.us/s/...',
    'registration_link': 'https://zoom.us/webinar/register/...',
    'organizer_name': 'John Doe',
    'organizer_email': 'john@democratsabroad.org',
    'run_of_show_url': 'https://docs.google.com/...',
    'recording_url': 'https://youtube.com/...',
    'survey_url': 'https://forms.google.com/...'
}
```

### Sample Template (Jinja2)

```html
<!-- templates/emails/speaker_intake_form.html -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Speaker Information Request - {{ event_name }}</title>
</head>
<body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
    <h2>Welcome, {{ speaker_name }}!</h2>

    <p>Thank you for agreeing to speak at our upcoming event:</p>

    <div style="background-color: #f0f0f0; padding: 15px; border-radius: 5px; margin: 20px 0;">
        <strong>{{ event_name }}</strong><br>
        {{ event_date }} at {{ event_time }}
    </div>

    <p>To help us prepare for the event, please complete our speaker intake form:</p>

    <p style="text-align: center; margin: 30px 0;">
        <a href="{{ intake_form_url }}"
           style="background-color: #0066cc; color: white; padding: 12px 30px;
                  text-decoration: none; border-radius: 5px; display: inline-block;">
            Complete Speaker Form
        </a>
    </p>

    <p>The form should take about 5 minutes to complete and includes:</p>
    <ul>
        <li>Biography and photo</li>
        <li>Recording and livestreaming consent</li>
        <li>Technical preferences and requirements</li>
        <li>Team members who will attend</li>
    </ul>

    <p>If you have any questions, please contact:<br>
    {{ organizer_name }}<br>
    <a href="mailto:{{ organizer_email }}">{{ organizer_email }}</a></p>

    <p>We look forward to your participation!</p>

    <hr style="margin-top: 40px; border: none; border-top: 1px solid #ccc;">
    <p style="font-size: 12px; color: #666;">
        Democrats Abroad | <a href="https://democratsabroad.org">democratsabroad.org</a>
    </p>
</body>
</html>
```

---

## Python Script Structure

### Core Script: `scripts/email_automation.py`

```python
"""
Email automation script for Airtable Event Management System.
Checks Airtable for events needing emails and sends via Gmail API.
"""

from pyairtable import Api
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
from jinja2 import Environment, FileSystemLoader
import logging

class EmailAutomation:
    def __init__(self):
        # Initialize Airtable connection
        # Initialize Gmail API connection
        # Load email templates
        pass

    def check_upcoming_events(self):
        """Query Airtable for events in next 7 days"""
        pass

    def check_completed_events(self):
        """Query Airtable for recently completed events"""
        pass

    def should_send_email(self, event, email_type):
        """Determine if specific email should be sent"""
        # Check if already sent (Email Communications table)
        # Check timing requirements
        # Check prerequisites (e.g., Zoom links exist)
        pass

    def send_speaker_intake_form(self, event):
        """Send intake form to all speakers"""
        pass

    def send_panelist_links(self, event):
        """Send unique Zoom panelist links to speakers"""
        pass

    def send_event_announcement(self, event):
        """Send promotional email to member list"""
        pass

    def send_thank_you(self, event):
        """Send thank you to speakers after event"""
        pass

    def log_to_airtable(self, email_data):
        """Log sent email to Email Communications table"""
        pass

    def send_via_gmail(self, to, subject, html_body, attachments=None):
        """Send email via Gmail API"""
        pass

if __name__ == "__main__":
    automation = EmailAutomation()
    automation.check_upcoming_events()
    automation.check_completed_events()
```

---

## Error Handling & Monitoring

### Logging Strategy

1. **File-based logs**: `logs/email_YYYY-MM-DD.log`
2. **Airtable logging**: All sent emails in Email Communications table
3. **GitHub Actions artifacts**: Upload logs after each run

### Error Scenarios

| Error | Handling Strategy |
|-------|------------------|
| **Gmail API quota exceeded** | Log error, retry next day, alert admin |
| **Airtable API failure** | Retry with exponential backoff (3 attempts) |
| **Invalid email address** | Log warning, skip recipient, continue |
| **Template rendering error** | Log error, alert admin, skip email |
| **Network timeout** | Retry once, then fail gracefully |

### Monitoring & Alerts

- **Daily summary email** to admin with count of emails sent/failed
- **GitHub Actions notifications** on workflow failure
- **Airtable view** for failed emails (Delivery Status = "Failed")

---

## Testing Strategy

### Local Testing

```bash
# Test with dry-run mode (don't actually send)
python scripts/email_automation.py --dry-run --event-id recXYZ123

# Test specific email type
python scripts/email_automation.py --test-email speaker_intake_form --to test@example.com

# Test template rendering
python scripts/email_automation.py --render-template speaker_intake_form --event-id recXYZ123
```

### Staging Environment

1. Create separate Airtable base for testing
2. Use test email addresses (team members only)
3. Test all email types before production deployment

---

## Rollout Plan

### Phase 2A: Email Infrastructure Setup (Week 1-2)

1. **Week 1: Gmail API Setup**
   - Set up Google Cloud project
   - Create service account
   - Configure domain-wide delegation
   - Test authentication locally

2. **Week 2: Script Development**
   - Build core `email_automation.py`
   - Create email templates
   - Implement Airtable logging
   - Local testing with test events

### Phase 2B: GitHub Actions Integration (Week 3)

1. Set up GitHub Secrets
2. Create workflow YAML files
3. Test scheduled runs
4. Test manual triggers
5. Monitor logs and fix issues

### Phase 2C: Production Rollout (Week 4)

1. Send first real emails (speaker intake forms only)
2. Monitor delivery and responses
3. Gradually enable additional email types
4. Gather feedback and iterate

---

## Success Metrics

### Email Delivery Metrics

- **Delivery rate**: Target 99%+ successful delivery
- **Open rate**: Track for promotional emails (target 30%+)
- **Response rate**: For intake forms (target 80%+ completion)
- **Time saved**: Measure reduction in manual email time (goal: 3-5 hours/week)

### System Metrics

- **Automation reliability**: Target 99%+ scheduled runs succeed
- **Error rate**: < 1% of emails fail to send
- **Processing time**: Daily check completes in < 5 minutes

---

## Future Enhancements

### Phase 3+ Improvements

1. **Email personalization**: Dynamic content based on recipient profile
2. **A/B testing**: Test subject lines and content variants
3. **Advanced analytics**: Click tracking, conversion tracking
4. **SMS notifications**: Critical reminders via Twilio (optional)
5. **Multi-language support**: Template translations for international speakers
6. **Email scheduling**: User-controlled send times per event
7. **Bounce handling**: Automatic cleanup of invalid email addresses

---

## Cost Summary

| Component | Monthly Cost | Notes |
|-----------|-------------|-------|
| Google Workspace | $0 | Already subscribed |
| Gmail API | $0 | Free up to 2,000 emails/day |
| GitHub Actions | $0 | Free for public repos; 2,000 minutes/month for private |
| Airtable | $0 | Part of existing subscription |
| **Total** | **$0/month** | Zero additional cost |

---

## Security Considerations

### Credential Management

- ✅ Service account credentials stored in GitHub Secrets (encrypted)
- ✅ No credentials committed to Git repository
- ✅ Rotate service account keys every 90 days
- ✅ Limit OAuth scopes to minimum required

### Email Security

- ✅ SPF/DKIM configured for democratsabroad.org domain
- ✅ Validate all email addresses before sending
- ✅ Sanitize template variables to prevent injection
- ✅ Rate limiting to prevent abuse

### Data Privacy

- ✅ Log only necessary information (no email body content in logs)
- ✅ Comply with GDPR/privacy regulations
- ✅ Allow users to opt-out of non-critical emails

---

## Support & Maintenance

### Regular Maintenance Tasks

- **Weekly**: Review error logs, check delivery rates
- **Monthly**: Review email templates for updates
- **Quarterly**: Rotate service account credentials, audit permissions
- **Annually**: Review and update email automation strategy

### Documentation

- Maintain runbook for common issues
- Document all email templates and their purpose
- Keep architecture diagrams updated