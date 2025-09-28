# Technical Documentation

## System Overview

The DA Event Management System is built on Airtable as the database backend with Python for API integration and automation. This document covers technical details, administrative procedures, and development information.

---

## Architecture

### Platform

**Airtable**
- Plan: Pro or Plus (required for API access)
- Base ID: `appL5mQf4myxTXpMv`
- 7 interconnected tables
- 167 total fields
- 10 primary relationships (including self-referencing)

**Python Environment**
- Version: 3.12.0+
- Package manager: uv (modern Python package manager)
- Primary library: pyairtable 3.2.0
- Configuration: python-dotenv 1.1.1

---

## Database Schema

### Tables and Field Counts

1. **Events Master** - 50 fields (Table ID: `tbldUqVq6Er0ivwFW`)
2. **Speakers** - 33 fields (Table ID: `tblxKGytwTnAucOZT`)
3. **Tasks & Workflow** - 24 fields (Table ID: `tblf7ofibG2ibnvzt`)
4. **Volunteers & Staff** - 19 fields (Table ID: `tblsFrrK9BTEvICAN`)
5. **Committees & Caucuses** - 17 fields (Table ID: `tblTIn7IqSsgV7Hyx`)
6. **Email Communications** - 20 fields (Table ID: `tblWHIvwcC5DYGDRp`)
7. **Reports & Analytics** - 13 fields (Table ID: `tblj7QCJz8xQSjMDG`)

### Key Relationships

1. Events Master ↔ Speakers (many-to-many)
2. Events Master → Tasks & Workflow (one-to-many)
3. Events Master ↔ Volunteers & Staff (many-to-many)
4. Events Master ↔ Committees & Caucuses (many-to-many)
5. Events Master → Email Communications (one-to-many)
6. Tasks & Workflow ↔ Volunteers & Staff (many-to-many)
7. Tasks & Workflow → Email Communications (one-to-many)
8. Email Communications → Volunteers & Staff (many-to-one)
9. Reports & Analytics ↔ Events Master (many-to-many)
10. Tasks & Workflow ↔ Tasks & Workflow (self-referencing for dependencies)

For complete schema details, see `.agent-os/product/airtable-schema.md`

---

## Development Environment Setup

### Prerequisites

- Python 3.12.0 or higher
- uv package manager
- Git
- Airtable account with API access

### Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd airtable
```

2. **Install uv (if not already installed):**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. **Create virtual environment and install dependencies:**
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

4. **Configure environment variables:**
```bash
cp .env.example .env  # Create from example if provided
# Edit .env and add:
# AIRTABLE_API_KEY=your_personal_access_token
# AIRTABLE_BASE_ID=appL5mQf4myxTXpMv
```

5. **Test connection:**
```bash
python test_airtable_connection.py
```

### Dependencies

```
pyairtable==3.2.0
python-dotenv==1.1.1
```

---

## API Access

### Authentication

The system uses Personal Access Tokens for API authentication.

**Token Scopes Required:**
- `data.records:read`
- `data.records:write`
- `schema.bases:read`

**Rate Limits:**
- 5 requests per second per base
- Scripts include rate limiting and retry logic

### Creating a Personal Access Token

1. Go to https://airtable.com/create/tokens
2. Click "Create new token"
3. Name: "DA Event Management System"
4. Add scopes: data.records:read, data.records:write, schema.bases:read
5. Add access to base: DA Event Management System
6. Click "Create token"
7. Copy token immediately (shown only once)
8. Add to `.env` file as `AIRTABLE_API_KEY`

### Python API Usage Example

```python
from pyairtable import Api
from dotenv import load_dotenv
import os

load_dotenv()

api = Api(os.getenv('AIRTABLE_API_KEY'))
base = api.base(os.getenv('AIRTABLE_BASE_ID'))

# Get all events
events_table = base.table('Events Master')
events = events_table.all()

# Get schema information
schema = base.schema()
for table in schema.tables:
    print(f"{table.name}: {len(table.fields)} fields")
```

---

## System Components

### Forms

**Event Request Form**
- Fields: 11 input fields
- Submits to: Events Master table
- Public access (anyone with link)
- Confirmation message on submission

**Speaker Intake Form**
- Fields: 18 input fields
- Submits to: Speakers table
- Public access (anyone with link)
- File upload support (photos)
- Confirmation message on submission

### Dashboard

**4-Page Interface:**
1. Event Management Insights (Overview)
2. Events Overview (Table view)
3. Speaker Management
4. Task Tracking

**Features:**
- Role-based access control
- Mobile-responsive design
- Custom views and filters
- Inline editing capabilities

### Custom Views

**Events Master:**
- All Events (default grid)
- Upcoming Events (filtered by date)
- Pending Approval (filtered by status)
- Events Calendar (calendar view)
- By Caucus (grouped)
- Completed Events (filtered and sorted)

**Speakers:**
- All Speakers (default grid)
- Active Speakers (filtered)
- Frequent Speakers (sorted by count)
- Recently Added (sorted by date)

**Tasks & Workflow:**
- All Tasks (default grid)
- Overdue Tasks (filtered by date and status)
- By Event (grouped)
- By Status (grouped)

**Volunteers & Staff:**
- All Volunteers (default grid)
- Active (filtered)
- By Role (grouped)

**Email Communications:**
- All Emails (default grid)
- Recent Emails (sorted by date, limited to 50)
- By Event (grouped)
- Failed Deliveries (filtered)

---

## Backup & Recovery

### Current Backup Strategy

**Manual Backups:**
- Weekly exports recommended
- Export each table to CSV
- Store in secure cloud storage
- Revision history available in Airtable (by record)

**Recovery Capabilities:**
- Airtable maintains revision history for all records
- Complete base rebuild specifications documented
- Successful rebuild completed in 45 minutes (demonstrated)

### Automated Backup (Planned)

```python
# Future implementation
import csv
from datetime import datetime

def backup_table(table_name):
    table = base.table(table_name)
    records = table.all()

    filename = f"backup_{table_name}_{datetime.now().strftime('%Y%m%d')}.csv"

    # Export to CSV
    with open(filename, 'w', newline='') as csvfile:
        # CSV export logic
        pass
```

**Planned Schedule:**
- Daily automated backups via GitHub Actions
- 30-day retention
- Stored in cloud storage (S3 or similar)

---

## Security

### Access Control

**Forms:**
- Public access (anyone with link)
- No authentication required
- Rate limiting via Airtable

**Dashboard:**
- Restricted to event coordinators
- Airtable authentication required
- Role-based permissions

**API:**
- Personal Access Token authentication
- Token scoped to specific base
- Environment variables for credentials (never committed)

### Data Privacy

**Personal Information:**
- Speaker consent tracked explicitly
- Email addresses protected
- Personal information limited to need-to-know
- GDPR considerations for international speakers

**Sensitive Data:**
- API keys stored in `.env` (gitignored)
- No credentials in code or documentation
- Tokens can be revoked if compromised

### Best Practices

- Never commit `.env` files
- Rotate API tokens periodically
- Use least-privilege access for tokens
- Monitor API usage for anomalies
- Regular security audits

---

## Automation (Future Phases)

### Phase 2: Task Automation (4-6 weeks)

**Automatic Task Creation:**
- Trigger: Event status changes to "Approved"
- Creates 20 standard workflow tasks
- Due dates calculated from event date
- Tasks pre-assigned based on type

**Email Automation:**
- Approval notifications to organizers
- Speaker intake form delivery
- Zoom link distribution
- Thank you emails post-event
- Post-event surveys

**Platform Integrations:**
- Zoom API: Meeting/webinar creation
- NationBuilder API: Event publishing
- Mighty Networks API: Community posting
- Calendar invite generation (.ics files)

### Phase 3: Post-Event Automation (2-3 weeks)

**Video Workflow:**
- Recording download tracking
- Video editing workflow management
- YouTube upload automation
- Recording links shared to platforms

### Phase 4: Reporting & Analytics (3-4 weeks)

**Automated Reports:**
- Event attendance summaries
- Speaker frequency reports
- Volunteer activity reports
- Monthly and quarterly summaries
- Email performance analytics

---

## Testing

### Connection Test Script

`test_airtable_connection.py` verifies:
- API authentication
- Access to all 7 tables
- Record counts
- Sample data retrieval

**Run tests:**
```bash
python test_airtable_connection.py
```

**Expected output:**
```
✅ Events Master: Accessible
✅ Speakers: Accessible
✅ Tasks & Workflow: Accessible
✅ Volunteers & Staff: Accessible
✅ Committees & Caucuses: Accessible
✅ Email Communications: Accessible
✅ Reports & Analytics: Accessible
```

### Manual Testing Checklist

**Forms:**
- [ ] Event Request Form submission
- [ ] Speaker Intake Form submission
- [ ] Form validation (required fields)
- [ ] File upload (speaker photos)
- [ ] Confirmation messages

**Dashboard:**
- [ ] Event Management Insights displays metrics
- [ ] Events Overview filtering and sorting
- [ ] Event Approval Inbox functionality
- [ ] Task Kanban board drag-and-drop
- [ ] Overdue Tasks dashboard accuracy
- [ ] Speaker Management filtering

**Data Relationships:**
- [ ] Events link to speakers correctly
- [ ] Events link to tasks correctly
- [ ] Events link to volunteers correctly
- [ ] Speaker event history displays
- [ ] Task dependencies work
- [ ] Volunteer assignments track

---

## Troubleshooting

### Common Issues

**API Connection Fails:**
- Verify `.env` file exists and contains correct credentials
- Check API token hasn't expired or been revoked
- Verify token has correct scopes
- Check network connectivity

**Form Submissions Not Appearing:**
- Check form is connected to correct table
- Verify required fields are completed
- Check Airtable rate limits haven't been exceeded
- Review form submission confirmations

**Dashboard Not Loading:**
- Clear browser cache
- Check Airtable account access
- Verify interface hasn't been deleted or modified
- Check browser console for errors

**Rate Limiting:**
- Implement delays between API calls (200ms minimum)
- Batch operations when possible
- Monitor API usage in Airtable dashboard

### Error Messages

**"Invalid API key":**
- Regenerate Personal Access Token
- Update `.env` file
- Restart application

**"Base not found":**
- Verify `AIRTABLE_BASE_ID` in `.env`
- Check token has access to the base

**"Table not found":**
- Verify table names match exactly (case-sensitive)
- Check table hasn't been renamed or deleted

---

## Maintenance

### Regular Tasks

**Weekly:**
- Review pending event approvals
- Check overdue tasks
- Export backup of all tables
- Monitor API usage

**Monthly:**
- Review and clean test data
- Audit user access permissions
- Check for duplicate records
- Update documentation as needed

**Quarterly:**
- Review and update field choices (as needed)
- Audit relationships for orphaned records
- Performance review of dashboard
- Security audit of API access

### Updates and Changes

**Adding New Fields:**
1. Update Airtable table schema
2. Update `.agent-os/product/airtable-schema.md`
3. Update forms if field is user-facing
4. Update dashboard views if needed
5. Test thoroughly before announcing

**Modifying Workflows:**
1. Document current workflow
2. Make changes in test environment first
3. Update documentation
4. Train users on changes
5. Roll out gradually

---

## Development Roadmap

### Completed (Phase 1)

- ✅ Database schema design and implementation
- ✅ 7 tables with 167 fields
- ✅ All relationships configured
- ✅ Event Request Form
- ✅ Speaker Intake Form
- ✅ 4-page dashboard interface
- ✅ API access and test scripts
- ✅ Comprehensive documentation

### In Progress

- Development environment setup
- Testing and validation
- User training materials

### Planned

**Phase 2: Automation (4-6 weeks)**
- Automatic task creation
- Email automation system
- Zoom API integration
- NationBuilder integration
- Mighty Networks integration

**Phase 3: Post-Event Automation (2-3 weeks)**
- Video workflow automation
- Recording management
- YouTube upload automation

**Phase 4: Reporting & Analytics (3-4 weeks)**
- Automated report generation
- Email analytics dashboard
- Volunteer management features

---

## Performance Considerations

### Airtable Limits

**Record Limits:**
- 50,000 records per base (Pro plan)
- 100,000 records per base (Enterprise)

**API Rate Limits:**
- 5 requests per second per base
- 1,000 requests per workspace per day (approx)

**Attachment Storage:**
- 20 GB per base (Pro plan)
- Unlimited (Enterprise)

### Optimization Strategies

**API Calls:**
- Batch operations when possible
- Use views to filter data server-side
- Cache frequently accessed data
- Implement exponential backoff on retries

**Dashboard Performance:**
- Limit records displayed in views (use pagination)
- Use filtered views instead of showing all records
- Optimize formulas and rollups
- Regular cleanup of old/archived records

---

## Support and Resources

### Documentation

- **User Guide:** `README.md`
- **Schema Documentation:** `.agent-os/product/airtable-schema.md`
- **Progress Tracking:** `progress.md`
- **Roadmap:** `.agent-os/product/roadmap.md`
- **Email Plan:** `.agent-os/product/email-automation-plan.md`

### External Resources

- [Airtable API Documentation](https://airtable.com/developers/web/api/introduction)
- [pyairtable Documentation](https://pyairtable.readthedocs.io/)
- [Gmail API Documentation](https://developers.google.com/gmail/api)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

### Contact

**System Administrator:** [Name and Email]
**Developer:** Brett McHargue
**Airtable Support:** support@airtable.com

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

## License and Credits

**Built for:** Democrats Abroad
**Developed by:** Brett McHargue
**Platform:** Airtable
**Development Time:** Phase 1 completed in 1 day

---

*Last Updated: September 28, 2025*