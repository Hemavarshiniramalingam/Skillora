from __future__ import annotations

from datetime import date, timedelta

from celery import shared_task
from django.core.mail import send_mail

from .models import Internship, Scholarship


@shared_task
def send_deadline_reminders():
    upcoming = date.today() + timedelta(days=3)
    internship_deadlines = Internship.objects.filter(deadline__lte=upcoming)
    scholarship_deadlines = Scholarship.objects.filter(deadline__lte=upcoming)

    for internship in internship_deadlines:
        send_mail(
            subject=f"Internship deadline approaching: {internship.title}",
            message=f"This internship opportunity is nearing its deadline: {internship.title} on {internship.deadline}.",
            from_email=None,
            recipient_list=["ops@skillora.local"],
            fail_silently=True,
        )

    for scholarship in scholarship_deadlines:
        send_mail(
            subject=f"Scholarship deadline approaching: {scholarship.title}",
            message=f"This scholarship is nearing its deadline: {scholarship.title} on {scholarship.deadline}.",
            from_email=None,
            recipient_list=["ops@skillora.local"],
            fail_silently=True,
        )

    return {
        "internship_count": internship_deadlines.count(),
        "scholarship_count": scholarship_deadlines.count(),
    }


@shared_task
def send_new_opportunity_notification(student_email: str, opportunity_title: str, opportunity_type: str):
    send_mail(
        subject=f"New {opportunity_type.title()} match: {opportunity_title}",
        message=f"We found a new {opportunity_type} that matches your profile: {opportunity_title}.",
        from_email=None,
        recipient_list=[student_email],
        fail_silently=True,
    )
    return {"sent_to": student_email, "opportunity": opportunity_title}
