from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied

from apps.accounts.models import User
from .models import Company, CompanyAlumniEmployment
from .alumni_serializers import CompanyAlumniEmploymentSerializer


class CompanyVerifiedAlumniListView(generics.ListAPIView):
    """List current, verified alumni for a verified company; students only."""

    serializer_class = CompanyAlumniEmploymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role != User.Role.STUDENT:
            raise PermissionDenied("Only students can view company alumni.")

        company = get_object_or_404(
            Company,
            pk=self.kwargs["company_id"],
            verification_status=Company.VerificationStatus.VERIFIED,
        )
        return (
            CompanyAlumniEmployment.objects.filter(
                company=company,
                employment_status=CompanyAlumniEmployment.EmploymentStatus.CURRENT,
                verification_status=CompanyAlumniEmployment.VerificationStatus.VERIFIED,
                alumni__verification_status=(
                    "VERIFIED"
                ),
            )
            .select_related("alumni", "alumni__user", "company")
            .order_by("alumni__user__last_name", "alumni__user__first_name", "id")
        )
