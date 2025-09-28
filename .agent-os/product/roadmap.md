# Product Roadmap

## Phase 1: Foundation & Airtable Setup

**Goal:** Establish the Airtable base structure and basic Python connectivity to replace manual Google Forms workflow.

**Success Criteria:**
- Airtable base created with all 7 tables properly structured and related
- Python scripts can read/write to Airtable successfully
- Event intake form and speaker intake form functional and populating database
- 20 standard workflow tasks auto-create when events are approved

### Features

- [ ] Design and create Airtable base schema - Define all 7 tables (Events Master, Speakers Database, Tasks & Workflow, Volunteers & Staff, Committees & Caucuses, Email Communications, Reports & Analytics) with proper fields and relationships `M`
- [ ] Build event intake form in Airtable - Replace Google Form with Airtable form that captures all webinar details and auto-populates Events Master table `S`
- [ ] Create speaker intake form in Airtable - Replace webinar intake Google Form with Airtable form for speaker details, consent, bio, photo, and preferences `S`
- [ ] Create Email Communications table - Set up table to track all email communications with templates, delivery status, and recipient tracking `S`
- [ ] Set up Python development environment - Install Python 3.11+, pyairtable, python-dotenv, and initialize project structure with folders for scripts and config `XS`
- [ ] Implement basic Airtable connectivity - Create airtable_sync.py with authentication, basic CRUD operations, and error handling `S`
- [ ] Build speaker lookup functionality - Python script to search existing speakers and pre-populate form data for repeat speakers `M`
- [ ] Implement standard workflow task automation - Script to auto-create 20 standard tasks (pre-event, during, post-event) when event is approved with proper due dates `M`
- [ ] Create email templates - Design standard email templates for announcements, intake forms, panelist links, thank yous, reminders, and surveys `S`

### Dependencies

- Airtable account with API access
- Python 3.11+ installed locally
- API credentials secured in .env file

## Phase 2: Core Automation & Integrations

**Goal:** Automate the webinar creation, cross-platform publishing, and email communication workflow to eliminate manual data entry.

**Success Criteria:**
- Events automatically create Zoom meetings with registration links
- Event details automatically post to NationBuilder, Mighty Networks, and DA website
- Task workflow automation functioning for each new event with 20 standard tasks
- Email automation via Gmail API sends intake forms, panelist links, announcements, and thank yous automatically
- GitHub Actions runs daily automated checks and email distribution

### Phase 2A: Email Infrastructure Setup (Weeks 1-2)

- [ ] Google Cloud Console setup - Create project, enable Gmail API, configure service account with domain-wide delegation `S`
- [ ] Gmail API authentication - Create and test service account credentials, configure OAuth scopes, verify email sending works `M`
- [ ] Email template system - Create 9 HTML email templates using Jinja2 (intake form, announcement, calendar invite, panelist links, run of show, reminder, thank you, survey, recording available) `M`
- [ ] Email Communications table setup - Configure Airtable table with proper fields for tracking all sent emails with delivery status and recipients `S`
- [ ] Core email automation script - Build `scripts/email_automation.py` with Gmail API integration, Airtable logging, template rendering, and error handling `L`
- [ ] Local testing - Test all email types with test events and verify Airtable logging works correctly `M`

### Phase 2B: GitHub Actions Integration (Week 3)

- [ ] GitHub Secrets configuration - Store Airtable API key, Gmail credentials, and other sensitive data in GitHub repository secrets `XS`
- [ ] Daily email workflow - Create `.github/workflows/daily-email-automation.yml` with scheduled trigger at 9 AM ET `S`
- [ ] Manual trigger workflow - Create workflow_dispatch for on-demand email sending by email type and event ID `S`
- [ ] Workflow testing - Test scheduled runs, manual triggers, verify logs upload, and confirm emails send correctly `M`
- [ ] Error monitoring setup - Configure GitHub Actions notifications and daily summary email to admin `S`

### Phase 2C: Platform Integrations (Weeks 4-6)

- [ ] Zoom API integration - Script to automatically create Zoom meetings/webinars from Airtable event data, store registration links, and generate unique panelist links for speakers `L`
- [ ] Speaker intake form email automation - Automatically send webinar intake form to speakers when added to event, track responses in Email Communications table `M`
- [ ] Panelist link distribution - Automatically email unique Zoom panelist links to all speakers 3 days before event `S`
- [ ] Calendar invite generation - Create and send .ics calendar files to member list 3 days before event `M`
- [ ] NationBuilder event publisher - Automated sync script that pushes event details to NationBuilder when event status changes to "Approved" `L`
- [ ] Mighty Networks posting automation - Script to format and post event announcements to Mighty Networks community platform (pre-event) `M`
- [ ] DA Website event posting - Script to publish event details to Democrats Abroad website via API or CMS integration `M`
- [ ] Run of Show generation - Automatically create event script/agenda template document with speaker info and timing `S`
- [ ] Signal green room setup - Create Signal group chat and invite speakers/moderators 3 days before event `S`
- [ ] Attendee data sync - Script to pull Zoom registration/attendance data back into Airtable after events for reporting `M`

### Dependencies

- Google Workspace account with admin access for domain-wide delegation
- Google Cloud Console project with Gmail API enabled
- GitHub repository with Actions enabled
- Zoom account with API access (Pro or higher)
- NationBuilder account with API credentials
- Mighty Networks API access or alternative posting method
- DA Website CMS access or API credentials
- Signal account for green room coordination

## Phase 3: Post-Event Automation & Video Workflow

**Goal:** Automate post-event tasks including thank you emails, video editing workflow, and multi-platform distribution.

**Success Criteria:**
- Automated thank you emails sent to speakers within 24 hours of event
- Video editing workflow tracked from recording to YouTube upload
- Post-event content distributed to Mighty Networks automatically
- Post-event surveys sent and responses tracked

### Features

- [ ] Thank you email automation - Automatically send personalized thank you emails to speakers and special guests 1 day after event `S`
- [ ] Video editing workflow tracking - Create task tracking for video download, editing (intro/outro, captions), and quality review phases `M`
- [ ] YouTube upload automation - Script to upload edited videos to YouTube with proper titles, descriptions, tags, and thumbnails `M`
- [ ] Post-event Mighty Networks posting - Automatically post recording links and event recap to Mighty Networks 3 days after event `S`
- [ ] Post-event survey automation - Automatically send post-event surveys to attendees and sync responses back to Airtable for analysis `S`
- [ ] Recording download automation - Automatically download Zoom cloud recordings when available and store in designated folder `M`

### Dependencies

- YouTube account with API access for Democrats Abroad channel
- Video editing guidelines and templates
- Survey platform integration (Google Forms, Typeform, or Airtable forms)
- Cloud storage for video files (Google Drive, Dropbox, or AWS S3)

## Phase 4: Reporting, Analytics & Workflow Polish

**Goal:** Provide automated insights and analytics while refining the user experience based on real-world usage.

**Success Criteria:**
- Automated weekly/monthly reports generated from Airtable data
- Volunteer coordination and committee management features operational
- System handles 15+ events per month smoothly with minimal manual intervention
- Comprehensive email tracking and communication analytics available

### Features

- [ ] Report generation scripts - Python scripts to generate 23+ different reports including event management, task tracking, email activity, speaker frequency, volunteer contributions, and trends with CSV/PDF export `L`
- [ ] Email analytics dashboard - Report on all email communications sent, delivery rates, open/click rates, and response tracking `M`
- [ ] Task completion analytics - Reports on task completion rates, overdue tasks, and workload distribution across volunteers `M`
- [ ] Volunteer & staff management - Implement volunteer assignment tracking, availability calendars, and automated role notifications `M`
- [ ] Committee & caucus organization - Build features to track organizing committees, caucus groups, and collaborative planning workflows `M`
- [ ] Post-event survey automation - Automatically send post-event surveys and sync responses back to Airtable for analysis `S`
- [ ] Dashboard views in Airtable - Create optimized Airtable views for different user roles (event coordinators, volunteer managers, leadership) `S`
- [ ] Error handling and logging - Comprehensive logging system for all scripts with error notifications and retry logic `M`
- [ ] Scheduled automation setup - Configure cron jobs or GitHub Actions for automated daily/weekly script execution `S`

### Dependencies

- Sufficient event data collected from Phase 2 usage
- Feedback from event coordinators on workflow pain points
- Cloud hosting decision finalized if moving beyond local execution