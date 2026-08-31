from django.contrib import admin

from .models import StudentProfile


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'university', 'major', 'graduation_year', 'gpa')
    list_filter = ('university', 'major', 'graduation_year')
    search_fields = ('user__username', 'user__email', 'university', 'major')
    ordering = ('user__username',)
