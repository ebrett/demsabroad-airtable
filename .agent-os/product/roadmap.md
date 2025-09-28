# Product Roadmap

**Project:** Democrats Abroad Event Management System
**Started:** September 28, 2025
**Current Phase:** Phase 2 (Not Started)
**Last Updated:** September 28, 2025

## Overview

This roadmap outlines the 4-phase development plan for the DA Event Management System, which replaces manual Google Forms and spreadsheet workflows with an automated Airtable-based solution.

### Phase Summary

| Phase | Status | Focus |
|-------|--------|-------|
| **Phase 1** | ✅ Complete | Foundation & Airtable Setup |
| **Phase 2** | 📋 Planned | Core Automation & Integrations |
| **Phase 3** | 📋 Planned | Post-Event Automation & Video |
| **Phase 4** | 📋 Planned | Reporting & Analytics |

---

## Phase 1: Foundation & Airtable Setup ✅ COMPLETE

**Goal:** Establish the Airtable base structure and basic Python connectivity to replace manual Google Forms workflow.

**Status:** ✅ **Completed September 28, 2025**

**Success Criteria:** ✅ All Met
- ✅ Airtable base created with all 7 tables properly structured and related
- ✅ Python scripts can read/write to Airtable successfully
- ✅ Event intake form and speaker intake form functional and populating database
- ⚠️ Standard workflow tasks (manual creation for now - automation deferred to Phase 2)

### Features

- [x] Design and create Airtable base schema - Define all 7 tables (Events Master, Speakers, Tasks & Workflow, Volunteers & Staff, Committees & Caucuses, Email Communications, Reports & Analytics) with proper fields and relationships (167 total fields) `M` ✅
- [x] Build event intake form in Airtable - Replace Google Form with Airtable form that captures all webinar details and auto-populates Events Master table `S` ✅
- [x] Create speaker intake form in Airtable - Replace webinar intake Google Form with Airtable form for speaker details, consent, bio, photo, and preferences `S` ✅
- [x] Create Email Communications table - Set up table to track all email communications with templates, delivery status, and recipient tracking `S` ✅
- [x] Set up Python development environment - Install Python 3.12, pyairtable, python-dotenv via uv package manager with virtual environment `XS` ✅
- [x] Implement basic Airtable connectivity - Created test_airtable_connection.py with authentication, table access verification, and error handling `S` ✅
- [x] Create Event Coordinator Dashboard - Built 4-page dashboard interface with overview, events grid, speakers grid, and tasks board `M` ✅
- [x] Create views for all tables - Built 15+ views including Upcoming Events, Pending Approval, Overdue Tasks, Active Speakers, etc. `S` ✅
- [ ] Build speaker lookup functionality - Python script to search existing speakers and pre-populate form data for repeat speakers `M` (Deferred to Phase 2)
- [ ] Implement standard workflow task automation - Script to auto-create 20 standard tasks (pre-event, during, post-event) when event is approved with proper due dates `M` (Deferred to Phase 2 - Priority #1)
- [ ] Create email templates - Design standard email templates for announcements, intake forms, panelist links, thank yous, reminders, and surveys `S` (Deferred to Phase 2)

### Dependencies ✅

- ✅ Airtable account with API access (Pro/Plus plan)
- ✅ Python 3.12 installed locally with uv package manager
- ✅ API credentials secured in .env file
- ✅ Base ID: appL5mQf4myxTXpMv

### Key Deliverables

- **Airtable Base:** 7 tables, 167 fields, 15+ views, 2 forms, 1 dashboard
- **Documentation:** mission.md, airtable-schema.md, phase1 spec, email automation plan
- **Code:** test_airtable_connection.py, Python environment setup
- **Time Investment:** ~8 hours total

## Phase 2: Core Automation & Integrations 📋 PLANNED

**Goal:** Automate the webinar creation, cross-platform publishing, and email communication workflow to eliminate manual data entry.

**Status:** 📋 **Not Started**

**Priority Tasks:**
1. **Task Automation Script** - Auto-create 20 standard tasks when event approved
2. **Email Infrastructure** - Gmail API integration and template system
3. **Zoom Integration** - Auto-create meetings and distribute panelist links
4. **Platform Publishing** - NationBuilder and Mighty Networks automation

**Success Criteria:**
- Events automatically create Zoom meetings with registration links
- Event details automatically post to NationBuilder, Mighty Networks, and DA website
- Task workflow automation functioning for each new event with 20 standard tasks
- Email automation via Gmail API sends intake forms, panelist links, announcements, and thank yous automatically
- GitHub Actions runs daily automated checks and email distribution

### Phase 2A: Email Infrastructure Setup

- [ ] Google Cloud Console setup - Create project, enable Gmail API, configure service account with domain-wide delegation `S`
- [ ] Gmail API authentication - Create and test service account credentials, configure OAuth scopes, verify email sending works `M`
- [ ] Email template system - Create 9 HTML email templates using Jinja2 (intake form, announcement, calendar invite, panelist links, run of show, reminder, thank you, survey, recording available) `M`
- [ ] Email Communications table setup - Configure Airtable table with proper fields for tracking all sent emails with delivery status and recipients `S`
- [ ] Core email automation script - Build `scripts/email_automation.py` with Gmail API integration, Airtable logging, template rendering, and error handling `L`
- [ ] Local testing - Test all email types with test events and verify Airtable logging works correctly `M`

### Phase 2B: GitHub Actions Integration

- [ ] GitHub Secrets configuration - Store Airtable API key, Gmail credentials, and other sensitive data in GitHub repository secrets `XS`
- [ ] Daily email workflow - Create `.github/workflows/daily-email-automation.yml` with scheduled trigger at 9 AM ET `S`
- [ ] Manual trigger workflow - Create workflow_dispatch for on-demand email sending by email type and event ID `S`
- [ ] Workflow testing - Test scheduled runs, manual triggers, verify logs upload, and confirm emails send correctly `M`
- [ ] Error monitoring setup - Configure GitHub Actions notifications and daily summary email to admin `S`

### Phase 2C: Platform Integrations

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

## Phase 3: Post-Event Automation & Video Workflow 📋 PLANNED

**Goal:** Automate post-event tasks including thank you emails, video editing workflow, and multi-platform distribution.

**Status:** 📋 **Not Started**

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

## Phase 4: Reporting, Analytics & Workflow Polish 📋 PLANNED

**Goal:** Provide automated insights and analytics while refining the user experience based on real-world usage.

**Status:** 📋 **Not Started**

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