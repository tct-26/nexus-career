from django.contrib import admin

from .models import Company, CompanyAlumniEmployment, RecruiterProfile, WorkflowAuditEvent


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "industry", "verification_status", "created_at")
    list_filter = ("verification_status", "industry")
    search_fields = ("name", "contact_email")


@admin.register(RecruiterProfile)
class RecruiterProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "company", "designation", "created_at")
    search_fields = ("user__username", "company__name")


@admin.register(WorkflowAuditEvent)
class WorkflowAuditEventAdmin(admin.ModelAdmin):
    list_display = ("action", "object_type", "object_id", "actor", "created_at")
    list_filter = ("action", "object_type", "created_at")
    search_fields = ("actor__username", "object_id")
    readonly_fields = (
        "actor",
        "object_type",
        "object_id",
        "action",
        "details",
        "created_at",
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(CompanyAlumniEmployment)
class CompanyAlumniEmploymentAdmin(admin.ModelAdmin):
    list_display = (
        "alumni", "company", "designation", "employment_status",
        "verification_status", "verified_at",
    )
    list_filter = ("employment_status", "verification_status", "company")
    search_fields = ("alumni__user__username", "alumni__user__email", "company__name")
    readonly_fields = ("verified_by", "verified_at", "created_at", "updated_at")
