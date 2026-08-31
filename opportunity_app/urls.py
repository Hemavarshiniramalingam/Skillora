from django.urls import path

from .views import application_list_create, healthcheck, internship_list_create, match_for_student, scholarship_list_create

urlpatterns = [
    path("health/", healthcheck, name="healthcheck"),
    path("internships/", internship_list_create, name="internship-list-create"),
    path("scholarships/", scholarship_list_create, name="scholarship-list-create"),
    path("applications/", application_list_create, name="application-list-create"),
    path("match/<int:student_id>/", match_for_student, name="match-for-student"),
]
