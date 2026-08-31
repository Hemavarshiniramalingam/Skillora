from django.contrib import admin

from .models import Application, Internship, Organization, Scholarship


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'industry', 'website')
    search_fields = ('name', 'industry')
    list_filter = ('industry',)


@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'location', 'internship_type', 'is_active', 'deadline')
    list_filter = ('internship_type', 'is_active', 'organization')
    search_fields = ('title', 'organization__name', 'location')


@admin.register(Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'amount', 'deadline', 'is_active')
    list_filter = ('is_active', 'organization')
    search_fields = ('title', 'organization__name', 'amount')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'internship', 'scholarship', 'status', 'submitted_at')
    list_filter = ('status', 'submitted_at')
    search_fields = ('user__username', 'internship__title', 'scholarship__title')
