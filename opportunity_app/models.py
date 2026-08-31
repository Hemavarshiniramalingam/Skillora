from django.db import models


class Student(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    major = models.CharField(max_length=255, blank=True)
    gpa = models.FloatField(default=0.0)
    preferred_fields = models.TextField(blank=True)

    def __str__(self):
        return self.full_name


class Internship(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    deadline = models.DateField()
    skills_required = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Scholarship(models.Model):
    title = models.CharField(max_length=255)
    provider = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    deadline = models.DateField()
    eligibility = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="applications")
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE, related_name="applications", null=True, blank=True)
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE, related_name="applications", null=True, blank=True)
    status = models.CharField(max_length=50, default="applied")
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} -> {self.internship or self.scholarship}"


class MatchResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="match_results")
    opportunity_type = models.CharField(max_length=20, choices=[("internship", "Internship"), ("scholarship", "Scholarship")])
    opportunity_id = models.IntegerField()
    score = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-score", "-created_at"]

    def __str__(self):
        return f"{self.student} matched {self.opportunity_type} {self.opportunity_id} ({self.score})"
