# Product Mission

## Pitch

Airtable Event Manager is a Python-powered automation system that helps webinar organizers centralize event management by integrating Airtable with Zoom, NationBuilder, and Mighty Networks, eliminating manual data entry across multiple Google Forms and spreadsheets.

## Users

### Primary Customers

- **Webinar Organizers**: Organizations and teams that regularly host educational or promotional webinars via Zoom and need to manage the complete event lifecycle from planning to post-event follow-up.
- **Non-Profit Communications Teams**: Small to medium organizations that manage community engagement through webinars and need to track events across multiple platforms (NationBuilder, Mighty Networks).

### User Personas

**Event Coordinator** (28-45 years old)
- **Role:** Communications or Events Manager
- **Context:** Manages 5-15 webinars per month using Zoom, coordinates with speakers, tracks RSVPs, and posts events to community platforms
- **Pain Points:** Manually copying data between Google Forms and spreadsheets, losing track of task status (graphics, platform postings), difficulty reusing speaker information, time-consuming post-event reporting
- **Goals:** Centralize event data in one system, automate cross-platform posting, reduce manual data entry, generate automated reports, easily track event progress

## The Problem

### Fragmented Data Across Multiple Systems

Organizations currently juggle multiple Google Forms (event request, webinar intake, post-event survey) and spreadsheets (upcoming events tracker) with no connection between them. This fragmentation leads to 3-5 hours per week of manual data transfer and increases the risk of errors or missed information.

**Our Solution:** Centralize all event data in Airtable with automated Python scripts that sync data to Zoom, NationBuilder, and Mighty Networks.

### No Centralized Task Tracking

Critical event-related tasks like graphics creation, platform posting (Mighty Networks), promotional emails, and speaker coordination are tracked informally or not at all. This results in missed deadlines, last-minute scrambling, and inconsistent event quality.

**Our Solution:** Build task workflow automation within Airtable that tracks every event milestone and sends automated reminders.

### Speaker Information Management

When working with repeat speakers, organizers must manually search through old forms or spreadsheets to find contact information, bios, and headshots. This wastes time and creates friction when planning new events with familiar faces.

**Our Solution:** Maintain a centralized speakers database with full history, making it one-click easy to invite returning speakers to new events.

### Limited Reporting and Analytics

Generating reports on event performance, attendance trends, speaker frequency, or volunteer contributions requires manually compiling data from disconnected sources. This makes it difficult to learn from past events or demonstrate impact to stakeholders.

**Our Solution:** Automated Python scripts generate comprehensive reports from Airtable data, providing insights on event success metrics and trends.

## Differentiators

### Airtable-First Architecture

Unlike traditional event management platforms that lock you into proprietary systems, we build on Airtable's flexible database foundation. This provides familiar form-building capabilities, customizable views, and the ability to adapt the system as your needs evolve without vendor lock-in.

### Purpose-Built for Webinar-to-Community Workflow

Generic event management tools don't understand the specific workflow of webinar organizers who need to push event data to community platforms like NationBuilder and Mighty Networks. Our Python automation scripts are purpose-built for this exact use case, eliminating the 3-5 hours per week spent on manual cross-platform data entry.

### Speaker Relationship Management

While other tools focus only on events, we recognize that speaker relationships are a core asset. Our integrated speakers database with full event history makes it effortless to work with repeat speakers and maintain those valuable relationships over time.

## Key Features

### Core Features

- **Event Master Database**: Centralized Airtable base tracking all webinar details, status, dates, and linked relationships to speakers, tasks, and volunteers
- **Speakers Database**: Comprehensive directory of speakers with contact info, bios, headshots, specialties, and full event history for easy reuse
- **Task & Workflow Automation**: Automated task creation and tracking for each event phase (graphics, posting, emails, reminders) with status monitoring
- **Form-to-Database Integration**: Intelligent forms that replace Google Forms, automatically populate Airtable, and leverage existing speaker data

### Integration Features

- **NationBuilder Sync**: Python scripts that automatically push event details to NationBuilder for constituent engagement and RSVP tracking
- **Mighty Networks Publisher**: Automated posting of event information to Mighty Networks community platform, eliminating manual copy-paste
- **Zoom Integration**: Scripts to create Zoom meetings, retrieve registration links, and sync attendee data back to Airtable

### Management Features

- **Volunteer & Staff Coordination**: Track volunteer assignments, staff responsibilities, and availability across events with automated notifications
- **Committees & Caucuses Organization**: Manage organizing committees, caucus groups, and collaborative planning teams within the system
- **Reports & Analytics Dashboard**: Automated Python-generated reports on event performance, speaker frequency, attendance trends, and volunteer contributions