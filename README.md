# OpportunityAI

**AI-powered student internship & scholarship matching platform**

## Phase 4: API, Notifications & Integration/DevOps ⚡

This branch implements the complete REST API layer, Celery-based notifications, and Docker deployment infrastructure.

### Key Features Implemented

✅ **REST API** - Django REST Framework endpoints for all core models
✅ **Matching Engine** - Student to opportunity scoring algorithm  
✅ **Celery Tasks** - Automated deadline reminders and notifications
✅ **Docker** - Multi-container development and production environments
✅ **Environment Config** - Flexible settings for dev/prod/testing
✅ **CI/CD** - GitHub Actions for automated testing on PRs

### Quick Start

```bash
# Windows
setup.bat

# Linux/Mac
bash setup.sh
```

Or manually:

```bash
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

### API Documentation

See [API_INTEGRATION_GUIDE.md](API_INTEGRATION_GUIDE.md) for complete API documentation and examples.

### Project Structure

```
├── opportunity_app/        # Core Django app
│   ├── models.py          # Student, Internship, Scholarship, Application, MatchResult
│   ├── serializers.py     # DRF serializers
│   ├── views.py           # API endpoints
│   ├── services.py        # Matching algorithm
│   └── tasks.py           # Celery background jobs
├── skillora/              # Django project config
│   ├── settings/          # Settings package (base, dev, prod)
│   ├── celery.py         # Celery app setup
│   ├── urls.py           # URL routing
│   └── wsgi.py           # WSGI application
├── Dockerfile            # Docker image
├── docker-compose.yml    # Multi-container setup
├── requirements.txt      # Python dependencies
├── .env.example         # Environment template
└── validate_setup.py    # Setup validation script
```

### Technology Stack

- **Framework:** Django 5.1+
- **API:** Django REST Framework 3.15+
- **Task Queue:** Celery 5.4+
- **Broker/Cache:** Redis 5.0+
- **Database:** SQLite (dev), PostgreSQL (prod)
- **Deployment:** Docker & Docker Compose

### API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/internships/` | GET, POST | List/create internships |
| `/api/scholarships/` | GET, POST | List/create scholarships |
| `/api/applications/` | GET, POST | List/create applications |
| `/api/match/<student_id>/` | GET | Compute matches for student |
| `/api/health/` | GET | Health check |

### Testing & Validation

```bash
# Run validation script
python validate_setup.py

# Run tests
python manage.py test

# With coverage
coverage run --source='.' manage.py test
coverage report
```

### Environment Variables

See `.env.example` for all available options. Key variables:

- `DJANGO_SECRET_KEY` - Django secret key
- `DJANGO_DEBUG` - Enable debug mode
- `DB_*` - Database connection settings
- `CELERY_BROKER_URL` - Redis connection for Celery
- `EMAIL_BACKEND` - Email service backend

### Docker

```bash
# Start all services
docker-compose up

# Build image
docker-compose build

# Access services
Web:      http://localhost:8000
Database: postgres://localhost:5432
Redis:    redis://localhost:6379
```

### Development Workflow

1. Create feature branch: `git checkout -b feature/your-feature develop`
2. Make changes and test locally
3. Push to remote: `git push origin feature/your-feature`
4. Create PR to `develop` branch
5. Address review feedback
6. After approval and passing CI, merge to develop
7. Periodically merge `develop` into `main` for releases

### Integration & Merge Duties

As the integration owner, when merging other feature branches:

```bash
git checkout develop
git pull origin develop
git merge feature/their-branch  # or use GitHub UI
python manage.py check
python manage.py test
# Resolve any conflicts
git push origin develop
```

### Next Steps

- [ ] Test all API endpoints
- [ ] Integrate frontend with API
- [ ] Set up production database (PostgreSQL)
- [ ] Configure production email (SMTP)
- [ ] Deploy to production environment
- [ ] Set up monitoring/logging
- [ ] Add authentication/authorization
- [ ] Implement rate limiting
- [ ] Add API webhooks
- [ ] Set up analytics

### Documentation

- **API Guide:** [API_INTEGRATION_GUIDE.md](API_INTEGRATION_GUIDE.md)
- **Setup Validation:** Run `python validate_setup.py`
- **Django Admin:** `/admin/` (requires superuser)

### Support

For issues or questions:
1. Check the API guide and setup documentation
2. Run validation script: `python validate_setup.py`
3. Check logs: `cat django.log` (if configured)
4. Review Django/DRF documentation

### License

OpportunityAI - Educational Project
