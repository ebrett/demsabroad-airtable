# Democrats Abroad Event Management System

**A comprehensive solution for managing events, speakers, tasks, and volunteers**

---

## What Is This?

The DA Event Management System replaces our previous Google Forms and spreadsheet workflow with a centralized Airtable-based solution. This system helps you manage the complete event lifecycle from initial request through post-event follow-up.

### What It Replaces

**Before:** Multiple disconnected tools
- ✅ Event request Google Form → Now: Airtable Event Request Form
- ✅ Webinar intake Google Form → Now: Airtable Speaker Intake Form
- ✅ Upcoming events spreadsheet → Now: Events Master table + Dashboard
- ✅ Manual data transfer → Now: Automatic population

**After:** One integrated system
- All event data in one place
- Speaker information automatically saved and reusable
- Task tracking built-in
- Visual dashboard for management

---

## Key Features

### 📝 Smart Forms

**Event Request Form**
- Replaces the Google Form for event proposals
- Automatically creates event records in the system
- Captures organizer details, event info, audience, and speakers
- Simple, user-friendly interface

**Speaker Intake Form**
- Replaces the webinar intake Google Form
- Collects speaker bio, photo, contact info, social media
- Tracks consent for recording and livestreaming
- Captures team member information
- Foreign policy acknowledgment

### 🔗 Connected Data

**Everything Links Together:**
- Events automatically link to speakers, tasks, and volunteers
- View a speaker's complete event history
- See all tasks for an event in one place
- Track volunteer assignments across events

### 📈 Ready for Automation (Coming Soon)

The system is built with automation in mind:
- Future: Automatically create standard tasks when you approve an event
- Future: Send email reminders automatically
- Future: Integrate with Zoom, NationBuilder, and Mighty Networks

---

## How It Works

### For Event Organizers (Caucus Chairs, Committee Members)

**Step 1: Submit Event Request**
1. Fill out the Event Request Form (link provided by coordinator)
2. Include event details, audience, speakers
3. Submit and wait for approval notification

**Step 2: After Approval**
- You'll be contacted by the events team
- Speakers will receive intake forms
- Event will be scheduled and promoted

### For Speakers

**Step 1: Receive Speaker Intake Form**
- Sent to you by email after event is approved
- Takes ~5-10 minutes to complete

**Step 2: Complete the Form**
- Provide bio and photo
- Confirm recording/livestreaming consent
- Add any team members who will attend
- Acknowledge foreign policy guidelines

**Step 3: Receive Event Details**
- Zoom links sent closer to event date
- Run of show provided if needed

### For Event Coordinators

**Your Daily Workflow:**

**1. Review New Requests**
- Go to Dashboard → Overview page
- Check "Events Awaiting Approval"
- Click on an event to review details

**2. Approve or Request Changes**
- Change Status to:
  - `Approved` - Event is good to go
  - `Draft` - Needs more information (contact organizer)

**3. Manage Event Logistics**
- Update Status as event progresses:
  - `Scheduled` - Once logistics are confirmed
  - `In Progress` - During the event
  - `Completed` - After the event
- Track tasks on the Tasks page
- Assign volunteers as needed

**4. Track Progress**
- Use Calendar view to see all upcoming events
- Monitor overdue tasks
- Update event details as needed

---

## The System Structure

### 7 Connected Tables

**1. Events Master** - The hub
- Every event's complete information
- Date, time, description, audience
- Links to speakers, tasks, volunteers
- Platform integration tracking (Zoom, NationBuilder, Mighty Networks)

**2. Speakers** - Reusable speaker database
- Contact information
- Bio and photo
- Consent preferences
- Event history

**3. Tasks & Workflow** - Task tracking
- All event-related tasks
- Assignments and due dates
- Status tracking
- Email tracking

**4. Volunteers & Staff** - Your team
- Contact information
- Skills and availability
- Event and task assignments

**5. Committees & Caucuses** - Organizing groups
- All caucuses and committees
- Event hosting history
- Contact information

**6. Email Communications** - Email tracking
- All emails sent for events
- Templates used
- Delivery status
- Open/click tracking

**7. Reports & Analytics** - Reporting (future)
- Generated reports
- Event performance data
- Speaker and volunteer analytics

---

## Interface Overview

The system includes a custom dashboard with several specialized views for managing different aspects of your events:

### Event Management Insights

![Event Management Insights](screenshots/01-event-management-insights.png)

Your command center for high-level oversight and decision-making.

**Event Status & Approvals Section:**
- **Events Needing Approval** - Shows count of events awaiting your review with direct link to approval inbox
- **Scheduled Events** - Number of confirmed upcoming events
- **In-Progress Events** - Events currently happening
- **Completed Events** - Historical count of finished events
- **Cancelled Events** - Tracking of cancelled events for analysis

**Task Status & Overdue Tasks Section:**
- **Number of Overdue Tasks** - Immediate visibility into tasks requiring attention with link to detailed view
- **Task Status Distribution** - Visual pie chart breakdown showing all tasks by status (Not Started, In Progress, Completed)
- **Priority & Due Date Filters** - Quickly focus on critical items

### Events Overview

![Events Overview](screenshots/02-events-overview.png)

Central table view for managing all events with filtering and search capabilities.

**Key Features:**
- Filter by Event Status, Event Type, and Event Date
- View columns: Event Name, Event Date, Status, Host Organization, Expected Attendance, Event Organizer Name
- Quick add new event records
- Sort and group events by any field

### Event Approval Inbox

![Event Approval Inbox](screenshots/03-event-approval-inbox.png)

Streamlined interface for reviewing and approving incoming event requests.

**Features:**
- List view of all pending events with status filters
- Detail panel showing complete event information including:
  - Event Name, Type, Date, and Time
  - Status and Host Organization
  - Co-hosts, Overview/Purpose, Target Audience
  - Expected Attendance
  - Zoom Meeting Link, Registration Link, Meeting ID
  - Recording Consent tracking
- Quick status updates from pending to approved

### Task Tracking Kanban

![Task Tracking Kanban](screenshots/04-task-tracking-kanban.png)

Visual kanban board for managing event tasks by status.

**Columns:**
- **Not Started** - Tasks queued for action
- **In Progress** - Currently active tasks
- **Completed** - Finished tasks
- **Additional columns available** - Customize based on your workflow

**Task Cards Show:**
- Task Name
- Associated Event
- Due Date
- Filter by Status and Task Category

### Tasks & Workflow Management by Event

![Tasks & Workflow Management by Event](screenshots/05-tasks-workflow-by-event.png)

Hierarchical view showing events with their associated tasks nested underneath.

**Features:**
- Expandable event rows showing linked tasks
- Event-level information: Event Name, Event Type, Event Date, Status, Host Organization
- Task-level details: Task Name, Task Category, Status, Priority, Due Date, Platform
- Filter by Status, Due Date, and Event
- Add tasks directly to events

### Overdue Tasks

![Overdue Tasks](screenshots/06-overdue-tasks.png)

Dedicated dashboard for monitoring tasks that need immediate attention.

**Sections:**
- **Awaiting Approval / Overdue Tasks / All Records Tabs** - Filter view based on urgency
- **Overdue Tasks** - Count with direct access to task list
- **Overdue Urgent Tasks** - Separate counter for high-priority items
- **Overdue Tasks by Priority** - Visual chart showing distribution of overdue items by priority level
- **Overdue Tasks Dashboard** - Complete table listing with Task Name, Event, Due Date, Status, and Volunteers & Staff assignments

### Speaker Management

![Speaker Management](screenshots/07-speaker-management.png)

Comprehensive interface for managing your speaker database.

**Features:**
- Filter by Status, Speaker Type, and Specialties/Topics
- View columns: Speaker Name, Email, Title/Role, Organization, Specialties/Topics, Status
- Track speaker contact information, availability, and event history
- Group and sort capabilities
- Quick record creation

---

## Event Lifecycle

### The Complete Journey

```
1. REQUEST SUBMITTED
   ↓ (Organizer fills out Event Request Form)

2. PENDING APPROVAL (Status: "Pending Approval")
   ↓ (Coordinator reviews in dashboard)

3. APPROVED (Status: "Approved")
   ↓ (Coordinator sends speaker intake forms)
   ↓ (Speakers fill out intake forms)

4. SCHEDULED (Status: "Scheduled")
   ↓ (Zoom created, logistics confirmed)
   ↓ (Event promoted via email, social media)

5. IN PROGRESS (Status: "In Progress")
   ↓ (Event happening now!)

6. COMPLETED (Status: "Completed")
   ↓ (Thank yous sent, recording uploaded)
   ↓ (Survey sent to attendees)
```

### Status Meanings

| Status | What It Means | Who Changes It |
|--------|---------------|----------------|
| **Date Reserved** | Date is held, details being finalized | Coordinator |
| **Draft** | Being prepared, not ready for approval | Organizer/Coordinator |
| **Pending Approval** | Waiting for coordinator review | Set manually after submission |
| **Approved** | Ready to proceed with logistics | Coordinator |
| **Scheduled** | Logistics confirmed, event is public | Coordinator |
| **In Progress** | Event is happening now | Coordinator |
| **Completed** | Event finished | Coordinator |
| **Cancelled** | Event cancelled | Coordinator |

---

## Benefits & Time Savings

### What You Gain

**For Event Coordinators:**
- ⏱️ **Save 3-5 hours per week** - No more manual data transfer
- 📊 **See everything at a glance** - Dashboard shows what needs attention
- 🔍 **Find information instantly** - No more searching through spreadsheets
- ✅ **Track tasks easily** - Know what's done and what's pending
- 📧 **Email history** - See what communications have been sent

**For Event Organizers:**
- ✏️ **Simpler submission** - One form with clear instructions
- 👁️ **Transparency** - See your event's status
- 💬 **Better communication** - System tracks all touchpoints

**For Speakers:**
- 📝 **One-time data entry** - Information saved for future events
- ✅ **Clear consent tracking** - Know exactly what you've agreed to
- 🎯 **Streamlined process** - Clear instructions on what's needed

**For Everyone:**
- 🎯 **Nothing falls through the cracks** - Tasks tracked systematically
- 📈 **Better planning** - See patterns and trends
- 🤝 **Better coordination** - Everyone knows their responsibilities

---

## Getting Started

### Accessing the System

**Event Coordinators:**
1. You'll receive an email with your dashboard link
2. Bookmark it for easy access
3. Check it daily for new requests and overdue tasks

**Event Organizers:**
1. Use the Event Request Form link provided by your coordinator
2. You'll receive email updates about your event's status

**Speakers:**
1. You'll receive the Speaker Intake Form via email
2. Complete it before the event date

### Important Links

*[Links to be provided by administrator]*
- **Event Request Form:** [URL]
- **Speaker Intake Form:** [URL]
- **Event Coordinator Dashboard:** [URL]

### Need Help?

Contact: [Event Coordinator Contact Info]

---

## Frequently Asked Questions

### For Event Organizers

**Q: How long does approval take?**
A: Usually 3-5 business days. You'll receive an email when your event is approved or if we need more information.

**Q: Can I submit multiple events?**
A: Yes! Submit a separate form for each event.

**Q: What if I don't know the exact speaker yet?**
A: That's okay. Submit the request with "TBD" or tentative speakers. You can update later.

**Q: What information do I need to provide about my audience?**
A: Include who this event is for, expected attendance size, and why this event would interest them.

### For Speakers

**Q: When will I receive the intake form?**
A: After the event is approved, usually 7-10 days before the event.

**Q: Is the photo required?**
A: Yes, we need a photo for promotional materials. If you don't have one ready, you can provide a link to your photo online.

**Q: What if I have a team member attending?**
A: Great! Include their name and email in the intake form so they can receive a Zoom panelist link.

**Q: What is the foreign policy acknowledgment?**
A: All DA speakers must acknowledge they won't discuss U.S. foreign policy or criticize non-U.S. governments during official DA events.

### For Event Coordinators

**Q: How do I approve an event?**
A: Go to the event record and change Status from "Pending Approval" to "Approved".

**Q: How do I send speaker intake forms?**
A: For now, manually send the form link to speakers. (Future: This will be automated)

**Q: Can I edit events after they're submitted?**
A: Yes! You can edit any field in any event record.

**Q: How do I create tasks?**
A: Go to Tasks & Workflow table and create a new record, or create from the event record. (Future: Tasks will be auto-created)

**Q: Can I run reports?**
A: Not yet - this is coming in Phase 4. For now, you can export tables to CSV and analyze in Excel.

**Q: What if I accidentally delete something?**
A: Airtable has revision history - you can restore deleted records. Click the record history icon.

---

## Tips & Best Practices

### For Event Coordinators

**Daily Routine:**
1. Check Overview page first thing
2. Review and approve/decline pending events
3. Check overdue tasks
4. Update event statuses as things progress

**Organization Tips:**
- Use the Status field consistently
- Add notes in Special Instructions field
- Keep tasks updated with assignments
- Mark tasks complete as they're done

**Communication:**
- Reply to organizers promptly about approvals
- Send intake forms to speakers as soon as event is approved
- Keep volunteers informed about their assignments

### For Event Organizers

**Form Submission Tips:**
- Provide as much detail as possible in Overview/Purpose
- Be specific about your target audience
- Include speaker connection information
- Give realistic attendance estimates

**Follow-up:**
- Check your email for approval notifications
- Respond quickly if coordinator needs more info
- Confirm speaker availability before submitting

### For Speakers

**Form Completion Tips:**
- Use a professional photo
- Write bio in third person
- Include all social media you want promoted
- Be specific about topics to avoid
- Respond promptly to Zoom link emails

---

## What's Coming Next

### Phase 2: Automation (4-6 weeks)

**Task Automation:**
- When you approve an event, 20 standard tasks will be created automatically
- Tasks will have proper due dates calculated from event date
- Tasks will be pre-assigned based on type

**Email Automation:**
- Automatic emails to organizers when events are approved
- Automatic speaker intake form delivery
- Automatic Zoom links sent to speakers
- Automatic thank you emails after events
- Automatic post-event surveys

**Platform Integrations:**
- Zoom meetings created automatically
- Events posted to NationBuilder automatically
- Events shared to Mighty Networks automatically
- Calendar invites generated automatically

### Phase 3: Post-Event Automation (2-3 weeks)

**Video Workflow:**
- Recording download tracking
- Video editing workflow
- YouTube upload automation
- Recording links shared to Mighty Networks

### Phase 4: Reporting & Analytics (3-4 weeks)

**Automated Reports:**
- Event attendance summaries
- Speaker frequency reports
- Volunteer activity reports
- Monthly and quarterly summaries
- Email performance analytics

---

## System Requirements

### For Event Coordinators
- Internet connection
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Airtable account (free)

### For Event Organizers & Speakers
- Internet connection
- Modern web browser
- No account needed to submit forms

### For Future Automation
- Python 3.11+
- Access to Google Workspace (for email automation)
- GitHub account (for scheduled automations)

---

## Support & Training

### Training Available

**For Event Coordinators:**
- Dashboard walkthrough (30 minutes)
- Approval workflow training (15 minutes)
- Task management training (15 minutes)
- Ongoing support as needed

**For Event Organizers:**
- Form submission guide (written)
- Q&A session (optional)

**For Speakers:**
- Intake form instructions (included in form)

### Getting Help

**Have a question?**
- Email: [Event Coordinator Email]
- Check this README for answers
- Watch for training session announcements

**Found a bug or have a suggestion?**
- Contact: [Developer Contact]
- Describe what happened and what you expected
- Include screenshots if helpful

---

## Technical Details (For Administrators)

### System Components

**Airtable Base:**
- 7 interconnected tables
- 167 total fields
- 9 primary relationships
- 15+ custom views

**Forms:**
- Event Request Form (11 fields)
- Speaker Intake Form (18 fields)

**Dashboard:**
- 4-page interface
- Role-based access control
- Mobile-responsive

**API Access:**
- Python integration ready
- Personal Access Token configured
- Rate limiting implemented

### Backup & Recovery

**Current:**
- Manual exports recommended weekly
- Revision history available in Airtable
- Complete rebuild specs documented

**Future:**
- Automated daily backups via API
- CSV exports to cloud storage

### Security

**Access Control:**
- Forms: Public (anyone with link)
- Dashboard: Restricted to coordinators
- API: Token-based, limited to this base

**Data Privacy:**
- Speaker consent tracked
- Email addresses protected
- Personal information limited to need-to-know

---

## Success Stories

### Time Saved

**Before:**
- 20+ minutes per event to manually enter data across multiple spreadsheets
- 3-5 hours per week managing spreadsheets
- Frequent errors from manual data transfer
- Difficulty finding speaker information

**After:**
- Event data entered once via form
- Dashboard provides instant access to all information
- No manual data transfer needed
- Speaker history instantly available

### Improved Coordination

**Before:**
- Tasks tracked informally or not at all
- Missed deadlines common
- Unclear who was responsible for what

**After:**
- All tasks visible in one place
- Clear ownership and due dates
- Dashboard shows what needs attention

### Better Speaker Experience

**Before:**
- Speakers re-entered same information for every event
- Unclear what materials were needed
- Last-minute scrambling for bios and photos

**After:**
- Speaker information saved and reused
- Clear instructions on what's needed
- Standardized intake process

---

## Glossary

**Airtable** - Cloud-based database platform that combines spreadsheet and database features

**Base** - An Airtable database (like a collection of related spreadsheets)

**Table** - Similar to a spreadsheet tab, contains records of one type

**Record** - A single row in a table (like one event, one speaker, etc.)

**Field** - A column in a table (like Event Name, Email, etc.)

**View** - A filtered/sorted way of looking at table data

**Interface** - A custom dashboard built on top of tables

**Form** - Web form that creates records in a table

**Link** - Connection between records in different tables

**Status** - The current stage of an event in the workflow

---

## Version History

**Version 1.0** - September 28, 2025
- Initial release
- 7 tables created
- 2 forms published
- 4-page dashboard launched
- API access configured
- Phase 1 complete

---

## Credits

**Built for:** Democrats Abroad
**Developed by:** Brian McConnell
**Platform:** Airtable
**Project Duration:** Phase 1 completed in 1 day
**Documentation:** Comprehensive specs and guides maintained

---

## Contact

**Event Coordinator:** [Name and Email]
**System Administrator:** [Name and Email]
**Technical Support:** [Developer Contact]

**System Links:**
- Event Request Form: [URL]
- Speaker Intake Form: [URL]
- Coordinator Dashboard: [URL]
- Technical Documentation: See `progress.md`

---

*Last Updated: September 28, 2025*
