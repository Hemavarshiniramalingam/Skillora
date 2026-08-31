# OpportunityAI - Phase 4: API, Notifications & Integration/DevOps

## Overview
This branch (`feature/integration-devops`) implements the complete REST API layer, Celery-based notifications, and deployment infrastructure for OpportunityAI - an AI-powered student internship & scholarship matching platform.

## Architecture

### API Endpoints
- `GET/POST /api/internships/` - List and create internship opportunities
- `GET/POST /api/scholarships/` - List and create scholarship opportunities  
- `GET/POST /api/applications/` - List and create student applications
- `GET /api/match/<student_id>/` - Compute and retrieve matching scores for a student
- `GET /api/health/` - Health check endpoint

### Database Models
- **Student** - Student profile with major, GPA, and preferred fields
- **Internship** - Internship opportunities with deadline and required skills
- **Scholarship** - Scholarship opportunities with eligibility criteria
- **Application** - Student applications to internships/scholarships
- **MatchResult** - Computed match scores between students and opportunities

### Matching Algorithm
The matching service (`opportunity_app/services.py`) implements a scoring algorithm that:
- Awards points for major/field matching
- Considers GPA thresholds  
- Matches preferred fields with required skills/eligibility
- Returns sorted list of opportunities by match score

### Celery Tasks
- **send_deadline_reminders** - Sends email notifications for deadlines within 3 days (daily)
- **send_new_opportunity_notification** - Sends alert when new match found for student

## Setup

### Local Development

1. **Clone and checkout branch:**
   ```bash
   git pull origin develop
   git checkout -b feature/integration-devops develop
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your local settings
   ```

4. **Initialize database:**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **Run development server:**
   ```bash
   python manage.py runserver
   ```

6. **Start Celery worker (separate terminal):**
   ```bash
   celery -A skillora worker -l info
   ```

7. **Start Celery Beat scheduler (separate terminal):**
   ```bash
   celery -A skillora beat -l info
   ```

### Docker Deployment

```bash
docker-compose up
```

This starts:
- Django web application on port 8000
- PostgreSQL database on port 5432
- Redis cache/broker on port 6379
- Celery worker
- Celery Beat scheduler

## Project Structure

```
skillora/
├── skillora/
│   ├── settings/
│   │   ├── base.py          # Shared settings
│   │   ├── dev.py           # Development overrides
│   │   └── prod.py          # Production overrides
│   ├── celery.py            # Celery app configuration
│   ├── urls.py              # Main URL router
│   └── wsgi.py              # WSGI application
├── opportunity_app/
│   ├── models.py            # Student, Internship, Scholarship, Application, MatchResult
│   ├── serializers.py       # DRF serializers for all models
│   ├── views.py             # API endpoint implementations
│   ├── services.py          # Matching algorithm
│   ├── tasks.py             # Celery tasks
│   ├── urls.py              # API URL routing
│   └── migrations/          # Database migrations
├── Dockerfile               # Docker image definition
├── docker-compose.yml       # Multi-container orchestration
├── requirements.txt         # Python dependencies
├── .env.example             # Environment variable template
└── .gitignore               # Git ignore rules
```

## Configuration Files

### .env (Environment Variables)
```
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

DB_ENGINE=django.db.backends.sqlite3|postgresql
DB_NAME=db.sqlite3|skillora
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

### Settings Hierarchy
- `skillora/settings.py` → imports `dev.py`
- `dev.py` → imports from `base.py` + development overrides
- `prod.py` → imports from `base.py` + production overrides

To use production settings:
```bash
export DJANGO_SETTINGS_MODULE=skillora.settings.prod
python manage.py runserver
```

## API Examples

### Get Internships
```bash
curl http://localhost:8000/api/internships/
```

### Create Internship
```bash
curl -X POST http://localhost:8000/api/internships/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Frontend Engineer Intern",
    "company": "Acme Corp",
    "description": "Build React components",
    "location": "San Francisco, CA",
    "deadline": "2026-12-31",
    "skills_required": "React,JavaScript,CSS"
  }'
```

### Get Student Matches
```bash
curl http://localhost:8000/api/match/1/
```

## Testing

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test opportunity_app

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

## CI/CD

GitHub Actions workflow (`.github/workflows/ci.yml`) runs on every PR to `develop` and `main`:
- Install dependencies
- Run Django system checks
- Execute test suite
- Generate coverage report

## Integration Checklist

- [ ] Test all API endpoints with Postman/curl
- [ ] Verify database migrations apply cleanly
- [ ] Test matching algorithm with sample data
- [ ] Verify Celery tasks execute on schedule
- [ ] Test email notifications (console backend for dev)
- [ ] Docker image builds and starts successfully
- [ ] Environment variable defaults work without .env file
- [ ] Database backups configured (production)
- [ ] Error logging configured
- [ ] Performance tested with load

## Deployment

### Production Deployment Steps

1. **Set environment variables** for production database, email, secrets, etc.
2. **Run migrations:** `python manage.py migrate`
3. **Collect static files:** `python manage.py collectstatic --noinput`
4. **Start Gunicorn:** `gunicorn skillora.wsgi:application --bind 0.0.0.0:8000`
5. **Start Celery worker:** `celery -A skillora worker -l info`
6. **Start Celery Beat:** `celery -A skillora beat -l info`

Or use Docker:
```bash
docker-compose -f docker-compose.prod.yml up
```

## Troubleshooting

### Migrations not applying
```bash
python manage.py showmigrations
python manage.py showmigrations opportunity_app
python manage.py migrate opportunity_app 0001
```

### Celery not picking up tasks
```bash
# Verify Redis connection
redis-cli ping

# Check Celery worker logs
celery -A skillora worker -l debug
```

### Database connection errors
- Verify `DATABASES` settings in `.env`
- Check PostgreSQL service is running
- Confirm credentials are correct

## Security Notes

⚠️ **Never commit `.env` file** - it contains secrets!

Production checklist:
- [ ] `DEBUG = False`
- [ ] Strong `SECRET_KEY` (use Django's `get_random_secret_key()`)
- [ ] `ALLOWED_HOSTS` configured correctly
- [ ] Database password in environment variable, not hardcoded
- [ ] HTTPS/SSL enabled
- [ ] CSRF protection enabled
- [ ] CORS headers configured if needed
- [ ] Rate limiting implemented
- [ ] Logging and monitoring set up

## Next Steps / Future Work

1. **Authentication:** Implement JWT tokens for user authentication
2. **Advanced Matching:** ML-based scoring using student behavior patterns
3. **Notifications:** Push notifications, SMS alerts
4. **Admin Dashboard:** Monitoring, reporting, user management
5. **API Rate Limiting:** Prevent abuse with throttling
6. **Webhooks:** Real-time opportunity notifications
7. **Analytics:** Track match success rates, application outcomes

## Dependencies

- Django 5.1+
- Django REST Framework 3.15+
- Celery 5.4+
- Redis 5.0+ (broker and result backend)
- PostgreSQL 16+ (production database)
- python-dotenv 1.0+ (environment management)

## Branch Strategy

This branch is part of the feature branch workflow:
- Merge into `develop` after testing
- Merge `develop` into `main` for releases
- Use GitHub PRs for code review and CI

## Contributing

When merging other branches:
1. Pull latest from `develop`
2. Merge feature branch: `git merge feature/branch-name`
3. Resolve any conflicts
4. Run full test suite locally
5. Verify with: `python manage.py check`
6. Create Pull Request with detailed description
7. Ensure CI passes before merging

## License

OpportunityAI - Educational Project
