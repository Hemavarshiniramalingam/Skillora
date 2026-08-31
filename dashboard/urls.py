from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('internships/', views.internships, name='internships'),
    path('internships/<slug:slug>/', views.internship_detail, name='internship_detail'),
    path('scholarships/', views.scholarships, name='scholarships'),
    path('scholarships/<slug:slug>/', views.scholarship_detail, name='scholarship_detail'),
    path('profile/', views.profile, name='profile'),
    path('tracker/', views.tracker, name='tracker'),
]
