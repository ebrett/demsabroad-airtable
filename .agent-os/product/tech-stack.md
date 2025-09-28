# Technical Stack

## Core Technologies

### Programming Language
- **Python 3.11+**: Primary language for all automation scripts and API integrations

### Database & Backend
- **Airtable API**: Cloud-based database backend for all data storage (events, speakers, tasks, volunteers)
- **pyairtable**: Official Python client library for Airtable API interactions

### API Integrations
- **Zoom API**: Webinar/meeting creation, registration management, attendee data retrieval
- **NationBuilder API**: Event publishing, constituent management, RSVP tracking
- **Mighty Networks API**: Community event posting and engagement
- **SendGrid or similar**: Email automation for notifications and reminders

### Development Tools
- **pip/poetry**: Python package management
- **python-dotenv**: Environment variable management for API keys and secrets
- **requests**: HTTP library for API calls (if needed beyond SDK libraries)

## Project Structure

### Script Organization
- **scripts/**: Main automation scripts directory
  - `airtable_sync.py`: Core Airtable data operations
  - `zoom_integration.py`: Zoom API handlers
  - `nationbuilder_sync.py`: NationBuilder event publisher
  - `mighty_networks_sync.py`: Mighty Networks posting automation
  - `email_automation.py`: Email notification system
  - `report_generator.py`: Analytics and reporting scripts

### Configuration
- **config/**: Configuration files and templates
- **.env**: API keys and credentials (not committed to git)
- **requirements.txt**: Python dependencies

## Hosting & Deployment

### Application Hosting
- **Local execution** initially, with future options for:
  - **AWS Lambda** or **Google Cloud Functions**: Serverless execution for scheduled tasks
  - **Heroku** or **Railway**: Simple hosting for continuous script execution

### Scheduling
- **Cron jobs** (Linux/Mac) or **Task Scheduler** (Windows): For automated script execution
- **GitHub Actions**: Alternative for scheduled workflow automation

### Code Repository
- **GitHub**: Version control and collaboration
  - Repository URL: TBD (to be created)

## Data & Security

### API Authentication
- Environment variables for all API keys and tokens
- OAuth 2.0 flows where required (Zoom, NationBuilder)

### Logging & Monitoring
- **Python logging module**: Structured logging for debugging and audit trails
- **Log files**: Stored locally or sent to cloud logging service

## Future Considerations

### Optional Enhancements
- **Flask/FastAPI**: Web dashboard for manual triggers and monitoring
- **PostgreSQL**: Local caching layer if Airtable rate limits become an issue
- **Celery + Redis**: Task queue for complex async operations
- **Docker**: Containerization for consistent deployment environments