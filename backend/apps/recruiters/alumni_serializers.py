from rest_framework import serializers

from apps.alumni.models import AlumniProfile
from .models import Company, CompanyAlumniEmployment


class CompanyAlumniEmploymentSerializer(serializers.ModelSerializer):
    alumni_profile_id = serializers.IntegerField(source="alumni_id", read_only=True)
    full_name = serializers.SerializerMethodField()
    department = serializers.CharField(source="alumni.department", read_only=True)
    degree_programme = serializers.CharField(source="alumni.degree_programme", read_only=True)
    graduation_year = serializers.IntegerField(source="alumni.graduation_year", read_only=True)
    is_open_to_referrals = serializers.BooleanField(
        source="alumni.is_open_to_referrals", read_only=True
    )

    class Meta:
        model = CompanyAlumniEmployment
        fields = [
            "id", "alumni_profile_id", "full_name", "designation",
            "department", "degree_programme", "graduation_year",
            "is_open_to_referrals", "start_date",
        ]
        read_only_fields = fields

    def get_full_name(self, obj):
        return obj.alumni.user.get_full_name() or obj.alumni.user.username


class OpportunityCompanyAlumniSerializer(serializers.ModelSerializer):
    alumni_profile_id = serializers.IntegerField(source="alumni_id", read_only=True)
    full_name = serializers.SerializerMethodField()
    designation = serializers.CharField(read_only=True)
    graduation_year = serializers.IntegerField(source="alumni.graduation_year", read_only=True)

    class Meta:
        model = CompanyAlumniEmployment
        fields = ["alumni_profile_id", "full_name", "designation", "graduation_year"]
        read_only_fields = fields

    def get_full_name(self, obj):
        return obj.alumni.user.get_full_name() or obj.alumni.user.username


class CompanyAlumniCompanySerializer(serializers.ModelSerializer):
    verified_alumni_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Company
        fields = ["id", "name", "industry", "website", "verified_alumni_count"]
        read_only_fields = fields
