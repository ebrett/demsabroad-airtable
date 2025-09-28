# Airtable Schema Design

## Overview

This document defines the complete Airtable base structure for the Event Management System, designed to replace the current Google Forms and spreadsheet workflow.

**Last Updated:** September 28, 2025 (from live API schema)

---

## Table 1: Events Master

**Purpose**: Central hub for all event information, linking to speakers, tasks, volunteers, and committees.

**Table ID**: `tbldUqVq6Er0ivwFW`

### Fields (50)

| Field Name | Field Type | Description | Options/Validation |
|------------|-----------|-------------|-------------------|
| Event Name | Single line text | Event title | Required |
| Event Type | Single select | Type of event | Webinar, Panel, Town Hall, Meet & Greet, Other |
| Event Date | Date | Scheduled date | Required |
| Event Time | Single line text | Time (all events in ET) | Required (format: "9:00 AM ET") |
| Status | Single select | Current event status | Date Reserved, Draft, Pending Approval, Approved, Scheduled, In Progress, Completed, Cancelled |
| Host Organization | Multiple select | Hosting entity | Global Black Caucus, Global Disability Caucus, Global LGBTQ+ Caucus, Global Seniors Caucus, Global Women's Caucus, Global Youth Caucus, Global Veterans & Military Families Caucus, Global Environmental & Climate Caucus, Global Asian Pacific Islander Caucus, Global Latino Caucus |
| Co-hosts | Multiple select | Co-hosting entities | Same options as Host Organization |
| Overview/Purpose | Rich text | Event description and goals | Required |
| Target Audience | Multi-line text | Intended audience description | |
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
| Calendar Invite Sent | Checkbox | Calendar file sent to members | |
| Thank You Sent | Checkbox | Thank you emails sent to speakers/guests | |
| Post-Event Mighty Posted | Checkbox | Recording/recap posted to Mighty | |
| Post-Event Mighty URL | URL | Link to post-event Mighty post | |
| Video Edited | Checkbox | Recording edited and finalized | |
| Special Instructions | Multi-line text | Any special notes or requirements | |
| Created Date | Created time | Auto-timestamp | Auto-generated |
| Last Modified | Last modified time | Auto-timestamp | Auto-generated |
| Speakers | Link to another record | Links to Speakers table | Multiple allowed |
| Tasks & Workflow | Link to another record | Links to Tasks & Workflow table | Multiple allowed |
| Volunteers & Staff (Events Assigned) | Link to another record | Links to Volunteers & Staff table | Multiple allowed |
| Volunteers & Staff (Events Approved) | Link to another record | Links to Volunteers & Staff table (approvers) | Multiple allowed |
| Committees & Caucuses (Events Hosted) | Link to another record | Links to Committees & Caucuses table (hosts) | Multiple allowed |
| Committees & Caucuses (Events Co-Hosted) | Link to another record | Links to Committees & Caucuses table (co-hosts) | Multiple allowed |
| Email Communications | Link to another record | Links to Email Communications table | Multiple allowed |
| Reports & Analytics | Link to another record | Links to Reports & Analytics table | Multiple allowed |
| Tasks | Link to another record | Links to Tasks & Workflow table | Multiple allowed (alternate link field) |
| Volunteers | Link to another record | Links to Volunteers & Staff table | Multiple allowed (alternate link field) |
| Committees | Link to another record | Links to Committees & Caucuses table | Multiple allowed (alternate link field) |
| Emails Sent | Link to another record | Links to Email Communications table | Multiple allowed (alternate link field) |
| Reports | Link to another record | Links to Reports & Analytics table | Multiple allowed (alternate link field) |

**Note**: All events use Eastern Time (ET). There is no separate timezone field - all times are assumed to be ET.

---

## Table 2: Speakers

**Purpose**: Centralized repository of all speaker information for easy reuse across events.

**Table ID**: `tblxKGytwTnAucOZT`

### Fields (33)

| Field Name | Field Type | Description | Options/Validation |
|------------|-----------|-------------|-------------------|
| Speaker Name | Single line text | Full name | Required |
| Email | Email | Primary contact email | Required |
| Alternate Email | Email | Secondary contact | |
| Phone | Phone number | Contact number | |
| Photo | Multiple attachments | Headshot/profile photo | Image files |
| Photo URL | URL | Link to photo (Google Drive, etc.) | |
| Bio | Rich text | Speaker biography | |
| Bio Short | Multi-line text | Shortened bio (1-2 paragraphs) | |
| Title/Role | Single line text | Current position | |
| Organization | Single line text | Affiliated organization | |
| DA Connection | Multi-line text | How speaker connected with DA | |
| Speaker Type | Single select | Category of speaker | Elected Official, Candidate, Author, Academic, Activist, DA Member, Expert, Other |
| Specialties/Topics | Multiple select | Areas of expertise | Healthcare, Climate, Education, Civil Rights, Immigration, Foreign Policy, Economics, Technology, Voting Rights, Democracy, Disability Rights, LGBTQ+ Rights, Women's Rights |
| Social Media - LinkedIn | URL | LinkedIn profile | |
| Social Media - Twitter/X | URL | Twitter handle/profile | |
| Social Media - Facebook | URL | Facebook profile | |
| Social Media - Instagram | URL | Instagram handle | |
| Website | URL | Personal or professional website | |
| Past Events | Link to another record | Links to Events Master | Multiple allowed |
| Total Events | Count | Number of events participated in | Auto-calculated from Past Events |
| Recording Consent Default | Single select | Default recording preference | Always Yes, Always No, Ask Each Time |
| Livestream Consent Default | Single select | Default livestream preference | Always Yes, Always No, Ask Each Time |
| Team Members | Multi-line text | Names/emails of staff who attend | Format: Name (email) |
| Availability Notes | Multi-line text | General availability or constraints | |
| Topics to Avoid | Multi-line text | Sensitive topics to avoid | |
| Foreign Policy Agreement Signed | Checkbox | Has acknowledged DA policy | |
| Promotional Consent | Checkbox | OK with DA promotion | Default checked |
| Status | Single select | Speaker status | Active, Inactive, Do Not Contact |
| Notes | Multi-line text | Internal notes about speaker | |
| First Event Date | Rollup | Date of first DA event | Auto-calculated from Past Events |
| Last Event Date | Rollup | Date of most recent event | Auto-calculated from Past Events |
| Created Date | Created time | Record creation date | Auto-generated |
| Last modified | Last modified time | Last update | Auto-generated |

---

## Table 3: Tasks & Workflow

**Purpose**: Track all tasks associated with events, with automated task creation for standard workflows.

**Table ID**: `tblf7ofibG2ibnvzt`

### Fields (24)

| Field Name | Field Type | Description | Options/Validation |
|------------|-----------|-------------|-------------------|
| Task Name | Single line text | Task description | Required |
| Event | Link to another record | Links to Events Master | Required |
| Task Type | Single select | Category of task | Graphics, Email, Social Media, Zoom Setup, Platform Posting, Video Editing, Documentation, Follow-up, Other |
| Task Category | Single select | Workflow phase | Pre-Event, During Event, Post-Event |
| Status | Single select | Current status | Not Started, In Progress, Completed, Blocked, Cancelled |
| Priority | Single select | Task priority | Low, Medium, High, Urgent |
| Due Date | Date | Deadline | |
| Description | Multi-line text | Task details | |
| Checklist | Multi-line text | Sub-tasks (one per line) | |
| Dependencies | Link to another record | Other tasks that must complete first | Links to Tasks & Workflow (self-referencing) |
| Dependent Tasks | Link to another record | Tasks that depend on this one | Links to Tasks & Workflow (self-referencing, reverse link) |
| Automation Type | Single select | If auto-created | Standard, Custom |
| Platform | Single select | For posting tasks | NationBuilder, Mighty Networks, Facebook, YouTube, Email, Signal |
| Email Type | Single select | Type of email communication | Announcement, Calendar Invite, Speaker Intake Form, Panelist Zoom Link, Thank You, Reminder, Survey, Other |
| Email Sent Date | Date | When email was sent | |
| Email Recipients | Multi-line text | Who received the email | |
| Email Template Used | Single line text | Name of email template | |
| Completion Notes | Multi-line text | Notes added when completed | |
| Created Date | Created time | Auto-timestamp | Auto-generated |
| Completed Date | Date | When task was completed | |
| Last Modified | Last modified time | Auto-timestamp | Auto-generated |
| Volunteers & Staff | Link to another record | Links to Volunteers & Staff table (assigned to) | Multiple allowed |
| Email Communications | Link to another record | Links to Email Communications table | Multiple allowed |
| Events Master | Link to another record | Links to Events Master table | Multiple allowed (alternate link field) |

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

**Table ID**: `tblsFrrK9BTEvICAN`

### Fields (19)

| Field Name | Field Type | Description | Options/Validation |
|------------|-----------|-------------|-------------------|
| Name | Single line text | Full name | Required |
| Email | Email | Contact email | Required |
| Phone | Phone number | Contact number | |
| Role Type | Multiple select | Type of role(s) | Moderator, Tech Support, Graphics, Social Media, Outreach, General Volunteer, Staff, Approver |
| Availability | Multi-line text | General availability notes | |
| Skills | Multiple select | Specific skills | Zoom Management, Graphic Design, Social Media, Writing, Translation, Video Editing, Event Planning, Public Speaking |
| Languages | Multiple select | Languages spoken | English, Spanish, French, German, Italian, Portuguese, Mandarin, Arabic, Other |
| Country Committee | Single select | Local affiliation | Global Black Caucus, Global Disability Caucus, Global LGBTQ+ Caucus, Global Seniors Caucus, Global Women's Caucus, Global Youth Caucus, Global Veterans & Military Families Caucus, Global Environmental & Climate Caucus, Global Asian Pacific Islander Caucus, Global Latino Caucus |
| Caucus Membership | Multiple select | Caucus affiliations | Global Black Caucus, Global Disability Caucus, Global LGBTQ+ Caucus, Global Seniors Caucus, Global Women's Caucus, Global Youth Caucus, Global Veterans & Military Families Caucus, Global Environmental & Climate Caucus, Global Asian Pacific Islander Caucus, Global Latino Caucus |
| Events Assigned | Link to another record | Links to Events Master | Multiple allowed |
| Tasks Assigned | Link to another record | Links to Tasks & Workflow | Multiple allowed |
| Total Events | Count | Number of events helped with | Auto-calculated from Events Assigned |
| Events Approved | Link to another record | Links to Events Master (events this person approved) | Multiple allowed |
| Status | Single select | Current status | Active, Inactive, On Leave |
| Notes | Multi-line text | Internal notes | |
| Created Date | Created time | Record creation date | Auto-generated |
| Last Modified | Last modified time | Last update | Auto-generated |
| Email Communications | Link to another record | Links to Email Communications (emails sent by this person) | Multiple allowed |
| Events Master | Link to another record | Links to Events Master | Multiple allowed (alternate link field) |

---

## Table 5: Committees & Caucuses

**Purpose**: Track organizing entities (country committees, global teams, caucuses) and their event involvement.

**Table ID**: `tblTIn7IqSsgV7Hyx`

### Fields (17)

| Field Name | Field Type | Description | Options/Validation |
|------------|-----------|-------------|-------------------|
| Name | Single line text | Official name | Required |
| Type | Single select | Organization type | Country Committee, Global Team, Global Caucus, Chapter |
| Region | Single select | Geographic region | Americas, EMEA, Asia Pacific, Global |
| Primary Contact Name | Single line text | Leader/chair name | |
| Primary Contact Email | Email | Leader/chair email | |
| Events Hosted | Link to another record | Links to Events Master (as host) | Multiple allowed |
| Events Co-Hosted | Link to another record | Links to Events Master (as co-host) | Multiple allowed |
| Total Events | Number | Total events involved in | Manually tracked |
| Members Count | Number | Approximate membership size | |
| Status | Single select | Current status | Active, Inactive |
| Description | Multi-line text | Brief description of group | |
| Website | URL | Organization website/page | |
| Social Media | Multi-line text | Social media handles | |
| Notes | Multi-line text | Internal notes | |
| Created Date | Created time | Record creation date | Auto-generated |
| Last Modified | Last modified time | Last update | Auto-generated |
| Events Master | Link to another record | Links to Events Master | Multiple allowed (alternate link field) |

---

## Table 6: Email Communications

**Purpose**: Track all email communications sent for events, including templates and delivery status.

**Table ID**: `tblWHIvwcC5DYGDRp`

### Fields (20)

| Field Name | Field Type | Description | Options/Validation |
|------------|-----------|-------------|-------------------|
| Email ID | Auto Number | Unique identifier | Auto-generated |
| Email Type | Single select | Type of communication | Announcement, Calendar Invite, Speaker Intake Form, Panelist Zoom Link, Thank You, Reminder, Survey, Run of Show, Other |
| Event | Link to another record | Links to Events Master | Required |
| Related Task | Link to another record | Links to Tasks & Workflow | If applicable |
| Subject Line | Single line text | Email subject | Required |
| Template Name | Single select | Pre-built template used | Template 1 |
| Recipients | Multi-line text | Email addresses (one per line) | |
| Recipient Count | Number | Total recipients | |
| Sent Date | Date | When email was sent | |
| Sent By | Link to another record | Links to Volunteers & Staff | |
| Delivery Status | Single select | Email delivery status | Draft, Scheduled, Sent, Failed |
| Email Body | Rich text | Email content/body | |
| Attachments | Multiple attachments | Files attached to email | |
| Reply-To Email | Email | Reply-to address | |
| Opens | Number | Email open count (if tracked) | |
| Clicks | Number | Link click count (if tracked) | |
| Notes | Multi-line text | Additional notes | |
| Created Date | Created time | Record creation | Auto-generated |
| Last Modified | Last modified time | Last update | Auto-generated |
| Events Master | Link to another record | Links to Events Master | Multiple allowed (alternate link field) |

---

## Table 7: Reports & Analytics

**Purpose**: Store generated reports and analytics data for historical tracking.

**Table ID**: `tblj7QCJz8xQSjMDG`

### Fields (13)

| Field Name | Field Type | Description | Options/Validation |
|------------|-----------|-------------|-------------------|
| Report Name | Single line text | Report title | Required |
| Report Type | Single select | Category of report | Attendance Summary, Speaker Frequency, Event Performance, Volunteer Activity, Caucus Engagement, Monthly Summary, Quarterly Summary |
| Date Range Start | Date | Report period start | Required |
| Date Range End | Date | Report period end | Required |
| Generated Date | Date | When report was created | Auto-filled |
| Report File | Multiple attachments | PDF/CSV file | |
| Report URL | Single line text | Link to report (if hosted externally) | |
| Key Metrics | Multi-line text | Summary of key findings | |
| Events Included | Link to another record | Links to Events Master | Multiple allowed |
| Notes | Multi-line text | Additional context or insights | |
| Created By | Single line text | Who/what generated report | System or person name |
| Created Date | Created time | Record creation | Auto-generated |
| Events Master | Link to another record | Links to Events Master | Multiple allowed (alternate link field) |

---

## Key Relationships

### Primary Relationships:
1. **Events Master → Speakers**: Many-to-many (one event has multiple speakers; one speaker attends multiple events)
2. **Events Master → Tasks & Workflow**: One-to-many (one event has many tasks)
3. **Events Master → Volunteers & Staff**: Many-to-many (one event has multiple volunteers; one volunteer works multiple events)
4. **Events Master → Committees & Caucuses**: Many-to-many (one event has multiple organizing groups; one group hosts multiple events)
5. **Events Master → Email Communications**: One-to-many (one event has many emails sent)
6. **Tasks & Workflow → Volunteers & Staff**: Many-to-many (one task can be assigned to multiple people; one person can have multiple tasks)
7. **Tasks & Workflow → Email Communications**: One-to-many (one task may trigger multiple emails)
8. **Email Communications → Volunteers & Staff**: Many-to-one (emails are sent by staff members)
9. **Reports & Analytics → Events Master**: Many-to-many (one report covers multiple events)
10. **Tasks & Workflow → Tasks & Workflow**: Many-to-many (tasks can have dependencies on other tasks)

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
| Event date and timing | Event Date, Event Time |

**Note**: The Timezone, Approval Status, and Approver fields from the original Google Form are not included in the current schema. All events are assumed to be in Eastern Time (ET).

### Webinar Intake Form → Speakers Table

| Google Form Field | Airtable Field |
|------------------|----------------|
| Timestamp | Created Date |
| Email Address | Email (requestor - may differ from speaker) |
| Speaker Name | Speaker Name |
| Please add the name and email... | Team Members |
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
3. **Pending Approval** - Filtered to "Pending Approval" status
4. **Events Calendar** - Calendar view by Event Date
5. **By Caucus** - Grouped by Host Organization
6. **Completed Events** - Filtered to "Completed" status, sorted descending

### Speakers Views:
1. **All Speakers** - Default grid view
2. **Active Speakers** - Filtered to "Active" status
3. **Frequent Speakers** - Sorted by Total Events (descending)
4. **Recently Added** - Sorted by Created Date (descending)

### Tasks & Workflow Views:
1. **All Tasks** - Default grid view
2. **Overdue Tasks** - Filtered to past due date + not completed
3. **By Event** - Grouped by Event
4. **By Status** - Grouped by Status

### Volunteers & Staff Views:
1. **All Volunteers** - Default grid view
2. **Active** - Filtered to "Active" status
3. **By Role** - Grouped by Role Type

### Email Communications Views:
1. **All Emails** - Default grid view
2. **Recent Emails** - Sorted by Sent Date descending, last 50
3. **By Event** - Grouped by Event
4. **Failed Deliveries** - Filtered to "Failed" Delivery Status

---

## Schema Statistics

**Total Tables**: 7
**Total Fields**: 167
- Events Master: 50 fields
- Speakers: 33 fields
- Tasks & Workflow: 24 fields
- Volunteers & Staff: 19 fields
- Committees & Caucuses: 17 fields
- Email Communications: 20 fields
- Reports & Analytics: 13 fields

**Total Relationships**: 10 primary relationships (including self-referencing)

---

## Design Notes

### Removed Fields (from original design)
- **Timezone** - All events use Eastern Time (ET), no need for separate field
- **Approval Status** - Consolidated into single "Status" field
- **Approver** - Removed in favor of "Events Approved" relationship in Volunteers & Staff table

### Duplicate Link Fields
Several tables have multiple link fields to the same table (e.g., "Tasks & Workflow" and "Tasks" both linking Events Master to Tasks). These appear to be alternate relationship paths created during base setup and can be consolidated in future schema cleanup.

### Field Type Notes
- **Rich text** fields support formatted text with bold, italics, links, etc.
- **Multi-line text** fields are plain text with line breaks
- **Multiple attachments** allow uploading multiple files
- **Rollup** fields calculate values from linked records
- **Count** fields automatically count linked records
- **Auto Number** fields generate sequential IDs

---

*This schema documentation was generated from the live Airtable API on September 28, 2025.*