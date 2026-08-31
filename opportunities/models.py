from django.conf import settings
from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=200, blank=True)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Internship(models.Model):
    INTERNSHIP_TYPES = [
        ('Remote', 'Remote'),
        ('Hybrid', 'Hybrid'),
        ('On-site', 'On-site'),
    ]

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='internships')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    internship_type = models.CharField(max_length=20, choices=INTERNSHIP_TYPES, default='Remote')
    pay = models.CharField(max_length=100, blank=True)
    deadline = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Scholarship(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='scholarships')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    amount = models.CharField(max_length=100, blank=True)
    deadline = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Application(models.Model):
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('under_review', 'Under review'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications', null=True, blank=True)
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE, related_name='applications', null=True, blank=True)
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE, related_name='applications', null=True, blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='submitted')
    notes = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return self.status
