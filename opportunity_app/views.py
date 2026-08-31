from __future__ import annotations

from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Application, Internship, MatchResult, Scholarship, Student
from .serializers import ApplicationSerializer, InternshipSerializer, MatchResultSerializer, ScholarshipSerializer
from .services import calculate_student_match_scores


@api_view(["GET", "POST"])
def internship_list_create(request):
    if request.method == "GET":
        internships = Internship.objects.all()
        serializer = InternshipSerializer(internships, many=True)
        return Response(serializer.data)

    serializer = InternshipSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def scholarship_list_create(request):
    if request.method == "GET":
        scholarships = Scholarship.objects.all()
        serializer = ScholarshipSerializer(scholarships, many=True)
        return Response(serializer.data)

    serializer = ScholarshipSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def application_list_create(request):
    if request.method == "GET":
        applications = Application.objects.all()
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)

    serializer = ApplicationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def match_for_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    opportunities = calculate_student_match_scores(student)

    with transaction.atomic():
        MatchResult.objects.filter(student=student).delete()
        for item in opportunities:
            MatchResult.objects.create(
                student=student,
                opportunity_type=item["type"],
                opportunity_id=item["id"],
                score=item["score"],
            )

    results = MatchResult.objects.filter(student=student)
    serializer = MatchResultSerializer(results, many=True)
    return Response({"student_id": student.id, "results": serializer.data})


@api_view(["GET"])
def healthcheck(request):
    return Response({"status": "ok"})
