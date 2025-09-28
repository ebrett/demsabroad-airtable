# Airtable Schema Design

## Overview

This document defines the complete Airtable base structure for the Event Management System, designed to replace the current Google Forms and spreadsheet workflow.

---

## Table 1: Events Master

**Purpose**: Central hub for all event information, linking to speakers, tasks, volunteers, and committees.

### Fields

| Field Name | Field Type | Description | Options/Validation |
|------------|-----------|-------------|-------------------|
| Event ID | Auto Number | Unique identifier | Auto-generated |
| Event Name | Single line text | Event title | Required |
| Event Type | Single select | Type of event | Webinar, Panel, Town Hall, Meet & Greet, Other |
| Event Date | Date | Scheduled date | Required |
| Event Time | Single line text | Time with timezone | Required (format: "9:00 AM ET") |
| Timezone | Single select | Primary timezone | ET, CET, BST, PT, etc. |
| Status | Single select | Current event status | Date Reserved, Draft, Pending Approval, Approved, Scheduled, In Progress, Completed, Cancelled |
| Approval Status | Single select | Approval workflow | Pending, Approved, Needs Revision |
| Approver | Single line text | Name of approver | |
| Host Organization | Multiple select | Hosting entity | Global Caucus names, Country Committees |
| Co-hosts | Multiple select | Co-hosting entities | Same options as Host Organization |
| Overview/Purpose | Long text | Event description and goals | Required |
| Target Audience | Long text | Intended audience description | |
| Expected Attendance | Number | Estimated attendees | |
| Zoom Meeting Link | URL | Zoom webinar/meeting URL | Auto-populated by script |
| Zoom Registration Link | URL | Public registration URL | Auto-populated by script |
| Zoom Meeting ID | Single line text | Zoom meeting ID | Auto-populated by script |
| Recording Consent | Checkbox | Consent to record | |
| Live Stream Consent | Checkbox | Consent to livestream | |
| Live Stream Platform | Multiple select | Where to stream | Facebook, YouTube |
| Recording URL | URL | Link to recorded event | Added post-event |
| Event Organizer Name | Single line text | Name of organizer | Required |
| Event Organizer Email | Email | Organizer contact | Required |
| Speakers | Link to another record | Links to Speakers Database | Multiple allowed |
| Tasks | Link to another record | Links to Tasks & Workflow | Multiple allowed |
| Volunteers | Link to another record | Links to Volunteers & Staff | Multiple allowed |
| Committees | Link to another record | Links to Committees & Caucuses | Multiple allowed |
| NationBuilder Synced | Checkbox | Synced to NationBuilder | Auto-checked by script |
| NationBuilder Event ID | Single line text | NB event identifier | Auto-populated |
| Mighty Networks Posted | Checkbox | Posted to Mighty Networks | Auto-checked by script |
| Mighty Networks URL | URL | Link to MN post | Auto-populated |
| Promotional Email Sent | Checkbox | Member email sent | |
| Foreign Policy Agreement | Checkbox | Speakers acknowledged policy | Required before approval |
| Run of Show Created | Checkbox | Event script/agenda created | |
| Run of Show URL | URL | Link to run of show document | |
| Signal Green Room Created | Checkbox | Speaker green room set up | |
| Signal Green Room Link | URL | Link to Signal chat | |
| Website Posted | Checkbox | Event posted to DA website | |
| Website Event URL | URL | Link to event on website | |
| Calendar Invite Sent | Checkbox | Calendar file sent to members | |
| Thank You Sent | Checkbox | Thank you emails sent to speakers/guests | |
| Post-Event Mighty Posted | Checkbox | Recording/recap posted to Mighty | |
| Post-Event Mighty URL | URL | Link to post-event Mighty post | |
| Video Edited | Checkbox | Recording edited and finalized | |
| Special Instructions | Long text | Any special notes or requirements | |
| Created Date | Created time | Auto-timestamp | Auto-generated |
| Last Modified | Last modified time | Auto-timestamp | Auto-generated |

---

## Table 2: Speakers Database

**Purpose**: Centralized repository of all speaker information for easy reuse across events.

### Fields

| Field Name | Field Type | Description | Options/Validation |
|------------|-----------|-------------|-------------------|
| Speaker ID | Auto Number | Unique identifier | Auto-generated |
| Speaker Name | Single line text | Full name | Required |
| Email | Email | Primary contact email | Required |
| Alternate Email | Email | Secondary contact | |
| Timezone | Single select | Speaker's timezone | ET, CET, BST, PT, AEDT, etc. |
| Phone | Phone number | Contact number | |
| Photo | Attachment | Headshot/profile photo | Image files |
| Photo URL | URL | Link to photo (Google Drive, etc.) | |
| Bio | Long text | Speaker biography | |
| Bio Short | Long text | Shortened bio (1-2 paragraphs) | |
| Title/Role | Single line text | Current position | |
| Organization | Single line text | Affiliated organization | |
| DA Connection | Long text | How speaker connected with DA | |
| Speaker Type | Single select | Category of speaker | Elected Official, Candidate, Author, Academic, Activist, DA Member, Expert, Other |
| Specialties/Topics | Multiple select | Areas of expertise | List of common topics |
| Social Media - LinkedIn | URL | LinkedIn profile | |
| Social Media - Twitter/X | URL | Twitter handle/profile | |
| Social Media - Facebook | URL | Facebook profile | |
| Social Media - Instagram | URL | Instagram handle | |
| Website | URL | Personal or professional website | |
| Past Events | Link to another record | Links to Events Master | Multiple allowed |
| Total Events | Count | Number of events participated in | Auto-calculated from Past Events |
| Recording Consent Default | Single select | Default recording preference | Always Yes, Always No, Ask Each Time |
| Livestream Consent Default | Single select | Default livestream preference | Always Yes, Always No, Ask Each Time |
| Team Members | Long text | Names/emails of staff who attend | Format: Name (email) |
| Availability Notes | Long text | General availability or constraints | |
| Topics to Avoid | Long text | Sensitive topics to avoid | |
| Foreign Policy Agreement Signed | Checkbox | Has acknowledged DA policy | |
| Promotional Consent | Checkbox | OK with DA promotion | Default checked |
| Status | Single select | Speaker status | Active, Inactive, Do Not Contact |
| Notes | Long text | Internal notes about speaker | |
| First Event Date | Date | Date of first DA event | Auto-calculated |
| Last Event Date | Date | Date of most recent event | Auto-calculated |
| Created Date | Created time | Record creation date | Auto-generated |
| Last Modified | Last modified time | Last update | Auto-generated |

---

## Table 3: Tasks & Workflow

**Purpose**: Track all tasks associated with events, with automated task creation for standard workflows.

### Fields

| Field Name | Field Type | Description | Options/Validation |
|------------|-----------|-------------|-------------------|
| Task ID | Auto Number | Unique identifier | Auto-generated |
| Task Name | Single line text | Task description | Required |
| Event | Link to another record | Links to Events Master | Required |
| Task Type | Single select | Category of task | Graphics, Email, Social Media, Zoom Setup, Platform Posting, Video Editing, Documentation, Follow-up, Other |
| Task Category | Single select | Workflow phase | Pre-Event, During Event, Post-Event |
| Status | Single select | Current status | Not Started, In Progress, Completed, Blocked, Cancelled |
| Priority | Single select | Task priority | Low, Medium, High, Urgent |
| Due Date | Date | Deadline | |
| Assigned To | Link to another record | Links to Volunteers & Staff | |
| Description | Long text | Task details | |
| Checklist | Long text | Sub-tasks (one per line) | |
| Dependencies | Link to another record | Other tasks that must complete first | Links to Tasks & Workflow |
| Automation Type | Single select | If auto-created | Standard, Custom |
| Platform | Single select | For posting tasks | NationBuilder, Mighty Networks, Facebook, YouTube, Website, Email, Signal |
| Email Type | Single select | Type of email communication | Announcement, Calendar Invite, Speaker Intake Form, Panelist Zoom Link, Thank You, Reminder, Survey, Other |
| Email Sent Date | Date | When email was sent | |
| Email Recipients | Long text | Who received the email | |
| Email Template Used | Single line text | Name of email template | |
| Completion Notes | Long text | Notes added when completed | |
| Created Date | Created time | Auto-timestamp | Auto-generated |
| Completed Date | Date | When task was completed | |
| Last Modified | Last modified time | Auto-timestamp | Auto-generated |

### Standard Workflow Tasks (Auto-Created)

When a new event is approved, these tasks are automatically created:

#### Pre-Event Tasks (14 tasks):
1. **Reserve Date/Time** (Immediate) - Confirm date/time reservation, update status to "Date Reserved"
2. **Create Event on Website** (10 days before) - Post event details to DA website
3. **Graphics Request** (10 days before) - Request promotional graphics from comms team
4. **Zoom Meeting Setup** (8 days before) - Create Zoom meeting/webinar and get registration link
5. **NationBuilder Post** (7 days before) - Publish event to NationBuilder
6. **Mighty Networks Post** (7 days before) - Post event announcement to Mighty Networks
7. **Email Announcement** (7 days before) - Send promotional email to members
8. **Send Webinar Intake Form** (7 days before) - Email intake form to all speakers
9. **Create Run of Show** (5 days before) - Draft event script/agenda document
10. **Send Panelist Zoom Links** (3 days before) - Email unique panelist links to all speakers
11. **Invite to Signal Green Room** (3 days before) - Set up and invite speakers to Signal chat
12. **Send Calendar Invite** (3 days before) - Send .ics calendar file to member list
13. **Moderator Prep** (2 days before) - Send questions to moderator/speaker if requested
14. **Social Media Reminder** (1 day before) - Post reminder on social channels

#### During Event Tasks (1 task):
15. **Hold Event** (Event day) - Execute event, track attendance

#### Post-Event Tasks (5 tasks):
16. **Send Thank You** (1 day after) - Email thank you to speakers and special guests
17. **Edit Video** (2 days after) - Edit recording, add intro/outro, captions
18. **Upload to YouTube** (3 days after) - Upload edited video to YouTube channel
19. **Post Recording to Mighty** (3 days after) - Share recording/recap on Mighty Networks
20. **Post-Event Survey** (3 days after) - Send follow-up survey to attendees

---

## Table 4: Volunteers & Staff

**Purpose**: Track people who support events (volunteers, staff, moderators, tech support).

### Fields

| Field Name | Field Type | Description | Options/Validation |
|------------|-----------|-------------|-------------------|
| Person ID | Auto Number | Unique identifier | Auto-generated |
| Name | Single line text | Full name | Required |
| Email | Email | Contact email | Required |
| Phone | Phone number | Contact number | |
| Timezone | Single select | Volunteer's timezone | ET, CET, BST, PT, etc. |
| Role Type | Multiple select | Type of role(s) | Moderator, Tech Support, Graphics, Social Media, Outreach, General Volunteer, Staff |
| Availability | Long text | General availability notes | |
| Skills | Multiple select | Specific skills | Zoom Management, Graphic Design, Social Media, Writing, Translation, etc. |
| Languages | Multiple select | Languages spoken | English, Spanish, French, German, etc. |
| Country Committee | Single select | Local affiliation | List of country committees |
| Caucus Membership | Multiple select | Caucus affiliations | List of caucuses |
| Events Assigned | Link to another record | Links to Events Master | Multiple allowed |
| Tasks Assigned | Link to another record | Links to Tasks & Workflow | Multiple allowed |
| Total Events | Count | Number of events helped with | Auto-calculated |
| Status | Single select | Current status | Active, Inactive, On Leave |
| Notes | Long text | Internal notes | |
| Created Date | Created time | Record creation date | Auto-generated |
| Last Modified | Last modified time | Last update | Auto-generated |

---

## Table 5: Committees & Caucuses

**Purpose**: Track organizing entities (country committees, global teams, caucuses) and their event involvement.

### Fields

| Field Name | Field Type | Description | Options/Validation |
|------------|-----------|-------------|-------------------|
| Organization ID | Auto Number | Unique identifier | Auto-generated |
| Name | Single line text | Official name | Required |
| Type | Single select | Organization type | Country Committee, Global Team, Global Caucus, Chapter |
| Region | Single select | Geographic region | Americas, EMEA, Asia Pacific, Global |
| Primary Contact Name | Single line text | Leader/chair name | |
| Primary Contact Email | Email | Leader/chair email | |
| Events Hosted | Link to another record | Links to Events Master (as host) | Multiple allowed |
| Events Co-Hosted | Link to another record | Links to Events Master (as co-host) | Multiple allowed |
| Total Events | Count | Total events involved in | Auto-calculated |
| Members Count | Number | Approximate membership size | |
| Status | Single select | Current status | Active, Inactive |
| Description | Long text | Brief description of group | |
| Website | URL | Organization website/page | |
| Social Media | Long text | Social media handles | |
| Notes | Long text | Internal notes | |
| Created Date | Created time | Record creation date | Auto-generated |
| Last Modified | Last modified time | Last update | Auto-generated |

---

## Table 6: Email Communications

**Purpose**: Track all email communications sent for events, including templates and delivery status.

### Fields

| Field Name | Field Type | Description | Options/Validation |
|------------|-----------|-------------|-------------------|
| Email ID | Auto Number | Unique identifier | Auto-generated |
| Email Type | Single select | Type of communication | Announcement, Calendar Invite, Speaker Intake Form, Panelist Zoom Link, Thank You, Reminder, Survey, Run of Show, Other |
| Event | Link to another record | Links to Events Master | Required |
| Related Task | Link to another record | Links to Tasks & Workflow | If applicable |
| Subject Line | Single line text | Email subject | Required |
| Template Name | Single select | Pre-built template used | List of standard templates |
| Recipients | Long text | Email addresses (one per line) | |
| Recipient Count | Number | Total recipients | |
| Sent Date | Date & Time | When email was sent | |
| Sent By | Link to another record | Links to Volunteers & Staff | |
| Delivery Status | Single select | Email delivery status | Draft, Scheduled, Sent, Failed |
| Email Body | Long text | Email content/body | |
| Attachments | Attachment | Files attached to email | |
| Reply-To Email | Email | Reply-to address | |
| Opens | Number | Email open count (if tracked) | |
| Clicks | Number | Link click count (if tracked) | |
| Notes | Long text | Additional notes | |
| Created Date | Created time | Record creation | Auto-generated |
| Last Modified | Last modified time | Last update | Auto-generated |

---

## Table 7: Reports & Analytics

**Purpose**: Store generated reports and analytics data for historical tracking.

### Fields

| Field Name | Field Type | Description | Options/Validation |
|------------|-----------|-------------|-------------------|
| Report ID | Auto Number | Unique identifier | Auto-generated |
| Report Name | Single line text | Report title | Required |
| Report Type | Single select | Category of report | Attendance Summary, Speaker Frequency, Event Performance, Volunteer Activity, Caucus Engagement, Monthly Summary, Quarterly Summary |
| Date Range Start | Date | Report period start | Required |
| Date Range End | Date | Report period end | Required |
| Generated Date | Date | When report was created | Auto-filled |
| Report File | Attachment | PDF/CSV file | |
| Report URL | URL | Link to report (if hosted externally) | |
| Key Metrics | Long text | Summary of key findings | |
| Events Included | Link to another record | Links to Events Master | Multiple allowed |
| Notes | Long text | Additional context or insights | |
| Created By | Single line text | Who/what generated report | System or person name |

---

## Key Relationships

### Primary Relationships:
1. **Events Master → Speakers Database**: Many-to-many (one event has multiple speakers; one speaker attends multiple events)
2. **Events Master → Tasks & Workflow**: One-to-many (one event has many tasks)
3. **Events Master → Volunteers & Staff**: Many-to-many (one event has multiple volunteers; one volunteer works multiple events)
4. **Events Master → Committees & Caucuses**: Many-to-many (one event has multiple organizing groups; one group hosts multiple events)
5. **Events Master → Email Communications**: One-to-many (one event has many emails sent)
6. **Tasks & Workflow → Volunteers & Staff**: Many-to-many (one task can be assigned to multiple people; one person can have multiple tasks)
7. **Tasks & Workflow → Email Communications**: One-to-many (one task may trigger multiple emails)
8. **Email Communications → Volunteers & Staff**: Many-to-one (emails are sent by staff members)
9. **Reports & Analytics → Events Master**: Many-to-many (one report covers multiple events)

---

## Form Mappings

### Event Request Form → Events Master Table

| Google Form Field | Airtable Field |
|------------------|----------------|
| Timestamp | Created Date |
| Email Address | Event Organizer Email |
| Your name | Event Organizer Name |
| Which Country Committee... | Host Organization, Co-hosts |
| Name of speaker(s) | Speakers (linked) |
| Speaker connection with DA | Special Instructions (include context) |
| Overview | Overview/Purpose |
| Audience | Target Audience, Expected Attendance |
| Event date and timing | Event Date, Event Time, Timezone |
| Status of Approval | Approval Status |
| Approver | Approver |

### Webinar Intake Form → Speakers Database Table

| Google Form Field | Airtable Field |
|------------------|----------------|
| Timestamp | Created Date |
| Email Address | Email (requestor - may differ from speaker) |
| Speaker Name | Speaker Name |
| Please add the name and email... | Team Members |
| What time zone is the speaker in? | Timezone |
| Please upload a photo... | Photo URL, Photo |
| Please provide a bio... | Bio |
| Will anyone from the speaker's team... | Team Members (conditional) |
| If yes, please add the name(s)... | Team Members |
| Do you consent to recording...? | Recording Consent Default |
| Do you consent to live-streaming...? | Livestream Consent Default |
| Should we send questions...? | Notes (include preference) |
| Are you willing to take questions...? | Notes (include preference) |
| Are there any topics we should avoid? | Topics to Avoid |
| Promotion | Promotional Consent |
| Additional information | Notes |
| Do you have any questions? | Notes |
| Foreign policy statement | Foreign Policy Agreement Signed |

---

## Views Recommendations

### Events Master Views:
1. **All Events** - Default grid view
2. **Upcoming Events** - Filtered to future dates, sorted by date
3. **Events Pending Approval** - Filtered to "Pending Approval" status
4. **Events This Month** - Calendar view
5. **By Caucus/Committee** - Grouped by Host Organization
6. **Completed Events** - Filtered to "Completed" status

### Speakers Database Views:
1. **All Speakers** - Default grid view
2. **Active Speakers** - Filtered to "Active" status
3. **Frequent Speakers** - Sorted by Total Events (descending)
4. **By Expertise** - Grouped by Specialties/Topics
5. **Recently Added** - Sorted by Created Date (descending)

### Tasks & Workflow Views:
1. **All Tasks** - Default grid view
2. **My Tasks** - Filtered by assigned person
3. **Overdue Tasks** - Filtered to past due date + not completed
4. **By Event** - Grouped by Event
5. **By Status** - Grouped by Status
6. **Timeline** - Timeline view by Due Date

### Volunteers & Staff Views:
1. **All Volunteers** - Default grid view
2. **Active Volunteers** - Filtered to "Active" status
3. **By Role** - Grouped by Role Type
4. **By Skills** - Grouped by Skills
5. **Most Active** - Sorted by Total Events (descending)

---

## Automation Recommendations

### Airtable Native Automations:
1. **New Event Approved** → Create standard workflow tasks
2. **Event Date Approaching** → Send reminders 7, 3, 1 days before
3. **Task Overdue** → Notify assigned person
4. **Speaker Added to Event** → Send confirmation email
5. **Event Completed** → Update status, trigger post-event tasks

### Python Script Automations:
1. **Zoom Integration** → Create meetings, update links
2. **NationBuilder Sync** → Publish events when approved
3. **Mighty Networks Post** → Auto-post event announcements
4. **Email Campaigns** → Send promotional emails to member list
5. **Attendance Data Sync** → Pull Zoom registration/attendance data post-event
6. **Weekly Reports** → Generate and email summary reports

---

## Reporting Capabilities

### Available Reports (Via Python Scripts)

#### 1. **Event Management Reports**
- **Upcoming Events Report** - All scheduled events with status, speakers, and task completion %
- **Event History Report** - Past events with attendance, recording views, survey results
- **Events by Caucus/Committee** - Breakdown of events hosted by each organizing group
- **Event Timeline Report** - Gantt-style view of all events and their task deadlines

#### 2. **Task Tracking Reports**
- **Task Status Dashboard** - All tasks grouped by status (Not Started, In Progress, Completed, Blocked)
- **Overdue Tasks Report** - Tasks past due date with assigned person and event
- **Task Completion Rate** - Percentage of tasks completed on time vs late
- **Task Assignment Report** - Who is assigned to what, workload distribution

#### 3. **Communication Reports**
- **Email Activity Report** - All emails sent, by type, with open/click rates
- **Speaker Communication Tracking** - Status of intake forms sent/received, thank yous sent
- **Platform Posting Report** - Track which events were posted to which platforms (NationBuilder, Mighty, Website, YouTube)

#### 4. **Speaker Reports**
- **Speaker Frequency Report** - Most frequent speakers, total events per speaker
- **Speaker Database Report** - All active speakers with contact info and expertise
- **New vs Returning Speakers** - Breakdown of new speakers vs repeat speakers per time period
- **Speaker Consent Summary** - Recording/livestream consent status for all speakers

#### 5. **Volunteer Reports**
- **Volunteer Activity Report** - Events and tasks completed per volunteer
- **Volunteer Skills Matrix** - Available volunteers by skill type
- **Most Active Volunteers** - Top 10 volunteers by contribution

#### 6. **Analytics Reports**
- **Monthly Summary** - Total events, attendance, tasks completed, emails sent
- **Quarterly Summary** - Trends over 3 months with comparisons to previous quarter
- **Year-End Report** - Annual statistics and highlights
- **Attendance Trends** - Average attendance by event type, caucus, time of day

### Report Formats
- **PDF** - Formatted reports for sharing with leadership
- **CSV/Excel** - Raw data exports for further analysis
- **HTML Dashboard** - Interactive web-based reports (if Flask/FastAPI added later)
- **Email Summary** - Automated weekly/monthly email digests

### Report Automation
Python scripts can be scheduled to automatically generate and email reports:
- **Weekly**: Upcoming events, overdue tasks
- **Monthly**: Full event summary, speaker activity, volunteer contributions
- **Quarterly**: Trend analysis, performance metrics
- **Ad-hoc**: On-demand custom reports via command line

---

## Migration Plan

### Phase 1: Structure Setup
1. Create all 7 tables in Airtable
2. Set up field types and validations
3. Configure relationships between tables
4. Create recommended views
5. Set up base-level permissions

### Phase 2: Data Migration
1. Import existing event data from Google Sheets
2. Import speaker data from webinar intake forms
3. De-duplicate and clean data
4. Verify relationships are properly linked

### Phase 3: Forms Setup
1. Create Airtable form for event requests (replacing Google Form)
2. Create Airtable form for speaker intake (replacing Google Form)
3. Set up form notifications and automations
4. Test form submissions end-to-end

### Phase 4: Integration & Automation
1. Develop Python scripts for API integrations
2. Test Zoom, NationBuilder, Mighty Networks connections
3. Implement task automation workflows
4. Set up scheduled report generation

### Phase 5: Training & Rollout
1. Train event organizers on new system
2. Create documentation and video tutorials
3. Parallel run with old system for 2 weeks
4. Full transition to Airtable system
5. Decommission Google Forms