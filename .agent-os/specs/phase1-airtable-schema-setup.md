# Specification: Phase 1 - Airtable Base Schema Setup

**Version:** 1.0
**Status:** Ready for Implementation
**Estimated Effort:** Medium (1 week)
**Priority:** Critical (Blocker for all other phases)

---

## Overview

This specification defines the complete setup of the Airtable base structure for the Event Management System. This is the foundation upon which all automation, forms, and integrations will be built.

**Goal:** Create a fully functional Airtable base with 7 tables, proper relationships, field validations, and recommended views that can replace the current Google Forms/Sheets workflow.

---

## Success Criteria

- ✅ All 7 tables created with correct field types and validations
- ✅ Relationships between tables properly configured and tested
- ✅ At least 2 test events created with linked speakers, tasks, and volunteers
- ✅ All recommended views created for each table
- ✅ Base can be accessed via Airtable API with proper permissions
- ✅ Documentation created for non-technical users on how to use the base

---

## Prerequisites

- Airtable account with Pro or Plus plan (required for extensions and API)
- Airtable Personal Access Token generated with read/write permissions
- Access to Democrats Abroad Google Workspace (for future form integration)

---

## Implementation Steps

### Step 1: Create New Airtable Base

1. Log into Airtable account
2. Create new base: **"DA Event Management System"**
3. Set base icon and color for easy identification
4. Configure base permissions (limit access to event coordinators only)

### Step 2: Create Tables in Order

Create tables in this specific order to properly set up linked relationships:

#### 2.1 Table: Events Master (Primary Hub)

**Purpose:** Central table linking all event information

**Fields to Create:**

| # | Field Name | Field Type | Configuration |
|---|-----------|-----------|---------------|
| 1 | Event ID | Auto Number | Auto-generated |
| 2 | Event Name | Single line text | Required |
| 3 | Event Type | Single select | Options: Webinar, Panel, Town Hall, Meet & Greet, Other |
| 4 | Event Date | Date | Include time, Required |
| 5 | Event Time | Single line text | Format: "9:00 AM ET" |
| 6 | Timezone | Single select | Options: ET, CT, MT, PT, AEDT, BST, CET, GMT, IST, JST |
| 7 | Status | Single select | Options: Date Reserved, Draft, Pending Approval, Approved, Scheduled, In Progress, Completed, Cancelled |
| 8 | Approval Status | Single select | Options: Pending, Approved, Needs Revision |
| 9 | Approver | Single line text | |
| 10 | Host Organization | Multiple select | Options: (See Caucus/Committee list below) |
| 11 | Co-hosts | Multiple select | Same options as Host Organization |
| 12 | Overview/Purpose | Long text | Enable rich text formatting |
| 13 | Target Audience | Long text | |
| 14 | Expected Attendance | Number | Integer, allow negative: No |
| 15 | Zoom Meeting Link | URL | |
| 16 | Zoom Registration Link | URL | |
| 17 | Zoom Meeting ID | Single line text | |
| 18 | Recording Consent | Checkbox | |
| 19 | Live Stream Consent | Checkbox | |
| 20 | Live Stream Platform | Multiple select | Options: Facebook, YouTube |
| 21 | Recording URL | URL | |
| 22 | Event Organizer Name | Single line text | Required |
| 23 | Event Organizer Email | Email | Required |
| 24 | Speakers | Link to another record | Link to: Speakers Database (allow multiple) |
| 25 | Tasks | Link to another record | Link to: Tasks & Workflow (allow multiple) |
| 26 | Volunteers | Link to another record | Link to: Volunteers & Staff (allow multiple) |
| 27 | Committees | Link to another record | Link to: Committees & Caucuses (allow multiple) |
| 28 | NationBuilder Synced | Checkbox | |
| 29 | NationBuilder Event ID | Single line text | |
| 30 | Mighty Networks Posted | Checkbox | |
| 31 | Mighty Networks URL | URL | |
| 32 | Promotional Email Sent | Checkbox | |
| 33 | Foreign Policy Agreement | Checkbox | |
| 34 | Run of Show Created | Checkbox | |
| 35 | Run of Show URL | URL | |
| 36 | Signal Green Room Created | Checkbox | |
| 37 | Signal Green Room Link | URL | |
| 38 | Website Posted | Checkbox | |
| 39 | Website Event URL | URL | |
| 40 | Calendar Invite Sent | Checkbox | |
| 41 | Thank You Sent | Checkbox | |
| 42 | Post-Event Mighty Posted | Checkbox | |
| 43 | Post-Event Mighty URL | URL | |
| 44 | Video Edited | Checkbox | |
| 45 | Special Instructions | Long text | |
| 46 | Created Date | Created time | Auto-generated |
| 47 | Last Modified | Last modified time | Auto-generated |

**Host Organization Options:**
```
Global Black Caucus
Global Disability Caucus
Global LGBTQ+ Caucus
Global Seniors Caucus
Global Women's Caucus
Global Youth Caucus
Global Veterans & Military Families Caucus
Global Environmental & Climate Caucus
Global Asian Pacific Islander Caucus
Global Latino Caucus
[Add country committees as needed]
```

#### 2.2 Table: Speakers Database

**Purpose:** Reusable speaker directory with full history

**Fields to Create:**

| # | Field Name | Field Type | Configuration |
|---|-----------|-----------|---------------|
| 1 | Speaker ID | Auto Number | Auto-generated |
| 2 | Speaker Name | Single line text | Required |
| 3 | Email | Email | Required |
| 4 | Alternate Email | Email | |
| 5 | Timezone | Single select | Same options as Events Master |
| 6 | Phone | Phone number | |
| 7 | Photo | Attachment | Allow multiple: No |
| 8 | Photo URL | URL | |
| 9 | Bio | Long text | Enable rich text |
| 10 | Bio Short | Long text | Max 2 paragraphs |
| 11 | Title/Role | Single line text | |
| 12 | Organization | Single line text | |
| 13 | DA Connection | Long text | |
| 14 | Speaker Type | Single select | Options: Elected Official, Candidate, Author, Academic, Activist, DA Member, Expert, Other |
| 15 | Specialties/Topics | Multiple select | Options: Healthcare, Climate, Education, Civil Rights, Immigration, Foreign Policy, Economics, Technology, etc. |
| 16 | Social Media - LinkedIn | URL | |
| 17 | Social Media - Twitter/X | URL | |
| 18 | Social Media - Facebook | URL | |
| 19 | Social Media - Instagram | URL | |
| 20 | Website | URL | |
| 21 | Past Events | Link to another record | Link to: Events Master (allow multiple) |
| 22 | Total Events | Count | Count from: Past Events |
| 23 | Recording Consent Default | Single select | Options: Always Yes, Always No, Ask Each Time |
| 24 | Livestream Consent Default | Single select | Options: Always Yes, Always No, Ask Each Time |
| 25 | Team Members | Long text | Format: Name (email) |
| 26 | Availability Notes | Long text | |
| 27 | Topics to Avoid | Long text | |
| 28 | Foreign Policy Agreement Signed | Checkbox | |
| 29 | Promotional Consent | Checkbox | Default: checked |
| 30 | Status | Single select | Options: Active, Inactive, Do Not Contact |
| 31 | Notes | Long text | |
| 32 | First Event Date | Formula | `MIN({Past Events})` |
| 33 | Last Event Date | Formula | `MAX({Past Events})` |
| 34 | Created Date | Created time | Auto-generated |
| 35 | Last Modified | Last modified time | Auto-generated |

#### 2.3 Table: Tasks & Workflow

**Purpose:** Track all event-related tasks with automation support

**Fields to Create:**

| # | Field Name | Field Type | Configuration |
|---|-----------|-----------|---------------|
| 1 | Task ID | Auto Number | Auto-generated |
| 2 | Task Name | Single line text | Required |
| 3 | Event | Link to another record | Link to: Events Master, Required |
| 4 | Task Type | Single select | Options: Graphics, Email, Social Media, Zoom Setup, Platform Posting, Video Editing, Documentation, Follow-up, Other |
| 5 | Task Category | Single select | Options: Pre-Event, During Event, Post-Event |
| 6 | Status | Single select | Options: Not Started, In Progress, Completed, Blocked, Cancelled |
| 7 | Priority | Single select | Options: Low, Medium, High, Urgent |
| 8 | Due Date | Date | Include time |
| 9 | Assigned To | Link to another record | Link to: Volunteers & Staff (allow multiple) |
| 10 | Description | Long text | |
| 11 | Checklist | Long text | One item per line |
| 12 | Dependencies | Link to another record | Link to: Tasks & Workflow (allow multiple) |
| 13 | Automation Type | Single select | Options: Standard, Custom |
| 14 | Platform | Single select | Options: NationBuilder, Mighty Networks, Facebook, YouTube, Website, Email, Signal |
| 15 | Email Type | Single select | Options: Announcement, Calendar Invite, Speaker Intake Form, Panelist Zoom Link, Thank You, Reminder, Survey, Other |
| 16 | Email Sent Date | Date | Include time |
| 17 | Email Recipients | Long text | |
| 18 | Email Template Used | Single line text | |
| 19 | Completion Notes | Long text | |
| 20 | Created Date | Created time | Auto-generated |
| 21 | Completed Date | Date | |
| 22 | Last Modified | Last modified time | Auto-generated |

#### 2.4 Table: Volunteers & Staff

**Purpose:** People who support events

**Fields to Create:**

| # | Field Name | Field Type | Configuration |
|---|-----------|-----------|---------------|
| 1 | Person ID | Auto Number | Auto-generated |
| 2 | Name | Single line text | Required |
| 3 | Email | Email | Required |
| 4 | Phone | Phone number | |
| 5 | Timezone | Single select | Same options as Events Master |
| 6 | Role Type | Multiple select | Options: Moderator, Tech Support, Graphics, Social Media, Outreach, General Volunteer, Staff |
| 7 | Availability | Long text | |
| 8 | Skills | Multiple select | Options: Zoom Management, Graphic Design, Social Media, Writing, Translation, Video Editing, etc. |
| 9 | Languages | Multiple select | Options: English, Spanish, French, German, Italian, Portuguese, etc. |
| 10 | Country Committee | Single select | Same options as Host Organization |
| 11 | Caucus Membership | Multiple select | Same options as Host Organization |
| 12 | Events Assigned | Link to another record | Link to: Events Master (allow multiple) |
| 13 | Tasks Assigned | Link to another record | Link to: Tasks & Workflow (allow multiple) |
| 14 | Total Events | Count | Count from: Events Assigned |
| 15 | Status | Single select | Options: Active, Inactive, On Leave |
| 16 | Notes | Long text | |
| 17 | Created Date | Created time | Auto-generated |
| 18 | Last Modified | Last modified time | Auto-generated |

#### 2.5 Table: Committees & Caucuses

**Purpose:** Organizing entities and their involvement

**Fields to Create:**

| # | Field Name | Field Type | Configuration |
|---|-----------|-----------|---------------|
| 1 | Organization ID | Auto Number | Auto-generated |
| 2 | Name | Single line text | Required |
| 3 | Type | Single select | Options: Country Committee, Global Team, Global Caucus, Chapter |
| 4 | Region | Single select | Options: Americas, EMEA, Asia Pacific, Global |
| 5 | Primary Contact Name | Single line text | |
| 6 | Primary Contact Email | Email | |
| 7 | Events Hosted | Link to another record | Link to: Events Master (allow multiple) |
| 8 | Events Co-Hosted | Link to another record | Link to: Events Master (allow multiple) |
| 9 | Total Events | Formula | `{Events Hosted} + {Events Co-Hosted}` (count) |
| 10 | Members Count | Number | Integer |
| 11 | Status | Single select | Options: Active, Inactive |
| 12 | Description | Long text | |
| 13 | Website | URL | |
| 14 | Social Media | Long text | |
| 15 | Notes | Long text | |
| 16 | Created Date | Created time | Auto-generated |
| 17 | Last Modified | Last modified time | Auto-generated |

#### 2.6 Table: Email Communications

**Purpose:** Track all emails sent for events

**Fields to Create:**

| # | Field Name | Field Type | Configuration |
|---|-----------|-----------|---------------|
| 1 | Email ID | Auto Number | Auto-generated |
| 2 | Email Type | Single select | Options: Announcement, Calendar Invite, Speaker Intake Form, Panelist Zoom Link, Thank You, Reminder, Survey, Run of Show, Other |
| 3 | Event | Link to another record | Link to: Events Master, Required |
| 4 | Related Task | Link to another record | Link to: Tasks & Workflow |
| 5 | Subject Line | Single line text | Required |
| 6 | Template Name | Single select | Options: (will populate as templates are created) |
| 7 | Recipients | Long text | One email per line |
| 8 | Recipient Count | Number | Integer |
| 9 | Sent Date | Date & Time | Include time |
| 10 | Sent By | Link to another record | Link to: Volunteers & Staff |
| 11 | Delivery Status | Single select | Options: Draft, Scheduled, Sent, Failed |
| 12 | Email Body | Long text | Enable rich text |
| 13 | Attachments | Attachment | Allow multiple |
| 14 | Reply-To Email | Email | |
| 15 | Opens | Number | Integer (for tracking) |
| 16 | Clicks | Number | Integer (for tracking) |
| 17 | Notes | Long text | |
| 18 | Created Date | Created time | Auto-generated |
| 19 | Last Modified | Last modified time | Auto-generated |

#### 2.7 Table: Reports & Analytics

**Purpose:** Store generated reports

**Fields to Create:**

| # | Field Name | Field Type | Configuration |
|---|-----------|-----------|---------------|
| 1 | Report ID | Auto Number | Auto-generated |
| 2 | Report Name | Single line text | Required |
| 3 | Report Type | Single select | Options: Attendance Summary, Speaker Frequency, Event Performance, Volunteer Activity, Caucus Engagement, Monthly Summary, Quarterly Summary |
| 4 | Date Range Start | Date | |
| 5 | Date Range End | Date | |
| 6 | Generated Date | Date | Auto-filled |
| 7 | Report File | Attachment | Allow multiple: No |
| 8 | Report URL | URL | |
| 9 | Key Metrics | Long text | |
| 10 | Events Included | Link to another record | Link to: Events Master (allow multiple) |
| 11 | Notes | Long text | |
| 12 | Created By | Single line text | |
| 13 | Created Date | Created time | Auto-generated |

### Step 3: Create Views for Each Table

#### Events Master Views:
1. **All Events** - Grid view (default)
2. **Upcoming Events** - Filter: Event Date >= Today, Sort: Event Date (ascending)
3. **Pending Approval** - Filter: Approval Status = "Pending"
4. **This Month** - Calendar view by Event Date
5. **By Caucus** - Group by: Host Organization
6. **Completed Events** - Filter: Status = "Completed", Sort: Event Date (descending)

#### Speakers Database Views:
1. **All Speakers** - Grid view (default)
2. **Active Speakers** - Filter: Status = "Active"
3. **Frequent Speakers** - Sort: Total Events (descending)
4. **Recently Added** - Sort: Created Date (descending)

#### Tasks & Workflow Views:
1. **All Tasks** - Grid view (default)
2. **Overdue** - Filter: Due Date < Today AND Status ≠ "Completed"
3. **By Event** - Group by: Event
4. **By Status** - Group by: Status
5. **Timeline** - Timeline view by Due Date

#### Volunteers & Staff Views:
1. **All Volunteers** - Grid view (default)
2. **Active** - Filter: Status = "Active"
3. **By Role** - Group by: Role Type

#### Email Communications Views:
1. **All Emails** - Grid view (default)
2. **Recent Emails** - Sort: Sent Date (descending), Show: Last 50
3. **By Event** - Group by: Event
4. **Failed Deliveries** - Filter: Delivery Status = "Failed"

### Step 4: Test Data Entry

Create 2 test events to verify all relationships work:

**Test Event 1:**
- Name: "Test Event: Speaker Panel"
- Status: Approved
- Add 2 test speakers (create new speaker records)
- Add 5 test tasks (manually create)
- Add 1 test volunteer
- Link to 1 caucus

**Test Event 2:**
- Name: "Test Event: Town Hall"
- Status: Pending Approval
- Add 1 test speaker
- Add 3 test tasks
- Link to 2 caucuses (co-hosting)

**Verification Checklist:**
- [ ] Event links appear in speaker's "Past Events" field
- [ ] Task count appears correctly on event record
- [ ] Volunteer total events increments correctly
- [ ] All views filter and display correctly

### Step 5: API Access Setup

1. Generate Airtable Personal Access Token
2. Note Base ID (from base URL: app...)
3. Note Table IDs for each table
4. Test API access with simple Python script:

```python
from pyairtable import Api

api = Api('YOUR_TOKEN')
base = api.base('YOUR_BASE_ID')
events_table = base.table('Events Master')

# Test: Fetch all events
events = events_table.all()
print(f"Found {len(events)} events")
```

### Step 6: Documentation

Create a simple guide for event coordinators:

**Document: "How to Use the Event Management System"**

Topics to cover:
1. How to submit a new event request
2. How to add speakers to an event
3. How to track task status
4. How to update event information
5. How to mark tasks as complete
6. Common workflows (approval process, speaker intake, etc.)

---

## Deliverables

1. ✅ Fully configured Airtable base with 7 tables
2. ✅ All field types and validations configured correctly
3. ✅ All table relationships working bidirectionally
4. ✅ All recommended views created and tested
5. ✅ 2 test events with complete data
6. ✅ API access token generated and tested
7. ✅ User documentation (1-2 page guide)

---

## Validation & Testing

### Functional Tests:

1. **Relationship Tests:**
   - Create event → Add speaker → Verify speaker's "Past Events" shows event
   - Create task → Assign to volunteer → Verify volunteer's "Tasks Assigned" increments
   - Add caucus as host → Verify caucus "Events Hosted" increments

2. **View Tests:**
   - Filter "Upcoming Events" → Only future events appear
   - Filter "Pending Approval" → Only pending events appear
   - Sort "Frequent Speakers" → Speakers with most events at top

3. **API Tests:**
   - Read event from API → All fields populate correctly
   - Create event via API → Event appears in Airtable interface
   - Update event via API → Changes reflect in Airtable

### Data Integrity Tests:

1. Required fields cannot be left blank
2. Email fields only accept valid email format
3. URL fields only accept valid URLs
4. Number fields only accept numeric values
5. Select fields only allow defined options

---

## Acceptance Criteria

- [ ] All 7 tables exist with exact field names and types as specified
- [ ] All linked relationships work bidirectionally
- [ ] At least 15 views created across all tables
- [ ] 2 complete test events created with all relationships
- [ ] API access works with pyairtable library
- [ ] User documentation created and reviewed
- [ ] Schema can support all 20 standard workflow tasks
- [ ] Base is accessible to event coordinators (permissions set)

---

## Next Steps After Completion

Once this specification is complete, proceed to:

**Phase 1, Feature 2:** Build Event Intake Form in Airtable
- Create Airtable form that populates Events Master table
- Configure form logic and conditional fields
- Replace existing Google Form

---

## Estimated Timeline

- **Day 1-2:** Create all 7 tables with fields
- **Day 3:** Configure relationships and test
- **Day 4:** Create all views
- **Day 5:** Create test data and verify
- **Day 6:** Set up API access and test
- **Day 7:** Write documentation and final review

**Total: 1 week**

---

## Notes & Considerations

1. **Airtable Plan Requirements:** This spec requires Airtable Pro or Plus for API access
2. **Field Limits:** Airtable has a limit of 500 fields per table (we're well under)
3. **Record Limits:** Free plan = 1,200 records per base; Pro = 50,000 (sufficient for years)
4. **Backup Strategy:** Export base weekly as CSV backup until automated backups set up
5. **Migration:** Existing Google Sheets data will be migrated in a separate step (not part of this spec)

---

## Questions & Decisions

**Q: Should we import existing event data from Google Sheets now?**
A: No, do that as a separate migration task after base structure is validated.

**Q: Who should have edit access to the base?**
A: Start with 2-3 core event coordinators, expand access as needed.

**Q: Should we use Airtable Forms or custom forms?**
A: Start with Airtable Forms (simpler), can build custom forms later if needed.