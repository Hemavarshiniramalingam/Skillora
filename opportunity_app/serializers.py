from rest_framework import serializers

from .models import Application, Internship, MatchResult, Scholarship, Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "full_name", "email", "major", "gpa", "preferred_fields"]


class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        fields = ["id", "title", "company", "description", "location", "deadline", "skills_required"]


class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholarship
        fields = ["id", "title", "provider", "description", "amount", "deadline", "eligibility"]


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["id", "student", "internship", "scholarship", "status", "applied_at"]


class MatchResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchResult
        fields = ["id", "student", "opportunity_type", "opportunity_id", "score", "created_at"]
