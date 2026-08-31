from .base import *

DEBUG = False
ALLOWED_HOSTS = [host.strip() for host in os.getenv("DJANGO_ALLOWED_HOSTS", "example.com").split(",") if host.strip()]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME", "skillora"),
        "USER": os.getenv("DB_USER", "skillora"),
        "PASSWORD": os.getenv("DB_PASSWORD", "skillora"),
        "HOST": os.getenv("DB_HOST", "db"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}

EMAIL_BACKEND = os.getenv("EMAIL_BACKEND", "django.core.mail.backends.smtp.EmailBackend")

CSRF_TRUSTED_ORIGINS = [
    origin.strip() for origin in os.getenv("CSRF_TRUSTED_ORIGINS", "https://example.com").split(",") if origin.strip()
]

CELERY_BEAT_SCHEDULE = {
    "deadline-reminders": {
        "task": "opportunity_app.tasks.send_deadline_reminders",
        "schedule": 60 * 60 * 24,
    },
}
