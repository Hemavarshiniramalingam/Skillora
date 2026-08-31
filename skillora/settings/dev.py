from .base import *

DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]
EMAIL_BACKEND = os.getenv("EMAIL_BACKEND", "django.core.mail.backends.console.EmailBackend")

CELERY_BEAT_SCHEDULE = {
    "deadline-reminders": {
        "task": "opportunity_app.tasks.send_deadline_reminders",
        "schedule": 60 * 60 * 24,
    },
}
